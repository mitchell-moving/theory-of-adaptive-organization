"""Apply the locked decision rule. Imports search results; does not retune the grid."""
from __future__ import annotations

import math

import numpy as np

from common import (
    EPSILONS,
    K_C,
    K_G,
    K_GMAX,
    K_GMIN,
    K_R,
    K_R4C,
    LAMBDAS,
    T_MAT,
    chsh_S,
    fmt,
    loss_from_C,
    mean_outcome_mi_from_C,
)
from search import choose_model


def tol(j1: float, j2: float) -> float:
    return 0.01 * max(j1, j2) + 1e-12


def pair_label(j_c: float, feas_c: bool, j_x: float, feas_x: bool) -> str:
    if (not feas_c) and (not feas_x):
        return "EXCLUDED"
    if feas_c and not feas_x:
        return "WIN"
    if feas_x and not feas_c:
        return "LOSE"
    delta = j_x - j_c
    band = tol(j_c, j_x)
    if delta > band:
        return "WIN"
    if delta < -band:
        return "LOSE"
    return "TIE"


def cell_label(labels: list[str]) -> str:
    used = [z for z in labels if z != "EXCLUDED"]
    if not used:
        return "EXCLUDED"
    if any(z == "LOSE" for z in used):
        return "LOSE"
    if all(z == "WIN" for z in used):
        return "WIN"
    return "TIE"


def aggregate(labels: list[str]) -> str:
    if not labels:
        return "EMPTY"
    n = len(labels)
    nW = sum(z == "WIN" for z in labels)
    nL = sum(z == "LOSE" for z in labels)
    nT = sum(z == "TIE" for z in labels)
    if nW / n >= 0.90 and nL == 0:
        return "WIN"
    if nL / n >= 0.50:
        return "LOSE"
    if nT / n >= 0.90:
        return "TIE"
    return "MIXED"


def J_of(feas: bool, K: float, L: float, lam: float) -> float:
    if not feas:
        return math.inf
    return lam * math.log(K) + L


def _entropy(evals: np.ndarray) -> float:
    h = 0.0
    for wi in evals:
        if wi > 1e-15:
            h -= float(wi) * math.log(float(wi))
    return h


def wing_mi(rho: np.ndarray) -> float:
    """Quantum mutual information S(A)+S(B)-S(AB) for a two-qubit real state."""
    rho = np.asarray(rho, dtype=np.float64)
    sab = _entropy(np.clip(np.linalg.eigvalsh(rho), 0.0, None))
    ra = np.zeros((2, 2), dtype=np.float64)
    rb = np.zeros((2, 2), dtype=np.float64)
    for i in range(2):
        for k in range(2):
            for j in range(2):
                ra[i, k] += rho[2 * i + j, 2 * k + j]
                rb[j, k] += rho[2 * i + j, 2 * i + k]
    sa = _entropy(np.clip(np.linalg.eigvalsh(ra), 0.0, None))
    sb = _entropy(np.clip(np.linalg.eigvalsh(rb), 0.0, None))
    return sa + sb - sab


def singlet_C() -> np.ndarray:
    return T_MAT.copy()


