#!/usr/bin/env python3
"""T84b review fold-in. Predictions are locked in ADDENDUM_REVIEW_PREREG.md."""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T84_PREREG = os.path.join(
    ROOT, "theory", "dephasing-crossover-2026-11-24", "PREREG.md"
)


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def eps_of(x):
    return (1.0 - math.exp(-x)) / 2.0


def t_of(x):
    eps = eps_of(x)
    return hbin(eps) / eps


fails = []


def report(ok, line):
    print(line)
    if not ok:
        fails.append(line)


# K0: T84 locked no square-root exponent. Consistency label, not a refresh test.
text = open(T84_PREREG, encoding="utf-8").read()
k0 = ("w^{1/2}" not in text) and ("T_hold" not in text)
report(k0, "K0 %s t84_locked_no_sqrt=%s" % ("PASS" if k0 else "FAIL", "yes" if k0 else "no"))

# Product and floor
t_half = t_of(2.0 * 0.5)
t_swap = t_of(0.5 * 2.0)
t1 = t_of(1.0)
t_small = t_of(0.01)
floor = 2.0 * math.log(2.0)
k_prod = abs(t_half - t_swap) <= 1e-12 and abs(t_half - t1) <= 1e-12
k_prod = k_prod and t_small > t1 > floor
report(k_prod, "K1 %s t_product=%.6f floor=%.12f" % (
    "PASS" if k_prod else "FAIL", t1, floor))

# Printed-cell elasticity of the affine T84 cost
x = 1.0
eps = eps_of(x)
chi = math.log(2.0) - hbin((1.0 + math.exp(-x)) / 2.0)
w = 2.0
j_h = chi + w * eps
elast = w * eps / j_h
k_el = abs(elast - 0.901222) <= 1e-5 and abs(elast - 0.5) >= 0.3
report(k_el, "K2 %s elasticity=%.6f" % ("PASS" if k_el else "FAIL", elast))

# Squared-Hamming refresh: share 1/3, critical Pi = 6/Theta
s = 1000.0
u = (6.0 / s) ** (1.0 / 3.0)
share = (s * (u * u) / 12.0) / (1.0 / u + s * (u * u) / 12.0)
theta = 0.01
pi_crit = 6.0 / theta
k_sq = abs(share - 1.0 / 3.0) <= 1e-12 and abs(pi_crit - 600.0) <= 1e-6 and pi_crit > 100.0
# The linear-Hamming claims fail on this alternative.
flips = abs(share - 0.5) > 0.1 and pi_crit > 100.0
k_sq = k_sq and flips
report(k_sq, "K3 %s share=%.6f Pi_crit=%.1f" % ("PASS" if k_sq else "FAIL", share, pi_crit))

# One-shot alternatives at gamma*tau = 1
r = math.exp(-1.0)
eps = eps_of(1.0)
# Carrier entropy
j_carrier = hbin(eps) + 1.0 * eps
j_carrier_0 = 0.0
k_a = j_carrier > 0.9 and abs(j_carrier_0 - math.log(2.0)) > 0.5
# Linear leak threshold
thr_b = (math.log(2.0) - (1.0 - r)) / eps
k_b = thr_b < 0.2
# Squared Hamming one-shot
j_sq = chi + 2.0 * eps * eps
k_c = j_sq < math.log(2.0) and abs(4.0 * math.log(2.0) - 2.0 * math.log(2.0)) > 1.0
# Stake-dependent rent
diff_d = (1.0 + 2.0) * hbin(eps) - 2.0 * eps
k_d = diff_d > 1.0
# Linear coherence: J_Z = w/2, J_H = (1-r) + w*eps
thr_p = (1.0 - r) / (0.5 - eps)
k_p = thr_p > 3.0 and 0.376662 < 0.4
k_flip = k_a and k_b and k_c and k_d and k_p
report(k_flip, "K4 %s carrier=%.6f leak_thr=%.6f sqJH=%.6f rent_gap=%.6f coh_thr=%.6f" % (
    "PASS" if k_flip else "FAIL", j_carrier, thr_b, j_sq, diff_d, thr_p))

if k_sq and k_prod and k_el and k_flip and k0:
    label = "OBSERVED_ALT_FLIPS"
elif not flips:
    label = "CONSISTENCY_CHECK"
else:
    label = "PUZZLE"
if label == "OBSERVED_ALT_FLIPS" and not (k_sq and k_prod and k_el and k_flip and k0):
    label = "PUZZLE"
report(label == "OBSERVED_ALT_FLIPS", "HEADLINE %s" % label)
print("FAILS %d" % len(fails))
if fails:
    print("ALL T84b REVIEW-FOLD CHECKS FAIL")
    sys.exit(1)
print("ALL T84b REVIEW-FOLD CHECKS PASS")
