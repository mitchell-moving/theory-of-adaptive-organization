"""Independent T82e scan.

Integrator is written from the Hamiltonian
H = w1*I1 + w2*I2 + (beta/2)*(I1**2 + I2**2) + eps*cos(theta1-theta2),
beta = 0.25, not imported from the scoreboard. Stormer-Verlet is
kick-drift-kick on those equations. A second scan of the coarse grid uses RK4.
"""
from __future__ import annotations

import math

import numpy as np

BETA = 0.25
TWOPI = 2.0 * math.pi
T_FINAL = 2000.0
TOL = 0.002
SEC_TOL = 1e-3
R = 0.6
PRED = {
    0.01: 2.0 * math.sqrt(2.0) * math.sqrt(0.01),
    0.04: 2.0 * math.sqrt(2.0) * math.sqrt(0.04),
    0.09: 2.0 * math.sqrt(2.0) * math.sqrt(0.09),
}


def fmt(x):
    return "%.12f" % x


def grid_of(lo, hi, step):
    n = int(round((hi - lo) / step))
    return lo + step * np.arange(n + 1, dtype=np.float64)


def hbin(p):
    out = np.zeros_like(p)
    ok = (p > 0.0) & (p < 1.0)
    q = 1.0 - p
    out[ok] = -p[ok] * np.log(p[ok]) - q[ok] * np.log(q[ok])
    return out


def j_of(theta):
    cabs = np.abs(np.cos(theta))
    hp = hbin(0.5 * (1.0 + R * cabs))
    hr = hbin(np.array([0.5 * (1.0 + R)]))[0]
    p_d = 0.5 * (hp - hr)
    info = 0.5 * (math.log(2.0) - hp)
    loss = 0.5 * R * R - (R ** 4) * (np.cos(theta) ** 2) / 4.0
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


def half_width(eps):
    if eps == 0.0:
        return 0.0
    return 2.0 * math.sqrt(2.0 * BETA * eps)


def scan_verlet(eps, omegas, h):
    omegas = np.asarray(omegas, dtype=np.float64)
    n = int(round(T_FINAL / h))
    ngrid = omegas.size
    th1 = np.zeros(ngrid)
    th2 = np.full(ngrid, math.pi)
    i1 = np.zeros(ngrid)
    i2 = np.zeros(ngrid)
    psi0 = th1 - th2
    j_acc = np.zeros(ngrid)
    first = np.full(ngrid, np.nan)
    last = np.full(ngrid, np.nan)
    ncross = np.zeros(ngrid, dtype=np.int32)
    max_dth = 0.0
    for _ in range(n):
        s = np.sin(th1 - th2)
        di1 = eps * s
        di2 = -eps * s
        i1m = i1 + 0.5 * h * di1
        i2m = i2 + 0.5 * h * di2
        th1n = th1 + h * (1.0 + BETA * i1m)
        th2n = th2 + h * (omegas + BETA * i2m)
        s2 = np.sin(th1n - th2n)
        i1n = i1m + 0.5 * h * (eps * s2)
        i2n = i2m + 0.5 * h * (-eps * s2)
        dth = th1n - th1
        max_dth = max(max_dth, float(np.max(np.abs(dth))))
        tau0 = th1 / TWOPI
        tau1 = th1n / TWOPI
        # At this step size the advance is far below 2pi, so at most one integer.
        up = tau1 > tau0
        m = np.where(up, np.floor(tau0) + 1.0, np.ceil(tau0) - 1.0)
        hit = np.where(up, m <= tau1 + 1e-15, m >= tau1 - 1e-15)
        # reject a zero-length step
        span = tau1 - tau0
        hit = hit & (span != 0.0)
        frac = np.zeros(ngrid)
        np.divide(m - tau0, span, out=frac, where=hit)
        th_cross = th2 + frac * (th2n - th2)
        new = hit & (ncross == 0)
        first = np.where(new, th_cross, first)
        last = np.where(hit, th_cross, last)
        ncross = ncross + hit.astype(np.int32)
        th1, th2, i1, i2 = th1n, th2n, i1n, i2n
        j_acc += j_of(th2)
    dth1 = th1 - 0.0
    nu = (th2 - math.pi) / dth1
    psi_net = (th1 - th2) - psi0
    librates = np.abs(psi_net) < math.pi
    nu_sec = np.full(ngrid, np.nan)
    ok = ncross >= 2
    nu_sec[ok] = (last[ok] - first[ok]) / ((ncross[ok] - 1) * TWOPI)
    other = (~ok) | (np.abs(nu - nu_sec) > SEC_TOL)
    on = (~other) & (np.abs(nu - 1.0) <= TOL) & librates
    delta = 1.0 - omegas
    trapped = np.abs(delta) < half_width(eps) - 0.0
    if eps == 0.0:
        trapped = np.zeros(ngrid, dtype=bool)
    return {
        "nu": nu,
        "nu_sec": nu_sec,
        "j": j_acc / float(n),
        "other": other,
        "librates": librates,
        "on": on,
        "trapped": trapped,
        "ncross": ncross,
        "max_dth": max_dth,
        "omega": omegas,
    }


