"""P4-DRIFT locked test: does the novelty band move with world drift? Model drift_model.py. LS = (4, 11). T 6000, c_nat 0.01, zero-read start.
ON: drift r in {0, 1/1000, 1/100} x 11 mu x 24 seeds (1601-1624). Controls at r = 1/100: OFF and RANDOM, 8 seeds (1601-1608) x 11 mu."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import drift_model as m
MUS = [3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]; X = np.log10(MUS)
RS = [0.0, 1/1000, 1/100]; SEEDS = list(range(1601, 1625)); SEEDS_CTL = list(range(1601, 1609)); TIE = 0.95; NB = 2000
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}}
def one(a):
    r, mu, arm, s = a; P = dict(m.BASE); P.update(ARMS[arm]); P.update(mu=mu, LS=(4, 11), drift=r); x = m.run(P, s); hf = x["hist_final"]
    return a, dict(A=x["A"], growth=x["growth"], eff=x["eff_final"], reader_share=float(sum(hf[2:])),
                   share_0to4=float(sum(hf[l + 2] for l in range(0, 5))), share_7to11=float(sum(hf[l + 2] for l in range(7, 12))))
def holm(ps, alpha=0.05):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); rej = [False]*len(ps)
    for k, i in enumerate(order):
        if ps[i] <= alpha/(len(ps) - k): rej[i] = True
        else: break
    return rej
def centroid(means):
    w = np.clip(np.asarray(means), 0, None); return float((w*X).sum()/w.sum()) if w.sum() > 0 else None
def edges(means):
    v = np.asarray(means); h = 0.5*v.max(); lo = hi = None
    for i in range(len(v) - 1):
        if lo is None and v[i] < h <= v[i + 1]: lo = X[i] + (h - v[i])/(v[i + 1] - v[i])*(X[i + 1] - X[i])
        if v[i] >= h > v[i + 1]: hi = X[i] + (v[i] - h)/(v[i] - v[i + 1])*(X[i + 1] - X[i])
    return lo, hi
def peak(med):
    med = np.asarray(med); mx = med.max()
    if not mx > 0: return None, None, []
    top = [i for i in range(len(med)) if med[i] >= TIE*mx]; loc = float(np.mean(X[top])); gi = min(top, key=lambda i: (abs(X[i] - loc), i))
    return loc, gi, top
if __name__ == "__main__":
    jobs = [(r, mu, "ON", s) for r in RS for mu in MUS for s in SEEDS] + [(RS[2], mu, a, s) for mu in MUS for a in ("OFF", "RANDOM") for s in SEEDS_CTL]
    with Pool(8) as p: out = p.map(one, jobs)
    json.dump([{"r": k[0], "mu": k[1], "arm": k[2], "seed": k[3], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda r, mu, a, f: np.array([v[f] for (k, v) in out if k[0] == r and k[1] == mu and k[2] == a])
    M = {r: np.array([g(r, mu, "ON", "A") for mu in MUS]) for r in RS}
    for r in RS:
        print(f"--- drift r={r:.4g}")
        for i, mu in enumerate(MUS):
            print(f"mu={mu:g} | mean A {M[r][i].mean():.4f} median {np.median(M[r][i]):.4f} | share lags 0-4 {g(r,mu,'ON','share_0to4').mean():.3f} 7-11 {g(r,mu,'ON','share_7to11').mean():.3f} | growth {g(r,mu,'ON','growth').mean():.4f}")
    for mu in MUS: print(f"controls r=0.01 mu={mu:g}: median A OFF {np.median(g(RS[2],mu,'OFF','A')):.4f} RANDOM {np.median(g(RS[2],mu,'RANDOM','A')):.4f}")
    C = {r: centroid(M[r].mean(1)) for r in RS}; E = {r: edges(M[r].mean(1)) for r in RS}; PK = {r: peak(np.median(M[r], 1)) for r in RS}
    for r in RS: print(f"r={r:.4g}: centroid {C[r]:.3f} | edges low {E[r][0]} high {E[r][1]} | tie-rule peak loc {PK[r][0]} top set {[MUS[i] for i in PK[r][2]]}")
    rng = np.random.default_rng(0); dc, dl, dh = [], [], []
    for _ in range(NB):
        B = {r: np.array([row[rng.integers(0, len(row), len(row))] for row in M[r]]).mean(1) for r in (RS[0], RS[2])}
        c0, c2 = centroid(B[RS[0]]), centroid(B[RS[2]]); e0, e2 = edges(B[RS[0]]), edges(B[RS[2]])
        if None not in (c0, c2): dc.append(c2 - c0)
        if None not in (e0[0], e2[0]): dl.append(e2[0] - e0[0])
        if None not in (e0[1], e2[1]): dh.append(e2[1] - e0[1])
    q = lambda v: np.percentile(v, [2.5, 97.5]) if v else (np.nan, np.nan)
    Dc = C[RS[2]] - C[RS[0]]; cc = q(dc)
    D1 = Dc >= 0.25 and cc[0] > 0; D1m = C[RS[0]] < C[RS[1]] < C[RS[2]]
    print(f"D1 centroid shift fast-static {Dc:.3f} (boot 95% {cc[0]:.3f}..{cc[1]:.3f}; {len(dc)}/{NB}) ->", "PASS" if D1 else "FAIL")
    print(f"D1m monotone centroid {C[RS[0]]:.3f} < {C[RS[1]]:.3f} < {C[RS[2]]:.3f} ->", "PASS" if D1m else "FAIL")
    if None in (E[RS[0]][0], E[RS[2]][0]): print("D2 low edge missing -> FAIL"); D2 = False
    else:
        Dl = E[RS[2]][0] - E[RS[0]][0]; cl = q(dl); D2 = Dl > 0 and cl[0] > 0
        print(f"D2 low-edge shift {Dl:.3f} (boot 95% {cl[0]:.3f}..{cl[1]:.3f}; {len(dl)}/{NB}) ->", "PASS" if D2 else "FAIL")
    if None in (E[RS[0]][1], E[RS[2]][1]): print("D3 high edge missing -> FAIL"); D3 = False
    else:
        Dh = E[RS[2]][1] - E[RS[0]][1]; ch = q(dh); D3 = abs(Dh) < 0.25
        print(f"D3 high-edge shift {Dh:.3f} (boot 95% {ch[0]:.3f}..{ch[1]:.3f}; {len(dh)}/{NB}) ->", "PASS" if D3 else "FAIL")
    loc, gi, top = PK[RS[2]]; pk = MUS[gi]; Aon = g(RS[2], pk, "ON", "A"); med2 = np.median(M[RS[2]], 1)
    tests = [("D4a fast peak > lowest mu", mannwhitneyu(Aon, M[RS[2]][0], alternative="greater").pvalue),
             ("D4b fast peak > highest mu", mannwhitneyu(Aon, M[RS[2]][-1], alternative="greater").pvalue),
             ("C1 ON > OFF at fast peak", mannwhitneyu(Aon, g(RS[2], pk, "OFF", "A"), alternative="greater").pvalue),
             ("C2 ON > RANDOM at fast peak", mannwhitneyu(Aon, g(RS[2], pk, "RANDOM", "A"), alternative="greater").pvalue)]
    rej = holm([t[1] for t in tests]); R = {}
    for (n, pv), rj in zip(tests, rej): R[n] = rj; print(f"  {n}: p={pv:.4g} Holm-reject={rj}")
    D4 = 0 not in top and len(MUS) - 1 not in top and R["D4a fast peak > lowest mu"] and R["D4b fast peak > highest mu"] and med2[0] <= 0.5*med2[gi] and med2[-1] <= 0.5*med2[gi]
    print(f"D4 two-sided band at fast drift (peak grid mu {pk:g}; end medians {med2[0]:.4f}, {med2[-1]:.4f} vs {med2[gi]:.4f}) ->", "PASS" if D4 else "FAIL")
    C12 = R["C1 ON > OFF at fast peak"] and R["C2 ON > RANDOM at fast peak"]; print("C1+C2 ->", "PASS" if C12 else "FAIL")
    print("PRIMARY (D1):", "PASS" if D1 else "FAIL", "| ALL (D1, D1m, D2, D3, D4, C1+C2):", "PASS" if all([D1, D1m, D2, D3, D4, C12]) else "FAIL")
