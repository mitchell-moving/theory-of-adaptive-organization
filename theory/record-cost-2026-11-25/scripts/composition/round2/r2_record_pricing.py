"""Round 2, script 2: 'retrievable-distinction' pricing, the additive per-record reading of kappa*I_mem.
P_rec(S) = sup over k independent uniform bits X_1..X_k encoded into states of S of  sum_j I_acc(X_j ; S),
each bit read with its own best measurement. Additivity over independent records is the same requirement used
for systems in round 1 (t6), applied to the records a holder keeps retrievable.
- classical N-simplex: P_rec = log2 N (outcome of one fine-grained measurement carries everything; sum of
  informations of independent bits about one classical variable <= its entropy).
- QM (and real QM, a sub-theory): P_rec <= log2 N_holder by information causality's entropic bound
  (Pawlowski et al. 2009, 10.1038/nature08400): sum_j I(X_j; S) <= I(X_1..X_k ; S) <= log2 d for independent X_j.
- polygons: computed here by brute force over vertex encodings (optimal for fixed decoders by convexity of I in the
  encoded states) and over binary extreme measurements (a LOWER bound on P_rec if multi-outcome reads help).
Then: re-rank the sibling's zero-drift single-system table and round 1's zero-drift bipartite table under P_rec.
"""
import itertools, json, numpy as np
def H(p):
    p = np.asarray(p, float).ravel(); p = p[p > 1e-15]; return float(-(p*np.log2(p)).sum())
def polygon(n): return np.array([[np.cos(2*np.pi*i/n), np.sin(2*np.pi*i/n), 1.0] for i in range(n)])
def extreme_effects(V):
    cons = [(v, 0.0) for v in V] + [(v, 1.0) for v in V]; pts = []
    for (a, ba), (b, bb), (c, bc) in itertools.combinations(cons, 3):
        A = np.array([a, b, c])
        if abs(np.linalg.det(A)) < 1e-9: continue
        e = np.linalg.solve(A, [ba, bb, bc]); vals = V @ e
        if vals.min() > -1e-9 and vals.max() < 1 + 1e-9 and not any(np.allclose(e, p, atol=1e-7) for p in pts): pts.append(e)
    return np.array(pts)
def P_rec_polygon(n, k):
    V = polygon(n); E = extreme_effects(V)
    E = np.array([e for e in E if (V @ e).max() - (V @ e).min() > 1e-9])   # non-trivial binary reads (e, u-e)
    Pv = V @ E.T   # prob of outcome 1 for vertex i under effect m
    strings = list(itertools.product(range(2), repeat=k)); best = (0, None)
    for enc in itertools.product(range(n), repeat=len(strings)):
        P = Pv[list(enc)]   # strings x effects
        tot = 0
        for j in range(k):
            mask = np.array([s[j] for s in strings])
            p1 = P.mean(0); p1_0 = P[mask == 0].mean(0); p1_1 = P[mask == 1].mean(0)
            h = lambda p: -(np.where(p > 1e-15, p*np.log2(np.clip(p, 1e-15, 1)), 0) + np.where(1-p > 1e-15, (1-p)*np.log2(np.clip(1-p, 1e-15, 1)), 0))
            I = h(p1) - 0.5*(h(p1_0) + h(p1_1)); tot += I.max()
        if tot > best[0] + 1e-12: best = (tot, enc)
    return best
out = {"P_rec_polygons": []}
for n, k in [(4, 2), (4, 3), (5, 2), (6, 2), (6, 3), (8, 2)]:
    v, enc = P_rec_polygon(n, k)
    out["P_rec_polygons"].append(dict(n=n, k_bits=k, sum_I_acc_bits=round(v, 6), encoding=list(enc)))
# single-system zero-drift table (sibling nocloning/NOTE.md sec.3 errors), q = 4
pr = {r["n"]: max(x["sum_I_acc_bits"] for x in out["P_rec_polygons"] if x["n"] == r["n"]) for r in out["P_rec_polygons"]}
sib = {"classical N=2": (1.0, 0.250), "classical N=3": (np.log2(3), 0.167), "classical N=4": (2.0, 0.125),
       "square (gbit)": (max(pr[4], 1.0), 0.125), "pentagon": (max(pr[5], 1.0), 0.176), "hexagon": (max(pr[6], 1.0), 0.167),
       "octagon": (max(pr[8], 1.0), 0.172), "disk (rebit)": (1.0, 0.1817), "ball (qubit)": (1.0, 0.1817)}
q = 4.0
out["single_system_zero_drift_P_rec"] = sorted((round(P + q*e, 4), k, round(P, 4)) for k, (P, e) in sib.items())
out["single_system_zero_drift_logN"] = sorted((round(L + q*e, 4), k) for k, (L, e) in
    {"classical N=2": (1, .25), "classical N=3": (np.log2(3), .167), "classical N=4": (2, .125), "square (gbit)": (1, .125),
     "pentagon": (1, .176), "hexagon": (1, .167), "octagon": (1, .172), "disk (rebit)": (1, .1817), "ball (qubit)": (1, .1817)}.items())
# bipartite zero drift (round-1 t5 errors): e_A, e_B, e_joint
tsir = 1 - np.cos(np.pi/8)**2; d = 0.5 - 1/np.pi
pairs = {"classical pair": (2.0, .25, .25, .25), "boxworld pair": (2*pr[4], .125, .125, 0.0),
         "real-QM pair": (2.0, d, d, tsir), "QM pair": (2.0, d, d, tsir)}
out["bipartite_zero_drift_P_rec (boxworld price is a lower bound: product of two gbits; PR correlations can only raise it)"] = \
    {k: round(P + q*(a + b + c), 3) for k, (P, a, b, c) in pairs.items()}
out["bipartite_zero_drift_logN (round 1)"] = {k: round(2 + q*(a + b + c), 3) for k, (P, a, b, c) in pairs.items()}
# break-even: how large would the boxworld pair's error have to be... and how much q makes it win again
out["boxworld_pair_wins_again_if_q_exceeds"] = round((2*pr[4] - 2)/((2*d + tsir) - 0.25), 3)
json.dump(out, open("r2_record_pricing.json", "w"), indent=1); print(json.dumps(out, indent=1))
