"""Toy 1 (Q2), corrected version. See t1a_polygon_pertick_FLAWED.py for the first attempt and why it was wrong
(its LP rewarded the identity map, i.e. lagging; and greedy per-tick shrinking compounds a loss that need not compound).

Task (fixed capacity = one perfectly distinguishable pair): the world presents a binary question whose
direction theta drifts continuously and without bound. The tracker must, at every theta, hold the answer as a
pair of record states pointing exactly along the current direction (no lag, readout at any time, no clock).
State spaces: regular n-gon (n even, so a vertex and its opposite are a perfectly distinguishable pair).
n=2 is the classical bit (segment); n=4 the gbit square; disk = rebit; ball = qubit.

Claim tested: the cheapest strategy shrinks the record ONCE toward the centre (maximally mixed state) to a radius r
such that the rotated record fits in P for every theta, then rotates at zero further loss. r* = inradius/circumradius = cos(pi/n).
We check this by LP over general affine maps M_theta(x) = A x + b with the exact-direction constraint
A v_k + b = lam_k R_theta v_k, on a dense theta grid, maximizing min_k lam_k.
Information measure: the drift-direction bias of the answer pair is the gauge norm of P at the record point;
worst case over theta is r (at vertex directions). Bits retained of the 1-bit distinction = 1 - h2((1+bias)/2).
"""
import numpy as np, json
from scipy.optimize import linprog

def polygon(n):
    ang = 2*np.pi*np.arange(n)/n
    V = np.c_[np.cos(ang), np.sin(ang)]
    U = np.c_[np.cos(ang+np.pi/n), np.sin(ang+np.pi/n)]
    return V, U, np.cos(np.pi/n)

def R(d): return np.array([[np.cos(d), -np.sin(d)], [np.sin(d), np.cos(d)]])
def h2(p):
    p = np.clip(p, 1e-15, 1-1e-15); return float(-(p*np.log2(p)+(1-p)*np.log2(1-p)))

def best_exact_direction(n, theta):
    V, U, h = polygon(n); Rt = R(theta); m = len(V)
    nv = 6 + m + 1   # A(4) b(2) lam_k(m) t
    c = np.zeros(nv); c[-1] = -1
    Aub, bub, Aeq, beq = [], [], [], []
    for k, v in enumerate(V):
        for u in U:   # positivity of image
            row = np.zeros(nv); row[0:2] = u[0]*v; row[2:4] = u[1]*v; row[4:6] = u
            Aub.append(row); bub.append(h)
        tv = Rt @ v
        for i in range(2):  # exact direction: (A v + b)_i - lam_k (R v)_i = 0
            row = np.zeros(nv); row[2*i:2*i+2] = v; row[4+i] = 1; row[6+k] = -tv[i]
            Aeq.append(row); beq.append(0)
        row = np.zeros(nv); row[-1] = 1; row[6+k] = -1; Aub.append(row); bub.append(0)  # t <= lam_k
    res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub), A_eq=np.array(Aeq), b_eq=np.array(beq),
                  bounds=[(None, None)]*6 + [(0, None)]*m + [(None, None)], method="highs")
    return -res.fun, res.x[4:6]

out = {"rows": []}
thetas = np.linspace(0, 2*np.pi, 49)
for n in [4, 6, 8, 12, 24]:
    vals = [best_exact_direction(n, th) for th in thetas]
    worst = min(v[0] for v in vals); argw = thetas[int(np.argmin([v[0] for v in vals]))]
    maxb = max(np.abs(v[1]).max() for v in vals)
    r = np.cos(np.pi/n)
    out["rows"].append(dict(n=n, lp_worst_case_r=round(worst, 8), closed_form_cos_pi_over_n=round(r, 8),
                            worst_theta_over_2pi_n=round(argw/(2*np.pi/n), 4), max_abs_translation_b=float(maxb),
                            bits_lost_of_1bit=round(h2((1+r)/2), 5), cost_in_kappa_ln2_units=round(h2((1+r)/2), 5)))
out["classical_bit_segment"] = dict(n=2, r_star=0.0, bits_lost_of_1bit=1.0,
    note="inradius of a segment is 0: an unboundedly drifting direction cannot be carried at all; best lagging strategy has alignment |cos(theta)|, zero at theta=pi/2")
out["disk_rebit"] = dict(r_star=1.0, bits_lost_of_1bit=0.0, note="SO(2) rotations are reversible symmetries of the disk")
out["ball_qubit"] = dict(r_star=1.0, bits_lost_of_1bit=0.0, note="SO(3) rotations (unitaries) are reversible symmetries of the Bloch ball")
# lagging alternative (no shrink, snap to nearest symmetry every 2pi/n): mean |cos| misalignment = sin(pi/n)/(pi/n)
out["lag_strategy_mean_alignment"] = {str(n): round(np.sin(np.pi/n)/(np.pi/n), 5) for n in [2, 4, 6, 8, 12, 24, 64, 256]}
# asymptotics: bits lost ~ (pi^2/(4 n^2)) log2(4 n^2 e / pi^2)
out["asymptotic_check"] = {str(n): [round(h2((1+np.cos(np.pi/n))/2), 7), round((np.pi**2/(4*n**2))*np.log2(4*n**2*np.e/np.pi**2), 7)] for n in [64, 256, 1024]}
json.dump(out, open("outputs/t1_polygon_drift.json", "w"), indent=1)
for k, v in out.items(): print(k, json.dumps(v, indent=1) if not isinstance(v, list) else "\n".join(map(str, v)))
# --- self-check added after the first run: can the one-time shrink be COMPOSED tick by tick?
# A tick map T must send the shrunk record r*R_theta(P) to r*R_(theta+d)(P). That set spans the plane (and the centre),
# so linearity forces T = R_d on the whole state space, which is a valid (positive) map only if R_d P = P.
comp = []
for n in [4, 6, 8, 12, 24]:
    V, U, h = polygon(n)
    for d in [0.01, 0.1, 2*np.pi/n]:
        img = (R(d) @ V.T).T
        comp.append(dict(n=n, d=round(d, 4), R_d_is_positive=bool((img @ U.T <= h + 1e-9).all())))
out["tick_composition_check"] = comp
json.dump(out, open("outputs/t1_polygon_drift.json", "w"), indent=1)
print("tick_composition_check"); [print(c) for c in comp]
