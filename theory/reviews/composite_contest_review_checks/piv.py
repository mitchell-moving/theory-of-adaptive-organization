import sys, math, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'composite_contest_checks'))
from search import vertex_correlators
from common import T_FLAT
from scipy.optimize import milp, LinearConstraint, Bounds
C = vertex_correlators(); n=1024
def minsupp(s):
    A = np.hstack([C.T, np.zeros((25,n))]); As=np.concatenate([np.ones(n),np.zeros(n)])[None]
    Ap=np.hstack([np.eye(n),-np.eye(n)])
    r=milp(np.concatenate([np.zeros(n),np.ones(n)]),integrality=np.concatenate([np.zeros(n),np.ones(n)]),bounds=Bounds(0,1),
      constraints=[LinearConstraint(A,T_FLAT-s,T_FLAT+s),LinearConstraint(As,1,1),LinearConstraint(Ap,-np.inf,0)],options={"time_limit":300})
    p=np.clip(r.x[:n],0,None); return r.status, round(r.fun), float(np.max(np.abs(p@C-T_FLAT))**2)
sstar=(math.sqrt(2)-1)/2
for eps in [sstar**2*(1+1e-9), 0.05, 0.1, 0.12, 0.25, 1.0]:
    print("eps",eps, minsupp(math.sqrt(eps)))
print("floor (3-2sqrt2)/4 =", repr((3-2*math.sqrt(2))/4), " ((sqrt2-1)/2)^2 =", repr(sstar**2), " (1/2-1/(2sqrt2))^2=",(0.5-1/(2*math.sqrt(2)))**2)
