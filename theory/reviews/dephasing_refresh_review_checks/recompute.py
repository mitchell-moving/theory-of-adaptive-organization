#!/usr/bin/env python3
"""Independent recomputation for the T84b refresh review.

Does not import the scored scripts. Stdlib only.
Pinned to forge-dephasing-refresh 067c485dd86517f7ffaad01486cbd696f690842b.
"""
from decimal import Decimal, getcontext
import math

getcontext().prec = 50


def hbin(p):
    p = Decimal(p)
    if p <= 0 or p >= 1:
        return Decimal(0)
    return -p * p.ln() - (1 - p) * (1 - p).ln()


def Lbar(u):
    u = Decimal(u)
    if u == 0:
        return Decimal(0)
    return Decimal("0.5") - (1 - (-u).exp()) / (2 * u)


def Lp(u):
    u = Decimal(u)
    return (1 - (1 + u) * (-u).exp()) / (2 * u * u)


def s_star(u):
    u = Decimal(u)
    return 2 / (1 - (1 + u) * (-u).exp())


def Pi(theta):
    theta = Decimal(theta)
    return 2 * theta * theta / (1 - (1 + theta) * (-theta).exp())


def theta_of_C(u):
    target = Lbar(u) + Decimal(u) * Lp(u)
    lo, hi = Decimal("1e-18"), Decimal(1)
    while Lbar(hi) < target:
        hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if Lbar(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def elast(u):
    u = Decimal(u)
    s = s_star(u)
    j = 1 / u + s * Lbar(u)
    return s * Lbar(u) / j


def t_of(theta):
    theta = Decimal(theta)
    eps = (1 - (-theta).exp()) / 2
    return hbin(eps) / eps


def gaussian_Lbar(u, n=8000):
    if u <= 0:
        return 0.0
    h = u / n
    acc = 0.0
    for i in range(n + 1):
        v = i * h
        eps = 0.5 * (1.0 - math.exp(-v * v))
        w = 4 if i % 2 else 2
        if i == 0 or i == n:
            w = 1
        acc += w * eps
    return (h / 3.0) * acc / u


def gaussian_elasticity(s):
    lo, hi = 1e-4, 3.0
    best_u, best_j = lo, 1e300
    u = lo
    while u < hi:
        j = 1.0 / u + s * gaussian_Lbar(u)
        if j < best_j:
            best_u, best_j = u, j
        u *= 1.04
    a, b = best_u / 1.15, best_u * 1.15
    gr = (math.sqrt(5) - 1) / 2
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc = 1 / c + s * gaussian_Lbar(c)
    fd = 1 / d + s * gaussian_Lbar(d)
    for _ in range(50):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = 1 / c + s * gaussian_Lbar(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = 1 / d + s * gaussian_Lbar(d)
    u = 0.5 * (a + b)
    loss = s * gaussian_Lbar(u)
    j = 1 / u + loss
    return u, loss / j


def main():
    series = 4 + (Decimal(8) / 3) * Decimal("0.01") + (Decimal(7) / 9) * Decimal("0.0001")
    pi = Pi("0.01")
    print("Pi_c(0.01)", pi)
    print("series_gap", abs(pi - series))
    print("Pi_c(1e-6)-4", Pi("0.000001") - 4)
    for u in ("0.0001", "0.01"):
        th = theta_of_C(u)
        print("accounting_C", u, s_star(u) * th * th)
    u = Decimal("0.01")
    s = s_star(u)
    j = 1 / u + s * Lbar(u)
    print("ratio_u", u * s.sqrt() / 2)
    print("ratio_J", j / s.sqrt())
    for u in ("0.01", "0.5", "1", "2"):
        print("elasticity", u, elast(u))
    print("squared_share_identity", (Decimal(6) / Decimal(1000)) and "see algebra")
    s = Decimal(1000)
    uu = (Decimal(6) / s) ** (Decimal(1) / 3)
    share = (s * uu * uu / 12) / (1 / uu + s * uu * uu / 12)
    print("squared_share", share)
    print("squared_Pi_at_0.01", Decimal(6) / Decimal("0.01"))
    ln2 = Decimal(2).ln()
    print("ln2", ln2)
    print("gap_to_4", 4 - ln2)
    print("t(0.01)", t_of("0.01"))
    print("t(1)", t_of("1"))
    print("Pi(1)", Pi(1))
    eps = (1 - (-Decimal(1)).exp()) / 2
    r = (-Decimal(1)).exp()
    chi = ln2 - hbin((1 + r) / 2)
    jh = chi + 2 * eps
    print("printed_elasticity", (2 * eps) / jh)
    print("carrier", hbin(eps) + eps)
    print("leak_threshold", (ln2 - (1 - r)) / eps)
    print("squared_one_shot", chi + 2 * eps * eps)
    print("rent_gap", 3 * hbin(eps) - 2 * eps)
    print("coherence_threshold", (1 - r) / (Decimal("0.5") - eps))
    for s in (20.0, 100.0, 10000.0):
        gu, ge = gaussian_elasticity(s)
        print("gaussian_envelope", s, "u", gu, "elasticity", ge, "minus_1/3", ge - 1.0 / 3.0)


if __name__ == "__main__":
    main()
