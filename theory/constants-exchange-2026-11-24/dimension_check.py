#!/usr/bin/env python3
"""Dimension check for theory/constants-exchange-2026-11-24.

Locked to PREREG.md. Checks that the published and repository formulas have
the dimensions claimed, then scores each one by the locked monomials (A), (B),
(F1), (F2), (F3). A scientific miss does not fail this script: the identities
are what the exit code reports. Deterministic. No network. No randomness.
"""
import sympy as sp

M, L, T, Theta = sp.symbols("M L T Theta", positive=True)

k_B = M * L**2 * T**(-2) * Theta**(-1)
hbar = M * L**2 * T**(-1)
c = L / T
G = L**3 / (M * T**2)
energy = M * L**2 / T**2
power = energy / T
nat = sp.Integer(1)
rate = 1 / T  # a rate the cost already takes from the world or the clock


def show(expr):
    return str(sp.simplify(expr))


def identity(expr, target):
    ratio = sp.simplify(expr / target)
    ok = ratio == 1 and not (ratio.free_symbols & {M, L, T, Theta})
    return ok, show(ratio)


def score(constants, kind, energy_named, extras):
    """Apply the locked rule. constants, extras are tuples of names."""
    cset = set(constants)
    xset = set(extras)
    reasons = []
    mixed = (
        ("k_B" in cset and "hbar" in cset)
        or (("k_B" in cset or "hbar" in cset) and ("c" in cset or "G" in cset))
        or ("c" in cset and "G" in cset)
    )
    if mixed:
        reasons.append("F1")
    if "c" in cset or "G" in cset or xset:
        reasons.append("F3")
    if kind == "time" and not energy_named:
        if "F3" not in reasons:
            reasons.append("F3")
    allowed_a = kind in ("energy", "power") and cset == {"k_B"} and not xset
    allowed_b = (
        kind == "time" and cset == {"hbar"} and energy_named and not xset
    )
    if not reasons and (allowed_a or allowed_b):
        tag = "A" if allowed_a else "B"
        return "pass " + tag
    if not reasons:
        reasons.append("F2")
    return "fail " + "+".join(reasons)


# id, bridge, constant label, combination text, expression, target, kind,
# constants, energy named by the cost, extra dimensionful inputs
ROWS = [
    (
        "erasure",
        "Landauer",
        "k_B",
        "k_B*T*nats",
        k_B * Theta * nat,
        energy,
        "energy",
        ("k_B",),
        True,
        (),
    ),
    (
        "ongoing-heat",
        "Horowitz-Esposito",
        "k_B",
        "k_B*T*(nats/time)",
        k_B * Theta * rate,
        power,
        "power",
        ("k_B",),
        True,
        (),
    ),
    (
        "tracking",
        "CT7-OU-telegraph",
        "k_B",
        "k_B*T*rate",
        k_B * Theta * rate,
        power,
        "power",
        ("k_B",),
        True,
        (),
    ),
    (
        "clock",
        "Barato-Seifert",
        "k_B",
        "k_B*T*(omega^2/D)",
        k_B * Theta * rate,
        power,
        "power",
        ("k_B",),
        True,
        (),
    ),
    (
        "ml-tracking",
        "Margolus-Levitin",
        "hbar",
        "hbar/(E-E0)",
        hbar / energy,
        T,
        "time",
        ("hbar",),
        False,
        ("energy",),
    ),
    (
        "ml-landauer",
        "Margolus-Levitin+Landauer",
        "k_B+hbar",
        "hbar/(k_B*T)",
        hbar / (k_B * Theta),
        T,
        "time",
        ("k_B", "hbar"),
        True,
        (),
    ),
    (
        "mt",
        "Mandelstam-Tamm",
        "hbar",
        "hbar/DeltaE",
        hbar / energy,
        T,
        "time",
        ("hbar",),
        False,
        ("energy",),
    ),
    (
        "bekenstein-1981",
        "Bekenstein-1981",
        "hbar+c",
        "E*R/(hbar*c)",
        energy * L / (hbar * c),
        nat,
        "dimensionless",
        ("hbar", "c"),
        True,
        ("length",),
    ),
    (
        "stock-printed",
        "SCALE_ENDS-entropy",
        "hbar+c+G",
        "G*mass^2/(hbar*c)",
        G * M**2 / (hbar * c),
        nat,
        "dimensionless",
        ("hbar", "c", "G"),
        True,
        ("mass",),
    ),
]


def main():
    print("basis M L T Theta")
    print("k_B = " + show(k_B))
    print("hbar = " + show(hbar))
    print("c = " + show(c))
    print("G = " + show(G))
    print("energy = " + show(energy))
    print("power = " + show(power))
    print(
        "note clock-and-tracking-rate: phase taken dimensionless, so a phase "
        "rate and a phase diffusion are both 1/time and their ratio omega^2/D "
        "is 1/time; a world variance rate over an error in the same units is "
        "1/time. Neither rate is a new constant."
    )
    print(
        "note ml-if-named: hbar/(E-E0) is monomial B when that energy is "
        "supplied. The cost does not name E-E0, so the tracking use is F3."
    )
    bad = []
    n_pass = 0
    n_fail = 0
    for row in ROWS:
        rid, bridge, clabel, combo, expr, target, kind, constants, named, extras = row
        ok, ratio = identity(expr, target)
        flag = "OK" if ok else "BROKEN"
        print(
            "identity %s: (%s) / target = %s %s"
            % (rid, combo, ratio, flag)
        )
        if not ok:
            bad.append(rid)
        mark = score(constants, kind, named, extras)
        if mark.startswith("pass"):
            n_pass += 1
        else:
            n_fail += 1
        print(
            "score %s | %s | %s | %s | %s | %s"
            % (rid, bridge, clabel, combo, kind, mark)
        )
    n_fail += 1
    print(
        "reading lloyd-2000: abstract names c, hbar and G together; "
        "no formula dimension-checked; score fail F1+F3"
    )
    if bad:
        print("DIMENSIONS BROKEN " + " ".join(bad))
        return 1
    print("DIMENSIONS OK")
    print("scientific pass %d" % n_pass)
    print("scientific fail %d" % n_fail)
    print("count includes the lloyd reading; that line is not an identity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
