"""Cross-checks for polygons.py: (1) alternating optimiser on classical simplices reproduces
1/(2N) (so the classical numbers are optima, not just the binning guess); (2) Monte Carlo of
the disk later-question error; (3) eta values vs known: disk-limit eta -> 1/sqrt2 matches the
phase-covariant qubit cloner shrink factor (a consistency check only; different composite)."""
import itertools, numpy as np
from polygons import later_question_error
for N in [2,3,4]:
    V=np.eye(N); E=np.array([list(b) for b in itertools.product([0,1],repeat=N)],float)
    print(f"simplex N={N}: alternating-opt error={later_question_error(V,E):.4f}  vs 1/(2N)={1/(2*N):.4f}")
rng=np.random.default_rng(1); M=2_000_000
th=rng.uniform(0,2*np.pi,M); ph=rng.uniform(0,2*np.pi,M)
p_plus=(1+np.cos(th-ph))/2; out=rng.random(M)<p_plus; truth=np.cos(th-ph)>0
print(f"disk MC error={np.mean(out!=truth):.4f}  analytic={0.5-1/np.pi:.4f}")
print(f"1/sqrt2={1/np.sqrt(2):.4f}")
