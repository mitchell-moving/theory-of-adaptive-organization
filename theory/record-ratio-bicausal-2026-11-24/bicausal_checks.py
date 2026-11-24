#!/usr/bin/env python3
"""T79 checks. Criteria are PREREG.md and PREREG_3.md.
The preregistrations are not read for numbers that could be edited into a pass.
SEED is set and not drawn from.
"""
from __future__ import annotations

import math
import os
import sys

SEED = 20261124  # not drawn from
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "theory", "record_ratio_reframes_checks"))
from record_ratio_reframes_checks import functionals  # noqa: E402

PI = math.pi
HALF_PI = 0.5 * PI
N_TH = 720
TIE = 1e-9
EPS0 = 1e-6
DT = 0.05
N_STEP = 20
TAU_GRID = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0)
W_GRID = (1.0, 2.0, 10.0)
SCALE = ((1.0, 1.0, 1.0), (2.0, 1.0, 1.0), (1.0, 2.0, 2.0), (2.0, 2.0, 2.0))
STARTS = ((0, 0), (N_TH, 50), (N_TH // 2, 10))
PATH_STARTS = (
    (0.80, 0.15, 0.05),
    (0.05, 0.20, 0.75),
    (0.50, 0.40, 0.10),
)


def theta_of(j: int) -> float:
    return j * HALF_PI / N_TH


def alpha_of(k: int) -> float:
    return k / 50.0


def q_of(i: int) -> float:
    return i / 50.0


def hbin(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    q = 1.0 - p
    return -p * math.log(p) - q * math.log(q)


def u_alpha(a: float) -> float:
    c = 0.5 * (1.0 - a)
    return 1.0 - hbin(c) / math.log(2.0)


def rho_of(accounting: str, tau: float) -> float:
    if accounting == "lineage":
        return 1.0
    return max(1.0 - tau, 0.0)


def load(name: str):
    rows = []
    for j in range(N_TH + 1):
        f = functionals(name, 0.0, theta_of(j), 0.0)
        rows.append((f["I"], f["P_D"], f["L"]))
    return rows


def solve3(M, b):
    A = [list(row) + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        piv = max(range(col, 3), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        pivv = A[col][col]
        if abs(pivv) < 1e-18:
            raise ZeroDivisionError("singular chain")
        for r in range(col + 1, 3):
            f = A[r][col] / pivv
            for c in range(col, 4):
                A[r][c] -= f * A[col][c]
    x = [0.0, 0.0, 0.0]
    for i in range(2, -1, -1):
        acc = A[i][3]
        for c in range(i + 1, 3):
            acc -= A[i][c] * x[c]
        x[i] = acc / A[i][i]
    return x


class Menu:
    def __init__(self, rows):
        self.I = [r[0] for r in rows]
        self.P = [r[1] for r in rows]
        self.L = [r[2] for r in rows]
        self.n = len(rows)

    def scaled(self, factor: float) -> "Menu":
        f = factor
        return Menu([(self.I[j] * f, self.P[j] * f, self.L[j] * f) for j in range(self.n)])


def child_table(menu: Menu, beta: float, kc: float, wc: float, tie: str) -> int:
    best = None
    vals = []
    for j in range(menu.n):
        c = kc * menu.I[j] + kc * beta * menu.P[j] + wc * menu.L[j]
        vals.append(c)
        if best is None or c < best:
            best = c
    tied = [j for j, c in enumerate(vals) if c <= best + TIE]
    return tied[0] if tie == "small" else tied[-1]


def parent_table(menu: Menu, j: int, kp: float, kd: float, wp: float, tie: str) -> int:
    pd = menu.P[j]
    info = menu.I[j]
    loss = menu.L[j]
    best = None
    vals = []
    for k in range(51):
        a = alpha_of(k)
        c = kp * info + kp * u_alpha(a) * pd + kd * (1.0 - a) * pd + wp * loss
        vals.append(c)
        if best is None or c < best:
            best = c
    tied = [k for k, c in enumerate(vals) if c <= best + TIE]
    return tied[0] if tie == "small" else tied[-1]


def maps(menu, rho, kc, wc, kp, kd, wp, tie):
    child = []
    for k in range(51):
        child.append(child_table(menu, alpha_of(k) * rho, kc, wc, tie))
    parent = [parent_table(menu, j, kp, kd, wp, tie) for j in range(menu.n)]
    return child, parent


def nash_pairs(child, parent):
    out = []
    for k in range(51):
        j = child[k]
        if parent[j] == k:
            out.append((j, k))
    return out


def stackelberg(menu, child, kp, kd, wp, tie):
    best = None
    vals = []
    for k in range(51):
        j = child[k]
        a = alpha_of(k)
        pd = menu.P[j]
        c = kp * menu.I[j] + kp * u_alpha(a) * pd + kd * (1.0 - a) * pd + wp * menu.L[j]
        vals.append(c)
        if best is None or c < best:
            best = c
    tied = [k for k, c in enumerate(vals) if c <= best + TIE]
    return tied[0] if tie == "small" else tied[-1]


def rationalizing(menu, j_star, wc, kc):
    stake = wc / kc
    hit = []
    for i in range(101):
        q = q_of(i)
        best = None
        vals = []
        for j in range(menu.n):
            c = menu.I[j] + q * menu.P[j] + stake * menu.L[j]
            vals.append(c)
            if best is None or c < best:
                best = c
        if vals[j_star] <= best + TIE:
            hit.append(q)
    return hit


def summarize_q(alphas, qs):
    if not alphas:
        return {
            "n": 0,
            "unique_a": False,
            "pinned": False,
            "unbounded": False,
            "qhat": None,
            "qlo": None,
            "qhi": None,
            "alpha": None,
            "width": None,
        }
    uniq = sorted(set(alphas))
    unbounded = (1.98 in qs or abs(qs[-1] - 2.0) < 1e-12) and any(abs(q - 1.98) < 1e-12 for q in qs) and any(abs(q - 2.0) < 1e-12 for q in qs)
    # exact grid: 99/50 = 1.98, 100/50 = 2
    unbounded = (99 / 50.0 in [round(q, 10) for q in qs]) and (2.0 in [round(q, 10) for q in qs])
    width = qs[-1] - qs[0] if qs else None
    pinned = len(uniq) == 1 and bool(qs) and not unbounded and width <= 0.02 + 1e-12
    qhat = 0.5 * (qs[0] + qs[-1]) if qs else None
    return {
        "n": len(uniq),
        "unique_a": len(uniq) == 1,
        "pinned": pinned,
        "unbounded": unbounded,
        "qhat": qhat,
        "qlo": qs[0] if qs else None,
        "qhi": qs[-1] if qs else None,
        "alpha": uniq[0] if len(uniq) == 1 else None,
        "width": width,
        "alphas": uniq,
    }


def iterate(child, parent):
    """Return (fixed_points, cycles, uncapped)."""
    fixed = []
    cycles = []
    uncapped = 0
    for j0, k0 in STARTS:
        seen = []
        index = {}
        j, k = j0, k0
        hit = None
        for _ in range(200):
            key = (j, k)
            if key in index:
                hit = seen[index[key]:]
                break
            index[key] = len(seen)
            seen.append(key)
            j = child[k]
            k = parent[j]
        if hit is None:
            uncapped += 1
            continue
        if len(hit) == 1:
            fixed.append(hit[0])
        else:
            cycles.append(hit)
    return fixed, cycles, uncapped


def costs_at(menu, j, k, rho, kc, wc, kp, kd, wp):
    a = alpha_of(k)
    beta = a * rho
    cc = kc * menu.I[j] + kc * beta * menu.P[j] + wc * menu.L[j]
    jp = kp * menu.I[j] + kp * u_alpha(a) * menu.P[j] + kd * (1.0 - a) * menu.P[j] + wp * menu.L[j]
    return cc, jp


def chain_rates(info, pd, alpha, rho):
    k = [[0.0] * 3 for _ in range(3)]
    k[0][1] = info + EPS0
    k[1][0] = 1.0
    k[1][2] = pd + EPS0
    k[2][1] = alpha * rho * (pd + EPS0) + EPS0
    k[2][0] = 1.0
    k[0][2] = EPS0
    return k


def stationary(k):
    Q = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        s = 0.0
        for j in range(3):
            if i != j:
                Q[i][j] = k[i][j]
                s += k[i][j]
        Q[i][i] = -s
    M = [[Q[i][j] for i in range(3)] for j in range(3)]
    M[2] = [1.0, 1.0, 1.0]
    return solve3(M, [0.0, 0.0, 1.0])


def sigma_steady(k, pi):
    acc = 0.0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            acc += pi[i] * k[i][j] * math.log(k[i][j] / k[j][i])
    return acc


def sigma_path(k, p0):
    P = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        leave = 0.0
        for j in range(3):
            if i != j:
                P[i][j] = DT * k[i][j]
                leave += k[i][j]
        P[i][i] = 1.0 - DT * leave
        if P[i][i] <= 0.0:
            raise RuntimeError("skeleton step left the simplex")
    acc = 0.0
    p = list(p0)
    h0 = sum(-x * math.log(x) for x in p0 if x > 0.0)
    for _ in range(N_STEP):
        for i in range(3):
            for j in range(3):
                if i == j or p[i] <= 0.0:
                    continue
                acc += p[i] * P[i][j] * math.log(P[i][j] / P[j][i])
        nxt = [0.0, 0.0, 0.0]
        for i in range(3):
            for j in range(3):
                nxt[j] += p[i] * P[i][j]
        p = nxt
    hn = sum(-x * math.log(x) for x in p if x > 0.0)
    return acc + (hn - h0)


def fmt(x):
    if x is None:
        return "NA"
    return "%.6f" % x


def cell_key(acc, tau, w, kc, kp, kd, tie):
    return (acc, tau, w, kc, kp, kd, tie)


def run_cell(menu, acc, tau, wc, wp, kc, kp, kd, tie):
    rho = rho_of(acc, tau)
    child, parent = maps(menu, rho, kc, wc, kp, kd, wp, tie)
    pairs = nash_pairs(child, parent)
    stag = stackelberg(menu, child, kp, kd, wp, tie)
    fixed, cycles, uncapped = iterate(child, parent)
    # Rationalizing set of each Nash angle. Headline uses the first pair's
    # angle when several share one alpha; all pairs are kept for sigma.
    reports = []
    for j, k in pairs:
        qs = rationalizing(menu, j, wc, kc)
        sm = summarize_q([alpha_of(k)], qs)
        cc, jp = costs_at(menu, j, k, rho, kc, wc, kp, kd, wp)
        reports.append({
            "j": j,
            "k": k,
            "theta": theta_of(j),
            "alpha": alpha_of(k),
            "beta": alpha_of(k) * rho,
            "pd": menu.P[j],
            "info": menu.I[j],
            "q": qs,
            "sm": sm,
            "cc": cc,
            "jp": jp,
        })
    alphas = [r["alpha"] for r in reports]
    # One cell-level summary uses the tie-consistent set of alphas.
    # q is pinned only when the alpha is unique; the set R is that unique pair's.
    if len(reports) == 1:
        sm = reports[0]["sm"]
    elif len(reports) == 0:
        sm = summarize_q([], [])
    else:
        sm = summarize_q(alphas, reports[0]["q"])
        sm["pinned"] = False
        sm["unique_a"] = False
    return {
        "rho": rho,
        "pairs": reports,
        "stag": alpha_of(stag),
        "stag_j": child[stag],
        "fixed": fixed,
        "cycles": len(cycles),
        "cycle_list": cycles,
        "uncapped": uncapped,
        "sm": sm,
        "child": child,
        "parent": parent,
    }


def main():
    ant = Menu(load("ANT"))
    bias = Menu(load("BIAS"))
    lines = []
    fails = []

    def add(name, ok, detail):
        lines.append("%s %s %s" % (name, "PASS" if ok else "FAIL", detail))
        if not ok:
            fails.append(name)

    # G-parent
    j_eq = N_TH
    k_full = parent_table(ant, j_eq, 1.0, 1.0, 1.0, "small")
    k_zero = parent_table(ant, j_eq, 1.0, 0.0, 1.0, "small")
    g_parent = abs(alpha_of(k_full) - 0.6) <= 0.02 + 1e-12 and k_zero == 0
    add("G-parent", g_parent, "full=%s zero=%s pd=%.6e" % (fmt(alpha_of(k_full)), fmt(alpha_of(k_zero)), ant.P[j_eq]))

    # G-rev
    krev = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i != j:
                krev[i][j] = 1.0
    srev = sigma_steady(krev, stationary(krev))
    add("G-rev", abs(srev) < 1e-12, "sigma=%.3e" % srev)

    cells = []

    def take(menu, acc, tau, wc, wp, kc, kp, kd, tie, family):
        result = run_cell(menu, acc, tau, wc, wp, kc, kp, kd, tie)
        result.update({
            "acc": acc, "tau": tau, "wc": wc, "wp": wp,
            "kc": kc, "kp": kp, "kd": kd, "tie": tie, "family": family,
        })
        cells.append(result)
        return result

    for acc in ("child", "lineage"):
        for tie in ("small", "large"):
            for tau in TAU_GRID:
                for w in W_GRID:
                    take(ant, acc, tau, w, w, 1.0, 1.0, 1.0, tie, "headline")
            for tau in (0.0, 0.25, 2.0):
                for kc, kp, kd in SCALE:
                    take(ant, acc, tau, 1.0, 1.0, kc, kp, kd, tie, "scale")
            for tau in TAU_GRID:
                take(ant, acc, tau, 1.0, 1.0, 1.0, 1.0, 0.0, tie, "nocost")

    # G-iter over headline cells
    bad_iter = []
    for c in cells:
        if c["family"] != "headline":
            continue
        nash_set = {(r["j"], r["k"]) for r in c["pairs"]}
        for j, k in c["fixed"]:
            if (j, k) not in nash_set:
                bad_iter.append((c["acc"], c["tau"], c["wc"], c["tie"], j, k))
    add("G-iter", not bad_iter, "bad=%d" % len(bad_iter))

    def is_head(c):
        return c["family"] == "headline"

    # P1
    p1_bad = [c for c in cells if is_head(c) and not c["sm"]["pinned"]]
    add("P1", not p1_bad, "unpinned=%d of %d" % (len(p1_bad), sum(1 for c in cells if is_head(c))))

    # P2
    p2_bad = []
    pinned_head = [c for c in cells if is_head(c) and c["sm"]["pinned"]]
    for c in cells:
        if not is_head(c):
            continue
        if not c["sm"]["pinned"]:
            p2_bad.append(c)
            continue
        q = c["sm"]["qhat"]
        if not (0.0 < q < 1.0):
            p2_bad.append(c)
    # stake dependence among pinned
    groups = {}
    for c in pinned_head:
        groups.setdefault((c["acc"], c["tau"], c["tie"]), []).append(c)
    for key, group in groups.items():
        qs = [g["sm"]["qhat"] for g in group]
        if max(qs) - min(qs) > 0.02 + 1e-12:
            p2_bad.extend(group)
    add("P2", not p2_bad, "bad=%d pinned=%d" % (len(p2_bad), len(pinned_head)))

    # P3
    p3_bad = []
    for c in cells:
        if not is_head(c):
            continue
        alphas = c["sm"]["alphas"] if c["pairs"] else []
        if len(alphas) == 1 and abs(alphas[0] - c["stag"]) <= 1e-12:
            p3_bad.append(c)
    # empty Nash is not a fail of "they differ"? PREREG: fails if exactly one Nash alpha and Stackelberg equals it.
    # Empty or multiple means the prediction's fail condition is not met, so P3 holds on that cell.
    add("P3", not p3_bad, "same=%d" % len(p3_bad))

    # P4
    p4_bad = []
    scope = [c for c in cells if c["family"] in ("headline", "scale")]
    for c in scope:
        if not c["sm"]["pinned"]:
            p4_bad.append(("unpinned", c))
    buckets = {}
    for c in scope:
        if c["sm"]["pinned"]:
            buckets.setdefault((c["acc"], c["tau"]), []).append(c)
    for key, group in buckets.items():
        qs = [g["sm"]["qhat"] for g in group]
        if max(qs) - min(qs) > 0.02 + 1e-12:
            p4_bad.append(("spread", group[0]))
        if key[1] in (2.0, 4.0):
            for g in group:
                if g["sm"]["qhat"] > 0.02 + 1e-12:
                    p4_bad.append(("slow", g))
        if key[1] == 0.0:
            for g in group:
                if abs(g["sm"]["qhat"] - g["sm"]["alpha"]) > 0.02 + 1e-12:
                    p4_bad.append(("fast", g))
    add("P4", not p4_bad, "bad=%d" % len(p4_bad))

    # sigma cloud
    cloud = []
    for c in cells:
        if c["family"] != "headline":
            continue
        for r in c["pairs"]:
            k = chain_rates(r["info"], r["pd"], r["alpha"], c["rho"])
            pi = stationary(k)
            sig = sigma_steady(k, pi)
            paths = [sigma_path(k, p0) for p0 in PATH_STARTS]
            cloud.append({
                "acc": c["acc"], "tau": c["tau"], "w": c["wc"], "tie": c["tie"],
                "sigma": sig, "paths": paths, "qhat": r["sm"]["qhat"],
                "alpha": r["alpha"], "pinned": r["sm"]["pinned"],
                "cell": (c["acc"], c["tau"], c["wc"], c["tie"]),
            })

    def p5_clauses(points, sig_of):
        reasons = []
        if not points:
            return ["empty"]
        ordered = sorted(points, key=lambda p: (sig_of(p), p["tau"], p["w"], p["tie"]))
        for a, b in zip(ordered, ordered[1:]):
            if abs(sig_of(a) - sig_of(b)) <= 1e-3 and abs(a["qhat"] - b["qhat"]) > 0.02:
                reasons.append("same-sigma")
                break
        for a, b in zip(ordered, ordered[1:]):
            if sig_of(b) > sig_of(a) + 1e-3 and b["qhat"] > a["qhat"] + 0.02:
                reasons.append("not-monotone")
                break
        lo = min(points, key=lambda p: sig_of(p))
        hi = max(points, key=lambda p: sig_of(p))
        if sig_of(lo) > 0.05 or abs(lo["qhat"] - 1.0) > 0.02:
            reasons.append("not-one-at-zero")
        if hi["qhat"] > 0.02:
            reasons.append("not-to-zero")
        for i, a in enumerate(points):
            for b in points[i + 1:]:
                if a["tau"] != b["tau"] and abs(sig_of(a) - sig_of(b)) <= 1e-3 and abs(a["qhat"] - b["qhat"]) > 0.02:
                    reasons.append("tau-left")
                    break
            if "tau-left" in reasons:
                break
        return reasons

    p5_reasons = []
    for acc in ("child", "lineage"):
        pts = [p for p in cloud if p["acc"] == acc]
        p5_reasons.extend(acc + ":" + r for r in p5_clauses(pts, lambda p: p["sigma"]))
        for s_i in range(3):
            path_reasons = p5_clauses(pts, lambda p, s_i=s_i: p["paths"][s_i])
            if "not-monotone" in path_reasons:
                p5_reasons.append("%s:start%d-monotone" % (acc, s_i + 1))
            if pts:
                steady_lo = min(pts, key=lambda p: p["sigma"])["cell"]
                path_lo = min(pts, key=lambda p, s_i=s_i: p["paths"][s_i])["cell"]
                if path_lo != steady_lo:
                    p5_reasons.append("%s:start%d-argmin" % (acc, s_i + 1))
    add("P5", not p5_reasons, "reasons=%s" % (",".join(p5_reasons) if p5_reasons else "none"))

    # Common cause
    def label_share():
        bits = []
        ok = True
        met = True
        for tie in ("small", "large"):
            for wc, wp, target in ((1.0, 1.0, 0.5), (1.0, 2.0, 1.0 / 3.0), (2.0, 1.0, 2.0 / 3.0)):
                c = run_cell(ant, "child", 0.0, wc, wp, 1.0, 1.0, 1.0, tie)
                alphas = sorted({r["alpha"] for r in c["pairs"]})
                if len(alphas) != 1:
                    met = False
                    bits.append("%s-w%s/%s-n%d" % (tie, fmt(wc), fmt(wp), len(alphas)))
                    continue
                gap = abs(alphas[0] - target)
                bits.append("%s-w%s/%s-a%s-t%s" % (tie, fmt(wc), fmt(wp), fmt(alphas[0]), fmt(target)))
                if gap > 0.02:
                    ok = False
        if not met:
            return "NOT-MET", " ".join(bits)
        return ("REPRODUCED" if ok else "CONTRADICTED"), " ".join(bits)

    def label_blanket():
        bits = []
        ok = True
        for tie in ("small", "large"):
            j = child_table(bias, 0.0, 1.0, 1.0, tie)
            full = parent_table(bias, j, 1.0, 1.0, 1.0, tie)
            hidden_rows = [(bias.I[t], 0.0, bias.L[t]) for t in range(bias.n)]
            hidden = Menu(hidden_rows)
            blind = parent_table(hidden, j, 1.0, 1.0, 1.0, tie)
            gap = abs(alpha_of(full) - alpha_of(blind))
            bits.append("%s full=%s blind=%s pd=%.6f" % (tie, fmt(alpha_of(full)), fmt(alpha_of(blind)), bias.P[j]))
            if gap > 0.02:
                ok = False
        return ("REPRODUCED" if ok else "CONTRADICTED"), " ".join(bits)

    def label_copy():
        base = run_cell(ant, "child", 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, "small")
        doubled = ant.scaled(2.0)
        two = run_cell(doubled, "child", 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, "small")
        if not base["pairs"] or not two["pairs"]:
            return "NOT-MET", "empty"
        a1 = sorted(r["alpha"] for r in base["pairs"])
        a2 = sorted(r["alpha"] for r in two["pairs"])
        q1 = base["pairs"][0]["q"] if len(base["pairs"]) == 1 else None
        q2 = two["pairs"][0]["q"] if len(two["pairs"]) == 1 else None
        same_a = a1 == a2
        same_q = q1 == q2
        ratios = []
        if len(base["pairs"]) == len(two["pairs"]):
            for r, s in zip(base["pairs"], two["pairs"]):
                if abs(r["cc"]) > 1e-15:
                    ratios.append(s["cc"] / r["cc"])
                if abs(r["jp"]) > 1e-15:
                    ratios.append(s["jp"] / r["jp"])
        cost_ok = all(abs(v - 2.0) <= 1e-9 * 2.0 for v in ratios) and len(ratios) >= 2
        ok = same_a and same_q and cost_ok
        detail = "alphas=%s q_same=%s cost=%s" % (
            ",".join(fmt(a) for a in a1),
            same_q,
            ",".join("%.12f" % v for v in ratios[:4]),
        )
        return ("REPRODUCED" if ok else "CONTRADICTED"), detail

    def label_bulk():
        base = run_cell(ant, "child", 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, "small")
        # unused slot, multiplied, not read
        bulk = 1.0 * 100.0
        again = run_cell(ant, "child", 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, "small")
        if not base["pairs"]:
            return "NOT-MET", "empty bulk=%s" % fmt(bulk)
        same = [(r["alpha"], r["sm"]["qhat"]) for r in base["pairs"]] == [
            (r["alpha"], r["sm"]["qhat"]) for r in again["pairs"]
        ]
        qhat = base["pairs"][0]["sm"]["qhat"]
        return ("REPRODUCED" if same else "CONTRADICTED"), "qhat=%s abs025=%s bulk=%s" % (
            fmt(qhat), fmt(abs(qhat - 0.25) if qhat is not None else None), fmt(bulk)
        )

    b_lab, b_det = label_blanket()
    s_lab, s_det = label_share()
    f_lab, f_det = label_copy()
    u_lab, u_det = label_bulk()
    lines.append("B-blanket %s %s" % (b_lab, b_det))
    lines.append("S-share %s %s" % (s_lab, s_det))
    lines.append("F-copy %s %s" % (f_lab, f_det))
    lines.append("F-bulk %s %s" % (u_lab, u_det))
    lines.append("H-iface %s %s" % (u_lab, u_det))

    lines.append("FAILS %d" % len(fails))

    nocost = [c for c in cells if c["family"] == "nocost"]
    n_unique0 = n_multi = n_empty = n_zero_in = 0
    for c in nocost:
        alphas = sorted({r["alpha"] for r in c["pairs"]})
        if not alphas:
            n_empty += 1
            continue
        if alphas == [0.0]:
            n_unique0 += 1
        else:
            n_multi += 1
        for r in c["pairs"]:
            if abs(r["alpha"]) < 1e-12 and any(abs(q) < 1e-12 for q in r["q"]):
                n_zero_in += 1
    lines.append(
        "ADV-nocost cells=%d unique0=%d multi=%d empty=%d alpha0_with_0_in_R=%d"
        % (len(nocost), n_unique0, n_multi, n_empty, n_zero_in)
    )
    lines.append("ADV-coupled same-as-headline-w=1")

    # cell dump, stable order already insertion order
    for c in cells:
        alphas = ",".join(fmt(a) for a in (c["sm"]["alphas"] if c["pairs"] else []))
        qh = c["sm"]["qhat"]
        lines.append(
            "CELL %s tau=%s w=%s kc=%s kp=%s kd=%s tie=%s n=%d alphas=%s stag=%s qhat=%s qlo=%s qhi=%s pinned=%d beta=%s"
            % (
                c["acc"], fmt(c["tau"]), fmt(c["wc"]), fmt(c["kc"]), fmt(c["kp"]), fmt(c["kd"]),
                c["tie"], c["sm"]["n"], alphas or "NONE", fmt(c["stag"]), fmt(qh),
                fmt(c["sm"]["qlo"]), fmt(c["sm"]["qhi"]), 1 if c["sm"]["pinned"] else 0,
                fmt(c["pairs"][0]["beta"] if c["pairs"] else None),
            )
        )
        for r in c["pairs"]:
            lines.append(
                "PAIR %s tau=%s w=%s kc=%s kp=%s kd=%s tie=%s theta=%.6f alpha=%s beta=%s qlo=%s qhi=%s qhat=%s pd=%.6e I=%.6e"
                % (
                    c["acc"], fmt(c["tau"]), fmt(c["wc"]), fmt(c["kc"]), fmt(c["kp"]), fmt(c["kd"]),
                    c["tie"], r["theta"], fmt(r["alpha"]), fmt(r["beta"]),
                    fmt(r["sm"]["qlo"]), fmt(r["sm"]["qhi"]), fmt(r["sm"]["qhat"]),
                    r["pd"], r["info"],
                )
            )
        if c["family"] == "headline":
            for cyc in c["cycle_list"]:
                body = ",".join(
                    "%.6f/%.2f" % (theta_of(j), alpha_of(k)) for j, k in cyc
                )
                lines.append(
                    "CYCLE %s tau=%s w=%s tie=%s len=%d %s"
                    % (c["acc"], fmt(c["tau"]), fmt(c["wc"]), c["tie"], len(cyc), body)
                )
    for p in cloud:
        lines.append(
            "P5PT %s tau=%s w=%s tie=%s sigma=%.6e qhat=%s path=%s pinned=%d alpha=%s"
            % (
                p["acc"], fmt(p["tau"]), fmt(p["w"]), p["tie"], p["sigma"], fmt(p["qhat"]),
                ",".join("%.6e" % s for s in p["paths"]), 1 if p["pinned"] else 0, fmt(p["alpha"]),
            )
        )
    # a few witness Nash angles for the memo
    for c in cells:
        if c["family"] == "headline" and c["tie"] == "small" and c["tau"] in (0.0, 0.25, 0.5, 1.0, 2.0):
            if not c["pairs"]:
                lines.append("WITNESS %s tau=%s w=%s EMPTY stag=%s" % (c["acc"], fmt(c["tau"]), fmt(c["wc"]), fmt(c["stag"])))
                continue
            r = c["pairs"][0]
            lines.append(
                "WITNESS %s tau=%s w=%s theta=%.6f alpha=%s beta=%s pd=%.6e I=%.6e qlo=%s qhi=%s qhat=%s pinned=%d stag=%s n=%d cycles=%d"
                % (
                    c["acc"], fmt(c["tau"]), fmt(c["wc"]), r["theta"], fmt(r["alpha"]), fmt(r["beta"]),
                    r["pd"], r["info"], fmt(r["sm"]["qlo"]), fmt(r["sm"]["qhi"]), fmt(r["sm"]["qhat"]),
                    1 if c["sm"]["pinned"] else 0, fmt(c["stag"]), c["sm"]["n"], c["cycles"],
                )
            )

    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
