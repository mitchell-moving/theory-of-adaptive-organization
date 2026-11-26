#!/usr/bin/env python3
"""Route A, model W2 (PREREG.md section 2.1): A-C1 and A-T2.

dx = -a (x - g m) dt + sqrt(2D) dW_x,  dm = -gamma (m - c x) dt + sqrt(2 D_M) dW_m.
Stationary covariance from the Lyapunov equation; heats Q_i = E[f_i^2] + D_i E[d_i f_i];
memory learning rate l_M from the Gaussian steady state (Horowitz-Esposito split).
Cost J = Q_M + Q_X + w E[(x-m)^2]. Scored: rho = Q_M*(0.5)/Q_M*(0) (A-T2).
"""
import json, sys
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import minimize

A0, D, DM, W = 1.0, 1.0, 1.0, 10.0


def stats(gamma, c, g, a=A0, d=D, dm=DM, w=W):
    A = np.array([[a, -a * g], [-gamma * c, gamma]])
    ev = np.linalg.eigvals(A)
    if np.min(ev.real) <= 0:
        return None
    S = solve_continuous_lyapunov(A, 2 * np.diag([d, dm]))  # A S + S A^T = 2 Dmat
    ux = np.array([1.0, -g]); um = np.array([-c, 1.0])
    Qx = a * a * ux @ S @ ux - d * a
    Qm = gamma * gamma * um @ S @ um - dm * gamma
    loss = S[0, 0] + S[1, 1] - 2 * S[0, 1]
    Si = np.linalg.inv(S)
    # v_m = f_m + D_M (S^-1 z)_m ; l_M = E[v_m * (-(S^-1 z)_m + m / S_mm)]
    vm = -gamma * um + dm * Si[1]
    q = -Si[1] + np.array([0.0, 1.0 / S[1, 1]])
    lM = vm @ S @ q
    J = Qm + Qx + w * loss
    return dict(J=J, Qm=Qm, Qx=Qx, loss=loss, lM=lM, S=S.tolist())


def obj(p, g):
    gamma, c = np.exp(p[0]), p[1]
    if g * c >= 1:
        return 1e12
    s = stats(gamma, c, g)
    return 1e12 if s is None else s["J"]


def optimize(g, tol=1e-10):
    best = None
    for lg in np.linspace(-3, 5, 17):
        for c in np.linspace(-1, 3, 17):
            if g * c >= 1:
                continue
            r = minimize(obj, [lg, c], args=(g,), method="Nelder-Mead",
                         options=dict(xatol=tol, fatol=tol, maxiter=20000))
            if best is None or r.fun < best.fun:
                best = r
    gamma, c = float(np.exp(best.x[0])), float(best.x[1])
    return gamma, c, stats(gamma, c, g)


def simulate(gamma, c, g, n=400000, dt=1e-3, seed=1):
    rng = np.random.default_rng(seed)
    x = m = 0.0; xs = np.empty(n); ms = np.empty(n)
    sx, sm = np.sqrt(2 * D * dt), np.sqrt(2 * DM * dt)
    nx = rng.standard_normal(n); nm = rng.standard_normal(n)
    for i in range(n):
        x, m = x - A0 * (x - g * m) * dt + sx * nx[i], m - gamma * (m - c * x) * dt + sm * nm[i]
        xs[i] = x; ms[i] = m
    b = n // 10
    return np.cov(np.vstack([xs[b:], ms[b:]]))


def main():
    out = {}
    # A-C1 (CONSISTENCY_CHECK): at g = 0 the world bath heat is 0 at every memory design
    ac1 = [stats(gm, c, 0.0)["Qx"] for gm in (0.3, 1.0, 4.0) for c in (0.2, 0.9, 1.5)]
    out["A-C1_max_abs_Qx_at_g0"] = float(np.max(np.abs(ac1)))
    # JP-heat sanity: Q_M >= D_M l_M at random designs
    rng = np.random.default_rng(7); viol = 0
    for _ in range(2000):
        g = rng.uniform(-1, 0.9); c = rng.uniform(-1, 1.05); gm = np.exp(rng.uniform(-2, 3))
        s = stats(gm, c, g)
        if s and s["Qm"] < DM * s["lM"] - 1e-9:
            viol += 1
    out["JP_heat_violations_of_2000"] = viol
    rows = {}
    for g in (0.0, 0.25, 0.5, 0.75, 0.9):
        gamma, c, s = optimize(g)
        rows[str(g)] = dict(gamma=gamma, c=c, J=s["J"], Qm=s["Qm"], Qx=s["Qx"], loss=s["loss"], lM=s["lM"])
    out["optimum_by_g"] = rows
    rho = rows["0.5"]["Qm"] / rows["0.0"]["Qm"]
    out["A-T2_rho"] = rho
    # tolerance check: halve-tolerance (here: looser 1e-5 vs 1e-10) must move rho by < 0.01
    g5 = optimize(0.5, tol=1e-5)[2]["Qm"]; g0 = optimize(0.0, tol=1e-5)[2]["Qm"]
    out["A-T2_rho_loose_tol"] = g5 / g0
    # simulation cross-check of the Lyapunov covariance at the g = 0.5 optimum
    r5 = rows["0.5"]
    Ssim = simulate(r5["gamma"], r5["c"], 0.5)
    Slyap = np.array(stats(r5["gamma"], r5["c"], 0.5)["S"])
    out["sim_vs_lyap_max_rel_diff"] = float(np.max(np.abs(Ssim - Slyap) / np.abs(Slyap).max()))
    json.dump(out, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
