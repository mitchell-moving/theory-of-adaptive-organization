"""P1-S3 model. Units hbar=m=omega=1; Gaussian (Wigner) representation (see ../p1s/PREREG_P1S_2026-11-26.md §1).
Changes from P1-S (review fixes): shared income R split among living agents plus a basal upkeep m (population
regulated by starvation and ruin, small random death mu instead of random culls) [fix 2]; one force path per world
seed, generated from its own RNG and identical across arms [fix 3]; per-memory-variable record heredity h_j, offspring
body born fresh at the origin [fix 4]; anticipation measured by action u (common units across agents) [fix 6].
Fitness has no loss term and no reward for prediction or heredity."""
import numpy as np
from scipy.linalg import solve_continuous_are
BASE = dict(dt=0.02, gamma=0.1, D_e=0.05, x_r=4.0, R=50.0, m=0.2, q=0.02, mu=0.005, u_max=5.0, Nmax=500,
            sig_f=1.0, tau_f=30.0, c=0.02, tau_a=2.0, window=0.2, snap_every=1.0, r_cap=2.0)
NG = 20  # B 9 | b 3 | g 3 | logk 1 | h 3 | (unused 1)

def Amat(P): return np.array([[0, 1, 0], [-1, -P["gamma"], 1], [0, 0, -1/P["tau_f"]]])
def info_rate(P, k):
    if k <= 0: return 0.0
    S = solve_continuous_are(Amat(P).T, np.array([[1.0], [0], [0]]),
                             np.diag([1e-12, 2*P["D_e"] + k, 2*P["sig_f"]**2/P["tau_f"]]), np.array([[1/(4*k)]]))
    return S[0, 0]*2*k
def info_table(P):
    lk = np.linspace(-4, 1, 201); return lk, np.array([info_rate(P, 10**l) for l in lk])

def designed(P, kind, k):
    """Genome of a designed controller, written in the same linear-memory form the evolving agents use."""
    g = np.zeros(NG); g[15] = np.log10(k) if k > 0 else -4.0
    if kind == "sieve":
        g[0:9] = (-np.eye(3)).ravel(); g[15] = -99; return g
    A = Amat(P)
    if kind == "judge":
        S = solve_continuous_are(A.T, np.array([[1.0], [0], [0]]),
                                 np.diag([1e-12, 2*P["D_e"] + k, 2*P["sig_f"]**2/P["tau_f"]]), np.array([[1/(4*k)]]))
        L = S[:, 0]*4*k; K = np.array([0.0, -1.0, -1.0])       # u = -p_hat - f_hat
        h = np.array([0.0, 0.0, 1.0])                          # pass on the force estimate only
    else:  # reflex: filter on (x, p), force treated as extra noise; u = -x_hat - p_hat
        A2 = A[:2, :2]
        S = solve_continuous_are(A2.T, np.array([[1.0], [0]]), np.diag([1e-12, 2*P["D_e"] + k + P["sig_f"]**2]),
                                 np.array([[1/(4*k)]]))
        L = np.r_[S[:, 0]*4*k, 0.0]; K = np.array([-1.0, -1.0, 0.0]); A = np.pad(A2, ((0, 1), (0, 1))); A[2, 2] = -1
        h = np.zeros(3)
    Bm = A - np.outer(L, [1, 0, 0]) + np.outer([0, 1, 0], K)
    g[0:9] = Bm.ravel(); g[9:12] = L; g[12:15] = K; g[16:19] = h; return g

def fresh(rng, n):
    G = np.zeros((n, NG))
    G[:, 0:9] = (-np.eye(3) + rng.normal(0, 0.2, (n, 3, 3))).reshape(n, 9)
    G[:, 9:12] = rng.normal(0, 0.5, (n, 3)); G[:, 12:15] = rng.normal(0, 0.5, (n, 3))
    G[:, 15] = rng.uniform(-4, 1, n); G[:, 16:19] = rng.uniform(0, 1, (n, 3)); return G

def mutate(rng, g):
    g = g.copy(); g[:15] += rng.normal(0, 0.05, 15); g[15] = np.clip(g[15] + rng.normal(0, 0.1), -4, 1)
    g[16:19] = np.clip(g[16:19] + rng.normal(0, 0.05, 3), 0, 1); return g

def force_path(P, world_seed, nsteps):
    r = np.random.default_rng(10_000 + world_seed); a = np.exp(-P["dt"]/P["tau_f"]); s = P["sig_f"]*np.sqrt(1 - a*a)
    f = np.empty(nsteps + 1); f[0] = r.normal(0, P["sig_f"]); e = r.normal(0, 1, nsteps)
    for i in range(nsteps): f[i + 1] = a*f[i] + s*e[i]
    return f

