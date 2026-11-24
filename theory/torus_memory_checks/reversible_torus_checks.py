"""T82b closed reversible torus. Criteria are PREREG_REVERSIBLE.md.

The preregistration is not read for numbers. No random module.
A miss is printed. It does not change the lock.
"""
from __future__ import annotations

import hashlib
import math
import os

BETA = 0.25
H = 0.05
N_STEPS = 2000
N_PATH = 32
DELTA = 1e-6
REV_TOL = 1e-4
VOL_ONE = 1e-6
VOL_FIFTY = 1e-3
P1_PAIR = 1e-4
P1_ACT = 1e-3
Q_ANGLE = 0.02
Q_ACTION = 0.02
Q_RATIONAL = 0.05
NU_FREE = 1e-6
RAT_PERIODIC = 1e-4
RAT_QUASI = 1e-3
TONGUE_TOL = 1e-3
REL_GAP = 0.05
HALF_WIN = 0.5

LOCKED_HASH = "84b5cd7fb8c4e843ae1f54e837cdca1fec603c57916f6d1787716ca6cf0988dc"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG_REVERSIBLE.md")

TWOPI = 2.0 * math.pi
OMEGA10 = 1.0
FAMILIES = (
    ("rat", 1.5),
    ("irr", math.sqrt(2.0)),
    ("gold", (math.sqrt(5.0) - 1.0) / 2.0),
)
ACTIONS = (-0.4, -0.2, 0.0, 0.2, 0.4)
ANGLES = tuple(TWOPI * k / 8.0 for k in range(8))
DELTAS = (-0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15)
P3_TIMES = (20.0, 40.0, 60.0, 80.0, 100.0)
PORT_MID = 0.239059227845
PORT_FAR = 0.048343059332


def fmt(x):
    return "%.12f" % x


def fmte(x):
    return "%.6e" % x


def wrap(x):
    """Principal value in (-pi, pi]."""
    y = math.fmod(x + math.pi, TWOPI)
    if y < 0.0:
        y += TWOPI
    y -= math.pi
    if y == -math.pi:
        return math.pi
    return y


def step_mass(p, c, contact):
    """T81 lazy step. contact is 'agent' or 'sink'."""
    n = len(p)
    new = [0.0] * n
    agent = 0.0
    sink = 0.0
    for j, mass in enumerate(p):
        if mass == 0.0:
            continue
        new[j] += 0.5 * mass
        if j > 0:
            new[j - 1] += 0.25 * mass
        else:
            if contact == "agent":
                agent += 0.25 * mass
            else:
                sink += 0.25 * mass
        if j < n - 1:
            new[j + 1] += 0.25 * mass
        else:
            new[j] += 0.25 * c * mass
            sink += 0.25 * (1.0 - c) * mass
    return new, agent, sink


def return_prob(n, starts, t, c, contact):
    """Agent mass after t steps, averaged over starts. Each start is mass 1."""
    if not starts:
        return 0.0
    acc = 0.0
    for s in starts:
        p = [0.0] * n
        p[s] = 1.0
        agent = 0.0
        for _ in range(t):
            p, a, _sink = step_mass(p, c, contact)
            agent += a
        acc += agent
    return acc / len(starts)


def horizon(omega2):
    return max(1, int(round(80.0 / omega2)))


def site_of(theta2):
    x = math.fmod(theta2, TWOPI)
    if x < 0.0:
        x += TWOPI
    s = int(math.floor(N_PATH * x / TWOPI))
    if s < 0 or s >= N_PATH:
        return 0
    return s


def force(theta, eps):
    s = math.sin(theta[0] - theta[1])
    return (-eps * s, eps * s)


def verlet(theta, action, h, eps, gamma, omega0):
    f = force(theta, eps)
    mid = (action[0] - 0.5 * h * f[0], action[1] - 0.5 * h * f[1])
    nxt = (
        theta[0] + h * (omega0[0] + BETA * mid[0]),
        theta[1] + h * (omega0[1] + BETA * mid[1]),
    )
    f2 = force(nxt, eps)
    end = (mid[0] - 0.5 * h * f2[0], mid[1] - 0.5 * h * f2[1])
    if gamma != 0.0:
        decay = math.exp(-gamma * h)
        end = (end[0] * decay, end[1] * decay)
    return nxt, end


