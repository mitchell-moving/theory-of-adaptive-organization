"""C: the cost picks which distinctions stay copyable.
Toy reading of J = kappa*I + q*kappa*P_D + w*L, on the ball (qubit-like) state space, geometry only:
an effect along unit vector a gives p = (1 + a.r)/2 (affine effects on the ball; no Hilbert space, no hbar, no heat).
- The world drifts by rotation about a conserved axis n (diffusion D of the phase: unknown to the tracker).
- Stakes: R readers each decide the sign of the s-component of a pure state +-s; s sits at angle beta from n.
- Design choice: the record basis, at angle alpha from n (in the n-s plane).
  stake term:   q*kappa*P_D,   P_D(alpha) = (1 - cos(beta - alpha))/2          (read the alpha-record, act on s)
  refresh term: w*R*D*sin^2(alpha)  (the drifting part of an alpha-record decays at rate ~ D*sin^2(alpha);
                each reader's copy must be refreshed; cf. B2: uncopyability over the orbit = sin^2(alpha)/2)
Minimise over alpha. Then compare state spaces under three cost terms.
"""
import numpy as np
from scipy.optimize import minimize_scalar
def alpha_star(beta,rho):  # rho = 2 w R D / (q kappa)
    J=lambda a: (1-np.cos(beta-a))/2 + rho*np.sin(a)**2/2
    return minimize_scalar(J,bounds=(0,beta),method='bounded').x
print("(1) optimal record angle alpha* (0 = conserved axis, beta = stake direction); beta = 60 deg")
beta=np.pi/3
for rho in [0,0.05,0.2,0.5,1,2,5,20]:
    a=alpha_star(beta,rho); print(f"   rho={rho:5.2f}  alpha*={np.degrees(a):5.1f} deg   P_D={(1-np.cos(beta-a))/2:.3f}")
print("   stationarity: sin(beta-alpha) = rho*sin(2alpha)/... ; alpha*=beta/2 exactly when rho = 1/(2cos(beta/2)) =",
      round(1/(2*np.cos(beta/2)),4), "-> check:", round(np.degrees(alpha_star(beta,1/(2*np.cos(beta/2)))),2),"deg")
print("   reading: rho grows with readers R and drift D. Many readers / fast drift push records onto the conserved (copyable) axis;")
print("   few readers / high stakes keep records on the stake direction, which is drifting and therefore not copyable for free.")
print("\n(2) readers needed before the record moves halfway to the conserved axis (beta=60deg, w*D/(q*kappa)=0.05):",
      int(np.ceil((1/(2*np.cos(beta/2)))/(2*0.05))))

print("\n(3) state-space comparison (capacity N=2 for all; all can store one bit). Terms per unit time:")
print("    irreversibility to follow continuous drift: lam*2*Theta^2/V for spaces with no continuous reversible group (sibling C3, TUR) ;")
print("    record term: w*R*D if no record survives the drift (no drift-fixed distinguishable pair), else 0;")
print("    dimension price (rival pricing, sibling OM3): kK*log2(K), K = affine dim + 1.")
spaces={'classical bit (segment)':(1,False,True),'square':(2,False,True),'disk/rebit':(2,True,False),'ball/qubit':(3,True,True)}
def J(sp,lam,Theta,V,w,R,D,kK):
    d,cont,rec=spaces[sp]; K=d+1
    return (0 if cont else lam*2*Theta**2/V) + (0 if rec else w*R*D) + kK*np.log2(K)
for (lam,Theta,V,w,R,D,kK) in [(0.05,1,0.1,0.1,3,1,0),(0.05,1,0.1,0.1,3,1,0.2),(0.05,0.3,0.1,0.1,1,0.1,0.2),(0,0,0.1,0.1,3,1,0),(0.05,1,0.1,0.1,3,0,0)]:
    vals={s:J(s,lam,Theta,V,w,R,D,kK) for s in spaces}
    best=min(vals,key=vals.get)
    print(f"   lam={lam},Theta={Theta},V={V},w={w},R={R},D={D},kK={kK}: "+", ".join(f"{s.split()[0]}={v:.3f}" for s,v in vals.items())+f"  -> cheapest: {best}")
print("   note: at Theta=0 and D=0 (no drift) the classical bit ties at zero with every space under N-pricing; with kK>0 it wins.")
print("   the classical bit 'has records' only because its dynamics is discrete; following continuous drift costs it irreversibility.")