def run(P, T, seed, mode, arm=None, founders=None, labels=None, snap=True):
    """mode 'evolve': arm in {'on','off','sieve'}; mode 'fixed': founders = genomes (N0,NG), labels = type ids, no mutation."""
    dt = P["dt"]; N = P["Nmax"]; nst = int(T/dt); rng = np.random.default_rng(seed)
    fp = force_path(P, seed, nst); lk, It = info_table(P)
    G = np.zeros((N, NG)); lab = -np.ones(N, int); alive = np.zeros(N, bool)
    n0 = 250 if founders is None else len(founders)
    G[:n0] = fresh(rng, n0) if founders is None else founders
    if mode == "evolve" and arm == "sieve": G[:n0, 15] = -99
    if labels is not None: lab[:n0] = labels
    alive[:n0] = True
    x = rng.normal(0, np.sqrt(.5), N); p = rng.normal(0, np.sqrt(.5), N); z = np.zeros((N, 3)); E = np.ones(N); age = np.zeros(N)
    t_win = T*(1 - P["window"]); snap_k = int(round(P["snap_every"]/dt)); lag = int(round(P["tau_a"]/dt))
    st = dict(ruin=0, starve=0, rand=0, cull=0, births=0, agent_time=0.0); snaps = []; hk = []; lkk = []; Nser = []
    extinct = None
    for s in range(nst):
        t = s*dt; f = fp[s]; inw = t >= t_win
        reading = G[:, 15] > -50
        k = np.where(reading, 10**np.clip(G[:, 15], -4, 1), 0.0)
        Ir = np.where(reading, np.interp(np.clip(G[:, 15], -4, 1), lk, It), 0.0)
        Bm = G[:, 0:9].reshape(N, 3, 3); b = G[:, 9:12]; g = G[:, 12:15]
        u = np.clip(np.einsum('ij,ij->i', g, z), -P["u_max"], P["u_max"])
        dy = np.where(reading, x*dt + rng.normal(0, 1, N)*np.sqrt(dt/(4*np.maximum(k, 1e-30))), 0.0)
        xn = x + p*dt
        p = p + (-x - P["gamma"]*p + f + u)*dt + rng.normal(0, 1, N)*np.sqrt(2*P["D_e"]*dt) + rng.normal(0, 1, N)*np.sqrt(k*dt)
        x = xn; z = np.clip(z + np.einsum('ijk,ik->ij', Bm, z)*dt + b*dy[:, None], -50, 50)
        na = alive.sum(); inc = min(P["R"]/max(na, 1), P["r_cap"])
        E = E + (inc - P["m"] - P["c"]*Ir - P["q"]*u*u)*dt; age += dt
        ruin = alive & ((np.abs(x) > P["x_r"]) | ~np.isfinite(x)); starve = alive & ~ruin & (E <= 0)
        rnd = alive & ~ruin & ~starve & (rng.random(N) < P["mu"]*dt)
        if inw:
            st["agent_time"] += na*dt; st["ruin"] += ruin.sum(); st["starve"] += starve.sum(); st["rand"] += rnd.sum()
        alive &= ~(ruin | starve | rnd)
        if not alive.any(): extinct = t; break
        for i in np.flatnonzero(alive & (E >= 2.0)):
            free = np.flatnonzero(~alive)
            if free.size: j = free[0]
            else:
                j = rng.choice(np.flatnonzero(alive & (np.arange(N) != i)))
                if inw: st["cull"] += 1
            if mode == "evolve":
                gj = fresh(rng, 1)[0] if arm == "off" else mutate(rng, G[i])
                if arm == "sieve": gj[15] = -99
            else: gj = G[i].copy()
            hpar = G[i, 16:19]; G[j] = gj; lab[j] = lab[i]
            z[j] = hpar*z[i]; E[i] = 1.0; E[j] = 1.0
            x[j] = rng.normal(0, np.sqrt(.5)); p[j] = rng.normal(0, np.sqrt(.5)); age[j] = 0.0; alive[j] = True
            if inw: st["births"] += 1
        if inw and s % snap_k == 0:
            Nser.append(alive.sum())
            if snap and s + lag <= nst:
                mm = alive & (age >= 2.0)
                snaps.append((fp[s + lag], x[mm].copy(), p[mm].copy(), u[mm].copy(), lab[mm].copy()))
            hk.append(G[alive, 16:19].max(1).mean()); lkk.append(np.median(np.where(G[alive, 15] > -50, G[alive, 15], -4)))
    res = dict(extinct_t=extinct, **{kk: (float(v) if isinstance(v, float) else int(v)) for kk, v in st.items()})
    if extinct is not None: return res
    res["N_mean"] = float(np.mean(Nser)); res["h_max_mean"] = float(np.mean(hk)); res["logk_median"] = float(np.median(lkk))
    tot = st["ruin"] + st["starve"] + st["rand"] + st["cull"]
    res["ruin_share"] = st["ruin"]/tot if tot else 0.0
    res["ruin_hazard"] = st["ruin"]/st["agent_time"]
    res["gen_time"] = st["agent_time"]/max(st["births"], 1)
    if labels is not None: res["final_freq"] = {int(l): float(np.mean(lab[alive] == l)) for l in np.unique(labels)}
    if snap and snaps:
        Y = np.concatenate([np.full(s[1].size, s[0]) for s in snaps])
        X0 = np.vstack([np.c_[np.ones_like(s[1]), s[1], s[2]] for s in snaps]); U = np.concatenate([s[3] for s in snaps])
        def r2(X):
            beta, *_ = np.linalg.lstsq(X, Y, rcond=None); r = Y - X@beta; return 1 - r.var()/Y.var()
        res["r2_body"] = float(r2(X0)); res["dA_u"] = float(r2(np.c_[X0, U]) - r2(X0))
        # within-type check of the action measure is reported by the caller via labels (fixed mode)
    return res
