"""D: Abramsky-style naturality of copying, checked exhaustively in small toy categories.
Copy Delta_A is natural iff Delta_B o f == (f (x) f) o Delta_A for every process f: A -> B.
Set (functions), Rel (relations), FinStoch (stochastic maps) on a 2-element object; plus where it fails."""
import itertools, numpy as np
X=[0,1]
def rel_compose_delta_after(R):  # Delta o R : pairs (x,(y,y)) with (x,y) in R
    return {(x,(y,y)) for (x,y) in R}
def rel_RR_after_delta(R):
    return {(x,(y1,y2)) for x in X for y1 in X for y2 in X if (x,y1) in R and (x,y2) in R}
allpairs=[(x,y) for x in X for y in X]
nat=0; fails=[]
for bits in itertools.product([0,1],repeat=4):
    R={p for p,b in zip(allpairs,bits) if b}
    if rel_compose_delta_after(R)==rel_RR_after_delta(R): nat+=1
    else: fails.append(sorted(R))
print(f"Rel on 2: copy natural for {nat}/16 relations; natural exactly for the partial functions? fails e.g. {fails[:3]}")
funcs=[R for R in [set(zip(X,f)) for f in itertools.product(X,repeat=2)]]
print("Set on 2: copy natural for all 4 functions:", all(rel_compose_delta_after(R)==rel_RR_after_delta(R) for R in funcs))
D=np.zeros((4,2)); D[0,0]=1; D[3,1]=1
rng=np.random.default_rng(0); ok=0; okdet=0; n=0
for _ in range(2000):
    M=rng.random((2,2)); M/=M.sum(0)
    ok+= np.allclose(D@M, np.kron(M,M)@D)
for f in itertools.product(X,repeat=2):
    M=np.zeros((2,2)); M[list(f),[0,1]]=1; okdet+=np.allclose(D@M,np.kron(M,M)@D)
print(f"FinStoch on 2: copy natural for {ok}/2000 random stochastic maps, {okdet}/4 deterministic maps")
print("Reading: copy is natural exactly on the deterministic (sharp-record) maps. Indefinite processes break it.")
print("Abramsky 2009: in a compact closed category, a natural diagonal forces triviality. Rel is compact closed and its copy is")
print("not natural (above); FinStoch is not compact closed (its 'cap' is not a stochastic map), yet copy still fails naturality.")
print("So: failure of uniform copying already happens in classical-probabilistic and relational worlds; it is the INDEFINITE")
print("processes that break it, matching A1 (self-reference forces indefinite states).")
