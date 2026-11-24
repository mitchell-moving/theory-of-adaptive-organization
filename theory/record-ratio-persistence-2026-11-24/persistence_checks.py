#!/usr/bin/env python3
"""T78 persistence checks. Criteria are PREREG.md.
The preregistration is not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, "..", "record_ratio_reframes_checks"))
if REF not in sys.path:
    sys.path.insert(0, REF)

import fixed_point_checks as fpc
import record_ratio_reframes_checks as base

SEED = 20261124  # not drawn from
TIE = 1e-9
FLAT = 1e-9
MARGIN = 1e-4
GENS = 100000
WEIGHT_BAR = 0.999
GAP_QUAL = 1e-3
Q = (0.0, 0.25, 0.5, 0.64, 1.0, 2.0)
ALPHAS = (0.5, 1.0)
RHOS = (0.5, 1.0)
REP_W = (1.0, 2.0)
TH2 = (0.0, math.pi / 4.0, base.HALF_PI)


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


def cells():
    out = []
    for phi in (0.0, math.pi / 4.0, base.HALF_PI):
        for w in (1.0, 2.0, 10.0):
            out.append(("ANT", 0.0, phi, w))
    for w in (1.0, 2.0, 10.0):
        out.append(("BIAS", 0.0, 0.0, w))
    out.append(("ANT", 0.5, 0.0, 1.0))
    return out


def phi_tag(phi):
    if abs(phi) < 1e-15:
        return "0"
    if abs(phi - math.pi / 4.0) < 1e-12:
        return "pi/4"
    if abs(phi - base.HALF_PI) < 1e-12:
        return "pi/2"
    return f"{phi:.6f}"


def cell_tag(name, gamma, phi, w):
    return f"{name},g={gamma:.1f},phi={phi_tag(phi)},w={w:.0f}"


def rows_for(name, gamma, phi):
    thetas = base.theta_grid()
    rows = []
    for th in thetas:
        f = base.functionals(name, gamma, th, phi)
        rows.append({"th": th, "I": f["I"], "P_D": f["P_D"], "L": f["L"]})
    return rows


def loss_range(rows):
    vals = [r["L"] for r in rows]
    return max(vals) - min(vals)


def record_range(rows, q):
    vals = [r["I"] + q * r["P_D"] for r in rows]
    return max(vals) - min(vals)


def install(rows, q, w, score):
    """score(row) -> float. Returns the policy record from PREREG §2.3."""
    charged = [r["I"] + q * r["P_D"] + w * r["L"] for r in rows]
    jmin = min(charged)
    tied = [r for r, j in zip(rows, charged) if j <= jmin + TIE]
    scores = [score(r) for r in tied]
    smin = min(scores)
    smax = max(scores)
    if smax - smin < FLAT:
        chosen = min(tied, key=lambda r: r["th"])
        return {
            "score": smin,
            "theta": chosen["th"],
            "P_D": chosen["P_D"],
            "I": chosen["I"],
            "L": chosen["L"],
        }
    best = [r for r, s in zip(tied, scores) if s <= smin + TIE]
    chosen = min(best, key=lambda r: r["th"])
    return {
        "score": smin,
        "theta": chosen["th"],
        "P_D": chosen["P_D"],
        "I": chosen["I"],
        "L": chosen["L"],
    }


def selected(costs):
    best = min(costs.values())
    return {q for q, c in costs.items() if c <= best + TIE}


def fmt_set(qs):
    return "{" + ",".join(f"{q:.2f}" for q in sorted(qs)) + "}"


def g0(rep, cache):
    thetas = base.theta_grid()
    gap = 0.0
    for phi in (0.0, base.HALF_PI):
        for th in thetas:
            f = base.functionals("ANT", 0.0, th, phi)
            ci, cd, cl = base.closed_form_ant(th, phi)
            gap = max(gap, abs(f["I"] - ci), abs(f["P_D"] - cd), abs(f["L"] - cl))
    ant = cache[("ANT", 0.0, 0.0)]
    half = cache[("ANT", 0.0, base.HALF_PI)]
    bias = cache[("BIAS", 0.0, 0.0)]
    l_flat = loss_range(half)
    l_curve = loss_range(ant)
    led_ant = record_range(ant, 1.0)
    led_bias = record_range(bias, 1.0)

    def quot(phi, theta, central):
        step = 1e-4
        if central:
            fp = base.functionals("ANT", 0.0, theta + step, phi)
            fm = base.functionals("ANT", 0.0, theta - step, phi)
            scale = 2.0 * step
        else:
            fp = base.functionals("ANT", 0.0, theta, phi)
            fm = base.functionals("ANT", 0.0, theta - step, phi)
            scale = step
        d_i = (fp["I"] - fm["I"]) / scale
        d_l = (fp["L"] - fm["L"]) / scale
        d_p = (fp["P_D"] - fm["P_D"]) / scale
        return -(d_i + 1.0 * d_l) / d_p

    p64 = quot(0.0, base.HALF_PI - 1e-3, False)
    p1 = quot(base.HALF_PI, 1.0, True)
    ok = (
        gap < 1e-9
        and l_flat < 1e-12
        and l_curve > 0.02
        and led_ant < 1e-9
        and led_bias > 0.02
        and abs(p64 - 0.64) < 0.01
        and abs(p1 - 1.0) < 1e-6
    )
    rep.add(
        "G0",
        ok,
        f"closed={gap:.3e} Lflat={l_flat:.3e} Lcurve={l_curve:.6f} "
        f"ledANT={led_ant:.3e} ledBIAS={led_bias:.6f} "
        f"q64={p64:.12f} q1={p1:.12f}",
    )


def policies(rows, w, score):
    return {q: install(rows, q, w, score) for q in Q}


def base_score(rows, w):
    return policies(rows, w, lambda r: r["I"] + w * r["L"])


def finite_support(costs):
    m = min(costs.values())
    weights = {}
    for q, c in costs.items():
        gap = c - m
        if gap > 1.0:
            weights[q] = 0.0
        else:
            weights[q] = math.exp(-GENS * gap)
    z = sum(weights.values())
    xs = {q: (w / z if z > 0.0 else 0.0) for q, w in weights.items()}
    xmax = max(xs.values())
    return {q for q, x in xs.items() if x >= WEIGHT_BAR * xmax}


def p1_p2_base(rep, cache):
    worst = 0.0
    worst_cell = ""
    misses = []
    dyn_bad = []
    skips = 0
    base_records = []
    for name, gamma, phi, w in cells():
        rows = cache[(name, gamma, phi)]
        pol = base_score(rows, w)
        costs = {q: pol[q]["score"] for q in Q}
        gap = min(costs[q] - costs[0.0] for q in Q if q > 0.0)
        if gap < worst:
            worst = gap
            worst_cell = cell_tag(name, gamma, phi, w)
        if gap < -MARGIN:
            qbest = min((q for q in Q if q > 0.0), key=lambda q: (costs[q], q))
            misses.append(
                f"{cell_tag(name, gamma, phi, w)} q={qbest:.2f} "
                f"th0={pol[0.0]['theta']:.6f} thq={pol[qbest]['theta']:.6f} "
                f"C0={costs[0.0]:.6f} Cq={costs[qbest]:.6f} "
                f"PD0={pol[0.0]['P_D']:.6e} PDq={pol[qbest]['P_D']:.6e} "
                f"gap={costs[0.0] - costs[qbest]:.6e}"
            )
        supp = selected(costs)
        outsiders = [costs[q] for q in Q if q not in supp]
        if outsiders:
            spill = min(outsiders) - min(costs.values())
            if spill < GAP_QUAL:
                skips += 1
            else:
                finite = finite_support(costs)
                if finite != supp:
                    dyn_bad.append(
                        f"{cell_tag(name, gamma, phi, w)} "
                        f"exact={fmt_set(supp)} finite={fmt_set(finite)}"
                    )
        else:
            finite = finite_support(costs)
            if finite != supp:
                dyn_bad.append(
                    f"{cell_tag(name, gamma, phi, w)} "
                    f"exact={fmt_set(supp)} finite={fmt_set(finite)}"
                )
        base_records.append((name, gamma, phi, w, rows, pol, costs, supp))
    under = " UNDER-MARGIN" if -MARGIN < worst < 0.0 else ""
    where = f" at={worst_cell}" if worst < 0.0 else ""
    detail = f"worst_gap={worst:.3e}{where}{under}"
    if misses:
        detail += " | " + " || ".join(misses)
    rep.add("P1", not misses, detail)
    rep.add(
        "G-dyn",
        not dyn_bad,
        f"skip_gap={skips}" + ((" | " + " || ".join(dyn_bad)) if dyn_bad else " match"),
    )
    return base_records


def p2_consider(buckets, ties, rows, supp, channel, tag):
    """ties is a two-count list [n_tie, n_tie_nonflat]."""
    pos = [q for q in sorted(supp) if q > 0.0]
    lrange = loss_range(rows)
    if pos and 0.0 in supp:
        ties[0] += 1
        if lrange >= FLAT and any(record_range(rows, q) >= FLAT for q in pos):
            ties[1] += 1
        return
    if 0.0 in supp or not pos:
        return
    for q in pos:
        rrange = record_range(rows, q)
        if lrange >= FLAT and rrange >= FLAT:
            buckets.append(
                f"{tag} {channel} S={fmt_set(supp)} q={q:.2f} "
                f"Lrange={lrange:.6e} Rrange={rrange:.6e}"
            )
            return


def a_restore(rep, cache, p2_misses, ties):
    misses = []
    for alpha in ALPHAS:
        for name, gamma, phi, w in cells():
            rows = cache[(name, gamma, phi)]

            def score(r, alpha=alpha, w=w):
                return r["I"] + alpha * r["P_D"] + w * r["L"]

            pol = policies(rows, w, score)
            costs = {q: pol[q]["score"] for q in Q}
            supp = selected(costs)
            p2_consider(
                p2_misses, ties, rows, supp, f"restore,a={alpha:.1f}", cell_tag(name, gamma, phi, w)
            )
            gap = min(costs[q] - costs[0.0] for q in Q if q > 0.0)
            if gap < -MARGIN:
                qbest = min((q for q in Q if q > 0.0), key=lambda q: (costs[q], q))
                same = abs(pol[0.0]["theta"] - pol[qbest]["theta"]) <= TIE
                tag = "OTHER" if same else "RESTORE"
                misses.append(
                    f"{tag} {cell_tag(name, gamma, phi, w)} a={alpha:.1f} "
                    f"S={fmt_set(supp)} th0={pol[0.0]['theta']:.6f} "
                    f"thq={pol[qbest]['theta']:.6f} "
                    f"PD0={pol[0.0]['P_D']:.6e} PDq={pol[qbest]['P_D']:.6e} "
                    f"C0={costs[0.0]:.6f} Cq={costs[qbest]:.6f} "
                    f"gap={costs[0.0] - costs[qbest]:.6e} q={qbest:.2f}"
                )
    rep.add(
        "A-restore",
        not misses,
        f"n={len(misses)}" + ((" | " + " || ".join(misses)) if misses else " none"),
    )


def a_ruin(rep, cache, p2_misses, ties):
    misses = []
    for rho in RHOS:
        for name, gamma, phi, w in cells():
            rows = cache[(name, gamma, phi)]
            pol = base_score(rows, w)
            pmax = max(r["P_D"] for r in rows)
            ps = {}
            gs = {}
            for q in Q:
                if pmax < 1e-12:
                    p = 0.0
                else:
                    p = min(1.0, rho * pol[q]["P_D"] / pmax)
                ps[q] = p
                if p >= 1.0:
                    gs[q] = 0.0
                else:
                    gs[q] = (1.0 - p) * math.exp(-pol[q]["score"])
            if all(g <= 0.0 for g in gs.values()):
                misses.append(f"ALL-GONE {cell_tag(name, gamma, phi, w)} rho={rho:.1f}")
                continue
            logs = {q: (-math.inf if gs[q] <= 0.0 else math.log(gs[q])) for q in Q}
            best = max(logs.values())
            supp = {q for q, lg in logs.items() if lg >= best - TIE}
            p2_consider(
                p2_misses, ties, rows, supp, f"ruin,rho={rho:.1f}", cell_tag(name, gamma, phi, w)
            )
            qbest = min((q for q in Q if q > 0.0), key=lambda q: (-logs[q], q))
            if gs[0.0] <= 0.0 and gs[qbest] > 0.0:
                over = True
            elif gs[0.0] <= 0.0:
                over = False
            else:
                over = logs[qbest] > logs[0.0] + MARGIN
            if over:
                tag = "RUIN-REMOVE" if ps[0.0] > ps[qbest] else "OTHER"
                g0s = "0" if gs[0.0] <= 0.0 else f"{gs[0.0]:.6e}"
                misses.append(
                    f"{tag} {cell_tag(name, gamma, phi, w)} rho={rho:.1f} "
                    f"S={fmt_set(supp)} th0={pol[0.0]['theta']:.6f} "
                    f"thq={pol[qbest]['theta']:.6f} "
                    f"PD0={pol[0.0]['P_D']:.6e} PDq={pol[qbest]['P_D']:.6e} "
                    f"p0={ps[0.0]:.6f} pq={ps[qbest]:.6f} "
                    f"C0={pol[0.0]['score']:.6f} Cq={pol[qbest]['score']:.6f} "
                    f"g0={g0s} gq={gs[qbest]:.6e} q={qbest:.2f}"
                )
    rep.add(
        "A-ruin",
        not misses,
        f"n={len(misses)}" + ((" | " + " || ".join(misses)) if misses else " none"),
    )


def a_repin(rep):
    misses = []
    imax = 0.0
    for w in REP_W:
        rows = rows_for("ANT", 0.0, 0.0)
        pol = base_score(rows, w)
        costs = {q: pol[q]["score"] for q in Q}
        for q in Q:
            charged = [r["I"] + q * r["P_D"] + w * r["L"] for r in rows]
            jmin = min(charged)
            th1 = min(r["th"] for r, j in zip(rows, charged) if j <= jmin + TIE)
            back = 0.0
            pair = (th1, th1)
            for th2 in TH2:
                info = fpc.second_pinch("ANT", 0.0, th1, th2)["I"]
                if info > back:
                    back = info
                    pair = (th1, th2)
            imax = max(imax, back)
            if back >= 1e-6:
                misses.append(
                    f"REPIN w={w:.0f} q={q:.2f} th={pair[0]:.6f},{pair[1]:.6f} "
                    f"Iback={back:.3e}"
                )
        gap = min(costs[q] - costs[0.0] for q in Q if q > 0.0)
        if gap < -MARGIN:
            misses.append(f"OTHER w={w:.0f} cost_gap={-gap:.3e}")
    rep.add(
        "A-repin",
        not misses,
        f"Iback_max={imax:.3e}" + ((" | " + " || ".join(misses)) if misses else " empty"),
    )


def main():
    os.environ["SEED"] = str(SEED)
    rep = Report()
    cache = {}
    for name, gamma, phi, _w in cells():
        key = (name, gamma, phi)
        if key not in cache:
            cache[key] = rows_for(name, gamma, phi)
    g0(rep, cache)
    _records = p1_p2_base(rep, cache)
    p2_misses = []
    ties = [0, 0]
    for _name, _gamma, _phi, _w, rows, _pol, _costs, supp in _records:
        p2_consider(p2_misses, ties, rows, supp, "base", cell_tag(_name, _gamma, _phi, _w))
    a_restore(rep, cache, p2_misses, ties)
    a_ruin(rep, cache, p2_misses, ties)
    rep.add(
        "P2",
        not p2_misses,
        f"ties={ties[0]} ties_nonflat={ties[1]} misses={len(p2_misses)}"
        + ((" | " + " || ".join(p2_misses)) if p2_misses else ""),
    )
    a_repin(rep)
    # P2 was appended after the adversarial lines because those lines fill p2_misses.
    # Named checks stay one line each. Order is not a criterion. Reorder to the
    # prereg order for the stored stdout: G0 P1 P2 A-restore A-ruin A-repin G-dyn.
    order = ["G0", "P1", "P2", "A-restore", "A-ruin", "A-repin", "G-dyn"]
    by = {}
    for line in rep.lines:
        by[line.split()[0]] = line
    rep.lines = [by[name] for name in order]
    rep.dump()


if __name__ == "__main__":
    main()
