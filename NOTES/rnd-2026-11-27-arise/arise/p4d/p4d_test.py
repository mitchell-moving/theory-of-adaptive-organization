"""P4d locked test. tau 3, Mmol 20, beta 1.5, reader absent at start, P 40, cnat 0.01, T 3000. Fresh seeds 701-710."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import p4d_model as m
MUS = [0.001, 0.003, 0.01, 0.03, 0.1]; SEEDS = list(range(701, 711))
W = dict(tau=3.0, Mmol=20.0, beta=1.5, absent=True, P=40.0, cnat=0.01, T=3000.0)
ARMS = {"ON": {}, "NOCUE": {"Lc": 0.0}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}, "PRICE": {"cnat": 0.1}}
def one(a):
    mu, arm, s = a; P = dict(m.BASE); P.update(W); P.update(ARMS[arm]); P["mu"] = mu; return a, m.run(P, s)
def holm(ps, alpha=0.05):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); rej = [False]*len(ps)
    for r, i in enumerate(order):
        if ps[i] <= alpha/(len(ps) - r): rej[i] = True
        else: break
    return rej
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(mu, a, s) for mu in MUS for a in ARMS for s in SEEDS])
    R = {(mu, a): [r for (k, r) in out if k[0] == mu and k[1] == a] for mu in MUS for a in ARMS}
    json.dump({f"{k[0]}|{k[1]}|{k[2]}": r["series"] for (k, r) in out}, open("series.json", "w"))
    rows = [{**{x: k[i] for i, x in enumerate(["mu", "arm", "seed"])}, **{x: v for x, v in r.items() if x != "series"}} for (k, r) in out]
    json.dump(rows, open("runs.json", "w"))
    rd = lambda mu, a, f="reader": np.array([r[f] for r in R[(mu, a)]])
    S = {mu: rd(mu, "ON").mean() - rd(mu, "NOCUE").mean() for mu in MUS}
    fam, labels = [], []
    print("mu | reader ON NOCUE OFF RANDOM PRICE | hedger_ON | kappa_ON switch_ON | appear ON/10 NOCUE/10 | S=ON-NOCUE")
    for mu in MUS:
        on = rd(mu, "ON")
        print(mu, "|", " ".join(f"{rd(mu, a).mean():.3f}" for a in ARMS), "|", f"{rd(mu,'ON','hedger').mean():.3f}", "|",
              f"{np.nanmean(rd(mu,'ON','kappa')):.3f} {np.nanmean(rd(mu,'ON','switch')):.4f}", "|",
              int(np.sum(~np.isnan(rd(mu,'ON','first_reader')))), int(np.sum(~np.isnan(rd(mu,'NOCUE','first_reader')))), "|", f"{S[mu]:+.3f}")
        for name, other in [("hedger", rd(mu, "ON", "hedger")), ("NOCUE", rd(mu, "NOCUE")), ("OFF", rd(mu, "OFF")),
                            ("RANDOM", rd(mu, "RANDOM")), ("PRICE", rd(mu, "PRICE"))]:
            fam.append(mannwhitneyu(on, other, alternative="greater").pvalue); labels.append((mu, name))
    rej = holm(fam)
    for (mu, name), pv, rj in zip(labels, fam, rej): print(f"  mu={mu} ON>{name}: p={pv:.4g} Holm-reject={rj}")
    mstar = max(MUS, key=lambda mu: S[mu]); interior = mstar in MUS[1:-1]
    app = int(np.sum(~np.isnan(rd(mstar, "ON", "first_reader"))))
    allsig = all(rj for (mu, name), rj in zip(labels, rej) if mu == mstar)
    print(f"mu* = {mstar}; (P1) interior optimum: {'PASS' if interior else 'FAIL'}")
    print(f"(P2) reader appears at mu*: {app}/10 -> {'PASS' if app >= 8 else 'FAIL'}")
    print(f"(P3) at mu*, ON beats hedger, NOCUE, OFF, RANDOM, PRICE (all 5 Holm-significant in 25-test family): {'PASS' if allsig else 'FAIL'}")
