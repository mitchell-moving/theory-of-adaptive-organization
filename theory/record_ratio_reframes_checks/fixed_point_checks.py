#!/usr/bin/env python3
"""T76 fixed-point checks. Criteria are PREREG_FIXED_POINTS.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
R = base.R
N_GRID = base.N_GRID
TIE = base.TIE
PI = base.PI
HALF_PI = base.HALF_PI
STEP = HALF_PI / N_GRID


def w_pi(abs_delta: float) -> float:
    return abs_delta / (R * R)


def w_0(abs_delta: float) -> float:
    return abs_delta * math.log((1.0 + R) / (1.0 - R)) / (2.0 * R ** 3)


def w_crit(theta: float, abs_delta: float) -> float:
    c = math.cos(theta)
    return abs_delta * math.log((1.0 + R * c) / (1.0 - R * c)) / (2.0 * R ** 3 * c)


def solve_crit(abs_delta: float, w: float):
    """Unique root of w_crit = w on (0, pi/2), or None if it is not bracketed once."""
    lo = 1e-8
    hi = HALF_PI - 1e-8

    def f(th):
        return w_crit(th, abs_delta) - w

    if f(lo) < 0.0 or f(hi) > 0.0:
        return None, 0
    sign_changes = 0
    prev = f(lo)
    grid_n = 2000
    for i in range(1, grid_n + 1):
        th = lo + (hi - lo) * i / grid_n
        cur = f(th)
        if prev == 0.0 or prev * cur < 0.0:
            sign_changes += 1
        prev = cur
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), sign_changes


class Report:
    def __init__(self):
        self.fails = []
        self.lines = []

    def add(self, name, ok, detail):
        tag = "PASS" if ok else "FAIL"
        self.lines.append(f"{name} {tag} {detail}")
        if not ok:
            self.fails.append(name)

    def dump(self):
        for line in self.lines:
            print(line)
        print(f"FAILS {len(self.fails)}")


def binom_pmf(n: int, k: int, p: float) -> float:
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    if p >= 1.0:
        return 1.0 if k == n else 0.0
    logc = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    return math.exp(logc + k * math.log(p) + (n - k) * math.log(1.0 - p))


def repeated(name: str, gamma: float, theta: float, phi: float, n: int):
    """I(W;K), single-copy P_D, L from the count K of n i.i.d. pinches."""
    rows = base.ensemble_rows(name)
    nv = base.n_theta(theta)
    weights = []
    ps = []
    ys = []
    for weight, pre in rows:
        post = base.dephase(pre, gamma)
        weights.append(weight)
        ps.append(0.5 * (1.0 + base.dot(nv, post)))
        ys.append(math.sin(phi) * pre[0] + math.cos(phi) * pre[2])
    one = base.functionals(name, gamma, theta, phi)
    pmfs = []
    for p in ps:
        pmfs.append([binom_pmf(n, k, p) for k in range(n + 1)])
    pk = []
    hk_w = 0.0
    for weight, pmf in zip(weights, pmfs):
        ent = 0.0
        for prob in pmf:
            if prob > 0.0:
                ent -= prob * math.log(prob)
        hk_w += weight * ent
    h_k = 0.0
    for k in range(n + 1):
        mass = 0.0
        for weight, pmf in zip(weights, pmfs):
            mass += weight * pmf[k]
        pk.append(mass)
        if mass > 0.0:
            h_k -= mass * math.log(mass)
    info = h_k - hk_w
    a_hat = []
    for k in range(n + 1):
        if pk[k] <= 0.0:
            a_hat.append(0.0)
            continue
        acc = 0.0
        for weight, pmf, y in zip(weights, pmfs, ys):
            acc += weight * pmf[k] * y
        a_hat.append(acc / pk[k])
    loss = 0.0
    for weight, pmf, y in zip(weights, pmfs, ys):
        for k in range(n + 1):
            d = y - a_hat[k]
            loss += weight * pmf[k] * d * d
    return {"I": info, "P_D": one["P_D"], "L": loss, "ledger_rep": info + n * one["P_D"]}


def minimize_rep(name, gamma, phi, kappa, kappa_d, w, n, thetas):
    best = None
    vals = []
    for th in thetas:
        rec = repeated(name, gamma, th, phi, n)
        j = kappa * rec["I"] + kappa_d * n * rec["P_D"] + w * rec["L"]
        vals.append(j)
        if best is None or j < best:
            best = j
    tied = [thetas[i] for i, j in enumerate(vals) if j <= best + TIE]
    return {"theta": tied[0], "tied": tied, "J": best, "unique": len(tied) == 1, "vals": vals}


def j_rep_at(name, gamma, phi, kappa, kappa_d, w, n, theta):
    rec = repeated(name, gamma, theta, phi, n)
    return kappa * rec["I"] + kappa_d * n * rec["P_D"] + w * rec["L"], rec


def second_pinch(name, gamma, theta1, theta2):
    rows = base.ensemble_rows(name)
    n1 = base.n_theta(theta1)
    n2 = base.n_theta(theta2)
    dot12 = base.dot(n1, n2)
    p2_given = (0.5 * (1.0 + dot12), 0.5 * (1.0 - dot12))
    h2 = (base.hbin(p2_given[0]), base.hbin(p2_given[1]))
    p1s = []
    weights = []
    for weight, pre in rows:
        post = base.dephase(pre, gamma)
        weights.append(weight)
        p1s.append(0.5 * (1.0 + base.dot(n1, post)))
    p_m1 = 0.0
    h_cond_w = 0.0
    p_d2 = 0.0
    for weight, p1 in zip(weights, p1s):
        p_m1 += weight * p1
        h_cond_w += weight * (p1 * h2[0] + (1.0 - p1) * h2[1])
        p_d2 += weight * (p1 * h2[0] + (1.0 - p1) * h2[1])
    h_cond = p_m1 * h2[0] + (1.0 - p_m1) * h2[1]
    return {"I": h_cond - h_cond_w, "P_D2": p_d2}


def product_cost(kappa, kappa_d, w, theta):
    """Two independent ANT draws, each pinched once. Sum of costs, computed from the joint."""
    rows = []
    for weight, pre in base.ANT:
        post = base.dephase(pre, 0.0)
        nv = base.n_theta(theta)
        p = 0.5 * (1.0 + base.dot(nv, post))
        y = pre[2]
        s_phi = base.hbin(p)
        s_rho = base.qubit_entropy(base.norm(post))
        rows.append((weight, p, y, s_phi, s_rho))
    # joint outcome masses and conditional entropy
    masses = [0.0, 0.0, 0.0, 0.0]  # (m1, m2) with m=0 -> +
    h_cond = 0.0
    p_d = 0.0
    # loss adds across the two separate predictions; build each from the marginal
    one = base.functionals("ANT", 0.0, theta, 0.0)
    for w1, p1, _y1, s1, r1 in rows:
        for w2, p2, _y2, s2, r2 in rows:
            ww = w1 * w2
            probs = (p1 * p2, p1 * (1.0 - p2), (1.0 - p1) * p2, (1.0 - p1) * (1.0 - p2))
            for i, pr in enumerate(probs):
                masses[i] += ww * pr
            h_cond += ww * (s1 + s2)
            p_d += ww * ((s1 - r1) + (s2 - r2))
    h_m = 0.0
    for pr in masses:
        if pr > 0.0:
            h_m -= pr * math.log(pr)
    info = h_m - h_cond
    return kappa * info + kappa_d * p_d + w * (2.0 * one["L"])


def record_cost(name, gamma, theta, kappa, delta):
    f = base.functionals(name, gamma, theta, 0.0)
    kappa_d = kappa + delta
    return kappa * f["I"] + kappa_d * f["P_D"], f


def ls_affine(xs, ys, target):
    """target ~ a x + b y + c. Returns a, b, c, max abs residual."""
    n = float(len(target))
    sx = sy = st = 0.0
    sxx = syy = sxy = sxt = syt = 0.0
    for x, y, t in zip(xs, ys, target):
        sx += x
        sy += y
        st += t
        sxx += x * x
        syy += y * y
        sxy += x * y
        sxt += x * t
        syt += y * t
    # rows [sxx, sxy, sx], [sxy, syy, sy], [sx, sy, n]
    a = [
        [sxx, sxy, sx, sxt],
        [sxy, syy, sy, syt],
        [sx, sy, n, st],
    ]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda i: abs(a[i][col]))
        a[col], a[pivot] = a[pivot], a[col]
        div = a[col][col]
        if abs(div) < 1e-18:
            return None
        for j in range(col, 4):
            a[col][j] /= div
        for i in range(3):
            if i == col:
                continue
            factor = a[i][col]
            for j in range(col, 4):
                a[i][j] -= factor * a[col][j]
    aa, bb, cc = a[0][3], a[1][3], a[2][3]
    max_abs = 0.0
    for x, y, t in zip(xs, ys, target):
        max_abs = max(max_abs, abs(aa * x + bb * y + cc - t))
    return aa, bb, cc, max_abs


def cell_phase(q, w):
    delta = q - 1.0  # kappa = 1
    if abs(delta) <= 1e-15:
        if w == 0.0:
            return "flat", 0.0
        return "pointer", 0.0
    if delta > 0.0:
        return "pointer", delta
    ad = abs(delta)
    if w < w_pi(ad):
        return "equator", delta
    if w > w_0(ad):
        return "pointer", delta
    return "interior", delta


def matches_phase(phase, minimized, root):
    if phase == "flat":
        vals = minimized["vals"]
        return (max(vals) - min(vals)) < 1e-9
    if phase == "equator":
        return minimized["unique"] and abs(minimized["theta"] - HALF_PI) <= 1e-12
    if phase == "pointer":
        return minimized["unique"] and abs(minimized["theta"]) <= 1e-12
    if root is None:
        return False
    interior = STEP < minimized["theta"] < HALF_PI - STEP
    close = abs(minimized["theta"] - root) <= STEP + 1e-9
    return minimized["unique"] and interior and close


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    thetas = base.theta_grid()

    # n=1 repeated record must reproduce the single-copy functionals. A miss is a code bug.
    bug = 0.0
    for name in ("ANT", "BIAS"):
        for th in (0.0, 0.3, PI / 4.0, 1.0, HALF_PI):
            one = base.functionals(name, 0.0, th, 0.0)
            rec = repeated(name, 0.0, th, 0.0, 1)
            bug = max(bug, abs(one["I"] - rec["I"]), abs(one["P_D"] - rec["P_D"]), abs(one["L"] - rec["L"]))
    if bug >= 1e-10:
        raise SystemExit(f"n=1 repeated record mismatches single copy by {bug}")

    # ----- phase boundary -----
    mono_vals = []
    for i in range(50):
        th = 0.02 + i * (HALF_PI - 0.04) / 49.0
        mono_vals.append(w_crit(th, 1.0))
    mono_ok = all(mono_vals[i] > mono_vals[i + 1] for i in range(49))
    rep.add(
        "T-mono",
        mono_ok,
        f"w_crit(0.02)={mono_vals[0]:.6f} w_crit(end)={mono_vals[-1]:.6f} decreases={mono_ok}",
    )

    cells = (
        (0.0, 1.0),
        (0.0, 3.0),
        (0.0, 10.0),
        (0.5, 1.0),
        (0.5, 1.5),
        (0.5, 2.0),
        (0.67, 1.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (2.0, 1.0),
    )
    cell_ok = True
    bits = []
    for q, w in cells:
        phase, delta = cell_phase(q, w)
        m = base.minimize("ANT", 0.0, 0.0, 1.0, q, w, thetas)
        root = None
        n_sign = 0
        if phase == "interior":
            root, n_sign = solve_crit(abs(delta), w)
            if n_sign != 1:
                cell_ok = False
        ok = matches_phase(phase, m, root)
        cell_ok = cell_ok and ok
        root_s = f"{root:.6f}" if root is not None else "-"
        bits.append(
            f"q={q} w={w} phase={phase} theta={m['theta']:.6f} n_tie={len(m['tied'])} "
            f"root={root_s} signs={n_sign} ok={ok}"
        )
    rep.add("T-cells", cell_ok, " | ".join(bits))

    def quotients(kappa_d, w):
        j0 = base.functionals("ANT", 0.0, 0.0, 0.0)
        jh = base.functionals("ANT", 0.0, 1e-4, 0.0)
        left = base.functionals("ANT", 0.0, HALF_PI - 1e-4, 0.0)
        right = base.functionals("ANT", 0.0, HALF_PI, 0.0)

        def j(f):
            return 1.0 * f["I"] + kappa_d * f["P_D"] + w * f["L"]

        q_right = (j(jh) - j(j0)) / 1e-4
        q_left = (j(right) - j(left)) / 1e-4
        return q_right, q_left

    slope_specs = (
        ("q=0 w=1", 0.0, 1.0, -1.0, -1.0),
        ("q=0 w=10", 0.0, 10.0, 1.0, 1.0),
        ("q=0.5 w=1.5", 0.5, 1.5, -1.0, 1.0),
    )
    slope_ok = True
    slope_bits = []
    for label, kd, w, sign_right, sign_left in slope_specs:
        qr, ql = quotients(kd, w)
        ok = (
            qr * sign_right > 1e-6
            and ql * sign_left > 1e-6
            and abs(qr) > 1e-6
            and abs(ql) > 1e-6
        )
        slope_ok = slope_ok and ok
        slope_bits.append(f"{label} right={qr:.6e} left={ql:.6e} ok={ok}")
    rep.add("T-slope", slope_ok, " | ".join(slope_bits))

    root_g0, _ = solve_crit(1.0, 3.0)
    m_g = base.minimize("ANT", 0.5, 0.0, 1.0, 0.0, 3.0, thetas)
    gap_g = abs(m_g["theta"] - root_g0)
    rep.add(
        "T-gamma",
        gap_g >= 0.1,
        f"root_gamma0={root_g0:.6f} theta_gamma_half={m_g['theta']:.6f} "
        f"n_tie={len(m_g['tied'])} gap={gap_g:.6f}",
    )

    lam_rows = ((0.0, "equator"), (0.5, "equator"), (0.66, "interior"), (0.8, "pointer"), (1.0, "pointer"))
    lam_ok = True
    lam_bits = []
    for lam, _expect in lam_rows:
        phase, delta = cell_phase(lam, 1.0)  # charged q_eff = lambda when nominal q=1, kappa=1
        m = base.minimize("ANT", 0.0, 0.0, 1.0, lam, 1.0, thetas)
        root = None
        if phase == "interior":
            root, n_sign = solve_crit(abs(delta), 1.0)
            if n_sign != 1:
                lam_ok = False
        ok = matches_phase(phase, m, root)
        lam_ok = lam_ok and ok
        root_s = f"{root:.6f}" if root is not None else "-"
        lam_bits.append(f"lambda={lam} phase={phase} theta={m['theta']:.6f} n_tie={len(m['tied'])} root={root_s} ok={ok}")
    rep.add("T-lambda", lam_ok, " | ".join(lam_bits))

    # ----- flow -----
    seq_ok = True
    seq_bits = []
    angles = (0.0, PI / 4.0, HALF_PI)
    max_i = 0.0
    same_pd = 0.0
    right_pd = None
    for name in ("ANT", "BIAS"):
        for t1 in angles:
            for t2 in angles:
                sec = second_pinch(name, 0.0, t1, t2)
                max_i = max(max_i, abs(sec["I"]))
                if abs(t1 - t2) <= 1e-15:
                    same_pd = max(same_pd, abs(sec["P_D2"]))
                if abs(t1) <= 1e-15 and abs(t2 - HALF_PI) <= 1e-15 and name == "ANT":
                    right_pd = sec["P_D2"]
    added_best = None
    for th2 in thetas:
        sec = second_pinch("ANT", 0.0, 0.0, th2)
        added = 1.0 * sec["I"] + 1.0 * sec["P_D2"]
        if added_best is None or added < added_best:
            added_best = added
    seq_ok = max_i < 1e-9 and same_pd < 1e-9 and right_pd is not None and right_pd > 0.05 and added_best < 1e-9
    rep.add(
        "F-seq",
        seq_ok,
        f"max_I={max_i:.3e} same_basis_P_D={same_pd:.3e} right_angle_P_D={right_pd:.6f} added_min={added_best:.3e}",
    )

    prod_ok = True
    prod_bits = []
    for q, w in ((0.0, 1.0), (1.0, 1.0), (2.0, 1.0)):
        single = base.minimize("ANT", 0.0, 0.0, 1.0, q, w, thetas)
        best = None
        tied = []
        max_gap = 0.0
        for th in (0.0, 0.3, PI / 4.0, 1.0, HALF_PI):
            one = base.functionals("ANT", 0.0, th, 0.0)
            j1 = 1.0 * one["I"] + q * one["P_D"] + w * one["L"]
            jp = product_cost(1.0, q, w, th)
            max_gap = max(max_gap, abs(jp - 2.0 * j1))
        vals = []
        for th in thetas:
            jv = product_cost(1.0, q, w, th)
            vals.append(jv)
            if best is None or jv < best:
                best = jv
        tied = [thetas[i] for i, jv in enumerate(vals) if jv <= best + TIE]
        sep = abs(tied[0] - single["theta"])
        ok = max_gap < 1e-9 and sep <= STEP + 1e-12
        prod_ok = prod_ok and ok
        prod_bits.append(f"q={q} w={w} max_cost_gap={max_gap:.3e} theta_prod={tied[0]:.6f} theta_one={single['theta']:.6f} ok={ok}")
    rep.add("F-prod", prod_ok, " | ".join(prod_bits))

    def mutual_from_channel(pairs):
        p_plus = 0.0
        h_mw = 0.0
        for weight, p in pairs:
            p_plus += weight * p
            h_mw += weight * base.hbin(p)
        return base.hbin(p_plus) - h_mw

    f0 = base.functionals("ANT", 0.0, 0.0, 0.0)
    menu_ok = True
    max_tv = 0.0
    max_gap_miss = 0.0
    pd_half = None
    gap_at_half = None
    for th in thetas:
        direct = []
        garb = []
        eps = 0.5 * (1.0 - math.cos(th))
        for weight, pre in base.ANT:
            post = base.dephase(pre, 0.0)
            vz = post[2]
            p_dir = 0.5 * (1.0 + vz * math.cos(th))
            p0 = 0.5 * (1.0 + vz)
            p_g = (1.0 - eps) * p0 + eps * (1.0 - p0)
            direct.append((weight, p_dir))
            garb.append((weight, p_g))
            max_tv = max(max_tv, abs(p_dir - p_g))
        f = base.functionals("ANT", 0.0, th, 0.0)
        i_dir = mutual_from_channel(direct)
        i_garb = mutual_from_channel(garb)
        # kappa = kappa_D = 1. Garbling path pays the pointer disturbance.
        gap = (i_dir + f["P_D"]) - (i_garb + f0["P_D"])
        max_gap_miss = max(max_gap_miss, abs(gap - f["P_D"]))
        if abs(th - HALF_PI) <= 1e-15:
            pd_half = f["P_D"]
            gap_at_half = gap
    menu_ok = (
        max_tv < 1e-12
        and abs(f0["P_D"]) < 1e-12
        and pd_half is not None
        and pd_half > 0.05
        and max_gap_miss < 1e-12
        and abs(gap_at_half - pd_half) < 1e-12
    )
    rep.add(
        "F-menu",
        menu_ok,
        f"max_channel={max_tv:.3e} max_gap_miss={max_gap_miss:.3e} "
        f"P_D(0)={f0['P_D']:.3e} P_D(pi/2)={pd_half:.6f} gap={gap_at_half:.6f}",
    )

    rep_ok = True
    rep_bits = []
    for n in (1, 2, 8):
        m = minimize_rep("ANT", 0.0, 0.0, 1.0, 0.0, 1.0, n, thetas)
        ok = m["unique"] and abs(m["theta"] - HALF_PI) <= 1e-12
        rep_ok = rep_ok and ok
        rep_bits.append(f"q0_w1_n{n} theta={m['theta']:.6f} n_tie={len(m['tied'])} ok={ok}")
    for n in (1, 2, 8, 20):
        m = minimize_rep("ANT", 0.0, 0.0, 1.0, 1.0, 1.0, n, thetas)
        ok = m["unique"] and abs(m["theta"]) <= 1e-12
        rep_ok = rep_ok and ok
        rep_bits.append(f"q1_w1_n{n} theta={m['theta']:.6f} n_tie={len(m['tied'])} ok={ok}")
    m1 = minimize_rep("ANT", 0.0, 0.0, 1.0, 0.0, 4.0, 1, thetas)
    m8 = minimize_rep("ANT", 0.0, 0.0, 1.0, 0.0, 4.0, 8, thetas)
    j8_eq, _ = j_rep_at("ANT", 0.0, 0.0, 1.0, 0.0, 4.0, 8, HALF_PI)
    j8_0, _ = j_rep_at("ANT", 0.0, 0.0, 1.0, 0.0, 4.0, 8, 0.0)
    ok_w4 = m1["unique"] and abs(m1["theta"]) <= 1e-12 and j8_eq < j8_0 and m8["theta"] >= 0.3
    rep_ok = rep_ok and ok_w4
    rep_bits.append(
        f"q0_w4 n1={m1['theta']:.6f} n8={m8['theta']:.6f} n_tie8={len(m8['tied'])} "
        f"J8_eq={j8_eq:.6f} J8_0={j8_0:.6f} ok={ok_w4}"
    )
    a = minimize_rep("ANT", 0.0, 0.0, 1.0, 0.5, 1.5, 1, thetas)
    b = minimize_rep("ANT", 0.0, 0.0, 1.0, 0.5, 1.5, 8, thetas)
    drop = a["theta"] - max(b["tied"])
    ok_drop = drop >= 0.05 - 1e-12
    rep_ok = rep_ok and ok_drop
    rep_bits.append(
        f"q0.5_w1.5 n1={a['theta']:.6f} n8={b['theta']:.6f} n_tie8={len(b['tied'])} drop={drop:.6f} ok={ok_drop}"
    )
    range_rep = 0.0
    vals_rep = []
    i16 = repeated("ANT", 0.0, 0.0, 0.0, 16)["I"]
    target_inf = 1.5 * math.log(2.0)
    for th in thetas:
        vals_rep.append(repeated("ANT", 0.0, th, 0.0, 2)["ledger_rep"])
    range_rep = max(vals_rep) - min(vals_rep)
    ok_range = range_rep > 0.005
    ok_inf = abs(i16 - target_inf) < 0.02
    j20_eq, _ = j_rep_at("ANT", 0.0, 0.0, 1.0, 1.0, 1.0, 20, HALF_PI)
    j20_0, _ = j_rep_at("ANT", 0.0, 0.0, 1.0, 1.0, 1.0, 20, 0.0)
    ok_cert = j20_eq > j20_0
    rep_ok = rep_ok and ok_range and ok_inf and ok_cert
    rep_bits.append(f"range_I2_plus_2PD={range_rep:.6f} ok={ok_range}")
    rep_bits.append(f"I16={i16:.6f} target={target_inf:.6f} ok={ok_inf}")
    rep_bits.append(f"J20_eq={j20_eq:.6f} J20_0={j20_0:.6f} ok={ok_cert}")
    rep.add("F-rep", rep_ok, " | ".join(rep_bits))

    xs, ys, ts = [], [], []
    for th in thetas:
        one = base.functionals("BIAS", 0.0, th, 0.0)
        two = repeated("BIAS", 0.0, th, 0.0, 2)
        xs.append(one["I"])
        ys.append(one["P_D"])
        ts.append(two["ledger_rep"])
    fit = ls_affine(xs, ys, ts)
    if fit is None:
        rep.add("F-span", False, "singular")
    else:
        aa, bb, cc, resid = fit
        ratio = bb / aa if abs(aa) > 1e-12 else float("nan")
        rep.add(
            "F-span",
            resid > 0.01,
            f"alpha={aa:.6f} beta={bb:.6f} intercept={cc:.6f} beta_over_alpha={ratio:.6f} max_resid={resid:.6e}",
        )

    # ----- duality -----
    def record_sum_range(name, gamma, delta):
        vals = []
        for th in thetas:
            rp, _ = record_cost(name, gamma, th, 1.0, delta)
            rm, _ = record_cost(name, gamma, th, 1.0, -delta)
            vals.append(rp + rm)
        return max(vals) - min(vals)

    r_ant0 = record_sum_range("ANT", 0.0, 1.0)
    r_ant1 = record_sum_range("ANT", 0.5, 1.0)
    r_bias = record_sum_range("BIAS", 0.0, 1.0)
    d_ok = r_ant0 < 1e-9 and r_ant1 < 1e-9 and r_bias > 0.02
    rep.add(
        "D-value",
        d_ok,
        f"range_ANT_g0={r_ant0:.3e} range_ANT_g_half={r_ant1:.3e} range_BIAS={r_bias:.6f}",
    )

    m0 = base.minimize("ANT", 0.0, 0.0, 1.0, 0.0, 1.0, thetas)
    m1 = base.minimize("ANT", 0.0, 0.0, 1.0, 1.0, 1.0, thetas)
    m2 = base.minimize("ANT", 0.0, 0.0, 1.0, 2.0, 1.0, thetas)
    d_arg = (
        m0["unique"]
        and m1["unique"]
        and m2["unique"]
        and abs(m0["theta"] - m1["theta"]) >= 1.0
        and abs(m2["theta"] - m1["theta"]) <= STEP + 1e-12
        and abs(m2["theta"] - m0["theta"]) >= 1.0
    )
    rep.add(
        "D-argmin",
        d_arg,
        f"theta_q0={m0['theta']:.6f} theta_q1={m1['theta']:.6f} theta_q2={m2['theta']:.6f} "
        f"gap01={abs(m0['theta']-m1['theta']):.6f} gap21={abs(m2['theta']-m1['theta']):.6f}",
    )

    rep.dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
