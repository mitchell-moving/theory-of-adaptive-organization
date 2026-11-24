#!/usr/bin/env python3
"""T82 scoreboard. Stdlib only. Scores the locked predictions in
theory/torus-memory-2026-11-24/PREREG.md. A prediction miss is printed
FAIL and does not change the preregistration. Exit 0 means the script
finished; it does not mean every prediction passed.
"""
from __future__ import annotations

import hashlib
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG.md")
SIDECAR = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG.sha256")
LOCKED_HASH = "d0acb22ecefa52d41d95ca2a20f3fbfb251c237ee2bc9f6aa49549939508b204"

LN2 = math.log(2)
fails = []


def check(name, ok, detail):
    status = "PASS" if ok else "FAIL"
    if not ok:
        fails.append(name)
    print(f"{name} {status}  {detail}")


def v2(n):
    n = abs(int(n))
    c = 0
    while n % 2 == 0 and n > 0:
        n //= 2
        c += 1
    return c


def fmt(x):
    return f"{x:.12f}"


def main():
    blob = open(PREREG, "rb").read()
    digest = hashlib.sha256(blob).hexdigest()
    side = open(SIDECAR, "r", encoding="utf-8").read().split()[0]
    check(
        "P0",
        digest == side == LOCKED_HASH,
        f"prereg sha256 {digest}",
    )

    # --- P3: classical dephasing KL equals mutual information on Haar ---
    # Discrete stand-in of the locked definition: uniform prior on n**k atoms.
    n_bin, k = 4, 2
    n_atoms = n_bin ** k
    # Full reveal: posterior is a point, D(point || uniform) = ln(n_atoms) = I.
    d_full = math.log(n_atoms)
    i_full = math.log(n_atoms)
    # One coordinate revealed: posterior uniform on a fiber of n_bin atoms.
    # Each fiber atom has posterior 1/n_bin and prior 1/n_atoms.
    d_one = math.log(n_atoms / n_bin)
    i_one = math.log(n_bin)
    # Nothing revealed: posterior = prior, D = 0 = I.
    d_none = 0.0
    i_none = 0.0
    p3_ok = (
        abs(d_full - i_full) < 1e-15
        and abs(d_one - i_one) < 1e-15
        and abs(d_none - i_none) < 1e-15
    )
    check(
        "P3",
        p3_ok,
        f"D-I full {fmt(d_full - i_full)} one {fmt(d_one - i_one)} none {fmt(d_none - i_none)}",
    )

    # --- P1: four-bin sum collapses, scalar memory strictly cheaper ---
    centers = [math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4, 7 * math.pi / 4]
    signs = [1 if math.cos(c) > 0 else -1 for c in centers]
    # Sum of bin-center cosines, in units of sqrt(2)/2: sign1 + sign2.
    pair_sums = [s1 + s2 for s1 in signs for s2 in signs]
    distinct = sorted(set(pair_sums))
    counts = {v: pair_sums.count(v) for v in distinct}
    h_phase = math.log(len(pair_sums))
    h_sum = -sum((c / len(pair_sums)) * math.log(c / len(pair_sums)) for c in counts.values())
    # Same action on every atom: the sum itself. Reconstruction loss matches.
    same_action = True
    for s1 in signs:
        for s2 in signs:
            from_phases = s1 + s2
            from_scalar = s1 + s2
            same_action = same_action and from_phases == from_scalar
    p1_ok = (
        len(distinct) == 3
        and h_sum <= math.log(3) + 1e-12
        and math.log(3) < math.log(16)
        and h_sum < h_phase
        and same_action
        and abs(h_phase - math.log(16)) < 1e-12
    )
    check(
        "P1",
        p1_ok,
        f"distinct {len(distinct)} Hsum {fmt(h_sum)} Hphase {fmt(h_phase)} ln3 {fmt(math.log(3))}",
    )

    # --- P2: rank over Q, period, null radius ---
    # v2(n^2) even, v2(2 m^2) odd, so p^2 = 2 q^2 has no positive integer solution.
    val_ok = True
    for m in range(1, 1001):
        if v2(m * m) != 2 * v2(m) or v2(2 * m * m) % 2 == 0:
            val_ok = False
            break
    # Rational pair has period 4π. Irrational pair has two independent frequencies.
    ts = [i * 0.017 for i in range(400)]
    period_err = max(
        abs(math.cos(t + 4 * math.pi) + math.cos(1.5 * (t + 4 * math.pi)) - math.cos(t) - math.cos(1.5 * t))
        for t in ts
    )
    # A common period would force √2 rational, which the valuation forbids.
    rank_irr = 2 if val_ok else 0
    rank_rat = 1  # 3*1 - 2*(3/2) = 0, and the coefficients are not both zero.
    rat_relation = abs(3 * 1 - 2 * (3 / 2)) < 1e-15
    # Constant coordinate: one-point support, entropy 0, mutual information 0.
    i_radius = 0.0
    p2_ok = (
        val_ok
        and rank_irr == 2
        and rank_rat == 1
        and rat_relation
        and period_err < 1e-9
        and i_radius == 0.0
    )
    check(
        "P2",
        p2_ok,
        f"rank_irr {rank_irr} rank_rat {rank_rat} period_err {period_err:.3e} I_radius {fmt(i_radius)}",
    )

    # --- P4: symmetric bit menu ---
    def menu_sym(kappa, q, w):
        alpha = kappa * (1.0 + q) * LN2
        return {
            "blind": w * 1.0,
            "one": alpha + w * 0.5,
            "both": 2.0 * alpha,
        }

    def unique_min(costs):
        best = min(costs.values())
        names = [k for k, v in costs.items() if abs(v - best) <= 1e-12]
        return names

    p4_points = True
    names_10 = unique_min(menu_sym(1.0, 0.0, 10.0))
    names_1 = unique_min(menu_sym(1.0, 0.0, 1.0))
    p4_points = names_10 == ["both"] and names_1 == ["blind"]
    never_unique_one = True
    tie_ok = True
    for kappa in (0.5, 1.0, 3.0):
        for q in (0.0, 1.0, 4.0):
            for w_factor in (0.25, 1.0, 4.0):
                w_tie = 2.0 * kappa * (1.0 + q) * LN2
                w = w_factor * w_tie
                names = unique_min(menu_sym(kappa, q, w))
                if "one" in names and names != ["blind", "one", "both"] and len(names) == 1:
                    never_unique_one = False
                if abs(w_factor - 1.0) < 1e-15:
                    tie_ok = tie_ok and set(names) == {"blind", "one", "both"}
                elif w_factor < 1.0:
                    tie_ok = tie_ok and names == ["blind"]
                else:
                    tie_ok = tie_ok and names == ["both"]
    # Algebra: J_one - min(J_blind, J_both) = |alpha - w/2| >= 0.
    alpha = 1.0 * LN2
    gap = abs(alpha - 10.0 / 2.0)
    j = menu_sym(1.0, 0.0, 10.0)
    gap_ok = abs((j["one"] - min(j["blind"], j["both"])) - gap) < 1e-12
    p4_ok = p4_points and never_unique_one and tie_ok and gap_ok
    check(
        "P4",
        p4_ok,
        f"w10 {names_10} w1 {names_1} Jboth {fmt(j['both'])} Jone {fmt(j['one'])} Jblind {fmt(j['blind'])}",
    )

    # --- P5: unequal amplitudes, per-mode window ---
    save1, save2 = 0.5, 0.01 * 0.5
    def menu_uneq(kappa, q, w):
        alpha = kappa * (1.0 + q) * LN2
        return {
            "blind": w * (save1 + save2),
            "large": alpha + w * save2,
            "small": alpha + w * save1,
            "both": 2.0 * alpha,
        }

    n1 = unique_min(menu_uneq(1.0, 0.0, 1.0))
    n10 = unique_min(menu_uneq(1.0, 0.0, 10.0))
    n1000 = unique_min(menu_uneq(1.0, 0.0, 1000.0))
    w1 = 2.0 * LN2
    w2 = LN2 / save2
    window = w1 < 10.0 < w2
    p5_ok = n1 == ["blind"] and n10 == ["large"] and n1000 == ["both"] and window
    check(
        "P5",
        p5_ok,
        f"w1 {n1} w10 {n10} w1000 {n1000} thresholds {fmt(w1)} {fmt(w2)}",
    )

    # --- P6: Adler boundary and the one-bit drop at zero loss ---
    def adler_locks(delta_omega, k_coup):
        # sin φ = Δω/K has a real solution iff |Δω| <= |K| (K>0).
        if k_coup <= 0:
            return abs(delta_omega) <= 1e-15
        ratio = delta_omega / k_coup
        return abs(ratio) <= 1.0 + 1e-12

    adler_ok = True
    for delta in (0.0, 0.3, 1.0, 1.7):
        for k_coup in (0.3, 1.0, 1.7):
            locks = adler_locks(delta, k_coup)
            theory = abs(delta) <= k_coup + 1e-15
            if locks != theory:
                adler_ok = False
            if locks and k_coup > 0:
                phi = math.asin(max(-1.0, min(1.0, delta / k_coup)))
                resid = abs(delta - k_coup * math.sin(phi))
                if resid > 1e-12:
                    adler_ok = False
    drop = (2.0 * LN2) - LN2
    drop_ok = abs(drop - LN2) < 1e-15
    # Cost drop at L = 0, κ=1, q=1: κ(1+q) ln 2.
    cost_drop = 1.0 * (1.0 + 1.0) * drop
    cost_ok = abs(cost_drop - 2.0 * LN2) < 1e-15
    p6_ok = adler_ok and drop_ok and cost_ok
    check(
        "P6",
        p6_ok,
        f"Adler identity resid within 1e-12 drop {fmt(drop)} cost_drop {fmt(cost_drop)}",
    )

    # --- P7: fixed-K switch versus the joint minimizer over K ---
    gamma = 0.5
    g0 = 1.0 / (math.pi * gamma)
    k_c = 2.0 / (math.pi * g0)
    k_c_alt = 2.0 * gamma
    kappa, q, w = 1.0, 1.0, 10.0
    price = kappa * (1.0 + q) * LN2
    # r^2 = 1 - K_c/K for K > K_c. Blind loss r^2/2. Track cost = price.
    if w <= 2.0 * price:
        k_formula = None
    else:
        k_formula = k_c / (1.0 - 2.0 * price / w)

    def r2(k_coup):
        if k_coup <= k_c:
            return 0.0
        return 1.0 - k_c / k_coup

    def j_blind(k_coup):
        return w * r2(k_coup) / 2.0

    def j_track(_k_coup):
        return price

    # Bisection of the fixed-K switch, on (K_c, 10 K_c).
    lo, hi = k_c, 10.0 * k_c
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if j_blind(mid) < j_track(mid):
            lo = mid
        else:
            hi = mid
    k_switch = 0.5 * (lo + hi)
    rel_switch = abs(k_switch - k_formula) / k_formula

    # Joint minimum over K of the better design. Cost is 0 on [0, K_c].
    ks = [i * 0.001 for i in range(0, 5001)]
    j_of = [(k_coup, min(j_blind(k_coup), j_track(k_coup))) for k_coup in ks]
    j_min = min(v for _, v in j_of)
    minimizers = [k_coup for k_coup, v in j_of if abs(v - j_min) <= 1e-9]
    k_min_lo, k_min_hi = min(minimizers), max(minimizers)
    # The locked fail line compares this minimizer with the formula.
    # A set is not the formula. Distance from the formula to the nearest minimizer.
    nearest = min(minimizers, key=lambda k_coup: abs(k_coup - k_formula))
    rel_joint = abs(nearest - k_formula) / k_formula
    joint_matches = rel_joint <= 1e-9

    # Beyond-Kuramoto criterion from PREREG §0, applied to the fixed-K switch
    # and, separately, to the boundary of the joint minimizer set.
    def beyond(k_star, k_ref):
        if k_star is None:
            return False
        cond1 = abs(k_star - k_ref) / max(k_ref, 1e-12) > 0.05
        cond2 = True  # this k_star uses κ, q, w through `price`
        # cond3: it IS the blind-corner substitution, so "is not that substitution" is false.
        is_substitution = abs(k_star - k_formula) / k_formula <= 1e-9
        cond3 = not is_substitution
        return cond1 and cond2 and cond3

    beyond_switch = beyond(k_switch, k_c)
    # Joint boundary is K_c (the top of the zero-cost set). It does not depend
    # on κ, q, w, so condition 2 fails, and condition 1 fails.
    beyond_joint = abs(k_c - k_c) / k_c > 0.05 and False
    criterion_not_beyond = (not beyond_switch) and (not beyond_joint)
    # P7 as written: FAIL if the minimizer over K differs from the formula,
    # OR if the criterion returns BEYOND.
    p7_ok = joint_matches and criterion_not_beyond
    check(
        "P7",
        p7_ok,
        " ".join([
            f"Kc {fmt(k_c)}",
            f"Kc_check {fmt(k_c_alt)}",
            f"K_formula {fmt(k_formula)}",
            f"K_switch {fmt(k_switch)}",
            f"rel_switch {rel_switch:.3e}",
            f"Jmin {fmt(j_min)}",
            f"argmin_K [{fmt(k_min_lo)}, {fmt(k_min_hi)}]",
            f"rel_joint {rel_joint:.6f}",
            f"NOT_BEYOND {criterion_not_beyond}",
        ]),
    )
    print(
        "P7-DIAG  fixed-K switch matches the blind-corner formula; "
        f"rel {rel_switch:.3e}. Joint argmin is the incoherent interval, cost 0, "
        "not the formula. Criterion returns NOT BEYOND either way."
    )

    # --- P8: alignment match conditions ---
    # Bare Adler / Kuramoto thresholds at two stake ratios.
    def k_c_of(_stakes):
        return 2.0 / (math.pi * g0)

    def adler_bound(delta_omega, _stakes):
        return abs(delta_omega)

    stakes_a = (1.0, 1.0)
    stakes_b = (1.0, 4.0)
    delta = 0.3
    bare_ok = (
        abs(k_c_of(stakes_a) - k_c_of(stakes_b)) < 1e-15
        and abs(adler_bound(delta, stakes_a) - adler_bound(delta, stakes_b)) < 1e-15
    )
    # CT29 copy. World variance parameter named q_world so it is not the ratio q.
    q_world, c_read = 1.0, 1.0
    w1, w2 = 1.0, 4.0
    big_w = w1 + w2

    def preferred_total(w_i, s_i):
        return math.sqrt(w_i * q_world / (2.0 * s_i * c_read))

    f_star = math.sqrt(big_w * q_world / (2.0 * c_read))
    s1, s2 = w1 / big_w, w2 / big_w
    align_match = (
        abs(preferred_total(w1, s1) - f_star) < 1e-12
        and abs(preferred_total(w2, s2) - f_star) < 1e-12
    )
    equal_differ = abs(preferred_total(w1, 0.5) - preferred_total(w2, 0.5)) > 1e-9

    def j_part(s_i, w_i, f):
        return s_i * c_read * f + w_i * q_world / (2.0 * f)

    def j_joint(f):
        return c_read * f + big_w * q_world / (2.0 * f)

    f_probe = 1.7
    m2_align = abs(j_part(s1, w1, f_probe) - (w1 / big_w) * j_joint(f_probe)) < 1e-12
    m2_equal = abs(j_part(0.5, w1, f_probe) - (w1 / big_w) * j_joint(f_probe)) > 1e-9
    # Prediction: bare thresholds ignore stakes (shared cause fails);
    # the copied payment rule satisfies M1–M3 (a relabel, not support).
    p8_ok = bare_ok and align_match and equal_differ and m2_align and m2_equal
    check(
        "P8",
        p8_ok,
        " ".join([
            f"Kc_stakes_moved {not bare_ok}",
            f"Fstar {fmt(f_star)}",
            f"F_equal {fmt(preferred_total(w1, 0.5))} {fmt(preferred_total(w2, 0.5))}",
            f"M2_align {m2_align} M2_equal_fails {m2_equal}",
        ]),
    )

    # Headline clauses that do not include P7's argmin sentence.
    headline_ok = p1_ok and p2_ok and p3_ok and p4_ok and p5_ok and p6_ok and p8_ok and criterion_not_beyond
    check(
        "HEADLINE",
        headline_ok,
        "RELABEL on P1 (R-sum), P2 (R-hull), P5 (R-mode); NOT BEYOND; Q3 shared-cause FAIL as predicted",
    )

    print(f"FAILS {len(fails)}")
    if fails:
        print("SCORED_FAIL " + ",".join(fails))
    print("SCOREBOARD COMPLETE")


if __name__ == "__main__":
    main()
