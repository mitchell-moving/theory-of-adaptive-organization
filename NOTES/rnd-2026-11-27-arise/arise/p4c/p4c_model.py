"""P4c (from P4b): eps=0; novelty only by stochastic nucleation (rate mu per compartment-time, one molecule
1/Mmol of a random core, from food-set side reactions); optional reader-absent start. P4b text follows: mutually exclusive autocatalytic cores in growing, dividing compartments (toy, lumped cores).
Cores k=0..3 compete Lotka-Volterra style (beta>1 => one core wins per compartment: alternative stable states).
Core 0 = HEDGER (diverts theta*duty of its synthesis to detox D, always, unpriced). Core 1 = READER (diverts theta of
its synthesis to D while the cue is on; pays c_nat * h(duty) nats/time as extra decay). Cores 2,3 = plain.
A toxin pulse raises decay of all cores by tau/(1+D/Dk). Fitness = compartment volume growth only."""
import numpy as np
BASE = dict(dt=0.05, Nc=200, r=1.0, K=1.0, beta=1.5, eps=0.0, delta=0.05, tau=1.0, Dk=0.05, dD=1.0, theta=0.3,
            gamma=0.1, P=30.0, Lt=5.0, Lc=4.0, cnat=0.01, cue_mode="cued", heredity="on", Mmol=200.0, T=3000.0, window=0.5, mu=0.01, absent=True)
def hb(p): return 0.0 if p <= 0 or p >= 1 else float(-p*np.log(p) - (1-p)*np.log(1-p))
def schedule(P, nst, wrng):
    dt = P["dt"]; tox = np.zeros(nst + 1); cue = np.zeros(nst + 1); onsets = []; t = 0.0
    while True:
        t += wrng.uniform(0.5, 1.5)*P["P"]
        i0 = int(t/dt)
        if i0 >= nst: break
        tox[i0:i0 + int(P["Lt"]/dt)] = 1; cue[max(0, i0 - int(P["Lc"]/dt)):i0] = 1; onsets.append(i0)
    if P["cue_mode"] == "random":
        L = int(P["Lc"]/dt); cue = np.zeros(nst + 1)
        for o in wrng.integers(0, nst + 1 - L, len(onsets)): cue[o:o + L] = 1
    return tox[:nst + 1], cue[:nst + 1], onsets
def ident(x, thr=0.8):
    f = x/np.maximum(x.sum(1, keepdims=True), 1e-12); k = f.argmax(1); return np.where(f.max(1) >= thr, k, -1)
def kappa(a, b):
    m = (a >= 0) & (b >= 0); a, b = a[m], b[m]
    if len(a) == 0: return float("nan")
    po = np.mean(a == b); pe = sum(np.mean(a == k)*np.mean(b == k) for k in range(4))
    return float((po - pe)/(1 - pe)) if pe < 1 else float("nan")
def run(P, seed):
    rng = np.random.default_rng(seed); wrng = np.random.default_rng(70_000 + seed)
    N, dt = P["Nc"], P["dt"]; nst = int(P["T"]/dt); tox, cue, onsets = schedule(P, nst, wrng)
    duty = cue.mean(); th = np.zeros((nst + 1, 4)); th[:, 0] = P["theta"]*duty; th[:, 1] = P["theta"]*cue
    if P["Lc"] == 0: th[:] = 0.0                      # SIEVE: no cue, no reading, no hedging
    price = np.zeros(4); price[1] = P["cnat"]*hb(duty) if P["Lc"] > 0 else 0.0
    x = rng.dirichlet(np.ones(4), N)*0.5
    if P["absent"]: x[:, 1] = 0.0
    first = float("nan"); D = np.zeros(N); V = rng.uniform(1, 2, N)
    birth_id = np.full(N, -2); pairs = []; t_win = int(nst*(1 - P["window"])); fis = 0; ctime = 0.0
    freq = []; excl = []; Dpre = []
    B = P["beta"]*np.ones((4, 4)) - (P["beta"] - 1)*np.eye(4)
    for st in range(nst):
        comp = 1 - (x @ B.T)/P["K"]
        syn = P["r"]*x*np.maximum(comp, -1.0)
        prod = np.where(syn > 0, syn, 0.0)
        dec = (P["delta"] + P["tau"]*tox[st]/(1 + D/P["Dk"]))[:, None]*x + price*x
        x = np.maximum(x + (syn*(1 - th[st]) + P["eps"] - dec)*dt, 0.0)
        D = D + ((prod*th[st]).sum(1) - P["dD"]*D)*dt
        V = V*(1 + P["gamma"]*x.sum(1)/P["K"]*dt)
        nuc = np.flatnonzero(rng.random(N) < P["mu"]*dt)
        if len(nuc): x[nuc, rng.integers(0, 4, len(nuc))] += 1.0/P["Mmol"]
        if np.isnan(first) and st % int(1/dt) == 0 and np.sum(ident(x) == 1) >= 2: first = st*dt
        inw = st >= t_win
        if inw: ctime += N*dt
        if inw and st in onsets: Dpre.append(D.mean())
        for i in np.flatnonzero(V >= 2):
            idp = ident(x[i:i+1])[0]
            if inw and birth_id[i] != -2: pairs.append((birth_id[i], idp))
            d = rng.integers(0, N - 1); d = d + (d >= i); V[i] = V[d] = 1.0; D[d] = D[i]; xp = x[i].copy()
            for j in (i, d):
                xj = rng.poisson(xp*P["Mmol"])/P["Mmol"] + 0.0  # small-number noise (Vasas-type)
                if P["heredity"] == "off": xj = xj[rng.permutation(4)]   # chemistry intact, core state randomized
                x[j] = xj
            birth_id[i] = birth_id[d] = idp
            if inw: fis += 1
        if inw and st % int(1/dt) == 0:
            idn = ident(x); freq.append([np.mean(idn == k) for k in range(4)]); excl.append(np.mean(idn >= 0))
    pa = np.array(pairs) if pairs else np.zeros((0, 2), int); f = np.mean(freq, 0)
    sw = float(np.mean(pa[(pa[:, 0] >= 0) & (pa[:, 1] >= 0), 0] != pa[(pa[:, 0] >= 0) & (pa[:, 1] >= 0), 1])) if len(pa) else float("nan")
    return dict(reader=float(f[1]), hedger=float(f[0]), plain=float(f[2] + f[3]), excl=float(np.mean(excl)),
                kappa=kappa(pa[:, 0], pa[:, 1]) if len(pa) else float("nan"), switch=sw, growth=fis/ctime,
                D_at_toxin=float(np.mean(Dpre)) if Dpre else float("nan"), first_reader=first, n_pairs=len(pa))
if __name__ == "__main__":
    import time; t0 = time.time(); P = dict(BASE); P["T"] = 600.0
    print({k: round(v, 3) for k, v in run(P, 999).items()}, round(time.time() - t0, 1), "s")
