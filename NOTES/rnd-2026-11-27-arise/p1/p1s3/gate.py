"""P1-S3 pre-lock GATE (pilot seeds 101-105 only; test seeds will be 301-305).
For each world (sig_f, c, x_r) and design reading strength k: two fixed-design competitions, 125 v 125, no mutation,
same force path per seed. Judge = designed Kalman judge; rivals = sieve (no reading) and reflex (no force model)."""
import sys, json, itertools, numpy as np
from multiprocessing import Pool
import p1s3_sim as m
TG = 5000.0; SEEDS = [101, 102, 103, 104, 105]
GRID = list(itertools.product([1.0, 1.25, 1.5], [0.005, 0.02], [3.0, 4.0], [0.1, 1.0]))
def one(a):
    sf, c, xr, k, rival, seed = a
    P = dict(m.BASE); P.update(sig_f=sf, c=c, x_r=xr)
    J = m.designed(P, "judge", k); Rv = m.designed(P, rival, k if rival == "reflex" else 0)
    F = np.array([J]*125 + [Rv]*125); L = np.array([1]*125 + [0]*125)
    r = m.run(P, TG, seed, "fixed", founders=F, labels=L, snap=False)
    return dict(sig_f=sf, c=c, x_r=xr, k=k, rival=rival, seed=seed, extinct=r["extinct_t"],
                judge_freq=None if r["extinct_t"] is not None else r["final_freq"].get(1, 0.0),
                ruin_share=r.get("ruin_share"), gen_time=r.get("gen_time"))
if __name__ == "__main__":
    jobs = [(sf, c, xr, k, rv, s) for (sf, c, xr, k) in GRID for rv in ("sieve", "reflex") for s in SEEDS]
    with Pool(8) as pool: out = pool.map(one, jobs)
    json.dump(out, open("gate_raw.json", "w"), indent=0)
    print("sig_f c x_r k | G1 judge>sieve freq>=0.75 (n/5, no extinction) | G2 judge>reflex freq>=0.65 | G3 ruin share>=0.25 (median) | gen_time | PASS")
    passing = []
    for (sf, c, xr, k) in GRID:
        rs = [o for o in out if (o["sig_f"], o["c"], o["x_r"], o["k"]) == (sf, c, xr, k)]
        s1 = [o for o in rs if o["rival"] == "sieve"]; s2 = [o for o in rs if o["rival"] == "reflex"]
        g1 = sum(o["extinct"] is None and o["judge_freq"] >= 0.75 for o in s1)
        g2 = sum(o["extinct"] is None and o["judge_freq"] >= 0.65 for o in s2)
        rsh = [o["ruin_share"] for o in s1 if o["ruin_share"] is not None]; g3 = np.median(rsh) if rsh else 0
        gt = np.median([o["gen_time"] for o in s1 if o["gen_time"]]) if rsh else None
        ok = g1 >= 4 and g2 >= 4 and g3 >= 0.25
        fr1 = [None if o["judge_freq"] is None else round(o["judge_freq"], 2) for o in s1]
        fr2 = [None if o["judge_freq"] is None else round(o["judge_freq"], 2) for o in s2]
        print(sf, c, xr, k, "|", g1, fr1, "|", g2, fr2, "|", round(g3, 3), "|", gt and round(gt, 1), "|", "PASS" if ok else "-")
        if ok: passing.append((sf, -c, -xr, k))
    if passing:
        sf, nc, nxr, k = sorted(passing)[0]
        print("CHOSEN WORLD (rule: smallest sig_f, then larger c, then larger x_r, then smaller k):", dict(sig_f=sf, c=-nc, x_r=-nxr, k=k))
    else:
        print("NO WORLD PASSES THE GATE")
