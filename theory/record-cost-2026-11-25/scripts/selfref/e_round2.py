"""Round 2 numerics.
E1  composite version of R3: connected drift that conserves a COMPLETE record (every state of a maximal
    distinguishable set) and still moves something. Lie-algebra dimension in real and complex QM, single and composite.
    Classical and boxworld: reversible groups are finite (permutations; Gross et al. 2010 for boxworld), so dim = 0.
E2  R2a re-check on multi-frequency orbits (where the round-1 four-point argument does not apply as written).
E3  discrete ticks: reversible finite worlds are periodic (Lean: perm_periodic); a finite-capacity tracker of an
    irrational rotation keeps a constant error forever unless it pays to re-acquire.
"""
import numpy as np, itertools
def stab_dim(N, field, fixed):
    """dim of {X in Lie(O(N)) or Lie(U(N)) : [X,P_i]=0 for i in fixed} modulo generators acting trivially (i*identity)."""
    gens=[]
    for i in range(N):
        for j in range(i,N):
            if field=='R':
                if i!=j: A=np.zeros((N,N)); A[i,j]=1; A[j,i]=-1; gens.append(A)
            else:
                if i==j: A=np.zeros((N,N),complex); A[i,i]=1j; gens.append(A)
                else:
                    A=np.zeros((N,N),complex); A[i,j]=1; A[j,i]=-1; gens.append(A)
                    B=np.zeros((N,N),complex); B[i,j]=1j; B[j,i]=1j; gens.append(B)
    P=[np.diag([1.0 if k==m else 0 for k in range(N)]) for m in fixed]
    if not P: null=len(gens)
    else:
        M=np.array([np.concatenate([(g@p-p@g).ravel() for p in P]) for g in gens]).T
        M=np.vstack([M.real,M.imag])
        null=len(gens)-np.linalg.matrix_rank(M,1e-9)
    return null-(1 if field=='C' else 0)
print("E1. dim of connected drift conserving a record (0 = no such drift)")
print("    system            record         real QM   complex QM   classical  boxworld")
for (NA,NB) in [(2,1),(3,1),(4,1),(2,2),(2,3),(3,3)]:
    N=NA*NB; lab=f"{NA}" if NB==1 else f"{NA}x{NB}"
    full=stab_dim(N,'R',range(N)), stab_dim(N,'C',range(N))
    part=stab_dim(N,'R',[0,1]), stab_dim(N,'C',[0,1])
    print(f"    {lab:6s} (N={N})   complete({N})     {full[0]:3d}        {full[1]:3d}          0         {'0' if NB>1 or NA==2 else '-'}")
    if N>2: print(f"    {lab:6s} (N={N})   two states       {part[0]:3d}        {part[1]:3d}          0         {'0' if NB>1 or NA==2 else '-'}")
print("    analytic: real QM complete record -> generators antisymmetric AND diagonal -> 0 for every N.")
print("              complex QM complete record -> diagonal phases U(1)^N / U(1) -> N-1 >= 1 for every N>=2.")
print("              quaternionic QM complete record -> Sp(1)^N -> 3N (passes; known to lack good composites).")

def hom(r): return np.concatenate([[1.0],np.asarray(r,float)])
def fit(states):
    W=np.array([hom(s) for s in states]).T; Y=np.array([np.kron(hom(s),hom(s)) for s in states]).T
    T,*_=np.linalg.lstsq(W.T,Y.T,rcond=None); return np.abs(T.T@W-Y).max()
print("\nE2. multi-frequency orbits t -> (cos t, sin t, r cos kt, r sin kt) (a circle group acting with weights 1 and k on R^4)")
ts=np.linspace(0,2*np.pi,64,endpoint=False)
for k,r in [(2,0.5),(3,0.5),(2,1.0)]:
    pts=[np.array([np.cos(t),np.sin(t),r*np.cos(k*t),r*np.sin(k*t)])/np.sqrt(1+r*r) for t in ts]
    q=[np.array([np.cos(t),np.sin(t),r*np.cos(k*t),r*np.sin(k*t)]) for t in [0,np.pi/2,np.pi,3*np.pi/2]]
    four=np.allclose(q[0]+q[2],q[1]+q[3])
    print(f"    weights (1,{k}), r={r}: quarter-phase identity p0+p2=p1+p3 holds? {four};  best linear copier residual = {fit(pts):.3e}")
print("    -> round-1 four-point step does not apply to these orbits, but no copier exists; the frequency-doubling proof (NOTE R2a') covers them.")

print("\nE3. discrete ticks")
rng=np.random.default_rng(3)
M=12; perm=rng.permutation(M); x=0; seen=[]
for t in range(200):
    seen.append(x); x=perm[x]
period=next(p for p in range(1,200) if all(seen[i]==seen[i+p] for i in range(len(seen)-p)))
print(f"    random reversible map on {M} states: orbit period = {period}; a tracker that has stored one period predicts with error 0 forever.")
golden=np.pi*(3-np.sqrt(5))
for m in [1,2,4,6]:
    bins=2**m; errs=[]
    for trial in range(4000):
        th0=rng.uniform(0,2*np.pi); est=(np.floor(th0/(2*np.pi/bins))+0.5)*(2*np.pi/bins)
        t=rng.integers(1,10**6); phi=rng.uniform(0,2*np.pi)
        truth=np.cos(th0+golden*t-phi)>0; guess=np.cos(est+golden*t-phi)>0
        errs.append(truth!=guess)
    print(f"    irrational rotation, tracker with {m} bits of phase, later question at a random tick up to 1e6: error = {np.mean(errs):.3f} (~1/(2*2^m)={1/(2*bins):.3f}); never decays without new acquisition")
