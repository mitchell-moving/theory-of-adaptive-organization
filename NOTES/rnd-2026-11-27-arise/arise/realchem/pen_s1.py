"""REALCHEM-S1: heredity vs novelty for a cross-inhibited PEN-toolbox autocatalytic pair in passaged droplets,
using the published kinetic constants of Montagne et al. 2011 (MSB 7:466, Table 1; doi 10.1038/msb.2010.120).
Species per droplet (nM): a, b (autocatalytic triggers), ia (inhibits template Ta; made from b), ib (inhibits Tb; made from a).
Reduced model (quasi-steady template occupancy, first-order enzymatics valid at low substrate, as in the paper's raw model):
  da/dt = kc*Ta*occ(a, ia) - kexo_a*a + leak ;  dib/dt = ki*Ti*a/(a+Ka) - kexo_i*ib   (and symmetric)
  occ(a, ia) = (a/Ka)/(1 + a/Ka + ia/Ki);  Ka = kd_a/ka, Ki = kd_inh/ka;  kc = (1/kpol + 1/knick)^-1, ki = (1/kpolSD + 1/knick)^-1.
Intrinsic noise: tau-leaping (Poisson production and degradation counts in droplet volume V). Passage every Tp min:
each droplet splits into two daughters by binomial partition of molecules, each refilled to V with fresh mix (no triggers);
one daughter replaces a random droplet (no selection: neutral passaging; this run measures heredity and switching only)."""
import numpy as np
NA = 6.022e23
PUB = dict(ka=26e6, kd_a=2.3, kd_inh=0.0057, kpol=17.0, kpolSD=6.9, knick=3.0, kexo_a=0.32, kexo_i=1.2)  # Table 1
def rates(P):
    Ka = P["kd_a"]/P["ka"]*1e9; Ki = P["kd_inh"]/P["ka"]*1e9                          # nM
    kc = 1/(1/P["kpol"] + 1/P["knick"]); ki = 1/(1/P["kpolSD"] + 1/P["knick"]); return Ka, Ki, kc, ki
def deriv(x, P, T, Ti, leak):
    Ka, Ki, kc, ki = rates(P); a, b, ia, ib = x.T
    pa = kc*T*(a/Ka)/(1 + a/Ka + ia/Ki); pb = kc*T*(b/Ka)/(1 + b/Ka + ib/Ki)
    pib = ki*Ti*a/(a + Ka); pia = ki*Ti*b/(b + Ka)
    prod = np.c_[pa + leak, pb + leak, pia, pib]; deg = np.c_[P["kexo_a"]*a, P["kexo_a"]*b, P["kexo_i"]*ia, P["kexo_i"]*ib]
    return prod, deg
def bistable(T, Ti, P=PUB, tmax=300.0, dt=0.01):
    out = []
    for x0 in ([300.0, 1.0, 0.0, 0.0], [1.0, 300.0, 0.0, 0.0]):   # the other trigger seeded at 1 nM, so independence is not mistaken for bistability
        x = np.array([x0])
        for _ in range(int(tmax/dt)):
            pr, dg = deriv(x, P, T, Ti, 0.0); x = np.maximum(x + (pr - dg)*dt, 0)
        out.append(x[0])
    okA = out[0][0] > 50 and out[0][0] > 10*out[0][1]; okB = out[1][1] > 50 and out[1][1] > 10*out[1][0]
    return okA and okB, out
def ident(x):
    a, b = x[:, 0], x[:, 1]
    return np.where((a > 50) & (a > 10*b), 0, np.where((b > 50) & (b > 10*a), 1, -1))
def run(V_fL, leak, T, Ti, seed, N=200, passages=40, Tp=60.0, dt=0.05, P=PUB):
    rng = np.random.default_rng(seed); c = NA*V_fL*1e-15*1e-9                      # molecules per nM
    n = np.zeros((N, 4)); n[:N//2, 0] = 300*c; n[N//2:, 1] = 300*c; n = np.round(n)
    pairs = []; birth = np.full(N, -2)
    for p in range(passages):
        for _ in range(int(Tp/dt)):
            pr, dg = deriv(n/c, P, T, Ti, leak)
            n = np.maximum(n + rng.poisson(pr*c*dt) - rng.poisson(np.minimum(dg*c*dt, n + 0.0)), 0)
        idn = ident(n/c)
        if p >= passages//2: pairs += [(birth[i], idn[i]) for i in range(N) if birth[i] >= -1]
        par = rng.integers(0, N, N)                                                    # neutral passage: each slot gets a daughter of a random droplet
        n = rng.binomial(n[par].astype(np.int64), 0.5).astype(float); birth = idn[par]
    pa = np.array(pairs); m = (pa[:, 0] >= 0); pa = pa[m]
    valid = pa[pa[:, 1] >= 0]; sw = float(np.mean(valid[:, 0] != valid[:, 1])) if len(valid) else float("nan")
    loss = float(np.mean(pa[:, 1] < 0)) if len(pa) else float("nan")
    po = np.mean(pa[:, 0] == pa[:, 1]); pe = sum(np.mean(pa[:, 0] == k)*np.mean(pa[:, 1] == k) for k in (-1, 0, 1))
    kap = float((po - pe)/(1 - pe)) if pe < 1 else float("nan")
    return dict(kappa=kap, switch=sw, loss=loss, n=len(pa))
if __name__ == "__main__":
    import sys, itertools
    from multiprocessing import Pool
    T = 60.0
    print("Ka, Ki (nM), kc, ki (1/min):", [round(v, 4) for v in rates(PUB)])
    Ti_choice = None
    for Ti in (1.0, 3.0, 10.0, 30.0):
        ok, out = bistable(T, Ti); print(f"Ti={Ti} nM bistable={ok} A-start {np.round(out[0][:2],1)} B-start {np.round(out[1][:2],1)}")
        if ok and Ti_choice is None: Ti_choice = Ti
    if Ti_choice is None: print("NO BISTABILITY IN GRID: STOP"); sys.exit()
    print("chosen Ti =", Ti_choice)
    grid = list(itertools.product([0.1, 0.3, 1.0, 3.0, 10.0], [0.0, 1e-3, 1e-2]))
    with Pool(8) as pool: res = pool.starmap(run, [(V, lk, T, Ti_choice, s) for (V, lk) in grid for s in (1, 2, 3)])
    k = 0; band = []
    for (V, lk) in grid:
        rs = res[k:k + 3]; k += 3
        med = {f: float(np.nanmedian([r[f] for r in rs])) for f in ("kappa", "switch", "loss")}
        inb = med["kappa"] >= 0.5 and med["switch"] >= 0.002
        if inb: band.append((V, lk))
        print(f"V={V} fL leak={lk} nM/min | kappa {med['kappa']:.3f} switch {med['switch']:.4f} loss {med['loss']:.3f} {'BAND' if inb else ''}")
    print("BAND:", band)
