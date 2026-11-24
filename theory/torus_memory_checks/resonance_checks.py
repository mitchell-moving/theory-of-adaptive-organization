"""T82d resonance scan of the step map. Criteria are PREREG_RESONANCE.md.

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
STOP = 1e-4
ITERS = 40
N = 32
TAIL0 = 200
NSTEPS = 400
DIST = 1e-3
LOCKED_HASH = "3a37da80f100480efa7442a372fc94aa449541ea4b04b39a8b03ec0db5ad4a39"
ROOT = os.path.dirname(os.path.dirname(HERE))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG_RESONANCE.md")

T_LO = 300
T_HI = 1200
STAKES = (1.0, 2.0, 4.0)
GAINS = ((0.5, 0.5), (1.0, 1.0), (1.5, 1.5))
FINE = (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75)
INITS = ((1.0, 0.0), (5.0, 0.5), (9.0, 1.0))
Q0S = (0.0, 0.25, 0.5, 0.75, 1.0)
RATIOS = (0.5, 1.0, 1.25, 4.0 / 3.0, 1.5, 2.0)


def fmt(x):
    return "%.12f" % x


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


def grid_of(n_points):
    rows = []
    last = n_points - 1
    for j in range(n_points):
        th = j * (math.pi / 2.0) / last
        rows.append((th, closed_form_ant(th, 0.0)))
    return rows


GRID181 = grid_of(181)
GRID2881 = grid_of(2881)
PD_TOP = GRID181[-1][1][1]


def widths_on(grid, w, q):
    best = None
    best_j = None
    scored = []
    for j, (th, (info, pd, loss)) in enumerate(grid):
        cost = info + q * pd + w * loss
        scored.append((cost, pd, th))
        if best is None or cost < best:
            best = cost
            best_j = j
    found = []
    seen = set()
    for cost, pd, _th in scored:
        if cost > best + TIE:
            continue
        width = 1 + math.floor(8.0 * pd / PD_TOP + PD_EPS)
        if width < 1:
            width = 1
        if width > 9:
            width = 9
        if width not in seen:
            seen.add(width)
            found.append(width)
    return found, best_j


def block_sites(width):
    j0 = N // 2
    raw = range(j0 - (width // 2), j0 + (width // 2) + 1)
    return [j for j in raw if 0 <= j < N]


def returns_upto(starts, t_max):
    """Cumulative agent mass at every horizon, averaged over starts.

    The recurrence is flow.step_mass, the same step as return_prob.
    """
    acc = [0.0] * (t_max + 1)
    for s in starts:
        p = [0.0] * N
        p[s] = 1.0
        agent = 0.0
        for t in range(1, t_max + 1):
            p, got, _sink = flow.step_mass(p, 1.0, "agent")
            agent += got
            acc[t] += agent
    scale = 1.0 / float(len(starts))
    return [v * scale for v in acc]


def all_tables(t_max):
    series = {}
    for width in range(1, 10):
        key = tuple(block_sites(width))
        if key not in series:
            series[key] = returns_upto(list(key), t_max)
    tables = {}
    for t in range(T_LO, t_max + 1):
        tables[t] = {width: series[tuple(block_sites(width))][t] for width in range(1, 10)}
    return tables


def iterate_floored(w, table):
    traces = []
    terminals = []
    stopped = []
    for q0 in Q0S:
        q = q0
        updates = []
        did = False
        for _ in range(ITERS):
            ws, _j = widths_on(GRID181, w, q)
            nxt = sum(table[width] for width in ws) / float(len(ws))
            updates.append(nxt)
            if abs(nxt - q) <= STOP:
                did = True
                break
            q = nxt
        traces.append(updates)
        stopped.append(did)
        if did:
            terminals.append(updates[-1])
    return traces, stopped, terminals


def least_period_1d(traces, stopped):
    if all(stopped):
        return 1
    for p in range(2, 17):
        ok = True
        for updates, did in zip(traces, stopped):
            if did:
                continue
            if len(updates) < 2 * p:
                ok = False
                break
            window = updates[-2 * p :]
            for i in range(p):
                if abs(window[i + p] - window[i]) > 1e-9:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return p
    return None


def levels_of(updates):
    window = updates[-6:]
    evens = window[0::2]
    odds = window[1::2]
    return sum(evens) / 3.0, sum(odds) / 3.0


def interp_return(table, w_real):
    if w_real <= 1.0:
        return table[1]
    if w_real >= 9.0:
        return table[9]
    k = int(math.floor(w_real))
    f = w_real - k
    if k >= 9:
        return table[9]
    return (1.0 - f) * table[k] + f * table[k + 1]


def iterate_interp(w, table, grid):
    traces = []
    stopped = []
    terminals = []
    for q0 in Q0S:
        q = q0
        updates = []
        did = False
        for _ in range(ITERS):
            best = None
            best_pd = None
            for _th, (info, pd, loss) in grid:
                cost = info + q * pd + w * loss
                if best is None or cost < best - TIE:
                    best = cost
                    best_pd = pd
            w_real = 1.0 + 8.0 * best_pd / PD_TOP
            nxt = interp_return(table, w_real)
            updates.append(nxt)
            if abs(nxt - q) <= STOP:
                did = True
                break
            q = nxt
        traces.append(updates)
        stopped.append(did)
        if did:
            terminals.append(updates[-1])
    return least_period_1d(traces, stopped)


def q_of_rho(table, rho):
    if rho <= 1.0:
        return table[1]
    if rho >= 9.0:
        return table[9]
    k = int(math.floor(rho))
    frac = rho - k
    if k < 1:
        return table[1]
    if k >= 9:
        return table[9]
    return (1.0 - frac) * table[k] + frac * table[k + 1]


def coupled_orbit(alpha, beta, rho0, q0, w, table):
    rho, q = rho0, q0
    states = []
    for _ in range(NSTEPS):
        ws, _j = widths_on(GRID181, w, q)
        target = sum(ws) / float(len(ws))
        q_ret = q_of_rho(table, rho)
        rho = rho + alpha * (target - rho)
        q = q + beta * (q_ret - q)
        states.append((rho, q))
    return states


def least_period_2d(states):
    tail = states[TAIL0:NSTEPS]
    n = len(tail)
    for p in range(1, 33):
        ok = True
        for i in range(n - p):
            dr = tail[i + p][0] - tail[i][0]
            dq = tail[i + p][1] - tail[i][1]
            if math.hypot(dr, dq) > DIST:
                ok = False
                break
        if ok:
            return p, tail
    return None, states[TAIL0:NSTEPS]


def blocks_of(ts):
    if not ts:
        return []
    out = []
    start = prev = ts[0]
    for t in ts[1:]:
        if t == prev + 1:
            prev = t
            continue
        out.append((start, prev))
        start = prev = t
    out.append((start, prev))
    return out


def nearest_int(c):
    """Nearest integer. A tie resolves to the lower integer."""
    down = math.floor(c)
    if c - down < 0.5:
        return int(down)
    if c - down > 0.5:
        return int(down) + 1
    return int(down)


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

    tables = all_tables(T_HI)

    # One-dimensional periods.
    periods = {w: {} for w in STAKES}
    for t in range(T_LO, T_HI + 1):
        table = tables[t]
        for w in STAKES:
            traces, stopped, terminals = iterate_floored(w, table)
            p = least_period_1d(traces, stopped)
            mean = None if not terminals else sum(terminals) / float(len(terminals))
            periods[w][t] = (p, mean, traces, stopped)

    # P-port
    p415, mean415, _tr, _st = periods[2.0][415]
    p500, _m500, tr500, st500 = periods[2.0][500]
    p831, mean831, _tr, _st = periods[2.0][831]
    port_ok = p415 == 1 and mean415 is not None and abs(mean415 - 0.246706007043) <= 1e-6
    port_ok = port_ok and p831 == 1 and mean831 is not None and abs(mean831 - 0.422916079022) <= 1e-6
    port_ok = port_ok and p500 == 2 and not any(st500)
    levels = None
    if p500 == 2 and tr500:
        pairs = []
        for updates, did in zip(tr500, st500):
            if did or len(updates) < 6:
                port_ok = False
                continue
            a, b = levels_of(updates)
            pairs.append(tuple(sorted((a, b))))
        if len(pairs) == 5 and all(pair == pairs[0] for pair in pairs):
            levels = pairs[0]
            if abs(levels[0] - 0.288952) > 5e-7 or abs(levels[1] - 0.291620) > 5e-7:
                port_ok = False
        else:
            port_ok = False
    else:
        port_ok = False

    port550 = True
    for rho0, q0 in INITS:
        p, tail = least_period_2d(coupled_orbit(1.0, 1.0, rho0, q0, 2.0, tables[550]))
        if p != 1:
            port550 = False
            continue
        rho = sum(s[0] for s in tail) / float(len(tail))
        q = sum(s[1] for s in tail) / float(len(tail))
        if abs(rho - 6.0) > 1e-6 or abs(q - 0.313065981732) > 1e-9:
            port550 = False
        print("P-port-550 init %s %s period %s rho %s q %s" % (
            fmt(rho0), fmt(q0), str(p), fmt(rho), fmt(q)
        ))
    port_ok = port_ok and port550
    print(
        "P-port %s p415 %s p500 %s p831 %s levels %s"
        % (
            "PASS" if port_ok else "FAIL",
            str(p415),
            str(p500),
            str(p831),
            " ".join(fmt(v) for v in levels) if levels else "NONE",
        )
    )
    if not port_ok:
        fails.append("P-port")

    def half_ts(w):
        return [t for t in range(T_LO, T_HI + 1) if periods[w][t][0] == 2]

    for w in STAKES:
        bs = blocks_of(half_ts(w))
        if not bs:
            print("BAND w %s NONE" % fmt(w))
        for lo, hi in bs:
            print("BAND w %s %d %d length %d" % (fmt(w), lo, hi, hi - lo + 1))

    band = blocks_of(half_ts(2.0))
    one = len(band) == 1 and band[0][0] <= 500 <= band[0][1] and (band[0][1] - band[0][0] + 1) >= 3
    # plateau means length >= 3, and no outside points: one block containing 500 is exactly that
    # if the single block has length < 3 it is not a plateau
    print("P-band %s" % ("PASS" if one else "FAIL"))
    if not one:
        fails.append("P-band")

    if one:
        lo, hi = band[0]
        where = lo > 415 and hi < 831
        center = 0.5 * (lo + hi)
    else:
        lo = hi = None
        where = False
        center = None
    print("P-where %s" % ("PASS" if where else "FAIL"))
    if not where:
        fails.append("P-where")

    tau = 1.0 / (math.sin(math.pi / 64.0) ** 2)
    align_ok = center is not None
    closest = None
    if center is not None:
        for r in RATIOS:
            rel = abs(center / (r * tau) - 1.0)
            if closest is None or rel < closest[0]:
                closest = (rel, r)
            if rel <= 0.05:
                align_ok = False
    print(
        "P-align %s tau %s C %s closest_r %s rel %s"
        % (
            "PASS" if align_ok else "FAIL",
            fmt(tau),
            fmt(center) if center is not None else "NONE",
            fmt(closest[1]) if closest else "NONE",
            fmt(closest[0]) if closest else "NONE",
        )
    )
    if not align_ok:
        fails.append("P-align")

    high = [t for t, (p, _m, _tr, _st) in periods[2.0].items() if p is None or p >= 3]
    stair_ok = not high
    print("P-stair %s high %d" % ("PASS" if stair_ok else "FAIL", len(high)))
    if high:
        print("P-stair-T " + " ".join("%d:%s" % (t, str(periods[2.0][t][0])) for t in high[:20]))
    if not stair_ok:
        fails.append("P-stair")

    single_ok = True
    for w in STAKES:
        n_blocks = len(blocks_of(half_ts(w)))
        if n_blocks > 1:
            single_ok = False
        print("P-single-N w %s blocks %d" % (fmt(w), n_blocks))
    print("P-single %s" % ("PASS" if single_ok else "FAIL"))
    if not single_ok:
        fails.append("P-single")

    # Coupled gains.
    coupled_period = {g: {} for g in GAINS}
    interior = {g: 0 for g in GAINS}
    endpoint = {g: 0 for g in GAINS}
    for t in range(T_LO, T_HI + 1):
        table = tables[t]
        for gain in GAINS:
            found = []
            for rho0, q0 in INITS:
                p, tail = least_period_2d(coupled_orbit(gain[0], gain[1], rho0, q0, 2.0, table))
                rho = sum(s[0] for s in tail) / float(len(tail))
                found.append((p, rho))
            if any(p != found[0][0] for p, _rho in found):
                coupled_period[gain][t] = "SPLIT"
            else:
                coupled_period[gain][t] = found[0][0]
                if found[0][0] == 1 and all(1.0 + DIST < rho < 9.0 - DIST for _p, rho in found):
                    interior[gain] += 1
                if found[0][0] == 1 and all(
                    rho <= 1.0 + DIST or rho >= 9.0 - DIST for _p, rho in found
                ):
                    endpoint[gain] += 1
    n_lo = interior[(0.5, 0.5)]
    n_hi = interior[(1.5, 1.5)]
    differ = 0
    for t in range(T_LO, T_HI + 1):
        if coupled_period[(0.5, 0.5)][t] != coupled_period[(1.5, 1.5)][t]:
            differ += 1
    fine_periods = []
    for g in FINE:
        found = []
        for rho0, q0 in INITS:
            p, _tail = least_period_2d(coupled_orbit(g, g, rho0, q0, 2.0, tables[500]))
            found.append(p)
        if any(p != found[0] for p in found):
            fine_periods.append("SPLIT")
        else:
            fine_periods.append(found[0])
    gain_ok = (n_hi - n_lo) <= 2 and differ <= 2 and all(
        p == fine_periods[0] for p in fine_periods
    )
    print(
        "P-gain-PLACE gain 1.000000000000 interior %d endpoint %d"
        % (interior[(1.0, 1.0)], endpoint[(1.0, 1.0)])
    )
    print("P-gain-N low %d high %d differ %d" % (n_lo, n_hi, differ))
    print("P-gain-FINE " + " ".join(str(p) for p in fine_periods))
    print("P-gain %s" % ("PASS" if gain_ok else "FAIL"))
    if not gain_ok:
        fails.append("P-gain")

    # Null: floor removed.
    if center is None:
        center_t = None
        null_ok = False
    else:
        center_t = nearest_int(center)
        null_ok = True
    null_horizons = [500, 550]
    if center_t is not None:
        null_horizons.append(center_t)
    for t in null_horizons:
        for n_pts, grid in ((181, GRID181), (2881, GRID2881)):
            p = iterate_interp(2.0, tables[t], grid)
            print("P-null-RUN T %d grid %d period %s" % (t, n_pts, str(p)))
            if p != 1:
                null_ok = False
    if center is not None and abs(center - math.floor(center) - 0.5) < 1e-12:
        print("DIAG center-tie %s -> %d" % (fmt(center), center_t))
    print("P-null %s" % ("PASS" if null_ok else "FAIL"))
    if not null_ok:
        fails.append("P-null")

    for t in half_ts(2.0):
        found = []
        for rho0, q0 in INITS:
            p, tail = least_period_2d(coupled_orbit(1.0, 1.0, rho0, q0, 2.0, tables[t]))
            rho = sum(s[0] for s in tail) / float(len(tail))
            found.append((p, rho))
        same = all(item[0] == found[0][0] for item in found)
        print(
            "COUPLED-ISLAND T %d period %s rho %s"
            % (t, str(found[0][0]) if same else "SPLIT", fmt(found[0][1]))
        )

    print("FAILS %d" % len(fails))
    if fails:
        print("SCORED_FAIL %s" % " ".join(fails))
    else:
        print("SCORED_FAIL none")
    print("SCOREBOARD COMPLETE")


if __name__ == "__main__":
    main()
