"""Toy 3b: after an (irreversible) positive map T writes A's x=0 answer onto a blank B while keeping t recoverable,
can ANY positive map N undo it (N(T(D(s,t) x blank)) = D(s,t) x blank)? If yes, a classical-style
'copy, use, uncopy' cycle (Bennett) costs nothing in boxworld either, despite Gross et al.'s trivial reversible group.
We test N for the T found by each of the best wiring LPs, and also a joint relaxation:
any positive T that copies + any positive N with N(Y_st) = D_st x blank where Y_st are free joint states with B y=0 = s."""
import itertools, json, numpy as np
from scipy.optimize import linprog
src = open('t3_boxworld.py').read()
exec(src.split("# --- (a) symmetries")[0])
blank = (0, 0)
D = {al: local_det(al, blank) for al in itertools.product(range(2), repeat=2)}
exec("NSrows = []" + src.split("NSrows = []")[1].split("import time; t0=time.time()")[0])
def positive_map_constraints(nvars_offset=0, total=256):
    Aeq, beq, Aub, bub = [], [], [], []
    for v in V:
        for k in range(16):
            row = np.zeros(total); row[nvars_offset+k*16:nvars_offset+(k+1)*16] = -v; Aub.append(row); bub.append(0)
        for r in NSrows:
            row = np.zeros(total)
            if isinstance(r, tuple):
                for k in range(16): row[nvars_offset+k*16:nvars_offset+(k+1)*16] = r[1][k]*v
                Aeq.append(row); beq.append(1)
            else:
                for k in range(16): row[nvars_offset+k*16:nvars_offset+(k+1)*16] = r[k]*v
                Aeq.append(row); beq.append(0)
    return Aeq, beq, Aub, bub
D = {al: local_det(al, (0, 0)) for al in itertools.product(range(2), repeat=2)}
# Joint relaxation: unknowns N (256) and output states Y_st (4 x 16). Constraint N Y_st = D_st x blank is bilinear,
# so instead ask: is there a positive N and joint states Y_st in the 2-gbit polytope, B's y=0 answer = s,
# whose span relation matches the inputs (Y must satisfy Y00+Y11 = Y01+Y10, forced by linearity of T),
# with N(Y_st)=D_st? We parametrise Y_st as convex combos of the 24 vertices (weights w_st), then N Y_st = sum_i w_st,i N v_i:
# still bilinear. So we test the T's found by the wiring LPs (several), which is a sufficient-not-necessary check.
Aeq, beq, Aub, bub = lp_constraints()
decs = [("A-first", 1, (0, 1), f) for f in itertools.product(range(2), repeat=4)] + [("A-first", 1, (1, 0), f) for f in itertools.product(range(2), repeat=4)]
found = []
for d in decs:
    c = success_row(mkdec(d))
    for seed in range(3):
        cc = -c + 1e-3*np.random.default_rng(seed).normal(size=256)  # perturb to get different optimal T
        r = linprog(cc, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(-5, 5)]*256, method="highs")
        if r.status == 0 and (c @ r.x) > 0.999: found.append(r.x.reshape(16, 16))
res = []
for T in found[:20]:
    A2, b2, U2, ub2 = positive_map_constraints()
    for (st), v in D.items():
        y = T @ v
        for k in range(16):
            row = np.zeros(256); row[k*16:(k+1)*16] = y; A2.append(row); b2.append(v[k])
    r = linprog(np.zeros(256), A_ub=np.array(U2), b_ub=np.array(ub2), A_eq=np.array(A2), b_eq=np.array(b2), bounds=[(-20, 20)]*256, method="highs")
    res.append(r.status)
out = {"T_maps_tested": len(res), "uncopy_N_feasible_count": int(sum(1 for s in res if s == 0)), "lp_status_codes": res}
json.dump(out, open("outputs/t3b_uncopy.json", "w"), indent=1); print(out)
