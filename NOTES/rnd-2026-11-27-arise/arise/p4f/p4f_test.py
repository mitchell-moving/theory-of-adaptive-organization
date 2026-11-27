"""P4f locked test. Fresh seeds 901-910, T 6000, zero-read start. L_inf = {2,3,4,5,6} from gate.out."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import p4f_model as m
SEEDS = list(range(901, 911)); LINF = [2, 3, 4, 5, 6]; MUS = [1e-4, 1e-3, 1e-2]; MU_ON = [1e-5] + MUS
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}, "NOCUE": {"cue_mode": "none"},
        "C0.1": {"cnat": 0.1}, "C1": {"cnat": 1.0}, "C10": {"cnat": 10.0}}
def one(a):
    mu, arm, s = a; P = dict(m.BASE); P.update(ARMS[arm]); P["mu"] = mu; r = m.run(P, s); hf = r["hist_final"]; rd = hf[2:]
    return a, dict(A=r["A"], f_inf=float(sum(hf[l + 2] for l in LINF)), eff=r["eff_final"], growth=r["growth"],
                   mode_lag=int(np.argmax(rd)) if sum(rd) > 0 else -1, MI_final=r["MI"][-1])
def holm(ps, alpha=0.05):
    o = sorted(range(len(ps)), key=lambda i: ps[i]); rej = [False]*len(ps)
    for r, i in enumerate(o):
        if ps[i] <= alpha/(len(ps) - r): rej[i] = True
        else: break
    return rej
if __name__ == "__main__":
    jobs = [(1e-5, "ON", s) for s in SEEDS] + [(mu, a, s) for mu in MUS for a in ARMS for s in SEEDS]
    with Pool(8) as p: out = p.map(one, jobs)
    json.dump([{"mu": k[0], "arm": k[1], "seed": k[2], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda mu, a, f: np.array([v[f] for (k, v) in out if k[0] == mu and k[1] == a])
    print("mu | A: ON OFF RANDOM NOCUE C0.1 C1 C10 | f_inf: ON NOCUE OFF | eff: ON C0.1 C1 C10 | modelag ON in L_inf")
    for mu in MU_ON:
        arms = list(ARMS) if mu in MUS else ["ON"]
        print(mu, "|", " ".join(f"{a}={g(mu,a,'A').mean():.4f}" for a in arms), "|",
              " ".join(f"{a}={g(mu,a,'f_inf').mean():.3f}" for a in arms if a in ("ON", "NOCUE", "OFF")), "|",
              " ".join(f"{a}={g(mu,a,'eff').mean():.3f}" for a in arms if a in ("ON", "C0.1", "C1", "C10")), "|",
              int(np.isin(g(mu, "ON", "mode_lag"), LINF).sum()), "/10")
    fam, lab = [], []
    for mu in MUS:
        on = g(mu, "ON", "A")
        for n, x, y in [("F1 A ON>OFF", on, g(mu, "OFF", "A")), ("F1 A ON>RANDOM", on, g(mu, "RANDOM", "A")),
                        ("F2 f_inf ON>NOCUE", g(mu, "ON", "f_inf"), g(mu, "NOCUE", "f_inf")),
                        ("F3 eff ON>C1", g(mu, "ON", "eff"), g(mu, "C1", "eff")), ("F3 eff ON>C10", g(mu, "ON", "eff"), g(mu, "C10", "eff"))]:
            fam.append(mannwhitneyu(x, y, alternative="greater").pvalue); lab.append((mu, n))
    rej = holm(fam)
    for (mu, n), pv, rj in zip(lab, fam, rej): print(f"  mu={mu} {n}: p={pv:.4g} Holm={rj}")
    R = lambda pre: [rj for (mu, n), rj in zip(lab, rej) if n.startswith(pre)]
    print("F1 (A ON > OFF and > RANDOM at all 3 mu):", "PASS" if all(R("F1")) else f"FAIL ({sum(R('F1'))}/6)")
    print("F2 (f_inf ON > NOCUE at all 3 mu):", "PASS" if all(R("F2")) else f"FAIL ({sum(R('F2'))}/3)")
    print("F3 (price caps read effort: ON > C1 and > C10 at all 3 mu):", "PASS" if all(R("F3")) else f"FAIL ({sum(R('F3'))}/6)")
    med = {mu: np.median(g(mu, "ON", "A")) for mu in MU_ON}; ms = max(MU_ON, key=lambda mu: med[mu])
    print("F4 interior optimum of median A over mu in {1e-5,1e-4,1e-3,1e-2}:", {k: round(v, 4) for k, v in med.items()}, "argmax", ms,
          "PASS" if ms in (1e-4, 1e-3) else "FAIL")
    print("F5 (lag convergence: mode lag in L_inf >= 8/10 at all 3 mu):",
          "PASS" if all(np.isin(g(mu, "ON", "mode_lag"), LINF).sum() >= 8 for mu in MUS) else "FAIL")
