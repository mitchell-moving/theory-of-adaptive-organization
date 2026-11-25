import sys, math, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'composite_contest_checks'))
from common import MENU, T_MAT
I=np.eye(2); X=np.array([[0,1],[1,0.]]); Z=np.diag([1.,-1])
psi=np.array([0,1,-1,0.])/math.sqrt(2)           # real singlet, real amplitudes only
assert np.isrealobj(psi)
def obs(u, wing):
    x,y,z=u
    if abs(y)>0.5:                                  # menu direction y: trivial readout +-I (eigenvalues all +1 or all -1)
        return (1. if wing=='A' else -1.)*I
    return x*X+z*Z                                   # real symmetric, eigenvalues +-1 for unit (x,z)
C=np.array([[psi@np.kron(obs(u,'A'),obs(v,'B'))@psi for v in MENU] for u in MENU])
print(np.round(C,15)); print("target"); print(np.round(T_MAT,15))
d=C-T_MAT; print("mean loss L =", np.sum(d*d)/25, " worst-pair L_inf =", np.max(d*d))
for u in MENU:
    for w in 'AB':
        ev=np.linalg.eigvalsh(obs(u,w)); assert np.allclose(np.abs(ev),1), ev
print("all local observables have eigenvalues in {+1,-1}; state and observables are real")
lam=np.array([1e-4,1e-3,1e-2,1e-1]); print("J_R=lam ln10:",lam*math.log(10)," J_C=lam ln16:",lam*math.log(16))
