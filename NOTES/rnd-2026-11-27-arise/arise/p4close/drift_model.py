"""P4-DRIFT model = P4f/P4-BAND model with a drifting cue-to-toxin lag (see schedule). P4f (= P4e + non-saturating anticipation measure A = mean pop. detox at toxin onsets minus mean detox, last 50%). P4e text: OPEN-ENDED cores. Each compartment has S=4 slots; each slot holds a core with inherited parameters
(lag in {-1 = no read, 0..15}, read strength theta in [0, 0.6]). Slots compete Lotka-Volterra (beta). Nucleation at rate mu
per compartment-time puts ONE molecule (1/M) of a NEW core with random (lag, theta) into the emptiest slot. No reader is written in.
A cue pulse (length 1) precedes each toxin onset by Lstar; a core with lag l diverts theta of its synthesis to detox D during
[l, l+w) after the last cue onset. Price per nat (linear proxy): c_nat * (theta/0.6) * h(duty), duty = fraction of time a reader acts.
Fitness = compartment volume growth only."""
import numpy as np
BASE = dict(dt=0.05, Nc=200, S=4, r=1.0, K=1.0, beta=1.5, delta=0.05, tau=3.0, Dk=0.05, dD=1.0, gamma=0.1, P=40.0, Lt=5.0,
            Lstar=6.0, w=4.0, cnat=0.01, Mmol=20.0, mu=1e-3, cue_mode="cued", heredity="on", T=6000.0, window=0.5, maxlag=15)
def hb(p): return 0.0 if p <= 0 or p >= 1 else float(-p*np.log(p) - (1-p)*np.log(1-p))
def mi_binary(a, b):
    a = a.astype(bool); b = b.astype(bool); I = 0.0
    for u in (0, 1):
        for v in (0, 1):
            pj = np.mean((a == u) & (b == v)); pa = np.mean(a == u); pb = np.mean(b == v)
            if pj > 0: I += pj*np.log(pj/(pa*pb))
    return float(I)
def schedule(P, nst, wrng):
    dt = P["dt"]; tox = np.zeros(nst + 1, bool); onsets = []; t = 0.0
    while True:
        t += wrng.uniform(0.5, 1.5)*P["P"]; i0 = int(t/dt)
        if i0 >= nst: break
        tox[i0:i0 + int(P["Lt"]/dt)] = True; onsets.append(i0)
    if P["cue_mode"] == "cued":
        # DRIFT (P4-DRIFT): the cue-to-toxin lag switches between two regimes LS = (LA, LB) as a Poisson process of rate
        # P["drift"] per unit time, checked at each onset; the starting regime is random per seed (world rng). drift 0 = static.
        LS = P.get("LS", (P["Lstar"],)); reg = int(wrng.integers(0, len(LS))); cues = []; prev = 0.0
        for o in onsets:
            tt = o*dt
            if P.get("drift", 0.0) > 0 and wrng.random() < 1 - np.exp(-P["drift"]*(tt - prev)): reg = (reg + 1) % len(LS)
            prev = tt; cues.append(max(0, o - int(LS[reg]/dt)))
    elif P["cue_mode"] == "random": cues = sorted(wrng.integers(0, nst, len(onsets)).tolist())
    else: cues = []
    since = np.full(nst + 1, 1e9); last = None; cs = set(cues)
    for st in range(nst + 1):
        if st in cs: last = st
        if last is not None: since[st] = (st - last)*dt
    return tox, since, len(cues)
