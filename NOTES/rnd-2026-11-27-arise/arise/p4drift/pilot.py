"""P4-DRIFT PILOT (range/compute only; not evidence). Pilot seeds 1391-1394, never used in the locked test. mu fixed at 1e-3 only.
Checks: (a) each regime LS=(4,) and LS=(11,) is learnable statically (mean A > 0.005);
(b) manipulation strength vs drift rate r in {1/3000, 1/1000, 1/300, 1/100} with LS=(4, 11).
Pre-stated choice rule: r_fast = the largest r with mean A(r)/mean A(static, LS=(4,11), r=0) in [0.3, 0.8]; r_slow = r_fast/10 (rounded to the list
1/3000, 1/1000, 1/300 if it falls there, else exactly r_fast/10). If no r qualifies, change the regime pair before any lock and log it."""
import time
from multiprocessing import Pool
import numpy as np, drift_model as m
def one(a):
    LS, r, s = a; P = dict(m.BASE); P.update(mu=1e-3, LS=LS, drift=r); t0 = time.time(); x = m.run(P, s)
    return LS, r, s, x["A"], round(time.time() - t0, 1)
if __name__ == "__main__":
    S = range(1391, 1395)
    jobs = [((4,), 0.0, s) for s in S] + [((11,), 0.0, s) for s in S] + [((4, 11), r, s) for r in (0.0, 1/3000, 1/1000, 1/300, 1/100) for s in S]
    with Pool(8) as p: out = p.map(one, jobs)
    for row in out: print("pilot LS=%s r=%.5f seed=%d A=%.4f sec=%.1f" % row)
    for LS, r in [((4,), 0.0), ((11,), 0.0)] + [((4, 11), r) for r in (0.0, 1/3000, 1/1000, 1/300, 1/100)]:
        print("mean", LS, round(r, 5), round(np.mean([o[3] for o in out if o[0] == LS and o[1] == r]), 4))
