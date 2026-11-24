"""T82 coupled flow-ratio loop. Criteria are PREREG_COUPLED.md.

The preregistration is not read for numbers. No random module.
A class other than FIXED is printed and does not change the lock.
"""
from __future__ import annotations

import hashlib
import math
import os

R = 0.6
TIE = 1e-9
PD_EPS = 1e-15
W_MAX = 9
N = 32
TOL = 1e-3
THICK = 0.05
RAT_DEN = 32
TAIL0 = 200
NSTEPS = 400
LYAP_STEPS = 40
LYAP_EPS = 1e-6

LOCKED_HASH = "0ff192a126020f647447a9511386944bcdda6d3de7ef55b0a7b16b2129f9c560"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG_COUPLED.md")

# Horizons and stakes printed by T81. Not recomputed.
CELLS = (
    ("m3-a", 208, 2.0),
    ("m3-b", 415, 2.0),
    ("m3-c", 831, 2.0),
    ("m3-d", 415, 1.0),
    ("m3-e", 21, 2.0),
    ("m3-f", 3323, 2.0),
)
GAINS = ((1.0, 1.0), (0.5, 0.5), (1.5, 0.5), (0.5, 1.5))
INITS = ((1.0, 0.0), (5.0, 0.5), (9.0, 1.0))
E_MID = 0.239059227845
E_FAR = 0.048343059332

OUTSIDE = [0]
OUTSIDE_GAIN = {}


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


def widths_for(w, q, pd_top):
    best = None
    rows = []
    for j in range(181):
        th = j * (math.pi / 2.0) / 180.0
        info, pd, loss = closed_form_ant(th, 0.0)
        cost = info + q * pd + w * loss
        rows.append((cost, pd))
        if best is None or cost < best:
            best = cost
    found = []
    seen = set()
    for cost, pd in rows:
        if cost <= best + TIE:
            width = 1 + math.floor(8.0 * pd / pd_top + PD_EPS)
            if width < 1 or width > W_MAX:
                if width < 1:
                    width = 1
                if width > W_MAX:
                    width = W_MAX
            if width not in seen:
                seen.add(width)
                found.append(width)
    return found


def rate_target(w, q, pd_top):
    ws = widths_for(w, q, pd_top)
    return sum(ws) / len(ws)


def step_mass(p, c, contact):
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
            if contact == "agent":
                agent += 0.25 * mass
        if j < n - 1:
            new[j + 1] += 0.25 * mass
        else:
            new[j] += 0.25 * c * mass
    return new, agent


def return_prob(n, starts, t, c):
    acc = 0.0
    for s in starts:
        p = [0.0] * n
        p[s] = 1.0
        agent = 0.0
        for _ in range(t):
            p, a = step_mass(p, c, "agent")
            agent += a
        acc += agent
    return acc / len(starts)


