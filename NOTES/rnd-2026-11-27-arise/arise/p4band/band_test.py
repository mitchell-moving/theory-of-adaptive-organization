"""P4-BAND locked test: one transect, two-sided novelty band. Model band_model.py (byte-identical to p4f_model.py / p4g_model.py).
Fresh seeds 1401-1420 (ON) and 1401-1410 (OFF, RANDOM). T 6000, zero-read start, no reader written in, c_nat 0.01."""
import json, numpy as np
from multiprocessing import Pool
from scipy.stats import mannwhitneyu
import band_model as m
MUS = [1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]; X = np.log10(MUS)
SEEDS_ON = list(range(1401, 1421)); SEEDS_CTL = list(range(1401, 1411)); LINF = (2, 3, 4, 5, 6)
ARMS = {"ON": {}, "OFF": {"heredity": "off"}, "RANDOM": {"cue_mode": "random"}}
TIE = 0.95; NB = 2000
def one(a):
    mu, arm, s = a; P = dict(m.BASE); P.update(ARMS[arm]); P["mu"] = mu; r = m.run(P, s); hf = r["hist_final"]
    return a, dict(A=r["A"], eff=r["eff_final"], f_inf=float(sum(hf[l + 2] for l in LINF)), reader_share=float(sum(hf[2:])),
                   dominated=float(1 - hf[0]), growth=r["growth"])
def holm(ps, alpha=0.05):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); rej = [False]*len(ps)
    for r, i in enumerate(order):
        if ps[i] <= alpha/(len(ps) - r): rej[i] = True
        else: break
    return rej
def peak(med):
    """Tie rule (registered): top set = grid points with median >= TIE * max median. Peak location = mean log10 mu of top set.
    Peak grid index = member of top set nearest that mean (lower index if equidistant)."""
    med = np.asarray(med); mx = med.max()
    if not mx > 0: return None, None, []
    top = [i for i in range(len(med)) if med[i] >= TIE*mx]; loc = float(np.mean(X[top]))
    gi = min(top, key=lambda i: (abs(X[i] - loc), i)); return loc, gi, top
def quad(xs, ys):
    b2, b1, b0 = np.polyfit(xs, ys, 2); return b2, b1, b0, (-b1/(2*b2) if b2 != 0 else np.nan)
