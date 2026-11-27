"""PILOT (timing/range only, not evidence). Pilot seeds 1391-1392; these seeds are never used in the locked test."""
import time, sys
from multiprocessing import Pool
import band_model as m
def one(a):
    mu, s = a; P = dict(m.BASE); P.update(mu=mu); t0 = time.time(); r = m.run(P, s)
    return mu, s, r["A"], round(time.time() - t0, 1)
if __name__ == "__main__":
    jobs = [(mu, s) for mu in (1e-6, 1e-3, 3e-1) for s in (1391, 1392)] + [(1.0, 1391), (1.0, 1392)]
    with Pool(8) as p:
        for row in p.map(one, jobs): print("pilot mu=%g seed=%d A=%.4f sec=%.1f" % row)
