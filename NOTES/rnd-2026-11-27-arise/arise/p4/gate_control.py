import numpy as np
from multiprocessing import Pool
import p4_sim as m, gate as g
def one(a):
    mode, seed = a; P = dict(m.BASE); P.update(delta=0.1, P=20.0, c=0.2, T=1000.0)
    if mode == "random": P["cue_mode"] = "random"
    else: P["reader"] = False
    init = np.r_[g.init_state("reader",100), g.init_state("non",100)]; lab = np.r_[np.ones(100,int), np.zeros(100,int)]
    return mode, seed, m.run(P, seed, init=init, labels=lab)["label_freq"]
if __name__ == "__main__":
    with Pool(8) as p: out = p.map(one, [(k, s) for k in ["random", "readeroff"] for s in range(101, 106)])
    for k in ["random", "readeroff"]:
        fr = [o[2] for o in out if o[0] == k]; n = sum(f >= 0.75 for f in fr)
        print(k, [round(f, 2) for f in fr], f"{n}/5", "OK" if n <= 2 else "CONTROL FAILS")
