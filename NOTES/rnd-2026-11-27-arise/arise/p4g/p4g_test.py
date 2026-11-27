"""P4g locked test. Fresh seeds 1001-1010, T 6000, zero-read start, no reader written in.
Part 1 (price cap): mu 1e-3, c in CS. Part 2 (high-novelty side): c 0.01, mu in {1e-2, 3e-2, 1e-1}."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import p4g_model as m
SEEDS = list(range(1001, 1011)); CS = [0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0]; CSTAR_D = 0.6170211155852342
def one(a):
    part, x, s = a; P = dict(m.BASE)
    if part == "cap": P.update(mu=1e-3, cnat=x)
    else: P.update(mu=x, cnat=0.01)
    r = m.run(P, s); return a, dict(eff=r["eff_final"], A=r["A"], f_inf=float(sum(r["hist_final"][l + 2] for l in (2, 3, 4, 5, 6))))
def cross(E, CS):
    half = 0.5*E[0]
    for i in range(len(CS) - 1):
        if E[i] >= half > E[i + 1]:
            x0, x1 = np.log(CS[i]), np.log(CS[i + 1]); return float(np.exp(x0 + (E[i] - half)/(E[i] - E[i + 1])*(x1 - x0)))
    return None
if __name__ == "__main__":
    jobs = [("cap", c, s) for c in CS for s in SEEDS] + [("high", mu, s) for mu in (1e-2, 3e-2, 1e-1) for s in SEEDS]
    with Pool(8) as p: out = p.map(one, jobs)
    json.dump([{"part": k[0], "x": k[1], "seed": k[2], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda part, x, f: np.array([v[f] for (k, v) in out if k[0] == part and k[1] == x])
    E = [g("cap", c, "eff").mean() for c in CS]
    for c, e in zip(CS, E): print(f"c={c}: effort {e:.3f}  f_inf {g('cap', c, 'f_inf').mean():.3f}  A {g('cap', c, 'A').mean():.4f}")
    ce = cross(E, CS); rng = np.random.default_rng(0); boots = []
    M = np.array([g("cap", c, "eff") for c in CS])
    for _ in range(2000):
        idx = rng.integers(0, 10, 10); b = cross(M[:, idx].mean(1).tolist(), CS)
        if b: boots.append(b)
    lo, hi = (np.percentile(boots, [2.5, 97.5]) if boots else (None, None))
    print(f"c*_evolved = {ce}  (bootstrap 95% over seeds: {lo}–{hi}; {len(boots)}/2000 with a crossing); c*_designed = {CSTAR_D:.3f}")
    ok = ce is not None and CSTAR_D/2 <= ce <= 2*CSTAR_D
    print("P-cap (c*_evolved within a factor 2 of c*_designed):", "PASS" if ok else "FAIL")
    for mu in (1e-2, 3e-2, 1e-1): print(f"mu={mu}: A median {np.median(g('high', mu, 'A')):.4f} mean {g('high', mu, 'A').mean():.4f} f_inf {g('high', mu, 'f_inf').mean():.3f} effort {g('high', mu, 'eff').mean():.3f}")
    pv = mannwhitneyu(g("high", 1e-2, "A"), g("high", 1e-1, "A"), alternative="greater").pvalue
    print(f"P-high (A at mu 1e-2 > A at mu 1e-1, one-sided MW): p={pv:.4g}", "PASS" if pv < 0.05 else "FAIL")
