import json, glob
R = {(r["cell"], r["seed"]): r for r in (json.load(open(f)) for f in glob.glob("out/*.json"))}
S = range(301, 306); cells = ["P_on", "P_off", "P_sieve", "U_on", "High_on"]
print("cell seed extinct_t N_mean gen_time dA_u r2_body ruin_hz ruin_share h_max logk_med")
for c in cells:
    for s in S:
        r = R[(c, s)]
        if r["extinct_t"] is not None: print(f"{c:8s} {s} EXTINCT at {r['extinct_t']:.1f}"); continue
        print(f"{c:8s} {s} - {r['N_mean']:6.1f} {r['gen_time']:7.1f} {r.get('dA_u',float('nan')):+.4f} {r.get('r2_body',float('nan')):.4f} {r['ruin_hazard']:.5f} {r['ruin_share']:.3f} {r['h_max_mean']:.3f} {r['logk_median']:+.3f}")
alive = lambda c, s: R[(c, s)]["extinct_t"] is None
g = lambda c, s, k: R[(c, s)][k]
def tally(name, fn):
    det = []
    for s in S:
        try: v, ok = fn(s)
        except Exception: v, ok = None, False
        det.append((s, v, ok))
    n = sum(d[2] for d in det)
    print(f"{name}: {n}/5 -> {'PASS' if n >= 4 else 'FAIL'}   " + "; ".join(f"s{s}:{v if not isinstance(v,float) else round(v,4)}{'+' if ok else '-'}" for s, v, ok in det))
    return n >= 4
A = tally("H-A P_on dA_u>=0.19", lambda s: (g("P_on",s,"dA_u"), alive("P_on",s) and g("P_on",s,"dA_u") >= 0.19))
def hb(s):
    if not alive("P_on", s): return None, False
    off = 0.0 if not alive("P_off", s) else g("P_off", s, "dA_u")
    v = g("P_on", s, "dA_u") - off; return v, v >= 0.10 and alive("P_off", s)
B = tally("H-B dA_u(on)-dA_u(off)>=0.10 (off must be alive to measure)", hb)
D = tally("H-D off extinct or ruin(off)/ruin(on)>=1.3", lambda s: ("off_extinct" if not alive("P_off",s) else g("P_off",s,"ruin_hazard")/g("P_on",s,"ruin_hazard"),
          alive("P_on",s) and (not alive("P_off",s) or g("P_off",s,"ruin_hazard") >= 1.3*g("P_on",s,"ruin_hazard"))))
C = tally("H-C on alive & (sieve extinct or ratio>=1/0.7)", lambda s: ("sieve_extinct" if not alive("P_sieve",s) else g("P_sieve",s,"ruin_hazard")/g("P_on",s,"ruin_hazard"),
          alive("P_on",s) and (not alive("P_sieve",s) or g("P_sieve",s,"ruin_hazard") >= g("P_on",s,"ruin_hazard")/0.7)))
E = tally("H-E h_max(P_on)-h_max(U_on)>=0.10", lambda s: (g("P_on",s,"h_max_mean")-g("U_on",s,"h_max_mean"), alive("P_on",s) and alive("U_on",s) and g("P_on",s,"h_max_mean")-g("U_on",s,"h_max_mean") >= 0.10))
F = tally("H-F logk(High)<=logk(P_on)-0.5", lambda s: (g("High_on",s,"logk_median")-g("P_on",s,"logk_median"), alive("P_on",s) and alive("High_on",s) and g("High_on",s,"logk_median") <= g("P_on",s,"logk_median")-0.5))
print("PRIMARY (H-A & H-B & H-D):", "HIT" if (A and B and D) else "OPEN MISS")
