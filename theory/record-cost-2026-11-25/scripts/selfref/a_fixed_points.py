"""A: self-tracking loops and fixed points (Lawvere / trace route), no physics.
A self-tracking loop: a record x is fed back through a process f; consistency demands x = f(x).
(1) Deterministic finite worlds (Set): fixed-point-free processes exist for n>=2, so 'every loop is consistent' fails.
(2) Convex (probabilistic) worlds: every stochastic process has a fixed state (Brouwer / Perron-Frobenius).
    The flip's fixed state is exactly (1/2,1/2): the 'liar' bit is forced to a fair value.
(3) The record copier that copies sharp records 0,1 does NOT clone that fixed state (linearity), but does broadcast it.
(4) Rel and qubit analogues.
"""
import itertools, numpy as np
rng=np.random.default_rng(1)
print("(1) Set: fraction of endomaps of an n-set with a fixed point (exhaustive for n<=6)")
for n in range(1,7):
    tot=0; fp=0
    for f in itertools.product(range(n),repeat=n):
        tot+=1; fp+= any(f[i]==i for i in range(n))
    print(f"   n={n}: {fp}/{tot} = {fp/tot:.4f}   (1-1/e = {1-np.exp(-1):.4f}); NOT-like derangements exist: {fp<tot}")
print("   => for n>=2 no rule assigns a consistent state to every loop; (Set, x) admits no trace (Hasegawa: trace on cartesian = Conway fixpoint operator).")

print("(2) Convex worlds: random stochastic maps on n outcomes always have a fixed distribution")
worst=0
for n in [2,3,5,8]:
    for _ in range(2000):
        M=rng.random((n,n)); M/=M.sum(0,keepdims=True)   # column stochastic
        w,v=np.linalg.eig(M); k=np.argmin(abs(w-1)); p=np.real(v[:,k]); p/=p.sum()
        worst=max(worst,np.abs(M@p-p).max(), -min(0,p.min()))
print(f"   max residual |Mp-p| or negativity over 8000 maps: {worst:.2e}")
NOT=np.array([[0,1],[1,0]])
w,v=np.linalg.eig(NOT); p=np.real(v[:,np.argmin(abs(w-1))]); p/=p.sum()
print(f"   fixed state of the flip: {p}  -> P(record=1) = {p[1]:.3f} exactly; any GPT: e(Tw)=1-e(w), Tw=w => e(w)=1/2")

print("(3) Copier of sharp records, extended linearly, on the liar's fixed state")
d0=np.array([1,0.]); d1=np.array([0,1.])
D=np.zeros((4,2)); D[:,0]=np.kron(d0,d0); D[:,1]=np.kron(d1,d1)   # copy map delta_i -> delta_i delta_i
u=np.array([.5,.5]); Tu=D@u
print(f"   D(u) = {Tu}  vs  u(x)u = {np.kron(u,u)}  -> cloned? {np.allclose(Tu,np.kron(u,u))}")
marg1=Tu.reshape(2,2).sum(1); marg2=Tu.reshape(2,2).sum(0)
print(f"   marginals of D(u): {marg1}, {marg2} -> broadcast? {np.allclose(marg1,u) and np.allclose(marg2,u)}")
print("   naturality check D o NOT == (NOT x NOT) o D on all states:", np.allclose(D@NOT, np.kron(NOT,NOT)@D),
      "(copy IS natural w.r.t. the flip; it fails only on the non-sharp fixed state as a CLONE)")

print("(4a) Rel on {0,1}: states = subsets; nonempty fixed subsets of the flip relation:")
subsets=[set(),{0},{1},{0,1}]
flip=lambda S:{1-x for x in S}
print("   ",[sorted(S) for S in subsets if S and flip(S)==S])
delta=lambda S:{(x,x) for x in S}; prod=lambda S:{(x,y) for x in S for y in S}
print("    diagonal on {0,1}:",sorted(delta({0,1})),"  vs  {0,1}x{0,1}:",sorted(prod({0,1})))
print("(4b) Qubit: X fixes |+>; z-copier |i>->|ii> on |+> gives Bell state")
plus=np.array([1,1])/np.sqrt(2); C=np.zeros((4,2)); C[0,0]=1; C[3,1]=1
print("    overlap |<++|C|+>|^2 =", round(abs(np.kron(plus,plus)@(C@plus))**2,4), "(clone would be 1)")
print("(5) Every random CPTP qubit map has a fixed state (Brouwer), so the trace/Lawvere obstruction is DISSOLVED, not triggered, in convex worlds")
def rand_channel(d=2,k=3):
    G=rng.normal(size=(k*d,d))+1j*rng.normal(size=(k*d,d)); Q,_=np.linalg.qr(G); return [Q[i*d:(i+1)*d,:] for i in range(k)]
res=0
for _ in range(500):
    K=rand_channel(); S=sum(np.kron(k,k.conj()) for k in K)
    w,v=np.linalg.eig(S); r=v[:,np.argmin(abs(w-1))].reshape(2,2); r=r/np.trace(r)
    res=max(res,abs(sum(k@r@k.conj().T for k in K)-r).max())
print(f"   max fixed-state residual over 500 random channels: {res:.1e}")
