"""Toy 3 (Q1, Q4, steering task 1): two gbits (boxworld, maximal 'no-signalling' composite).
(a) Enumerate ALL linear symmetries (reversible transformations) of the 2-gbit state space, via
    combinatorial automorphisms of the vertex-facet incidence graph, each checked for linearity.
    Expectation from Gross, Mueller, Colbeck, Dahlsten 2010 (PRL 104:080402): only local ops + swap (order 8*8*2=128).
(b) Check whether ANY reversible map makes a record: maps A=D(s,t) (x=0 answer s, x=1 answer t), B=blank
    to a joint state where B's y=0 answer equals s (or 1-s) for both s.
(c) Proof check of the affine obstruction: a positive linear map that writes A's x=0 answer onto a blank B
    and leaves A unchanged cannot exist (gbit vertices are affinely dependent: D00+D11 = D01+D10).
(d) LP: over ALL positive linear maps that make the x=0 record perfectly, the best retained information
    about A's x=1 answer t, measured (i) over all classical wirings of local measurements, (ii) over all
    effects of the maximal composite (dual cone of product effects). Classical analogue retains t fully.
Record-cost primitive: kappa per bit of t destroyed (it has to be re-acquired). No heat used.
"""
import itertools, json, numpy as np
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from scipy.optimize import linprog

idx = lambda a, b, x, y: ((a*2+b)*2+x)*2+y
def table(f):
    p = np.zeros(16)
    for a, b, x, y in itertools.product(range(2), repeat=4): p[idx(a, b, x, y)] = f(a, b, x, y)
    return p
def local_det(al, be):  # al=(a(x=0),a(x=1)), be=(b(y=0),b(y=1))
    return table(lambda a, b, x, y: float(a == al[x] and b == be[y]))
def pr(al, be, g):
    return table(lambda a, b, x, y: 0.5*float((a ^ b) == ((x*y) ^ (al*x) ^ (be*y) ^ g)))

locs = [(al, be) for al in itertools.product(range(2), repeat=2) for be in itertools.product(range(2), repeat=2)]
V = [local_det(al, be) for al, be in locs] + [pr(al, be, g) for al, be, g in itertools.product(range(2), repeat=3)]
V = np.array(V)  # 24 x 16
names = [f"L{al}{be}" for al, be in locs] + [f"PR{al}{be}{g}" for al, be, g in itertools.product(range(2), repeat=3)]
out = {}
# --- (a) symmetries: backtracking over images of an affine basis, pruned by the vertex-pair incidence invariant
Z = (np.abs(V) < 1e-12).astype(int)          # vertex-facet incidence
C = Z @ Z.T                                   # common-facet counts (preserved by any symmetry)
basis = []
for i in range(24):
    if np.linalg.matrix_rank(V[basis + [i]]) > len(basis): basis.append(i)
assert len(basis) == 9
Vp = np.linalg.pinv(V[basis].T)
syms = []; ncomb = 0
def bt(assign):
    global ncomb
    k = len(assign)
    if k == 9:
        ncomb += 1
        L = V[assign].T @ Vp
        img = (L @ V.T).T
        perm = []
        for w in img:
            d = np.abs(V - w).max(axis=1); j = int(np.argmin(d))
            if d[j] > 1e-9: return
            perm.append(j)
        if len(set(perm)) == 24: syms.append((perm, L))
        return
    for j in range(24):
        if j in assign or C[j, j] != C[basis[k], basis[k]]: continue
        if all(C[j, assign[m]] == C[basis[k], basis[m]] for m in range(k)): bt(assign + [j])
bt([])
out["candidate_basis_assignments_checked"] = ncomb
out["linear_symmetries"] = len(syms)
# local-ness test: does the B-marginal of the image of a product vertex depend on A's input?
def bmarg(p):  # P(b|y), with x=0 (no-signalling makes x irrelevant)
    return np.array([[p[idx(0, b, 0, y)] + p[idx(1, b, 0, y)] for b in range(2)] for y in range(2)])
def amarg(p):
    return np.array([[p[idx(a, 0, x, 0)] + p[idx(a, 1, x, 0)] for a in range(2)] for x in range(2)])
blank = (0, 0)
nonlocal_maps = 0; record_makers = 0; product_to_pr = 0; moves_not_copies = set()
for perm, L in syms:
    imgs = {al: L @ local_det(al, blank) for al in itertools.product(range(2), repeat=2)}
    bm = {al: bmarg(imgs[al]) for al in imgs}
    if any(np.abs(bm[al] - bm[(0, 0)]).max() > 1e-9 for al in bm): nonlocal_maps += 1
    for t in range(2):
        y0 = [bm[(s, t)][0, 1] for s in range(2)]  # P(b=1|y=0) for s=0,1
        # record = A keeps a sharp x-answer that still tells s AND B's y=0 answer tells s
        a_keeps = any(all(abs(amarg(imgs[(s, t)])[xx, 1] - (s ^ fl)) < 1e-9 for s in range(2)) for xx in range(2) for fl in range(2))
        b_has = (abs(y0[0]) < 1e-9 and abs(y0[1]-1) < 1e-9) or (abs(y0[0]-1) < 1e-9 and abs(y0[1]) < 1e-9)
        if a_keeps and b_has: record_makers += 1
        if b_has and not a_keeps: moves_not_copies.add(tuple(perm))
    if any(perm[i] >= 16 for i in range(16)): product_to_pr += 1
