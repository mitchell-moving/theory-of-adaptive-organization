"""Contestants for the tilted menu, as locked in PREREG_4.md.

Gmin is a Bloch product. Gmax is the maximal tensor product. R4a is its own
four-point phase space. R4c is the real-plane Born rule. The shared-bit
mixture is a sensitivity, not a lock contestant. No random seed.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize

S2 = math.sqrt(2.0)
S3 = math.sqrt(3.0)
MENU = np.array(
    [
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
        [1.0 / S2, 0.0, 1.0 / S2],
        [-1.0 / S2, 0.0, 1.0 / S2],
        [1.0 / S3, 1.0 / S3, 1.0 / S3],
    ],
    dtype=np.float64,
)
T = -(MENU @ MENU.T)
X = np.array([[0.0, 1.0], [1.0, 0.0]])
Z = np.diag([1.0, -1.0])
Y = np.array([[0.0, -1j], [1j, 0.0]])


def pauli(u: np.ndarray) -> np.ndarray:
    return u[0] * X.astype(complex) + u[1] * Y + u[2] * Z.astype(complex)


def singlet() -> np.ndarray:
    s = np.zeros(4, dtype=np.complex128)
    s[1] = 1.0 / S2
    s[2] = -1.0 / S2
    return s


def mean_loss(C: np.ndarray) -> float:
    d = C - T
    return float(np.sum(d * d) / 25.0)


def project_ball(v: np.ndarray) -> np.ndarray:
    nrm = float(np.linalg.norm(v))
    if nrm <= 1.0:
        return v
    return v / nrm


def product_pauli_rank() -> int:
    """Real rank of the 16 product Paulis. They span every Hermitian 4x4."""
    eye = np.eye(2, dtype=np.complex128)
    factors = (eye, X.astype(complex), Y, Z.astype(complex))
    rows = []
    for left in factors:
        for right in factors:
            op = np.kron(left, right)
            rows.append(np.concatenate([np.real(op).ravel(), np.imag(op).ravel()]))
    return int(np.linalg.matrix_rank(np.stack(rows), tol=1e-10))


def g_model(eta: float = 0.0) -> tuple[float, float, np.ndarray]:
    """Two-qubit singlet plus a coordinate eta outside the product Paulis.

    The scored correlators are product Paulis. The joint effect (1+eta)/2
    is computed and is not scored.
    """
    psi = singlet()
    rho = np.outer(psi, psi.conj())
    C = np.zeros((5, 5))
    for a in range(5):
        for b in range(5):
            op = np.kron(pauli(MENU[a]), pauli(MENU[b]))
            C[a, b] = float(np.real(np.trace(rho @ op)))
    joint = 0.5 * (1.0 + float(eta))
    return mean_loss(C), joint, C


def yy_entry(C: np.ndarray) -> float:
    """Scored correlator of the last menu direction, from this model's C."""
    return float(C[4, 4])


def _rank1_loss(n: np.ndarray, m: np.ndarray) -> float:
    return mean_loss(np.outer(MENU @ project_ball(n), MENU @ project_ball(m)))


def _gmin_starts() -> list[np.ndarray]:
    starts = []
    for i in range(3):
        for s in (1.0, -1.0):
            for j in range(3):
                for t in (1.0, -1.0):
                    x = np.zeros(6)
                    x[i] = s
                    x[3 + j] = t
                    starts.append(x)
    frame = MENU.T @ MENU
    _, axes = np.linalg.eigh(frame)
    axis = axes[:, -1]
    x = np.zeros(6)
    x[:3] = axis
    x[3:] = -axis
    starts.append(x)
    x = np.zeros(6)
    x[:3] = axis
    x[3:] = axis
    starts.append(x)
    return starts


