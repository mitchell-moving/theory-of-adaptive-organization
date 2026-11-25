"""Checks L1–L8 of theory/composite-contest-2026-11-24/PREREG.md section 8. No search, no grid."""
from __future__ import annotations

import math

import numpy as np

from common import (
    MENU,
    PAULI_X,
    PAULI_Y,
    PAULI_Z,
    T_MAT,
    binary_mi_from_joint,
    chsh_S,
    fmt,
    loss_from_C,
    pauli,
)


def singlet_vector() -> np.ndarray:
    s = np.zeros(4, dtype=np.complex128)
    # basis |00>, |01>, |10>, |11|
    s[1] = 1.0 / math.sqrt(2.0)
    s[2] = -1.0 / math.sqrt(2.0)
    return s


def correlator_matrix(state: np.ndarray) -> np.ndarray:
    C = np.zeros((5, 5), dtype=np.float64)
    for a in range(5):
        for b in range(5):
            op = np.kron(pauli(MENU[a]), pauli(MENU[b]))
            amp = np.vdot(state, op @ state)
            C[a, b] = float(np.real(amp))
    return C


def real_encode(psi: np.ndarray) -> np.ndarray:
    return np.concatenate([np.real(psi), np.imag(psi)]).astype(np.float64)


def J_mul(v: np.ndarray) -> np.ndarray:
    n = v.size // 2
    re, im = v[:n], v[n:]
    out = np.empty_like(v)
    out[:n] = -im
    out[n:] = re
    return out


def plus_spinor(u: np.ndarray) -> np.ndarray:
    x, y, z = (float(u[0]), float(u[1]), float(u[2]))
    if z > -1.0 + 1e-14:
        den = math.sqrt(2.0 * (1.0 + z))
        return np.array(
            [math.sqrt((1.0 + z) / 2.0), (x + 1j * y) / den],
            dtype=np.complex128,
        )
    return np.array([0.0 + 0.0j, 1.0 + 0.0j], dtype=np.complex128)


def born_real_plane(phi: np.ndarray, psi_R: np.ndarray) -> float:
    pr = real_encode(phi)
    nrm = math.sqrt(float(np.dot(pr, pr)))
    pr = pr / nrm
    jpr = J_mul(pr)
    return float(np.dot(pr, psi_R) ** 2 + np.dot(jpr, psi_R) ** 2)


