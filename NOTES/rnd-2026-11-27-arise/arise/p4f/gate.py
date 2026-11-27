"""P4f gate: ALL lags 0..15 (theta 0.3) vs zero-read, 100 v 100, mu 0, heredity on, cued, T 1500, pilot seeds 101-105.
Pass lag if freq >= 0.75 in >= 4/5. L_inf = passing lags. Validity at best lag: random cue <= 2/5."""
import numpy as np
from multiprocessing import Pool
import p4f_model as m
LAGS = list(range(16))
def one(a):
    l, s, mode = a; P = dict(m.BASE); P.update(mu=0.0, T=1500.0, cue_mode=mode)
    lag0 = np.r_[np.full(100, l), np.full(100, -1)]; th0 = np.r_[np.full(100, 0.3), np.zeros(100)]
    return a, m.run(P, s, init=(lag0, th0))["hist_final"][l + 2]
if __name__ == "__main__":
    with Pool(8) as p:
        out = p.map(one, [(l, s, "cued") for l in LAGS for s in range(101, 106)]); Linf = []; mean = {}
        for l in LAGS:
            fr = [f for (a, f) in out if a[0] == l]; n = sum(f >= 0.75 for f in fr); mean[l] = np.mean(fr)
            print(f"lag {l}: {[round(f,2) for f in fr]} {n}/5 {'PASS' if n >= 4 else '-'}")
            if n >= 4: Linf.append(l)
        if not Linf: print("NO LAG PAYS"); raise SystemExit
        b = max(Linf, key=lambda l: mean[l]); rc = p.map(one, [(b, s, "random") for s in range(101, 106)]); nc = sum(f >= 0.75 for (a, f) in rc)
        print("L_inf =", Linf, "| validity lag", b, [round(f, 2) for (a, f) in rc], f"{nc}/5", "VALID" if nc <= 2 else "INVALID")
