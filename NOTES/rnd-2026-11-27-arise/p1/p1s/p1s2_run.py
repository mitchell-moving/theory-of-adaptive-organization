"""P1-S2 runner: identical locked model p1s_sim.py, one parameter changed: sig_f = 1.0 (was 1.5)."""
import sys, json, time
import p1s_sim as m
P = dict(m.PAR); P["sig_f"] = 1.0
cell, seed, T, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
t0 = time.time(); r = m.run(cell, seed, T, P); r["wall_s"] = round(time.time() - t0, 1); r["sig_f"] = 1.0
json.dump(r, open(out, "w"), indent=1)
