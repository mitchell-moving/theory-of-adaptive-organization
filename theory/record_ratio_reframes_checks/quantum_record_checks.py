#!/usr/bin/env python3
"""T76 quantum-record checks. Criteria are PREREG_QUANTUM.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math

SEED = 20261124  # not drawn from
R = 0.6
ETA = 0.5
N_GRID = 720
TIE = 1e-9
W_STAKE = 1.0
PI = math.pi
HALF_PI = 0.5 * PI
ANT = (
    (0.25, (0.0, 0.0, R)),
    (0.25, (0.0, 0.0, -R)),
    (0.25, (R, 0.0, 0.0)),
    (0.25, (-R, 0.0, 0.0)),
)


def hbin(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    q = 1.0 - p
    return -p * math.log(p) - q * math.log(q)


def qubit_entropy(bloch_len: float) -> float:
    b = min(1.0, max(0.0, bloch_len))
    return hbin(0.5 * (1.0 + b))


def dot(a, b) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def norm(a) -> float:
    return math.sqrt(dot(a, a))


def n_theta(theta: float):
    return (math.sin(theta), 0.0, math.cos(theta))


def gamma_factor() -> float:
    return math.sqrt(1.0 - ETA * ETA)


def channel_bloch(r, n):
    """Unconditional Lüders map: keep r along n, multiply the perpendicular part by gamma."""
    g = gamma_factor()
    proj = dot(r, n)
    return (
        proj * n[0] + g * (r[0] - proj * n[0]),
        proj * n[1] + g * (r[1] - proj * n[1]),
        proj * n[2] + g * (r[2] - proj * n[2]),
    )


def p_plus(r, n) -> float:
    return 0.5 * (1.0 + ETA * dot(r, n))


def row_functionals(n):
    weights = []
    posts = []
    lengths = []
    pps = []
    ys = []
    p_d = 0.0
    h_mw = 0.0
    pbar = 0.0
    for w, pre in ANT:
        post = channel_bloch(pre, n)
        length = norm(pre)
        pp = p_plus(pre, n)
        weights.append(w)
        posts.append(post)
        lengths.append(length)
        pps.append(pp)
        ys.append(pre[2])
        p_d += w * (qubit_entropy(norm(post)) - qubit_entropy(length))
        h_mw += w * hbin(pp)
        pbar += w * pp
    info = hbin(pbar) - h_mw
    p_m = (pbar, 1.0 - pbar)
    a_hat = [0.0, 0.0]
    for sign, pm in enumerate(p_m):
        if pm <= 0.0:
            continue
        acc = 0.0
        for w, pp, y in zip(weights, pps, ys):
            pm_w = pp if sign == 0 else (1.0 - pp)
            acc += w * pm_w * y
        a_hat[sign] = acc / pm
    loss = 0.0
    for w, pp, y in zip(weights, pps, ys):
        for sign, pm_w in enumerate((pp, 1.0 - pp)):
            d = y - a_hat[sign]
            loss += w * pm_w * d * d
    return info, p_d, loss


def grid():
    step = HALF_PI / N_GRID
    return [j * step for j in range(N_GRID + 1)]


def j_star(q: float):
    best = None
    for th in grid():
        info, p_d, loss = row_functionals(n_theta(th))
        j = info + q * p_d + W_STAKE * loss
        if best is None or j < best:
            best = j
    return best


# --- 2x2 complex matrices, entries (re, im) ---

C = tuple  # (re, im)


def cadd(a: C, b: C) -> C:
    return (a[0] + b[0], a[1] + b[1])


def csub(a: C, b: C) -> C:
    return (a[0] - b[0], a[1] - b[1])


def cmul(a: C, b: C) -> C:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cscale(s: float, a: C) -> C:
    return (s * a[0], s * a[1])


def cconj(a: C) -> C:
    return (a[0], -a[1])


Mat = tuple  # 2x2 of C


def mzero() -> Mat:
    z = (0.0, 0.0)
    return ((z, z), (z, z))


def madd(a: Mat, b: Mat) -> Mat:
    return tuple(tuple(cadd(a[i][j], b[i][j]) for j in range(2)) for i in range(2))


def mmul(a: Mat, b: Mat) -> Mat:
    out = mzero()
    rows = []
    for i in range(2):
        row = []
        for j in range(2):
            s = (0.0, 0.0)
            for k in range(2):
                s = cadd(s, cmul(a[i][k], b[k][j]))
            row.append(s)
        rows.append(tuple(row))
    return tuple(rows)


def mdag(a: Mat) -> Mat:
    return (
        (cconj(a[0][0]), cconj(a[1][0])),
        (cconj(a[0][1]), cconj(a[1][1])),
    )


def mscale(s: float, a: Mat) -> Mat:
    return tuple(tuple(cscale(s, a[i][j]) for j in range(2)) for i in range(2))


def outer(u, v) -> Mat:
    """|u><v|."""
    return tuple(tuple(cmul(u[i], cconj(v[j])) for j in range(2)) for i in range(2))


def frobenius(a: Mat) -> float:
    s = 0.0
    for i in range(2):
        for j in range(2):
            s += a[i][j][0] ** 2 + a[i][j][1] ** 2
    return math.sqrt(s)


def bloch_rho(r) -> Mat:
    x, y, z = r
    return (
        ((0.5 * (1.0 + z), 0.0), (0.5 * x, -0.5 * y)),
        ((0.5 * x, 0.5 * y), (0.5 * (1.0 - z), 0.0)),
    )


def rho_bloch(rho: Mat):
    rx = 2.0 * rho[0][1][0]
    ry = 2.0 * rho[0][1][1]
    rz = rho[0][0][0] - rho[1][1][0]
    return (rx, ry, rz)


def axis_ket(n, plus: bool):
    nx, ny, nz = n
    # n is a unit vector. θ from z, φ from x.
    theta = math.acos(max(-1.0, min(1.0, nz)))
    phi = math.atan2(ny, nx)
    c = math.cos(0.5 * theta)
    s = math.sin(0.5 * theta)
    e = (math.cos(phi), math.sin(phi))
    if plus:
        return ((c, 0.0), cmul(e, (s, 0.0)))
    return (cscale(-1.0, (s, 0.0)), cmul(e, (c, 0.0)))


def kraus(n, plus: bool) -> Mat:
    alpha = math.sqrt(0.5 * (1.0 + ETA))
    beta = math.sqrt(0.5 * (1.0 - ETA))
    up = axis_ket(n, True)
    dn = axis_ket(n, False)
    if plus:
        return madd(mscale(alpha, outer(up, up)), mscale(beta, outer(dn, dn)))
    return madd(mscale(beta, outer(up, up)), mscale(alpha, outer(dn, dn)))


def effect(n, plus: bool) -> Mat:
    m = kraus(n, plus)
    return mmul(mdag(m), m)


def apply_kraus(m: Mat, rho: Mat):
    prod = mmul(mmul(m, rho), mdag(m))
    p = prod[0][0][0] + prod[1][1][0]
    if p <= 0.0:
        raise SystemExit("kraus probability is not positive")
    return p, mscale(1.0 / p, prod)


def _comm(a: Mat, b: Mat) -> Mat:
    return madd(mmul(a, b), mscale(-1.0, mmul(b, a)))


def commutator_norm_fixed() -> float:
    ez = effect((0.0, 0.0, 1.0), True)
    ex = effect((1.0, 0.0, 0.0), True)
    return frobenius(_comm(ez, ex))


def entropy_eigs(eigs) -> float:
    s = 0.0
    for e in eigs:
        if e > 1e-15:
            s -= e * math.log(e)
    return s


def qutrit_review():
    # diag(1/2, 1/4, 1/4). Lüders projectors leave it fixed.
    eigs = (0.5, 0.25, 0.25)
    s_rho = entropy_eigs(eigs)
    s_phi = s_rho
    p_d = s_phi - s_rho
    info = 0.0
    h_m = math.log(2.0)
    gap = abs((info + p_d) - (h_m - s_rho))
    return p_d, info, gap


def qutrit_coherent():
    """Lüders map of the review projectors on the coherent block.

    P0 = |0><0| and P1 = |1><1|+|2><2| keep coherence inside the block.
    The first run subtracted the entropy of the dephased diagonal instead.
    """
    rho = (
        (0.5, 0.0, 0.0),
        (0.0, 0.25, 0.125),
        (0.0, 0.125, 0.25),
    )
    phi = (
        (rho[0][0], 0.0, 0.0),
        (0.0, rho[1][1], rho[1][2]),
        (0.0, rho[2][1], rho[2][2]),
    )
    for i in range(3):
        for j in range(3):
            if abs(phi[i][j] - rho[i][j]) > 1e-15:
                raise SystemExit("named projectors moved the coherent block")
    # One state, fixed by the instrument: I = 0 and P_D = 0.
    return 0.0


def sequential():
    """First unsharp z, then unsharp x, on ANT. Returns I(W;M2|M1), P_D total, I(W;M1,M2), L2."""
    nz = (0.0, 0.0, 1.0)
    nx = (1.0, 0.0, 0.0)
    mz = (kraus(nz, True), kraus(nz, False))
    mx = (kraus(nx, True), kraus(nx, False))
    # joint[w_index][m1][m2] = probability
    joints = []
    pd_first = 0.0
    pd_second = 0.0
    for w, pre in ANT:
        rho = bloch_rho(pre)
        pd_first += w * (qubit_entropy(norm(channel_bloch(pre, nz))) - qubit_entropy(norm(pre)))
        row = []
        for m1 in (0, 1):
            p1, rho1 = apply_kraus(mz[m1], rho)
            # matrix probability must match the Bloch formula
            expect = p_plus(pre, nz) if m1 == 0 else 1.0 - p_plus(pre, nz)
            if abs(p1 - expect) > 1e-9:
                raise SystemExit(f"kraus/Bloch mismatch {p1} vs {expect}")
            cell = []
            for m2 in (0, 1):
                p2, _rho2 = apply_kraus(mx[m2], rho1)
                cell.append(p1 * p2)
            # disturbance of the second instrument on the conditional state
            post = channel_bloch(rho_bloch(rho1), nx)
            pd_second += w * p1 * (qubit_entropy(norm(post)) - qubit_entropy(norm(rho_bloch(rho1))))
            row.append(cell)
        joints.append(row)
    # I(W; M2 | M1)
    # p(m1), p(m2=+|m1), p(w,m1)
    h_m2_m1 = 0.0
    h_m2_m1w = 0.0
    for m1 in (0, 1):
        p_m1 = 0.0
        p_m2_plus = 0.0
        for wi, (w, _pre) in enumerate(ANT):
            p_wm1 = w * (joints[wi][m1][0] + joints[wi][m1][1])
            p_m1 += p_wm1
            p_m2_plus += w * joints[wi][m1][0]
            if p_wm1 > 0.0:
                cond = joints[wi][m1][0] / (joints[wi][m1][0] + joints[wi][m1][1])
                h_m2_m1w += p_wm1 * hbin(cond)
        if p_m1 > 0.0:
            h_m2_m1 += p_m1 * hbin(p_m2_plus / p_m1)
    cond_info = h_m2_m1 - h_m2_m1w
    # I(W; M1, M2)
    # four outcome masses
    masses = [0.0, 0.0, 0.0, 0.0]
    h_given_w = 0.0
    for wi, (w, _pre) in enumerate(ANT):
        local = []
        for m1 in (0, 1):
            for m2 in (0, 1):
                local.append(joints[wi][m1][m2])
        h = 0.0
        for k, pk in enumerate(local):
            masses[k] += w * pk
            if pk > 0.0:
                h -= pk * math.log(pk)
        h_given_w += w * h
    h_joint = 0.0
    for pk in masses:
        if pk > 0.0:
            h_joint -= pk * math.log(pk)
    info = h_joint - h_given_w
    # L2 from the marginal of M2
    pps = []
    ys = []
    weights = []
    pbar = 0.0
    for wi, (w, pre) in enumerate(ANT):
        p2 = joints[wi][0][0] + joints[wi][1][0]
        pps.append(p2)
        ys.append(pre[2])
        weights.append(w)
        pbar += w * p2
    a_hat = [0.0, 0.0]
    for sign, pm in enumerate((pbar, 1.0 - pbar)):
        if pm <= 0.0:
            continue
        acc = 0.0
        for w, pp, y in zip(weights, pps, ys):
            pm_w = pp if sign == 0 else (1.0 - pp)
            acc += w * pm_w * y
        a_hat[sign] = acc / pm
    loss = 0.0
    for w, pp, y in zip(weights, pps, ys):
        for sign, pm_w in enumerate((pp, 1.0 - pp)):
            d = y - a_hat[sign]
            loss += w * pm_w * d * d
    return cond_info, pd_first + pd_second, info, loss


def garble_gap() -> float:
    # projective z outcome probabilities, then a BSC, versus unsharp x
    nz = (0.0, 0.0, 1.0)
    nx = (1.0, 0.0, 0.0)
    # the +x label is ANT[2]
    p_z = 0.5 * (1.0 + dot(ANT[2][1], nz))
    p_x = p_plus(ANT[2][1], nx)
    worst = None
    for eps in (0.0, 0.25, 0.5):
        p_g = (1.0 - 2.0 * eps) * p_z + eps
        gap = abs(p_g - p_x)
        if worst is None or gap < worst:
            worst = gap
    return worst


def trace_distance_paths() -> float:
    plus_x = (R, 0.0, 0.0)
    after_unsharp = channel_bloch(plus_x, (1.0, 0.0, 0.0))
    # projective z: gamma = 0 along z
    proj = dot(plus_x, (0.0, 0.0, 1.0))
    after_z = (proj, 0.0, 0.0)  # Bloch (0,0,proj) and proj is 0
    after_z = (0.0, 0.0, proj)
    delta = (
        after_unsharp[0] - after_z[0],
        after_unsharp[1] - after_z[1],
        after_unsharp[2] - after_z[2],
    )
    return 0.5 * norm(delta)


def main():
    lines = []
    fails = 0

    norm_c = commutator_norm_fixed()
    target = (ETA ** 2) / math.sqrt(2.0)
    ok = abs(norm_c - 0.176776695297) < 1e-9 and norm_c > 0.1 and abs(norm_c - target) < 1e-12
    fails += 0 if ok else 1
    lines.append(f"Q-comm {'PASS' if ok else 'FAIL'} frobenius={norm_c:.12f}")

    pds = []
    for th in grid():
        _i, p_d, _l = row_functionals(n_theta(th))
        pds.append(p_d)
    j0 = j_star(0.0)
    undershoot = None
    for q in (0.5, 1.0, 2.0):
        gap = j_star(q) - j0
        if gap < -1e-9:
            undershoot = (q, gap)
    ok = min(pds) > 0.02 and undershoot is None
    fails += 0 if ok else 1
    extra = "" if undershoot is None else f" undershoot_q={undershoot[0]} gap={undershoot[1]:.3e}"
    lines.append(f"Q-slope {'PASS' if ok else 'FAIL'} min_PD={min(pds):.6f} max_PD={max(pds):.6f}{extra}")

    pd0 = row_functionals(n_theta(0.0))[1]
    pd90 = row_functionals(n_theta(HALF_PI))[1]
    ok = pd0 > 0.02 and pd90 > 0.02
    fails += 0 if ok else 1
    lines.append(f"Q-pointer {'PASS' if ok else 'FAIL'} PD0={pd0:.6f} PDpi2={pd90:.6f}")

    gap = garble_gap()
    ok = gap > 0.1
    fails += 0 if ok else 1
    lines.append(f"Q-garble {'PASS' if ok else 'FAIL'} min_gap={gap:.6f}")

    dist = trace_distance_paths()
    ok = dist > 0.2
    fails += 0 if ok else 1
    lines.append(f"Q-state {'PASS' if ok else 'FAIL'} trace_distance={dist:.6f}")

    cond, pd_tot, info, loss = sequential()
    costs = [info + q * pd_tot + W_STAKE * loss for q in (0.0, 1.0, 2.0)]
    ok = cond > 0.05 and pd_tot > 0.02 and (costs[1] - costs[0]) > 0.01 and (costs[2] - costs[0]) > 0.01
    fails += 0 if ok else 1
    lines.append(
        f"Q-reuse {'PASS' if ok else 'FAIL'} I_cond={cond:.6f} PD_total={pd_tot:.6f} "
        f"gap1={costs[1] - costs[0]:.6f} gap2={costs[2] - costs[0]:.6f}"
    )

    p_d, info_r, gap_r = qutrit_review()
    half = 0.5 * math.log(2.0)
    ok = abs(p_d) < 1e-12 and abs(info_r) < 1e-12 and abs(gap_r - half) < 1e-9 and abs(p_d) < 1e-12
    fails += 0 if ok else 1
    lines.append(
        f"Q-rank {'PASS' if ok else 'FAIL'} PD={p_d:.3e} I={info_r:.3e} "
        f"ledger_gap={gap_r:.12f} half_ln2={half:.12f}"
    )

    pd_c = qutrit_coherent()
    ok = pd_c > 0.01 and pd_c > 0.01
    fails += 0 if ok else 1
    lines.append(f"Q-coh {'PASS' if ok else 'FAIL'} PD={pd_c:.6f} cost_gap={pd_c:.6f}")

    lines.append(f"FAILS {fails}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
