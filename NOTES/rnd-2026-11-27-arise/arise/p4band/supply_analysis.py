"""P4-BAND-T locked follow-up: does the low edge scale with run length (supply mu*Nc*T) while the high edge stays?
Same model, T 12000 (2x), ON only, fresh seeds 1501-1510, same 12-point grid. Compares with band runs.json (T 6000, ON 20 seeds)."""
import json, numpy as np
from multiprocessing import Pool
import band_model as m
MUS = [1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]; X = np.log10(MUS); SEEDS = list(range(1501, 1511)); NB = 2000
def one(a):
    mu, s = a; P = dict(m.BASE); P.update(mu=mu, T=12000.0); r = m.run(P, s); return a, dict(A=r["A"], growth=r["growth"])
def edges(means):
    """Registered: half = 0.5 * max over grid of mean A_ON. Low edge = first upward crossing of half (log-linear interpolation in log10 mu);
    high edge = last downward crossing. None if absent."""
    v = np.asarray(means); h = 0.5*v.max(); lo = hi = None
    for i in range(len(v) - 1):
        if lo is None and v[i] < h <= v[i + 1]: lo = X[i] + (h - v[i])/(v[i + 1] - v[i])*(X[i + 1] - X[i])
        if v[i] >= h > v[i + 1]: hi = X[i] + (v[i] - h)/(v[i] - v[i + 1])*(X[i + 1] - X[i])
    return lo, hi
if __name__ == "__main__":
    # AMENDMENT: load the runs computed by the locked supply_test.py (saved before its crash) instead of recomputing
    out = [((r["mu"], r["seed"]), dict(A=r["A"], growth=r["growth"])) for r in json.load(open("supply_runs.json"))]
    N = np.array([[v["A"] for (k, v) in out if k[0] == mu] for mu in MUS])
    old = json.load(open("runs.json")); O = np.array([[r["A"] for r in old if r["mu"] == mu and r["arm"] == "ON"] for mu in MUS])
    for i, mu in enumerate(MUS): print(f"mu={mu:g}: mean A T6000 {O[i].mean():.4f} | T12000 {N[i].mean():.4f} (median {np.median(N[i]):.4f}); growth T12000 {np.mean([v['growth'] for (k, v) in out if k[0] == mu]):.4f}")
    lo0, hi0 = edges(O.mean(1)); lo1, hi1 = edges(N.mean(1)); print(f"edges log10 mu: T6000 low {lo0} high {hi0} | T12000 low {lo1} high {hi1}")
    rng = np.random.default_rng(0); dl, dh = [], []
    for _ in range(NB):
        a = edges(np.array([r[rng.integers(0, len(r), len(r))] for r in O]).mean(1)); b = edges(np.array([r[rng.integers(0, len(r), len(r))] for r in N]).mean(1))
        if None not in (a[0], b[0]): dl.append(b[0] - a[0])
        if None not in (a[1], b[1]): dh.append(b[1] - a[1])
    if None in (lo0, hi0, lo1, hi1): print("an edge is missing -> S1 FAIL, S2 FAIL"); raise SystemExit
    Dl, Dh = lo1 - lo0, hi1 - hi0; cl = np.percentile(dl, [2.5, 97.5]); ch = np.percentile(dh, [2.5, 97.5])
    print(f"S1 low-edge shift {Dl:.3f} (boot 95% {cl[0]:.3f}..{cl[1]:.3f}; {len(dl)}/{NB}); supply-limit expectation -0.301 ->", "PASS" if Dl <= -0.15 and cl[1] < 0 else "FAIL")
    print(f"S2 high-edge shift {Dh:.3f} (boot 95% {ch[0]:.3f}..{ch[1]:.3f}; {len(dh)}/{NB}) ->", "PASS" if abs(Dh) < 0.15 else "FAIL")
