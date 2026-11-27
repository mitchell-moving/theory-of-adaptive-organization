"""P4-CLOSE locked test: does the novelty window close as world drift rises? Model drift_model.py (unchanged from P4-DRIFT). LS = (4, 11), T 6000.
ON: r in {1/100, 1/30, 1/10} x 11 mu x 16 seeds (1701-1716). Control: RANDOM cue at r = 1/10, 8 seeds (1701-1708) x 11 mu."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import drift_model as m
MUS = [3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]; X = np.log10(MUS)
RS = [1/100, 1/30, 1/10]; SEEDS = list(range(1701, 1717)); SEEDS_CTL = list(range(1701, 1709)); NB = 2000; CLOSED = 0.005
def one(a):
    r, mu, arm, s = a; P = dict(m.BASE); P.update(mu=mu, LS=(4, 11), drift=r)
    if arm == "RANDOM": P["cue_mode"] = "random"
    x = m.run(P, s); hf = x["hist_final"]
    return a, dict(A=x["A"], growth=x["growth"], share_0to4=float(sum(hf[l + 2] for l in range(5))), share_7to11=float(sum(hf[l + 2] for l in range(7, 12))))
def edges(means):
    v = np.asarray(means); h = 0.5*v.max(); lo = hi = None
    for i in range(len(v) - 1):
        if lo is None and v[i] < h <= v[i + 1]: lo = X[i] + (h - v[i])/(v[i + 1] - v[i])*(X[i + 1] - X[i])
        if v[i] >= h > v[i + 1]: hi = X[i] + (v[i] - h)/(v[i] - v[i + 1])*(X[i + 1] - X[i])
    return lo, hi
def width(means):
    """Registered: 0 if max mean A < CLOSED (window closed); else high - low; None if an edge is missing."""
    if np.max(means) < CLOSED: return 0.0
    lo, hi = edges(means); return None if None in (lo, hi) else hi - lo
if __name__ == "__main__":
    jobs = [(r, mu, "ON", s) for r in RS for mu in MUS for s in SEEDS] + [(RS[2], mu, "RANDOM", s) for mu in MUS for s in SEEDS_CTL]
    with Pool(8) as p: out = p.map(one, jobs)
    json.dump([{"r": k[0], "mu": k[1], "arm": k[2], "seed": k[3], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda r, mu, a, f: np.array([v[f] for (k, v) in out if k[0] == r and k[1] == mu and k[2] == a])
    M = {r: np.array([g(r, mu, "ON", "A") for mu in MUS]) for r in RS}
    for r in RS:
        print(f"--- drift r={r:.4g}")
        for i, mu in enumerate(MUS):
            print(f"mu={mu:g} | mean A {M[r][i].mean():.4f} median {np.median(M[r][i]):.4f} | lags 0-4 {g(r,mu,'ON','share_0to4').mean():.3f} 7-11 {g(r,mu,'ON','share_7to11').mean():.3f} | growth {g(r,mu,'ON','growth').mean():.4f} | RANDOM median A {np.median(g(r,mu,'RANDOM','A')) if r == RS[2] else float('nan'):.4f}")
    W = {r: width(M[r].mean(1)) for r in RS}; E = {r: edges(M[r].mean(1)) for r in RS}
    for r in RS: print(f"r={r:.4g}: max mean A {M[r].mean(1).max():.4f} | edges {E[r]} | width {W[r]}")
    w10 = W[RS[2]]; K1 = w10 is not None and w10 < 1.5
    print(f"K1 window closes or narrows below 1.5 decades at r 1/10 (width {w10}) ->", "PASS" if K1 else "FAIL")
    K2 = None not in W.values() and W[RS[0]] > W[RS[1]] >= W[RS[2]]; print(f"K2 monotone narrowing (w1 > w2 >= w3) {[W[r] for r in RS]} ->", "PASS" if K2 else "FAIL")
    rng = np.random.default_rng(0); dl = []
    for _ in range(NB):
        a = edges(np.array([row[rng.integers(0, len(row), len(row))] for row in M[RS[0]]]).mean(1))[0]
        b = edges(np.array([row[rng.integers(0, len(row), len(row))] for row in M[RS[2]]]).mean(1))[0]
        if None not in (a, b): dl.append(b - a)
    if None in (E[RS[0]][0], E[RS[2]][0]) or not dl: print("K3 low edge missing -> FAIL"); K3 = False
    else:
        D = E[RS[2]][0] - E[RS[0]][0]; c = np.percentile(dl, [2.5, 97.5]); K3 = D > 0 and c[0] > 0
        print(f"K3 low-edge shift 1/10 vs 1/100 {D:.3f} (boot 95% {c[0]:.3f}..{c[1]:.3f}; {len(dl)}/{NB}) ->", "PASS" if K3 else "FAIL")
    K4 = W[RS[0]] is not None and abs(W[RS[0]] - 2.30) <= 0.5; print(f"K4 replication of P4-DRIFT width at r 1/100 (2.30 +- 0.5): {W[RS[0]]} ->", "PASS" if K4 else "FAIL")
    i = int(np.argmax(M[RS[2]].mean(1))); pv = mannwhitneyu(M[RS[2]][i], g(RS[2], MUS[i], "RANDOM", "A"), alternative="greater").pvalue
    print(f"C ON > RANDOM at r 1/10, mu {MUS[i]:g}: p={pv:.4g} ->", "PASS" if pv < 0.05 else "FAIL")
    print("PRIMARY K1:", "PASS" if K1 else "FAIL")
