"""P4 GATE v2 (pilot seeds 101-105). Reader lineage (A2 core, cue-timed B1 synthesis, priced) vs HEDGER lineage
(A1 core, same mean B1 flux, untimed, unpriced), 100 v 100, heredity on. Pass in cued world: reader freq >= 0.75 in >= 4/5.
Validity: at the chosen cell, random-cue world must give reader >= 0.75 in <= 2/5."""
import itertools, numpy as np
from multiprocessing import Pool
import p4b_sim as m
GRID = list(itertools.product([0.1, 0.3], [20.0, 60.0], [0.0, 0.2]))
def init_state(kind, n):
    x = np.zeros((n, m.S)); a, b = (2, 3) if kind == "reader" else (0, 1)
    x[:, a] = x[:, b] = 45.0; x[:, 4:8] = 2.5; return x
def one(a):
    d, Pp, c, seed, mode = a
    P = dict(m.BASE); P.update(delta=d, P=Pp, c=c, T=1000.0, hedge=True, cue_mode=mode)
    init = np.r_[init_state("reader", 100), init_state("non", 100)]; lab = np.r_[np.ones(100, int), np.zeros(100, int)]
    return a, m.run(P, seed, init=init, labels=lab)["label_freq"]
if __name__ == "__main__":
    with Pool(8) as pool:
        out = pool.map(one, [(d, Pp, c, s, "cued") for (d, Pp, c) in GRID for s in range(101, 106)])
        passing = []
        for (d, Pp, c) in GRID:
            fr = [f for (a, f) in out if a[:3] == (d, Pp, c)]; n = sum(f >= 0.75 for f in fr)
            print(f"delta={d} P={Pp} c={c} | reader freq {[round(f,2) for f in fr]} | {n}/5 | {'PASS' if n >= 4 else '-'}")
            if n >= 4: passing.append((-c, d, Pp))
        if not passing: print("NO WORLD PASSES THE GATE"); raise SystemExit
        c, d, Pp = sorted(passing)[0]; c = -c; print("CHOSEN:", dict(delta=d, P=Pp, c=c))
        ctl = pool.map(one, [(d, Pp, c, s, "random") for s in range(101, 106)])
        fr = [f for (a, f) in ctl]; n = sum(f >= 0.75 for f in fr)
        print("validity (random cue):", [round(f, 2) for f in fr], f"{n}/5", "VALID" if n <= 2 else "INVALID")
