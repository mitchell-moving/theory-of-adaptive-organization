"""B: copying that must work whatever the (unrecorded) drift has done.
GPT systems in homogeneous coords w=(1,r), r in R^d. Composite: local-tomographic tensor R^{(d+1)^2}
(only product states and product effects are used, so the no-go holds for ANY composite containing them).
Search for a LINEAR map T: R^{d+1} -> R^{(d+1)^2} (positivity not even required) such that
   T(w) = w (x) w  for every w in the drift orbit of the target states.
Least-squares residual 0 => linear copier exists; residual > 0 => none exists (stronger than no-cloning: even unphysical linear maps fail).
"""
import numpy as np
def hom(r): return np.concatenate([[1.0],np.asarray(r,float)])
def fit(states):
    W=np.array([hom(s) for s in states]).T                 # (d+1) x m
    Y=np.array([np.kron(hom(s),hom(s)) for s in states]).T # (d+1)^2 x m
    T,*_=np.linalg.lstsq(W.T,Y.T,rcond=None); T=T.T
    return np.abs(T@W-Y).max()
def rot2(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
def rotz(t): R=np.eye(3); R[:2,:2]=rot2(t); return R
ths=np.linspace(0,2*np.pi,24,endpoint=False)
cases=[]
cases.append(("classical bit (segment, d=1); dynamics {id,flip}; orbit of vertex = {0,1}", [[-1],[1]]))
tri=[np.array([np.cos(a),np.sin(a)]) for a in 2*np.pi*np.arange(3)/3]
cases.append(("classical trit (triangle, d=2); dynamics S3; orbit = 3 vertices", tri))
for n in [4,5,6,8]:
    cases.append((f"{n}-gon (d=2); dynamics C_{n}; orbit = {n} vertices", [rot2(2*np.pi*k/n)@[1,0] for k in range(n)]))
cases.append(("disk/rebit (d=2); continuous drift SO(2); orbit of z+ = circle (24 samples)", [rot2(t)@[1,0] for t in ths]))
cases.append(("disk, drift known to within +-0.1 rad; orbit = short arc (8 samples)", [rot2(t)@[1,0] for t in np.linspace(-.1,.1,8)]))
cases.append(("ball/qubit (d=3); drift about z; target z+ and z- (fixed points)", [[0,0,1],[0,0,-1]]))
cases.append(("ball; drift about z; target x+ (orbit = equator)", [rotz(t)@[1,0,0] for t in ths]))
cases.append(("ball; drift about z; target tilted state at 30deg from z (orbit = a latitude circle)", [rotz(t)@[np.sin(np.pi/6),0,np.cos(np.pi/6)] for t in ths]))
cases.append(("ball; drift SO(3) (no conserved axis); orbit of z+ = whole sphere (sampled)", [v/np.linalg.norm(v) for v in np.random.default_rng(0).normal(size=(40,3))]))
for name,st in cases:
    r=fit(st); print(f"{'COPIER EXISTS ' if r<1e-9 else 'NO COPIER     '} residual={r:.3e} | {name}")

print("\nGeneral 4-point argument (holds in any finite-dim GPT): an orbit of a compact connected drift through a moved point")
print("is a closed curve around its centroid c; points at phases 0,pi and pi/2,3pi/2 average to c, so")
print("T(c) = (p0p0+p2p2)/2 = (p1p1+p3p3)/2 is required; a product effect f(x)f separates them whenever f's slope differs on the two diameters.")
p=[rot2(t)@[1,0] for t in [0,np.pi/2,np.pi,3*np.pi/2]]
f=lambda r: 0.5*(1+r[0])           # an effect of the disk
lhs=(f(p[0])**2+f(p[2])**2)/2; rhs=(f(p[1])**2+f(p[3])**2)/2
print(f"   disk: (f(x)f) on clone-of-diameter-1 = {lhs:.3f}, on clone-of-diameter-2 = {rhs:.3f}  -> contradiction: {abs(lhs-rhs)>1e-9}")

print("\nDimension count: smallest state space with (i) finite capacity N, (ii) a continuous reversible drift moving some pure state,")
print("(iii) N jointly distinguishable pure states fixed by the drift (a copyable record that survives the drift).")
print("Claim [PROVED-TOY]: affine dimension d >= N+1. Table:")
rows=[("classical N-simplex","N-1","fails (no continuous symmetry)"),("disk/rebit, N=2","2","fails (SO(2) fixes only the centre)"),
      ("ball/qubit, N=2","3","meets d=N+1 with equality"),("double cone, N=2","3","meets (apexes fixed)"),("quantum, N levels","N^2-1",">= N+1, equality only N=2")]
for a,b,c in rows: print(f"   {a:22s} d={b:6s} {c}")

print("\nQuantum check: dimension of the connected drift group that fixes two basis states and acts nontrivially (Lie algebra count)")
def stab_dim(N,field):
    gens=[]
    for i in range(N):
        for j in range(i,N):
            if field=='R':
                if i!=j: A=np.zeros((N,N)); A[i,j]=1; A[j,i]=-1; gens.append(A)
            else:
                A=np.zeros((N,N),complex)
                if i==j: A[i,i]=1j; gens.append(A)
                else:
                    A[i,j]=1; A[j,i]=-1; gens.append(A.copy()); B=np.zeros((N,N),complex); B[i,j]=1j; B[j,i]=1j; gens.append(B)
    P=[np.diag([1.0 if k==m else 0 for k in range(N)]) for m in (0,1)]
    # constraints [X,P]=0 for both projectors; then quotient by multiples of identity (act trivially on states)
    M=np.array([np.concatenate([ (g@p-p@g).ravel() for p in P]) for g in gens]).T
    M=np.vstack([M.real,M.imag]) if np.iscomplexobj(M) else M
    null=len(gens)-np.linalg.matrix_rank(M,1e-9)
    triv=1 if field=='C' else 0
    return null-triv
for field in 'RC':
    for N in [2,3,4]:
        print(f"   {'real' if field=='R' else 'complex'} QM, N={N}: dim = {stab_dim(N,field)}")
