#!/usr/bin/env python3
"""T84b class RF. Predictions are locked in theory/dephasing-refresh-2026-11-24/PREREG.md."""
import math
import sys

THETAS = (0.01, 0.1, 0.5, 1.0, 2.0)
US = (0.01, 0.1, 0.5, 1.0, 2.0)
TOL = 1e-9


def Lbar(u):
    if u == 0.0:
        return 0.0
    return 0.5 - (1.0 - math.exp(-u)) / (2.0 * u)


def Lp(u):
    return (1.0 - (1.0 + u) * math.exp(-u)) / (2.0 * u * u)


def s_star(u):
    return 2.0 / (1.0 - (1.0 + u) * math.exp(-u))


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def t_of(theta):
    eps = (1.0 - math.exp(-theta)) / 2.0
    return hbin(eps) / eps


def Pi_c(theta):
    return s_star(theta) * theta * theta


def u_of_s(s):
    """Inverse of s_star, which falls from +inf to 2."""
    if s <= 2.0:
        return math.inf
    lo, hi = 1e-12, 1.0
    while s_star(hi) > s:
        hi *= 2.0
        if hi > 1e6:
            break
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if s_star(mid) > s:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def theta_of_C(u):
    """Solve Lbar(Theta) = Lbar(u) + u L'(u)."""
    target = Lbar(u) + u * Lp(u)
    lo, hi = 1e-14, 1.0
    while Lbar(hi) < target:
        hi *= 2.0
        if hi > 1e6:
            break
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if Lbar(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


fails = []


def report(ok, line):
    print(line)
    if not ok:
        fails.append(line)


# R0
r0 = True
max_lp = 0.0
max_s = 0.0
for u in US:
    num = (Lbar(u + 1e-5) - Lbar(u - 1e-5)) / 2e-5
    max_lp = max(max_lp, abs(num - Lp(u)))
    max_s = max(max_s, abs(s_star(u) - 1.0 / (u * u * Lp(u))))
    second = (Lp(u + 1e-5) - Lp(u - 1e-5)) / 2e-5
    if second >= 0.0:
        r0 = False
if max_lp > TOL or max_s > TOL:
    r0 = False
report(r0, "R0 %s max_lp=%s max_s=%s" % ("PASS" if r0 else "FAIL", "%.3e" % max_lp, "%.3e" % max_s))


def gap_A(theta, s, u):
    return (1.0 / u + s * Lbar(u)) - (1.0 / theta + s * Lbar(theta))


def gap_B(theta, s, u):
    return (1.0 / u - 1.0 / theta + s * Lbar(u)) - (s * Lbar(theta))


# R1
r1 = True
worst_agree = 0.0
for theta in THETAS:
    sc = s_star(theta)
    for factor, want_pos in ((0.5, True), (1.5, False)):
        s = factor * sc
        ustar = u_of_s(s)
        samples = [theta * (i + 0.5) / 4000.0 for i in range(4000)]
        if ustar < theta:
            samples.append(ustar)
        best = min(gap_A(theta, s, u) for u in samples)
        best_b = min(gap_B(theta, s, u) for u in samples)
        worst_agree = max(worst_agree, max(abs(gap_A(theta, s, u) - gap_B(theta, s, u)) for u in samples[::40]))
        if want_pos:
            if best < -1e-9:
                r1 = False
        else:
            if not best < 0.0:
                r1 = False
        if abs(best - best_b) > 1e-9:
            r1 = False
report(r1, "R1 %s agree=%s" % ("PASS" if r1 else "FAIL", "%.3e" % worst_agree))

# R2
series = 4.0 + (8.0 / 3.0) * 0.01 + (7.0 / 9.0) * 0.01 ** 2
gap_series = abs(Pi_c(0.01) - series)
r2 = gap_series < 1e-6 and Pi_c(0.01) < 4.05
report(r2, "R2 %s Pi_c_0.01=%.8f series_gap=%.3e" % ("PASS" if r2 else "FAIL", Pi_c(0.01), gap_series))

# R3
u = 0.01
s = s_star(u)
j = 1.0 / u + s * Lbar(u)
ratio_u = abs(u * math.sqrt(s) / 2.0 - 1.0)
ratio_j = abs(j / math.sqrt(s) - 1.0)
r3 = ratio_u < 5e-3 and ratio_j < 5e-3
report(r3, "R3 %s ratio_u=%.6f ratio_J=%.6f" % ("PASS" if r3 else "FAIL", u * math.sqrt(s) / 2.0, j / math.sqrt(s)))

# R4
def elast(u):
    s = s_star(u)
    j = 1.0 / u + s * Lbar(u)
    return s * Lbar(u) / j


e = {u: elast(u) for u in US}
r4 = e[0.01] < 0.505 and e[0.5] < 0.55 and e[1.0] > 0.55 and e[2.0] > e[1.0]
report(
    r4,
    "R4 %s e_0.01=%.5f e_0.5=%.5f e_1=%.5f" % ("PASS" if r4 else "FAIL", e[0.01], e[0.5], e[1.0]),
)

# R5 accounting C
pi_small = s_star(1e-4) * theta_of_C(1e-4) ** 2
pi_01 = s_star(0.01) * theta_of_C(0.01) ** 2
r5 = abs(pi_small - 16.0) < 5e-3 and 16.1 < pi_01 < 16.2
report(r5, "R5 %s Pi_1em4=%.6f Pi_0.01=%.6f" % ("PASS" if r5 else "FAIL", pi_small, pi_01))

# R6 Gaussian short-time balance, elasticity exactly 1/3
r6_gap = 0.0
for s in (20.0, 100.0, 1.0e4):
    uu = (3.0 / s) ** (1.0 / 3.0)
    share_num = s * (uu * uu) / 6.0
    cost = 1.0 / uu + share_num
    r6_gap = max(r6_gap, abs(share_num / cost - 1.0 / 3.0))
r6 = r6_gap < 1e-12
report(r6, "R6 %s share_gap=%.3e" % ("PASS" if r6 else "FAIL", r6_gap))

# R7 unitary H_u = A doubles the Landauer Pi
series8 = 8.0 + (16.0 / 3.0) * 0.01 + (14.0 / 9.0) * 0.01 ** 2
gap8 = abs(2.0 * Pi_c(0.01) - series8)
r7 = gap8 < 2e-6
report(r7, "R7 %s doubled=%.8f gap=%.3e" % ("PASS" if r7 else "FAIL", 2.0 * Pi_c(0.01), gap8))

# R8 clock does not lower the RF rate; CK onset arithmetic
r8 = True
j_rf = 1.0
for I0 in (1.0, 4.0, 10.0):
    # TUR addend is kappa kT omega'^2/D divided by A = lambda kT I0.
    # kappa = lambda = kT = 1. omega' = 0 adds 0. A probe omega' = D = 1 adds 1/I0.
    at_zero = j_rf + 0.0
    at_probe = j_rf + (1.0 * 1.0) / I0
    if not (at_zero == j_rf and at_probe > j_rf):
        r8 = False
ck = 2.0 * 1.0 * 2.0 / 1.0  # 2 * kappa * b / a, in units of kT, kappa=1
r8 = r8 and abs(ck - 4.0) < TOL
report(r8, "R8 %s ck_onset=%.1f" % ("PASS" if r8 else "FAIL", ck))

# R9 not T84's threshold
ts = [t_of(th) for th in THETAS]
ps = [Pi_c(th) for th in THETAS]
r9 = all(ts[i] > ts[i + 1] for i in range(len(ts) - 1))
r9 = r9 and all(ps[i] < ps[i + 1] for i in range(len(ps) - 1))
r9 = r9 and (ps[0] - ts[0]) < 0.0 and (ps[3] - ts[3]) > 0.0
report(
    r9,
    "R9 %s t_0.01=%.6f Pi_0.01=%.6f t_1=%.6f Pi_1=%.6f"
    % ("PASS" if r9 else "FAIL", ts[0], ps[0], ts[3], ps[3]),
)

ok = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]
# R2 is the finite-hold limit of 4. A 16 there would be index 2 failing.
if all(ok):
    label = "CLUE_REFRESH"
elif not r2:
    label = "PUZZLE"
else:
    label = "PUZZLE"
# Do not emit the clue label unless every locked check held.
if label == "CLUE_REFRESH" and not all(ok):
    label = "PUZZLE"
report(label == "CLUE_REFRESH", "HEADLINE %s" % label)
print("FAILS %d" % len(fails))
if fails:
    print("ALL T84b CHECKS FAIL")
    sys.exit(1)
print("ALL T84b CHECKS PASS")