def scan_rk4(eps, omegas, h):
    omegas = np.asarray(omegas, dtype=np.float64)
    n = int(round(T_FINAL / h))
    ngrid = omegas.size
    th1 = np.zeros(ngrid)
    th2 = np.full(ngrid, math.pi)
    i1 = np.zeros(ngrid)
    i2 = np.zeros(ngrid)
    psi0 = th1 - th2

    def deriv(a1, a2, b1, b2):
        s = np.sin(a1 - a2)
        return (
            1.0 + BETA * b1,
            omegas + BETA * b2,
            eps * s,
            -eps * s,
        )

    for _ in range(n):
        k1 = deriv(th1, th2, i1, i2)
        k2 = deriv(
            th1 + 0.5 * h * k1[0],
            th2 + 0.5 * h * k1[1],
            i1 + 0.5 * h * k1[2],
            i2 + 0.5 * h * k1[3],
        )
        k3 = deriv(
            th1 + 0.5 * h * k2[0],
            th2 + 0.5 * h * k2[1],
            i1 + 0.5 * h * k2[2],
            i2 + 0.5 * h * k2[3],
        )
        k4 = deriv(
            th1 + h * k3[0],
            th2 + h * k3[1],
            i1 + h * k3[2],
            i2 + h * k3[3],
        )
        th1 = th1 + (h / 6.0) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        th2 = th2 + (h / 6.0) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        i1 = i1 + (h / 6.0) * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        i2 = i2 + (h / 6.0) * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
    dth1 = th1
    nu = (th2 - math.pi) / dth1
    psi_net = (th1 - th2) - psi0
    librates = np.abs(psi_net) < math.pi
    on_nu = (np.abs(nu - 1.0) <= TOL) & librates
    return nu, librates, on_nu


def runs(mask):
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return []
    blocks = []
    start = prev = int(idx[0])
    for i in idx[1:]:
        i = int(i)
        if i == prev + 1:
            prev = i
            continue
        blocks.append((start, prev))
        start = prev = i
    blocks.append((start, prev))
    return blocks


def plateaus(mask, grid, step, min_len=3):
    out = []
    for lo, hi in runs(mask):
        if hi - lo + 1 >= min_len:
            width = (grid[hi] - grid[lo]) + step
            out.append((lo, hi, width, hi - lo + 1))
    return out


def nearest_label(nu):
    best = None
    for p, q, r in RATS:
        dist = abs(nu - r)
        if dist <= TOL and (best is None or dist < best[0]):
            best = (dist, p, q, r)
    return None if best is None else best[1:]


def higher_plateaus(nu, grid, step):
    labels = []
    for value in nu:
        lab = nearest_label(float(value))
        if lab is None or lab[1] < 2:
            labels.append(None)
        else:
            labels.append(lab)
    blocks = []
    start = None
    current = None
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
            width = (grid[hi] - grid[start]) + step
            blocks.append((current, start, hi, width, hi - start + 1))
        start = i if lab is not None else None
        current = lab
    return blocks


def report_plateaus(tag, rows, grid, step):
    blocks = plateaus(rows["on"], grid, step)
    print("%s plateaus %d" % (tag, len(blocks)))
    for lo, hi, width, n in blocks:
        print(
            "  %s %s width %s n %d"
            % (fmt(grid[lo]), fmt(grid[hi]), fmt(width), n)
        )
    return blocks