out["symmetries_where_B_image_depends_on_A_input (includes swaps)"] = nonlocal_maps
out["symmetries_that_write_A_x0_answer_into_blank_B"] = record_makers
out["symmetries_mapping_a_product_vertex_to_a_PR_box"] = product_to_pr
out["symmetries_that_MOVE_A_answer_into_B_leaving_A_without_it (swap family)"] = len(moves_not_copies)
# --- (c) affine relation used in the obstruction proof
D = {al: local_det(al, blank) for al in itertools.product(range(2), repeat=2)}
out["affine_relation_D00+D11-D01-D10_norm"] = float(np.abs(D[(0, 0)] + D[(1, 1)] - D[(0, 1)] - D[(1, 0)]).max())
# --- (d) LP over positive linear maps T (16x16) that make the x=0 record perfectly
NSrows = []
for a, x in itertools.product(range(2), repeat=2):   # no-signalling equalities on output tables
    r = np.zeros(16); 
    for b in range(2): r[idx(a, b, x, 0)] += 1; r[idx(a, b, x, 1)] -= 1
    NSrows.append(r)
for b, y in itertools.product(range(2), repeat=2):
    r = np.zeros(16)
    for a in range(2): r[idx(a, b, 0, y)] += 1; r[idx(a, b, 1, y)] -= 1
    NSrows.append(r)
for x, y in itertools.product(range(2), repeat=2):
    r = np.zeros(16)
    for a, b in itertools.product(range(2), repeat=2): r[idx(a, b, x, y)] = 1
    NSrows.append(("norm", r))
def lp_constraints():
    Aeq, beq, Aub, bub = [], [], [], []
    for v in V:  # image T v: positivity, NS, normalisation
        for k in range(16):
            row = np.zeros(256); row[k*16:(k+1)*16] = -v; Aub.append(row); bub.append(0)
        for r in NSrows:
            if isinstance(r, tuple):
                row = np.zeros(256)
                for k in range(16): row[k*16:(k+1)*16] = r[1][k]*v
                Aeq.append(row); beq.append(1)
            else:
                row = np.zeros(256)
                for k in range(16): row[k*16:(k+1)*16] = r[k]*v
                Aeq.append(row); beq.append(0)
    for (s, t), v in D.items():  # perfect record: P(b != s | y=0) = 0 for all a, x
        for a, x in itertools.product(range(2), repeat=2):
            k = idx(a, 1-s, x, 0); row = np.zeros(256); row[k*16:(k+1)*16] = v; Aeq.append(row); beq.append(0)
    return np.array(Aeq), np.array(beq), np.array(Aub), np.array(bub)
Aeq, beq, Aub, bub = lp_constraints()
def success_row(decoder):
    """decoder(p_table)-> linear functional: average over s,t of P(guess t)."""
    c = np.zeros(256)
    for (s, t), v in D.items():
        w = decoder(t)  # functional on output table (16)
        for k in range(16): c[k*16:(k+1)*16] += 0.25*w[k]*v
    return c
best = (0, None)
decs = []
# non-adaptive: settings (x,y), guess f(a,b)
for x, y in itertools.product(range(2), repeat=2):
    for f in itertools.product(range(2), repeat=4):
        decs.append(("nonadaptive", x, y, f))
# adaptive A first: x, then y=g(a), guess f(a,b)
for x in range(2):
    for g in itertools.product(range(2), repeat=2):
        for f in itertools.product(range(2), repeat=4):
            decs.append(("A-first", x, g, f))
for y in range(2):
    for g in itertools.product(range(2), repeat=2):
        for f in itertools.product(range(2), repeat=4):
            decs.append(("B-first", y, g, f))
def mkdec(d):
    def dec(t):
        w = np.zeros(16)
        for a, b in itertools.product(range(2), repeat=2):
            if d[0] == "nonadaptive": x, y = d[1], d[2]
            elif d[0] == "A-first": x, y = d[1], d[2][a]
            else: y, x = d[1], d[2][b]
            if d[3][a*2+b] == t: w[idx(a, b, x, y)] += 1
        return w
    return dec
import time; t0=time.time()
results = []
for d in decs:
    c = success_row(mkdec(d))
    r = linprog(-c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(-5, 5)]*256, method="highs")
    if r.status == 0:
        results.append((-r.fun, d, r.x))
results.sort(key=lambda z: -z[0])
out["record_LP_feasible"] = len(results) > 0
out["best_wiring_success_for_t"] = round(results[0][0], 6) if results else None
out["best_wiring"] = str(results[0][1]) if results else None
# (ii) full effect set for the best map: base-norm advantage between outputs for t=0 and t=1 (s fixed)
T = results[0][2].reshape(16, 16)
Pi = np.eye(16)
def best_effect_gap(p0, p1):
    # e = sum c_k pi_k (c>=0), u - e = sum d_k pi_k (d>=0) on the NS subspace; enforce on all 24 vertices
    # variables c(16), d(16): constraint e(v)+ (u-e)(v) = 1 for all vertices v -> (c+d).v = 1
    A_eq = np.array([np.r_[v, v] for v in V]); b_eq = np.ones(24)
    obj = -np.r_[p0 - p1, np.zeros(16)]
    r = linprog(obj, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)]*32, method="highs")
    return -r.fun
gaps = {s: best_effect_gap(T @ D[(s, 0)], T @ D[(s, 1)]) for s in range(2)}
out["full_effect_guess_success_for_t_given_best_wiring_map"] = {str(s): round(0.5 + 0.5*g, 6) for s, g in gaps.items()}
# Also: maximise the full-effect gap directly with a fixed effect family (alternating, few rounds) for robustness
out["classical_analogue"] = "A = two classical bits (s,t) (4-simplex): copy s onto blank B with a controlled flip; t untouched; success for t = 1.0; reversible"
json.dump(out, open("outputs/t3_boxworld.json", "w"), indent=1)
print(json.dumps(out, indent=1))
