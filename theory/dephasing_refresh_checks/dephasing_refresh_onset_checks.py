#!/usr/bin/env python3
"""T84b onset: is Pi_c -> 4 the Poisson look onset c* = 4 kappa kT?

Bars are locked in theory/dephasing-refresh-2026-11-24/ONSET_PREREG.md.
This file is not part of that lock.
"""
import math


def pi_c(theta):
    return 2.0 * theta * theta / (1.0 - (1.0 + theta) * math.exp(-theta))


def lbar(u):
    # expm1 keeps the small-u slope; 1-exp(-u) cancels in float64.
    return 0.5 + math.expm1(-u) / (2.0 * u)


def exp_age_coeff(f, gamma, n=400000):
    """alpha_E at finite f: (f/gamma) times the exponential-age Hamming mean.

    Integrate in s=f t so the Poisson density is e^{-s} on a fixed grid.
    """
    smax = 80.0
    ds = smax / n
    acc = 0.0
    scale = f / (2.0 * gamma)
    for i in range(n + 1):
        s = i * ds
        weight = 0.5 if i == 0 or i == n else 1.0
        acc += weight * math.exp(-s) * (-math.expm1(-gamma * s / f))
    return scale * acc * ds


fails = []


def report(ok, line):
    print(line)
    if not ok:
        fails.append(line)


kappa = 1.0
a = 1.0
b = 2.0
c_over = 2.0 * kappa * b / a
report(abs(c_over - 4.0) <= 1e-12, "M1 c*/(kappa kT)=%.12f" % c_over)

theta = 0.01
pic = pi_c(theta)
report(abs(pic - 4.0) <= 0.05, "M1 Pi_c(0.01)=%.8f residual=%+.8e" % (pic, pic - 4.0))
m1 = abs(c_over - 4.0) <= 1e-12 and abs(pic - 4.0) <= 0.05

def boundary_price(w):
    return w * theta * theta / pic


w0 = 1.0
dw = 1e-4
e_a = (math.log(boundary_price(w0 + dw)) - math.log(boundary_price(w0 - dw))) / (
    math.log(w0 + dw) - math.log(w0 - dw)
)
report(abs(e_a - 0.0) <= 0.05, "M2 elasticity e_A=%+.8f residual_from_0=%+.8f" % (e_a, e_a - 0.0))
m2 = abs(e_a - 0.0) <= 0.05

def limit_alpha_u():
    # Cancel the O(u) term in Lbar(u)/u. The lock is the limit, not one finite u.
    u = 1e-6
    a = lbar(u) / u
    a2 = lbar(u / 2.0) / (u / 2.0)
    return 2.0 * a2 - a


def limit_alpha_e():
    gamma = 1.0
    f = 1.0e6
    a = exp_age_coeff(f, gamma)
    a2 = exp_age_coeff(2.0 * f, gamma)
    return 2.0 * a2 - a


alpha_u = limit_alpha_u()
alpha_e = limit_alpha_e()
report(
    abs(alpha_u - 0.25) < 1e-9 and abs(alpha_e - 0.25) < 1e-9,
    "M3 alpha_U=%.10f alpha_E=%.10f gap_E_minus_U=%+.10f"
    % (alpha_u, alpha_e, alpha_e - alpha_u),
)
m3 = abs(alpha_u - 0.25) < 1e-9 and abs(alpha_e - 0.25) < 1e-9

beta = 1.0 / 8.0
limit = 1.0 / beta
report(abs(limit - 4.0) <= 0.05, "M4 half-slope limit=%.8f residual_from_4=%+.8f" % (limit, limit - 4.0))
m4 = abs(limit - 4.0) <= 0.05

if m1 and m2 and m3 and m4:
    headline = "HIT_SAME_ONSET"
elif m1:
    headline = "MISS_COINCIDENCE"
else:
    headline = "MISS_NUMBER"

print("HEADLINE %s" % headline)
print("FAILS %d" % len(fails))
if fails:
    print("BARS MISSED %d" % len(fails))
else:
    print("ALL T84b ONSET BARS HOLD")
