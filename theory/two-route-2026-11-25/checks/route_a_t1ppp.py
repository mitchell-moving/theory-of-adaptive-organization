#!/usr/bin/env python3
"""A-T1''' (PREREG_4.md, scoring per PREREG_4a.md): Nash gap G on model W2 with a shared
excursion cost w_x E[x^2] in both party costs, at w_x in {0.5, 1, 2}.

  J_m = Q_M + w E[(x-m)^2] + w_x E[x^2]          (memory picks gamma, c)
  J_w = Q_X + w_w E[(x-g m)^2] + w_x E[x^2]      (world picks g)
  J_tot = J_m + J_w;  G = J_tot(Nash) / min J_tot - 1.

a = D = D_M = 1, w = w_w = 10. Closed-form stationary moments (PREREG_3.md section 1.1,
checked symbolically in gate read v3), cross-checked here against the Lyapunov solver of
route_a_w2.py at every reported point.

Grids, boxes, guard, Nash schedule and tolerances are those of PREREG_2.md section 4 as
amended by PREREG_3.md section 2.1 and PREREG_4.md section 2.1. Usage:
  route_a_t1ppp.py run   [--wx 1.0] [--half]   one sweep point (JSON to stdout)
  route_a_t1ppp.py verify FILE                 fast re-check of a stored run (used by pytest)
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize, minimize_scalar

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from route_a_w2 import stats  # noqa: E402  Lyapunov cross-check

W, WW = 10.0, 10.0
LG_BOX, C_BOX, G_BOX, GUARD = (-3.0, 5.0), (-2.0, 3.0), (0.0, 3.0), 0.999
BIG = 1e12
# Locked: 1e-6 on designs, 1e-8 relative on J (PREREG_2.md section 4). The solvers run
# tighter than that (logged in DEVIATIONS.md before any result was seen) so that the
# locked 1e-6 Nash stop rule is not tripped by solver noise. --half halves all of them.
TOL = dict(nm_x=1e-8, nm_f=1e-10, brent=1e-10, stop=1e-6)


def moments(gamma, c, g):
    """Closed-form W2 moments; None if outside the stable region."""
    if gamma <= 0 or g * c >= 1:
        return None
    k = (g + gamma * gamma * c) / (gamma * (1 + gamma) * (1 - g * c))
    return dict(
        sxx=1 + g * k,
        qx=g * (g - gamma * c) / (1 + gamma),
        qm=gamma * c * (gamma * c - g) / (1 + gamma),
        xgm2=1 + g * (g - gamma * c) / (1 + gamma),
        xm2=1 + 1 / gamma + (g + c - 2) * k,
    )


def costs(gamma, c, g, wx):
    s = moments(gamma, c, g)
    if s is None:
        return None
    jm = s["qm"] + W * s["xm2"] + wx * s["sxx"]
    jw = s["qx"] + WW * s["xgm2"] + wx * s["sxx"]
    return jm, jw, jm + jw


def inside(lg, c, g):
    return (LG_BOX[0] <= lg <= LG_BOX[1] and C_BOX[0] <= c <= C_BOX[1]
            and G_BOX[0] <= g <= G_BOX[1] and g * c <= GUARD)


def mem_br(g, wx, tol):
    def f(p):
        if not inside(p[0], p[1], g):
            return BIG
        r = costs(np.exp(p[0]), p[1], g, wx)
        return BIG if r is None else r[0]
    best = None
    for lg in np.linspace(-3, 5, 17):
        for c0 in np.linspace(-1, 3, 17):
            if not inside(lg, c0, g):
                continue
            r = minimize(f, [lg, c0], method="Nelder-Mead",
                         options=dict(xatol=tol["nm_x"], fatol=tol["nm_f"], maxiter=40000, maxfev=80000))
            if best is None or r.fun < best.fun:
                best = r
    return float(np.exp(best.x[0])), float(best.x[1])


def world_br(gamma, c, wx, tol):
    gmax = min(G_BOX[1], GUARD / c) if c > 0 else G_BOX[1]

    def f(g):
        if not inside(np.log(gamma), c, g):
            return BIG
        r = costs(gamma, c, g, wx)
        return BIG if r is None else r[1]
    grid = np.linspace(0.0, gmax, 201)
    vals = [f(x) for x in grid]
    i = int(np.argmin(vals))
    lo, hi = grid[max(i - 1, 0)], grid[min(i + 1, 200)]
    r = minimize_scalar(f, bounds=(lo, hi), method="bounded", options=dict(xatol=tol["brent"]))
    return float(r.x) if r.fun <= vals[i] else float(grid[i])


def joint_min(wx, tol):
    def f(p):
        if not inside(*p):
            return BIG
        r = costs(np.exp(p[0]), p[1], p[2], wx)
        return BIG if r is None else r[2]
    best = None
    for lg in np.linspace(-3, 5, 17):
        for c0 in np.linspace(-1, 3, 17):
            for g0 in np.linspace(0, 2, 9):
                if not inside(lg, c0, g0):
                    continue
                r = minimize(f, [lg, c0, g0], method="Nelder-Mead",
                             options=dict(xatol=tol["nm_x"], fatol=tol["nm_f"], maxiter=60000, maxfev=120000))
                if best is None or r.fun < best.fun:
                    best = r
    return float(np.exp(best.x[0])), float(best.x[1]), float(best.x[2]), float(best.fun)


def nash(wx, tol):
    gamma, c, g = 6.884, 0.592, 0.0
    hist = []
    for phase, damp, rounds in (("undamped", 1.0, 200), ("damped", 0.5, 200)):
        for k in range(rounds):
            g_new = world_br(gamma, c, wx, tol)
            g_new = (1 - damp) * g + damp * g_new
            gm_br, c_br = mem_br(g_new, wx, tol)
            gm_new = (1 - damp) * gamma + damp * gm_br
            c_new = (1 - damp) * c + damp * c_br
            delta = max(abs(gm_new - gamma), abs(c_new - c), abs(g_new - g))
            gamma, c, g = gm_new, c_new, g_new
            hist.append([phase, k + 1, gamma, c, g, delta])
            if delta < tol["stop"]:
                return dict(settled=True, phase=phase, rounds=k + 1, gamma=gamma, c=c, g=g, history=hist)
    return dict(settled=False, phase="damped", rounds=400, gamma=gamma, c=c, g=g, history=hist)


def on_boundary(gamma, c, g, eps=1e-4):
    lg = np.log(gamma)
    return bool(min(lg - LG_BOX[0], LG_BOX[1] - lg, c - C_BOX[0], C_BOX[1] - c,
                    g - G_BOX[0], G_BOX[1] - g) < eps or g * c > GUARD - eps)


def lyap_check(gamma, c, g, wx):
    s = stats(gamma, c, g)
    S = np.array(s["S"])
    jm = s["Qm"] + W * s["loss"] + wx * S[0, 0]
    ux = np.array([1.0, -g])
    jw = s["Qx"] + WW * float(ux @ S @ ux) + wx * S[0, 0]
    cf = costs(gamma, c, g, wx)
    return float(max(abs(jm - cf[0]), abs(jw - cf[1])))


def run(wx, half):
    tol = {k: v / 2 for k, v in TOL.items()} if half else dict(TOL)
    jg, jc, jgg, jmin = joint_min(wx, tol)
    n = nash(wx, tol)
    out = dict(w_x=wx, half_tolerance=half, tol=tol,
               joint_min=dict(gamma=jg, c=jc, g=jgg, gc=jc * jgg, J_tot=jmin,
                              boundary=on_boundary(jg, jc, jgg), lyap_diff=lyap_check(jg, jc, jgg, wx)),
               nash=dict(settled=n["settled"], phase=n["phase"], rounds=n["rounds"],
                         gamma=n["gamma"], c=n["c"], g=n["g"], gc=n["c"] * n["g"]))
    if n["settled"]:
        jm, jw, jt = costs(n["gamma"], n["c"], n["g"], wx)
        out["nash"].update(J_m=jm, J_w=jw, J_tot=jt, boundary=on_boundary(n["gamma"], n["c"], n["g"]),
                           lyap_diff=lyap_check(n["gamma"], n["c"], n["g"], wx))
        out["G"] = jt / jmin - 1
    out["history_tail"] = n["history"][-5:]
    return out


def verify(path):
    """Fast re-check of a stored run: closed form vs Lyapunov, G recomputed, joint min below
    Nash, the Nash point a fixed point of one more best-reply round, every point interior."""
    data = json.load(open(path))
    fails = 0
    for r in data["runs"]:
        wx, jm, ns = r["w_x"], r["joint_min"], r["nash"]
        tol = r["tol"]
        jt = costs(jm["gamma"], jm["c"], jm["g"], wx)[2]
        ok = abs(jt - jm["J_tot"]) < 1e-9 and lyap_check(jm["gamma"], jm["c"], jm["g"], wx) < 1e-8
        if ns["settled"]:
            jn = costs(ns["gamma"], ns["c"], ns["g"], wx)[2]
            ok &= abs(jn / jm["J_tot"] - 1 - r["G"]) < 1e-12 and r["G"] >= -1e-9
            ok &= lyap_check(ns["gamma"], ns["c"], ns["g"], wx) < 1e-8
            g1 = world_br(ns["gamma"], ns["c"], wx, tol)
            ok &= abs(g1 - ns["g"]) < 1e-5
        print(f"w_x={wx} half={r['half_tolerance']}: {'OK' if ok else 'FAIL'}")
        fails += 0 if ok else 1
    print(f"FAILS {fails}")
    return fails


if __name__ == "__main__":
    if sys.argv[1] == "verify":
        sys.exit(1 if verify(sys.argv[2]) else 0)
    wx = float(sys.argv[sys.argv.index("--wx") + 1]) if "--wx" in sys.argv else 1.0
    json.dump(run(wx, "--half" in sys.argv), sys.stdout, indent=1)
    print()
