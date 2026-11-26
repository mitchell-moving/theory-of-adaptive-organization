"""Route (d): is a copy restriction a precondition for J>0 and non-trivial selection?
Toy population (Grossman-Stiglitz-like). World bit flips each period w.p. p (drift).
'Acquirers' pay a per period to read the current bit (a read = copying the world's
distinction onto a record). 'Copiers' pay c to copy last period's record of a random member,
with copy flip-noise eps. Stake q on error. Copier error e_C solves
  e_C = lam*g(0) + (1-lam)*g(e_C),  g(e) = flip(flip(e,p),eps), flip(x,r)=x(1-r)+(1-x)r.
Equilibrium: acquirer fraction lam* where costs equalise (a = c + q e_C), or a corner."""
import numpy as np
from scipy.optimize import brentq
def flip(x,r): return x*(1-r)+(1-x)*r
def eC(lam,p,eps):
    g0=flip(flip(0,p),eps)
    # e = lam*g0 + (1-lam)*flip(flip(e,p),eps): linear in e -> solve
    r=flip(p,eps)  # combined flip prob of drift then copy noise: p(1-eps)+eps(1-p)
    # flip(e,r)=e(1-2r)+r
    return (lam*g0+(1-lam)*r)/(1-(1-lam)*(1-2*r))
def equilibrium(a,c,q,p,eps):
    f=lambda lam: (c+q*eC(lam,p,eps))-a   # copier cost minus acquirer cost
    if f(1.0)>=0 and f(1e-9)>=0: return 1.0   # copying never pays -> all acquire
    if f(1e-9)<0 and f(1.0)<0: return 0.0     # copying always pays
    return brentq(f,1e-9,1.0)
print("a=1, q=10 throughout. Columns: drift p, copy cost c, copy noise eps -> lam*, mean cost per member, cost spread acquirer-vs-copier")
for p,c,eps in [(0.0,0,0),(0.0,0.5,0),(0.05,0,0),(0.05,0,0.05),(0.05,0.5,0),(0.2,0,0),(0.0,0,0.05)]:
    a,q=1.0,10.0
    lam=equilibrium(a,c,q,p,eps)
    e=eC(max(lam,1e-12),p,eps)
    Jmean=lam*a+(1-lam)*(c+q*e)
    print(f"  p={p:.2f} c={c:.1f} eps={eps:.2f} -> lam*={lam:.4f}, copier err={e:.4f}, mean J={Jmean:.4f}")
print("Reading: with no drift and perfect free copying (row 1) lam*->0 and mean J->0: one early read")
print("serves everyone forever (CORE line 78: frozen worlds allow zero ongoing cost). With drift, lam*>0")
print("and J>0 even when copying is perfect and free: the cost comes from acquiring NEW distinctions.")
