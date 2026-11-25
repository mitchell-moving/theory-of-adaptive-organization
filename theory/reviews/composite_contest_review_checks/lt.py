import sys, math, itertools, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'composite_contest_checks'))
from search import vertex_correlators
from common import T_FLAT
from scipy.optimize import milp, LinearConstraint, Bounds
C = vertex_correlators(); n=1024
# variables: p (1024), zA (32), zB (32)
def feas(s, mA, mB):
    nv = n+64
    rows=[]; lo=[]; hi=[]
    A = np.zeros((25,nv)); A[:,:n]=C.T; rows.append(A); lo+=list(T_FLAT-s); hi+=list(T_FLAT+s)
    S=np.zeros((1,nv)); S[0,:n]=1; rows.append(S); lo+=[1]; hi+=[1]
    LA=np.zeros((n,nv)); LB=np.zeros((n,nv))
    for k in range(n):
        a,b=divmod(k,32); LA[k,k]=1; LA[k,n+a]=-1; LB[k,k]=1; LB[k,n+32+b]=-1
    rows+= [LA,LB]; lo+=[-np.inf]*(2*n); hi+=[0]*(2*n)
    CA=np.zeros((2,nv)); CA[0,n:n+32]=1; CA[1,n+32:]=1; rows.append(CA); lo+=[0,0]; hi+=[mA,mB]
    obj=np.zeros(nv); obj[:n] = 0
    r=milp(obj,integrality=np.concatenate([np.zeros(n),np.ones(64)]),bounds=Bounds(0,1),
       constraints=[LinearConstraint(np.vstack(rows),lo,hi)],options={"time_limit":120})
    return r.status
lam=0.1; Jc=lam*math.log(16)
for eps in (0.05,0.1):
    for mA,mB in [(1,10),(2,5),(3,3),(2,4),(3,4),(4,4)]:
        st=feas(math.sqrt(eps),mA,mB)
        print(f"eps {eps} mA {mA} mB {mB} K {mA*mB} status {st} ({'feasible' if st==0 else 'infeasible' if st==2 else st})  J_H_lowerbound {lam*math.log(mA*mB)+0.042893:.4f} vs J_C {Jc:.4f}")
