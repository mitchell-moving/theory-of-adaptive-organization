#!/usr/bin/env python3
"""Post-hoc diagnosis after the locked T76 run.

Not a rescore. PREREG.md is not edited. Nothing here changes FAILS.
C1 and C2 missed the interior band. This script locates that band and,
inside it only, repeats the locked inversion so the miss has a diagnosis.
The preregistration's suggested next stakes are printed and not substituted.
"""
from __future__ import annotations

import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "t76", os.path.join(HERE, "record_ratio_reframes_checks.py")
)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

HALF = 0.5 * math.pi


def interior(th: float) -> bool:
    return 0.05 <= th <= HALF - 0.05


def main() -> int:
    print("POSTHOC not a rescore. Locked FAILS are unchanged.")
    print("Suggested next stakes in PREREG.md C1, not used as a score:")
    for w in (0.2, 0.3):
        r = m.minimize("ANT", 0.0, 0.0, 1.0, 0.5, w)
        print(f"  ANT w={w:.2f} theta={r['theta']:.6f} interior={interior(r['theta'])}")

    print("ANT plant (1, 0.5), w from 1.30 to 1.70 step 0.02")
    ant_int = []
    for i in range(21):
        w = 1.30 + i * 0.02
        r = m.minimize("ANT", 0.0, 0.0, 1.0, 0.5, w)
        flag = interior(r["theta"]) and r["unique"]
        print(
            f"  w={w:.2f} theta={r['theta']:.6f} ntie={len(r['tied'])} interior={flag}"
        )
        if flag:
            ant_int.append((w, r))
    if len(ant_int) >= 2:
        (w1, m1), (w2, m2) = ant_int[0], ant_int[-1]
        d1 = m.derivs("ANT", 0.0, m1["theta"], 0.0)
        d2 = m.derivs("ANT", 0.0, m2["theta"], 0.0)
        det = d1["I"] * d2["P_D"] - d1["P_D"] * d2["I"]
        print(f"ANT endpoint-interior det={det:.6e}")
        for w, r in (ant_int[0], ant_int[len(ant_int) // 2], ant_int[-1]):
            d = m.derivs("ANT", 0.0, r["theta"], 0.0)
            delta = -w * d["L"] / d["P_D"]
            print(f"  delta_hat w={w:.2f} theta={r['theta']:.4f} delta={delta:.6f}")

    print("BIAS plant (1, 0.5), w from 0.450 to 0.530 step 0.005")
    bias_int = []
    for i in range(17):
        w = 0.450 + i * 0.005
        r = m.minimize("BIAS", 0.0, 0.0, 1.0, 0.5, w)
        flag = interior(r["theta"]) and r["unique"]
        print(
            f"  w={w:.3f} theta={r['theta']:.6f} ntie={len(r['tied'])} interior={flag}"
        )
        if flag:
            bias_int.append((w, r))
    if len(bias_int) >= 2:
        (w1, m1), (w2, m2) = bias_int[0], bias_int[-1]
        d1 = m.derivs("BIAS", 0.0, m1["theta"], 0.0)
        d2 = m.derivs("BIAS", 0.0, m2["theta"], 0.0)
        det = d1["I"] * d2["P_D"] - d1["P_D"] * d2["I"]
        rhs1, rhs2 = -w1 * d1["L"], -w2 * d2["L"]
        kappa = (rhs1 * d2["P_D"] - d1["P_D"] * rhs2) / det
        kappa_d = (d1["I"] * rhs2 - rhs1 * d2["I"]) / det
        print(
            f"BIAS ends w=({w1:.3f},{w2:.3f}) theta=({m1['theta']:.4f},{m2['theta']:.4f}) "
            f"det={det:.6e} kappa={kappa:.6f} kappa_D={kappa_d:.6f}"
        )
    print("POSTHOC END")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