def gap_report(rows, grid):
    on = rows["on"]
    trapped = rows["trapped"]
    inside_off = trapped & ~on
    outside_on = on & ~trapped
    print(
        "  trapped %d on %d inside_off %d outside_on %d"
        % (int(trapped.sum()), int(on.sum()), int(inside_off.sum()), int(outside_on.sum()))
    )
    reasons = {"other": 0, "not_lib": 0, "nu": 0, "multi": 0}
    for i in np.flatnonzero(inside_off):
        flags = []
        if rows["other"][i]:
            flags.append("other")
        if not rows["librates"][i]:
            flags.append("not_lib")
        if abs(rows["nu"][i] - 1.0) > TOL:
            flags.append("nu")
        if len(flags) > 1:
            reasons["multi"] += 1
        elif flags:
            reasons[flags[0]] += 1
    print("  inside_off reasons %s" % reasons)
    # contiguous gaps inside the analytical interval
    if trapped.any():
        lo = int(np.flatnonzero(trapped)[0])
        hi = int(np.flatnonzero(trapped)[-1])
        print(
            "  analytical grid span %s %s width %s"
            % (fmt(grid[lo]), fmt(grid[hi]), fmt((grid[hi] - grid[lo]) + (grid[1] - grid[0])))
        )


def record_gap(rows, grid, blocks):
    if len(blocks) != 1:
        print("  record not one plateau")
        # counterfactual on the longest block that contains 1, if any
        holders = [b for b in blocks if any(abs(grid[i] - 1.0) <= 1e-9 for i in range(b[0], b[1] + 1))]
        if not holders:
            print("  no block contains 1")
            return
        lo, hi, width, n = max(holders, key=lambda b: b[3])
    else:
        lo, hi, width, n = blocks[0]
    if lo == 0 or hi == len(grid) - 1:
        print("  record edge")
        return
    center = int(np.argmin(np.abs(grid - 1.0)))
    j_in = rows["j"][center]
    j_out = 0.5 * (rows["j"][lo - 1] + rows["j"][hi + 1])
    gap = abs(j_in - j_out)
    print(
        "  record-like lo %s hi %s jin %s jout %s gap %s signed %s"
        % (fmt(grid[lo]), fmt(grid[hi]), fmt(j_in), fmt(j_out), fmt(gap), fmt(gap - 0.002))
    )


def null_baseline(grid):
    hit = 0
    which = []
    for w in grid:
        best = None
        for p, q, r in RATS:
            d = abs(w - r)
            if d <= TOL and (best is None or d < best[0]):
                best = (d, p, q, r)
        if best is not None:
            hit += 1
            which.append((float(w), best[1], best[2], best[3], best[0]))
    print("NULL rationals %d" % len(RATS))
    for p, q, r in RATS:
        print("  %d/%d %s" % (p, q, fmt(r)))
    print("NULL grid hits %d of %d fraction %s" % (hit, len(grid), fmt(hit / float(len(grid)))))
    for row in which:
        print("  grid %s rational %d/%d dist %s" % (fmt(row[0]), row[1], row[2], fmt(row[4])))


