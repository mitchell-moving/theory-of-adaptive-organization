"""T82e lossless island scan. Criteria are PREREG_T82E.md.

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
BETA_CHECK = 0.25
T_FINAL = 2000.0
H_COARSE = 0.05
H_FINE = 0.025
TOL = 0.002
SEC_TOL = 1e-3
LIB = math.pi
REL = 0.30
GAP = 0.002
LOCKED_HASH = "748514c79a5dd1d3393614207f9c0a814f1a49969da453bdf5af4fe37bbb4421"
ROOT = os.path.dirname(os.path.dirname(HERE))
PREREG = os.path.join(ROOT, "theory", "torus-memory-2026-11-24", "PREREG_T82E.md")
EPSILONS = (0.0, 0.01, 0.04, 0.09)
PRED = {
    0.01: 2.0 * math.sqrt(2.0) * math.sqrt(0.01),
    0.04: 2.0 * math.sqrt(2.0) * math.sqrt(0.04),
    0.09: 2.0 * math.sqrt(2.0) * math.sqrt(0.09),
}


def fmt(x):
    return "%.12f" % x


def hbin(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    q = 1.0 - p
    return -p * math.log(p) - q * math.log(q)


def j_of(theta):
    cabs = abs(math.cos(theta))
    hp = hbin(0.5 * (1.0 + R * cabs))
    hr = hbin(0.5 * (1.0 + R))
    p_d = 0.5 * (hp - hr)
    info = 0.5 * (math.log(2.0) - hp)
    loss = 0.5 * R * R - (R ** 4) * (math.cos(theta) ** 2) / 4.0
    return info + p_d + 2.0 * loss


def rationals():
    out = []
    for q in range(1, 6):
        for p in range(0, 2 * q + 1):
            if math.gcd(p, q) != 1:
                continue
            r = p / float(q)
            if r + 1e-15 < 0.5 or r - 1e-15 > 1.5:
                continue
            out.append((p, q, r))
    return out


RATS = rationals()


def grid_of(lo, hi, step):
    n = int(round((hi - lo) / step))
    return [lo + step * k for k in range(n + 1)]


def orbit(eps, omega2, h):
    n = int(round(T_FINAL / h))
    theta = (0.0, math.pi)
    action = (0.0, 0.0)
    omega = (1.0, omega2)
    psi0 = theta[0] - theta[1]
    j_acc = 0.0
    crosses = []
    for _ in range(n):
        nxt, nxt_a = flow.verlet(theta, action, h, eps, 0.0, omega)
        j_acc += j_of(nxt[1])
        for sample in flow.crossings(theta, action, nxt, nxt_a):
            crosses.append(sample[0])
        theta, action = nxt, nxt_a
    dth1 = theta[0] - 0.0
    nu = (theta[1] - math.pi) / dth1
    psi_net = (theta[0] - theta[1]) - psi0
    librates = abs(psi_net) < LIB
    if len(crosses) < 2:
        nu_sec = None
    else:
        nu_sec = (crosses[-1] - crosses[0]) / ((len(crosses) - 1) * flow.TWOPI)
    other = nu_sec is None or abs(nu - nu_sec) > SEC_TOL
    on = (not other) and abs(nu - 1.0) <= TOL and librates
    return {
        "nu": nu,
        "nu_sec": nu_sec,
        "j": j_acc / float(n),
        "other": other,
        "librates": librates,
        "on": on,
    }


def runs_of(indexes):
    if not indexes:
        return []
    blocks = []
    start = prev = indexes[0]
    for i in indexes[1:]:
        if i == prev + 1:
            prev = i
            continue
        blocks.append((start, prev))
        start = prev = i
    blocks.append((start, prev))
    return blocks


def nearest_label(nu):
    best = None
    for p, q, r in RATS:
        dist = abs(nu - r)
        if dist <= TOL and (best is None or dist < best[0]):
            best = (dist, p, q, r)
    return None if best is None else best[1:]


def width_of(grid, step, lo, hi):
    return (grid[hi] - grid[lo]) + step


def scan(eps, grid, h):
    rows = []
    for omega2 in grid:
        row = orbit(eps, omega2, h)
        row["omega"] = omega2
        rows.append(row)
    return rows


def one_one_plateaus(rows, grid, step):
    idx = [i for i, row in enumerate(rows) if row["on"]]
    blocks = [(lo, hi) for lo, hi in runs_of(idx) if hi - lo + 1 >= 3]
    out = []
    for lo, hi in blocks:
        out.append((lo, hi, width_of(grid, step, lo, hi)))
    return out


def higher_plateaus(rows, grid, step):
    labels = []
    for row in rows:
        lab = nearest_label(row["nu"])
        if lab is None or lab[1] < 2:
            labels.append(None)
        else:
            labels.append(lab)
    blocks = []
    start = None
    for i, lab in enumerate(labels + [None]):
        if start is None:
            if lab is not None:
                start = i
                current = lab
            continue
        if lab == current:
            continue
        hi = i - 1
        if hi - start + 1 >= 3:
            blocks.append((current, start, hi, width_of(grid, step, start, hi)))
        start = i if lab is not None else None
        current = lab
    return blocks


def contains_one(grid, lo, hi):
    for i in range(lo, hi + 1):
        if abs(grid[i] - 1.0) <= 1e-12:
            return True
    return False


def main():
    digest = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    fails = []
    if digest != LOCKED_HASH or abs(flow.BETA - BETA_CHECK) > 0.0:
        print("P0 FAIL hash %s" % digest)
        print("FAILS 1")
        print("SCORED_FAIL P0")
        print("SCOREBOARD COMPLETE")
        return
    print("P0 PASS hash %s" % digest)

    grid = grid_of(0.50, 1.50, 0.005)
    by_eps = {}
    for eps in EPSILONS:
        rows = scan(eps, grid, H_COARSE)
        by_eps[eps] = rows
        near = sum(1 for row in rows if abs(row["nu"] - 1.0) <= TOL)
        print("EPS %s near1 %d" % (fmt(eps), near))
        for lo, hi, width in one_one_plateaus(rows, grid, 0.005):
            print(
                "PLATEAU eps %s kind 1/1 %s %s width %s n %d"
                % (fmt(eps), fmt(grid[lo]), fmt(grid[hi]), fmt(width), hi - lo + 1)
            )
        for lab, lo, hi, width in higher_plateaus(rows, grid, 0.005):
            print(
                "PLATEAU eps %s kind %d/%d %s %s width %s n %d"
                % (fmt(eps), lab[0], lab[1], fmt(grid[lo]), fmt(grid[hi]), fmt(width), hi - lo + 1)
            )

    width_ok = True
    widths = {}
    for eps in (0.01, 0.04, 0.09):
        blocks = one_one_plateaus(by_eps[eps], grid, 0.005)
        holds = len(blocks) == 1 and contains_one(grid, blocks[0][0], blocks[0][1])
        if not holds:
            width_ok = False
            print("P-width-ONE eps %s blocks %d" % (fmt(eps), len(blocks)))
            continue
        meas = blocks[0][2]
        widths[eps] = meas
        rel = abs(meas / PRED[eps] - 1.0)
        if rel > REL:
            width_ok = False
        print(
            "P-width-W eps %s meas %s pred %s signed %s rel %s"
            % (fmt(eps), fmt(meas), fmt(PRED[eps]), fmt(meas - PRED[eps]), fmt(rel))
        )
    print("P-width %s" % ("PASS" if width_ok else "FAIL"))
    if not width_ok:
        fails.append("P-width")

    if 0.01 in widths and 0.04 in widths and widths[0.01] != 0.0:
        ratio = widths[0.04] / widths[0.01]
        scale_ok = 1.4 <= ratio <= 2.6
        print("P-scale %s ratio %s signed %s" % ("PASS" if scale_ok else "FAIL", fmt(ratio), fmt(ratio - 2.0)))
    else:
        scale_ok = False
        print("P-scale FAIL ratio NONE")
    if not scale_ok:
        fails.append("P-scale")

    higher_ok = True
    for eps in (0.01, 0.04, 0.09):
        blocks = higher_plateaus(by_eps[eps], grid, 0.005)
        print("P-higher-N eps %s count %d" % (fmt(eps), len(blocks)))
        if blocks:
            higher_ok = False
    print("P-higher %s" % ("PASS" if higher_ok else "FAIL"))
    if not higher_ok:
        fails.append("P-higher")

    near0 = sum(1 for row in by_eps[0.0] if abs(row["nu"] - 1.0) <= TOL)
    eps0_ok = near0 <= 1
    print("P-eps0 %s count %d signed %d" % ("PASS" if eps0_ok else "FAIL", near0, near0 - 1))
    if not eps0_ok:
        fails.append("P-eps0")

    blocks = one_one_plateaus(by_eps[0.04], grid, 0.005) if 0.04 in by_eps else []
    record_ok = False
    if len(blocks) == 1:
        lo, hi, _w = blocks[0]
        if lo > 0 and hi < len(grid) - 1:
            j_in = None
            for row in by_eps[0.04]:
                if abs(row["omega"] - 1.0) <= 1e-12:
                    j_in = row["j"]
            j_out = 0.5 * (by_eps[0.04][lo - 1]["j"] + by_eps[0.04][hi + 1]["j"])
            gap = abs(j_in - j_out)
            record_ok = gap >= GAP
            print(
                "P-record-J in %s out %s gap %s signed %s"
                % (fmt(j_in), fmt(j_out), fmt(gap), fmt(gap - GAP))
            )
    print("P-record %s" % ("PASS" if record_ok else "FAIL"))
    if not record_ok:
        fails.append("P-record")

    fine_step = 0.0025
    fine_grid = grid_of(0.70, 1.30, fine_step)
    fine_rows = scan(0.04, fine_grid, H_FINE)
    fine_blocks = one_one_plateaus(fine_rows, fine_grid, fine_step)
    for lo, hi, width in fine_blocks:
        print(
            "PLATEAU eps %s kind 1/1-fine %s %s width %s n %d"
            % (fmt(0.04), fmt(fine_grid[lo]), fmt(fine_grid[hi]), fmt(width), hi - lo + 1)
        )
    refine_ok = False
    if len(fine_blocks) == 1 and contains_one(fine_grid, fine_blocks[0][0], fine_blocks[0][1]) and 0.04 in widths:
        fine_w = fine_blocks[0][2]
        rel = abs(fine_w / widths[0.04] - 1.0)
        refine_ok = rel <= REL
        print(
            "P-refine-W fine %s coarse %s signed %s rel %s"
            % (fmt(fine_w), fmt(widths[0.04]), fmt(fine_w - widths[0.04]), fmt(rel))
        )
    print("P-refine %s" % ("PASS" if refine_ok else "FAIL"))
    if not refine_ok:
        fails.append("P-refine")

    print("FAILS %d" % len(fails))
    if fails:
        print("SCORED_FAIL %s" % " ".join(fails))
    else:
        print("SCORED_FAIL none")
    print("SCOREBOARD COMPLETE")


if __name__ == "__main__":
    main()
