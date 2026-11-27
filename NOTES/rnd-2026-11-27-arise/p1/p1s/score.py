import json, glob
R = {}
for f in glob.glob("out/*.json"):
    r = json.load(open(f)); R[(r["cell"], r["seed"])] = r
cells = ["P_low_on","P_low_off","P_low_sieve","U_low_on","P_high_on"]
print("cell seed extinct births dA_z dA_u r2_body ruin_hz budget_hz h_mean logk_med")
for c in cells:
    for s in range(1,6):
        r = R[(c,s)]
        if r["extinct_t"] is not None: print(c,s,"EXTINCT",r["extinct_t"]); continue
        print(f"{c:12s} {s} - {r['births']:7d} {r['dA_z']:+.4f} {r['dA_u']:+.4f} {r['r2_body']:.4f} {r['ruin_hazard']:.5f} {r['budget_hazard']:.5f} {r['h_mean']:.3f} {r['logk_median']:+.3f}")
ok = lambda c,s: R[(c,s)]["extinct_t"] is None
def tally(name, fn):
    n = 0; det = []
    for s in range(1,6):
        try: v, p = fn(s)
        except Exception as e: v, p = None, False
        det.append((s, v, p)); n += bool(p)
    print(f"{name}: {n}/5 -> {'PASS' if n>=4 else 'FAIL'}  ", "; ".join(f"s{s}:{v if v is None else round(v,4)}{'+' if p else '-'}" for s,v,p in det))
    return n >= 4
g = lambda c,s,k: R[(c,s)][k]
A = tally("H-A dA_z(P_low_on)>=0.05", lambda s: (g("P_low_on",s,"dA_z"), ok("P_low_on",s) and g("P_low_on",s,"dA_z")>=0.05))
B = tally("H-B dA_z on-off>=0.03", lambda s: (g("P_low_on",s,"dA_z")-g("P_low_off",s,"dA_z"), ok("P_low_on",s) and ok("P_low_off",s) and g("P_low_on",s,"dA_z")-g("P_low_off",s,"dA_z")>=0.03))
C = tally("H-C ruin(on)/ruin(sieve)<=0.7", lambda s: (g("P_low_on",s,"ruin_hazard")/g("P_low_sieve",s,"ruin_hazard"), ok("P_low_on",s) and ok("P_low_sieve",s) and g("P_low_on",s,"ruin_hazard")<=0.7*g("P_low_sieve",s,"ruin_hazard")))
D = tally("H-D ruin(off)/ruin(on)>=1.3", lambda s: (g("P_low_off",s,"ruin_hazard")/g("P_low_on",s,"ruin_hazard"), ok("P_low_on",s) and ok("P_low_off",s) and g("P_low_off",s,"ruin_hazard")>=1.3*g("P_low_on",s,"ruin_hazard")))
E = tally("H-E h(P)-h(U)>=0.15", lambda s: (g("P_low_on",s,"h_mean")-g("U_low_on",s,"h_mean"), ok("P_low_on",s) and ok("U_low_on",s) and g("P_low_on",s,"h_mean")-g("U_low_on",s,"h_mean")>=0.15))
F = tally("H-F high price logk<=-3 & |dA_z|<0.05", lambda s: (g("P_high_on",s,"logk_median"), ok("P_high_on",s) and g("P_high_on",s,"logk_median")<=-3 and abs(g("P_high_on",s,"dA_z"))<0.05))
print("PRIMARY (Qe):", "HIT" if (A and B and C and D) else "OPEN MISS")