def main():
    print("PRED", {k: fmt(v) for k, v in PRED.items()})
    print("HALF", {k: fmt(half_width(k)) for k in (0.01, 0.04, 0.09)})
    grid = grid_of(0.50, 1.50, 0.005)
    print("GRID n %d first %s last %s step %s" % (len(grid), fmt(grid[0]), fmt(grid[-1]), fmt(grid[1] - grid[0])))
    print("ONE dist %s" % fmt(np.min(np.abs(grid - 1.0))))
    null_baseline(grid)
    by = {}
    for eps in (0.0, 0.01, 0.04, 0.09):
        rows = scan_verlet(eps, grid, 0.05)
        by[eps] = rows
        near = int(np.sum(np.abs(rows["nu"] - 1.0) <= TOL))
        print("EPS %s near1 %d max_dth %s" % (fmt(eps), near, fmt(rows["max_dth"])))
        blocks = report_plateaus("coarse", rows, grid, 0.005)
        higher = higher_plateaus(rows["nu"], grid, 0.005)
        print("  higher %d" % len(higher))
        for lab, lo, hi, width, n in higher:
            print(
                "  HIGHER %d/%d %s %s width %s n %d"
                % (lab[0], lab[1], fmt(grid[lo]), fmt(grid[hi]), fmt(width), n)
            )
        if eps > 0.0:
            gap_report(rows, grid)
            # longest plateau width vs prediction, even if not unique
            if blocks:
                longest = max(blocks, key=lambda b: b[3])
                meas = longest[2]
                print(
                    "  longest width %s pred %s signed %s rel %s"
                    % (fmt(meas), fmt(PRED[eps]), fmt(meas - PRED[eps]), fmt(abs(meas / PRED[eps] - 1.0)))
                )
            if on_blocks := plateaus(rows["on"], grid, 0.005, min_len=1):
                span_lo = on_blocks[0][0]
                span_hi = on_blocks[-1][1]
                span = (grid[span_hi] - grid[span_lo]) + 0.005
                print("  on-span %s %s width %s" % (fmt(grid[span_lo]), fmt(grid[span_hi]), fmt(span)))
        if eps in (0.01, 0.04):
            record_gap(rows, grid, blocks)
        # center sample
        c = int(np.argmin(np.abs(grid - 1.0)))
        print(
            "  center nu %s nu_sec %s lib %s on %s j %s"
            % (
                fmt(rows["nu"][c]),
                fmt(rows["nu_sec"][c]),
                bool(rows["librates"][c]),
                bool(rows["on"][c]),
                fmt(rows["j"][c]),
            )
        )

    # ratio from unique widths only, and from longest
    w01 = plateaus(by[0.01]["on"], grid, 0.005)
    w04 = plateaus(by[0.04]["on"], grid, 0.005)
    if len(w01) == 1 and len(w04) == 1:
        print("SCALE unique %s" % fmt(w04[0][2] / w01[0][2]))
    else:
        print("SCALE unique NONE blocks %d %d" % (len(w01), len(w04)))
    if w01 and w04:
        print("SCALE longest %s" % fmt(max(w04, key=lambda b: b[3])[2] / max(w01, key=lambda b: b[3])[2]))

    fine = grid_of(0.70, 1.30, 0.0025)
    print("FINE n %d one dist %s" % (len(fine), fmt(np.min(np.abs(fine - 1.0)))))
    fine_rows = scan_verlet(0.04, fine, 0.025)
    fine_blocks = report_plateaus("fine", fine_rows, fine, 0.0025)
    print("  fine higher %d" % len(higher_plateaus(fine_rows["nu"], fine, 0.0025)))
    gap_report(fine_rows, fine)

    # RK4 cross-check on the coarse grid at 0.04, rotation number and libration only.
    print("RK4 eps 0.04 h 0.05")
    nu_r, lib_r, on_r = scan_rk4(0.04, grid, 0.05)
    nu_v = by[0.04]["nu"]
    lib_v = by[0.04]["librates"]
    print(
        "  max |nu rk4-verlet| %s lib disagree %d"
        % (fmt(np.max(np.abs(nu_r - nu_v))), int(np.sum(lib_r != lib_v)))
    )
    rk_blocks = plateaus(on_r, grid, 0.005)
    print("  rk4 nu+lib plateaus %d (no Poincare test)" % len(rk_blocks))
    for lo, hi, width, n in rk_blocks:
        print("  %s %s width %s n %d" % (fmt(grid[lo]), fmt(grid[hi]), fmt(width), n))

    # where Verlet and the analytical island disagree, print a sample
    print("DISAGREE samples eps 0.04")
    rows = by[0.04]
    shown = 0
    for i, w in enumerate(grid):
        if rows["trapped"][i] == rows["on"][i]:
            continue
        if shown >= 24:
            break
        print(
            "  w %s trapped %s on %s nu %s sec %s lib %s other %s"
            % (
                fmt(w),
                bool(rows["trapped"][i]),
                bool(rows["on"][i]),
                fmt(rows["nu"][i]),
                fmt(rows["nu_sec"][i]) if np.isfinite(rows["nu_sec"][i]) else "nan",
                bool(rows["librates"][i]),
                bool(rows["other"][i]),
            )
        )
        shown += 1


if __name__ == "__main__":
    main()
