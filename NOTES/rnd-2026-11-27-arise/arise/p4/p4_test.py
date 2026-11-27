"""P4 locked test. Fresh seeds 401-405, T=3000, random Dirichlet start, world from gate v2 (delta 0.1, P 60, c 0.2), hedger present."""
import numpy as np, json
from multiprocessing import Pool
import p4b_sim as m
W = dict(delta=0.1, P=60.0, c=0.2, hedge=True, T=3000.0)
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "SIEVE": {"Lc": 0.0}, "RANDOM": {"cue_mode": "random"}, "PRICE": {"c": 1.0}}
SEEDS = [401, 402, 403, 404, 405]
def one(a):
    arm, s = a; P = dict(m.BASE); P.update(W); P.update(ARMS[arm]); return arm, s, m.run(P, s)
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(a, s) for a in ARMS for s in SEEDS])
    R = {a: {s: r for (b, s, r) in out if b == a} for a in ARMS}
    for a in ARMS:
        for s in SEEDS: r = R[a][s]; print(a, s, {k: round(v, 3) for k, v in r.items()})
    k = lambda f: sum(bool(f(s)) for s in SEEDS)
    tests = {
      "(i) H_on>=0.10 and H_on-H_off>=0.10": k(lambda s: R["ON"][s]["H"] >= 0.10 and R["ON"][s]["H"] - R["OFF"][s]["H"] >= 0.10),
      "(ii-a) reader_freq_on>=0.75": k(lambda s: R["ON"][s]["reader_freq"] >= 0.75),
      "(ii-a2) AI_on-AI_sieve>=0.02": k(lambda s: R["ON"][s]["AI"] - R["SIEVE"][s]["AI"] >= 0.02),
      "(ii-b) reader_on-reader_off>=0.25": k(lambda s: R["ON"][s]["reader_freq"] - R["OFF"][s]["reader_freq"] >= 0.25),
      "(ii-c) random cue reader_freq<=0.30": k(lambda s: R["RANDOM"][s]["reader_freq"] <= 0.30),
      "(iii) price c=1.0 reader_freq<=0.30": k(lambda s: R["PRICE"][s]["reader_freq"] <= 0.30),
      "(s) growth_on>=1.10*growth_sieve": k(lambda s: R["ON"][s]["growth"] >= 1.10*R["SIEVE"][s]["growth"]),
    }
    for t, n in tests.items(): print(f"{t}: {n}/5 -> {'PASS' if n >= 4 else 'FAIL'}")
