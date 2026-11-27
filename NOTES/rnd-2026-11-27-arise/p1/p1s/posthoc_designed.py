"""POST HOC diagnostic (not preregistered; does not rescore P1-S or P1-S2).
Question: in the P1-S world, does a designed judge (steady-state Kalman filter on (x,p,f) + feedback that
cancels the estimated force) actually beat a reflex controller (filter on (x,p) only) and no reading (sieve),
at the same prices? If not, the miss says the world did not reward judging, not that selection failed to find it.
No births; on ruin an agent is counted and reborn in the coherent state with a fresh filter."""
import numpy as np, sys
sys.path.insert(0, '.')
import p1s_sim as m
from scipy.linalg import solve_continuous_are
def run(sig_f, k, mode, c=0.02, T=1500, N=300, seed=7):
    P = dict(m.PAR); P["sig_f"] = sig_f; tau = 30.0; dt = P["dt"]; rng = np.random.default_rng(seed)
    lk, It = m.info_rate_table(tau, P); Irate = 0 if k == 0 else np.interp(np.log10(k), lk, It)
    A = np.array([[0, 1, 0], [-1, -P["gamma"], 1], [0, 0, -1/tau]])
    if mode == "reflex": A2 = A[:2, :2]; Q2 = np.diag([1e-12, 2*P["D_e"] + k + sig_f**2])  # f treated as white-ish extra noise
    if k > 0:
        if mode == "judge":
            S = solve_continuous_are(A.T, np.array([[1.0], [0], [0]]), np.diag([1e-12, 2*P["D_e"] + k, 2*sig_f**2/tau]), np.array([[1/(4*k)]]))
            L = S[:, 0]*(4*k)
        else:
            S = solve_continuous_are(A2.T, np.array([[1.0], [0]]), Q2, np.array([[1/(4*k)]])); L = np.r_[S[:, 0]*(4*k), 0.0]
    x = rng.normal(0, .7071, N); p = rng.normal(0, .7071, N); sh = np.zeros((N, 3)); f = rng.normal(0, sig_f)
    af = np.exp(-dt/tau); sf = sig_f*np.sqrt(1 - af**2); ruins = 0; ucost = 0.0
    for s in range(int(T/dt)):
        if k == 0: u = np.zeros(N)
        elif mode == "judge": u = np.clip(-sh[:, 2] - 1.0*sh[:, 1], -5, 5)
        else: u = np.clip(-1.0*sh[:, 0] - 1.0*sh[:, 1], -5, 5)
        if k > 0:
            dy = x*dt + rng.normal(0, 1, N)*np.sqrt(dt/(4*k))
            Am = A if mode == "judge" else np.pad(A2, ((0, 1), (0, 1)))
            sh = sh + (sh@Am.T + np.c_[np.zeros(N), u, np.zeros(N)])*dt + np.outer(dy - sh[:, 0]*dt, L)
        xn = x + p*dt
        p = p + (-x - P["gamma"]*p + f + u)*dt + rng.normal(0, 1, N)*np.sqrt(2*P["D_e"]*dt) + rng.normal(0, 1, N)*np.sqrt(k*dt)
        x = xn; f = af*f + sf*rng.normal(); ucost += (P["q"]*u**2).sum()*dt
        r = np.abs(x) > P["x_r"]; ruins += r.sum()
        x[r] = rng.normal(0, .7071, r.sum()); p[r] = rng.normal(0, .7071, r.sum()); sh[r] = 0
    at = N*T
    return ruins/at, P["r0"] - c*Irate - ucost/at, Irate
print("sig_f mode k ruin_hazard net_income_rate nats_per_time")
for sig_f in (1.0, 1.5):
    print(sig_f, "sieve", 0, *[round(v, 5) for v in run(sig_f, 0, "sieve")])
    for k in (1e-3, 1e-2, 1e-1, 1.0):
        for mode in ("reflex", "judge"):
            print(sig_f, mode, k, *[round(v, 5) for v in run(sig_f, k, mode)])
