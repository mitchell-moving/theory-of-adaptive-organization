"""T82c horizon scan. Criteria are PREREG_HORIZON.md.

The preregistration is not read for numbers. No random module.
A miss is printed. It does not change the lock.
"""
from __future__ import annotations

import hashlib
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reversible_torus_checks as flow

R = 0.6
TIE = 1e-9
PD_EPS = 1e-15
W_MAX = 9
STOP = 1e-4
ITERS = 40
DIAM = 0.02
N = 32
H = 0.05
LOCKED_HASH = "abb56169340490e2a420d47f5c0cb556e90e86caf720a2a86d5423a4c5ee85d9"
ROOT = os.path.dirname(os.path.dirname(HERE))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG_HORIZON.md")

FAMILIES = (
    ("rat", 1.5),
    ("irr", math.sqrt(2.0)),
    ("gold", (math.sqrt(5.0) - 1.0) / 2.0),
)
TIMES = (20.0, 40.0, 60.0, 80.0, 100.0)
WALK_T = (104, 208, 415, 500, 831, 1661, 3323, 6646, 13291, 26582, 83069)
STARTS = (0.0, 0.25, 0.5, 0.75, 1.0)
SCAN_LO = 416
SCAN_HI = 830
CLAMPS = [0]


def fmt(x):
    return "%.12f" % x


def fmte(x):
    return "%.6e" % x


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    q = 1.0 - p
    return -p * math.log(p) - q * math.log(q)


def closed_form_ant(theta, phi):
    cabs = abs(math.cos(theta))
    hp = hbin(0.5 * (1.0 + R * cabs))
    hr = hbin(0.5 * (1.0 + R))
    p_d = 0.5 * (hp - hr)
    info = 0.5 * (math.log(2.0) - hp)
    loss = 0.5 * R * R - (R ** 4) * (math.cos(phi) ** 2) * (math.cos(theta) ** 2) / 4.0
    return info, p_d, loss


def widths_for(phi, w, q, pd_top):
    best = None
    rows = []
    for j in range(181):
        th = j * (math.pi / 2.0) / 180.0
        info, pd, loss = closed_form_ant(th, phi)
        cost = info + q * pd + w * loss
        rows.append((cost, pd))
        if best is None or cost < best:
            best = cost
    found = []
    seen = set()
    for cost, pd in rows:
        if cost > best + TIE:
            continue
        width = 1 + math.floor(8.0 * pd / pd_top + PD_EPS)
        if width < 1 or width > W_MAX:
            CLAMPS[0] += 1
            if width < 1:
                width = 1
            if width > W_MAX:
                width = W_MAX
        if width not in seen:
            seen.add(width)
            found.append(width)
    return found


