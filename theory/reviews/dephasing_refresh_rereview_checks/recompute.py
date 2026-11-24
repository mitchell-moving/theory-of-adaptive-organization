#!/usr/bin/env python3
"""Independent float64 recomputation for the T84b re-review.

Does not import the scoring scripts. The formulas are the locked ones.
Run from anywhere: python3 theory/reviews/dephasing_refresh_rereview_checks/recompute.py
"""
import math


def Lbar(u):
    if u == 0.0:
        return 0.0
    # expm1 keeps the small-u slope. Equivalent to 1/2 - (1-e^{-u})/(2u).
    return 0.5 + math.expm1(-u) / (2.0 * u)


def Lbar_parent(u):
    """The parent script's cancellation, used only to match its derivative gap."""
    if u == 0.0:
        return 0.0
    return 0.5 - (1.0 - math.exp(-u)) / (2.0 * u)


def Lp(u):
    return (1.0 - (1.0 + u) * math.exp(-u)) / (2.0 * u * u)


def s_star(u):
    return 2.0 / (1.0 - (1.0 + u) * math.exp(-u))


def Pi_c(theta):
    return 2.0 * theta * theta / (1.0 - (1.0 + theta) * math.exp(-theta))


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def t_of(theta):
    eps = (1.0 - math.exp(-theta)) / 2.0
    return hbin(eps) / eps


def theta_of_C(u):
    target = Lbar(u) + u * Lp(u)
    lo, hi = 1e-16, 1.0
    while Lbar(hi) < target:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if Lbar(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def exp_age_coeff(f, gamma, n=400000):
    """Trapezoid in s = f t, the same grid the onset script uses."""
    smax = 80.0
    ds = smax / n
    acc = 0.0
    scale = f / (2.0 * gamma)
    for i in range(n + 1):
        s = i * ds
        weight = 0.5 if i == 0 or i == n else 1.0
        acc += weight * math.exp(-s) * (-math.expm1(-gamma * s / f))
    return scale * acc * ds


def gauss_share(stake, n=200000):
    """Loss share under coherence e^{-(gamma t)^2}, A = 1, stake = w/A."""

    def edge(x):
        return 0.5 * -math.expm1(-(x * x))

    def average(u):
        m = max(8, int(u / (2.0 / n)))
        h = u / m
        total = 0.0
        for i in range(m + 1):
            wgt = 0.5 if i == 0 or i == m else 1.0
            total += wgt * edge(i * h)
        return total * h / u

    lo, hi = 1e-4, 1.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        avg = average(mid)
        # dJ/du has the sign of stake*(edge-avg) - 1/mid
        if stake * (edge(mid) - avg) - 1.0 / mid > 0.0:
            hi = mid
        else:
            lo = mid
    u = 0.5 * (lo + hi)
    avg = average(u)
    loss = stake * avg
    return loss / (1.0 / u + loss)


def main():
    theta = 0.01
    pic = Pi_c(theta)
    series = 4.0 + (8.0 / 3.0) * theta + (7.0 / 9.0) * theta * theta
    print("Pi_c(0.01)=%.12f" % pic)
    print("series_gap=%+.12e" % (pic - series))
    print("M1_from_4=%+.12e" % (pic - 4.0))
    print("c_star=%.1f" % (2.0 * 1.0 * 2.0 / 1.0))

    def boundary(w):
        return w * theta * theta / pic

    dw = 1e-4
    e_a = (math.log(boundary(1.0 + dw)) - math.log(boundary(1.0 - dw))) / (
        math.log(1.0 + dw) - math.log(1.0 - dw)
    )
    print("e_A=%.16f" % e_a)

    u = 1e-6
    a_u = Lbar(u) / u
    a_u2 = Lbar(u / 2.0) / (u / 2.0)
    alpha_u = 2.0 * a_u2 - a_u
    a_e = exp_age_coeff(1.0e6, 1.0)
    a_e2 = exp_age_coeff(2.0e6, 1.0)
    alpha_e = 2.0 * a_e2 - a_e
    print("alpha_U=%.16f" % alpha_u)
    print("alpha_E=%.16f" % alpha_e)
    print("gap_E_minus_U=%+.16f" % (alpha_e - alpha_u))
    print("alpha_E_minus_quarter=%+.16f" % (alpha_e - 0.25))
    print("exact_limit_E=0.5")
    print("M4_limit=%.1f residual=%+.1f" % (1.0 / (1.0 / 8.0), 1.0 / (1.0 / 8.0) - 4.0))

    s = s_star(0.01)
    j = 1.0 / 0.01 + s * Lbar(0.01)
    print("ratio_u=%.10f ratio_J=%.10f" % (0.01 * math.sqrt(s) / 2.0, j / math.sqrt(s)))
    for uu in (0.01, 0.5, 1.0):
        ss = s_star(uu)
        jj = 1.0 / uu + ss * Lbar(uu)
        print("elast_%s=%.10f" % (uu, ss * Lbar(uu) / jj))
    for uu in (1e-4, 0.01):
        th = theta_of_C(uu)
        print("acctC_%s=%.12f" % (uu, s_star(uu) * th * th))

    max_lp = 0.0
    for uu in (0.01, 0.1, 0.5, 1.0, 2.0):
        num = (Lbar_parent(uu + 1e-5) - Lbar_parent(uu - 1e-5)) / 2e-5
        max_lp = max(max_lp, abs(num - Lp(uu)))
    print("R0_max_lp=%.6e" % max_lp)

    worst = 0.0
    for ss in (20.0, 100.0, 1.0e4):
        uu = (3.0 / ss) ** (1.0 / 3.0)
        share = ss * (uu * uu) / 6.0
        worst = max(worst, abs(share / (1.0 / uu + share) - 1.0 / 3.0))
    print("R6_gap=%.6e" % worst)

    print("ln2=%.15f" % math.log(2.0))
    print("gap_to_4=%.15f" % (4.0 - math.log(2.0)))
    print("t_0.01=%.10f t_1=%.10f Pi_1=%.10f" % (t_of(0.01), t_of(1.0), Pi_c(1.0)))
    eps = (1.0 - math.exp(-1.0)) / 2.0
    chi = math.log(2.0) - hbin((1.0 + math.exp(-1.0)) / 2.0)
    print("K2=%.12f" % (2.0 * eps / (chi + 2.0 * eps)))
    print("K3_Pi=%.1f" % (6.0 / 0.01))
    r = math.exp(-1.0)
    print(
        "K4=%.10f %.10f %.10f %.10f %.10f"
        % (
            hbin(eps) + eps,
            (math.log(2.0) - (1.0 - r)) / eps,
            chi + 2.0 * eps * eps,
            3.0 * hbin(eps) - 2.0 * eps,
            (1.0 - r) / (0.5 - eps),
        )
    )
    for stake in (20.0, 1.0e4):
        share = gauss_share(stake)
        print("GAUSS_%s=%.8f from_1/3=%+.8f" % (stake, share, share - 1.0 / 3.0))


if __name__ == "__main__":
    main()
