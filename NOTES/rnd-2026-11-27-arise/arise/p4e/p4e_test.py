"""P4e locked test. Fresh seeds 801-810, T 6000, start = all zero-read cores. L_inf = {2,4,6} from gate.out."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu, wilcoxon
import p4e_model as m
MUS = [1e-5, 1e-4, 1e-3, 1e-2]; SEEDS = list(range(801, 811)); LINF = [2, 4, 6]
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}, "PRICE": {"cnat": 0.1}, "NOCUE": {"cue_mode": "none"}}
def one(a):
    mu, arm, s = a; P = dict(m.BASE); P.update(ARMS[arm]); P["mu"] = mu; r = m.run(P, s)
    hf = r["hist_final"]; rd = hf[2:]                       # lags 0..15 among dominant cores
    return a, dict(MI=r["MI"], MI_first=r["MI"][0], MI_final=r["MI"][-1], f_inf=float(sum(hf[l + 2] for l in LINF)),
                   f_2to6=float(sum(hf[l + 2] for l in range(2, 7))), eff=r["eff_final"], growth=r["growth"],
                   mode_lag=int(np.argmax(rd)) if sum(rd) > 0 else -1, reader_share=float(sum(rd)), eff_series=r["eff"], hist=r["hist"])
def holm(ps, alpha=0.05):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); rej = [False]*len(ps)
    for r, i in enumerate(order):
        if ps[i] <= alpha/(len(ps) - r): rej[i] = True
        else: break
    return rej
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(mu, a, s) for mu in MUS for a in ARMS for s in SEEDS])
    json.dump([{"mu": k[0], "arm": k[1], "seed": k[2], **v} for (k, v) in out], open("runs.json", "w"))
    R = {(mu, a): [v for (k, v) in out if k[0] == mu and k[1] == a] for mu in MUS for a in ARMS}
    g = lambda mu, a, f: np.array([v[f] for v in R[(mu, a)]])
    print("mu | MI_final ON OFF RANDOM PRICE NOCUE | MI_first ON | f_inf ON NOCUE | f_2to6 ON | reader_share ON | eff ON PRICE | growth ON NOCUE | modelag ON in L_inf")
    fam, lab = [], []
    for mu in MUS:
        print(mu, "|", " ".join(f"{g(mu,a,'MI_final').mean():.3f}" for a in ARMS), "|", f"{g(mu,'ON','MI_first').mean():.3f}", "|",
              f"{g(mu,'ON','f_inf').mean():.3f} {g(mu,'NOCUE','f_inf').mean():.3f}", "|", f"{g(mu,'ON','f_2to6').mean():.3f}", "|",
              f"{g(mu,'ON','reader_share').mean():.3f}", "|", f"{g(mu,'ON','eff').mean():.3f} {g(mu,'PRICE','eff').mean():.3f}", "|",
              f"{g(mu,'ON','growth').mean():.4f} {g(mu,'NOCUE','growth').mean():.4f}", "|", int(np.isin(g(mu,'ON','mode_lag'), LINF).sum()), "/10")
        on = g(mu, "ON", "MI_final"); d = on - g(mu, "ON", "MI_first")
        tests = [("MI ON>OFF", mannwhitneyu(on, g(mu, "OFF", "MI_final"), alternative="greater").pvalue),
                 ("MI ON>RANDOM", mannwhitneyu(on, g(mu, "RANDOM", "MI_final"), alternative="greater").pvalue),
                 ("MI ON final>first", wilcoxon(d, alternative="greater").pvalue if np.any(d != 0) else 1.0),
                 ("f_inf ON>NOCUE", mannwhitneyu(g(mu, "ON", "f_inf"), g(mu, "NOCUE", "f_inf"), alternative="greater").pvalue),
                 ("eff ON>PRICE", mannwhitneyu(g(mu, "ON", "eff"), g(mu, "PRICE", "eff"), alternative="greater").pvalue)]
        for n, pv in tests: fam.append(pv); lab.append((mu, n))
    rej = holm(fam)
    for (mu, n), pv, rj in zip(lab, fam, rej): print(f"  mu={mu} {n}: p={pv:.4g} Holm-reject={rj}")
    mstar = max(MUS, key=lambda mu: np.median(g(mu, "ON", "MI_final"))); R_ = {n: rj for (mu, n), rj in zip(lab, rej) if mu == mstar}
    ml = int(np.isin(g(mstar, "ON", "mode_lag"), LINF).sum())
    print(f"mu* = {mstar}")
    print(f"(a) information rises (T1-T3 at mu*): {'PASS' if R_['MI ON>OFF'] and R_['MI ON>RANDOM'] and R_['MI ON final>first'] else 'FAIL'}")
    print(f"(b) convergence on informative lag (T4 at mu* and mode lag in L_inf >= 8/10 [{ml}/10]): {'PASS' if R_['f_inf ON>NOCUE'] and ml >= 8 else 'FAIL'}")
    print(f"(c) price caps read strength (T5 at mu*): {'PASS' if R_['eff ON>PRICE'] else 'FAIL'}")
    print(f"(d) interior optimum (mu* in {{1e-4, 1e-3}}): {'PASS' if mstar in (1e-4, 1e-3) else 'FAIL'}")