def gmin_fit() -> tuple[float, np.ndarray]:
    """Minimal tensor product: correlators (n·u)(m·v), Bloch vectors in the ball."""

    def objective(x: np.ndarray) -> float:
        return _rank1_loss(x[:3], x[3:])

    best = math.inf
    best_x = np.zeros(6)
    for x0 in _gmin_starts():
        res = minimize(objective, x0, method="Powell", options={"maxiter": 80, "ftol": 1e-16})
        if float(res.fun) < best:
            best = float(res.fun)
            best_x = np.array(res.x, dtype=np.float64)
    n = project_ball(best_x[:3])
    m = project_ball(best_x[3:])
    C = np.outer(MENU @ n, MENU @ m)
    return mean_loss(C), C


def product_effect_min() -> float:
    """Smallest product-effect probability of the singlet, over the menu."""
    psi = singlet()
    rho = np.outer(psi, psi.conj())
    worst = 0.0
    eye = np.eye(2, dtype=np.complex128)
    for a in range(5):
        for b in range(5):
            for sa in (1.0, -1.0):
                for sb in (1.0, -1.0):
                    ea = 0.5 * (eye + sa * pauli(MENU[a]))
                    eb = 0.5 * (eye + sb * pauli(MENU[b]))
                    pr = float(np.real(np.trace(rho @ np.kron(ea, eb))))
                    if pr < worst:
                        worst = pr
    return worst


def gmax_fit() -> tuple[float, float, np.ndarray]:
    """Membership check for the maximal tensor product, not a fit.

    If every product-effect probability is at least -1e-9 and every target
    entry is in [-1, 1], the target itself is an admissible behavior.
    """
    worst = product_effect_min()
    inside = worst >= -1e-9 and float(np.max(np.abs(T))) <= 1.0 + 1e-9
    if inside:
        return mean_loss(T), worst, T.copy()
    return 1.0, worst, np.zeros((5, 5))


def r4a_fit(iters: int = 500) -> tuple[float, int, np.ndarray]:
    """Four ontic states per wing. Outcomes are functions of (q, p)."""

    def outcomes(q: int, psign: float) -> np.ndarray:
        out = np.empty(5)
        for i, u in enumerate(MENU):
            planar = float(u[0]) * (1.0 if q == 0 else -1.0) + float(u[2])
            if abs(planar) < 1e-12:
                out[i] = psign
            else:
                out[i] = psign * (1.0 if planar >= 0.0 else -1.0)
        return out

    rows = [outcomes(q, psign) for q in (0, 1) for psign in (1.0, -1.0)]
    behaviors = np.stack(
        [np.outer(rows[i], rows[j]).ravel() for i in range(4) for j in range(4)]
    )
    weights = np.full(16, 1.0 / 16.0)
    target = T.ravel()
    for k in range(iters):
        flat = weights @ behaviors
        grad = (flat - target) @ behaviors.T
        i = int(np.argmin(grad))
        gamma = 2.0 / (k + 2.0)
        weights *= 1.0 - gamma
        weights[i] += gamma
    C = (weights @ behaviors).reshape(5, 5)
    return mean_loss(C), int(np.sum(weights > 1e-8)), C


def _real_encode(psi: np.ndarray) -> np.ndarray:
    return np.concatenate([np.real(psi), np.imag(psi)]).astype(np.float64)


def _j_mul(v: np.ndarray) -> np.ndarray:
    n = v.size // 2
    out = np.empty_like(v)
    out[:n] = -v[n:]
    out[n:] = v[:n]
    return out


def _plus_spinor(u: np.ndarray) -> np.ndarray:
    x, y, z = (float(u[0]), float(u[1]), float(u[2]))
    if z > -1.0 + 1e-14:
        den = math.sqrt(2.0 * (1.0 + z))
        return np.array(
            [math.sqrt((1.0 + z) / 2.0), (x + 1j * y) / den],
            dtype=np.complex128,
        )
    return np.array([0.0 + 0.0j, 1.0 + 0.0j], dtype=np.complex128)


def _born_real_plane(phi: np.ndarray, psi_r: np.ndarray) -> float:
    pr = _real_encode(phi)
    nrm = math.sqrt(float(np.dot(pr, pr)))
    pr = pr / nrm
    return float(np.dot(pr, psi_r) ** 2 + np.dot(_j_mul(pr), psi_r) ** 2)