def run_grid(search: dict) -> tuple[str, list[dict]]:
    env = search["envelope"]
    Lr = float(search["L_rebit"])
    Lp = float(search["L_product"])
    Cr = search["C_rebit"]
    rows = []
    lines = []
    lines.append("SINGLET GRID")
    lines.append(
        f"L_rebit {fmt(Lr)} chsh_rebit {fmt(chsh_S(Cr))} "
        f"L_product {fmt(Lp)} L_M1 {fmt(search['L_M1'])} L_M2 {fmt(search['L_M2'])} "
        f"fw_support {search['fw_support']}"
    )
    lines.append("envelope " + " ".join(f"{M}:{fmt(L)}" for M, L in env))
    I_out_C = mean_outcome_mi_from_C(singlet_C())
    I_wings_C = 2.0 * math.log(2.0)
    I_wings_R = wing_mi(search["rho_rebit"])
    lines.append(
        f"info C I_A6 {fmt(0.0)} I_wings {fmt(I_wings_C)} I_out {fmt(I_out_C)} K_hv inf K {K_C}"
    )
    lines.append(
        f"info R I_A6 {fmt(0.0)} I_wings {fmt(I_wings_R)} I_out {fmt(mean_outcome_mi_from_C(Cr))} "
        f"K_hv inf K {K_R}"
    )
    for lam in LAMBDAS:
        for eps in EPSILONS:
            feas_h, Mh, Lh, _Jh = choose_model(env, lam, eps)
            # same model for R4a
            contestants = []
            # name, feas, K, L, J
            specs = [
                ("C", True, K_C, 0.0),
                ("R", Lr <= eps + 1e-15, K_R, Lr),
                ("H", feas_h, float(Mh), Lh),
                ("G", True, K_G, 0.0),
                ("R4a", feas_h, float(Mh), Lh),
                ("R4c", True, K_R4C, 0.0),
                ("Gmin", Lp <= eps + 1e-15, K_GMIN, Lp),
                ("Gmax", Lp <= eps + 1e-15, K_GMAX, Lp),
            ]
            j_c = J_of(True, K_C, 0.0, lam)
            labels = []
            detail = []
            for name, feas, K, L in specs:
                J = J_of(feas, K, L, lam)
                if name == "C":
                    lab = "SELF"
                else:
                    lab = pair_label(j_c, True, J, feas)
                    labels.append(lab)
                detail.append((name, feas, K, L, J, lab))
            lab_cell = cell_label(labels)
            lines.append(
                f"cell lam {fmt(lam)} eps {fmt(eps)} {lab_cell}"
            )
            for name, feas, K, L, J, lab in detail:
                lines.append(
                    f"  {name} feas {int(feas)} K {fmt(K)} L {fmt(L)} J {fmt(J)} {lab}"
                )
            rows.append(
                {
                    "lam": lam,
                    "eps": eps,
                    "label": lab_cell,
                    "pairs": labels,
                }
            )
    # aggregates
    pos = [r["label"] for r in rows if r["lam"] > 0]
    tight = [r["label"] for r in rows if r["lam"] > 0 and r["eps"] == 0.0]
    loose = [r["label"] for r in rows if r["lam"] > 0 and r["eps"] >= 0.05 - 1e-15]
    zero = [r["label"] for r in rows if r["lam"] == 0.0]
    lines.append(f"aggregate lambda>0 {aggregate(pos)} n {len(pos)}")
    lines.append(f"aggregate tight {aggregate(tight)} n {len(tight)} " + " ".join(tight))
    lines.append(f"aggregate loose {aggregate(loose)} n {len(loose)} " + " ".join(loose))
    lines.append(f"aggregate lambda0 {aggregate(zero)} n {len(zero)} " + " ".join(zero))
    # P1: every tight cell WIN
    p1 = all(z == "WIN" for z in tight)
    lines.append(f"P1 {'PASS' if p1 else 'FAIL'}")
    # P2 H infeasible at eps 0 and 1e-3: look at H feas flag via J inf
    # re-derive from lines is messy; recompute
    p2 = True
    p3 = True
    p4 = True
    p5 = True
    for lam in LAMBDAS:
        for eps in EPSILONS:
            feas_h, Mh, Lh, _ = choose_model(env, lam, eps)
            if eps <= 1e-3 + 1e-15 and feas_h:
                p2 = False
            if eps <= 1e-2 + 1e-15 and (Lr <= eps + 1e-15 or Lp <= eps + 1e-15):
                p3 = False
            # P4: C beats R4c and G whenever both feasible, lambda>0
            if lam > 0:
                j_c = J_of(True, K_C, 0.0, lam)
                for K in (K_R4C, K_G):
                    j_x = J_of(True, K, 0.0, lam)
                    if pair_label(j_c, True, j_x, True) != "WIN":
                        p4 = False
            if lam == 0.0:
                # find the row
                pass
    for r in rows:
        if r["lam"] == 0.0 and r["label"] != "TIE":
            p5 = False
    lines.append(f"P2 {'PASS' if p2 else 'FAIL'}")
    lines.append(f"P3 {'PASS' if p3 else 'FAIL'}")
    lines.append(f"P4 {'PASS' if p4 else 'FAIL'}")
    lines.append(f"P5 {'PASS' if p5 else 'FAIL'}")
    lines.append("P6 I_A6 is 0 by the protocol for every singlet-grid contestant")
    lines.append("P7 orbit dimension is 1 for every single-state loss-0 protocol")
    lines.append("P8 loose cells reported above; no locked label")
    return "\n".join(lines) + "\n", rows


