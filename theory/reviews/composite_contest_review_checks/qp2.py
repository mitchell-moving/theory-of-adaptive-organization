import sys, math, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'composite_contest_checks'))
from search import vertex_correlators
from common import T_FLAT
from scipy.optimize import milp, LinearConstraint, Bounds
C = vertex_correlators(); c = np.load('/tmp/cstar.npy')
g = c - T_FLAT
gap = float(np.min((C - c) @ g))   # FW optimality: >= 0 means global min
print("FW dual gap min_i (C_i-c)·(c-T) =", gap, " => lower bound on L:", float(np.sum(g**2)/25 + 2*min(gap,0)/25))
print("2*(3-2sqrt2)/25 =", 2*(3-2*math.sqrt(2))/25)
n=1024
A_eq = np.hstack([C.T, np.zeros((25,n))]); A_s = np.concatenate([np.ones(n),np.zeros(n)])[None]
Ap = np.hstack([np.eye(n), -np.eye(n)])
tol=1e-7
r = milp(np.concatenate([np.zeros(n),np.ones(n)]), integrality=np.concatenate([np.zeros(n),np.ones(n)]),
  bounds=Bounds(0,1), constraints=[LinearConstraint(A_eq,c-tol,c+tol),LinearConstraint(A_s,1,1),LinearConstraint(Ap,-np.inf,0)],
  options={"time_limit":120})
print("min support of exact optimum:", r.status, r.fun)
