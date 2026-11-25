"""Shared definitions for the composite contest. Locked by theory/composite-contest-2026-11-24/PREREG.md."""
from __future__ import annotations

import math

import numpy as np

# One thread. Callers also set the environment before import when they can.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    import os
    os.environ.setdefault(_k, "1")

MENU = np.array(
    [
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [1.0 / math.sqrt(2.0), 0.0, 1.0 / math.sqrt(2.0)],
        [-1.0 / math.sqrt(2.0), 0.0, 1.0 / math.sqrt(2.0)],
    ],
    dtype=np.float64,
)
N_SET = 5
T_MAT = -(MENU @ MENU.T)
T_FLAT = T_MAT.reshape(-1)

LAMBDAS = (0.0, 1e-4, 1e-3, 1e-2, 1e-1)
EPSILONS = (0.0, 1e-3, 1e-2, 0.05, 0.2, 1.0)

K_C = 16
K_R = 10
K_G = 17
K_R4C = 36
K_GMIN = 16
K_GMAX = 16

FW_ITERS = 8000
REOPT_ITERS = 4000
WEIGHT_TOL = 1e-10
SEESAW_ROUNDS = 40
STATE_ITERS = 2000
PRODUCT_ROUNDS = 200

X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.float64)
Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.float64)
PAULI_Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)


def pauli(u: np.ndarray) -> np.ndarray:
    return u[0] * PAULI_X + u[1] * PAULI_Y + u[2] * PAULI_Z


def loss_from_C(C: np.ndarray) -> float:
    D = np.asarray(C, dtype=np.float64) - T_MAT
    return float(np.dot(D.ravel(), D.ravel()) / 25.0)


def chsh_S(C: np.ndarray) -> float:
    # settings: z=0, x=1, y=2, p=3, m=4
    return float(C[0, 3] + C[0, 4] + C[1, 3] - C[1, 4])


def binary_mi_from_joint(p: np.ndarray) -> float:
    """Shannon I(A;B) in nats from a 2x2 joint. Rows A, cols B, order (+,+), (+,-), (-,+), (-,-)."""
    p = np.asarray(p, dtype=np.float64)
    p = np.clip(p, 0.0, None)
    s = p.sum()
    if s <= 0.0:
        return 0.0
    p = p / s

    def H(probs):
        h = 0.0
        for q in probs:
            if q > 0.0:
                h -= q * math.log(q)
        return h

    pa = p.sum(axis=1)
    pb = p.sum(axis=0)
    return H(pa) + H(pb) - H(p.ravel())


def outcome_mi_zero_marginal(C: float) -> float:
    """I(A;B) when E[ab]=C and both marginals are uniform."""
    c = float(np.clip(C, -1.0, 1.0))
    p = 0.5 * (1.0 + c)  # P(A=B)
    # joint: P(++)=P(--)=(1+C)/4, P(+-)=P(-+)=(1-C)/4
    pp = (1.0 + c) / 4.0
    pm = (1.0 - c) / 4.0
    joint = np.array([[pp, pm], [pm, pp]])
    return binary_mi_from_joint(joint)


def mean_outcome_mi_from_C(C: np.ndarray) -> float:
    total = 0.0
    for a in range(N_SET):
        for b in range(N_SET):
            total += outcome_mi_zero_marginal(C[a, b])
    return total / 25.0


def project_simplex(v: np.ndarray) -> np.ndarray:
    """Euclidean projection onto {p >= 0, sum p = 1}. Deterministic."""
    v = np.asarray(v, dtype=np.float64)
    n = v.size
    u = np.sort(v)[::-1]
    css = np.cumsum(u)
    rho = 0
    for i in range(n):
        if u[i] * (i + 1) > (css[i] - 1.0):
            rho = i
    theta = (css[rho] - 1.0) / (rho + 1.0)
    w = v - theta
    np.maximum(w, 0.0, out=w)
    s = w.sum()
    if s <= 0.0:
        w[:] = 1.0 / n
        return w
    if abs(s - 1.0) > 1e-15:
        w /= s
    return w


def fmt(x) -> str:
    if isinstance(x, str):
        return x
    if x is None:
        return "none"
    xf = float(x)
    if math.isinf(xf):
        return "inf" if xf > 0 else "-inf"
    if math.isnan(xf):
        return "nan"
    return format(xf, ".16e")
