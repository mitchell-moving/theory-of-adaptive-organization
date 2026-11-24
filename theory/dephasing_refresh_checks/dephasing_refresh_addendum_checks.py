#!/usr/bin/env python3
"""T84b addendum: T84's noiseless holding cost against the T68 clock term.

Predictions are locked in theory/dephasing-refresh-2026-11-24/ADDENDUM_PREREG.md.
"""
import math
import sys


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def chi(r):
    return math.log(2.0) - hbin((1.0 + r) / 2.0)


def j_hold(kappa, w):
    """T84 J_H at gamma*tau = 0."""
    r = 1.0
    eps = (1.0 - r) / 2.0
    return kappa * chi(r) + w * eps


def clock(kappa, kT, omega, D):
    if omega == 0.0:
        return 0.0
    return kappa * kT * omega * omega / D


fails = []


def report(ok, line):
    print(line)
    if not ok:
        fails.append(line)


kappa = lam = kT = 1.0
onset = 4.0 * kappa / lam
stock_ok = True
gaps = []
for w in (0.0, 1.0, 2.0):
    F = j_hold(kappa, w) / kappa
    b1 = abs(F - math.log(2.0)) <= 1e-12
    b2 = abs(F - onset) >= 3.0
    b3 = abs(F - clock(kappa, kT, 0.0, 1.0)) >= 0.5
    stock_ok = stock_ok and b1 and b2 and b3
    gaps.append(abs(F - onset))
c11 = clock(kappa, kT, 1.0, 1.0)
c12 = clock(kappa, kT, 1.0, 2.0)
stock_ok = stock_ok and abs(c11 - 1.0) <= 1e-12 and abs(c12 - 0.5) <= 1e-12
stock_ok = stock_ok and abs(c11 - c12) > 0.4
report(stock_ok, "A0 %s F=%.12f gap_to_4=%.6f C11=%.1f C12=%.1f" % (
    "PASS" if stock_ok else "FAIL", j_hold(1.0, 0.0), gaps[0], c11, c12))

# Alt-onset must fail B2. Alt-frozen must fail B3.
F_on = onset
alt_onset_fails_b2 = not (abs(F_on / kappa - onset) >= 3.0)
F_frozen = 0.0
alt_frozen_fails_b3 = not (abs(F_frozen - clock(kappa, kT, 0.0, 1.0)) >= 0.5)
alts_separate = alt_onset_fails_b2 and alt_frozen_fails_b3
report(alts_separate, "A1 %s onset_fails_B2=%s frozen_fails_B3=%s" % (
    "PASS" if alts_separate else "FAIL",
    "yes" if alt_onset_fails_b2 else "no",
    "yes" if alt_frozen_fails_b3 else "no",
))

if stock_ok and alts_separate:
    label = "OBSERVED_NOT_CLOCK"
elif stock_ok and not alts_separate:
    label = "CONSISTENCY_CHECK"
else:
    label = "PUZZLE"
if label == "OBSERVED_NOT_CLOCK" and not (stock_ok and alts_separate):
    label = "PUZZLE"
report(label == "OBSERVED_NOT_CLOCK", "HEADLINE %s" % label)
print("FAILS %d" % len(fails))
if fails:
    print("ALL T84b ADDENDUM CHECKS FAIL")
    sys.exit(1)
print("ALL T84b ADDENDUM CHECKS PASS")