def classical_control() -> str:
    """H1: classical axis. Loss 0 at K=6 for H and K=16 for C."""
    # Explicit check: product spin coherent state measured on its own axis is deterministic.
    def spinor(n):
        x, y, z = n
        if z > -1.0 + 1e-14:
            den = math.sqrt(2.0 * (1.0 + z))
            return np.array([math.sqrt((1.0 + z) / 2.0), (x + 1j * y) / den], dtype=np.complex128)
        return np.array([0.0, 1.0], dtype=np.complex128)

    poles = {
        "px": np.array([1.0, 0.0, 0.0]),
        "mx": np.array([-1.0, 0.0, 0.0]),
        "py": np.array([0.0, 1.0, 0.0]),
        "my": np.array([0.0, -1.0, 0.0]),
        "pz": np.array([0.0, 0.0, 1.0]),
        "mz": np.array([0.0, 0.0, -1.0]),
    }
    axes = {
        "x": np.array([1.0, 0.0, 0.0]),
        "y": np.array([0.0, 1.0, 0.0]),
        "z": np.array([0.0, 0.0, 1.0]),
    }
    # Pauli expectation of |n><n| along u is n·u. For a scored pair |n·u|=1, outcome is deterministic.
    max_err = 0.0
    for n in poles.values():
        psi = spinor(n)
        rho = np.outer(psi, psi.conj())
        for u in axes.values():
            if abs(float(np.dot(n, u))) < 0.5:
                continue
            op = u[0] * np.array([[0, 1], [1, 0]], dtype=np.complex128)
            op = op + u[1] * np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
            op = op + u[2] * np.array([[1, 0], [0, -1]], dtype=np.complex128)
            ev = float(np.real(np.trace(rho @ op)))
            max_err = max(max_err, abs(abs(ev) - 1.0))
    # Holevo of the six product states
    rhos = []
    for n in poles.values():
        psi = np.kron(spinor(n), spinor(n))
        rhos.append(np.outer(psi, psi.conj()))
    avg = sum(rhos) / 6.0
    w = np.clip(np.linalg.eigvalsh(avg).real, 0.0, None)
    chi = float(-sum(wi * math.log(wi) for wi in w if wi > 1e-15))
    lines = []
    lines.append("CLASSICAL-DIRECTION CONTROL")
    lines.append(f"quantum_axis_defect {fmt(max_err)}")
    lines.append(f"L_H {fmt(0.0)} K_H {fmt(6.0)} L_C {fmt(0.0)} K_C {fmt(16.0)}")
    lines.append(f"holevo {fmt(chi)} ln4 {fmt(2*math.log(2))} ln6 {fmt(math.log(6))}")
    h1_ok = True
    for lam in LAMBDAS:
        j_c = 0.0 if lam == 0 else lam * math.log(16.0)
        j_h = 0.0 if lam == 0 else lam * math.log(6.0)
        # both feasible, L=0
        lab = pair_label(j_c, True, j_h, True)
        expect = "TIE" if lam == 0 else "LOSE"
        if lab != expect:
            h1_ok = False
        lines.append(f"H1 lam {fmt(lam)} {lab} expect {expect} Jc {fmt(j_c)} Jh {fmt(j_h)}")
    lines.append(f"H1 {'PASS' if h1_ok else 'FAIL'}")
    # bound chi <= ln 4
    lines.append(f"holevo_le_ln4 {'PASS' if chi <= 2*math.log(2) + 1e-9 else 'FAIL'}")
    lines.append(f"holevo_lt_ln6 {'PASS' if chi < math.log(6) - 1e-9 else 'FAIL'}")
    return "\n".join(lines) + "\n"
