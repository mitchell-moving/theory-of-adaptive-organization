#!/usr/bin/env python3
"""Independent recomputation for the T84 review.

Does not import the scored script. Decimal entropy at 80 places.
Alternative costs are evaluated at the locked cells so a reader can see
which locked signs flip. This file does not add a prediction.
"""
from __future__ import annotations

import math
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()


def h(p: Decimal) -> Decimal:
    if p <= 0 or p >= 1:
        return D(0)
    return -p * p.ln() - (1 - p) * (1 - p).ln()


def chi(r: Decimal) -> Decimal:
    return LN2 - h((1 + r) / 2)


def cell(gt: str):
    r = (-D(gt)).exp()
    return r, (1 - r) / 2


def rounds(val: Decimal, digits: int) -> str:
    return format(val.quantize(D(10) ** -digits), "f")


def main() -> None:
    # (h/eps)' has numerator ln(1-eps) < 0 on (0, 1).
    for e in (D("1e-8"), D("1e-4"), D("0.1"), D("0.5")):
        assert (1 - e).ln() < 0
    assert h(D("0.5")) / D("0.5") == 2 * LN2

    # chi(r)/r increases: r*chi' - chi > 0, chi' = (1/2) ln((1+r)/(1-r)).
    def chi_prime(r: Decimal) -> Decimal:
        return D("0.5") * ((1 + r) / (1 - r)).ln()

    for r in (D("1e-4"), D("0.05"), D("0.5"), (-D(1)).exp(), D("0.9")):
        assert r * chi_prime(r) - chi(r) > 0

    expect = {
        ("t", "1e-4", 6): "10.210290",
        ("t_half", "", 12): "1.386294361120",
        ("t", "0.1", 6): "4.021138",
        ("t", "1", 6): "1.973877",
        ("t", "5", 6): "1.395653",
        ("JH", "1", 6): "0.701404",
        ("Delta", "1", 6): "0.008256",
        ("JP", "", 12): "0.693147180560",
        ("p2", "1", 6): "0.376662",
        ("chi_r", "0.05", 6): "0.025010",
        ("PD8", "", 8): "0.06540602",
        ("PD4", "", 8): "0.34657359",
        ("gap", "1", 6): "0.069283",
    }

    def t_of(gt: str) -> Decimal:
        _r, e = cell(gt)
        return h(e) / e

    r1, e1 = cell("1")
    jh = chi(r1) + 2 * e1
    delta = 2 * e1 - h(e1)
    def S(xs):
        return sum(-x * x.ln() for x in xs if x > 0)

    pd8 = S((D("0.5"), D("0.25"), D("0.25"))) - S((D("0.5"), D("0.375"), D("0.125")))
    pd4 = S((D("0.5"), D("0.25"), D("0.25"))) - S((D("0.5"), D("0.5"), D(0)))
    assert abs(pd4 - LN2 / 2) < D("1e-60")
    got = {
        ("t", "1e-4"): h(D("1e-4")) / D("1e-4"),
        ("t_half", ""): 2 * LN2,
        ("t", "0.1"): t_of("0.1"),
        ("t", "1"): t_of("1"),
        ("t", "5"): t_of("5"),
        ("JH", "1"): jh,
        ("Delta", "1"): delta,
        ("JP", ""): LN2,
        ("p2", "1"): 2 * chi(r1) / r1,
        ("chi_r", "0.05"): chi(D("0.05")) / D("0.05"),
        ("PD8", ""): pd8,
        ("PD4", ""): pd4,
        ("gap", "1"): chi(r1),
    }
    for (name, tag, digits), printed in expect.items():
        rounded = rounds(got[(name, tag)], digits)
        if rounded != printed:
            raise SystemExit(f"digit miss {name} {tag}: {rounded} != {printed}")
        print(f"MATCH {name} {tag} {printed}")
    gap = pd8 - D("0.065406")
    print(f"PD_gap {format(gap, '.3e')}")
    if not (D("1.7e-8") < gap < D("1.9e-8")):
        raise SystemExit("PD gap")

    # Identity of the chosen J.
    ident = (LN2 - chi(r1)) / e1 - h(e1) / e1
    print(f"P1_identity_residual {format(ident, 'e')}")
    if abs(ident) > D("1e-60"):
        raise SystemExit("P1 not an identity")

    # --- alternatives at gamma*tau = 1, kappa = 1 ---
    # A. Charge the carrier entropy, pointer is pure.
    jh_a = h(e1) + 1 * e1
    # Locked P1 at w=1 says the phase hold is cheaper (1 < 1.973877).
    if not (D(0) < jh_a):
        raise SystemExit("A did not flip")
    print(f"ALT_A w=1 pointer_cheaper JH={format(jh_a, '.6f')} locked_says_phase_hold")
    print(f"ALT_A gt0 JH={format(h(D(0)), 'f')} locked_Q3_wants_ln2")

    # B. Linear leak rent, pointer still pays ln 2.
    thr_b = LN2 / e1 - 2
    print(f"ALT_B threshold {format(thr_b, '.6f')} locked {format(h(e1)/e1, '.6f')}")
    if not (D(1) > thr_b and D(1) < h(e1) / e1):
        raise SystemExit("B did not flip at w=1")

    # C. Squared Hamming readout.
    thr_c = h(e1) / (e1 * e1)
    jh_c = chi(r1) + 2 * e1 * e1
    print(f"ALT_C threshold {format(thr_c, '.6f')} JH_w2 {format(jh_c, '.6f')} JP {format(LN2, '.6f')}")
    if not (jh_c < LN2 and D(2) > h(e1) / e1):
        raise SystemExit("C did not flip at w=2")
    print(f"ALT_C floor {format(4 * LN2, '.6f')}")

    # D. Stake-dependent rent, coefficient (1+w) on the information term.
    w = D(2)
    diff_d = (1 + w) * LN2 - ((1 + w) * chi(r1) + w * e1)
    print(f"ALT_D JP_minus_JH_w2 {format(diff_d, '.6f')}")
    if diff_d <= 0:
        raise SystemExit("D did not keep the pointer more expensive")

    # P2 under a linear coherence penalty, q=0, w=0.5.
    one_m_r = 1 - r1
    thr_p2 = 2 * one_m_r / r1
    jh_p = one_m_r * (1 + D("0.5") / 2)
    jz_p = D("0.5") / 2
    print(f"ALT_P2 threshold {format(thr_p2, '.6f')} locked {format(2*chi(r1)/r1, '.6f')}")
    print(f"ALT_P2 w=0.5 JZ {format(jz_p, '.6f')} JH {format(jh_p, '.6f')}")
    if not (jz_p < jh_p and D("0.5") > 2 * chi(r1) / r1):
        raise SystemExit("P2 did not flip")

    # Product only. gamma=2, T=1/2 equals gamma=1/2, T=2.
    def t_prod(g, T):
        _r, e = cell(str(g * T))
        return h(e) / e

    t_same = t_prod(D(2), D("0.5"))
    t_swap = t_prod(D("0.5"), D(2))
    if t_same != t_swap:
        raise SystemExit("product dependence failed")
    print(f"PRODUCT t {format(t_same, '.6f')}")

    elas = (2 * e1) / jh
    print(f"ELASTICITY gt1_w2 {format(elas, '.6f')}")

    # Elementary scrub balance: (ln 2)/T + w*(gamma*T)/2, gamma=1.
    # Optimum cost sqrt(2*ln2*w*gamma), which scales as w**(1/2).
    j_sqrt = (2 * LN2 * D(4)).sqrt()
    j_sqrt_1 = (2 * LN2).sqrt()
    print(f"SCRUB_J w=1 {format(j_sqrt_1, '.6f')} w=4 {format(j_sqrt, '.6f')} ratio {format(j_sqrt/j_sqrt_1, '.6f')}")
    if abs(j_sqrt / j_sqrt_1 - 2) > D("1e-20"):
        raise SystemExit("scrub ratio")

    # Projector check, float, independent of the scored script.
    def hf(p):
        if p <= 0.0 or p >= 1.0:
            return 0.0
        return -p * math.log(p) - (1 - p) * math.log(1 - p)

    def Sf(xs):
        return sum(-x * math.log(x) for x in xs if x > 0)

    def eigs2(a, b, c):
        tr = a + b
        root = math.sqrt(max(0.0, tr * tr - 4 * (a * b - c * c)))
        return (tr + root) / 2, (tr - root) / 2

    worst = 0.0
    for r in (1.0, 0.5, 0.1):
        rho = ((0.5, r / 2), (r / 2, 0.5))
        s_rho = Sf(eigs2(0.5, 0.5, r / 2))
        for theta in (0.0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2):
            cth, sth = math.cos(theta / 2), math.sin(theta / 2)
            pp = ((cth * cth, cth * sth), (cth * sth, sth * sth))
            pm = ((sth * sth, -cth * sth), (-cth * sth, cth * cth))

            def mm(a, b):
                return (
                    (a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
                    (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
                )

            def sand(p):
                return mm(mm(p, rho), p)

            phi, phi2 = sand(pp), sand(pm)
            pd_m = Sf(eigs2(phi[0][0] + phi2[0][0], phi[1][1] + phi2[1][1], 0.5 * (phi[0][1] + phi2[0][1] + phi[1][0] + phi2[1][0]))) - s_rho
            pd_c = hf((1 + abs(r * math.sin(theta))) / 2) - hf((1 + r) / 2)
            worst = max(worst, abs(pd_m - pd_c))
    print(f"THETA_PROJECTOR {worst:.3e}")
    if worst > 1e-12:
        raise SystemExit("projector")
    print("ALL INDEPENDENT RECOMPUTE CHECKS HOLD")


if __name__ == "__main__":
    main()
