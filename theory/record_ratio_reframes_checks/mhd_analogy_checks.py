#!/usr/bin/env python3
"""T76 MHD-analogy checks. Criteria are PREREG_MHD.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
HALF_PI = base.HALF_PI


class Report:
    def __init__(self):
        self.fails = []
        self.lines = []

    def add(self, name, ok, detail):
        self.lines.append(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
        if not ok:
            self.fails.append(name)

    def dump(self):
        for line in self.lines:
            print(line)
        print(f"FAILS {len(self.fails)}")


def j_at(theta, q, w):
    f = base.functionals("ANT", 0.0, theta, 0.0)
    return 1.0 * f["I"] + q * f["P_D"] + w * f["L"]


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    thetas = base.theta_grid()

    lin_ok = True
    lin_bits = []
    max_d2 = 0.0
    for th in (0.0, base.PI / 4.0, HALF_PI):
        for q in (0.25, 0.5, 0.75, 1.0):
            d2 = j_at(th, q + 0.25, 1.0) - 2.0 * j_at(th, q, 1.0) + j_at(th, q - 0.25, 1.0)
            max_d2 = max(max_d2, abs(d2))
            ok = abs(d2) < 1e-9
            lin_ok = lin_ok and ok
            if not ok:
                lin_bits.append(f"theta={th:.6f} q={q} d2={d2:.3e}")
    rep.add("H1-lin", lin_ok, f"max_abs_second_diff={max_d2:.3e}" + ((" | " + " | ".join(lin_bits)) if lin_bits else ""))

    joint_ok = True
    joint_bits = []
    stars = {}
    for w in (0.5, 1.0, 2.0, 4.0, 10.0):
        for q in (0.0, 0.25, 0.5, 0.75, 1.0, 2.0):
            m = base.minimize("ANT", 0.0, 0.0, 1.0, q, w, thetas)
            stars[(w, q)] = m
        j0 = stars[(w, 0.0)]["J"]
        for q in (0.0, 0.25, 0.5, 0.75, 1.0, 2.0):
            gap = stars[(w, q)]["J"] - j0
            ok = gap >= -1e-9
            joint_ok = joint_ok and ok
            if not ok:
                joint_bits.append(f"w={w} q={q} gap={gap:.6e}")
    rep.add(
        "H1-joint",
        joint_ok,
        "all J*(q) sit at or above J*(0)" if joint_ok else " | ".join(joint_bits),
    )

    d_half = stars[(1.0, 0.5)]["J"] - stars[(1.0, 0.0)]["J"]
    d_ten = stars[(10.0, 0.5)]["J"] - stars[(10.0, 0.0)]["J"]
    m_ten_0 = stars[(10.0, 0.0)]
    m_ten_h = stars[(10.0, 0.5)]
    half_ok = (
        d_half > 0.01
        and m_ten_0["unique"]
        and m_ten_h["unique"]
        and abs(m_ten_0["theta"]) <= 1e-12
        and abs(m_ten_h["theta"]) <= 1e-12
        and abs(d_ten) < 1e-9
    )
    rep.add(
        "H1-half",
        half_ok,
        f"gap_w1={d_half:.6f} gap_w10={d_ten:.3e} "
        f"theta10_q0={m_ten_0['theta']:.6f} n0={len(m_ten_0['tied'])} "
        f"theta10_q05={m_ten_h['theta']:.6f} n05={len(m_ten_h['tied'])}",
    )

    m0 = stars[(1.0, 0.0)]
    m1 = stars[(1.0, 1.0)]
    split = abs(m0["theta"] - m1["theta"])
    split_ok = m0["unique"] and m1["unique"] and abs(m0["theta"] - HALF_PI) <= 1e-12 and abs(m1["theta"]) <= 1e-12 and split >= 1.0
    rep.add(
        "H2-split",
        split_ok,
        f"theta_q0={m0['theta']:.6f} n0={len(m0['tied'])} theta_q1={m1['theta']:.6f} n1={len(m1['tied'])} gap={split:.6f}",
    )

    m2 = stars[(2.0, 0.0)]
    below_ok = m2["unique"] and abs(m2["theta"] - HALF_PI) <= 1e-12
    rep.add("H2-below", below_ok, f"theta={m2['theta']:.6f} n_tie={len(m2['tied'])}")

    lam_hi = base.minimize("ANT", 0.0, 0.0, 1.0, 0.7, 1.0, thetas)
    lam_lo = base.minimize("ANT", 0.0, 0.0, 1.0, 0.7, 0.5, thetas)
    move_ok = (
        lam_hi["unique"]
        and abs(lam_hi["theta"]) <= 1e-12
        and lam_lo["unique"]
        and abs(lam_lo["theta"] - HALF_PI) <= 1e-12
    )
    rep.add(
        "H2-move",
        move_ok,
        f"w1_theta={lam_hi['theta']:.6f} n1={len(lam_hi['tied'])} "
        f"w05_theta={lam_lo['theta']:.6f} n05={len(lam_lo['tied'])}",
    )

    rep.dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
