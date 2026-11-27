"""P4h locked test: does a moderate reading price RAISE anticipation? mu 1e-3, T 6000, zero-read start, fresh seeds 1101-1120."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import p4h_model as m
SEEDS = list(range(1101, 1121)); CS = [0.01, 0.3]
def one(a):
    c, s = a; P = dict(m.BASE); P.update(mu=1e-3, cnat=c); r = m.run(P, s); hf = np.array(r["hist_final"])
    rd = hf[2:]; useless = float(rd.sum() - rd[2:7].sum())     # dominant readers at lags outside 2-6
    return a, dict(A=r["A"], eff=r["eff_final"], useless=useless, f_inf=float(rd[2:7].sum()), growth=r["growth"])
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(c, s) for c in CS for s in SEEDS])
    json.dump([{"c": k[0], "seed": k[1], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda c, f: np.array([v[f] for (k, v) in out if k[0] == c])
    for c in CS: print(f"c={c}: A mean {g(c,'A').mean():.4f} median {np.median(g(c,'A')):.4f} | effort {g(c,'eff').mean():.3f} | useless-lag share {g(c,'useless').mean():.4f} | f_inf {g(c,'f_inf').mean():.3f} | growth {g(c,'growth').mean():.4f}")
    pv = mannwhitneyu(g(0.3, "A"), g(0.01, "A"), alternative="greater").pvalue
    print(f"H1 (A at c 0.3 > A at c 0.01): p={pv:.4g}", "PASS" if pv < 0.05 else "FAIL")
    pv2 = mannwhitneyu(g(0.01, "useless"), g(0.3, "useless"), alternative="greater").pvalue
    print(f"H2 (useless-lag share lower at c 0.3): p={pv2:.4g}", "PASS" if pv2 < 0.05 else "FAIL")