if __name__ == "__main__":
    jobs = [(mu, "ON", s) for mu in MUS for s in SEEDS_ON] + [(mu, a, s) for mu in MUS for a in ("OFF", "RANDOM") for s in SEEDS_CTL]
    with Pool(8) as p: out = p.map(one, jobs)
    json.dump([{"mu": k[0], "arm": k[1], "seed": k[2], **v} for (k, v) in out], open("runs.json", "w"))
    g = lambda mu, a, f: np.array([v[f] for (k, v) in out if k[0] == mu and k[1] == a])
    print("mu | median A ON | mean A ON | median A OFF | median A RANDOM | f_inf ON | reader_share ON | dominated ON | effort ON")
    med = []
    for mu in MUS:
        med.append(np.median(g(mu, "ON", "A")))
        print(f"{mu:g} | {med[-1]:.4f} | {g(mu,'ON','A').mean():.4f} | {np.median(g(mu,'OFF','A')):.4f} | {np.median(g(mu,'RANDOM','A')):.4f} | "
              f"{g(mu,'ON','f_inf').mean():.3f} | {g(mu,'ON','reader_share').mean():.3f} | {g(mu,'ON','dominated').mean():.3f} | {g(mu,'ON','eff').mean():.3f}")
    # B1 quadratic in log10 mu on per-seed A_ON
    xs = np.concatenate([np.full(len(SEEDS_ON), x) for x in X]); ys = np.concatenate([g(mu, "ON", "A") for mu in MUS])
    b2, b1, b0, xv = quad(xs, ys); rng = np.random.default_rng(0); B = np.array([g(mu, "ON", "A") for mu in MUS])
    bb2, bxv, bloc = [], [], []
    for _ in range(NB):
        R = np.array([row[rng.integers(0, len(row), len(row))] for row in B])
        q = quad(xs, R.reshape(-1)); bb2.append(q[0]); bxv.append(q[3]); bloc.append(peak(np.median(R, 1))[0])
    ci2 = np.percentile(bb2, [2.5, 97.5]); civ = np.nanpercentile(bxv, [2.5, 97.5])
    B1 = (ci2[1] < 0) and (X[0] < xv < X[-1])
    print(f"B1 quadratic: b2={b2:.5f} (boot 95% {ci2[0]:.5f}..{ci2[1]:.5f}); vertex log10 mu={xv:.3f} (mu {10**xv:.3g}; boot 95% {civ[0]:.3f}..{civ[1]:.3f}) -> {'PASS' if B1 else 'FAIL'}")
    loc, gi, top = peak(med)
    B2 = loc is not None and 0 not in top and len(MUS) - 1 not in top
    print(f"B2 peak (tie rule {TIE}): top set {[MUS[i] for i in top]}; peak log10 mu={loc:.3f} (mu {10**loc:.3g}); peak grid mu={MUS[gi]:g} -> {'PASS' if B2 else 'FAIL'}")
    bl = [b for b in bloc if b is not None]; cil = np.percentile(bl, [2.5, 97.5])
    B4 = len(bl) == NB and X[0] < cil[0] and cil[1] < X[-1]
    print(f"B4 bootstrap 95% CI on peak location: log10 mu {cil[0]:.3f}..{cil[1]:.3f} (mu {10**cil[0]:.3g}..{10**cil[1]:.3g}); {len(bl)}/{NB} defined -> {'PASS' if B4 else 'FAIL'}")
    pk = MUS[gi]; Aon = g(pk, "ON", "A")
    tests = [("B3a peak > lowest mu", mannwhitneyu(Aon, g(MUS[0], "ON", "A"), alternative="greater").pvalue),
             ("B3b peak > highest mu", mannwhitneyu(Aon, g(MUS[-1], "ON", "A"), alternative="greater").pvalue),
             ("C1 ON > OFF at peak", mannwhitneyu(Aon, g(pk, "OFF", "A"), alternative="greater").pvalue),
             ("C2 ON > RANDOM at peak", mannwhitneyu(Aon, g(pk, "RANDOM", "A"), alternative="greater").pvalue)]
    rej = holm([t[1] for t in tests]); R = {}
    for (n, pv), rj in zip(tests, rej): R[n] = rj; print(f"  {n}: p={pv:.4g} Holm-reject={rj}")
    size = med[0] <= 0.5*med[gi] and med[-1] <= 0.5*med[gi]
    B3 = R["B3a peak > lowest mu"] and R["B3b peak > highest mu"] and size
    print(f"B3 both-side drops (Holm both, and end medians <= 0.5 x peak median: low {med[0]:.4f}, high {med[-1]:.4f}, peak {med[gi]:.4f}) -> {'PASS' if B3 else 'FAIL'}")
    C12 = R["C1 ON > OFF at peak"] and R["C2 ON > RANDOM at peak"]; print("C1+C2 controls at peak ->", "PASS" if C12 else "FAIL")
    mo = max(np.median(g(mu, "OFF", "A")) for mu in MUS); mr = max(np.median(g(mu, "RANDOM", "A")) for mu in MUS)
    C3 = mo < 0.25*med[gi] and mr < 0.25*med[gi]
    print(f"C3 no band without heredity / timed cue (max median A OFF {mo:.4f}, RANDOM {mr:.4f} < 0.25 x {med[gi]:.4f}) -> {'PASS' if C3 else 'FAIL'}")
    print("OVERALL (B1 & B2 & B3 & B4 & C1+C2 & C3):", "PASS" if all([B1, B2, B3, B4, C12, C3]) else "FAIL")
