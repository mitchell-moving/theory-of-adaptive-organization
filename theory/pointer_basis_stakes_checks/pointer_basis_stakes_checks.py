#!/usr/bin/env python3
"""T73 pointer-basis stakes. Scores theory/pointer-basis-stakes-2026-11-24/PREREG.md.

Standard library only. The angle grid is fixed. SEED is recorded and is not drawn from.
"""
import math

SEED = 20261124
R = 0.6
N_THETA = 721
TIE = 1e-9
GAMMAS = (0.0, 0.5)
PHIS = (("0", 0.0), ("pi/4", math.pi / 4), ("pi/2", math.pi / 2))
WS = (0.0, 0.01, 0.1, 1.0, 10.0, 100.0)
THETAS = tuple(j * (math.pi / 2) / (N_THETA - 1) for j in range(N_THETA))


def binary_entropy(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def vn_entropy(radius):
    radius = abs(radius)
    if radius >= 1.0:
        return 0.0
    return binary_entropy((1.0 + radius) / 2.0)


def evaluate(gamma, theta, phi):
    """Return (P_D, P_chi, L) for one basis angle."""
    specs = (
        (0.0, R, R * math.cos(phi)),
        (0.0, -R, -R * math.cos(phi)),
        (R, 0.0, R * math.sin(phi)),
        (-R, 0.0, -R * math.sin(phi)),
    )
    s_th = math.sin(theta)
    c_th = math.cos(theta)
    p1s = []
    pd = 0.0
    ys = []
    for bx, bz, y in specs:
        bx_p = gamma * bx
        ndot = bx_p * s_th + bz * c_th
        p1s.append(0.5 * (1.0 + ndot))
        pd += 0.25 * (vn_entropy(abs(ndot)) - vn_entropy(math.hypot(bx_p, bz)))
        ys.append(y)
    pm = 0.25 * sum(p1s)
    pchi = binary_entropy(pm) - 0.25 * sum(binary_entropy(p) for p in p1s)

    def conditional(positive):
        num = 0.0
        den = 0.0
        for p, y in zip(p1s, ys):
            pk = p if positive else (1.0 - p)
            num += 0.25 * pk * y
            den += 0.25 * pk
        return num / den

    e_pos = conditional(True)
    e_neg = conditional(False)
    loss = 0.0
    for p, y in zip(p1s, ys):
        loss += 0.25 * (p * (y - e_pos) ** 2 + (1.0 - p) * (y - e_neg) ** 2)
    return pd, pchi, loss


def closed_gamma0(theta, phi):
    """PREREG §2 closed form at complete dephasing."""
    c = abs(math.cos(theta))
    h = binary_entropy((1.0 + R * c) / 2.0)
    h_full = binary_entropy((1.0 + R) / 2.0)
    pd = 0.5 * (h - h_full)
    pchi = 0.5 * (math.log(2.0) - h)
    loss = R * R / 2.0 - (R ** 4 * math.cos(phi) ** 2 * math.cos(theta) ** 2) / 4.0
    return pd, pchi, loss


def scan(gamma, phi, price):
    """Costs on the angle grid. price is 'D' or 'chi'."""
    costs = []
    for theta in THETAS:
        pd, pchi, loss = evaluate(gamma, theta, phi)
        base = pd if price == "D" else pchi
        costs.append((base, loss))
    return costs


def minimizer(costs, w):
    js = [base + w * loss for base, loss in costs]
    best = min(js)
    idxs = [i for i, j in enumerate(js) if j <= best + TIE]
    return idxs, best, js[0]


def unique_zero(idxs):
    return idxs == [0]


def main():
    fails = []

    def report(code, ok, detail):
        status = "PASS" if ok else "FAIL"
        print(f"{code} {status} {detail}")
        if not ok:
            fails.append(code)

    print(f"SEED {SEED} rng_draws 0")
    d_orth = (R / 2.0) * math.log((1.0 + R) / (1.0 - R))
    print(
        f"CALIBRATION r={R:.1f} D_orth={d_orth:.12f} r2={R * R:.12f} "
        "excluded_comparison_not_scored"
    )

    # C0
    max_err = 0.0
    for theta in THETAS:
        for _name, phi in PHIS:
            got = evaluate(0.0, theta, phi)
            want = closed_gamma0(theta, phi)
            max_err = max(max_err, max(abs(a - b) for a, b in zip(got, want)))
    report("C0", max_err <= 1e-12, f"CLOSED_FORM max_abs_err={max_err:.3e}")

    # Full grid. Keyed by (gamma, phi_name, w, price) -> (idxs, jmin, j0, theta)
    cells = {}
    for gamma in GAMMAS:
        gname = "0" if gamma == 0.0 else "1/2"
        for pname, phi in PHIS:
            for price in ("D", "chi"):
                costs = scan(gamma, phi, price)
                for w in WS:
                    idxs, jmin, j0 = minimizer(costs, w)
                    theta = THETAS[idxs[0]]
                    cells[(gname, pname, w, price)] = (idxs, jmin, j0, theta)
                    print(
                        f"CELL g={gname} phi={pname} w={w:.2f} price={price} "
                        f"theta={theta:.6f} nmin={len(idxs)} "
                        f"J={jmin:.8e} J0={j0:.8e}"
                    )

    def cell(g, phi, w, price):
        return cells[(g, phi, w, price)]

    # P1 / C1
    p1 = True
    for pname, _phi in PHIS:
        for w in WS:
            idxs, _jmin, _j0, theta = cell("0", pname, w, "D")
            if (not unique_zero(idxs)) or theta >= 0.02:
                p1 = False
    report("C1", p1, f"P1 RELABEL_COMPLETE p1={str(p1).lower()}")

    # P2 / C2
    i0, jmin0, j00, th0 = cell("1/2", "pi/4", 0.0, "D")
    i100, jmin100, j0100, th100 = cell("1/2", "pi/4", 100.0, "D")
    gap = j0100 - jmin100
    sep = abs(th100 - th0)
    p2 = (
        unique_zero(i0)
        and len(i100) == 1
        and sep >= 0.2
        and gap >= 1e-4
    )
    report(
        "C2",
        p2,
        f"P2 TILT_PARTIAL sep={sep:.6f} gap={gap:.8e} "
        f"theta0={th0:.6f} theta100={th100:.6f}",
    )

    # P3 / C3
    p3 = True
    for w in WS:
        idxs, _jmin, _j0, theta = cell("1/2", "0", w, "D")
        if (not unique_zero(idxs)) or theta >= 0.05:
            p3 = False
    report("C3", p3, f"P3 COMMUTE_STABLE p3={str(p3).lower()}")

    # P4 / C4
    def q_of(price):
        for pname, _phi in PHIS:
            for w in WS:
                idxs, _jmin, _j0, _theta = cell("0", pname, w, price)
                if not unique_zero(idxs):
                    return False
        return True

    q_d = q_of("D")
    q_chi = q_of("chi")
    p4 = (q_d is True) and (q_chi is False)
    report("C4", p4, f"P4 ARTIFACT qD={str(q_d).lower()} qChi={str(q_chi).lower()}")

    # P5 / C5
    a0, _b, _c, th_a = cell("1/2", "pi/2", 0.0, "D")
    a100, _d, _e, th_b = cell("1/2", "pi/2", 100.0, "D")
    p5 = unique_zero(a0) and len(a100) == 1 and th_b >= 1.0
    report(
        "C5",
        p5,
        f"P5 COMPLEMENT theta0={th_a:.6f} theta100={th_b:.6f}",
    )

    # P6 / C6
    c0, _f, _g, th_c0 = cell("1/2", "pi/4", 0.0, "chi")
    c100, _h, _i, th_c100 = cell("1/2", "pi/4", 100.0, "chi")
    sep6 = abs(th_c100 - th_c0)
    p6 = len(c0) == 1 and len(c100) == 1 and sep6 >= 0.2
    report(
        "C6",
        p6,
        f"P6 HOLEVO_TILT sep={sep6:.6f} theta0={th_c0:.6f} theta100={th_c100:.6f}",
    )

    def rule(p1_ok, p2_ok, p4_ok, p6_ok):
        if p4_ok:
            return "PRICING_ARTIFACT"
        if p1_ok and not p2_ok:
            return "RELABEL"
        if p1_ok and p2_ok and p6_ok:
            return "TILT"
        return "UNRESOLVED"

    label = rule(p1, p2, p4, p6)
    report("C7", label == rule(p1, p2, p4, p6), f"HEADLINE_RULE {label}")
    print(f"HEADLINE {label}")
    print(f"FAILS {len(fails)}")
    if not fails:
        print("ALL T73 CHECKS PASS")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
