"""Route (e): self-reference. Finite-set forms of Lawvere's fixed-point theorem / Cantor diagonal,
the self-copy counting bound, and whether either restricts copying single distinctions."""
import itertools, numpy as np
rng=np.random.default_rng(3)
# (1) Lawvere contrapositive on finite sets: Y={0,1} has the fixed-point-free map NOT, so no
# A -> Y^A is point-surjective. Diagonal predicate d(a)=NOT phi(a)(a) is never in the image.
for n in [3,4,5]:
    A=range(n); misses=0
    for _ in range(2000):
        phi=rng.integers(0,2,(n,n))          # phi(a) is a predicate on A (row a)
        d=1-np.diag(phi)
        if any((phi[a]==d).all() for a in A): misses+=1
    print(f"(1) |A|={n}: diagonal predicate found in image of a random A->2^A in {misses}/2000 trials (expect 0)")
# (2) Self-copy counting: universe = recorder R (m bits) x rest X (k bits). A reversible map
# (permutation) that writes a full copy of (R,X) into R is impossible when m < m+k (pigeonhole).
# But R CAN copy any chosen m bits of X exactly (CNOTs). Exhaustive check on m=1,k=2:
m,k=1,2
states=list(itertools.product([0,1],repeat=m+k))
def cnot_copy(s,j):   # copy bit j of X into R (R starts at 0)
    return (s[0]^s[1+j],)+s[1:]
for j in range(k):
    ok=all(cnot_copy((0,)+x,j)[0]==x[j] for x in itertools.product([0,1],repeat=k))
    print(f"(2) recorder bit copies rest-bit {j} exactly via a reversible CNOT: {ok}")
print(f"(2) a 1-bit recorder cannot hold a copy of the 3-bit whole: 2^{m} < 2^{m+k} states (counting)")
# (3) Budget compromise (classical): recorder of m bits, rest has k fine bits; queries are
# coarse (parity-free 'which half', the top bit) w.p. 1-f, or fine (a uniformly random lower
# bit) w.p. f. Best allocation: record top bit first, then fine bits; error vs m.
k=6
for f in [0.2,0.8]:
    row=[]
    for mm in range(0,k+1):
        # record top bit + (mm-1) fine bits
        if mm==0: err=0.5
        else:
            err=(1-f)*0+f*((k-1-(mm-1))/(k-1))*0.5
        row.append(f"m={mm}:{err:.3f}")
    print(f"(3) fine-query share f={f}: error by recorder size ", " ".join(row))
print("(3) Reading: the cheapest bounded self-record keeps coarse distinctions and leaves fine ones")
print("    UNRECORDED; every fine bit stays individually copyable (CNOT). That is 'not all at once',")
print("    not no-cloning.")
