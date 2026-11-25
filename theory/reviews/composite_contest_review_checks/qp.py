import sys, math, numpy as np
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'composite_contest_checks'))
from search import vertex_correlators
from common import T_FLAT
from scipy.optimize import nnls, linprog
C = vertex_correlators()           # 1024 x 25
# min ||C^T w - T||^2 s.t. w>=0, sum w = 1 via NNLS with heavy sum row
big = 1e4
A = np.vstack([C.T, big*np.ones((1,1024))]); b = np.concatenate([T_FLAT,[big]])
w,_ = nnls(A,b, maxiter=100000)
w /= w.sum()
c = w@C; L = float(np.sum((c-T_FLAT)**2)/25)
print("QP min mean loss", L, "support", int((w>1e-10).sum()), "LemmaB floor", (3-2*math.sqrt(2))/25)
np.save('/tmp/cstar.npy', c)
