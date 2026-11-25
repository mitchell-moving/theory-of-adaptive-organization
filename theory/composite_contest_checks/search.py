"""Classical search, rebit seesaw, product seesaw. Locked by theory/composite-contest-2026-11-24/PREREG.md §§5 and 9."""
from __future__ import annotations

import math

import numpy as np

from common import (
    FW_ITERS,
    N_SET,
    REOPT_ITERS,
    SEESAW_ROUNDS,
    STATE_ITERS,
    T_FLAT,
    T_MAT,
    WEIGHT_TOL,
    X,
    Z,
    loss_from_C,
)


def vertex_correlators() -> np.ndarray:
    signs = np.ones((32, N_SET), dtype=np.float64)
    for k in range(32):
        for i in range(N_SET):
            if (k >> i) & 1:
                signs[k, i] = -1.0
    C = np.empty((1024, 25), dtype=np.float64)
    p = 0
    for alpha in range(32):
        for beta in range(32):
            C[p] = np.outer(signs[alpha], signs[beta]).ravel()
            p += 1
    return C


def _loss_flat(corr: np.ndarray) -> float:
    d = corr - T_FLAT
    return float(np.dot(d, d) / 25.0)


def best_M1(C: np.ndarray) -> tuple[float, int]:
    # ||C_i - T||^2 / 25
    D = C - T_FLAT
    losses = np.sum(D * D, axis=1) / 25.0
    i = int(np.argmin(losses))
    return float(losses[i]), i


def best_M2(C: np.ndarray) -> tuple[float, int, int, float]:
    best = math.inf
    bi = bj = 0
    bt = 0.0
    for i in range(1023):
        V = C[i + 1 :] - C[i]
        d = C[i] - T_FLAT
        dd = float(np.dot(d, d))
        dv = V @ d
        vv = np.sum(V * V, axis=1)
        t = np.zeros(V.shape[0], dtype=np.float64)
        mask = vv > 1e-18
        t[mask] = -dv[mask] / vv[mask]
        np.clip(t, 0.0, 1.0, out=t)
        loss = (dd + 2.0 * t * dv + (t * t) * vv) / 25.0
        j = int(np.argmin(loss))
        val = float(loss[j])
        if val < best:
            best = val
            bi = i
            bj = i + 1 + j
            bt = float(t[j])
    return best, bi, bj, bt


def frank_wolfe(C: np.ndarray) -> np.ndarray:
    w = np.full(1024, 1.0 / 1024.0, dtype=np.float64)
    for k in range(FW_ITERS):
        corr = w @ C
        resid = corr - T_FLAT
        scores = C @ resid
        j = int(np.argmin(scores))
        gamma = 2.0 / (k + 2.0)
        w *= 1.0 - gamma
        w[j] += gamma
    return w


def reoptimize(atom_C: np.ndarray, p0: np.ndarray) -> np.ndarray:
    """Projected reduced gradient, exact line search, REOPT_ITERS steps."""
    A = np.ascontiguousarray(atom_C.T)  # (25, m)
    m = atom_C.shape[0]
    p = np.array(p0, dtype=np.float64)
    s = p.sum()
    if s <= 0.0:
        p[:] = 1.0 / m
    else:
        p /= s
    t = T_FLAT
    for _ in range(REOPT_ITERS):
        r = A @ p - t
        g = A.T @ r
        free = np.flatnonzero(p > 1e-15)
        if free.size <= 1:
            break
        gf = g[free]
        gf = gf - gf.mean()
        d = np.zeros(m, dtype=np.float64)
        d[free] = -gf
        nd = float(np.dot(d, d))
        if nd < 1e-28:
            break
        alpha_max = math.inf
        for i in range(m):
            if d[i] < -1e-18:
                alpha_max = min(alpha_max, -p[i] / d[i])
        Ad = A @ d
        denom = float(np.dot(Ad, Ad))
        if denom < 1e-28:
            break
        alpha = -float(np.dot(r, Ad)) / denom
        if alpha < 0.0:
            alpha = 0.0
        if alpha > alpha_max:
            alpha = alpha_max
        if alpha == 0.0:
            break
        p = p + alpha * d
        p[p < 1e-15] = 0.0
        sm = float(p.sum())
        if sm <= 0.0:
            p[:] = 1.0 / m
        else:
            p /= sm
    return p


