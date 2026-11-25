#!/usr/bin/env python3
"""T76 repeated-record asymptote. Criteria are PREREG_REPEAT_ASYMPTOTE.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fixed_point_checks as fp
import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
N = 256
HALF_PI = base.HALF_PI
PI4 = 0.25 * base.PI


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


def class_entropy(n: int) -> tuple[float, float]:
    """I(W;K) and H(C|K) at theta=0. C is {+z, -z, x-pair}."""
    ps = (0.5 * (1.0 + base.R), 0.5 * (1.0 - base.R), 0.5)
    priors = (0.25, 0.25, 0.5)
    pmfs = [[fp.binom_pmf(n, k, p) for k in range(n + 1)] for p in ps]
    h_c = 0.0
    h_k = 0.0
    hk_w = 0.0
    for prior, pmf in zip(priors, pmfs):
        ent = 0.0
        for prob in pmf:
            if prob > 0.0:
                ent -= prob * math.log(prob)
        hk_w += prior * ent
    for k in range(n + 1):
        masses = [prior * pmf[k] for prior, pmf in zip(priors, pmfs)]
        mass = sum(masses)
        if mass <= 0.0:
            continue
        h_k -= mass * math.log(mass)
        ent = 0.0
        for piece in masses:
            if piece > 0.0:
                share = piece / mass
                ent -= share * math.log(share)
        h_c += mass * ent
    # four labels: the x-pair's internal ln 2 is not in H(C|K)
    info = h_k - hk_w
    return info, h_c


def j_at(theta, q, w, n, cache):
    key = (round(theta, 12), n)
    if key not in cache:
        cache[key] = fp.repeated("ANT", 0.0, theta, 0.0, n)
    rec = cache[key]
    return rec["I"] + q * n * rec["P_D"] + w * rec["L"], rec


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    thetas = base.theta_grid()
    cache = {}

    info16 = fp.repeated("ANT", 0.0, 0.0, 0.0, 16)["I"]
    _info_c, h_c = class_entropy(16)
    target = 1.5 * math.log(2.0)
    gap = abs(info16 - (target - h_c))
    class_ok = gap < 1e-9 and h_c > 0.2
    rep.add("R-class", class_ok, f"I16={info16:.6f} H={h_c:.6f} identity_gap={gap:.3e}")

    def cell(q, w):
        return fp.minimize_rep("ANT", 0.0, 0.0, 1.0, q, w, N, thetas)

    low = cell(0.0, 1.0)
    j_c, _ = j_at(PI4, 0.0, 1.0, N, cache)
    j_0, _ = j_at(0.0, 0.0, 1.0, N, cache)
    j_e, _ = j_at(HALF_PI, 0.0, 1.0, N, cache)
    low_ok = (
        low["unique"]
        and abs(low["theta"] - PI4) <= 0.15
        and j_c < j_0 - 0.05
        and j_c < j_e - 0.05
    )
    rep.add(
        "R-low",
        low_ok,
        f"theta={low['theta']:.6f} n_tie={len(low['tied'])} "
        f"gap0={j_0 - j_c:.6f} gapeq={j_e - j_c:.6f}",
    )

    high_ok = True
    high_bits = []
    for w in (4.0, 10.0):
        m = cell(0.0, w)
        jp, _ = j_at(0.0, 0.0, w, N, cache)
        jc, _ = j_at(PI4, 0.0, w, N, cache)
        ok = m["unique"] and abs(m["theta"]) <= 1e-12 and jp < jc
        high_ok = high_ok and ok
        high_bits.append(
            f"w={w:g} theta={m['theta']:.6f} n_tie={len(m['tied'])} J0-Jc={jp - jc:.6f}"
        )
    rep.add("R-high", high_ok, " | ".join(high_bits))

    pos_ok = True
    pos_bits = []
    for q in (1.0, 0.5):
        m = cell(q, 1.0)
        ok = m["unique"] and abs(m["theta"]) <= 1e-12
        pos_ok = pos_ok and ok
        pos_bits.append(f"q={q:g} theta={m['theta']:.6f} n_tie={len(m['tied'])}")
    rep.add("R-pos", pos_ok, " | ".join(pos_bits))

    stars = {0.0: low}
    for q in (0.5, 1.0, 2.0):
        stars[q] = cell(q, 1.0)
    jstar0 = stars[0.0]["J"]
    ratio_ok = True
    ratio_bits = []
    for q, m in stars.items():
        gap_q = m["J"] - jstar0
        ok = gap_q >= -1e-9
        ratio_ok = ratio_ok and ok
        if not ok:
            ratio_bits.append(f"q={q:g} gap={gap_q:.6e}")
    d2 = (
        j_at(PI4, 1.5, 1.0, N, cache)[0]
        - 2.0 * j_at(PI4, 1.0, 1.0, N, cache)[0]
        + j_at(PI4, 0.5, 1.0, N, cache)[0]
    )
    d2_ok = abs(d2) < 1e-9
    ratio_ok = ratio_ok and d2_ok
    detail = f"max gap above J*(0) kept; second_diff={d2:.3e}"
    if ratio_bits:
        detail = " | ".join(ratio_bits) + f" | second_diff={d2:.3e}"
    rep.add("R-ratio", ratio_ok, detail)

    rep.dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
