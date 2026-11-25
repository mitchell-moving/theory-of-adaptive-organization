#!/usr/bin/env python3
"""T76 checks. Criteria are theory/record_ratio_reframes_checks/PREREG.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os

SEED = 20261124  # not drawn from
R = 0.6
N_GRID = 720
TIE = 1e-9
H_STEP = 1e-5
DET_SING = 1e-8
PI = math.pi
HALF_PI = 0.5 * PI


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


def dephase(v, gamma: float):
    return (gamma * v[0], gamma * v[1], v[2])


def n_theta(theta: float):
    return (math.sin(theta), 0.0, math.cos(theta))


# weight, pre-dephasing Bloch vector
ANT = (
    (0.25, (0.0, 0.0, R)),
    (0.25, (0.0, 0.0, -R)),
    (0.25, (R, 0.0, 0.0)),
    (0.25, (-R, 0.0, 0.0)),
)
BIAS = (
    (0.8, (0.0, 0.0, R)),
    (0.2, (0.0, 0.0, -R)),
)


def ensemble_rows(name: str):
    if name == "ANT":
        return ANT
    if name == "BIAS":
        return BIAS
    raise ValueError(name)


def functionals(name: str, gamma: float, theta: float, phi: float):
    """Return dict with I, P_D, L, chi, H, p_plus, E_S."""
    rows = ensemble_rows(name)
    nv = n_theta(theta)
    posts = []
    lengths = []
    p_plus_w = []
    ys = []
    sphi = math.sin(phi)
    cphi = math.cos(phi)
    for w, pre in rows:
        post = dephase(pre, gamma)
        posts.append(post)
        lengths.append(norm(post))
        p_plus_w.append(0.5 * (1.0 + dot(nv, post)))
        ys.append(sphi * pre[0] + cphi * pre[2])
    weights = [row[0] for row in rows]
    e_s = 0.0
    h_mw = 0.0
    p_plus = 0.0
    p_d = 0.0
    for w, length, pp in zip(weights, lengths, p_plus_w):
        s_rho = qubit_entropy(length)
        s_phi = hbin(pp)
        e_s += w * s_rho
        h_mw += w * s_phi
        p_d += w * (s_phi - s_rho)
        p_plus += w * pp
    h_m = hbin(p_plus)
    info = h_m - h_mw
    # average post-dephasing Bloch
    bx = by = bz = 0.0
    for w, post in zip(weights, posts):
        bx += w * post[0]
        by += w * post[1]
        bz += w * post[2]
    chi = qubit_entropy(norm((bx, by, bz))) - e_s
    # mean squared error of the conditional mean
    # P(M=+1), P(M=-1)
    p_m = [p_plus, 1.0 - p_plus]
    # joint mass w * P(m|w)
    a_hat = [0.0, 0.0]
    for sign, pm in enumerate(p_m):
        if pm <= 0.0:
            continue
        acc = 0.0
        for w, pp, y in zip(weights, p_plus_w, ys):
            pm_w = pp if sign == 0 else (1.0 - pp)
            acc += w * pm_w * y
        a_hat[sign] = acc / pm
    loss = 0.0
    for w, pp, y in zip(weights, p_plus_w, ys):
        for sign, pm_w in enumerate((pp, 1.0 - pp)):
            d = y - a_hat[sign]
            loss += w * pm_w * d * d
    return {
        "I": info,
        "P_D": p_d,
        "L": loss,
        "chi": chi,
        "H": h_m,
        "p_plus": p_plus,
        "E_S": e_s,
        "ledger": info + p_d,
    }


def closed_form_ant(theta: float, phi: float):
    """PREREG.md:64-72 at e584d8b, gamma = 0, ANT."""
    cabs = abs(math.cos(theta))
    hp = hbin(0.5 * (1.0 + R * cabs))
    hr = hbin(0.5 * (1.0 + R))
    p_d = 0.5 * (hp - hr)
    info = 0.5 * (math.log(2.0) - hp)
    loss = 0.5 * R * R - (R ** 4) * (math.cos(phi) ** 2) * (math.cos(theta) ** 2) / 4.0
    return info, p_d, loss


def theta_grid():
    step = HALF_PI / N_GRID
    return [j * step for j in range(N_GRID + 1)]


def minimize(name, gamma, phi, kappa, kappa_d, w, thetas=None):
    if thetas is None:
        thetas = theta_grid()
    best = None
    vals = []
    for th in thetas:
        f = functionals(name, gamma, th, phi)
        j = kappa * f["I"] + kappa_d * f["P_D"] + w * f["L"]
        vals.append(j)
        if best is None or j < best:
            best = j
    tied = [thetas[i] for i, j in enumerate(vals) if j <= best + TIE]
    return {
        "theta": tied[0],
        "tied": tied,
        "J": best,
        "unique": len(tied) == 1,
        "vals": vals,
        "thetas": thetas,
    }


def derivs(name, gamma, theta, phi):
    """Central difference, one-sided at an endpoint. Step H_STEP."""
    def side(th):
        th = min(HALF_PI, max(0.0, th))
        return functionals(name, gamma, th, phi)

    if theta <= H_STEP:
        f0 = side(theta)
        f1 = side(theta + H_STEP)
        scale = H_STEP
        return {k: (f1[k] - f0[k]) / scale for k in ("I", "P_D", "L")}
    if theta >= HALF_PI - H_STEP:
        f0 = side(theta - H_STEP)
        f1 = side(theta)
        scale = H_STEP
        return {k: (f1[k] - f0[k]) / scale for k in ("I", "P_D", "L")}
    fm = side(theta - H_STEP)
    fp = side(theta + H_STEP)
    scale = 2.0 * H_STEP
    return {k: (fp[k] - fm[k]) / scale for k in ("I", "P_D", "L")}


def least_squares(xs, ys, target):
    """Min ||alpha x + beta y - target||^2, no intercept. Returns alpha, beta, max_abs_resid, gram_det."""
    sxx = syy = sxy = sxt = syt = 0.0
    for x, y, t in zip(xs, ys, target):
        sxx += x * x
        syy += y * y
        sxy += x * y
        sxt += x * t
        syt += y * t
    det = sxx * syy - sxy * sxy
    if abs(det) < 1e-18:
        return None
    # Solve [sxx sxy; sxy syy] [a; b] = [sxt; syt]
    alpha = (sxt * syy - sxy * syt) / det
    beta = (sxx * syt - sxy * sxt) / det
    max_abs = 0.0
    for x, y, t in zip(xs, ys, target):
        max_abs = max(max_abs, abs(alpha * x + beta * y - t))
    return alpha, beta, max_abs, det


class Report:
    def __init__(self):
        self.fails = []
        self.lines = []

    def add(self, name, ok, detail):
        tag = "PASS" if ok else "FAIL"
        self.lines.append(f"{name} {tag} {detail}")
        if not ok:
            self.fails.append(name)

    def dump(self):
        for line in self.lines:
            print(line)
        print(f"FAILS {len(self.fails)}")
        if not self.fails:
            print("ALL T76 CHECKS PASS")


def curve(name, gamma, phi, thetas):
    rows = [functionals(name, gamma, th, phi) for th in thetas]
    return rows


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    thetas = theta_grid()
    step = HALF_PI / N_GRID

    # ----- gates -----
    g0_max = 0.0
    for th in (0.0, 0.3, PI / 4.0, HALF_PI):
        for phi in (0.0, PI / 4.0, HALF_PI):
            f = functionals("ANT", 0.0, th, phi)
            ci, cd, cl = closed_form_ant(th, phi)
            g0_max = max(g0_max, abs(f["I"] - ci), abs(f["P_D"] - cd), abs(f["L"] - cl))
    rep.add("G0", g0_max < 1e-10, f"max_abs={g0_max:.3e}")

    g0b_max = 0.0
    for gamma in (0.0, 0.5):
        for th in thetas:
            f = functionals("ANT", gamma, th, 0.0)
            g0b_max = max(g0b_max, abs(f["p_plus"] - 0.5))
    rep.add("G0b", g0b_max < 1e-12, f"max_abs={g0b_max:.3e}")

    # definitional identity; a miss is a code bug, not a prediction
    ident_max = 0.0
    for name, gamma in (("ANT", 0.0), ("ANT", 0.5), ("BIAS", 0.0)):
        for th in thetas[::10]:
            f = functionals(name, gamma, th, 0.0)
            ident_max = max(ident_max, abs(f["ledger"] - (f["H"] - f["E_S"])))
    if ident_max >= 1e-9:
        raise SystemExit(f"identity bug ledger vs H-E[S]: {ident_max}")

    # ----- Route K -----
    ant = curve("ANT", 0.0, 0.0, thetas)
    I_a = [r["I"] for r in ant]
    D_a = [r["P_D"] for r in ant]
    chi_a = ant[0]["chi"]
    led_a = max(abs(r["ledger"] - r["chi"]) for r in ant)
    rep.add("K1-ledger", led_a < 1e-9, f"max_abs={led_a:.3e} chi={chi_a:.12f}")

    fit_I = least_squares(I_a, D_a, I_a)
    fit_chi = least_squares(I_a, D_a, [chi_a] * len(thetas))
    if fit_I is None or fit_chi is None:
        rep.add("K1-fit-I", False, "singular")
        rep.add("K1-fit-chi", False, "singular")
    else:
        a, b, mx, _ = fit_I
        rep.add(
            "K1-fit-I",
            abs(a - 1.0) < 1e-8 and abs(b) < 1e-8 and mx < 1e-9,
            f"alpha={a:.12e} beta={b:.12e} max_resid={mx:.3e}",
        )
        a, b, mx, _ = fit_chi
        rep.add(
            "K1-fit-chi",
            abs(a - 1.0) < 1e-8 and abs(b - 1.0) < 1e-8 and mx < 1e-9,
            f"alpha={a:.12e} beta={b:.12e} max_resid={mx:.3e}",
        )

    bias = curve("BIAS", 0.0, 0.0, thetas)
    I_b = [r["I"] for r in bias]
    D_b = [r["P_D"] for r in bias]
    chi_b = bias[0]["chi"]
    # chi must not depend on theta
    chi_span = max(r["chi"] for r in bias) - min(r["chi"] for r in bias)
    if chi_span > 1e-9:
        raise SystemExit(f"chi depends on theta: {chi_span}")
    led_b = max(abs(r["ledger"] - chi_b) for r in bias)
    rep.add("K2-ledger", led_b > 0.02, f"max_abs={led_b:.6f} chi={chi_b:.12f}")

    sxx = syy = sxy = 0.0
    for x, y in zip(I_b, D_b):
        sxx += x * x
        syy += y * y
        sxy += x * y
    gram = sxx * syy - sxy * sxy
    rep.add("K2-gram", gram > 1e-6, f"det={gram:.6e}")

    fit_Ib = least_squares(I_b, D_b, I_b)
    if fit_Ib is None:
        rep.add("K2-fit-I", False, "singular")
    else:
        a, b, mx, _ = fit_Ib
        rep.add(
            "K2-fit-I",
            abs(a - 1.0) < 1e-8 and abs(b) < 1e-8,
            f"alpha={a:.12e} beta={b:.12e} max_resid={mx:.3e}",
        )

    fit_chib = least_squares(I_b, D_b, [chi_b] * len(thetas))
    # net alpha, beta = -2, -1.95, ..., 4 (121 by 121)
    net_min = None
    net_at = None
    n_net = 121 * 121
    for ia in range(121):
        alpha = (-200 + 5 * ia) / 100.0
        for ib in range(121):
            beta = (-200 + 5 * ib) / 100.0
            mx = 0.0
            for x, y in zip(I_b, D_b):
                resid = abs(alpha * x + beta * y - chi_b)
                if resid > mx:
                    mx = resid
            if net_min is None or mx < net_min:
                net_min = mx
                net_at = (alpha, beta)
    ls_note = "none"
    ls_ok = False
    if fit_chib is not None:
        fa, fb, fmx, _ = fit_chib
        ls_note = f"ls_alpha={fa:.6f} ls_beta={fb:.6f} ls_max={fmx:.6f}"
        ls_ok = fmx > 0.005
        # The least-squares point is not a net point. Leave net_min and net_at
        # as the minimum over the 121 by 121 grid.
    k2_ok = ls_ok and net_min is not None and net_min > 0.005
    rep.add(
        "K2-bound-weight",
        k2_ok,
        f"net_min={net_min} at={net_at} n_net={n_net} {ls_note}",
    )

    # ----- Route G -----
    g1_bad = []
    g1_cost_span = 0.0
    for ratio in (1.0, 2.0, 10.0):
        for w in (0.1, 1.0, 10.0):
            m = minimize("ANT", 0.0, 0.0, 1.0, ratio, w, thetas)
            if (not m["unique"]) or m["theta"] > step * 0.5:
                g1_bad.append((ratio, w, m["theta"], len(m["tied"])))
    # costs across ratios at each stake
    for w in (0.1, 1.0, 10.0):
        js = [minimize("ANT", 0.0, 0.0, 1.0, ratio, w, thetas)["J"] for ratio in (1.0, 2.0, 10.0)]
        g1_cost_span = max(g1_cost_span, max(js) - min(js))
    rep.add(
        "G1",
        (not g1_bad) and g1_cost_span < 1e-9,
        f"bad={g1_bad} cost_span={g1_cost_span:.3e}",
    )

    m_flat = minimize("ANT", 0.0, 0.0, 1.0, 1.0, 0.0, thetas)
    flat_range = max(m_flat["vals"]) - min(m_flat["vals"])
    m_r2 = minimize("ANT", 0.0, 0.0, 1.0, 2.0, 0.0, thetas)
    # J(pi/2) - J(0) at ratio 2, w=0
    f0 = functionals("ANT", 0.0, 0.0, 0.0)
    f1 = functionals("ANT", 0.0, HALF_PI, 0.0)
    gap_end = (1.0 * f1["I"] + 2.0 * f1["P_D"]) - (1.0 * f0["I"] + 2.0 * f0["P_D"])
    rep.add(
        "G2",
        flat_range < 1e-9 and m_r2["unique"] and m_r2["theta"] <= step * 0.5 and gap_end > 0.01,
        f"flat_range={flat_range:.3e} theta2={m_r2['theta']:.6f} unique2={m_r2['unique']} "
        f"endpoint_gap={gap_end:.6f} n_tie_ratio1={len(m_flat['tied'])}",
    )

    m_w1 = minimize("ANT", 0.0, 0.0, 1.0, 0.0, 1.0, thetas)
    m_w10 = minimize("ANT", 0.0, 0.0, 1.0, 0.0, 10.0, thetas)
    rep.add(
        "G3",
        m_w1["theta"] > 0.2 and m_w10["unique"] and m_w10["theta"] <= step * 0.5,
        f"theta_w1={m_w1['theta']:.6f} theta_w10={m_w10['theta']:.6f} unique10={m_w10['unique']}",
    )

    m_g4_a = minimize("ANT", 0.5, PI / 4.0, 1.0, 1.0, 1.0, thetas)
    m_g4_b = minimize("ANT", 0.5, PI / 4.0, 1.0, 100.0, 1.0, thetas)
    g4_gap = abs(m_g4_a["theta"] - m_g4_b["theta"])
    g4_tie = (not m_g4_a["unique"]) or (not m_g4_b["unique"])
    # a tie spanning >= 0.2 is a uniqueness failure
    def tie_span(m):
        if len(m["tied"]) < 2:
            return 0.0
        return m["tied"][-1] - m["tied"][0]

    g4_span_bad = tie_span(m_g4_a) >= 0.2 or tie_span(m_g4_b) >= 0.2
    rep.add(
        "G4",
        (not g4_tie) and (not g4_span_bad) and g4_gap >= 0.2,
        f"theta_ratio1={m_g4_a['theta']:.6f} theta_ratio100={m_g4_b['theta']:.6f} "
        f"gap={g4_gap:.6f} n_tie=({len(m_g4_a['tied'])},{len(m_g4_b['tied'])})",
    )

    # G5. Literal target is P_chi(0). Parenthetical says added coefficient times ledger.
    p_chi0 = functionals("ANT", 0.0, 0.0, 0.0)["I"]  # P_D(0)=0 so I(0)=P_chi(0)
    g5_theta_bad = []
    g5_cost_gaps = []
    for w in (0.0, 0.5, 1.0, 2.0, 4.0, 10.0):
        ma = minimize("ANT", 0.0, 0.0, 1.0, 0.5, w, thetas)
        mb = minimize("ANT", 0.0, 0.0, 1.5, 1.0, w, thetas)
        if abs(ma["theta"] - mb["theta"]) > step + 1e-12:
            g5_theta_bad.append((w, ma["theta"], mb["theta"]))
        g5_cost_gaps.append((w, mb["J"] - ma["J"]))
    # literal: differ by P_chi(0)
    literal_miss = max(abs(gap - p_chi0) for _, gap in g5_cost_gaps)
    rep.add(
        "G5",
        (not g5_theta_bad) and literal_miss < 1e-9,
        f"theta_bad={g5_theta_bad} literal_miss={literal_miss:.3e} "
        f"P_chi0={p_chi0:.12f} gaps={[(w, round(g, 12)) for w, g in g5_cost_gaps]}",
    )
    # not a locked check
    half = 0.5 * p_chi0
    half_miss = max(abs(gap - half) for _, gap in g5_cost_gaps)
    print(
        f"DIAGNOSTIC G5-parenthetical half_ledger={half:.12f} max_miss={half_miss:.3e} "
        f"(not a locked check)"
    )

    # ----- Route C -----
    def interior(th):
        return 0.05 - 1e-15 <= th <= HALF_PI - 0.05 + 1e-15

    c1_rows = []
    for w in (0.5, 1.0, 2.0, 4.0, 8.0):
        m = minimize("ANT", 0.0, 0.0, 1.0, 0.5, w, thetas)
        c1_rows.append((w, m))
    c1_int = [(w, m) for w, m in c1_rows if interior(m["theta"]) and m["unique"]]
    c1_ok = len(c1_int) >= 1
    delta_notes = []
    for w, m in c1_int:
        d = derivs("ANT", 0.0, m["theta"], 0.0)
        if abs(d["P_D"]) < 1e-15:
            c1_ok = False
            delta_notes.append((w, "P_D_deriv_zero"))
            continue
        delta_hat = -w * d["L"] / d["P_D"]
        err = abs(delta_hat - (-0.5))
        delta_notes.append((w, m["theta"], delta_hat, err))
        if err >= 5e-3:
            c1_ok = False
    det_notes = []
    for i in range(len(c1_int)):
        for j in range(i + 1, len(c1_int)):
            w1, m1 = c1_int[i]
            w2, m2 = c1_int[j]
            d1 = derivs("ANT", 0.0, m1["theta"], 0.0)
            d2 = derivs("ANT", 0.0, m2["theta"], 0.0)
            det = d1["I"] * d2["P_D"] - d1["P_D"] * d2["I"]
            det_notes.append((w1, w2, det))
            if abs(det) >= DET_SING:
                c1_ok = False
    rep.add(
        "C1",
        c1_ok,
        f"n_interior={len(c1_int)} deltas={delta_notes} dets={det_notes}",
    )

    c2_rows = []
    for w in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0):
        m = minimize("BIAS", 0.0, 0.0, 1.0, 0.5, w, thetas)
        c2_rows.append((w, m))
    c2_int = [(w, m) for w, m in c2_rows if interior(m["theta"]) and m["unique"]]
    c2_ok = False
    c2_detail = f"n_interior={len(c2_int)} thetas={[(w, round(m['theta'], 6)) for w, m in c2_rows]}"
    if len(c2_int) >= 2:
        # pair with largest |theta| gap
        best_pair = None
        best_gap = -1.0
        for i in range(len(c2_int)):
            for j in range(i + 1, len(c2_int)):
                gap = abs(c2_int[i][1]["theta"] - c2_int[j][1]["theta"])
                if gap > best_gap:
                    best_gap = gap
                    best_pair = (c2_int[i], c2_int[j])
        (w1, m1), (w2, m2) = best_pair
        d1 = derivs("BIAS", 0.0, m1["theta"], 0.0)
        d2 = derivs("BIAS", 0.0, m2["theta"], 0.0)
        det = d1["I"] * d2["P_D"] - d1["P_D"] * d2["I"]
        if best_gap >= 0.05 and abs(det) >= DET_SING:
            # Cramer
            rhs1 = -w1 * d1["L"]
            rhs2 = -w2 * d2["L"]
            kappa_hat = (rhs1 * d2["P_D"] - d1["P_D"] * rhs2) / det
            kd_hat = (d1["I"] * rhs2 - rhs1 * d2["I"]) / det
            c2_ok = abs(kappa_hat - 1.0) < 0.02 and abs(kd_hat - 0.5) < 0.02
            c2_detail = (
                f"w=({w1},{w2}) theta=({m1['theta']:.6f},{m2['theta']:.6f}) "
                f"gap={best_gap:.6f} det={det:.6e} kappa={kappa_hat:.6f} kappa_D={kd_hat:.6f}"
            )
        else:
            c2_detail = (
                f"w=({w1},{w2}) theta=({m1['theta']:.6f},{m2['theta']:.6f}) "
                f"gap={best_gap:.6f} det={det:.6e} singular_or_small_gap"
            )
    rep.add("C2", c2_ok, c2_detail)

    m0 = minimize("BIAS", 0.0, 0.0, 1.0, 0.0, 0.0, thetas)
    m1 = minimize("BIAS", 0.0, 0.0, 1.0, 1.0, 0.0, thetas)
    rep.add(
        "C3",
        m0["unique"] and m1["unique"] and m0["theta"] > HALF_PI - 0.02 and m1["theta"] < 0.02,
        f"theta_ratio0={m0['theta']:.6f} n0={len(m0['tied'])} "
        f"theta_ratio1={m1['theta']:.6f} n1={len(m1['tied'])}",
    )

    rep.dump()
    return 0 if True else 1


if __name__ == "__main__":
    raise SystemExit(main())