def integers_crossed(tau0, tau1):
    if tau1 == tau0:
        return []
    out = []
    if tau1 > tau0:
        m = math.floor(tau0) + 1.0
        while m <= tau1:
            out.append(m)
            m += 1.0
    else:
        m = math.ceil(tau0) - 1.0
        while m >= tau1:
            out.append(m)
            m -= 1.0
    return out


def crossings(theta, action, theta2, action2):
    tau0 = theta[0] / TWOPI
    tau1 = theta2[0] / TWOPI
    span = tau1 - tau0
    if span == 0.0:
        return []
    samples = []
    for m in integers_crossed(tau0, tau1):
        frac = (m - tau0) / span
        samples.append((
            theta[1] + frac * (theta2[1] - theta[1]),
            action[0] + frac * (action2[0] - action[0]),
        ))
    return samples


def q_of(samples, table):
    if not samples:
        return None
    num = 0.0
    den = 0.0
    for th2, i1 in samples:
        rho = math.exp(i1)
        num += rho * table[site_of(th2)]
        den += rho
    if den == 0.0:
        return None
    return num / den


def rat_dist(nu, bound):
    best = None
    for b in range(1, bound + 1):
        for a in range(0, 2 * b + 1):
            d = abs(nu - (a / float(b)))
            if best is None or d < best:
                best = d
    return best


def classify(nu):
    if nu is None:
        return "OTHER"
    if rat_dist(nu, 8) <= RAT_PERIODIC:
        return "PERIODIC"
    if rat_dist(nu, 16) > RAT_QUASI:
        return "QUASIPERIODIC"
    return "OTHER"


def ang_dist(theta, theta0):
    return math.hypot(wrap(theta[0] - theta0[0]), wrap(theta[1] - theta0[1]))


def state_dist(a, b):
    return math.sqrt(
        wrap(a[0] - b[0]) ** 2
        + wrap(a[1] - b[1]) ** 2
        + (a[2] - b[2]) ** 2
        + (a[3] - b[3]) ** 2
    )


def integrate(theta0, action0, n, h, eps, gamma, omega0, table):
    theta = theta0
    action = action0
    samples = []
    min_ret = None
    half = n // 2
    for step in range(1, n + 1):
        theta2, action2 = verlet(theta, action, h, eps, gamma, omega0)
        samples.extend(crossings(theta, action, theta2, action2))
        theta, action = theta2, action2
        if step >= half:
            d = ang_dist(theta, theta0)
            if min_ret is None or d < min_ret:
                min_ret = d
    dth1 = theta[0] - theta0[0]
    nu = None if dth1 == 0.0 else (theta[1] - theta0[1]) / dth1
    return theta, action, nu, q_of(samples, table), min_ret


def det3(b, c, d, i, j, k):
    return (
        b[i] * (c[j] * d[k] - c[k] * d[j])
        - b[j] * (c[i] * d[k] - c[k] * d[i])
        + b[k] * (c[i] * d[j] - c[j] * d[i])
    )


def det4(rows):
    a, b, c, d = rows
    return (
        a[0] * det3(b, c, d, 1, 2, 3)
        - a[1] * det3(b, c, d, 0, 2, 3)
        + a[2] * det3(b, c, d, 0, 1, 3)
        - a[3] * det3(b, c, d, 0, 1, 2)
    )


def jacobian_det(n, eps, omega0, table):
    base_th = (0.0, 0.0)
    base_i = (0.0, 0.0)
    columns = []
    for k in range(4):
        def once(sign, k=k):
            th = [base_th[0], base_th[1]]
            act = [base_i[0], base_i[1]]
            if k < 2:
                th[k] += sign * DELTA
            else:
                act[k - 2] += sign * DELTA
            th2, act2, _nu, _q, _m = integrate(
                (th[0], th[1]), (act[0], act[1]), n, H, eps, 0.0, omega0, table
            )
            return (th2[0], th2[1], act2[0], act2[1])

        plus = once(1.0)
        minus = once(-1.0)
        columns.append(tuple((plus[i] - minus[i]) / (2.0 * DELTA) for i in range(4)))
    rows = tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))
    return det4(rows)


def build_tables(horizons):
    tables = {}
    for t in sorted(set(horizons)):
        tables[t] = tuple(
            return_prob(N_PATH, [s], t, 1.0, "agent") for s in range(N_PATH)
        )
    return tables


def table_for(omega2, tables):
    return tables[horizon(omega2)]


def range_of(values):
    if any(v is None for v in values):
        return None
    return max(values) - min(values)


