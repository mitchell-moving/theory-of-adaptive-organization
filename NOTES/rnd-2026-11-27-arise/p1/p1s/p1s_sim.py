"""P1-S: selection of heritable linear controllers in a dephasing oscillator with a drifting force.
Units hbar = m = omega = 1. Gaussian (Wigner) representation, exact for linear dynamics with Gaussian
states and Gaussian measurement; the quantum content is (i) coherent-state births (Wigner variance 1/2
in x and p) and (ii) the measurement imprecision-backaction product N*Gamma = 1/4 (record noise
intensity N = 1/(4k), momentum backaction diffusion Gamma = k).
Fitness has NO loss term and NO reward for prediction or heredity: an agent dies at the ruin edge
|x| > x_r or when its energy budget hits 0; it splits when its budget reaches 2.
Usage: python3 p1s_sim.py CELL SEED T OUTJSON
"""
import sys, json, time
import numpy as np
from scipy.linalg import solve_continuous_are

PAR = dict(dt=0.02, gamma=0.1, D_e=0.05, x_r=4.0, r0=0.2, q=0.02, u_max=5.0,
           Nmax=300, sig_f=1.5, tau_a=2.0, snap_every=1.0, window=0.2)
CELLS = {  # name: (tau_f, price c per nat, arm)
    "P_low_on":    (30.0, 0.02, "on"),
    "P_low_off":   (30.0, 0.02, "off"),
    "P_low_sieve": (30.0, 0.02, "sieve"),
    "U_low_on":    (0.2,  0.02, "on"),
    "P_high_on":   (30.0, 2.0,  "on"),
}
NG = 17  # B(9) b(3) g(3) logk(1) h(1)

def info_rate_table(tau_f, P):
    lk = np.linspace(-4, 1, 201); out = []
    for l in lk:
        k = 10**l
        A = np.array([[0, 1, 0], [-1, -P["gamma"], 1], [0, 0, -1/tau_f]])
        Q = np.diag([1e-12, 2*P["D_e"] + k, 2*P["sig_f"]**2/tau_f])
        C = np.array([[1.0, 0, 0]]); R = np.array([[1/(4*k)]])
        S = solve_continuous_are(A.T, C.T, Q, R)
        out.append(S[0, 0]/(2*R[0, 0]))  # Duncan: nats per unit time = Var(x|record)/(2N)
    return lk, np.array(out)

def fresh(rng, n):
    G = np.empty((n, NG))
    G[:, 0:9] = (-np.eye(3) + rng.normal(0, 0.2, (n, 3, 3))).reshape(n, 9)
    G[:, 9:12] = rng.normal(0, 0.5, (n, 3)); G[:, 12:15] = rng.normal(0, 0.5, (n, 3))
    G[:, 15] = rng.uniform(-4, 1, n); G[:, 16] = rng.uniform(0, 1, n)
    return G

def mutate(rng, g):
    g = g.copy(); g[:15] += rng.normal(0, 0.05, 15); g[15] = np.clip(g[15] + rng.normal(0, 0.1), -4, 1)
    g[16] = np.clip(g[16] + rng.normal(0, 0.05), 0, 1); return g

