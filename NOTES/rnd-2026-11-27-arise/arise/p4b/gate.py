"""P4b gate, pilot seeds 101-105, T=1500, SAME random-mixture start as the test, hedger core present in every world."""
import itertools, numpy as np
from multiprocessing import Pool
import p4b_model as m
GRID = list(itertools.product([1.0, 2.0], [20.0, 40.0], [0.01, 0.05]))   # tau, P, cnat
ok = lambda r: r["reader"] >= 0.5 and r["reader"] >= r["hedger"] + 0.1
def one(a):
    tau, Pp, c, s, mode = a; P = dict(m.BASE); P.update(tau=tau, P=Pp, cnat=c, T=1500.0, cue_mode=mode); return a, m.run(P, s)
if __name__ == "__main__":
    with Pool(8) as pool:
        out = pool.map(one, [(t, Pp, c, s, "cued") for (t, Pp, c) in GRID for s in range(101, 106)]); passing = []
        for (t, Pp, c) in GRID:
            rs = [r for (a, r) in out if a[:3] == (t, Pp, c)]; n = sum(ok(r) for r in rs)
            print(f"tau={t} P={Pp} cnat={c} | reader {[round(r['reader'],2) for r in rs]} hedger {[round(r['hedger'],2) for r in rs]} "
                  f"kappa {[round(r['kappa'],2) for r in rs]} switch {[round(r['switch'],3) for r in rs]} | {n}/5 {'PASS' if n>=4 else '-'}")
            if n >= 4: passing.append((-c, t, -Pp))
        if not passing: print("NO WORLD PASSES THE GATE"); raise SystemExit
        c, t, Pp = sorted(passing)[0]; c, Pp = -c, -Pp; print("CHOSEN:", dict(tau=t, P=Pp, cnat=c))
        ctl = pool.map(one, [(t, Pp, c, s, "random") for s in range(101, 106)]); n = sum(ok(r) for (a, r) in ctl)
        print("validity (random cue): reader", [round(r['reader'], 2) for (a, r) in ctl], f"{n}/5", "VALID" if n <= 2 else "INVALID")
