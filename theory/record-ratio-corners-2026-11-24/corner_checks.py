#!/usr/bin/env python3
"""T80 corner checks. Criteria are PREREG.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from. No random module.
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, "..", "record_ratio_reframes_checks"))
if REF not in sys.path:
    sys.path.insert(0, REF)

import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
R = base.R
PI = math.pi
HALF_PI = 0.5 * PI
WINDOW_LO = 0.0
WINDOW_HI = 2.0
GRIDS = (9, 33, 129, 513)
FLOOR = 5e-3
WIDE = 0.01
TOL_MATCH = 1e-3
TIE = 1e-12
SLOPE_TIE = 1e-15
SCAN_STEP = 1e-4
BIN_W = 0.08
N_BINS = 25
PEAK_MASS = 0.10
PEAK_FACTOR = 1.5
CONC_MASS = 0.20
Q_PTR_TARGET = 0.688377871168


class Report:
    def __init__(self):
        self.fails = []
        self.lines = []

    def add(self, name, ok, detail):
        self.lines.append(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
        if not ok:
            self.fails.append(name)

    def dump(self):
        for line in self.lines:
            print(line)
        print(f"FAILS {len(self.fails)}")


def grid(n):
    step = HALF_PI / (n - 1)
    return [j * step for j in range(n)]


def pack(theta, phi):
    info, p_d, loss = base.closed_form_ant(theta, phi)
    return info, p_d, loss


def q_eq(phi, s):
    return 1.0 - s * R * R * math.cos(phi) ** 2


def q_ptr(phi, s):
    return 1.0 - s * (2.0 * R ** 3 * math.cos(phi) ** 2) / math.log((1.0 + R) / (1.0 - R))


def lam_at(theta, phi, s):
    u = math.cos(theta)
    u = min(1.0, max(0.0, u))
    if u <= 1e-15:
        return q_eq(phi, s)
    if u >= 1.0 - 1e-15:
        return q_ptr(phi, s)
    return 1.0 - s * (2.0 * R ** 3 * math.cos(phi) ** 2 * u) / math.log((1.0 + R * u) / (1.0 - R * u))


def clip(x):
    return min(WINDOW_HI, max(WINDOW_LO, x))


def nearest_index(thetas, target):
    best_d = None
    best_i = 0
    for i, th in enumerate(thetas):
        d = abs(th - target)
        if best_d is None or d < best_d - 1e-15 or (abs(d - best_d) <= 1e-15 and i < best_i):
            best_d = d
            best_i = i
    return best_i


def columns(thetas, phi, s):
    cols = []
    for th in thetas:
        info, p_d, loss = pack(th, phi)
        cols.append((info + s * loss, p_d, info, loss))
    return cols


def rationalizing(cols, k):
    """Crossing interval of action k inside [0, 2]. None if empty."""
    a_k, b_k = cols[k][0], cols[k][1]
    lo, hi = WINDOW_LO, WINDOW_HI
    for j, col in enumerate(cols):
        if j == k:
            continue
        a_j, b_j = col[0], col[1]
        d_b = b_k - b_j
        d_a = a_j - a_k
        if abs(d_b) <= SLOPE_TIE:
            if a_k > a_j + TIE:
                return None
            continue
        cross = d_a / d_b
        if d_b > 0.0:
            hi = min(hi, cross)
        else:
            lo = max(lo, cross)
    if lo > hi + 1e-15:
        return None
    if lo < WINDOW_LO:
        lo = WINDOW_LO
    if hi > WINDOW_HI:
        hi = WINDOW_HI
    if lo > hi:
        return None
    return (lo, hi)


def width_of(interval):
    if interval is None:
        return None
    return interval[1] - interval[0]


def cone_of(kind, theta, phi, s):
    flat = abs(math.cos(phi)) <= 1e-12
    if kind == "coarse":
        return None
    if flat and abs(theta - HALF_PI) <= 1e-12:
        return (0.0, 1.0)
    if flat and abs(theta) <= 1e-12:
        return (1.0, 2.0)
    if flat:
        return (1.0, 1.0)
    if abs(theta - HALF_PI) <= 1e-12:
        return (0.0, min(WINDOW_HI, max(q_eq(phi, s), 0.0)))
    if abs(theta) <= 1e-12:
        return (max(q_ptr(phi, s), 0.0), WINDOW_HI)
    return None


def expected_mark(family):
    if family in ("smooth", "pin", "cap"):
        return "smooth"
    if family == "flat-interior":
        return "tie-point"
    return "corner"


def mark_of(family, theta, phi):
    if family == "coarse":
        return "corner"
    if abs(theta) <= 1e-9 or abs(theta - HALF_PI) <= 1e-9:
        return "corner"
    if abs(math.cos(phi)) <= 1e-12:
        return "tie-point"
    return "smooth"


def build_cells():
    cells = []
    phis = (0.0, PI / 6.0, PI / 3.0)
    stakes = (0.5, 1.0, 2.0)
    for phi in phis:
        for s in stakes:
            for u in (0.3, 0.7):
                cells.append({
                    "family": "smooth",
                    "phi": phi,
                    "s": s,
                    "mode": "target",
                    "target": math.acos(u),
                    "tag": f"u={u:.1f}",
                })
    cells.append({
        "family": "pin",
        "phi": 0.0,
        "s": 2.0,
        "mode": "target",
        "target": 1.075559,
        "tag": "theta=1.075559",
    })
    for d_cap in (0.02, 0.05, 0.08):
        cells.append({
            "family": "cap",
            "phi": 0.0,
            "s": 1.0,
            "mode": "cap",
            "cap": d_cap,
            "tag": f"D={d_cap:.2f}",
        })
    for phi in phis:
        for s in stakes:
            cells.append({
                "family": "equator",
                "phi": phi,
                "s": s,
                "mode": "end",
                "which": "equator",
                "tag": "equator",
            })
    for phi in phis:
        for s in stakes:
            cells.append({
                "family": "pointer",
                "phi": phi,
                "s": s,
                "mode": "end",
                "which": "pointer",
                "tag": "pointer",
            })
    cells.append({
        "family": "flat-equator",
        "phi": HALF_PI,
        "s": 1.0,
        "mode": "end",
        "which": "equator",
        "tag": "flat-equator",
    })
    cells.append({
        "family": "flat-pointer",
        "phi": HALF_PI,
        "s": 1.0,
        "mode": "end",
        "which": "pointer",
        "tag": "flat-pointer",
    })
    cells.append({
        "family": "flat-interior",
        "phi": HALF_PI,
        "s": 1.0,
        "mode": "target",
        "target": PI / 4.0,
        "tag": "flat-interior",
    })
    for th, name in ((0.0, "pointer"), (PI / 4.0, "middle"), (HALF_PI, "equator")):
        cells.append({
            "family": "coarse",
            "phi": 0.0,
            "s": 1.0,
            "mode": "coarse",
            "target": th,
            "tag": name,
        })
    return cells


def install(cell, thetas):
    phi, s = cell["phi"], cell["s"]
    if cell["mode"] == "end":
        return 0 if cell["which"] == "pointer" else len(thetas) - 1
    if cell["mode"] == "coarse":
        # Menu is the three angles themselves; thetas is that menu.
        return nearest_index(thetas, cell["target"])
    if cell["mode"] == "target":
        return nearest_index(thetas, cell["target"])
    # cap
    cols = columns(thetas, phi, s)
    best_i = None
    best_a = None
    for i, col in enumerate(cols):
        if col[1] <= cell["cap"] + TIE:
            if best_a is None or col[0] < best_a - TIE or (abs(col[0] - best_a) <= TIE and i < best_i):
                best_a = col[0]
                best_i = i
    if best_i is None:
        return 0
    return best_i


def scan_interval(cols, k):
    best = {}
    qs = []
    n = int(round(WINDOW_HI / SCAN_STEP))
    costs_k = []
    a_k, b_k = cols[k][0], cols[k][1]
    # Precompute every action's (A, B)
    for i in range(n + 1):
        q = i * SCAN_STEP
        best_c = None
        for col in cols:
            c = col[0] + q * col[1]
            if best_c is None or c < best_c:
                best_c = c
        c_k = a_k + q * b_k
        if c_k <= best_c + TIE:
            qs.append(q)
    if not qs:
        return None
    return (qs[0], qs[-1])


def bin_of(q):
    if q >= WINDOW_HI - 1e-12:
        return N_BINS - 1
    if q < WINDOW_LO:
        q = WINDOW_LO
    x = q / BIN_W
    nearest = round(x)
    if abs(x - nearest) < 1e-9:
        idx = int(nearest)
    else:
        idx = int(math.floor(x))
    if idx < 0:
        return 0
    if idx > N_BINS - 1:
        return N_BINS - 1
    return idx


def add_mass(hist, interval, mass):
    if interval is None or mass == 0.0:
        return
    lo, hi = interval
    span = hi - lo
    if span <= 1e-15:
        hist[bin_of(0.5 * (lo + hi))] += mass
        return
    for i in range(N_BINS):
        a = i * BIN_W
        b = WINDOW_HI if i == N_BINS - 1 else (i + 1) * BIN_W
        inter = min(hi, b) - max(lo, a)
        if inter > 0.0:
            hist[i] += mass * inter / span


def normalize(hist):
    total = sum(hist)
    if total <= 0.0:
        return hist
    return [v / total for v in hist]


def peaks_of(hist):
    found = []
    for i, mass in enumerate(hist):
        if mass < PEAK_MASS:
            continue
        neighbors = []
        if i > 0:
            neighbors.append(hist[i - 1])
            if mass < hist[i - 1]:
                continue
        if i < N_BINS - 1:
            neighbors.append(hist[i + 1])
            if mass < hist[i + 1]:
                continue
        mean_n = sum(neighbors) / len(neighbors)
        if mass + 1e-15 < PEAK_FACTOR * mean_n:
            continue
        found.append(i)
    return found


def dyn_landing(thetas, costs, start):
    i = nearest_index(thetas, start)
    for _ in range(64):
        cands = []
        if i > 0:
            cands.append(i - 1)
        if i + 1 < len(thetas):
            cands.append(i + 1)
        strict = [j for j in cands if costs[j] < costs[i] - TIE]
        if strict:
            strict.sort(key=lambda j: (costs[j], j))
            i = strict[0]
            continue
        ties = [j for j in cands if abs(costs[j] - costs[i]) <= TIE and j < i]
        if ties:
            i = min(ties)
            continue
        break
    return i


def recorded_price(theta, phi, s, index, n):
    if index == n - 1:
        price = q_eq(phi, s)
    elif index == 0:
        price = q_ptr(phi, s)
    else:
        price = lam_at(theta, phi, s)
    return clip(price)


def argmin_index(thetas, phi, s, q):
    best = None
    best_i = 0
    for i, th in enumerate(thetas):
        info, p_d, loss = pack(th, phi)
        val = info + q * p_d + s * loss
        if best is None or val < best - TIE or (abs(val - best) <= TIE and i < best_i):
            best = val
            best_i = i
    return best_i


def corner_values():
    vals = [0.0, 1.0, 2.0]
    for phi in (0.0, PI / 6.0, PI / 3.0, HALF_PI):
        for s in (0.5, 1.0, 2.0):
            vals.append(q_eq(phi, s))
            vals.append(q_ptr(phi, s))
    return vals


def fmt(x):
    if x is None:
        return "empty"
    return f"{x:.6e}"


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    cells = build_cells()

    # G-form
    form_gap = 0.0
    for th in (0.0, 0.5, 1.0, HALF_PI):
        for phi in (0.0, HALF_PI):
            info, p_d, loss = pack(th, phi)
            got = base.functionals("ANT", 0.0, th, phi)
            for key, val in (("I", info), ("P_D", p_d), ("L", loss)):
                form_gap = max(form_gap, abs(got[key] - val))
    rep.add("G-form", form_gap < 1e-9, f"max_gap={form_gap:.3e}")

    # G-cone
    eq = q_eq(0.0, 1.0)
    ptr = q_ptr(0.0, 1.0)
    cone_ok = abs(eq - 0.64) < 1e-15 and abs(ptr - Q_PTR_TARGET) < 1e-9
    rep.add("G-cone", cone_ok, f"q_eq={eq:.12f} q_ptr={ptr:.12f}")

    grids = {n: grid(n) for n in GRIDS}
    coarse_menu = [0.0, PI / 4.0, HALF_PI]
    g33 = grids[33]
    g129 = grids[129]
    g513 = grids[513]

    # Precompute dynamics costs on the 33-grid and the coarse menu, per (phi, s).
    starts = [HALF_PI * (k / 16.0) ** 2 for k in range(17)]

    prepared = []
    for cell in cells:
        phi, s = cell["phi"], cell["s"]
        menu = coarse_menu if cell["family"] == "coarse" else None
        widths = {}
        intervals = {}
        installed = {}
        if menu is None:
            for n in GRIDS:
                thetas = grids[n]
                idx = install(cell, thetas)
                cols = columns(thetas, phi, s)
                interval = rationalizing(cols, idx)
                widths[n] = width_of(interval)
                intervals[n] = interval
                installed[n] = (idx, thetas[idx])
            theta_star = installed[513][1]
            r_use = intervals[513]
        else:
            idx = install(cell, menu)
            cols = columns(menu, phi, s)
            interval = rationalizing(cols, idx)
            widths["coarse"] = width_of(interval)
            r_use = interval
            theta_star = menu[idx]
            installed["coarse"] = (idx, theta_star)
            cols_coarse = cols
        mark = mark_of(cell["family"], theta_star, phi)
        prepared.append({
            "cell": cell,
            "mark": mark,
            "expected": expected_mark(cell["family"]),
            "theta": theta_star,
            "widths": widths,
            "intervals": intervals if menu is None else {"coarse": r_use},
            "r": r_use,
            "cols_coarse": columns(menu, phi, s) if menu is not None else None,
            "coarse_index": install(cell, menu) if menu is not None else None,
        })

    # Dynamics and G-dyn
    split_notes = []
    dyn_points = []  # (price, weight) per cell, weights sum to 1 per cell
    for item in prepared:
        cell = item["cell"]
        phi, s = cell["phi"], cell["s"]
        if cell["family"] == "coarse":
            thetas = coarse_menu
        else:
            thetas = g33
        costs = [columns(thetas, phi, s)[i][0] for i in range(len(thetas))]
        landings = [dyn_landing(thetas, costs, start) for start in starts]
        uniq = sorted(set(landings))
        if len(uniq) > 1:
            split_notes.append(f"{cell['family']}:{cell['tag']}:{uniq}")
        counts = {}
        for idx in landings:
            counts[idx] = counts.get(idx, 0) + 1
        points = []
        for idx, count in counts.items():
            price = recorded_price(thetas[idx], phi, s, idx, len(thetas))
            points.append((price, count / 17.0))
        item["dyn"] = points
        dyn_points.append(points)
    rep.add(
        "G-dyn",
        len(split_notes) == 0,
        f"splits={len(split_notes)}" + ("" if not split_notes else " " + " ".join(split_notes)),
    )

    # P1
    p1_bad = []
    smooth_w = []
    for item in prepared:
        if item["mark"] != "smooth":
            continue
        w = item["widths"]
        if any(w[n] is None for n in GRIDS):
            p1_bad.append((item, "empty"))
            continue
        ok = (
            w[33] <= 1.25 * w[9] + 1e-15
            and w[129] <= 1.25 * w[33] + 1e-15
            and w[513] <= 1.25 * w[129] + 1e-15
            and w[513] <= w[9] / 8.0 + 1e-15
            and w[513] <= FLOOR + 1e-15
        )
        smooth_w.append(w[513])
        if not ok:
            p1_bad.append((item, "shrink"))
    if smooth_w:
        max_w = max(smooth_w)
        detail = f"smooth={len(smooth_w)} bad={len(p1_bad)} max_w513={max_w:.6e}"
    else:
        detail = f"smooth=0 bad={len(p1_bad)}"
    if p1_bad:
        bits = []
        for item, why in p1_bad[:6]:
            c = item["cell"]
            ww = item["widths"]
            bits.append(
                f"{c['family']}:{c['tag']}:{why}:"
                + ",".join(fmt(ww[n]) for n in GRIDS)
            )
        detail += " " + " ".join(bits)
    rep.add("P1", len(p1_bad) == 0 and len(smooth_w) > 0, detail)

    # P2
    smooth_wide = []
    corner_narrow = []
    tie_wide = []
    n_corner = n_tie = n_smooth = 0
    for item in prepared:
        mark = item["mark"]
        w = item["widths"].get(513, item["widths"].get("coarse"))
        if mark == "smooth":
            n_smooth += 1
            if w is None or w >= WIDE:
                smooth_wide.append(item)
        elif mark == "corner":
            n_corner += 1
            if w is None or w < WIDE:
                corner_narrow.append(item)
        elif mark == "tie-point":
            n_tie += 1
            if w is None or w > 1e-6:
                tie_wide.append(item)
    p2_ok = not smooth_wide and not corner_narrow and not tie_wide
    detail = (
        f"smooth={n_smooth} corner={n_corner} tie={n_tie} "
        f"smooth_wide={len(smooth_wide)} corner_narrow={len(corner_narrow)} tie_wide={len(tie_wide)}"
    )
    bits = []
    for item in (smooth_wide + corner_narrow + tie_wide)[:6]:
        c = item["cell"]
        w = item["widths"].get(513, item["widths"].get("coarse"))
        bits.append(f"{c['family']}:{c['tag']}:{item['mark']}:{fmt(w)}")
    if bits:
        detail += " " + " ".join(bits)
    rep.add("P2", p2_ok, detail)

    # P3
    p3_bad = []
    max_gap = 0.0
    for item in prepared:
        cell = item["cell"]
        phi, s = cell["phi"], cell["s"]
        mark = item["mark"]
        if cell["family"] == "coarse":
            scanned = scan_interval(item["cols_coarse"], item["coarse_index"])
            crossing = item["r"]
            if scanned is None or crossing is None:
                gap = 1.0
                item["gap"] = gap
                item["cone"] = crossing
                p3_bad.append(item)
                continue
            gap = max(abs(scanned[0] - crossing[0]), abs(scanned[1] - crossing[1]))
            item["gap"] = gap
            item["cone"] = crossing
            item["scan"] = scanned
            max_gap = max(max_gap, gap)
            if gap > TOL_MATCH:
                p3_bad.append(item)
            continue
        r_use = item["r"]
        theta = item["theta"]
        if mark == "smooth":
            if r_use is None:
                item["gap"] = 1.0
                item["cone"] = None
                p3_bad.append(item)
                continue
            mid = 0.5 * (r_use[0] + r_use[1])
            target = lam_at(theta, phi, s)
            gap = abs(mid - target)
            item["gap"] = gap
            item["cone"] = (target, target)
            item["target"] = target
            max_gap = max(max_gap, gap)
            if gap > TOL_MATCH:
                p3_bad.append(item)
            continue
        if mark == "tie-point":
            target_iv = (1.0, 1.0)
        else:
            target_iv = cone_of("interval", theta, phi, s)
        item["cone"] = target_iv
        if r_use is None or target_iv is None:
            item["gap"] = 1.0
            p3_bad.append(item)
            continue
        if mark == "tie-point":
            mid = 0.5 * (r_use[0] + r_use[1])
            gap = abs(mid - 1.0)
            item["gap"] = gap
            max_gap = max(max_gap, gap)
            if gap > 1e-6:
                p3_bad.append(item)
            continue
        gap = max(abs(r_use[0] - target_iv[0]), abs(r_use[1] - target_iv[1]))
        item["gap"] = gap
        max_gap = max(max_gap, gap)
        if gap > TOL_MATCH:
            p3_bad.append(item)
    detail = f"bad={len(p3_bad)} max_gap={max_gap:.6e}"
    if p3_bad:
        bits = []
        for item in p3_bad[:6]:
            c = item["cell"]
            bits.append(f"{c['family']}:{c['tag']}:gap={item['gap']:.6e}")
        detail += " " + " ".join(bits)
    rep.add("P3", len(p3_bad) == 0, detail)

    # P4 histograms
    hist_a = [0.0] * N_BINS
    for item in prepared:
        add_mass(hist_a, item["r"], 1.0)
    hist_a = normalize(hist_a)

    hist_b = [0.0] * N_BINS
    for points in dyn_points:
        for price, weight in points:
            hist_b[bin_of(price)] += weight
    hist_b = normalize(hist_b)

    probes = [2.0 * (i / 20.0) ** 2 for i in range(21)]
    voronoi = []
    for i, q in enumerate(probes):
        if i == 0:
            voronoi.append(probes[1] - probes[0])
        elif i == len(probes) - 1:
            voronoi.append(probes[-1] - probes[-2])
        else:
            voronoi.append(0.5 * (probes[i + 1] - probes[i - 1]))
    # survival per (phi, s)
    pair_keys = []
    survival = {}
    for item in prepared:
        key = (round(item["cell"]["phi"], 12), item["cell"]["s"])
        if key in survival:
            continue
        pair_keys.append(key)
        phi, s = item["cell"]["phi"], item["cell"]["s"]
        row = []
        for q in probes:
            ref = argmin_index(g129, phi, s, q)
            live = 0
            for d_phi in (-0.05, 0.0, 0.05):
                phi2 = min(HALF_PI, max(0.0, phi + d_phi))
                for d_s in (-0.1, 0.0, 0.1):
                    s2 = s + d_s
                    got = argmin_index(g129, phi2, s2, q)
                    if abs(got - ref) <= 2:
                        live += 1
            row.append(live / 9.0)
        survival[key] = row
    hist_c = [0.0] * N_BINS
    for item in prepared:
        key = (round(item["cell"]["phi"], 12), item["cell"]["s"])
        row = survival[key]
        for q, v_w, surv in zip(probes, voronoi, row):
            hist_c[bin_of(q)] += v_w * surv
    hist_c = normalize(hist_c)

    schemes = (("P4a", hist_a), ("P4b", hist_b), ("P4c", hist_c))
    peak_sets = {}
    for name, hist in schemes:
        found = peaks_of(hist)
        peak_sets[name] = found
        conc = "CONCENTRATED" if max(hist) >= CONC_MASS else "DIFFUSE"
        ok = 1 <= len(found) <= 4
        bits = ",".join(f"{i}:{hist[i]:.6f}" for i in found) if found else "none"
        rep.add(name, ok, f"peaks={len(found)} bins={bits} {conc} max={max(hist):.6f}")

    s_a, s_b, s_c = peak_sets["P4a"], peak_sets["P4b"], peak_sets["P4c"]
    medians = []
    for i in s_a:
        for j in s_b:
            for k in s_c:
                if max(i, j, k) - min(i, j, k) <= 1:
                    trip = sorted((i, j, k))
                    medians.append(trip[1])
    agreed = sorted(set(medians))
    rep.add(
        "P4-agree",
        len(agreed) >= 1,
        f"n={len(agreed)} medians={agreed if agreed else 'none'}",
    )

    corners = corner_values()
    corner_bad = []
    if not agreed:
        corner_ok = False
        corner_detail = "no agreed peak"
    else:
        corner_ok = True
        bits = []
        for med in agreed:
            center = med * BIN_W + 0.04
            dist = min(abs(center - v) for v in corners)
            bits.append(f"{med}:{center:.4f}:d={dist:.4f}")
            if dist > 0.08 + 1e-12:
                corner_ok = False
                corner_bad.append(med)
        corner_detail = " ".join(bits)
    rep.add("P4-corner", corner_ok, corner_detail)

    # Reclass notes, printed and not a named check.
    re_n = 0
    for item in prepared:
        if item["mark"] != item["expected"]:
            re_n += 1
            c = item["cell"]
            rep.lines.append(
                f"NOTE reclass {c['family']} {c['tag']} expected={item['expected']} mark={item['mark']}"
            )
    rep.lines.append(f"NOTE reclass_count={re_n}")

    for name, hist in schemes:
        rep.lines.append(name.replace("P4", "HIST") + " " + " ".join(f"{v:.6f}" for v in hist))

    for item in prepared:
        c = item["cell"]
        w = item["widths"]
        if "coarse" in w:
            wtxt = f"w={fmt(w['coarse'])}"
        else:
            wtxt = "w=" + ",".join(fmt(w[n]) for n in GRIDS)
        r_use = item["r"]
        cone = item.get("cone")
        rtxt = "empty" if r_use is None else f"{r_use[0]:.6e},{r_use[1]:.6e}"
        ctxt = "empty" if cone is None else f"{cone[0]:.6e},{cone[1]:.6e}"
        rep.lines.append(
            f"CELL {c['family']} {c['tag']} phi={c['phi']:.6e} s={c['s']:.1f} "
            f"mark={item['mark']} theta={item['theta']:.6e} {wtxt} "
            f"R={rtxt} cone={ctxt} gap={item.get('gap', float('nan')):.6e}"
        )

    rep.dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