def elimination_curve(C: np.ndarray, w: np.ndarray) -> list[tuple[int, float, np.ndarray]]:
    support = np.flatnonzero(w > WEIGHT_TOL)
    atom = C[support]
    p = w[support]
    p = p / p.sum()
    p = reoptimize(atom, p)
    # drop numerical zeros and renorm
    keep = p > WEIGHT_TOL
    atom = atom[keep]
    p = p[keep]
    p = p / p.sum()
    curve = [(int(p.size), _loss_flat(p @ atom), p.copy())]
    while p.size > 1:
        m = p.size
        best_loss = math.inf
        best_i = m
        best_p = None
        best_atom = None
        for i in range(m):
            mask = np.ones(m, dtype=bool)
            mask[i] = False
            p_try = p[mask]
            p_try = p_try / p_try.sum()
            atom_try = atom[mask]
            p_opt = reoptimize(atom_try, p_try)
            # drop new zeros
            kz = p_opt > WEIGHT_TOL
            if not np.all(kz):
                p_opt = p_opt[kz]
                atom_try = atom_try[kz]
                if p_opt.size == 0:
                    continue
                p_opt = p_opt / p_opt.sum()
            loss = _loss_flat(p_opt @ atom_try)
            if loss < best_loss - 1e-15 or (abs(loss - best_loss) <= 1e-15 and i < best_i):
                best_loss = loss
                best_i = i
                best_p = p_opt
                best_atom = atom_try
        p = best_p
        atom = best_atom
        curve.append((int(p.size), float(best_loss), p.copy()))
    return curve


def lower_envelope(m1: float, m2: float, curve: list[tuple[int, float, np.ndarray]]) -> list[tuple[int, float]]:
    pts = [(1, m1), (2, m2)]
    for M, L, _p in curve:
        pts.append((int(M), float(L)))
    # best loss at each M
    best: dict[int, float] = {}
    for M, L in pts:
        if M not in best or L < best[M]:
            best[M] = L
    return sorted(best.items())


def choose_model(envelope: list[tuple[int, float]], lam: float, eps: float) -> tuple[bool, int, float, float]:
    best_J = math.inf
    best = None
    for M, L in envelope:
        if L <= eps + 1e-15:
            J = lam * math.log(M) + L
            if J < best_J:
                best_J = J
                best = (M, L, J)
    if best is None:
        # infeasible: report the smallest loss on the curve for the record
        M, L = min(envelope, key=lambda z: (z[1], z[0]))
        return False, M, L, math.inf
    return True, best[0], best[1], best[2]