def run(cell, seed, T, P=PAR):
    tau_f, c, arm = CELLS[cell]
    rng = np.random.default_rng(seed); dt = P["dt"]; N = P["Nmax"]
    lk_tab, I_tab = info_rate_table(tau_f, P)
    G = fresh(rng, N); alive = np.ones(N, bool)
    x = rng.normal(0, np.sqrt(0.5), N); p = rng.normal(0, np.sqrt(0.5), N)
    z = np.zeros((N, 3)); E = np.ones(N); age = np.zeros(N)
    f = rng.normal(0, P["sig_f"]); nsteps = int(T/dt)
    af = np.exp(-dt/tau_f); sf = P["sig_f"]*np.sqrt(1 - af**2)
    t_win = T*(1 - P["window"]); snap_k = int(round(P["snap_every"]/dt))
    fser = np.empty(nsteps + 1); snaps = []
    ruin_deaths = 0; budget_deaths = 0; agent_time = 0.0; births = 0; extinct_t = None
    hk, lkk = [], []
    for s in range(nsteps):
        t = s*dt; fser[s] = f
        k = np.where(arm == "sieve", 0.0, 10**G[:, 15]) if arm != "sieve" else np.zeros(N)
        Irate = np.interp(G[:, 15], lk_tab, I_tab) if arm != "sieve" else np.zeros(N)
        B = G[:, 0:9].reshape(N, 3, 3); b = G[:, 9:12]; g = G[:, 12:15]
        u = np.clip(np.einsum('ij,ij->i', g, z), -P["u_max"], P["u_max"])
        with np.errstate(divide='ignore', invalid='ignore'):
            dy = np.where(k > 0, x*dt + rng.normal(0, 1, N)*np.sqrt(dt/(4*np.maximum(k, 1e-30))), 0.0)
        xn = x + p*dt
        p = p + (-x - P["gamma"]*p + f + u)*dt + rng.normal(0, 1, N)*np.sqrt(2*P["D_e"]*dt) \
              + rng.normal(0, 1, N)*np.sqrt(k*dt)
        x = xn
        z = np.clip(z + np.einsum('ijk,ik->ij', B, z)*dt + b*dy[:, None], -50, 50)
        E = E + (P["r0"] - c*Irate - P["q"]*u**2)*dt; age += dt
        f = af*f + sf*rng.normal()
        inwin = t >= t_win
        if inwin: agent_time += alive.sum()*dt
        ruin = alive & ((np.abs(x) > P["x_r"]) | ~np.isfinite(x)); bud = alive & ~ruin & (E <= 0)
        if inwin: ruin_deaths += ruin.sum(); budget_deaths += bud.sum()
        alive &= ~(ruin | bud)
        if not alive.any():
            extinct_t = t; break
        rep = np.flatnonzero(alive & (E >= 2.0))
        for i in rep:
            free = np.flatnonzero(~alive)
            j = free[0] if free.size else rng.choice(np.flatnonzero(alive & (np.arange(N) != i)))
            if arm == "off":
                gj = fresh(rng, 1)[0]
            else:
                gj = mutate(rng, G[i])
            G[j] = gj; h_par = G[i, 16]
            z[j] = h_par*z[i]; E[i] = 1.0; E[j] = 1.0
            x[j] = rng.normal(0, np.sqrt(0.5)); p[j] = rng.normal(0, np.sqrt(0.5)); age[j] = 0.0
            alive[j] = True; births += 1
        if inwin and s % snap_k == 0:
            m = alive & (age >= 2.0)
            snaps.append((s, x[m].copy(), p[m].copy(), z[m].copy(), u[m].copy()))
            hk.append(G[alive, 16].mean()); lkk.append(np.median(G[alive, 15]))
    fser[s + 1] = f
    res = dict(cell=cell, seed=seed, T=T, extinct_t=extinct_t, births=int(births))
    if extinct_t is not None:
        return res
    lag = int(round(P["tau_a"]/dt)); X0, X1, X2, Y = [], [], [], []
    for (s, xs, ps, zs, us) in snaps:
        if s + lag > nsteps or xs.size == 0: continue
        fy = fser[s + lag]
        X0.append(np.c_[np.ones_like(xs), xs, ps]); X1.append(np.c_[np.ones_like(xs), xs, ps, zs])
        X2.append(np.c_[np.ones_like(xs), xs, ps, us]); Y.append(np.full(xs.size, fy))
    def r2(Xl):
        Xa = np.vstack(Xl); Ya = np.concatenate(Y)
        beta, *_ = np.linalg.lstsq(Xa, Ya, rcond=None); r = Ya - Xa@beta
        return float(1 - r.var()/Ya.var())
    r2_body, r2_z, r2_u = r2(X0), r2(X1), r2(X2)
    res.update(dA_z=r2_z - r2_body, dA_u=r2_u - r2_body, r2_body=r2_body,
               ruin_hazard=float(ruin_deaths/agent_time), budget_hazard=float(budget_deaths/agent_time),
               h_mean=float(np.mean(hk)), logk_median=float(np.median(lkk)), n_obs=int(sum(len(y) for y in Y)))
    return res

if __name__ == "__main__":
    cell, seed, T, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    t0 = time.time(); r = run(cell, seed, T); r["wall_s"] = round(time.time() - t0, 1)
    json.dump(r, open(out, "w"), indent=1); print(json.dumps(r))