def r4c_real(psi: np.ndarray) -> tuple[float, np.ndarray]:
    """Real-plane Born rule on the encoded singlet. Not the complex modulus."""
    psi_r = _real_encode(psi)
    psi_r = psi_r / np.linalg.norm(psi_r)
    C = np.zeros((5, 5))
    for a in range(5):
        for b in range(5):
            acc = 0.0
            for sa in (1.0, -1.0):
                for sb in (1.0, -1.0):
                    phi = np.kron(_plus_spinor(sa * MENU[a]), _plus_spinor(sb * MENU[b]))
                    acc += sa * sb * _born_real_plane(phi, psi_r)
            C[a, b] = acc
    return mean_loss(C), C


def information_of_protocol(rho: np.ndarray) -> tuple[float, float, float, float]:
    """Mutual information of settings with a one-point record, and Holevo.

    The joint is the product of the uniform setting distribution and one
    record state. Holevo is the average eigenvalue entropy minus that
    state's eigenvalue entropy.
    """
    settings = np.full(25, 1.0 / 25.0)
    record = np.array([1.0])
    joint = np.outer(settings, record).ravel()

    def entropy(p: np.ndarray) -> float:
        kept = p[p > 0.0]
        return float(-np.sum(kept * np.log(kept)))

    def clean(x: float) -> float:
        x = float(x)
        return 0.0 if x == 0.0 else x

    mutual = entropy(settings) + entropy(record) - entropy(joint)
    ev = np.clip(np.linalg.eigvalsh(rho).real, 0.0, None)
    ev = ev[ev > 1e-15]
    if ev.size == 0:
        state_s = 0.0
    else:
        ev = ev / float(np.sum(ev))
        state_s = float(-np.sum(ev * np.log(ev)))
    # one prepared state: the average is that state's entropy
    average_s = state_s
    return clean(mutual), clean(average_s - state_s), clean(average_s), clean(state_s)


def shared_bit_loss() -> float:
    """Real singlet, one shared bit. Not a lock contestant.

    Weight sqrt(2/3) on sharp xz projections. The rest reads y as +I on one
    wing and -I on the other.
    """
    psi = singlet()
    rho = np.outer(psi, psi.conj())
    p = math.sqrt(2.0 / 3.0)

    def proj_angle(u: np.ndarray) -> float:
        return math.atan2(float(u[2]), float(u[0]))

    def planar(u: np.ndarray) -> np.ndarray:
        ang = proj_angle(u)
        return math.cos(ang) * X + math.sin(ang) * Z

    def corr(ops_a, ops_b) -> np.ndarray:
        C = np.zeros((5, 5))
        for a in range(5):
            for b in range(5):
                C[a, b] = float(np.real(np.trace(rho @ np.kron(ops_a[a], ops_b[b]))))
        return C

    ops = [planar(MENU[i]) for i in range(5)]
    C1 = corr(ops, ops)
    ops_a = list(ops)
    ops_b = list(ops)
    ops_a[4] = np.eye(2)
    ops_b[4] = -np.eye(2)
    C2 = corr(ops_a, ops_b)
    return mean_loss(p * C1 + (1.0 - p) * C2)


def pair(jc: float, fc: bool, jx: float, fx: bool) -> str:
    if fc and not fx:
        return "WIN"
    if fx and not fc:
        return "LOSE"
    if not fc and not fx:
        return "EXCLUDED"
    delta = jx - jc
    band = 0.01 * max(jc, jx) + 1e-12
    if delta > band:
        return "WIN"
    if delta < -band:
        return "LOSE"
    return "TIE"


def cell(labels: list[str]) -> str:
    used = [z for z in labels if z != "EXCLUDED"]
    if any(z == "LOSE" for z in used):
        return "LOSE"
    if used and all(z == "WIN" for z in used):
        return "WIN"
    return "TIE"
