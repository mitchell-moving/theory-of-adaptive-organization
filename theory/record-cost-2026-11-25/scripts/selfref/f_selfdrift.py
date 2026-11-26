"""F: price the drift a tracker causes in its own record by reading it (round 3).
Task (persistent later questions): a phase theta (uniform) is stored ONCE in a capacity-N=2 system.
Questions phi_1..phi_T (uniform, independent) arrive over time; each answer sign cos(theta - phi_t) is given
by READING the stored system (reading is a write into the tracker, and it disturbs the store). No refresh.
Report the average error over the first T questions.
 - square (gbit): store the vertex of theta's quadrant; answering phi needs an edge effect. Affine relation
   v1+v3 = v2+v4 forces ANY instrument element that reveals the edge with certainty to output the same state on
   the two vertices of the edge (PROVED-TOY, checked below), so after the first read only one bit is left.
   Strategy value is ACHIEVABLE (an upper bound on the square's optimal error).
 - disk/ball (same for planar phases): store the pure state at angle theta; read with a measurement of strength
   eta along phi_t (effects (1 +- eta n.r)/2; Kraus = sqrt of effects, i.e. the qubit instrument: this BORROWS the
   quantum instrument rule for post-measurement states, flagged), answer by Bayes from all outcomes.
 - classical 1 bit (half-circle) and classical 2 bits (quadrant), which never disturb.
"""
import numpy as np
rng=np.random.default_rng(7)
# --- affine obstruction for the square, checked by linear algebra
V=np.array([[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]],float).T   # columns: vertices (x,y,1) in order around the square
# edge effect e = (1+x)/2 picks vertices 0 and 3. Instrument element T_+ with T_+(v)=e(v)*w_v. Linearity + v0+v2=v1+v3:
print("square affine relation v0+v2 == v1+v3:", np.allclose(V[:,0]+V[:,2],V[:,1]+V[:,3]))
print("  => T_+(v0)+T_+(v2) = T_+(v1)+T_+(v3); e(v1)=e(v2)=0 so T_+(v1)=T_+(v2)=0 (positivity), hence w_v0 = w_v3: the read erases the other bit.")
# --- simulation
G=720; grid=np.linspace(0,2*np.pi,G,endpoint=False)
sx=np.array([[0,1],[1,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
def proj_state(a): return 0.5*(np.eye(2)+np.cos(a)*sz+np.sin(a)*sx)
def kraus(eta,a):
    n=np.cos(a)*sz+np.sin(a)*sx
    ks=[]
    for s in (+1,-1):
        E=0.5*(np.eye(2)+s*eta*n); w,U=np.linalg.eigh(E); ks.append(U@np.diag(np.sqrt(np.clip(w,0,None)))@U.conj().T)
    return ks
def run_disk(eta,T,trials=1500):
    errs=np.zeros(T)
    rhos0=np.array([proj_state(a) for a in grid])
    for _ in range(trials):
        th=rng.uniform(0,2*np.pi); rho=proj_state(th)
        cond=rhos0.copy()            # unnormalised conditional states for each grid theta (posterior weights = traces)
        for t in range(T):
            phi=rng.uniform(0,2*np.pi); K=kraus(eta,phi)
            # Bayes answer before reading? we read first, then answer with posterior incl. this outcome
            p_plus=np.real(np.trace(K[0]@rho@K[0].conj().T)); s=0 if rng.random()<p_plus else 1
            rho=K[s]@rho@K[s].conj().T; rho/=np.trace(rho)
            cond=np.einsum('ij,gjk,lk->gil',K[s],cond,K[s].conj()); w=np.real(np.einsum('gii->g',cond)); w/=w.sum()
            score=np.sum(w*np.sign(np.cos(grid-phi)))
            ans=np.sign(score) if score!=0 else 1
            errs[t]+= ans!=np.sign(np.cos(th-phi))
    return errs/trials
def run_square(T,trials=20000):
    errs=np.zeros(T)
    for _ in range(trials):
        th=rng.uniform(0,2*np.pi); q=int(th//(np.pi/2)); c=(q+.5)*np.pi/2
        known=None
        for t in range(T):
            phi=rng.uniform(0,2*np.pi)
            if t==0:
                # read the edge effect splitting the 4 quadrant centres by the line orthogonal to phi; outcome = answer for centre c
                ans=np.sign(np.cos(c-phi)); errs[t]+=ans!=np.sign(np.cos(th-phi))
                # what survives: the two quadrants on the answered side -> half circle centred at phi or phi+pi
                known=phi if ans>0 else phi+np.pi
                # the half circle is the union of the 2 quadrants whose centres satisfy the answer; its centre:
                cs=[(k+.5)*np.pi/2 for k in range(4) if np.sign(np.cos((k+.5)*np.pi/2-phi))==ans]
                known=np.angle(np.exp(1j*cs[0])+np.exp(1j*cs[1]))
            else:
                ans=np.sign(np.cos(known-phi)); errs[t]+=ans!=np.sign(np.cos(th-phi))
    return errs/trials
T=6
sq=run_square(T); print("\nper-question error by question index t=1..6")
print("  square (achievable)  :", np.round(sq,3), " avg over 6:", round(sq.mean(),3))
print("  classical 1 bit      :", [0.25]*T)
print("  classical 2 bits     :", [0.125]*T, "(capacity price 2)")
best=None
for eta in [1.0,0.8,0.6,0.4,0.25]:
    d=run_disk(eta,T); print(f"  disk/ball eta={eta:4.2f}  :", np.round(d,3), " avg over 6:", round(d.mean(),3))
    if best is None or d.mean()<best[1]: best=(eta,d.mean())
print("best disk strength over the grid:",best)
