"""Exact worst-question error of a local hidden-variable record. See RUN_LOG.md and DEVIATIONS.md."""
from __future__ import annotations

import hashlib
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import LinearConstraint, Bounds, linprog, milp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / "composite_contest_checks"))

from common import K_C, K_G, K_GMAX, K_GMIN, K_R, K_R4C, N_SET, T_FLAT, fmt  # noqa: E402

LAMBDAS = (0.0, 1e-4, 1e-3, 1e-2, 1e-1)
EPSILONS = (0.0, 0.02, 0.04, 0.05, 0.1, 0.12, 0.25, 1.0)
CHECK = (0.0, 0.02, 0.04)
HEAD = (0.05, 0.1)
WEIGHT_TOL = 1e-10


def vertices() -> np.ndarray:
    signs = np.ones((32, N_SET), dtype=np.float64)
    for k in range(32):
        for i in range(N_SET):
            if (k >> i) & 1:
                signs[k, i] = -1.0
    C = np.empty((1024, 25), dtype=np.float64)
    p = 0
    for a in range(32):
        for b in range(32):
            C[p] = np.outer(signs[a], signs[b]).ravel()
            p += 1
    return C


def minimax(C: np.ndarray) -> tuple[float, int, float]:
    n = C.shape[0]
    cost = np.zeros(n + 1)
    cost[-1] = 1.0
    CT = np.ascontiguousarray(C.T)
    ones = np.ones((25, 1))
    A_ub = np.vstack([np.hstack([CT, -ones]), np.hstack([-CT, -ones])])
    b_ub = np.concatenate([T_FLAT, -T_FLAT])
    A_eq = np.zeros((1, n + 1))
    A_eq[0, :n] = 1.0
    res = linprog(
        cost, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=np.array([1.0]),
        bounds=[(0.0, None)] * n + [(0.0, None)], method="highs",
        options={"presolve": True, "time_limit": 60.0},
    )
    if not res.success:
        raise RuntimeError(res.message)
    s = float(res.x[-1])
    # smallest support at this error: the cost charges K, and a basic solution need not be smallest
    c_z = np.concatenate([np.zeros(n), np.ones(n)])
    A1 = np.hstack([CT, np.zeros((25, n))])
    A2 = np.hstack([-CT, np.zeros((25, n))])
    Ap = np.hstack([np.eye(n), -np.eye(n)])
    A_card = np.vstack([A1, A2, Ap])
    b_card = np.concatenate([T_FLAT + s, -T_FLAT + s, np.zeros(n)])
    A_sum = np.zeros((1, 2 * n))
    A_sum[0, :n] = 1.0
    card = milp(
        c_z,
        integrality=np.concatenate([np.zeros(n), np.ones(n)]),
        bounds=Bounds(np.zeros(2 * n), np.ones(2 * n)),
        constraints=[
            LinearConstraint(A_card, -np.inf, b_card),
            LinearConstraint(A_sum, np.array([1.0]), np.array([1.0])),
        ],
        options={"time_limit": 60.0},
    )
    if not card.success:
        raise RuntimeError(card.message)
    z = card.x[n:]
    p = np.clip(card.x[:n], 0.0, None)
    err = float(np.max(np.abs(p @ C - T_FLAT)))
    k = int(np.sum(z > 0.5))
    return err * err, k, s


def pair(jc, fc, jx, fx) -> str:
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


def agg(labels: list[str]) -> str:
    n = len(labels)
    nw = sum(z == "WIN" for z in labels)
    nl = sum(z == "LOSE" for z in labels)
    nt = sum(z == "TIE" for z in labels)
    if nw / n >= 0.90 and nl == 0:
        return "WIN"
    if nl / n >= 0.50:
        return "LOSE"
    if nt / n >= 0.90:
        return "TIE"
    return "MIXED"


def J(feas: bool, K: float, L: float, lam: float) -> float:
    if not feas:
        return math.inf
    return lam * math.log(K) + L