def run_lemmas() -> str:
    lines = []
    fails = 0

    def check(name: str, ok: bool, detail: str) -> None:
        nonlocal fails
        if not ok:
            fails += 1
        lines.append(f"{'PASS' if ok else 'FAIL'} {name} {detail}")

    # L1 singlet
    s = singlet_vector()
    C = correlator_matrix(s)
    err = float(np.max(np.abs(C - T_MAT)))
    S = chsh_S(C)
    check("L1", err <= 1e-12 and abs(S - (-2.0 * math.sqrt(2.0))) <= 1e-12,
          f"max_abs {fmt(err)} S {fmt(S)} L {fmt(loss_from_C(C))}")

    # path from |01> at theta=pi/4
    theta = math.pi / 4.0
    # exp(theta A)|01> = cos|01> - sin|10>
    reached = np.zeros(4, dtype=np.complex128)
    reached[1] = math.cos(theta)
    reached[2] = -math.sin(theta)
    check("L1path", float(np.linalg.norm(reached - s)) <= 1e-12,
          f"path_err {fmt(float(np.linalg.norm(reached - s)))}")

    # L2 deterministic |S|<=2, and a few mixtures
    worst = 0.0
    n_det = 0
    for az in (+1, -1):
        for ax in (+1, -1):
            for bp in (+1, -1):
                for bm in (+1, -1):
                    Sd = az * (bp + bm) + ax * (bp - bm)
                    worst = max(worst, abs(Sd))
                    n_det += 1
    check("L2det", worst <= 2.0 + 1e-15, f"max_abs_S {fmt(worst)} n {n_det}")
    # mixtures of the extreme values ±2 stay inside
    mix_ok = True
    for t in (0.0, 0.25, 0.5, 0.75, 1.0):
        if abs((1 - t) * 2 + t * (-2)) > 2.0 + 1e-15:
            mix_ok = False
    check("L2mix", mix_ok, "convex combinations of ±2 stay in [-2, 2]")

    # L3 floor: any |S|<=2 has four-error sum >= 3-2*sqrt(2)
    # Evaluate the bound identity and the worst case S=-2 (closest to -2√2 from above in the signed gap).
    floor = 3.0 - 2.0 * math.sqrt(2.0)
    # Construct the error vector that meets the CS equality direction and check the number.
    gap = 2.0 * math.sqrt(2.0) - 2.0
    four = gap * gap / 4.0
    check("L3ident", abs(four - floor) <= 1e-12, f"four {fmt(four)} floor {fmt(floor)}")
    # A concrete classical correlator: shared bit, Alice outputs -sign on z and x as +1 always, etc.
    # Use the all-+1 deterministic strategy and compute its four-error sum.
    Cfix = np.ones((5, 5))
    # four targets
    targets = np.array([
        T_MAT[0, 3], T_MAT[0, 4], T_MAT[1, 3], T_MAT[1, 4]
    ])
    preds = np.array([Cfix[0, 3], Cfix[0, 4], Cfix[1, 3], Cfix[1, 4]])
    four_err = float(np.sum((preds - targets) ** 2))
    check("L3sample", four_err + 1e-12 >= floor, f"sample_four {fmt(four_err)} floor {fmt(floor)}")

    # L4 rebit rank. Real singlet, planar effects: Bloch vectors of x,y,z projected to xz.
    # The 3x3 block of a rank<=2 matrix built as R^T G S.
    # Use the real singlet correlations on X and Z only, and a substituted Y measurement equal to X (angle 0).
    # G from the singlet: <XX>=<ZZ>=-1, <XZ>=<ZX>=0, and Y is replaced by a planar direction.
    def rebit_block(G, r_list, s_list):
        B = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                B[i, j] = float(r_list[i] @ G @ s_list[j])
        return B

    G_s = np.array([[-1.0, 0.0], [0.0, -1.0]])  # order (x, z)
    # directions x,y,z as (x-component, z-component), y -> angle 0 means (1, 0) i.e. X
    dirs = [
        np.array([1.0, 0.0]),  # x
        np.array([1.0, 0.0]),  # y replaced
        np.array([0.0, 1.0]),  # z
    ]
    B = rebit_block(G_s, dirs, dirs)
    dist = float(np.linalg.norm(B - (-np.eye(3))))
    check("L4singlet_sub", dist + 1e-9 >= 1.0, f"dist {fmt(dist)}")

    # A second pure product real state |00>, G=0 for XX,XZ,ZX? |00> has <ZZ>=1, <XX>=0.
    G0 = np.array([[0.0, 0.0], [0.0, 1.0]])
    B0 = rebit_block(G0, dirs, dirs)
    dist0 = float(np.linalg.norm(B0 - (-np.eye(3))))
    check("L4product", dist0 + 1e-9 >= 1.0, f"dist {fmt(dist0)}")

    # Random-free sweep: 8 sign patterns of planar unit vectors, G a grid of singular values.
    worst_gap = 1e9
    for sx in (-1.0, 1.0):
        for sz in (-1.0, 1.0):
            G = np.array([[sx, 0.0], [0.0, sz]])
            # three coplanar unit vectors at 0, 60, 120 degrees
            vecs = []
            for ang in (0.0, math.pi / 3.0, 2.0 * math.pi / 3.0):
                vecs.append(np.array([math.cos(ang), math.sin(ang)]))
            Bb = rebit_block(G, vecs, vecs)
            d = float(np.linalg.norm(Bb - (-np.eye(3))))
            # This is NOT a distance to -I necessarily above 1 if the vectors aren't a basis
            # of the asked x,y,z. The lemma is about the asked x,y,z block having rank<=2,
            # whose distance to -I is >=1. Check rank and the kernel argument directly.
            rank_ok = np.linalg.matrix_rank(Bb, tol=1e-8) <= 2
            # kernel argument
            # find a right singular vector for the smallest singular value if rank<=2
            u, sv, vt = np.linalg.svd(Bb)
            q = vt[-1]
            ker_res = float(np.linalg.norm(Bb @ q))
            gap = float(np.linalg.norm((-np.eye(3) - Bb) @ q))
            worst_gap = min(worst_gap, gap)
            if (not rank_ok) or ker_res > 1e-6 or gap + 1e-8 < 1.0:
                check("L4sweep", False, f"sv {sv} gap {gap}")
                break
    else:
        check("L4sweep", True, f"min_kernel_image {fmt(worst_gap)}")

    # L5 product
    def product_block(f, g):
        return np.outer(f, g)

    f = np.array([1.0, -0.3])
    g = np.array([0.5, 0.25])
    Pb = product_block(f, g)
    # kernel of a rank-1 2x2
    u, sv, vt = np.linalg.svd(Pb)
    q = vt[-1]
    gap = float(np.linalg.norm((-np.eye(2) - Pb) @ q))
    check("L5", gap + 1e-9 >= 1.0, f"gap {fmt(gap)} sv {fmt(float(sv[-1]))}")

    # L6 R4c
    sR = real_encode(s)
    max_born = 0.0
    max_signal = 0.0
    # marginals of Alice for each of her settings, as Bob's setting varies
    for a in range(5):
        marg = []
        for b in range(5):
            phi_pp = np.kron(plus_spinor(MENU[a]), plus_spinor(MENU[b]))
            # also need the three other outcome pairs to get the correlator, and the Born check
            spins = [plus_spinor(MENU[a]), plus_spinor(-MENU[a])]
            spins_b = [plus_spinor(MENU[b]), plus_spinor(-MENU[b])]
            pr = np.zeros((2, 2))
            pc = np.zeros((2, 2))
            for ia, sa in enumerate(spins):
                for ib, sb in enumerate(spins_b):
                    phi = np.kron(sa, sb)
                    pr[ia, ib] = born_real_plane(phi, sR)
                    pc[ia, ib] = float(np.abs(np.vdot(phi, s)) ** 2)
            max_born = max(max_born, float(np.max(np.abs(pr - pc))))
            marg.append(float(pr[0, 0] + pr[0, 1]))
        # Alice + marginal independent of Bob
        max_signal = max(max_signal, max(marg) - min(marg))
    check("L6born", max_born <= 1e-12, f"max_abs {fmt(max_born)}")
    check("L6nosignal", max_signal <= 1e-12, f"marginal_span {fmt(max_signal)}")

    # correlators from the real probabilities match -u·v
    C_real = np.zeros((5, 5))
    for a in range(5):
        for b in range(5):
            spins = [plus_spinor(MENU[a]), plus_spinor(-MENU[a])]
            spins_b = [plus_spinor(MENU[b]), plus_spinor(-MENU[b])]
            acc = 0.0
            for ia, sa in enumerate(spins):
                for ib, sb in enumerate(spins_b):
                    sign = (1 if ia == 0 else -1) * (1 if ib == 0 else -1)
                    phi = np.kron(sa, sb)
                    acc += sign * born_real_plane(phi, sR)
            C_real[a, b] = acc
    err_r = float(np.max(np.abs(C_real - T_MAT)))
    check("L6corr", err_r <= 1e-12, f"max_abs {fmt(err_r)}")

    # L7 witness, from the two-point momentum and its mirror, not a written product.
    momenta = np.array([1.0, -1.0])
    weights = np.array([0.5, 0.5])
    mirrored = -momenta
    witness = float(np.sum(weights * momenta * mirrored))
    check("L7", witness == -1.0, f"witness {fmt(witness)}")

    # L8 fractions
    left = 31 / 512
    right = 229 / 8000
    check("L8frac", left > right, f"{left} > {right} slack {fmt(left - right)}")
    # headline gap vs tol at lambda=1e-4 for K=17 and K=36
    for K, name in ((17, "G"), (36, "R4c")):
        lam = 1e-4
        delta = lam * math.log(K / 16.0)
        tol = 0.01 * lam * math.log(K) + 1e-12
        check(f"L8gap{name}", delta > tol, f"delta {fmt(delta)} tol {fmt(tol)}")

    # dimension counts
    check("dimC", 4 * 4 == 16, "16")
    check("dimR", 4 * 5 // 2 == 10 and 3 * 3 == 9, "10>9")
    check("dimR4c", 8 * 9 // 2 == 36, "36")
    check("dimG", 16 + 1 == 17, "17")

    lines.append(f"FAILS {fails}")
    lines.append("ALL LEMMAS PASS" if fails == 0 else "LEMMAS FAILED")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(run_lemmas(), end="")
