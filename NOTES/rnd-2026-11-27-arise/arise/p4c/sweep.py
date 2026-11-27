"""P4c pilot sweep (pilot seeds 101-103, T=1500, cued world P=40, cnat=0.01, reader ABSENT at start).
Records ONLY kappa and switch rate (reader/hedger outcomes are not written or printed)."""
import itertools, numpy as np
from multiprocessing import Pool
import p4c_model as m
GRID = list(itertools.product([1.1, 1.5, 3.0], [20.0, 200.0], [1.0, 2.0, 3.0], [0.001, 0.01, 0.1]))  # beta, Mmol, tau, mu
def one(a):
    b, M, t, mu, s = a; P = dict(m.BASE); P.update(beta=b, Mmol=M, tau=t, mu=mu, P=40.0, cnat=0.01, T=1500.0)
    r = m.run(P, s); return a, r["kappa"], r["switch"]
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [g + (s,) for g in GRID for s in (101, 102, 103)])
    rows = []
    with open("sweep.csv", "w") as f:
        f.write("beta,Mmol,tau,mu,kappa_med,switch_med\n")
        for g in GRID:
            k = np.nanmedian([o[1] for o in out if o[0][:4] == g]); sw = np.nanmedian([o[2] for o in out if o[0][:4] == g])
            rows.append((g, k, sw)); f.write(",".join(map(str, g)) + f",{k:.4f},{sw:.5f}\n")
    band = [r for r in rows if r[1] >= 0.5 and r[2] >= 0.002]
    for g, k, sw in rows: print(g, f"kappa {k:.3f} switch {sw:.4f}", "BAND" if (k >= 0.5 and sw >= 0.002) else "")
    order = sorted(band, key=lambda r: (-r[2], -r[1]))
    print("BAND ORDER (descending switch, then kappa):", [r[0] for r in order])
