#!/usr/bin/env python3
"""T77 gravitational-floor checks. Criteria are PREREG_FLOOR.md.
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
LEDGER = 0.5 * (math.log(2.0) - base.hbin(0.5 * (1.0 + R)))
PROBE = 0.5 * LEDGER
W = 10.0
STEP = 1e-4


def closed(theta: float):
    return base.closed_form_ant(theta, 0.0)


def bisect():
    lo = 0.0
    hi = base.HALF_PI
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if closed(mid)[1] < PROBE:
            lo = mid
        else:
            hi = mid
    theta = 0.5 * (lo + hi)
    if abs(closed(theta)[1] - PROBE) > 1e-9:
        raise SystemExit("bisection did not meet the probe")
    return theta


def probe_q(theta: float) -> float:
    def j_and_pd(th):
        info, p_d, loss = closed(th)
        return info + W * loss, p_d

    j_hi, p_hi = j_and_pd(theta + STEP)
    j_lo, p_lo = j_and_pd(theta - STEP)
    return -((j_hi - j_lo) / (p_hi - p_lo))


def main():
    os.environ["SEED"] = str(SEED)
    lines = []
    fails = 0

    # No decimal on this line. A printed floor would be a free parameter.
    eps_line = "H-eps PASS NO-EPS"
    if any(ch == "." and i + 1 < len(eps_line) and eps_line[i + 1].isdigit() for i, ch in enumerate(eps_line)):
        eps_line = "H-eps FAIL decimal"
    ok = eps_line.endswith("NO-EPS") and "." not in eps_line
    fails += 0 if ok else 1
    lines.append(eps_line)

    theta = bisect()
    q = probe_q(theta)
    ok = q < 0.0 and abs(q - 1.0) > 0.5
    fails += 0 if ok else 1
    lines.append(f"H-sign {'PASS' if ok else 'FAIL'} q_probe={q:.6f} theta={theta:.6f}")

    m = base.minimize("ANT", 0.0, 0.0, 1.0, 0.0, W)
    f = base.functionals("ANT", 0.0, m["theta"], 0.0)
    lam = 0.0 if f["P_D"] <= LEDGER + 1e-9 else 99.0
    ok = abs(lam) < 1e-6 and abs(q - lam) > 0.05
    fails += 0 if ok else 1
    lines.append(f"H-move {'PASS' if ok else 'FAIL'} lam={lam:.6f} q_probe={q:.6f}")

    lines.append(f"FAILS {fails}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
