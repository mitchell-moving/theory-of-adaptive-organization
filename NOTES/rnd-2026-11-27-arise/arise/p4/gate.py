"""P4 GATE (pilot seeds 101-105; test seeds will be 401-405). Designed anticipator lineage (A2 core) vs designed
non-reader lineage (A1 core), 100 v 100, heredity on, cued world. Pass: anticipator lineage frequency >= 0.75 in >= 4/5."""
import itertools, json, numpy as np
from multiprocessing import Pool
import p4_sim as m
GRID = list(itertools.product([0.1, 0.3], [20.0, 60.0], [0.0, 0.2]))
def init_state(kind, n):
    x = np.zeros((n, m.S)); a, b = (2, 3) if kind == "reader" else (0, 1)
    x[:, a] = x[:, b] = 45.0; x[:, 4:8] = 2.5; return x
def one(a):
    d, Pp, c, seed = a
    P = dict(m.BASE); P.update(delta=d, P=Pp, c=c, T=1000.0)
    init = np.r_[init_state("reader", 100), init_state("non", 100)]; lab = np.r_[np.ones(100, int), np.zeros(100, int)]
    r = m.run(P, seed, init=init, labels=lab); return (d, Pp, c, seed, r["label_freq"])
if __name__ == "__main__":
    jobs = [(d, Pp, c, s) for (d, Pp, c) in GRID for s in [101, 102, 103, 104, 105]]
    with Pool(8) as pool: out = pool.map(one, jobs)
    passing = []
    for (d, Pp, c) in GRID:
        fr = [o[4] for o in out if o[:3] == (d, Pp, c)]; n = sum(f >= 0.75 for f in fr)
        print(f"delta={d} P={Pp} c={c} | anticipator freq {[round(f,2) for f in fr]} | {n}/5 | {'PASS' if n >= 4 else '-'}")
        if n >= 4: passing.append((-c, d, Pp))
    if passing:
        c, d, Pp = sorted(passing)[0]; print("CHOSEN (largest c, then smallest delta, then smallest P):", dict(delta=d, P=Pp, c=-c))
    else: print("NO WORLD PASSES THE GATE")