def run(P, seed, init=None):
    rng = np.random.default_rng(seed); wrng = np.random.default_rng(90_000 + seed)
    N, S, dt = P["Nc"], P["S"], P["dt"]; nst = int(P["T"]/dt); tox, since, ncue = schedule(P, nst, wrng)
    hd = hb(min(ncue*P["w"]/P["T"], 0.999))
    x = np.zeros((N, S)); lag = np.full((N, S), -1); th = np.zeros((N, S)); x[:, 0] = 0.9
    if init is not None: lag[:, 0], th[:, 0] = init
    D = np.zeros(N); V = rng.uniform(1, 2, N); t_win = int(nst*(1 - P["window"])); fis = 0; ctime = 0.0
    Dser = np.zeros(nst + 1); hist = []; eff = []; snap = int(100/dt)
    for st in range(nst):
        act = (lag >= 0) & (since[st] >= lag) & (since[st] < lag + P["w"])
        div = th*act; price = np.where(lag >= 0, P["cnat"]*(th/0.6)*hd, 0.0)
        tot = x.sum(1, keepdims=True); comp = 1 - (P["beta"]*tot - (P["beta"] - 1)*x)/P["K"]
        syn = P["r"]*x*np.maximum(comp, -1.0); prod = np.maximum(syn, 0.0)
        dec = (P["delta"] + P["tau"]*tox[st]/(1 + D/P["Dk"]))[:, None]*x + price*x
        x = np.maximum(x + (syn*(1 - div) - dec)*dt, 0.0)
        D = D + ((prod*div).sum(1) - P["dD"]*D)*dt; Dser[st] = D.mean()
        V = V*(1 + P["gamma"]*x.sum(1)/P["K"]*dt)
        nuc = np.flatnonzero(rng.random(N) < P["mu"]*dt)
        for i in nuc:
            k = int(np.argmin(x[i])); x[i, k] = 1.0/P["Mmol"]; lag[i, k] = rng.integers(-1, P["maxlag"] + 1); th[i, k] = rng.uniform(0, 0.6)
        inw = st >= t_win
        if inw: ctime += N*dt
        for i in np.flatnonzero(V >= 2):
            d = rng.integers(0, N - 1); d = d + (d >= i); V[i] = V[d] = 1.0
            srcs = (i, i) if P["heredity"] == "on" else tuple(rng.integers(0, N, 2))   # off: contents of random compartments
            xs = [x[s].copy() for s in srcs]; ls = [lag[s].copy() for s in srcs]; ts = [th[s].copy() for s in srcs]; Ds = [D[s] for s in srcs]
            for j, (xx, ll, tt, dd) in zip((i, d), zip(xs, ls, ts, Ds)):
                x[j] = rng.poisson(xx*P["Mmol"])/P["Mmol"]; lag[j] = ll; th[j] = tt; D[j] = dd
            if inw: fis += 1
        if st % snap == 0:
            tot = x.sum(1); k = x.argmax(1); share = x[np.arange(N), k]/np.maximum(tot, 1e-12); ok = share >= 0.8
            ld = np.where(ok, lag[np.arange(N), k], -2)                    # -2 = mixed/empty
            hist.append(np.bincount(ld + 2, minlength=P["maxlag"] + 3)); eff.append(float(np.mean(np.where(ok & (ld >= 0), th[np.arange(N), k], 0.0))))
    win = int(600/dt); MI = []
    for a in range(0, nst - win + 1, win):
        Dw = Dser[a:a + win:20]; Tw = tox[a:a + win:20]; MI.append(mi_binary(Tw, Dw > np.median(Dw)) if Dw.max() > 0 else 0.0)
    on_idx = np.flatnonzero(np.diff(tox.astype(int)) == 1) + 1; on_idx = on_idx[(on_idx >= t_win) & (on_idx < nst)]
    A = float(Dser[on_idx].mean() - Dser[t_win:nst].mean()) if len(on_idx) else float("nan")
    H = np.array(hist); half = len(H)//2
    return dict(A=A, MI=MI, hist=H.tolist(), eff=eff, growth=fis/ctime, eff_final=float(np.mean(eff[half:])),
                hist_final=(H[half:].sum(0)/H[half:].sum()).tolist())
if __name__ == "__main__":
    import time; t0 = time.time(); P = dict(BASE); P["T"] = 600.0
    r = run(P, 999); print("MI", [round(v, 3) for v in r["MI"]], "eff", round(r["eff_final"], 3), "growth", round(r["growth"], 4), round(time.time() - t0, 1), "s")