def main() -> int:
    C = vertices()
    Lh, Kh, s = minimax(C)
    floor = (3.0 - 2.0 * math.sqrt(2.0)) / 4.0
    lines = [
        f"classical_s {fmt(s)} L_inf {fmt(Lh)} K {Kh} floor {fmt(floor)}",
        f"rebit_floor {fmt(1.0 / 9.0)} product_floor {fmt(0.25)}",
    ]
    q = {k: True for k in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6")}
    pos, zero, head = [], [], []
    for lam in LAMBDAS:
        for eps in EPSILONS:
            feas_h = Lh <= eps + 1e-12
            # floors decide R and the product theories; see DEVIATIONS.md
            feas_r = (1.0 / 9.0) <= eps + 1e-12
            feas_p = 0.25 <= eps + 1e-12
            # optimistic losses: the floors themselves
            Lr = 1.0 / 9.0
            Lp = 0.25
            jc = J(True, K_C, 0.0, lam)
            specs = [
                ("C", True, float(K_C), 0.0),
                ("R", feas_r, float(K_R), Lr),
                ("H", feas_h, float(Kh), Lh),
                ("G", True, float(K_G), 0.0),
                ("R4a", feas_h, float(Kh), Lh),
                ("R4c", True, float(K_R4C), 0.0),
                ("Gmin", feas_p, float(K_GMIN), Lp),
                ("Gmax", feas_p, float(K_GMAX), Lp),
            ]
            labels = []
            body = [f"cell lam {fmt(lam)} eps {fmt(eps)}"]
            for name, feas, K, L in specs:
                lab = "SELF" if name == "C" else pair(jc, True, J(feas, K, L, lam), feas)
                if name != "C":
                    labels.append(lab)
                body.append(f"  {name} feas {int(feas)} K {fmt(K)} L {fmt(L)} J {fmt(J(feas, K, L, lam))} {lab}")
            lab_cell = cell(labels)
            body[0] += " " + lab_cell
            lines.extend(body)
            (pos if lam > 0 else zero).append(lab_cell)
            if lam > 0 and eps in HEAD:
                head.append(lab_cell)
            if lam > 0 and eps in CHECK and lab_cell != "WIN":
                q["Q1"] = False
            if lam == 0.0 and eps in CHECK and lab_cell != "TIE":
                q["Q2"] = False
            if eps in (0.0, 0.02, 0.04, 0.05, 0.1) and feas_r:
                q["Q3"] = False
            if eps in CHECK and feas_h:
                q["Q4"] = False
            if eps < 0.25 - 1e-15 and feas_p:
                q["Q5"] = False
            if lam > 0:
                for Kbig in (K_G, K_R4C):
                    if pair(jc, True, J(True, Kbig, 0.0, lam), True) != "WIN":
                        q["Q6"] = False
    lines.append(f"aggregate lambda>0 {agg(pos)} n {len(pos)} " + " ".join(pos))
    lines.append(f"headline {agg(head)} n {len(head)} " + " ".join(head))
    lines.append(f"aggregate lambda0 {agg(zero)} n {len(zero)} " + " ".join(zero))
    for name in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6"):
        lines.append(f"{name} {'PASS' if q[name] else 'FAIL'}")
    lines.append("Q7 headline reported above; no locked label")
    # the classical loss must respect the Bell floor on the max absolute error
    ok_floor = Lh + 1e-8 >= floor
    lines.append(f"classical_above_floor {'PASS' if ok_floor else 'FAIL'} L {fmt(Lh)} floor {fmt(floor)}")
    text = "\n".join(lines) + "\n"
    (HERE / "decisions.out").write_text(text, encoding="utf-8", newline="\n")
    digest = hashlib.sha256((HERE / "decisions.out").read_bytes()).hexdigest()
    (HERE / "SHA256SUMS").write_text(digest + "  decisions.out\n", encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if ok_floor and all(q.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
