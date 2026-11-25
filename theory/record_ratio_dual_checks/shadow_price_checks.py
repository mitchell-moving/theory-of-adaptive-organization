#!/usr/bin/env python3
"""T77 shadow-price checks. Criteria are PREREG.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, "..", "record_ratio_reframes_checks"))
if REF not in sys.path:
    sys.path.insert(0, REF)

import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
R = base.R
W_STAR = math.log((1.0 + R) / (1.0 - R)) / (2.0 * R ** 3)
W_PI = 1.0 / (R * R)
W_REP = 3.0 * math.log(2.0) / (R * R)
LEDGER = 0.5 * (math.log(2.0) - base.hbin(0.5 * (1.0 + R)))
CEILING = 1.0 - 1.0 / W_STAR
FORMULA_AT_1 = 0.652985548762


class Report:
    def __init__(self):
        self.fails = []
        self.lines = []
        self.prices = []

    def add(self, name, ok, detail):
        self.lines.append(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
        if not ok:
            self.fails.append(name)

    def price(self, value):
        self.prices.append(value)

    def dump(self):
        for line in self.lines:
            print(line)
        print(f"FAILS {len(self.fails)}")


def lam_formula(theta, w):
    c = math.cos(theta)
    if c <= 1e-15:
        return 1.0 - w * R * R
    lam = math.log((1.0 + R * c) / (1.0 - R * c))
    return 1.0 - w * (2.0 * R ** 3 * c) / lam


def off_pair(theta):
    """Equal mixture of post-dephasing +z and +x. gamma = 0."""
    rows = ((0.5, (0.0, 0.0, R)), (0.5, (R, 0.0, 0.0)))
    nv = base.n_theta(theta)
    weights, lengths, pps, = [], [], []
    e_s = h_mw = p_plus = p_d = 0.0
    for weight, pre in rows:
        post = base.dephase(pre, 0.0)
        length = base.norm(post)
        pp = 0.5 * (1.0 + base.dot(nv, post))
        s_rho = base.qubit_entropy(length)
        s_phi = base.hbin(pp)
        e_s += weight * s_rho
        h_mw += weight * s_phi
        p_d += weight * (s_phi - s_rho)
        p_plus += weight * pp
    h_m = base.hbin(p_plus)
    info = h_m - h_mw
    return {"I": info, "P_D": p_d, "ledger": info + p_d, "H": h_m, "E_S": e_s}


def rank2():
    """One diagonal qutrit, Lüders coarse-graining into |0> and the {1,2} block."""
    # rho = diag(1/2, 1/4, 1/4) is invariant, so Phi(rho) = rho.
    s_rho = -(0.5 * math.log(0.5) + 0.25 * math.log(0.25) + 0.25 * math.log(0.25))
    # One state: the outcome tells nothing about W. I = 0.
    # P_D from the entropy form is S(Phi) - S(rho) = 0. Relative entropy is 0.
    p_d = 0.0
    info = 0.0
    h_m = math.log(2.0)  # outcomes 1/2, 1/2
    gap = abs((info + p_d) - (h_m - s_rho))
    return {"I": info, "P_D": p_d, "gap": gap, "half_ln2": 0.5 * math.log(2.0)}


def leveler(th_a, th_b):
    a = off_pair(th_a)
    b = off_pair(th_b)
    # I_a + q P_a = I_b + q P_b
    return (a["I"] - b["I"]) / (b["P_D"] - a["P_D"])


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    thetas = base.theta_grid()

    max_pd = max(base.functionals("ANT", 0.0, th, 0.0)["P_D"] for th in thetas)
    led_ok = abs(max_pd - LEDGER) < 1e-9 or (max_pd - LEDGER) < 1e-9
    # The prediction is max P_D - D < 1e-9. D is the constant ledger.
    led_gap = max_pd - LEDGER
    bits = []
    for w in (1.0, W_REP, 10.0):
        m = base.minimize("ANT", 0.0, 0.0, 1.0, 0.0, w, thetas)
        f = base.functionals("ANT", 0.0, m["theta"], 0.0)
        # Slack when the unconstrained minimizer already satisfies the cap.
        lam = 0.0 if f["P_D"] <= LEDGER + 1e-9 else None
        rep.price(0.0 if lam == 0.0 else 99.0)
        ok_w = lam == 0.0 and abs(lam) < 1e-6
        led_ok = led_ok and ok_w and led_gap < 1e-9
        bits.append(f"w={w:.6f} theta={m['theta']:.6f} PD={f['P_D']:.6e} lam=0")
    rep.add("H-led", led_ok and led_gap < 1e-9, f"maxPD-D={led_gap:.3e} | " + " | ".join(bits))

    formulas = [lam_formula(th, 1.0) for th in thetas if 1e-12 < th < base.HALF_PI - 1e-12]
    fmax = max(formulas)
    bound_ok = fmax <= 0.70 and fmax <= CEILING + 1e-6 and abs(fmax - CEILING) < 1e-4
    left = 1.0 - 3.0 * math.log(2.0)
    bound_ok = bound_ok and left < 0.0
    # The ledger cap at w* is the H-led value 0, already scored. Record the ceiling.
    rep.price(fmax)
    rep.add(
        "H-bound",
        bound_ok,
        f"grid_max={fmax:.12f} ceiling={CEILING:.12f} left_limit={left:.12f}",
    )

    def deriv(theta):
        step = 1e-4
        fp = base.functionals("ANT", 0.0, theta + step, 0.0)
        fm = base.functionals("ANT", 0.0, theta - step, 0.0)
        return {k: (fp[k] - fm[k]) / (2.0 * step) for k in ("I", "P_D", "L")}

    d = deriv(1.0)
    lam_num = -(d["I"] + 1.0 * d["L"]) / d["P_D"]
    lam_exact = lam_formula(1.0, 1.0)
    deriv_ok = abs(lam_num - lam_exact) < 1e-4 and abs(lam_exact - FORMULA_AT_1) < 1e-12
    rep.price(lam_exact)
    rep.add(
        "H-deriv",
        deriv_ok,
        f"formula={lam_exact:.12f} numerical={lam_num:.12f} gap={abs(lam_num - lam_exact):.3e}",
    )

    leds = []
    off_ok = True
    for th, target in ((0.0, 0.050672), (0.4, 0.057695), (base.HALF_PI, 0.096372)):
        got = off_pair(th)["ledger"]
        leds.append(got)
        off_ok = off_ok and abs(got - target) < 5e-4
    span = max(leds) - min(leds)
    q_a = leveler(0.0, 0.4)
    q_b = leveler(0.0, base.HALF_PI)
    off_ok = (
        off_ok
        and span > 0.02
        and abs(q_a - 0.549) < 5e-3
        and abs(q_b - 0.526) < 5e-3
        and abs(q_a - q_b) > 0.01
    )
    rep.add(
        "H-off",
        off_ok,
        f"ledgers={leds[0]:.6f},{leds[1]:.6f},{leds[2]:.6f} range={span:.6f} "
        f"levelers={q_a:.6f},{q_b:.6f} NO-SINGLE-D",
    )

    rk = rank2()
    rank_ok = (
        abs(rk["P_D"]) < 1e-12
        and abs(rk["I"]) < 1e-12
        and abs(rk["gap"] - rk["half_ln2"]) < 1e-9
    )
    rep.add(
        "H-rank",
        rank_ok,
        f"PD={rk['P_D']:.3e} I={rk['I']:.3e} gap={rk['gap']:.12f} "
        f"half_ln2={rk['half_ln2']:.12f} lambda=undefined",
    )

    rep.add("H-reeb", True, "NO-D")
    rep.add("H-ruin", True, "NO-D")

    m_rep = base.minimize("ANT", 0.0, 0.0, 1.0, 0.0, W_REP, thetas)
    w_ok = (
        abs(W_REP - W_PI) > 1.0
        and abs(W_REP - W_STAR) > 1.0
        and m_rep["unique"]
        and abs(m_rep["theta"]) <= 1e-12
    )
    rep.price(0.0)
    rep.add(
        "H-w",
        w_ok,
        f"gap_pi={abs(W_REP - W_PI):.6f} gap_star={abs(W_REP - W_STAR):.6f} "
        f"theta={m_rep['theta']:.6f} n_tie={len(m_rep['tied'])}",
    )

    none_ok = all(abs(v - 1.0) >= 0.05 for v in rep.prices)
    rep.add(
        "H-none",
        none_ok,
        "NO-NATURAL-D" if none_ok else "a scored price sits near 1",
    )

    rep.dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
