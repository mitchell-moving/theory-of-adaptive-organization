"""Pilot (seed 106, a pilot seed; test seeds are 301-305). Prints ONLY extinction for the evolving arms at full
length, and the designed references (fixed monocultures) for the action-anticipation bar."""
import json, numpy as np
from multiprocessing import Pool
import p1s3_sim as m
W = dict(sig_f=1.0, c=0.02, x_r=3.0); T = 30000.0
def P_of(cell):
    P = dict(m.BASE); P.update(W)
    if cell == "U_on": P["tau_f"] = 0.2
    if cell == "High_on": P["c"] = 0.2
    return P
def evo(cell):
    arm = {"P_on": "on", "P_off": "off", "P_sieve": "sieve", "U_on": "on", "High_on": "on"}[cell]
    r = m.run(P_of(cell), T, 106, "evolve", arm=arm, snap=False); return cell, r["extinct_t"]
def ref(kind):
    P = P_of("P_on"); g = m.designed(P, kind, 0.1 if kind != "sieve" else 0)
    r = m.run(P, 5000.0, 106, "fixed", founders=np.array([g]*250), labels=np.zeros(250, int)); return kind, r.get("dA_u"), r["extinct_t"]
if __name__ == "__main__":
    with Pool(8) as pool:
        a = pool.map_async(evo, ["P_on", "P_off", "P_sieve", "U_on", "High_on"]); b = pool.map_async(ref, ["judge", "reflex", "sieve"])
        ev, rf = a.get(), b.get()
    print("EXTINCTION ONLY (evolving arms, T=30000, seed 106):", ev)
    print("DESIGNED REFERENCES dA_u (fixed monocultures, T=5000, seed 106):", rf)
    json.dump(dict(extinction=ev, refs=rf), open("pilot.json", "w"))
