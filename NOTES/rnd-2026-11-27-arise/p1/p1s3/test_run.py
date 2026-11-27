"""P1-S3 locked test runner: world chosen by the gate; seeds 301-305; T = 30000."""
import sys, json
import p1s3_sim as m
W = dict(sig_f=1.0, c=0.02, x_r=3.0)
cell, seed, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
P = dict(m.BASE); P.update(W)
if cell == "U_on": P["tau_f"] = 0.2
if cell == "High_on": P["c"] = 0.2
arm = {"P_on": "on", "P_off": "off", "P_sieve": "sieve", "U_on": "on", "High_on": "on"}[cell]
r = m.run(P, 30000.0, seed, "evolve", arm=arm, snap=True); r.update(cell=cell, seed=seed)
json.dump(r, open(out, "w"), indent=1, default=float)
