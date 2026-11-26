"""Route (a): Spekkens elementary system. Checks, by exhaustive bipartite matching,
whether any reversible map (permutation of joint ontic states) clones the 6 pure
epistemic states; and whether lifting the knowledge-balance restriction (allowing
singleton epistemic states) makes copying possible. Also the 'priced' version."""
import itertools, numpy as np
from scipy.optimize import linear_sum_assignment

ontic = [1,2,3,4]
pure_epi = [frozenset(p) for p in itertools.combinations(ontic,2)]   # 6 pure epistemic states
blank = frozenset({1,2})

def clone_possible(states, blank):
    """Is there a permutation P of ontic pairs with P(S x blank) = S x S for all S?
    Necessary and sufficient here: each input point a must go to a point in the
    intersection of all targets S x S over S containing a's first coordinate (and
    a's 2nd in blank). Build allowed-image sets, then test for a perfect matching."""
    pts = [(a,b) for a in ontic for b in ontic]
    allowed = {}
    for p in pts:
        sets = [S for S in states if p[0] in S and p[1] in blank]
        if not sets:
            allowed[p] = set(pts)           # unconstrained
        else:
            tgt = set(pts)
            for S in sets:
                tgt &= {(x,y) for x in S for y in S}
            allowed[p] = tgt
    # every S x blank must map ONTO S x S: sizes match (|S|*|blank| vs |S|^2) only if |S|==|blank|
    cost = np.array([[0 if q in allowed[p] else 1 for q in pts] for p in pts])
    r,c = linear_sum_assignment(cost)
    ok = cost[r,c].sum()==0
    # also check bijectivity onto S x S for each S (images of S x blank equal S x S)
    if ok:
        perm = {pts[i]:pts[j] for i,j in zip(r,c)}
        for S in states:
            img = {perm[(a,b)] for a in S for b in blank}
            if img != {(x,y) for x in S for y in S}: ok=False
    return ok, {p:sorted(allowed[p]) for p in pts if p[1] in blank}

ok, allowed = clone_possible(pure_epi, blank)
print("KB-respecting pure epistemic states (6 pairs): perfect cloner exists?", ok)
for p,a in allowed.items():
    print("  input ontic",p,"-> allowed images",a)

# Lift knowledge balance: states are ontic singletons, blank is a known ontic state {1}
sing = [frozenset({x}) for x in ontic]
ok2,_ = clone_possible(sing, frozenset({1}))
print("Singleton (maximal-knowledge) states with blank {1}: cloner exists?", ok2,
      "(ontic CNOT-like permutation)")

# Two disjoint (orthogonal-like) epistemic states {1,2},{3,4}: copyable?
ok3,_ = clone_possible([frozenset({1,2}),frozenset({3,4})], blank)
print("Disjoint pair {12},{34} only: cloner exists?", ok3)

# Priced KB: if sharpening a pair to a singleton costs c per extra bit, a
# measure-and-prepare cloner (learn the ontic state, then prepare two copies)
# costs c per input bit acquired; under strict KB the cost is infinite.
for c in [0.1,1,10]:
    print(f"priced KB, c={c}: measure-prepare clone cost = {c*1:.1f} (1 extra bit) -> finite; strict KB = infinite")
