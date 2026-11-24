#!/usr/bin/env python3
"""Independent recomputation for the T82c/T82d review.

The walk, the angle cost, and the width menu are coded from the locked
descriptions (T81 lazy step; closed-form antenna at f625bb7; floor rule in
PREREG_RESONANCE.md). This file does not import the score scripts.
"""
from __future__ import annotations

import math

R = 0.6
TIE = 1e-9
PD_EPS = 1e-15
STOP = 1e-4
ITERS = 40
N = 32
TAIL0 = 200
NSTEPS = 400
DIST = 1e-3
Q0S = (0.0, 0.25, 0.5, 0.75, 1.0)
INITS = ((1.0, 0.0), (5.0, 0.5), (9.0, 1.0))
T_LO = 300
T_HI = 1200


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
    last = n_points - 1
    rows = []
    for j in range(n_points):
        th = j * (math.pi / 2.0) / last
        info, pd, loss = closed_form_ant(th, 0.0)
        rows.append((th, info, pd, loss))
    return rows


def step_mass(p, c=1.0):
    n = len(p)
    new = [0.0] * n
    agent = 0.0
    for j, mass in enumerate(p):
        if mass == 0.0:
            continue
        new[j] += 0.5 * mass
        if j > 0:
            new[j - 1] += 0.25 * mass
        else:
            agent += 0.25 * mass
        if j < n - 1:
            new[j + 1] += 0.25 * mass
        else:
            new[j] += 0.25 * c * mass
    return new, agent


