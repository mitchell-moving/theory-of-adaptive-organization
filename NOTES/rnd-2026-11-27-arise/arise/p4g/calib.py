"""P4g calibration (designed contest, no evolution): lag-4 reader (theta 0.3) vs zero-read, 100 v 100, mu 0, T 1500, pilot seeds 101-105,
across prices. pass_frac(c) = share of seeds with reader freq >= 0.75. c*_designed = log-interpolated c where pass_frac crosses 0.5."""
import numpy as np
from multiprocessing import Pool
import p4g_model as m
CS = [0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0]
def one(a):
    c, s = a; P = dict(m.BASE); P.update(mu=0.0, T=1500.0, cnat=c)
    lag0 = np.r_[np.full(100, 4), np.full(100, -1)]; th0 = np.r_[np.full(100, 0.3), np.zeros(100)]
    return a, m.run(P, s, init=(lag0, th0))["hist_final"][4 + 2]
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(c, s) for c in CS for s in range(101, 106)])
    pf = []
    for c in CS:
        fr = [f for (a, f) in out if a[0] == c]; pf.append(np.mean([f >= 0.75 for f in fr])); print(f"c={c}: {[round(f,2) for f in fr]} pass_frac {pf[-1]:.1f}")
    cs = None
    for i in range(len(CS) - 1):
        if pf[i] >= 0.5 > pf[i + 1]:
            x0, x1 = np.log(CS[i]), np.log(CS[i + 1]); cs = float(np.exp(x0 + (pf[i] - 0.5)/(pf[i] - pf[i + 1])*(x1 - x0))); break
    print("c*_designed =", cs)