def mean_of(values):
    if any(v is None for v in values):
        return None
    return sum(values) / float(len(values))


def smooth_ok(avg):
    if any(v is None for v in avg):
        return False, None, None
    first = [avg[i + 1] - avg[i] for i in range(len(avg) - 1)]
    second = [avg[i + 2] - 2.0 * avg[i + 1] + avg[i] for i in range(len(avg) - 2)]
    max_first = max(abs(d) for d in first)
    max_second = max(abs(s) for s in second)
    return max_second <= 0.5 * max_first, max_first, max_second


def longest_plateau(nus, deltas):
    flags = [nu is not None and abs(nu - 1.5) <= TONGUE_TOL for nu in nus]
    best = None
    i = 0
    while i < len(flags):
        if not flags[i]:
            i += 1
            continue
        j = i
        while j < len(flags) and flags[j]:
            j += 1
        length = j - i
        if length >= 3:
            span = deltas[j - 1] - deltas[i]
            if best is None or length > best[0]:
                best = (length, span / 2.0)
        i = j
    if best is None:
        return False, None
    return True, best[1]


def rel_diff(a, b):
    scale = max(abs(a), abs(b), 1e-12)
    return abs(a - b) / scale


def main():
    digest = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    fails = []
    if digest != LOCKED_HASH:
        print("P0 FAIL hash %s" % digest)
        print("FAILS 1")
        print("SCORED_FAIL P0")
        print("SCOREBOARD COMPLETE")
        return
    print("P0 PASS hash %s" % digest)

    port_mid = return_prob(N_PATH, [16], 415, 1.0, "agent")
    port_far = return_prob(N_PATH, [31], 415, 1.0, "agent")
    print("DIAG T81-port mid %s far %s" % (fmt(port_mid), fmt(port_far)))
    if abs(port_mid - PORT_MID) > 1e-12 or abs(port_far - PORT_FAR) > 1e-12:
        print("DIAG T81-port MISS")
        raise SystemExit(1)

    horizons = [horizon(w) for _name, w in FAMILIES]
    horizons.extend(horizon(1.5 + d) for d in DELTAS)
    tables = build_tables(horizons)
    empty = tuple(0.0 for _ in range(N_PATH))

    # I-rev
    rev_max = 0.0
    for _name, w20 in FAMILIES:
        for eps in (0.0, 0.05):
            omega = (OMEGA10, w20)
            th, act, _nu, _q, _m = integrate(
                (0.0, 0.0), (0.0, 0.0), N_STEPS, H, eps, 0.0, omega, empty
            )
            thb, actb, _nu, _q, _m = integrate(
                th, act, N_STEPS, -H, eps, 0.0, omega, empty
            )
            errs = (
                abs(actb[0]),
                abs(actb[1]),
                abs(wrap(thb[0])),
                abs(wrap(thb[1])),
            )
            rev_max = max(rev_max, max(errs))
    if rev_max <= REV_TOL:
        print("I-rev PASS max_err %s" % fmte(rev_max))
    else:
        print("I-rev FAIL max_err %s" % fmte(rev_max))
        fails.append("I-rev")

    omega_irr = (OMEGA10, math.sqrt(2.0))
    det1 = jacobian_det(1, 0.05, omega_irr, empty)
    det50 = jacobian_det(50, 0.05, omega_irr, empty)
    vol_ok = abs(det1 - 1.0) <= VOL_ONE and abs(det50 - 1.0) <= VOL_FIFTY
    mark = "PASS" if vol_ok else "FAIL"
    print("I-vol %s det1 %s det50 %s" % (mark, fmte(det1 - 1.0), fmte(det50 - 1.0)))
    if not vol_ok:
        fails.append("I-vol")

    # P1
    ends = []
    i1_at_zero = []
    for i1 in ACTIONS:
        for th2 in ANGLES:
            th, act, _nu, _q, _m = integrate(
                (0.0, th2), (i1, 0.0), N_STEPS, H, 0.0, 0.0, omega_irr, empty
            )
            ends.append((th[0], th[1], act[0], act[1]))
            if th2 == 0.0:
                i1_at_zero.append(act[0])
    pair_min = None
    for i in range(len(ends)):
        for j in range(i + 1, len(ends)):
            d = state_dist(ends[i], ends[j])
            if pair_min is None or d < pair_min:
                pair_min = d
    act_err = max(abs(i1_at_zero[k] - ACTIONS[k]) for k in range(len(ACTIONS)))
    p1_ok = pair_min >= P1_PAIR and act_err <= P1_ACT
    mark = "PASS" if p1_ok else "FAIL"
    print("P1 %s pair_min %s act_err %s" % (mark, fmte(pair_min), fmte(act_err)))
    if not p1_ok:
        fails.append("P1")

    def orbit_q(family_w, i1, th2, eps, gamma, n=N_STEPS):
        omega = (OMEGA10, family_w)
        table = table_for(family_w, tables)
        _th, _act, nu, q, min_ret = integrate(
            (0.0, th2), (i1, 0.0), n, H, eps, gamma, omega, table
        )
        return nu, q, min_ret

    # P2
    p2_ok = True
    for name, w20 in FAMILIES:
        if name == "rat":
            continue
        angle_ranges = []
        averages = []
        for i1 in ACTIONS:
            qs = [orbit_q(w20, i1, th2, 0.0, 0.0)[1] for th2 in ANGLES]
            angle_ranges.append(range_of(qs))
            averages.append(mean_of(qs))
        action_range = range_of(averages)
        ok_smooth, max_first, max_second = smooth_ok(averages)
        ang_max = None if any(r is None for r in angle_ranges) else max(angle_ranges)
        this = (
            ang_max is not None
            and ang_max <= Q_ANGLE
            and action_range is not None
            and action_range >= Q_ACTION
            and ok_smooth
        )
        p2_ok = p2_ok and this
        print(
            "P2-DETAIL %s ang_max %s act_range %s d1 %s d2 %s"
            % (
                name,
                fmt(ang_max) if ang_max is not None else "NONE",
                fmt(action_range) if action_range is not None else "NONE",
                fmte(max_first) if max_first is not None else "NONE",
                fmte(max_second) if max_second is not None else "NONE",
            )
        )
    print("P2 %s" % ("PASS" if p2_ok else "FAIL"))
    if not p2_ok:
        fails.append("P2")

    # P3
    w_rat = 1.5
    g0_qs = [orbit_q(w_rat, 0.0, th2, 0.0, 0.0)[1] for th2 in ANGLES]
    g0 = range_of(g0_qs)
    p3_ok = g0 is not None and g0 > Q_RATIONAL
    print("P3-G0 %s" % (fmt(g0) if g0 is not None else "NONE"))
    for gamma in (0.02, 0.05):
        series = []
        for t in P3_TIMES:
            n = int(round(t / H))
            qs = [orbit_q(w_rat, 0.0, th2, 0.0, gamma, n)[1] for th2 in ANGLES]
            series.append(range_of(qs))
            print(
                "P3-G gamma %s t %s G %s"
                % (fmt(gamma), fmt(t), fmt(series[-1]) if series[-1] is not None else "NONE")
            )
        half = None
        if g0 is not None:
            for t, g in zip(P3_TIMES, series):
                if g is not None and g <= 0.5 * g0:
                    half = t
                    break
        if half is None or g0 is None:
            p3_ok = False
            print("P3-HALF gamma %s t NONE" % fmt(gamma))
        else:
            score = abs(gamma * half / math.log(2.0) - 1.0)
            print("P3-HALF gamma %s t %s score %s" % (fmt(gamma), fmt(half), fmt(score)))
            if score > HALF_WIN:
                p3_ok = False
    print("P3 %s" % ("PASS" if p3_ok else "FAIL"))
    if not p3_ok:
        fails.append("P3")

    # P4
    p4_ok = True
    ranges = {}
    for name, w20 in FAMILIES:
        nus = []
        qs = []
        classes = []
        min_rets = []
        for th2 in ANGLES:
            nu, q, min_ret = orbit_q(w20, 0.0, th2, 0.0, 0.0)
            nus.append(nu)
            qs.append(q)
            classes.append(classify(nu))
            min_rets.append(min_ret)
            if nu is None or abs(nu - w20 / OMEGA10) > NU_FREE:
                p4_ok = False
        ranges[name] = range_of(qs)
        want = "PERIODIC" if name == "rat" else "QUASIPERIODIC"
        if any(c != want for c in classes):
            p4_ok = False
        print(
            "P4-DETAIL %s q_range %s class %s min_ret %s nu_err %s"
            % (
                name,
                fmt(ranges[name]) if ranges[name] is not None else "NONE",
                " ".join(classes),
                fmte(min(min_rets)),
                fmte(max(abs(nu - w20 / OMEGA10) for nu in nus)),
            )
        )
    if ranges["rat"] is None or ranges["rat"] <= Q_RATIONAL:
        p4_ok = False
    if ranges["irr"] is None or ranges["irr"] >= Q_ANGLE:
        p4_ok = False
    if ranges["gold"] is None or ranges["irr"] is None or ranges["gold"] > ranges["irr"]:
        p4_ok = False
    shifts = {}
    for name, w20 in FAMILIES:
        if name == "irr":
            continue
        nu0 = orbit_q(w20, 0.0, 0.0, 0.0, 0.0)[0]
        nu1 = orbit_q(w20, 0.0, 0.0, 0.05, 0.0)[0]
        shifts[name] = None if nu0 is None or nu1 is None else abs(nu1 - nu0)
        print(
            "P4-SHIFT %s %s" % (name, fmt(shifts[name]) if shifts[name] is not None else "NONE")
        )
    if shifts["gold"] is None or shifts["rat"] is None or shifts["gold"] > shifts["rat"]:
        p4_ok = False
    print("P4 %s" % ("PASS" if p4_ok else "FAIL"))
    if not p4_ok:
        fails.append("P4")

    # Tongues and the Kuramoto comparison.
    tongue = {}
    for eps, gamma in ((0.0, 0.0), (0.05, 0.0), (0.05, 0.02), (0.05, 0.05)):
        nus = []
        for delta in DELTAS:
            omega = (OMEGA10, 1.5 + delta)
            table = table_for(1.5 + delta, tables)
            _th, _act, nu, _q, _m = integrate(
                (0.0, 0.0), (0.0, 0.0), N_STEPS, H, eps, gamma, omega, table
            )
            nus.append(nu)
            print(
                "TONGUE eps %s gamma %s delta %s nu %s"
                % (fmt(eps), fmt(gamma), fmt(delta), fmt(nu) if nu is not None else "NONE")
            )
        has, width = longest_plateau(nus, DELTAS)
        tongue[(eps, gamma)] = (has, width)
        print(
            "TONGUE-RUN eps %s gamma %s plateau %s width %s"
            % (fmt(eps), fmt(gamma), "YES" if has else "NO", fmt(width) if width is not None else "NONE")
        )
    tongue_ok = (
        not tongue[(0.0, 0.0)][0]
        and not tongue[(0.05, 0.0)][0]
        and tongue[(0.05, 0.05)][0]
    )
    print("P4-tongue %s" % ("PASS" if tongue_ok else "FAIL"))
    if not tongue_ok:
        fails.append("P4-tongue")

    width = tongue[(0.05, 0.05)][1]
    circle = 0.05 / math.pi
    if width is None:
        print("P-kc FAIL no-width")
        fails.append("P-kc")
        gap = None
    else:
        gap = abs(width / circle - 1.0)
        differ = gap > REL_GAP
        if differ:
            print("P-kc PASS DIFFER gap %s width %s" % (fmt(gap), fmt(width)))
        else:
            print("P-kc FAIL MATCH gap %s width %s" % (fmt(gap), fmt(width)))
            fails.append("P-kc")

    w_lo = tongue[(0.05, 0.02)][1]
    w_hi = tongue[(0.05, 0.05)][1]
    beyond = False
    if w_hi is not None and w_lo is not None:
        away_eps = rel_diff(w_hi, 0.05) > REL_GAP
        away_circle = rel_diff(w_hi, circle) > REL_GAP
        gammas_differ = rel_diff(w_lo, w_hi) > REL_GAP
        ratio_lo = w_lo / 0.02
        ratio_hi = w_hi / 0.05
        ratio_moves = rel_diff(ratio_lo, ratio_hi) > REL_GAP
        beyond = away_eps and away_circle and gammas_differ and ratio_moves
        print(
            "BEYOND-DETAIL away_eps %s away_circle %s gamma_diff %s ratio_moves %s"
            % (away_eps, away_circle, gammas_differ, ratio_moves)
        )
    else:
        print("BEYOND-DETAIL missing-width")
    if beyond:
        print("BEYOND FAIL BEYOND")
        fails.append("BEYOND")
    else:
        print("BEYOND PASS NOT_BEYOND")

    print("FAILS %d" % len(fails))
    if fails:
        print("SCORED_FAIL %s" % " ".join(fails))
    else:
        print("SCORED_FAIL none")
    print("SCOREBOARD COMPLETE")


if __name__ == "__main__":
    main()
