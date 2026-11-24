#!/usr/bin/env python3
"""T85 scored check. Reads the locked bars in theory/ctc-fixed-point-2026-11-24/PREREG.md.

Toy two-qubit Deutsch fixed point. Not a claim about physical time travel.
"""
from __future__ import annotations

import numpy as np

TOL_ENT = 1e-9
TOL_GAP = 1e-8
TOL_SV = 1e-8
TOL_FIX = 1e-8
TOL_CYC = 1e-12

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
LN2 = float(np.log(2))


def kron(a, b):
    return np.kron(a, b)


def pt_first(rho):
    """Trace out the leading qubit of a 4x4 CR ⊗ CTC state. Returns CTC."""
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def pt_second(rho):
    """Trace out the trailing qubit. Returns CR."""
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def bloch(rho):
    return np.array([np.real(np.trace(rho @ p)) for p in (X, Y, Z)], dtype=float)


def from_bloch(r):
    return 0.5 * (I2 + r[0] * X + r[1] * Y + r[2] * Z)


def vn(rho):
    herm = 0.5 * (rho + rho.conj().T)
    ev = np.linalg.eigvalsh(herm).real
    ev = ev[ev > 1e-12]
    if ev.size == 0:
        return 0.0
    return float(-np.sum(ev * np.log(ev)))


def binary_h(p):
    p = float(p)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return float(-(p * np.log(p) + (1.0 - p) * np.log(1.0 - p)))


def trace_distance(a, b):
    diff = 0.5 * ((a - b) + (a - b).conj().T)
    ev = np.linalg.eigvalsh(diff).real
    return float(0.5 * np.sum(np.abs(ev)))


def evolve(U, rho_cr, rho_c):
    out = U @ kron(rho_cr, rho_c) @ U.conj().T
    return pt_first(out), pt_second(out)