def block_sites(n, width):
    j0 = n // 2
    raw = list(range(j0 - (width // 2), j0 + (width // 2) + 1))
    return [j for j in raw if 0 <= j < n]


def far_sites(n, width):
    length = len(block_sites(n, width))
    return list(range(n - length, n))


def q_table(starts_of, t):
    table = {}
    for width in range(1, W_MAX + 1):
        table[width] = return_prob(N, starts_of(width), t, 1.0)
    return table


def q_of_rho(table, rho):
    if rho <= 1.0:
        if rho < 1.0:
            OUTSIDE[0] += 1
            OUTSIDE_GAIN["low"] = OUTSIDE_GAIN.get("low", 0) + 1
        return table[1]
    if rho >= 9.0:
        if rho > 9.0:
            OUTSIDE[0] += 1
            OUTSIDE_GAIN["high"] = OUTSIDE_GAIN.get("high", 0) + 1
        return table[9]
    k = int(math.floor(rho))
    f = rho - k
    return (1.0 - f) * table[k] + f * table[k + 1]


def orbit_locked(alpha, beta, rho0, q0, stake, table, pd_top):
    """Both updates read the previous state."""
    rho, q = rho0, q0
    states = []
    for _ in range(NSTEPS):
        target = rate_target(stake, q, pd_top)
        q_ret = q_of_rho(table, rho)
        rho = rho + alpha * (target - rho)
        q = q + beta * (q_ret - q)
        states.append((rho, q))
    return states


def classify(states):
    tail = states[TAIL0:NSTEPS]
    rhos = [s[0] for s in tail]
    qs = [s[1] for s in tail]
    span_r = max(rhos) - min(rhos)
    span_q = max(qs) - min(qs)
    if span_r <= TOL and span_q <= TOL:
        return "FIXED", "range"
    if any(abs(q) > 2.0 or rho < 0.0 or rho > 12.0 for rho, q in tail):
        return "OTHER", "diverge"
    n = len(tail)
    for p in range(2, 33):
        ok = True
        for i in range(n - p):
            dr = tail[i + p][0] - tail[i][0]
            dq = tail[i + p][1] - tail[i][1]
            if math.hypot(dr, dq) > TOL:
                ok = False
                break
        if ok:
            return "CYCLE", "period %d" % p
    cx = sum(rhos) / n
    cy = sum(qs) / n
    radii = [math.hypot(rho - cx, q - cy) for rho, q in tail]
    mean_r = sum(radii) / n
    thick = max(radii) - min(radii)
    if mean_r <= TOL:
        return "OTHER", "drift"
    acc = 0.0
    prev = math.atan2(tail[0][1] - cy, tail[0][0] - cx)
    for rho, q in tail[1:]:
        ang = math.atan2(q - cy, rho - cx)
        d = ang - prev
        while d > math.pi:
            d -= 2.0 * math.pi
        while d <= -math.pi:
            d += 2.0 * math.pi
        acc += d
        prev = ang
    omega = (acc / (n - 1)) / (2.0 * math.pi)
    wmod = omega - math.floor(omega)
    dist = 1.0
    for b in range(1, RAT_DEN + 1):
        for a in range(b + 1):
            gap = abs(wmod - a / b)
            gap = min(gap, 1.0 - gap)
            if gap < dist:
                dist = gap
    thin = thick <= THICK * mean_r
    if thin and dist > TOL:
        return "TORUS", "omega %.6f" % wmod
    if thin and dist <= TOL:
        return "CYCLE", "wind %.6f" % wmod
    return "OTHER", "cloud"


def lyapunov(alpha, beta, rho, q, stake, table, pd_top):
    a = (rho, q)
    b = (rho, q + LYAP_EPS)
    for _ in range(LYAP_STEPS):
        a = one_step(alpha, beta, a[0], a[1], stake, table, pd_top)
        b = one_step(alpha, beta, b[0], b[1], stake, table, pd_top)
    d = math.hypot(a[0] - b[0], a[1] - b[1])
    if d == 0.0:
        return -1e9
    return math.log(d / LYAP_EPS) / LYAP_STEPS


def one_step(alpha, beta, rho, q, stake, table, pd_top):
    target = rate_target(stake, q, pd_top)
    q_ret = q_of_rho(table, rho)
    return rho + alpha * (target - rho), q + beta * (q_ret - q)


def main():
    digest = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    lines = []
    lines.append(
        "P0 %s  prereg sha256 %s"
        % ("PASS" if digest == LOCKED_HASH else "FAIL", digest)
    )
    _info, pd_top, _loss = closed_form_ant(math.pi / 2.0, 0.0)

    tables = {}
    for rule, sites_of in (("mid", block_sites), ("far", far_sites)):
        for _name, t, _w in CELLS:
            key = (rule, t)
            if key not in tables:
                tables[key] = q_table(lambda width, s=sites_of: s(N, width), t)

    qa = tables[("mid", 415)][1]
    qb = tables[("far", 415)][1]
    port_ok = abs(qa - E_MID) <= 1e-9 and abs(qb - E_FAR) <= 1e-9
    lines.append(
        "I-port %s  qa %.12f qb %.12f gaps %.3e %.3e"
        % (
            "PASS" if port_ok else "FAIL",
            qa,
            qb,
            abs(qa - E_MID),
            abs(qb - E_FAR),
        )
    )

    records = []
    for name, t, stake in CELLS:
        for rule in ("mid", "far"):
            table = tables[(rule, t)]
            for alpha, beta in GAINS:
                for rho0, q0 in INITS:
                    states = orbit_locked(alpha, beta, rho0, q0, stake, table, pd_top)
                    kind, tag = classify(states)
                    tail = states[TAIL0:]
                    qmean = sum(s[1] for s in tail) / len(tail)
                    rmean = sum(s[0] for s in tail) / len(tail)
                    lam = lyapunov(alpha, beta, tail[0][0], tail[0][1], stake, table, pd_top)
                    rec = {
                        "cell": name,
                        "rule": rule,
                        "gain": (alpha, beta),
                        "init": (rho0, q0),
                        "kind": kind,
                        "tag": tag,
                        "q": qmean,
                        "rho": rmean,
                        "lyap": lam,
                    }
                    records.append(rec)

    counts = {"FIXED": 0, "CYCLE": 0, "TORUS": 0, "OTHER": 0}
    for rec in records:
        counts[rec["kind"]] += 1
    settle_ok = counts["FIXED"] == len(records) and digest == LOCKED_HASH
    lines.append(
        "H-settle %s  n %d FIXED %d CYCLE %d TORUS %d OTHER %d"
        % (
            "PASS" if settle_ok else "FAIL",
            len(records),
            counts["FIXED"],
            counts["CYCLE"],
            counts["TORUS"],
            counts["OTHER"],
        )
    )

    hist_ok = True
    gaps = []
    for alpha, beta in GAINS:
        for rho0, q0 in INITS:
            pair = [
                rec
                for rec in records
                if rec["cell"] == "m3-b"
                and rec["gain"] == (alpha, beta)
                and rec["init"] == (rho0, q0)
            ]
            mid = next(rec for rec in pair if rec["rule"] == "mid")
            far = next(rec for rec in pair if rec["rule"] == "far")
            gap = abs(mid["q"] - far["q"])
            ok = mid["kind"] == "FIXED" and far["kind"] == "FIXED" and gap > 0.05
            hist_ok = hist_ok and ok
            gaps.append((alpha, beta, rho0, q0, mid["q"], far["q"], gap, mid["kind"], far["kind"], ok))
    lines.append(
        "H-history %s  m3-b pairs %d misses %d"
        % ("PASS" if hist_ok else "FAIL", len(gaps), sum(1 for g in gaps if not g[-1]))
    )

    init_ok = True
    groups = {}
    for rec in records:
        key = (rec["cell"], rec["rule"], rec["gain"])
        groups.setdefault(key, []).append(rec)
    init_miss = 0
    for key, group in groups.items():
        kinds = {rec["kind"] for rec in group}
        qs = [rec["q"] for rec in group]
        bad = len(kinds) != 1 or (kinds == {"FIXED"} and max(qs) - min(qs) > 0.02)
        if bad:
            init_ok = False
            init_miss += 1
    lines.append(
        "H-init %s  groups %d misses %d" % ("PASS" if init_ok else "FAIL", len(groups), init_miss)
    )

    lines.append(
        "CLASS-COUNTS FIXED %d CYCLE %d TORUS %d OTHER %d" % (
            counts["FIXED"], counts["CYCLE"], counts["TORUS"], counts["OTHER"]
        )
    )
    for rec in records:
        if rec["kind"] != "FIXED":
            lines.append(
                "NONFIXED %s %s gain %.1f %.1f init %.1f %.1f %s %s q %.6f rho %.6f lyap %.6f"
                % (
                    rec["cell"],
                    rec["rule"],
                    rec["gain"][0],
                    rec["gain"][1],
                    rec["init"][0],
                    rec["init"][1],
                    rec["kind"],
                    rec["tag"],
                    rec["q"],
                    rec["rho"],
                    rec["lyap"],
                )
            )
    for alpha, beta, rho0, q0, qm, qf, gap, km, kf, ok in gaps:
        lines.append(
            "M3B gain %.1f %.1f init %.1f %.1f qmid %.12f qfar %.12f gap %.12f %s %s %s"
            % (alpha, beta, rho0, q0, qm, qf, gap, km, kf, "PASS" if ok else "FAIL")
        )
    fails = []
    if digest != LOCKED_HASH:
        fails.append("P0")
    if not port_ok:
        fails.append("I-port")
    if not settle_ok:
        fails.append("H-settle")
    if not hist_ok:
        fails.append("H-history")
    if not init_ok:
        fails.append("H-init")
    seen = {}
    disagree = 0
    for rec in records:
        key = (rec["cell"], rec["rule"])
        prev = seen.get(key)
        if prev is None:
            seen[key] = rec
        elif abs(prev["q"] - rec["q"]) > 1e-9 or abs(prev["rho"] - rec["rho"]) > 1e-9 or prev["kind"] != rec["kind"]:
            disagree += 1
    for (cell, rule), rec in seen.items():
        lines.append(
            "FIXED-POINT %s %s %s q %.12f rho %.12f" % (cell, rule, rec["kind"], rec["q"], rec["rho"])
        )
    lines.append("FIXED-POINT-DISAGREE %d" % disagree)
    lines.append(
        "OUTSIDE %d low %d high %d" % (OUTSIDE[0], OUTSIDE_GAIN.get("low", 0), OUTSIDE_GAIN.get("high", 0))
    )
    lines.append("FAILS %d" % len(fails))
    if fails:
        lines.append("SCORED_FAIL " + " ".join(fails))
    lines.append("SCOREBOARD COMPLETE")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
