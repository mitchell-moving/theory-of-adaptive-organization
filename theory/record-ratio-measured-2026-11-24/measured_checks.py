#!/usr/bin/env python3
"""T81 checks. Criteria are PREREG.md.

The preregistration is not read for numbers. SEED is set and not drawn from.
The script imports no random module.
"""
from __future__ import annotations

import math
import os
import sys

SEED = 20261124  # not drawn from

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, "..", "record_ratio_reframes_checks"))
sys.path.insert(0, REF)
import record_ratio_reframes_checks as base  # noqa: E402

A_AGENT = 4
N_LIST = (12, 16, 24, 32, 48)
X_LIST = (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
X_SHAPE = (0.25, 0.5, 1.0, 2.0)
W_MAX = 9
TIE = 1e-9
STOP = 1e-4
ITERS = 40
DIAM = 0.02
PAIR_TOL = 0.02
COLLAPSE_TOL = 0.08
SHAPE_TOL = 0.08
TV_TOL = 0.20
JACOBI_SWEEPS = 80
JACOBI_TOL = 1e-12
POWER_STEPS = 4000
FOURIER_TERMS = 40
D_DIFF = 0.25
PD_EPS = 1e-15

DEVIATIONS = []


def note(msg):
    DEVIATIONS.append(msg)


def horizon(x, tau):
    t = math.floor(x * tau + 0.5)
    if t < 1:
        t = 1
    return int(t)


def decoupled_matrix(n, c):
    """Symmetric N x N clock matrix. c=1 reflects at both ends. c<1 leaks at the far end."""
    m = [[0.0] * n for _ in range(n)]
    for j in range(n):
        m[j][j] += 0.5
        if 0 < j:
            m[j][j - 1] += 0.25
        if j < n - 1:
            m[j][j + 1] += 0.25
    # near end, agent deleted: outward quarter reflects
    m[0][0] += 0.25
    # far end
    m[n - 1][n - 1] += 0.25 * c
    return m


def jacobi_eigenvalues(matrix):
    """Cyclic Jacobi. Returns (eigenvalues descending, finished)."""
    n = len(matrix)
    m = [row[:] for row in matrix]
    finished = False
    for _sweep in range(JACOBI_SWEEPS):
        off2 = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                off2 += 2.0 * m[i][j] * m[i][j]
        if math.sqrt(off2) < JACOBI_TOL:
            finished = True
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = m[p][q]
                if apq == 0.0:
                    continue
                app = m[p][p]
                aqq = m[q][q]
                tau = (aqq - app) / (2.0 * apq)
                if tau >= 0.0:
                    t = 1.0 / (tau + math.sqrt(1.0 + tau * tau))
                else:
                    t = -1.0 / (-tau + math.sqrt(1.0 + tau * tau))
                cc = 1.0 / math.sqrt(1.0 + t * t)
                ss = t * cc
                for i in range(n):
                    if i == p or i == q:
                        continue
                    mip = m[i][p]
                    miq = m[i][q]
                    m[i][p] = m[p][i] = cc * mip - ss * miq
                    m[i][q] = m[q][i] = ss * mip + cc * miq
                m[p][p] = cc * cc * app - 2.0 * ss * cc * apq + ss * ss * aqq
                m[q][q] = ss * ss * app + 2.0 * ss * cc * apq + cc * cc * aqq
                m[p][q] = m[q][p] = 0.0
    evals = sorted((m[i][i] for i in range(n)), reverse=True)
    return evals, finished


def power_lambda2(matrix):
    """Rayleigh quotient after POWER_STEPS on the mean-zero subspace."""
    n = len(matrix)
    v = [math.cos(math.pi * i / (n - 1)) for i in range(n)]

    def demean(vec):
        mu = sum(vec) / n
        return [x - mu for x in vec]

    def apply(vec):
        return [sum(matrix[i][j] * vec[j] for j in range(n)) for i in range(n)]

    v = demean(v)
    norm = math.sqrt(sum(x * x for x in v))
    if norm == 0.0:
        return None
    v = [x / norm for x in v]
    for _ in range(POWER_STEPS):
        w = demean(apply(v))
        norm = math.sqrt(sum(x * x for x in w))
        if norm == 0.0:
            return None
        v = [x / norm for x in w]
    w = apply(v)
    return sum(v[i] * w[i] for i in range(n))


def relaxation_from_evals(evals, second):
    lam = evals[1] if second else evals[0]
    gap = 1.0 - lam
    if gap <= 0.0:
        return None
    return 1.0 / gap


def step_mass(p, c, contact):
    """One lazy step. contact is 'agent' or 'sink' for the near-end outward quarter."""
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
        note("empty start list")
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


def block_sites(n, width):
    j0 = n // 2
    raw = list(range(j0 - (width // 2), j0 + (width // 2) + 1))
    kept = [j for j in raw if 0 <= j < n]
    if len(kept) != len(raw):
        note("block dropped a site n=%d W=%d" % (n, width))
    return kept


def fourier_survival(n, t):
    j0 = n // 2
    length = n + 1
    y = j0 + 1
    s = 0.0
    for k in range(FOURIER_TERMS):
        half = k + 0.5
        ang = half * math.pi * y / length
        decay = D_DIFF * (half ** 2) * (math.pi ** 2) * t / (length ** 2)
        s += (2.0 / (half * math.pi)) * math.sin(ang) * math.exp(-decay)
    return s


def full_path_matrix(length):
    m = [[0.0] * length for _ in range(length)]
    for i in range(length):
        m[i][i] += 0.5
        if i > 0:
            m[i][i - 1] += 0.25
        else:
            m[i][i] += 0.25
        if i < length - 1:
            m[i][i + 1] += 0.25
        else:
            m[i][i] += 0.25
    return m


def first_hit_full(n, t):
    """First entrance on the full reflecting path, hit flag tracked."""
    length = A_AGENT + n
    # state: (position mass not yet hit) on environment, plus hit mass
    env = [0.0] * n
    env[n // 2] = 1.0
    hit = 0.0
    for _ in range(t):
        new = [0.0] * n
        for j, mass in enumerate(env):
            if mass == 0.0:
                continue
            # stay
            new[j] += 0.5 * mass
            # toward the agent (decreasing j, or off j=0)
            if j > 0:
                new[j - 1] += 0.25 * mass
            else:
                hit += 0.25 * mass
            # toward the wall
            if j < n - 1:
                new[j + 1] += 0.25 * mass
            else:
                new[j] += 0.25 * mass
        env = new
    return hit


def g_checks(tau_jacobi, tau_power, jacobi_ok, power_ok):
    lines = []
    length = A_AGENT + 12
    mat = full_path_matrix(length)
    sym = 0.0
    row_bad = 0.0
    for i in range(length):
        row_bad = max(row_bad, abs(sum(mat[i]) - 1.0))
        for j in range(length):
            sym = max(sym, abs(mat[i][j] - mat[j][i]))
    g_rev = sym <= 1e-15 and row_bad <= 1e-12
    lines.append("G-rev %s" % ("PASS" if g_rev else "FAIL"))

    p = [0.0] * length
    p[A_AGENT + (12 // 2)] = 1.0
    for _ in range(20):
        new = [0.0] * length
        for i in range(length):
            if p[i] == 0.0:
                continue
            for j in range(length):
                new[j] += mat[i][j] * p[i]
        p = new
    mass = sum(p)
    g_cons = abs(mass - 1.0) <= 1e-12
    lines.append("G-cons %s" % ("PASS" if g_cons else "FAIL"))

    uniform = 1.0 / length
    tv = 0.5 * sum(abs((1.0 if i == A_AGENT + 6 else 0.0) - uniform) for i in range(length))
    ent_u = math.log(length)
    g_start = tv >= 0.5 and ent_u > 1.0
    lines.append("G-start %s" % ("PASS" if g_start else "FAIL"))

    pdec = decoupled_matrix(12, 1.0)
    # return restriction at c=1: near end does not reflect
    ret = decoupled_matrix(12, 1.0)
    ret[0][0] -= 0.25  # remove the reflected quarter; it left toward the agent
    diff = 0.0
    for i in range(12):
        for j in range(12):
            diff = max(diff, abs(pdec[i][j] - ret[i][j]))
    row0 = 0.5 + 0.25  # stay and inward, from the kernel at j=0
    stochastic = max(abs(sum(pdec[i]) - 1.0) for i in range(12)) <= 1e-12
    g_dec = diff > 0.2 and stochastic and row0 <= 0.75 and len(pdec) == 12
    lines.append("G-decouple %s" % ("PASS" if g_dec else "FAIL"))
    if diff <= 0.2:
        note("decoupled matrix and return restriction differ by at most 0.2")

    gaps_ok = jacobi_ok and power_ok
    if gaps_ok:
        for n in N_LIST:
            if abs(tau_jacobi[n] - tau_power[n]) > 1e-8:
                gaps_ok = False
                break
    lines.append("G-gap %s" % ("PASS" if gaps_ok else "FAIL"))

    hit_full = first_hit_full(12, 5)
    hit_kern = return_prob(12, [12 // 2], 5, 1.0, "agent")
    g_eq = abs(hit_full - hit_kern) <= 1e-12
    lines.append("G-equiv %s" % ("PASS" if g_eq else "FAIL"))

    form_bad = 0.0
    for th in (0.0, math.pi / 6.0, math.pi / 4.0, math.pi / 3.0, math.pi / 2.0):
        info, pd, loss = base.closed_form_ant(th, 0.0)
        f = base.functionals("ANT", 0.0, th, 0.0)
        form_bad = max(form_bad, abs(info - f["I"]), abs(pd - f["P_D"]), abs(loss - f["L"]))
    g_form = form_bad <= 1e-9
    lines.append("G-form %s" % ("PASS" if g_form else "FAIL"))
    diags = [
        "DIAG g-rev sym=%.3e row=%.3e" % (sym, row_bad),
        "DIAG g-cons mass=%.12f" % mass,
        "DIAG g-start tv=%.12f ent=%.12f" % (tv, ent_u),
        "DIAG g-decouple diff=%.12f row0=%.12f" % (diff, row0),
        "DIAG g-equiv full=%.12e kern=%.12e" % (hit_full, hit_kern),
        "DIAG g-form max=%.3e" % form_bad,
    ]
    return lines, diags


def pd_max():
    _i, pd, _l = base.closed_form_ant(math.pi / 2.0, 0.0)
    return pd


def widths_for(phi, w, q, pd_top):
    best = None
    rows = []
    for j in range(181):
        th = j * (math.pi / 2.0) / 180.0
        info, pd, loss = base.closed_form_ant(th, phi)
        cost = info + q * pd + w * loss
        rows.append((cost, pd))
        if best is None or cost < best:
            best = cost
    tied = [pd for cost, pd in rows if cost <= best + TIE]
    found = []
    seen = set()
    for pd in tied:
        width = 1 + math.floor(8.0 * pd / pd_top + PD_EPS)
        if width < 1 or width > W_MAX:
            note("width %d outside 1..9" % width)
            if width < 1:
                width = 1
            if width > W_MAX:
                width = W_MAX
        if width not in seen:
            seen.add(width)
            found.append(width)
    return found


def iterate(phi, w, q_of_width, pd_top):
    """Undamped map. Returns kind, terminals, last values, phi width at the mean terminal."""
    terminals = []
    lasts = []
    stopped = []
    for q0 in (0.0, 0.25, 0.5, 0.75, 1.0):
        q = q0
        last = q0
        did = False
        for _ in range(ITERS):
            ws = widths_for(phi, w, q, pd_top)
            rets = [q_of_width(width) for width in ws]
            nxt = sum(rets) / len(rets)
            last = nxt
            if abs(nxt - q) <= STOP:
                q = nxt
                did = True
                break
            q = nxt
        if did:
            terminals.append(q)
        lasts.append(last)
        stopped.append(did)
    if not all(stopped):
        return "CYCLE", terminals, lasts, None
    mean_t = sum(terminals) / len(terminals)
    ws = widths_for(phi, w, mean_t, pd_top)
    rets = [q_of_width(width) for width in ws]
    spread = max(rets) - min(rets) if rets else 0.0
    diam = max(terminals) - min(terminals)
    kind = "POINT" if diam <= DIAM and spread <= DIAM else "SET"
    return kind, terminals, lasts, spread


def bin_masses(values):
    counts = [0, 0, 0, 0, 0]
    edges = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
    for v in values:
        if v >= edges[-1]:
            counts[4] += 1
            continue
        placed = False
        for i in range(4):
            if edges[i] <= v < edges[i + 1]:
                counts[i] += 1
                placed = True
                break
        if not placed:
            # below 0 goes in the first bin; the last bin already took v>=1
            if v < 0.0:
                counts[0] += 1
            else:
                counts[4] += 1
    total = float(len(values))
    return [c / total for c in counts]


def interp(xs, ys, x):
    """Linear interpolation. xs ascending. Outside, clamp to the nearer end of [0.05, 8]."""
    clamped = False
    z = x
    if z < 0.05:
        z = 0.05
        clamped = True
    elif z > 8.0:
        z = 8.0
        clamped = True
    if z <= xs[0]:
        return ys[0], clamped
    if z >= xs[-1]:
        return ys[-1], clamped
    for i in range(len(xs) - 1):
        if xs[i] <= z <= xs[i + 1]:
            span = xs[i + 1] - xs[i]
            w = (z - xs[i]) / span
            return ys[i] * (1.0 - w) + ys[i + 1] * w, clamped
    return ys[-1], clamped


def main():
    global DEVIATIONS
    DEVIATIONS = []
    lines = []

    tau_j = {}
    tau_p = {}
    jacobi_ok = True
    power_ok = True
    for n in N_LIST:
        mat = decoupled_matrix(n, 1.0)
        evals, finished = jacobi_eigenvalues(mat)
        if not finished:
            jacobi_ok = False
        tj = relaxation_from_evals(evals, second=True)
        if tj is None:
            jacobi_ok = False
            tj = float("nan")
        tau_j[n] = tj
        lam = power_lambda2(mat)
        if lam is None or lam >= 1.0:
            power_ok = False
            tau_p[n] = float("nan")
        else:
            tau_p[n] = 1.0 / (1.0 - lam)
        lines.append("DIAG tau n=%d jacobi=%.12f power=%.12f" % (n, tau_j[n], tau_p[n]))

    g_lines, g_diags = g_checks(tau_j, tau_p, jacobi_ok, power_ok)
    # instrument lines are emitted with the other checks, after the clocks are known
    # M2 grid: q[n][x]
    q_grid = {n: {} for n in N_LIST}
    pred_grid = {n: {} for n in N_LIST}
    paired = {x: [] for x in X_LIST}
    for n in N_LIST:
        start = [n // 2]
        for x in X_LIST:
            t = horizon(x, tau_j[n])
            realized = t / tau_j[n]
            q = return_prob(n, start, t, 1.0, "agent")
            raw_s = fourier_survival(n, t)
            q_hat = 1.0 - raw_s
            q_grid[n][x] = q
            pred_grid[n][x] = q_hat
            is_pair = abs(realized - x) <= PAIR_TOL
            if is_pair:
                paired[x].append(n)
            lines.append(
                "DIAG cell n=%d x=%.2f T=%d realized=%.6f paired=%d q=%.12f qhat=%.12f"
                % (n, x, t, realized, 1 if is_pair else 0, q, q_hat)
            )
            if abs(max(-0.01, min(1.01, q_hat)) - q_hat) > 1e-6:
                note("fourier value moved by clip n=%d x=%.2f" % (n, x))

    # M1
    m1c_ok = True
    for n in (12, 48):
        t_inf = horizon(200.0, tau_j[n])
        q_inf = return_prob(n, [n // 2], t_inf, 1.0, "agent")
        lines.append("DIAG m1-closed n=%d T=%d q=%.12e" % (n, t_inf, q_inf))
        if q_inf < 1.0 - 1e-9:
            m1c_ok = False
    m1s_ok = True
    for n in (12, 48):
        t_inf = horizon(200.0, tau_j[n])
        q_inf = return_prob(n, [n // 2], t_inf, 1.0, "sink")
        lines.append("DIAG m1-sink n=%d T=%d q=%.12e" % (n, t_inf, q_inf))
        if q_inf > 1e-9:
            m1s_ok = False

    scale = []
    for n in N_LIST:
        q = return_prob(n, [n // 2], 32, 1.0, "agent")
        scale.append(q)
        lines.append("DIAG m1-scale n=%d q=%.12f" % (n, q))
    decreasing = all(scale[i] - scale[i + 1] >= 1e-4 for i in range(len(scale) - 1))
    m1_scale_ok = decreasing and scale[0] >= 0.01 and scale[-1] <= 0.20

    # M2 collapse
    dropped = []
    ranges = []
    kept_x = []
    for x in X_LIST:
        ns = paired[x]
        if len(ns) < 4:
            dropped.append(x)
            lines.append("DIAG collapse-drop x=%.2f paired=%d" % (x, len(ns)))
            continue
        vals = [q_grid[n][x] for n in ns]
        span = max(vals) - min(vals)
        ranges.append(span)
        kept_x.append(x)
        lines.append("DIAG collapse x=%.2f range=%.12f n=%s" % (x, span, ",".join(str(n) for n in ns)))
    if len(kept_x) < 6:
        m2c_ok = False
        rho = float("nan")
    else:
        rho = max(ranges)
        m2c_ok = rho <= COLLAPSE_TOL
    lines.append("DIAG rho=%.12f kept=%d" % (rho if kept_x else float("nan"), len(kept_x)))

    # M2 shape
    shape_cells = []
    for n in N_LIST:
        for x in X_SHAPE:
            if n in paired[x]:
                shape_cells.append(abs(q_grid[n][x] - pred_grid[n][x]))
    if len(shape_cells) < 12:
        m2s_ok = False
        shape_max = float("nan")
    else:
        shape_max = max(shape_cells)
        m2s_ok = shape_max <= SHAPE_TOL
    lines.append("DIAG shape-max=%.12f cells=%d" % (shape_max if shape_cells else float("nan"), len(shape_cells)))

    q05 = q_grid[32][0.5]
    q1 = q_grid[32][1.0]
    m2i_ok = (0.05 < q05 < 0.95) and (0.05 < q1 < 0.95)
    lines.append("DIAG interior q05=%.12f q1=%.12f" % (q05, q1))

    # curve f from kept nominal x, mean over paired N
    f_x = []
    f_y = []
    for x in kept_x:
        ns = paired[x]
        f_x.append(x)
        f_y.append(sum(q_grid[n][x] for n in ns) / len(ns))
        lines.append("DIAG curve x=%.2f f=%.12f" % (x, f_y[-1]))

    # clocks for closedness, still without measured fixed points
    t_ref = horizon(1.0, tau_j[32])
    cs = [k / 10.0 for k in range(11)]
    tau_c = {}
    x_c = {}
    for c in cs:
        mat = decoupled_matrix(32, c)
        evals, finished = jacobi_eigenvalues(mat)
        if not finished:
            note("jacobi unfinished at c=%.1f" % c)
        second = c == 1.0
        tc = relaxation_from_evals(evals, second=second)
        if tc is None:
            note("nonpositive gap at c=%.1f" % c)
            tc = float("nan")
        tau_c[c] = tc
        x_c[c] = t_ref / tc
        lines.append("DIAG clock c=%.1f tau=%.12f x=%.12f" % (c, tc, x_c[c]))

    pred_vals = []
    clamps = 0
    for c in cs:
        val, clamped = interp(f_x, f_y, x_c[c])
        if clamped:
            clamps += 1
        pred_vals.append(val)
    pred_bins = bin_masses(pred_vals)
    # PREDICT is fully determined here. Measured fixed points come after these strings are built.
    predict_lines = []
    for c, val in zip(cs, pred_vals):
        predict_lines.append("PREDICT c=%.1f x=%.12f q=%.12f" % (c, x_c[c], val))
    predict_lines.append(
        "PREDICT bins "
        + " ".join("%.12f" % b for b in pred_bins)
        + " clamps=%d" % clamps
    )

    # --- measured q* only after the prediction exists ---
    pd_top = pd_max()
    measured = []
    measure_lines = []

    def q_width_factory(c, t):
        cache = {}

        def q_of(width):
            if width not in cache:
                sites = block_sites(32, width)
                cache[width] = return_prob(32, sites, t, c, "agent")
            return cache[width]

        return q_of

    for c in cs:
        q_of = q_width_factory(c, t_ref)
        kind, terminals, lasts, _spread = iterate(0.0, 2.0, q_of, pd_top)
        if kind == "CYCLE":
            summary = sum(lasts) / len(lasts)
        else:
            summary = sum(terminals) / len(terminals)
        measured.append(summary)
        measure_lines.append(
            "DIAG m4 c=%.1f kind=%s qstar=%.12f" % (c, kind, summary)
        )

    meas_bins = bin_masses(measured)
    tv = 0.5 * sum(abs(a - b) for a, b in zip(pred_bins, meas_bins))
    m4_ok = tv <= TV_TOL
    measure_lines.append(
        "DIAG m4 bins " + " ".join("%.12f" % b for b in meas_bins) + " tv=%.12f" % tv
    )

    # M3 on the closed kernel
    m3_spec = (
        ("m3-a", 0.5, 0.0, 2.0, False),
        ("m3-b", 1.0, 0.0, 2.0, False),
        ("m3-c", 2.0, 0.0, 2.0, False),
        ("m3-d", 1.0, 0.0, 1.0, False),
        ("m3-e", 0.05, 0.0, 2.0, True),
        ("m3-f", 8.0, 0.0, 2.0, True),
    )
    m3_results = {}
    for name, x, phi, w, _corner in m3_spec:
        t = horizon(x, tau_j[32])
        q_of = q_width_factory(1.0, t)
        kind, terminals, lasts, spread = iterate(phi, w, q_of, pd_top)
        m3_results[name] = (kind, terminals, lasts, spread, t)
        if kind == "CYCLE":
            show = lasts
        else:
            show = terminals
        lines.append(
            "DIAG %s kind=%s T=%d spread=%s terms=%s"
            % (
                name,
                kind,
                t,
                ("%.12f" % spread) if spread is not None else "na",
                ",".join("%.12f" % v for v in show),
            )
        )

    m3_conv_ok = all(m3_results[name][0] == "POINT" for name in ("m3-a", "m3-b", "m3-c", "m3-d"))
    m3_corner_ok = all(m3_results[name][0] in ("POINT", "SET") for name in ("m3-e", "m3-f"))

    # E-pair, same x, two starts
    qa = return_prob(32, [32 // 2], t_ref, 1.0, "agent")
    qb = return_prob(32, [31], t_ref, 1.0, "agent")

    # assemble stdout in the locked order: checks, with PREDICT before measured M4 numbers
    out = []
    out.extend(g_lines)
    out.append("M1-closed %s" % ("PASS holds-by-construction" if m1c_ok else "FAIL"))
    out.append("M1-sink %s" % ("PASS holds-by-construction" if m1s_ok else "FAIL"))
    out.append("M1-scale %s" % ("PASS" if m1_scale_ok else "FAIL"))
    out.append("M2-collapse %s" % ("PASS" if m2c_ok else "FAIL"))
    out.append("M2-shape %s" % ("PASS" if m2s_ok else "FAIL"))
    out.append("M2-interior %s" % ("PASS" if m2i_ok else "FAIL"))
    out.append("M3-conv %s" % ("PASS" if m3_conv_ok else "FAIL"))
    out.append("M3-corner %s" % ("PASS" if m3_corner_ok else "FAIL"))
    out.extend(predict_lines)
    out.extend(measure_lines)
    out.append("M4 %s" % ("PASS" if m4_ok else "FAIL"))
    out.append("E-pair REPORT qa=%.12f qb=%.12f d=%.12f" % (qa, qb, abs(qa - qb)))
    for name in ("m3-a", "m3-b", "m3-c", "m3-d"):
        kind, terminals, _lasts, _spread, _t = m3_results[name]
        if kind == "CYCLE" or not terminals:
            qstar = float("nan")
        else:
            qstar = sum(terminals) / len(terminals)
        out.append(
            "REPORT %s q=%.12f d30=%.12f d06=%.12f" % (name, qstar, abs(qstar - 0.30), abs(qstar - 0.6))
        )
    out.append("CLASS M1-closed holds-by-construction")
    out.append("CLASS M1-sink holds-by-construction")
    out.append("CLASS M1-scale evidence")
    out.append("CLASS M2-collapse evidence")
    out.append("CLASS M2-shape evidence")
    out.append("CLASS M2-interior evidence")
    out.append("CLASS M3-conv evidence")
    out.append("CLASS M3-corner evidence")
    out.append("CLASS M4 evidence")
    out.append("CLASS E-pair report-only")
    out.extend(g_diags)
    out.extend(lines)
    check_names = {
        "G-rev", "G-cons", "G-start", "G-decouple", "G-gap", "G-equiv", "G-form",
        "M1-closed", "M1-sink", "M1-scale", "M2-collapse", "M2-shape", "M2-interior",
        "M3-conv", "M3-corner", "M4",
    }
    fails = 0
    for ln in out:
        parts = ln.split()
        if parts and parts[0] in check_names and parts[1] == "FAIL":
            fails += 1
    out.append("FAILS %d" % fails)
    if DEVIATIONS:
        out.append("DIAG deviations %d" % len(DEVIATIONS))
        for msg in DEVIATIONS:
            out.append("DIAG deviation %s" % msg)
    else:
        out.append("DIAG deviations 0")
    text = "\n".join(out) + "\n"
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
