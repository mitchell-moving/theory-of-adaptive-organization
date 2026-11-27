"""P4b locked test: fresh seeds 501-505, T=3000, random-mixture start, world from gate (tau 2, P 40, cnat 0.01)."""
import numpy as np
from multiprocessing import Pool
import p4b_model as m
W = dict(tau=2.0, P=40.0, cnat=0.01, T=3000.0)
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}, "PRICE": {"cnat": 0.1}, "SIEVE": {"Lc": 0.0}}
SEEDS = [501, 502, 503, 504, 505]
def one(a):
    arm, s = a; P = dict(m.BASE); P.update(W); P.update(ARMS[arm]); return arm, s, m.run(P, s)
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(a, s) for a in ARMS for s in SEEDS])
    R = {a: {s: r for (b, s, r) in out if b == a} for a in ARMS}
    for a in ARMS:
        for s in SEEDS: print(a, s, {k: round(v, 3) for k, v in R[a][s].items()})
        print(a, "MEAN", {k: round(float(np.nanmean([R[a][s][k] for s in SEEDS])), 3) for k in R[a][SEEDS[0]]})
    k = lambda f: sum(bool(f(s)) for s in SEEDS); on = R["ON"]
    T = {"(i-a) exclusivity excl_ON>=0.8": k(lambda s: on[s]["excl"] >= 0.8),
         "(i-b) kappa_ON>=0.5 and kappa_ON-kappa_OFF>=0.4": k(lambda s: on[s]["kappa"] >= 0.5 and on[s]["kappa"] - R["OFF"][s]["kappa"] >= 0.4),
         "(i-c) Vasas core switching switch_ON>=0.001": k(lambda s: on[s]["switch"] >= 0.001),
         "(ii-a) reader_ON>=0.5 and >=hedger_ON+0.1": k(lambda s: on[s]["reader"] >= 0.5 and on[s]["reader"] >= on[s]["hedger"] + 0.1),
         "(ii-b) reader_ON-reader_OFF>=0.25": k(lambda s: on[s]["reader"] - R["OFF"][s]["reader"] >= 0.25),
         "(ii-c) reader_RANDOM<=0.30 and reader_ON-reader_RANDOM>=0.25": k(lambda s: R["RANDOM"][s]["reader"] <= 0.30 and on[s]["reader"] - R["RANDOM"][s]["reader"] >= 0.25),
         "(iii) reader_PRICE<=0.10": k(lambda s: R["PRICE"][s]["reader"] <= 0.10),
         "(s) growth_ON>=1.02*growth_SIEVE": k(lambda s: on[s]["growth"] >= 1.02*R["SIEVE"][s]["growth"])}
    for t, n in T.items(): print(f"{t}: {n}/5 -> {'PASS' if n >= 4 else 'FAIL'}")
