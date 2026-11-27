"""P4-lite: compartmentalized autocatalytic cores in a drifting food supply (Vasas-2012-type toy chemistry).
Planted cores (disclosed design): A1 = {0,1}, A2 = {2,3} both eat food A; B1 = {4,5}, B2 = {6,7} eat food B.
The only difference between A1 and A2: species 2 can also catalyze synthesis of 4 (a B1 member) from food A
while a cue molecule is present ("reading" the cue), diverting a fraction theta of its catalysis and paying an
optional price c (extra decay of 2 per unit cue). Species 8..S-1: random catalysis (side reactions, parasites).
Variation: rare uncatalyzed synthesis eps of every species from its food. Fitness: compartment fission when total
amount reaches 2M (growth only); a daughter replaces a uniformly random compartment (Moran). No term rewards
anticipation or heredity."""
import numpy as np
S = 24
BASE = dict(dt=0.05, M=100.0, Nc=200, k=1.0, delta=0.1, eps=1e-3, theta=0.3, kq=1.0, c=0.0,
            P=40.0, Lc=8.0, cue_mode="cued", heredity="on", reader=True, hedge=False, T=3000.0, window=0.5)

def network(rng):
    C = np.zeros((S, S)); food = np.zeros(S, int)  # food 0 = A, 1 = B
    for a, b, f in [(0, 1, 0), (2, 3, 0), (4, 5, 1), (6, 7, 1)]:
        C[a, b] = C[b, a] = 1.0; food[a] = food[b] = f
    for i in range(8, S):
        C[i, rng.integers(0, S)] = rng.uniform(0.2, 0.9); food[i] = rng.integers(0, 2)
    return C, food

def schedule(P, T, rng, Lc, mode):
    """phase list: alternating A/B with jittered lengths; cue on in the last Lc of each A phase (cued),
    or at random times with the same duty (random)."""
    t = 0.0; ph = 0; edges = []
    while t < T:
        L = rng.uniform(0.5*P, 1.5*P); edges.append((t, t + L, ph)); t += L; ph = 1 - ph
    return edges

def run(P, seed, init=None, labels=None):
    rng = np.random.default_rng(seed); wrng = np.random.default_rng(50_000 + seed)
    C, food = network(np.random.default_rng(7))          # one fixed chemistry for every run
    N = P["Nc"]; dt = P["dt"]; nst = int(P["T"]/dt)
    edges = schedule(P["P"], P["T"] + 5*P["P"], wrng, P["Lc"], P["cue_mode"])
    phase = np.zeros(nst + 1, int); cue = np.zeros(nst + 1)
    for (a, b, ph) in edges:
        i0, i1 = int(a/dt), min(int(b/dt), nst + 1); phase[i0:i1] = ph
        if ph == 0: cue[max(i0, int((b - P["Lc"])/dt)):i1] = 1.0
    switchAB = [b for (a, b, ph) in edges if ph == 0 and b < P["T"]]
    if P["cue_mode"] == "random":   # same number and length of cue windows, onsets uniform in time, uncorrelated with switches
        L = int(P["Lc"]/dt); cnt = int(round(cue.sum()/max(L, 1))); cue = np.zeros(nst + 1)
        for o in wrng.integers(0, nst + 1 - L, cnt): cue[o:o + L] = 1.0
    if init is None:
        n = rng.dirichlet(np.ones(S), N)*P["M"]
    else:
        n = init.copy()
    lab = np.zeros(N, int) if labels is None else labels.copy()
    parent_vec = np.full((N, 5), np.nan)
    def cores(n):
        tot = n.sum(1, keepdims=True)
        return np.c_[n[:, 0:2].sum(1), n[:, 2:4].sum(1), n[:, 4:6].sum(1), n[:, 6:8].sum(1), n[:, 8:].sum(1)]/tot
    kq = P["kq"] if P["reader"] else 0.0
    t_win = P["T"]*(1 - P["window"]); fis = 0; ctime = 0.0; Hs, Hr = [], []
    AIrec = {}; rf = []
    sw_idx = {int(round(s/dt)): s for s in switchAB}; cue_idx = {int(round((s - P["Lc"])/dt)): s for s in switchAB}
    for st in range(nst):
        F = np.array([1.0, 0.0]) if phase[st] == 0 else np.array([0.0, 1.0]); q = cue[st]
        Fi = F[food]
        cat = n @ C.T                                   # catalytic drive for each species
        cat[:, 3] -= q*P["theta"]*n[:, 2]*C[3, 2]       # diversion of species 2's catalysis while reading
        hq = (P["Lc"]/P["P"])*F[0] if P["hedge"] else 0.0  # hedger (A1 core): same mean B1 flux, untimed, unpriced
        cat[:, 1] -= hq*P["theta"]*n[:, 0]*C[1, 0]
        syn = P["k"]*cat*Fi + P["eps"]*Fi
        syn[:, 4] += hq*P["theta"]*n[:, 0]*F[0]
        syn[:, 4] += q*kq*P["theta"]*n[:, 2]*F[0]       # cue-read synthesis of B1 member from food A
        dec = P["delta"]*n; dec[:, 2] += P["c"]*q*n[:, 2]
        n = np.maximum(n + (syn - dec)*dt, 0.0)
        t = st*dt; inw = t >= t_win
        if inw: ctime += N*dt
        if st in cue_idx and inw: AIrec.setdefault(cue_idx[st], [None, None])[0] = cores(n)[:, 2:4].sum(1).mean()
        if st in sw_idx and inw: AIrec.setdefault(sw_idx[st], [None, None])[1] = cores(n)[:, 2:4].sum(1).mean()
        tot = n.sum(1)
        for i in np.flatnonzero(tot >= 2*P["M"]):
            cv = cores(n[i:i+1])[0]
            if inw and not np.isnan(parent_vec[i, 0]):
                j = rng.integers(0, N); cj = cores(n[j:j+1])[0]
                cs = lambda a, b: float(a@b/np.linalg.norm(a)/np.linalg.norm(b))
                Hs.append(cs(cv, parent_vec[i])); Hr.append(cs(cv, cj))
            d = rng.integers(0, N - 1); d = d + (d >= i)
            if P["heredity"] == "on":
                u = np.clip(rng.normal(0.5, 0.5/np.sqrt(n[i] + 1.0)), 0, 1)
                n[d] = n[i]*u; n[i] = n[i]*(1 - u); lab[d] = lab[i]
            else:
                half = tot[i]/2
                n[d] = rng.dirichlet(np.ones(S))*half; n[i] = rng.dirichlet(np.ones(S))*half; lab[d] = lab[i]
            parent_vec[i] = cv; parent_vec[d] = cv
            if inw: fis += 1
        if inw and st % int(1/dt) == 0:
            cvs = cores(n); rf.append(np.mean(cvs[:, 1] > cvs[:, 0]))
    ai = [b - a for (a, b) in AIrec.values() if a is not None and b is not None]
    return dict(reader_freq=float(np.mean(rf)), AI=float(np.mean(ai)) if ai else float("nan"), n_switch=len(ai),
                H=float(np.mean(Hs) - np.mean(Hr)) if Hs else float("nan"), H_parent=float(np.mean(Hs)) if Hs else float("nan"),
                growth=fis/ctime, label_freq=float(np.mean(lab == 1)))