def block_sites(width):
    j0 = N // 2
    raw = range(j0 - (width // 2), j0 + (width // 2) + 1)
    return tuple(j for j in raw if 0 <= j < N)


def returns_upto(starts, t_max):
    acc = [0.0] * (t_max + 1)
    for s in starts:
        p = [0.0] * N
        p[s] = 1.0
        agent = 0.0
        for t in range(1, t_max + 1):
            p, got = step_mass(p, 1.0)
            agent += got
            acc[t] += agent
    scale = 1.0 / float(len(starts))
    return [v * scale for v in acc]


def all_tables(t_max):
    series = {}
    for width in range(1, 10):
        key = block_sites(width)
        if key not in series:
            series[key] = returns_upto(list(key), t_max)
    tables = {}
    for t in range(1, t_max + 1):
        tables[t] = {width: series[block_sites(width)][t] for width in range(1, 10)}
    return tables


def prepare(grid, stake, span, offset, mode):
    """mode: floor, round, real. span is the menu multiplier (locked value 8)."""
    pd_top = grid[-1][2]
    rows = []
    for _th, info, pd, loss in grid:
        a = info + stake * loss
        rows.append((a, pd, pd_top))
    return rows, pd_top


def widths_at(rows, pd_top, q, span, offset, mode):
    best = None
    scored = []
    run_best = None
    run_pd = None
    for a, pd, _top in rows:
        cost = a + q * pd
        scored.append((cost, pd))
        if best is None or cost < best:
            best = cost
        # Locked interpolation rule: earliest angle that beats the running
        # value by more than TIE.
        if run_best is None or cost < run_best - TIE:
            run_best = cost
            run_pd = pd
    if mode == "real":
        return None, run_pd
    found = []
    seen = set()
    for cost, pd in scored:
        if cost > best + TIE:
            continue
        x = span * pd / pd_top + offset
        if mode == "round":
            width = 1 + int(math.floor(x + 0.5))
        else:
            width = 1 + int(math.floor(x + PD_EPS))
        if width < 1:
            width = 1
        if width > 9:
            width = 9
        if width not in seen:
            seen.add(width)
            found.append(width)
    return found, run_pd


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


def iterate_menu(rows, pd_top, table, span, offset, mode):
    traces = []
    stopped = []
    terminals = []
    width_trace = []
    for q0 in Q0S:
        q = q0
        updates = []
        wtrace = []
        did = False
        for _ in range(ITERS):
            found, best_pd = widths_at(rows, pd_top, q, span, offset, mode)
            if mode == "real":
                w_real = 1.0 + span * best_pd / pd_top
                nxt = interp_return(table, w_real)
                wtrace.append(w_real)
            else:
                nxt = sum(table[w] for w in found) / float(len(found))
                wtrace.append(tuple(found))
            updates.append(nxt)
            if abs(nxt - q) <= STOP:
                did = True
                break
            q = nxt
        traces.append(updates)
        stopped.append(did)
        width_trace.append(wtrace)
        if did:
            terminals.append(updates[-1])
    return least_period_1d(traces, stopped), traces, stopped, terminals, width_trace


def interp_return(table, w_real):
    if w_real <= 1.0:
        return table[1]
    if w_real >= 9.0:
        return table[9]
    k = int(math.floor(w_real))
    frac = w_real - k
    if k >= 9:
        return table[9]
    if k < 1:
        return table[1]
    return (1.0 - frac) * table[k] + frac * table[k + 1]


def q_of_rho(table, rho):
    return interp_return(table, rho)


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


def scan_periods(rows, pd_top, tables, span, offset, mode, t0, t1):
    periods = {}
    for t in range(t0, t1 + 1):
        p, _tr, _st, _term, _wt = iterate_menu(rows, pd_top, tables[t], span, offset, mode)
        periods[t] = p
    return periods


def half_blocks(periods, t0, t1):
    ts = [t for t in range(t0, t1 + 1) if periods[t] == 2]
    return blocks_of(ts)


def fmt_blocks(blocks):
    if not blocks:
        return "NONE"
    return " ".join("%d-%d" % (a, b) for a, b in blocks)


def coupled_orbit(rows, pd_top, alpha, beta, rho0, q0, table):
    rho, q = rho0, q0
    states = []
    for _ in range(NSTEPS):
        found, _pd = widths_at(rows, pd_top, q, 8.0, 0.0, "floor")
        target = sum(found) / float(len(found))
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
        worst = 0.0
        for i in range(n - p):
            dr = tail[i + p][0] - tail[i][0]
            dq = tail[i + p][1] - tail[i][1]
            err = math.hypot(dr, dq)
            if err > worst:
                worst = err
            if err > DIST:
                ok = False
                break
        if ok:
            return p, tail, worst
    return None, states[TAIL0:NSTEPS], None


def spectral_gap():
    """Largest-magnitude eigenvalue of the N=32 lazy step, c=1.

    Site 0 leaks a quarter of its mass. The matrix is the column-stochastic
    form of that step, diagonalized with numpy.
    """
    import numpy as np

    mat = np.zeros((N, N))
    for j in range(N):
        mat[j, j] += 0.5
        if j > 0:
            mat[j - 1, j] += 0.25
        if j < N - 1:
            mat[j + 1, j] += 0.25
        else:
            mat[j, j] += 0.25
    ev = np.linalg.eigvals(mat)
    return float(max(abs(z) for z in ev))


def merge_len(intervals, lo, hi):
    segs = []
    for a, b in intervals:
        a = max(a, lo)
        b = min(b, hi)
        if b > a:
            segs.append((a, b))
    if not segs:
        return 0.0
    segs.sort()
    total = 0.0
    cs, ce = segs[0]
    for a, b in segs[1:]:
        if a <= ce:
            ce = max(ce, b)
        else:
            total += ce - cs
            cs, ce = a, b
    total += ce - cs
    return total


def farey(qmax):
    vals = []
    for q in range(1, qmax + 1):
        for p in range(1, 4 * q + 1):
            vals.append(p / float(q))
    uniq = sorted(set(vals))
    return uniq


def main():
    tau = 1.0 / (math.sin(math.pi / 64.0) ** 2)
    print("TAU %.15f" % tau)
    print("SIN2 %.15e" % (math.sin(math.pi / 64.0) ** 2))
    lam = spectral_gap()
    print("SPECTRAL lambda %.15f one_minus %.15e inv_gap %.6f inv_log %.6f" % (
        lam, 1.0 - lam, 1.0 / (1.0 - lam) if lam < 1.0 else float("inf"),
        -1.0 / math.log(lam) if 0.0 < lam < 1.0 else float("inf"),
    ))

    print("BLOCKS")
    for w in range(1, 10):
        sites = block_sites(w)
        print("  width %d n %d sites %s" % (w, len(sites), " ".join(str(s) for s in sites)))

    tables = all_tables(T_HI)
    # Port digits at the locked horizons, stake 2, official floor.
    grid181 = grid_of(181)
    rows2, pd_top = prepare(grid181, 2.0, 8.0, 0.0, "floor")
    print("PD_TOP %.15f" % pd_top)

    for t, expect in ((415, 1), (500, 2), (550, 1), (831, 1)):
        p, traces, stopped, terminals, wtrace = iterate_menu(
            rows2, pd_top, tables[t], 8.0, 0.0, "floor"
        )
        mean = None if not terminals else sum(terminals) / float(len(terminals))
        levels = []
        if p == 2:
            for updates, did in zip(traces, stopped):
                if did or len(updates) < 6:
                    continue
                window = updates[-6:]
                a = sum(window[0::2]) / 3.0
                b = sum(window[1::2]) / 3.0
                levels.append(tuple(sorted((a, b))))
        print(
            "PORT T %d period %s mean %s levels %s widths %s"
            % (
                t,
                str(p),
                "%.12f" % mean if mean is not None else "NONE",
                " ".join("%.12f %.12f" % lv for lv in levels[:1]) if levels else "NONE",
                str(wtrace[0][-6:] if wtrace and wtrace[0] else None),
            )
        )

    print("SCAN stake 2 official floor 300-1200")
    per = scan_periods(rows2, pd_top, tables, 8.0, 0.0, "floor", T_LO, T_HI)
    blocks = half_blocks(per, T_LO, T_HI)
    print("ISLANDS " + fmt_blocks(blocks))
    other = sorted(t for t, p in per.items() if p not in (1, 2))
    print("OTHER_PERIODS %d" % len(other))

    for stake in (1.0, 4.0):
        rows, top = prepare(grid181, stake, 8.0, 0.0, "floor")
        ps = scan_periods(rows, top, tables, 8.0, 0.0, "floor", T_LO, T_HI)
        print("STAKE %.1f islands %s" % (stake, fmt_blocks(half_blocks(ps, T_LO, T_HI))))

    # Centers against ratios.
    centers = []
    for a, b in blocks:
        if b - a + 1 >= 3:
            centers.append(0.5 * (a + b))
        else:
            centers.append(0.5 * (a + b))
    print("CENTERS " + " ".join("%.1f" % c for c in centers))
    ratios_locked = (0.5, 1.0, 1.25, 4.0 / 3.0, 1.5, 2.0)
    for c in centers:
        best = None
        for r in ratios_locked:
            rel = abs(c / (r * tau) - 1.0)
            if best is None or rel < best[0]:
                best = (rel, r)
        print("ALIGN center %.4f nearest_locked %.6f rel %.6f target %.6f" % (
            c, best[1], best[0], best[1] * tau
        ))
        # also nearest q<=4 and q<=5
        for qmax in (4, 5):
            best2 = None
            for r in farey(qmax):
                rel = abs(c / (r * tau) - 1.0)
                if best2 is None or rel < best2[0]:
                    best2 = (rel, r)
            print("  nearest_q<=%d r %.6f rel %.6f target %.6f" % (
                qmax, best2[1], best2[0], best2[1] * tau
            ))

    # Look-elsewhere on [416, 830].
    lo, hi = 416.0, 830.0
    length = hi - lo
    print("LEE interval %.1f %.1f length %.1f" % (lo, hi, length))
    ratios4 = []
    for q in range(1, 5):
        for p in range(1, 12):
            r = p / float(q)
            ratios4.append(r)
    ratios4 = sorted(set(ratios4))
    # keep those whose 5% window can meet the interval, or the target is near it
    use = []
    for r in ratios4:
        target = r * tau
        if target * 1.05 >= lo and target * 0.95 <= hi:
            use.append(r)
    print("RATIOS_Q4 " + " ".join("%.6f->%.3f" % (r, r * tau) for r in use))

    def coverage(eps, ratios):
        intervals = []
        for r in ratios:
            target = r * tau
            intervals.append((target * (1.0 - eps), target * (1.0 + eps)))
        return merge_len(intervals, lo, hi) / length

    observed = (0.032130, 0.004887, 0.014474)
    ordered = tuple(sorted(observed))
    for eps in (0.05, ordered[2], ordered[1], ordered[0]):
        cov = coverage(eps, use)
        print("COV eps %.6f f %.6f f3 %.6e" % (eps, cov, cov ** 3))

    # Nested order-statistic probability.
    f_tight = coverage(ordered[0], use)
    f_mid = coverage(ordered[1], use)
    f_loose = coverage(ordered[2], use)
    # regions: R0 δ<=tight, R1 tight<δ<=mid, R2 mid<δ<=loose, R3 outside
    p0, p1 = f_tight, f_mid - f_tight
    p2, p3 = f_loose - f_mid, 1.0 - f_loose
    print("REGION p0 %.6f p1 %.6f p2 %.6f p3 %.6f" % (p0, p1, p2, p3))
    prob = 0.0
    # compositions of 3 into 4 bins, success if c3==0, c2<=1, c0>=1
    for c0 in range(4):
        for c1 in range(4 - c0):
            for c2 in range(4 - c0 - c1):
                c3 = 3 - c0 - c1 - c2
                if c3 != 0 or c2 > 1 or c0 < 1:
                    continue
                ways = math.factorial(3) / (
                    math.factorial(c0) * math.factorial(c1) * math.factorial(c2) * math.factorial(c3)
                )
                prob += ways * (p0 ** c0) * (p1 ** c1) * (p2 ** c2) * (p3 ** c3)
    print("ORDERED_GAP_PROB %.6e" % prob)

    # Pre-specified triple, windows around the three targets only.
    spec = (1.25, 4.0 / 3.0, 1.5)
    spec_p = 1.0
    for r, eps in zip(spec, observed):
        target = r * tau
        a = max(lo, target * (1.0 - eps))
        b = min(hi, target * (1.0 + eps))
        frac = max(0.0, b - a) / length
        spec_p *= frac
        print("SPEC r %.6f eps %.6f window %.3f %.3f frac %.6f" % (r, eps, a, b, frac))
    print("SPEC_PRODUCT %.6e" % spec_p)

    # Integer-center version of the 5% coverage.
    n_int = 0
    hit05 = 0
    for t in range(416, 831):
        n_int += 1
        best = min(abs(t / (r * tau) - 1.0) for r in use)
        if best <= 0.05:
            hit05 += 1
    print("INTEGER n %d within_0.05 %d frac %.6f" % (n_int, hit05, hit05 / float(n_int)))

    # Floor variants, grid 181, full scan.
    print("FLOOR_VARIANTS")
    variants = [
        ("floor", 8.0, 0.0),
        ("floor", 8.0, 0.25),
        ("floor", 8.0, 0.5),
        ("floor", 8.0, 0.75),
        ("round", 8.0, 0.0),
        ("floor", 4.0, 0.0),
        ("floor", 16.0, 0.0),
        ("real", 8.0, 0.0),
    ]
    for mode, span, offset in variants:
        ps = scan_periods(rows2, pd_top, tables, span, offset, mode, T_LO, T_HI)
        bs = half_blocks(ps, T_LO, T_HI)
        high = sum(1 for p in ps.values() if p not in (1, 2) and p is not None)
        undef = sum(1 for p in ps.values() if p is None)
        print("  %s span %.1f off %.2f islands %s high %d undef %d" % (
            mode, span, offset, fmt_blocks(bs), high, undef
        ))

    # Finer and coarser angle grids. Official floor, and the real (no-floor) map.
    print("GRIDS")
    island_ts = []
    for a, b in blocks:
        island_ts.extend(range(a, b + 1))
    probe_ts = sorted(set(island_ts + list(range(300, 1201, 25)) + [415, 500, 550, 831]))
    for n_pts in (46, 91, 181, 361, 721, 1441, 2881):
        grid = grid_of(n_pts)
        rows, top = prepare(grid, 2.0, 8.0, 0.0, "floor")
        # full scan only for n<=361; larger grids on the probe list
        if n_pts <= 361:
            ps = scan_periods(rows, top, tables, 8.0, 0.0, "floor", T_LO, T_HI)
            bs = half_blocks(ps, T_LO, T_HI)
            pr = scan_periods(rows, top, tables, 8.0, 0.0, "real", T_LO, T_HI)
            br = half_blocks(pr, T_LO, T_HI)
            print("  n %d floor %s real %s" % (n_pts, fmt_blocks(bs), fmt_blocks(br)))
        else:
            floor_hits = []
            real_hits = []
            for t in probe_ts:
                pf, *_rest = iterate_menu(rows, top, tables[t], 8.0, 0.0, "floor")
                rr, *_rest = iterate_menu(rows, top, tables[t], 8.0, 0.0, "real")
                if pf == 2:
                    floor_hits.append(t)
                if rr == 2:
                    real_hits.append(t)
            print(
                "  n %d probe_floor_p2 %s probe_real_p2 %s"
                % (n_pts, fmt_blocks(blocks_of(floor_hits)), fmt_blocks(blocks_of(real_hits)))
            )

    # Width pairs actually visited on each official island horizon.
    print("WIDTH_PAIRS")
    for t in island_ts:
        _p, _tr, _st, _term, wtrace = iterate_menu(
            rows2, pd_top, tables[t], 8.0, 0.0, "floor"
        )
        print("  T %d period tail widths %s" % (t, str(wtrace[0][-8:])))

    # Coupled islands and the fine gain list at T=500.
    print("COUPLED")
    for t in island_ts:
        found = []
        for rho0, q0 in INITS:
            states = coupled_orbit(rows2, pd_top, 1.0, 1.0, rho0, q0, tables[t])
            p, tail, _worst = least_period_2d(states)
            rho = sum(s[0] for s in tail) / float(len(tail))
            found.append((p, rho))
        print("  T %d periods %s rho0 %.6f" % (
            t, " ".join(str(p) for p, _r in found), found[0][1]
        ))

    fine = (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75)
    print("FINE_T500")
    for g in fine:
        found = []
        details = []
        for rho0, q0 in INITS:
            states = coupled_orbit(rows2, pd_top, g, g, rho0, q0, tables[500])
            p, tail, worst = least_period_2d(states)
            steps = [
                math.hypot(tail[i + 1][0] - tail[i][0], tail[i + 1][1] - tail[i][1])
                for i in range(len(tail) - 1)
            ]
            found.append(p)
            details.append((max(steps) if steps else None, worst, tail[0], tail[-1]))
        print(
            "  g %.2f periods %s max_step %.3e closure %.3e tail0 %s"
            % (
                g,
                " ".join(str(p) for p in found),
                details[0][0],
                details[0][1] if details[0][1] is not None else -1.0,
                "(%.6f,%.6f)" % details[0][2],
            )
        )

    # Local separation at each fine gain: two starts 1e-6 apart in q.
    print("SEPARATION")
    for g in fine:
        s1 = coupled_orbit(rows2, pd_top, g, g, 5.0, 0.5, tables[500])
        s2 = coupled_orbit(rows2, pd_top, g, g, 5.0, 0.5 + 1e-6, tables[500])
        d0 = 1e-6
        d40 = math.hypot(s1[39][0] - s2[39][0], s1[39][1] - s2[39][1])
        dend = math.hypot(s1[-1][0] - s2[-1][0], s1[-1][1] - s2[-1][1])
        lam40 = math.log(d40 / d0) / 40.0 if d40 > 0.0 else -99.0
        print("  g %.2f d40 %.3e dend %.3e lam40 %.4f" % (g, d40, dend, lam40))

    # Period versus gain on a 0.05 grid, one initial condition, T=500.
    print("GAIN_GRID")
    runs = []
    prev = None
    run_g = None
    for i in range(1, 40):
        g = i * 0.05
        states = coupled_orbit(rows2, pd_top, g, g, 5.0, 0.5, tables[500])
        p, _tail, _w = least_period_2d(states)
        if p != prev:
            if prev is not None:
                runs.append((run_g, g - 0.05, prev))
            run_g = g
            prev = p
    runs.append((run_g, 1.95, prev))
    for a, b, p in runs:
        print("  g %.2f-%.2f period %s" % (a, b, str(p)))

    # Does a period-4 set in T widen with gain? Sample three gains on three windows.
    print("TONGUE_WINDOWS")
    for g in (0.5, 1.0, 1.5):
        for name, a, b in (("near500", 490, 510), ("near556", 545, 565), ("near614", 600, 620)):
            counts = {}
            for t in range(a, b + 1):
                states = coupled_orbit(rows2, pd_top, g, g, 5.0, 0.5, tables[t])
                p, _tail, _w = least_period_2d(states)
                counts[p] = counts.get(p, 0) + 1
            parts = " ".join("%s:%d" % (str(k), counts[k]) for k in sorted(counts, key=lambda z: (z is None, z or 0)))
            print("  g %.2f %s %s" % (g, name, parts))

    # P3 probe. Integrator copied from the locked separable step.
    print("P3_PROBE")
    beta = 0.25
    h = 0.05
    n = 2000

    def verlet(theta, action, eps, gamma, omega):
        s = math.sin(theta[0] - theta[1])
        f = (-eps * s, eps * s)
        mid = (action[0] - 0.5 * h * f[0], action[1] - 0.5 * h * f[1])
        nxt = (
            theta[0] + h * (omega[0] + beta * mid[0]),
            theta[1] + h * (omega[1] + beta * mid[1]),
        )
        s2 = math.sin(nxt[0] - nxt[1])
        f2 = (-eps * s2, eps * s2)
        end = (mid[0] - 0.5 * h * f2[0], mid[1] - 0.5 * h * f2[1])
        if gamma != 0.0:
            decay = math.exp(-gamma * h)
            end = (end[0] * decay, end[1] * decay)
        return nxt, end

    def run(theta0, action0, eps, gamma, omega):
        th, act = theta0, action0
        for _ in range(n):
            th, act = verlet(th, act, eps, gamma, omega)
        return th, act

    omega = (1.0, 1.5)
    angles = []
    for gamma in (0.0, 0.02, 0.05):
        th, act = run((0.0, 0.0), (0.0, 0.0), 0.0, gamma, omega)
        angles.append(th)
        print("  I0 gamma %.2f theta %s action %s" % (gamma, th, act))
    d01 = math.hypot(angles[0][0] - angles[1][0], angles[0][1] - angles[1][1])
    d02 = math.hypot(angles[0][0] - angles[2][0], angles[0][1] - angles[2][1])
    print("  angle_diff 0-vs-0.02 %.3e 0-vs-0.05 %.3e" % (d01, d02))
    for gamma, expect in ((0.02, 0.4 * math.exp(-2.0)), (0.05, 0.4 * math.exp(-5.0))):
        th, act = run((0.0, 0.0), (0.4, 0.0), 0.0, gamma, omega)
        print(
            "  probe gamma %.2f I1 %.15f gap_to_formula %.3e theta2 %.15f"
            % (gamma, act[0], act[0] - expect, th[1])
        )
    th, act = run((0.0, 0.3), (0.4, 0.0), 0.0, 0.02, omega)
    print("  unstated_theta0_0.3 theta2 %.20f" % th[1])
    print("DONE")


if __name__ == "__main__":
    main()
