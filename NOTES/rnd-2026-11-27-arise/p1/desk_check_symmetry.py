"""P1 desk check (not a preregistered test). Elementary, known in kind (ZHP 1993; DDZ 2005).
Claim checked: for a harmonic oscillator (hbar=m=omega=1) with position dephasing D,
any loss a*Var x + b*Var p averaged over whole periods is minimized over pure Gaussian
initial states by the coherent state, because the Hamiltonian rotates phase space.
The diffusion part of the covariance does not depend on the initial state (linear Gaussian),
so only the rotated initial covariance matters. ZHP's purity-loss rate for a pure state,
4D Var x(t), has the same period average. Short horizons break the tie (x-squeezing)."""
import numpy as np, sympy as sp
from scipy.optimize import minimize
t, Vx, Vp, C, a, b = sp.symbols('t V_x V_p C a b', real=True)
varx = Vx*sp.cos(t)**2 + Vp*sp.sin(t)**2 + 2*C*sp.sin(t)*sp.cos(t)
varp = Vx*sp.sin(t)**2 + Vp*sp.cos(t)**2 - 2*C*sp.sin(t)*sp.cos(t)
avg = sp.simplify(sp.integrate(a*varx + b*varp, (t, 0, 2*sp.pi))/(2*sp.pi))
print("period average of a*Varx+b*Varp:", avg)
zhp = sp.simplify(sp.integrate(4*varx, (t, 0, 2*sp.pi))/(2*sp.pi))
print("period average of ZHP purity-loss rate / D:", zhp)
# minimize (Vx+Vp) s.t. Vx*Vp - C^2 = 1/4 -> Vx=Vp=1/2, C=0
def best(T, a_, b_):
    ts = np.linspace(0, T, 2001)
    def f(z):
        r, th = z  # squeeze r, angle th: Vx = (cosh2r - sinh2r cos2th)/2 etc.
        vx = (np.cosh(2*r) - np.sinh(2*r)*np.cos(2*th))/2
        vp = (np.cosh(2*r) + np.sinh(2*r)*np.cos(2*th))/2
        c = -np.sinh(2*r)*np.sin(2*th)/2
        vxt = vx*np.cos(ts)**2 + vp*np.sin(ts)**2 + 2*c*np.sin(ts)*np.cos(ts)
        vpt = vx*np.sin(ts)**2 + vp*np.cos(ts)**2 - 2*c*np.sin(ts)*np.cos(ts)
        return np.trapezoid(a_*vxt + b_*vpt, ts)/T
    res = min((minimize(f, [r0, th0], method='Nelder-Mead', options={'xatol':1e-9,'fatol':1e-12}) for r0 in (0.05, 0.5, 1.0) for th0 in (0.1, 1.0, 2.0)), key=lambda r: r.fun)
    return abs(res.x[0]), res.fun
for (a_, b_) in [(1,0),(0,1),(1,1),(3,1)]:
    for T in [0.25, 1.0, 2*np.pi, 20*np.pi]:
        r, J = best(T, a_, b_)
        print(f"loss a={a_} b={b_}  horizon T={T:7.3f}  optimal |squeeze r|={r:.4f}  J={J:.5f}")