def channel_affine(U, rho_cr):
    outs = []
    refs = [np.zeros(3), np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
    for v in refs:
        red_c, _ = evolve(U, rho_cr, from_bloch(v))
        outs.append(bloch(red_c))
    d = outs[0]
    M = np.column_stack([outs[i + 1] - d for i in range(3)])
    return M, d


def svd_sv(A):
    return np.linalg.svd(A, compute_uv=False)


def null_vectors(A, tol=TOL_SV):
    _u, s, vt = np.linalg.svd(A)
    mask = s < tol
    # vt rows are right singular vectors. Pad if A is fat, but A is 3x3.
    vecs = []
    for i, keep in enumerate(mask):
        if keep:
            vecs.append(vt[i].real.copy())
    # If a singular value was dropped because s is shorter, nothing more.
    return vecs, s


def min_norm_solution(A, b):
    r, *_ = np.linalg.lstsq(A, b, rcond=TOL_SV)
    return np.real(r)


def line_ends(r0, n):
    n = np.real(n)
    n = n / np.linalg.norm(n)
    b = 2.0 * float(np.dot(r0, n))
    c = float(np.dot(r0, r0) - 1.0)
    disc = b * b - 4.0 * c
    pts = [np.real(r0)]
    if disc >= -1e-10:
        root = np.sqrt(max(disc, 0.0))
        for t in ((-b + root) / 2.0, (-b - root) / 2.0):
            pts.append(np.real(r0 + t * n))
    return pts


def gate_I():
    return np.eye(4, dtype=complex)


def gate_SWAP():
    U = np.zeros((4, 4), dtype=complex)
    U[0, 0] = 1
    U[2, 1] = 1
    U[1, 2] = 1
    U[3, 3] = 1
    return U


def gate_CNOT_CR():
    U = np.eye(4, dtype=complex)
    U[2, 2] = 0
    U[3, 3] = 0
    U[2, 3] = 1
    U[3, 2] = 1
    return U


def gate_CNOT_C():
    U = np.eye(4, dtype=complex)
    U[1, 1] = 0
    U[3, 3] = 0
    U[3, 1] = 1
    U[1, 3] = 1
    return U


def gate_CZ():
    U = np.eye(4, dtype=complex)
    U[3, 3] = -1
    return U


def gate_DCNOT():
    return gate_CNOT_C() @ gate_CNOT_CR()


def gate_DISC():
    s2 = 1.0 / np.sqrt(2.0)
    U = np.zeros((4, 4), dtype=complex)
    U[:, 0] = [1, 0, 0, 0]
    U[:, 1] = [0, s2, 0, s2]
    U[:, 2] = [0, 0, 1, 0]
    U[:, 3] = [0, -s2, 0, s2]
    return U


def gate_heis(a, b, c):
    H = (a * kron(X, X) + b * kron(Y, Y) + c * kron(Z, Z)) / 2.0
    w, v = np.linalg.eigh(H)
    return (v * np.exp(-1j * w)) @ v.conj().T


RHO0 = np.array([[1, 0], [0, 0]], dtype=complex)
RHO1 = np.array([[0, 0], [0, 1]], dtype=complex)
RHOP = 0.5 * np.array([[1, 1], [1, 1]], dtype=complex)
RHOI = I2 / 2


def deltas(U, rho_cr, r):
    rho_c = from_bloch(r)
    red_c, red_cr = evolve(U, rho_cr, rho_c)
    dist = trace_distance(red_c, rho_c)
    return dist, vn(red_c) - vn(rho_c), vn(red_cr) - vn(rho_cr)


def sample_points(M, dvec):
    A = M - np.eye(3)
    r0 = min_norm_solution(A, -dvec)
    vecs, s = null_vectors(A)
    nullity = len(vecs)
    pts = [r0]
    if nullity == 1:
        pts = line_ends(r0, vecs[0])
    elif nullity >= 3:
        pts = [np.zeros(3)]
        for i in range(3):
            e = np.zeros(3)
            e[i] = 1.0
            pts.append(e)
            pts.append(-e)
    elif nullity == 2:
        pts = [r0]
        for v in vecs:
            pts.extend(line_ends(r0, v))
    return pts, nullity, float(np.min(s))


def main():
    fails = []

    def check(name, ok, detail):
        status = "PASS" if ok else "FAIL"
        print("%s %s %s" % (name, status, detail))
        if not ok:
            fails.append(name)

    print("T85 ctc fixed point")
    print("definition DEUTSCH-FIXED-POINT")
    print("model toy-deutsch-prescription")

    named = {
        "I": gate_I(),
        "SWAP": gate_SWAP(),
        "CNOT_CR": gate_CNOT_CR(),
        "CNOT_C": gate_CNOT_C(),
        "CZ": gate_CZ(),
        "DCNOT": gate_DCNOT(),
        "DISC": gate_DISC(),
    }
    expect_nonunique = {"I", "CNOT_CR", "CNOT_C", "CZ", "DISC"}
    expect_unique = {"SWAP", "DCNOT"}

    # --- named uniqueness at I/2 ---
    named_ok = True
    named_bits = []
    for name, U in named.items():
        M, dvec = channel_affine(U, RHOI)
        _pts, nullity, svmin = sample_points(M, dvec)
        nonunique = svmin < TOL_SV
        want = name in expect_nonunique
        bit_ok = (nonunique == want) and (name in expect_unique or name in expect_nonunique)
        if not bit_ok:
            named_ok = False
        named_bits.append("%s:%s" % (name, "nonunique" if nonunique else "unique"))
    check("P1b-named", named_ok, " ".join(named_bits))

    # --- DISC Bloch matrix ---
    M0, d0 = channel_affine(named["DISC"], RHO0)
    Mp, dp = channel_affine(named["DISC"], RHOP)
    target = np.diag([1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0), 1.0])
    errM = max(np.max(np.abs(M0 - target)), np.max(np.abs(Mp - target)), np.max(np.abs(d0)), np.max(np.abs(dp)))
    check("P-disc-matrix", errM <= TOL_ENT, "max_abs=%.3e" % errM)

    # --- Heisenberg grid ---
    grid_vals = [0.0, np.pi / 4, np.pi / 2, np.pi]
    n_non = 0
    sv_unique = []
    sv_non = []
    grid = []
    for a in grid_vals:
        for b in grid_vals:
            for c in grid_vals:
                U = gate_heis(a, b, c)
                M, dvec = channel_affine(U, RHOI)
                svmin = float(np.min(svd_sv(M - np.eye(3))))
                nonunique = svmin < TOL_SV
                if nonunique:
                    n_non += 1
                    sv_non.append(svmin)
                else:
                    sv_unique.append(svmin)
                grid.append((U, M, dvec, nonunique))
    grid_ok = n_non == 20 and max(sv_non) < TOL_SV and min(sv_unique) > 0.2
    check(
        "P1b-grid",
        grid_ok,
        "nonunique=%d/64 unique_sv_min=%.6f nonunique_sv_max=%.3e" % (n_non, min(sv_unique), max(sv_non)),
    )

    # --- accepted fixed points ---
    accepted = []
    rejected = 0

    def consider(U, rho_cr, r, tag):
        nonlocal rejected
        if np.linalg.norm(r) > 1.0 + 1e-7:
            r = r / np.linalg.norm(r)
        dist, d_c, d_cr = deltas(U, rho_cr, r)
        if dist > TOL_FIX:
            rejected += 1
            print("reject %s dist=%.3e" % (tag, dist))
            return
        accepted.append((d_c, d_cr, tag))

    for U, M, dvec, _non in grid:
        pts, nullity, _sv = sample_points(M, dvec)
        for r in pts:
            consider(U, RHOI, r, "grid-n%d" % nullity)
    for name in ("SWAP", "I", "CNOT_CR", "CNOT_C", "CZ", "DCNOT", "DISC"):
        M, dvec = channel_affine(named[name], RHOI)
        pts, nullity, _sv = sample_points(M, dvec)
        for r in pts:
            consider(named[name], RHOI, r, "named-%s" % name)

    for rho in (RHO0, RHO1, RHOP, RHOI):
        M, dvec = channel_affine(named["SWAP"], rho)
        pts, _n, _s = sample_points(M, dvec)
        for r in pts:
            consider(named["SWAP"], rho, r, "swap")

    for rho in (RHO0, RHOP):
        for z in (1.0, 0.0, -1.0):
            consider(named["DISC"], rho, np.array([0.0, 0.0, z]), "disc-z")
    for rho in (RHO0, RHO1):
        for z in (1.0, 0.0, -1.0):
            consider(named["CNOT_C"], rho, np.array([0.0, 0.0, z]), "cnotc-z")

    abs_c = max(abs(d_c) for d_c, _d_cr, _t in accepted)
    min_cr = min(d_cr for _d_c, d_cr, _t in accepted)
    check("P1a", abs_c <= TOL_ENT and rejected == 0, "max_abs_dS_C=%.3e n=%d rejections=%d" % (abs_c, len(accepted), rejected))
    check("P2-bound", min_cr >= -TOL_ENT and rejected == 0, "min_dS_CR=%.3e" % min_cr)
    print("P2-candidate UNSUPPORTED honest_min_dS_CR=%.6e" % min_cr)

    # --- illicit ensemble, not one density operator ---
    _c0, out0 = evolve(named["CNOT_C"], RHO0, RHO0)
    _c1, out1 = evolve(named["CNOT_C"], RHO1, RHO1)
    mixed_out = 0.5 * (out0 + out1)
    mixed_in = 0.5 * (RHO0 + RHO1)
    illicit = vn(mixed_out) - vn(mixed_in)
    _mc0, cr0 = evolve(named["CNOT_C"], RHO0, RHOI)
    _mc1, cr1 = evolve(named["CNOT_C"], RHO1, RHOI)
    sel0 = vn(cr0) - vn(RHO0)
    sel1 = vn(cr1) - vn(RHO1)
    ill_ok = abs(illicit - (-LN2)) <= TOL_ENT and abs(sel0 - LN2) <= TOL_ENT and abs(sel1 - LN2) <= TOL_ENT
    check(
        "P2-illicit",
        ill_ok,
        "delta=%.12f selector_dS=%.12f not-a-process" % (illicit, 0.5 * (sel0 + sel1)),
    )

    # --- depolarizing gap on DISC ---
    target_gap = binary_h((2.0 + np.sqrt(2.0)) / 4.0)
    target_I = LN2 - binary_h(0.75)
    gap_ok = True
    gap_print = []
    for gamma in (1e-6, 0.01, 0.1, 0.5, 1.0):
        # r = (1-gamma)(M r + d) on each input. d=0 and M known; solve.
        outs = []
        uniq = True
        for rho in (RHO0, RHOP):
            M, dvec = channel_affine(named["DISC"], rho)
            A = np.eye(3) - (1.0 - gamma) * M
            svmin = float(np.min(svd_sv(A)))
            if svmin < TOL_SV:
                uniq = False
            r = min_norm_solution(A, (1.0 - gamma) * dvec)
            red_c, red_cr = evolve(named["DISC"], rho, from_bloch(r))
            outs.append(red_cr)
            if trace_distance(red_c, from_bloch(r)) > TOL_FIX:
                uniq = False
            if np.linalg.norm(r) > TOL_ENT:
                uniq = False
        p0 = float(np.real(outs[0][0, 0]))
        p1 = float(np.real(outs[1][0, 0]))
        pbar = 0.5 * (p0 + p1)
        info = binary_h(pbar) - 0.5 * (binary_h(p0) + binary_h(p1))
        pd = 0.5 * (vn(outs[0]) + vn(outs[1]))
        this = uniq and abs(pd - target_gap) <= TOL_GAP and abs(info - target_I) <= TOL_GAP and pd > 0.1
        if not this:
            gap_ok = False
        gap_print.append("g=%.6f I=%.12f PD=%.12f" % (gamma, info, pd))
    check("P3-gap", gap_ok, "qgap_target=%.12f I_target=%.12f %s" % (target_gap, target_I, " ".join(gap_print)))
    print("P3-candidate UNSUPPORTED qgap_stays=%.12f" % target_gap)

    # --- phase damping keeps the pure selector ---
    def z_dephase(gamma, rho):
        return (1.0 - gamma) * rho + gamma * (Z @ rho @ Z)

    def noisy_image(U, rho_cr, rho_c, gamma, kind):
        red_c, red_cr = evolve(U, rho_cr, rho_c)
        if kind == "phase":
            red_c = z_dephase(gamma, red_c)
        return red_c, red_cr

    pure_pairs = [(RHO0, RHO0), (RHOP, RHO1)]
    phase_ok = True
    dists = []
    cr_outs = []
    for rho_cr, rho_c in pure_pairs:
        red_c, red_cr = noisy_image(named["DISC"], rho_cr, rho_c, 0.5, "phase")
        dist = trace_distance(red_c, rho_c)
        dists.append(dist)
        cr_outs.append(red_cr)
        if dist > TOL_ENT:
            phase_ok = False
    # Both outputs are pure and orthogonal, so P_D = 0 and the ratio gap is 0.
    pd_phase = 0.5 * (vn(cr_outs[0]) + vn(cr_outs[1]))
    if abs(pd_phase) > TOL_ENT:
        phase_ok = False
    check("P3-phase", phase_ok, "qgap=%.3e dist0=%.3e dist1=%.3e" % (pd_phase, dists[0], dists[1]))

    # --- contraction nullity ---
    M, _d = channel_affine(named["DISC"], RHO0)
    n0 = len(null_vectors(M - np.eye(3))[0])
    n_eps = len(null_vectors(np.eye(3) - (1.0 - 1e-6) * M)[0])
    check("P3-contraction", n0 >= 1 and n_eps == 0, "nullity0=%d nullity_eps=%d" % (n0, n_eps))

    # --- closed observer + bath loop ---
    # Basis |w, m, b>, index ((w*2+m)*2+b).
    def basis(w, m, b):
        v = np.zeros(8, dtype=complex)
        v[((w * 2 + m) * 2 + b)] = 1.0
        return v

    def projector_state():
        # fair W, M=|0>, B=|0>, product
        s0 = basis(0, 0, 0)
        s1 = basis(1, 0, 0)
        rho = 0.5 * (np.outer(s0, s0.conj()) + np.outer(s1, s1.conj()))
        return rho

    def apply_map(rho, images):
        """images: list of 8 basis images (as vectors) for inputs 0..7."""
        U = np.column_stack(images)
        return U @ rho @ U.conj().T

    def cnot_wm_images():
        imgs = []
        for w in (0, 1):
            for m in (0, 1):
                for b in (0, 1):
                    imgs.append(basis(w, m ^ w, b))
        return imgs

    def swap_mb_images():
        imgs = []
        for w in (0, 1):
            for m in (0, 1):
                for b in (0, 1):
                    imgs.append(basis(w, b, m))
        return imgs

    Z8_B = np.zeros((8, 8), dtype=complex)
    for w in (0, 1):
        for m in (0, 1):
            for b, sign in ((0, 1.0), (1, -1.0)):
                i = (w * 2 + m) * 2 + b
                Z8_B[i, i] = 0.5 * sign

    def energy_b(rho):
        return float(np.real(np.trace(rho @ Z8_B)))

    def reduce_wm(rho):
        """Trace out B. Axes are (w, m, b, w', m', b')."""
        t = rho.reshape(2, 2, 2, 2, 2, 2)
        return np.trace(t, axis1=2, axis2=5).reshape(4, 4)

    def reduce_w(rho):
        wm = reduce_wm(rho).reshape(2, 2, 2, 2)
        return np.trace(wm, axis1=1, axis2=3)

    def reduce_m(rho):
        wm = reduce_wm(rho).reshape(2, 2, 2, 2)
        return np.trace(wm, axis1=0, axis2=2)

    def mutual_wm(rho):
        return vn(reduce_w(rho)) + vn(reduce_m(rho)) - vn(reduce_wm(rho))

    rho = projector_state()
    e0 = energy_b(rho)
    i0 = mutual_wm(rho)
    sum_q = 0.0
    half_sum = None
    steps = (
        ("cnot", cnot_wm_images()),
        ("swap", swap_mb_images()),
        ("swap", swap_mb_images()),
        ("cnot", cnot_wm_images()),
    )
    for k, (_name, imgs) in enumerate(steps):
        rho = apply_map(rho, imgs)
        e1 = energy_b(rho)
        sum_q += (e1 - e0) / 1.0
        e0 = e1
        if k == 1:
            half_sum = sum_q
    i1 = mutual_wm(rho)
    dist = trace_distance(rho, projector_state())
    net_i = i1 - i0
    check(
        "P4-cycle",
        abs(sum_q) <= TOL_CYC and abs(net_i) <= TOL_CYC and dist <= TOL_CYC,
        "sum=%.3e netI=%.3e dist=%.3e" % (sum_q, net_i, dist),
    )
    check("P4-half", half_sum is not None and abs(half_sum - (-0.5)) <= TOL_CYC, "sum=%.12f" % half_sum)

    print("rejections=%d" % rejected)
    print("FAILS %d" % len(fails))
    if fails:
        print("failed " + ",".join(fails))


if __name__ == "__main__":
    main()