def block_sites(n, width):
    j0 = n // 2
    raw = list(range(j0 - (width // 2), j0 + (width // 2) + 1))
    return [j for j in raw if 0 <= j < n]


def q_width_factory(t, cache):
    def q_of(width):
        if width not in cache:
            cache[width] = flow.return_prob(N, block_sites(N, width), t, 1.0, "agent")
        return cache[width]

    return q_of


def iterate(phi, w, q_of, pd_top):
    traces = []
    terminals = []
    stopped = []
    for q0 in STARTS:
        q = q0
        updates = []
        did = False
        for _ in range(ITERS):
            ws = widths_for(phi, w, q, pd_top)
            nxt = sum(q_of(width) for width in ws) / float(len(ws))
            updates.append(nxt)
            if abs(nxt - q) <= STOP:
                did = True
                q = nxt
                break
            q = nxt
        traces.append(updates)
        stopped.append(did)
        if did:
            terminals.append(q)
    if not all(stopped):
        return "CYCLE", terminals, traces, stopped, None
    mean_t = sum(terminals) / float(len(terminals))
    ws = widths_for(phi, w, mean_t, pd_top)
    rets = [q_of(width) for width in ws]
    spread = max(rets) - min(rets) if rets else 0.0
    diam = max(terminals) - min(terminals)
    kind = "POINT" if diam <= DIAM and spread <= DIAM else "SET"
    return kind, terminals, traces, stopped, spread


def period2(updates):
    if len(updates) < 6:
        return False, None, None
    tail = updates[-6:]
    evens = tail[0::2]
    odds = tail[1::2]
    if max(evens) - min(evens) > 1e-9:
        return False, None, None
    if max(odds) - min(odds) > 1e-9:
        return False, None, None
    even = sum(evens) / 3.0
    odd = sum(odds) / 3.0
    if abs(even - odd) <= 1e-4:
        return False, None, None
    return True, even, odd


def trace(omega0, th2, n, gamma, dephase):
    theta = (0.0, th2)
    action = (0.0, 0.0)
    samples = []
    for step in range(1, n + 1):
        theta2, action2 = flow.verlet(theta, action, H, 0.0, 0.0, omega0)
        for th_s, i1 in flow.crossings(theta, action, theta2, action2):
            samples.append((step, th_s, i1))
        theta, action = theta2, action2
        if dephase and gamma != 0.0:
            decay = math.exp(-gamma * H)
            action = (action[0] * decay, action[1] * decay)
            theta = (theta[0], flow.wrap(theta[1]) * decay)
    return samples, theta, action


def q_cut(samples, n_cut, table):
    num = 0.0
    den = 0.0
    seen = False
    for step, th2, i1 in samples:
        if step > n_cut:
            break
        seen = True
        rho = math.exp(i1)
        num += rho * table[flow.site_of(th2)]
        den += rho
    if not seen or den == 0.0:
        return None
    return num / den


def gap_of(values):
    if any(v is None for v in values):
        return None
    return max(values) - min(values)


def show_gap(name, g):
    return "%s %s" % (name, fmt(g) if g is not None else "NONE")


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

    pd_top = closed_form_ant(math.pi / 2.0, 0.0)[1]

    # Period-2 port and dense scan.
    cache500 = {}
    q500 = q_width_factory(500, cache500)
    kind500, _terms, traces500, stopped500, _spread = iterate(0.0, 2.0, q500, pd_top)
    levels = []
    widths = []
    port_ok = kind500 == "CYCLE" and not any(stopped500)
    for updates in traces500:
        ok, even, odd = period2(updates)
        if not ok:
            port_ok = False
            continue
        pair = tuple(sorted((even, odd)))
        levels.append(pair)
        wa = widths_for(0.0, 2.0, even, pd_top)
        wb = widths_for(0.0, 2.0, odd, pd_top)
        widths.append((wa, wb))
    if len(levels) != 5 or any(p != levels[0] for p in levels):
        port_ok = False
    step = None
    if levels:
        step = abs(levels[0][1] - levels[0][0])
        if abs(levels[0][0] - 0.288952) > 5e-7 or abs(levels[0][1] - 0.291620) > 5e-7:
            port_ok = False
        if abs(step - 2.668522e-3) > 1e-8:
            port_ok = False
    width_pair = None
    if widths and all(len(a) == 1 and len(b) == 1 for a, b in widths):
        width_pair = tuple(sorted((widths[0][0][0], widths[0][1][0])))
        if width_pair != (7, 8) or any(
            tuple(sorted((a[0], b[0]))) != (7, 8) for a, b in widths
        ):
            port_ok = False
    else:
        port_ok = False
    print(
        "P-port %s kind %s levels %s step %s widths %s"
        % (
            "PASS" if port_ok else "FAIL",
            kind500,
            " ".join(fmt(v) for v in levels[0]) if levels else "NONE",
            fmt(step) if step is not None else "NONE",
            "%d %d" % width_pair if width_pair is not None else "NONE",
        )
    )
    if not port_ok:
        fails.append("P-port")

    classes = []
    res_ok = True
    for t in range(SCAN_LO, SCAN_HI + 1):
        q_of = q_width_factory(t, {})
        kind, _terms, traces, stopped, _spread = iterate(0.0, 2.0, q_of, pd_top)
        bad = False
        if kind == "CYCLE":
            for updates, did in zip(traces, stopped):
                if did:
                    continue
                ok, even, odd = period2(updates)
                if not ok:
                    bad = True
                    continue
                wa = widths_for(0.0, 2.0, even, pd_top)
                wb = widths_for(0.0, 2.0, odd, pd_top)
                if len(wa) != 1 or len(wb) != 1 or abs(wa[0] - wb[0]) != 1:
                    bad = True
        classes.append((t, kind, bad))
    if any(bad for _t, kind, bad in classes if kind == "CYCLE"):
        res_ok = False

    cycle_ts = [t for t, kind, _bad in classes if kind == "CYCLE"]
    blocks = []
    if cycle_ts:
        start = cycle_ts[0]
        prev = cycle_ts[0]
        for t in cycle_ts[1:]:
            if t == prev + 1:
                prev = t
                continue
            blocks.append((start, prev))
            start = t
            prev = t
        blocks.append((start, prev))
    one = len(blocks) == 1 and blocks[0][0] <= 500 <= blocks[0][1]
    if not one:
        res_ok = False
        length = 0
        below = False
        above = False
    else:
        lo, hi = blocks[0]
        length = hi - lo + 1
        if length > 207:
            res_ok = False
        below = any(kind in ("POINT", "SET") for t, kind, _b in classes if t < lo)
        above = any(kind in ("POINT", "SET") for t, kind, _b in classes if t > hi)
        if not below or not above:
            res_ok = False
    n_point = sum(1 for _t, kind, _b in classes if kind == "POINT")
    n_set = sum(1 for _t, kind, _b in classes if kind == "SET")
    n_cycle = len(cycle_ts)
    if one:
        print(
            "P-res-BLOCK %d %d length %d below %s above %s"
            % (blocks[0][0], blocks[0][1], length, "YES" if below else "NO", "YES" if above else "NO")
        )
    else:
        print("P-res-BLOCK NONE blocks %d" % len(blocks))
    print("P-res-COUNTS POINT %d SET %d CYCLE %d" % (n_point, n_set, n_cycle))
    print("P-res-T " + " ".join(str(t) for t in cycle_ts))
    print("P-res %s" % ("PASS" if res_ok else "FAIL"))
    if not res_ok:
        fails.append("P-res")
    print("DIAG clamps %d" % CLAMPS[0])

    # Site tables for the flow horizons.
    need = set()
    for _name, w20 in FAMILIES:
        need.add(flow.horizon(w20))
    for t in WALK_T:
        need.add(t)
    tables = {}
    for t in sorted(need):
        tables[t] = tuple(
            flow.return_prob(N, [s], t, 1.0, "agent") for s in range(N)
        )

    # One conservative trace per family and angle, out to t=100.
    n_full = int(round(100.0 / H))
    traces = {}
    for name, w20 in FAMILIES:
        omega = (1.0, w20)
        traces[name] = [
            trace(omega, th2, n_full, 0.0, False) for th2 in flow.ANGLES
        ]

    # H-label
    ends = []
    starts = [(0.0, th2, 0.0, 0.0) for th2 in flow.ANGLES]
    for samples, theta, action in traces["irr"]:
        ends.append((theta[0], theta[1], action[0], action[1]))
    def min_pair(states):
        best = None
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                d = flow.state_dist(states[i], states[j])
                if best is None or d < best:
                    best = d
        return best
    d0 = min_pair(starts)
    d1 = min_pair(ends)
    ratio = d1 / d0 if d0 else 0.0
    label_ok = ratio >= 0.5
    print("H-label %s d0 %s d1 %s ratio %s" % (
        "PASS" if label_ok else "FAIL", fmte(d0), fmte(d1), fmt(ratio)
    ))
    if not label_ok:
        fails.append("H-label")

    # H-flow
    flow_ok = True
    flow_gaps = {}
    for name, w20 in FAMILIES:
        table = tables[flow.horizon(w20)]
        series = []
        for t in TIMES:
            n_cut = int(round(t / H))
            qs = [q_cut(samples, n_cut, table) for samples, _th, _act in traces[name]]
            series.append(gap_of(qs))
            print("H-flow-G %s t %s %s" % (name, fmt(t), fmt(series[-1]) if series[-1] is not None else "NONE"))
        flow_gaps[name] = series
        if any(g is None for g in series):
            flow_ok = False
            continue
        if min(series) < 0.5 * max(series):
            flow_ok = False
    for i, t in enumerate(TIMES):
        gr = flow_gaps["rat"][i]
        gi = flow_gaps["irr"][i]
        if gr is None or gi is None or gr < gi:
            flow_ok = False
    print("H-flow %s" % ("PASS" if flow_ok else "FAIL"))
    if not flow_ok:
        fails.append("H-flow")

    # H-walk
    walk_ok = True
    walk_gaps = {"rat": {}, "irr": {}}
    for name in ("rat", "irr"):
        for t in WALK_T:
            qs = [q_cut(samples, n_full, tables[t]) for samples, _th, _act in traces[name]]
            g = gap_of(qs)
            walk_gaps[name][t] = g
            print("H-walk-G %s T %d %s" % (name, t, fmt(g) if g is not None else "NONE"))
        g_long = walk_gaps[name][83069]
        g_ref = walk_gaps[name][415]
        if g_long is None or g_ref is None or g_long < 0.5 * g_ref:
            walk_ok = False
    for t in WALK_T:
        gr = walk_gaps["rat"][t]
        gi = walk_gaps["irr"][t]
        if gr is None or gi is None or gr < gi:
            walk_ok = False
    print("H-walk %s" % ("PASS" if walk_ok else "FAIL"))
    if not walk_ok:
        fails.append("H-walk")

    # H-gamma: phase contraction on the irrational family.
    g0 = flow_gaps["irr"][-1]
    gamma_ok = g0 is not None
    print("H-gamma-G0 %s" % (fmt(g0) if g0 is not None else "NONE"))
    omega_irr = (1.0, math.sqrt(2.0))
    table_irr = tables[flow.horizon(math.sqrt(2.0))]
    for gamma in (0.02, 0.05):
        series = []
        angled = [trace(omega_irr, th2, n_full, gamma, True) for th2 in flow.ANGLES]
        for t in TIMES:
            n_cut = int(round(t / H))
            qs = [q_cut(samples, n_cut, table_irr) for samples, _th, _act in angled]
            series.append(gap_of(qs))
            print(
                "H-gamma-G gamma %s t %s %s"
                % (fmt(gamma), fmt(t), fmt(series[-1]) if series[-1] is not None else "NONE")
            )
        half = None
        if g0 is not None:
            for t, g in zip(TIMES, series):
                if g is not None and g <= 0.5 * g0:
                    half = t
                    break
        if half is None:
            gamma_ok = False
            print("H-gamma-HALF gamma %s t NONE" % fmt(gamma))
        else:
            score = abs(gamma * half / math.log(2.0) - 1.0)
            print("H-gamma-HALF gamma %s t %s score %s" % (fmt(gamma), fmt(half), fmt(score)))
            if score > 0.5:
                gamma_ok = False
    print("H-gamma %s" % ("PASS" if gamma_ok else "FAIL"))
    if not gamma_ok:
        fails.append("H-gamma")

    print("FAILS %d" % len(fails))
    if fails:
        print("SCORED_FAIL %s" % " ".join(fails))
    else:
        print("SCORED_FAIL none")
    print("SCOREBOARD COMPLETE")


if __name__ == "__main__":
    main()