def best_disk(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Minimize r^T A r - 2 b·r on the unit disk. A symmetric 2x2."""
    evals, evec = np.linalg.eigh(A)
    # unconstrained
    if evals[0] > 1e-12:
        r = np.linalg.solve(A, b)
        if float(np.dot(r, r)) <= 1.0 + 1e-10:
            n2 = float(np.dot(r, r))
            if n2 > 1.0:
                r = r / math.sqrt(n2)
            return r
    # boundary critical points via the secular polynomial in the eigenbasis
    bp = evec.T @ b
    w0, w1 = float(evals[0]), float(evals[1])
    b0, b1 = float(bp[0]), float(bp[1])
    # b0^2 (w1-λ)^2 + b1^2 (w0-λ)^2 - (w0-λ)^2 (w1-λ)^2 = 0
    # Let u = λ. Expand with numpy.
    # (w - u) = -u + w
    def poly_from_linear(slope, intercept):
        # slope * u + intercept, as highest-degree-first of degree 1
        return np.array([slope, intercept], dtype=np.float64)

    p_w0 = poly_from_linear(-1.0, w0)  # w0 - u
    p_w1 = poly_from_linear(-1.0, w1)
    p0 = np.polymul(p_w0, p_w0)  # (w0-u)^2
    p1 = np.polymul(p_w1, p_w1)
    left = b0 * b0 * p1 + b1 * b1 * p0
    right = np.polymul(p0, p1)
    # left - right = 0. right is degree 4, left degree 2.
    poly = -right
    poly[-len(left) :] += left
    roots = np.roots(poly)
    cands = []
    if evals[0] > 1e-12:
        r_unc = np.linalg.solve(A, b)
        if float(np.dot(r_unc, r_unc)) <= 1.0 + 1e-8:
            cands.append(r_unc)
    for lam in roots:
        if abs(lam.imag) > 1e-8:
            continue
        lam = float(lam.real)
        y = np.zeros(2)
        ok = True
        for i, (wi, bi) in enumerate(((w0, b0), (w1, b1))):
            den = wi - lam
            if abs(den) < 1e-10:
                if abs(bi) > 1e-8:
                    ok = False
                y[i] = 0.0
            else:
                y[i] = bi / den
        if not ok:
            continue
        n2 = float(np.dot(y, y))
        if n2 < 1e-14:
            continue
        y = y / math.sqrt(n2)
        cands.append(evec @ y)
        cands.append(-(evec @ y))
    # also the two axis endpoints in case the polynomial misses a root
    for ang in (0.0, math.pi / 2, math.pi, 3 * math.pi / 2):
        cands.append(np.array([math.cos(ang), math.sin(ang)]))
    if not cands:
        return np.zeros(2)

    def f(r):
        return float(r @ A @ r - 2.0 * np.dot(b, r))

    best = min(cands, key=f)
    n2 = float(np.dot(best, best))
    if n2 > 1.0:
        best = best / math.sqrt(n2)
    return best


def correlators_from_effects(G: np.ndarray, ra: np.ndarray, rb: np.ndarray) -> np.ndarray:
    C = np.zeros((N_SET, N_SET), dtype=np.float64)
    for a in range(N_SET):
        for b in range(N_SET):
            C[a, b] = float(ra[a] @ G @ rb[b])
    return C


def optimize_effects(G: np.ndarray, ra: np.ndarray, rb: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # v_b = G s_b, Alice wants r · v ≈ T
    for a in range(N_SET):
        A = np.zeros((2, 2))
        bvec = np.zeros(2)
        for b in range(N_SET):
            v = G @ rb[b]
            A += np.outer(v, v)
            bvec += T_MAT[a, b] * v
        ra[a] = best_disk(A, bvec)
    for b in range(N_SET):
        A = np.zeros((2, 2))
        bvec = np.zeros(2)
        for a in range(N_SET):
            v = G.T @ ra[a]
            A += np.outer(v, v)
            bvec += T_MAT[a, b] * v
        rb[b] = best_disk(A, bvec)
    return ra, rb


XX = np.kron(X, X)
XZ = np.kron(X, Z)
ZX = np.kron(Z, X)
ZZ = np.kron(Z, Z)


def unpack_chol(x: np.ndarray) -> np.ndarray:
    L = np.zeros((4, 4), dtype=np.float64)
    k = 0
    for i in range(4):
        for j in range(i + 1):
            L[i, j] = x[k]
            k += 1
    S = L @ L.T
    tau = float(np.trace(S))
    if tau < 1e-18:
        return np.eye(4) / 4.0
    return S / tau


def G_of_rho(rho: np.ndarray) -> np.ndarray:
    def tr(M):
        return float(np.trace(rho @ M))

    return np.array([[tr(XX), tr(XZ)], [tr(ZX), tr(ZZ)]], dtype=np.float64)


def loss_of_rho(rho: np.ndarray, ra: np.ndarray, rb: np.ndarray) -> float:
    return loss_from_C(correlators_from_effects(G_of_rho(rho), ra, rb))


def _chol_matrix(x: np.ndarray) -> np.ndarray:
    L = np.zeros((4, 4), dtype=np.float64)
    k = 0
    for i in range(4):
        for j in range(i + 1):
            L[i, j] = x[k]
            k += 1
    return L


def loss_grad_chol(x: np.ndarray, ra: np.ndarray, rb: np.ndarray) -> tuple[float, np.ndarray]:
    """Loss and Euclidean gradient on the 10 Cholesky entries."""
    L = _chol_matrix(x)
    S = L @ L.T
    tau = float(np.trace(S))
    if tau < 1e-18:
        return loss_of_rho(np.eye(4) / 4.0, ra, rb), np.zeros(10)
    rho = S / tau
    G = G_of_rho(rho)
    C = correlators_from_effects(G, ra, rb)
    dC = 2.0 * (C - T_MAT) / 25.0
    dG = np.zeros((2, 2), dtype=np.float64)
    for a in range(N_SET):
        for b in range(N_SET):
            rx, rz = float(ra[a, 0]), float(ra[a, 1])
            sx, sz = float(rb[b, 0]), float(rb[b, 1])
            dc = float(dC[a, b])
            dG[0, 0] += dc * rx * sx
            dG[0, 1] += dc * rx * sz
            dG[1, 0] += dc * rz * sx
            dG[1, 1] += dc * rz * sz
    d_rho = dG[0, 0] * XX + dG[0, 1] * XZ + dG[1, 0] * ZX + dG[1, 1] * ZZ
    d_rho = 0.5 * (d_rho + d_rho.T)
    # rho = S/tau, dL = <d_rho, dS>/tau - <d_rho, S> dtau / tau^2
    coeff = float(np.sum(d_rho * S)) / (tau * tau)
    dS = d_rho / tau - coeff * np.eye(4)
    dS = 0.5 * (dS + dS.T)
    # <dS, dL L^T + L dL^T> = 2 <dS @ L, dL>
    gL = 2.0 * (dS @ L)
    grad = np.zeros(10, dtype=np.float64)
    k = 0
    for i in range(4):
        for j in range(i + 1):
            grad[k] = gL[i, j]
            k += 1
    return loss_from_C(C), grad


def state_step(x: np.ndarray, ra: np.ndarray, rb: np.ndarray) -> np.ndarray:
    """One gradient step on the Cholesky factor with an exact line search on a bracket."""
    base, grad = loss_grad_chol(x, ra, rb)
    gnorm = float(np.linalg.norm(grad))
    if gnorm < 1e-14:
        return x
    direction = -grad / gnorm

    def at(alpha: float) -> float:
        return loss_of_rho(unpack_chol(x + alpha * direction), ra, rb)

    alphas = (0.0, 1e-4, 1e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0)
    vals = [at(a) for a in alphas]
    j = min(range(len(vals)), key=lambda i: vals[i])
    if j == 0:
        return x
    lo = alphas[j - 1]
    hi = alphas[j + 1] if j + 1 < len(alphas) else alphas[j]
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c = b - phi * (b - a)
    d = a + phi * (b - a)
    fc, fd = at(c), at(d)
    for _ in range(25):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - phi * (b - a)
            fc = at(c)
        else:
            a, c, fc = c, d, fd
            d = a + phi * (b - a)
            fd = at(d)
    alpha = c if fc < fd else d
    cand = x + alpha * direction
    if at(alpha) + 1e-15 < base:
        return cand
    return x


def projected_angles() -> np.ndarray:
    from common import MENU

    ang = np.zeros((N_SET, 2), dtype=np.float64)
    for i in range(N_SET):
        x, _y, z = MENU[i]
        n = math.hypot(x, z)
        if n < 1e-12:
            ang[i] = np.array([1.0, 0.0])  # y -> angle 0
        else:
            ang[i] = np.array([x / n, z / n])
    return ang


def chol_from_psi(psi: np.ndarray) -> np.ndarray:
    x = np.zeros(10, dtype=np.float64)
    # L column 0 = psi, which is x[0], x[1], x[3], x[6] in the lower-tri packing
    # packing: (0,0), (1,0),(1,1), (2,0),(2,1),(2,2), (3,0),(3,1),(3,2),(3,3)
    x[0] = psi[0]
    x[1] = psi[1]
    x[3] = psi[2]
    x[6] = psi[3]
    return x


def rebit_seesaw() -> tuple[float, np.ndarray]:
    from common import MENU

    ang = projected_angles()
    s2 = 1.0 / math.sqrt(2.0)
    starts_psi = [
        np.array([0.0, s2, -s2, 0.0]),
        np.array([0.0, s2, -s2, 0.0]),
        np.array([0.0, s2, -s2, 0.0]),
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.array([s2, 0.0, 0.0, s2]),
    ]
    start_angles = [
        ang.copy(),
        np.tile(np.array([1.0, 0.0]), (N_SET, 1)),
        np.tile(np.array([0.0, 1.0]), (N_SET, 1)),
        ang.copy(),
        ang.copy(),
    ]
    best_L = math.inf
    best_C = None
    best_rho = None
    for psi, ang0 in zip(starts_psi, start_angles):
        x = chol_from_psi(psi)
        ra = ang0.copy()
        rb = ang0.copy()
        last = math.inf
        for _round in range(SEESAW_ROUNDS):
            rho = unpack_chol(x)
            G = G_of_rho(rho)
            ra, rb = optimize_effects(G, ra, rb)
            for _ in range(STATE_ITERS):
                x2 = state_step(x, ra, rb)
                if np.allclose(x2, x):
                    x = x2
                    break
                x = x2
            L = loss_of_rho(unpack_chol(x), ra, rb)
            if last - L < 1e-15:
                last = L
                break
            last = L
        C = correlators_from_effects(G_of_rho(unpack_chol(x)), ra, rb)
        L = loss_from_C(C)
        if L < best_L:
            best_L = L
            best_C = C
            best_rho = unpack_chol(x)
    return float(best_L), best_C, best_rho


def product_seesaw() -> tuple[float, np.ndarray]:
    def run(f0, g0):
        f = f0.copy()
        g = g0.copy()
        for _ in range(200):
            for a in range(N_SET):
                den = float(np.dot(g, g))
                num = float(np.dot(T_MAT[a], g))
                f[a] = 0.0 if den < 1e-18 else float(np.clip(num / den, -1.0, 1.0))
            for b in range(N_SET):
                den = float(np.dot(f, f))
                num = float(np.dot(T_MAT[:, b], f))
                g[b] = 0.0 if den < 1e-18 else float(np.clip(num / den, -1.0, 1.0))
        return loss_from_C(np.outer(f, g)), np.outer(f, g)

    # top singular vector by power iteration on T^T T
    v = np.ones(N_SET, dtype=np.float64)
    v /= np.linalg.norm(v)
    for _ in range(200):
        v = T_MAT.T @ (T_MAT @ v)
        n = np.linalg.norm(v)
        if n < 1e-18:
            break
        v = v / n
    if v[int(np.argmax(np.abs(v)))] < 0:
        v = -v
    Tv = T_MAT @ v
    sigma = float(np.linalg.norm(Tv))
    # rank-1 target ≈ ± sigma v u, with u = Tv/sigma
    if sigma < 1e-12:
        f_svd = np.ones(N_SET)
        g_svd = np.ones(N_SET)
    else:
        u = Tv / sigma
        scale = math.sqrt(sigma)
        # sign: T is negative semidefinite on its range, so f and g opposite signs
        f_svd = np.clip(-scale * v, -1.0, 1.0)
        g_svd = np.clip(scale * u, -1.0, 1.0)
    L1, C1 = run(f_svd, g_svd)
    L2, C2 = run(np.ones(N_SET), np.ones(N_SET))
    if L1 <= L2:
        return float(L1), C1
    return float(L2), C2


def shannon_mi_from_weights(pair_index: np.ndarray, weights: np.ndarray) -> float:
    """I(alpha; beta) for a distribution on joint vertices."""
    w = np.asarray(weights, dtype=np.float64)
    w = np.clip(w, 0.0, None)
    s = w.sum()
    if s <= 0:
        return 0.0
    w = w / s
    # accumulate joint 32x32 sparsely
    joint = np.zeros((32, 32), dtype=np.float64)
    for idx, wt in zip(pair_index, w):
        if wt <= 0:
            continue
        alpha = int(idx) // 32
        beta = int(idx) % 32
        joint[alpha, beta] += wt

    def H(p):
        p = p[p > 0]
        return float(-np.sum(p * np.log(p)))

    return H(joint.sum(axis=1)) + H(joint.sum(axis=0)) - H(joint.ravel())


def run_search() -> dict:
    C = vertex_correlators()
    L1, i1 = best_M1(C)
    L2, i2a, i2b, t2 = best_M2(C)
    w = frank_wolfe(C)
    curve = elimination_curve(C, w)
    env = lower_envelope(L1, L2, curve)
    Lr, Cr, rho_r = rebit_seesaw()
    Lp, Cp = product_seesaw()
    return {
        "L_M1": L1,
        "M1_vertex": i1,
        "L_M2": L2,
        "M2": [i2a, i2b, t2],
        "fw_support": int(np.sum(w > WEIGHT_TOL)),
        "envelope": env,
        "curve_sizes": [(int(M), float(L)) for M, L, _ in curve],
        "L_rebit": float(Lr),
        "C_rebit": Cr,
        "rho_rebit": rho_r,
        "L_product": float(Lp),
        "C_product": Cp,
        "fw_weights_support": (
            np.flatnonzero(w > WEIGHT_TOL),
            w[w > WEIGHT_TOL] / np.sum(w[w > WEIGHT_TOL]),
        ),
    }
