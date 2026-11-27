"""P4c gate per SWEEP_AND_RULES: band cells in pre-stated order, at most 3; reader PRESENT at start; pilot seeds 101-105."""
import numpy as np
from multiprocessing import Pool
import p4c_model as m
ORDER = [(3.0, 20.0, 3.0, 0.1), (1.5, 20.0, 3.0, 0.1), (3.0, 200.0, 3.0, 0.1)]
ok = lambda r: r["reader"] >= 0.3 and r["reader"] >= r["hedger"] + 0.1
def one(a):
    (b, M, t, mu), s, mode = a; P = dict(m.BASE)
    P.update(beta=b, Mmol=M, tau=t, mu=mu, P=40.0, cnat=0.01, T=1500.0, absent=False, cue_mode=mode); return m.run(P, s)
if __name__ == "__main__":
    with Pool(8) as p:
        for cell in ORDER:
            rs = p.map(one, [(cell, s, "cued") for s in range(101, 106)]); n = sum(map(ok, rs))
            print(cell, "cued reader", [round(r["reader"], 2) for r in rs], "hedger", [round(r["hedger"], 2) for r in rs], f"{n}/5")
            if n < 4: print(" -> gate FAIL at this cell"); continue
            rc = p.map(one, [(cell, s, "random") for s in range(101, 106)]); nc = sum(map(ok, rc))
            print(" random reader", [round(r["reader"], 2) for r in rc], f"{nc}/5", "VALID" if nc <= 2 else "INVALID")
            if nc <= 2: print("CHOSEN REGIME:", cell); break
        else: print("NO REGIME PASSES")
