"""Toy 5 (steering task 1): bipartite classical / real-QM / QM / boxworld under ONE cost with drift.
Cost (same as sibling nocloning/scripts/tracking.py, extended to a pair; no heat):
  J = kappa*log2(N_AB) + q*(e_A + e_B + e_joint) + lam*(Sigma_A + Sigma_B + Sigma_joint) [+ L for joint-only reads]
  kappa = 1 per bit, q = 4, lam in {0.05, 0.005} per nat of path-KL irreversibility.
  N_AB = 4 for all four pairs (t6 computes the gbit pair; the others are standard).
Coordinates (each drifts by total angle Theta):
  A, B local later-questions (sibling's task): disk/ball error 1/2-1/pi at zero Sigma (continuous reversible group);
  square and classical bit follow drift only by Markov jumps: Sigma >= 2 Theta^2 / V (TUR; sibling C3 shows it is
  n-independent for rings), error from sibling's ring model err_ring(N, V).
  joint coordinate: a CHSH-type correlation question whose frame drifts. Zero-drift success: classical 0.75,
  QM and real QM cos^2(pi/8) (real states and real measurements reach Tsirelson), boxworld 1.0.
  QM/real QM rotate the frame with a continuous local rotation (zero Sigma). Boxworld/classical have finite reversible
  groups (t3: boxworld pair has exactly 128 symmetries), so they follow by Markov jumps; stylised blur model:
  correlation bias multiplied by exp(-V/2) for a Gaussian phase slip of variance V, with Sigma = 2 Theta^2 / V.
The joint-coordinate blur model is a modelling choice [NUM within stated model], not derived.
"""
import numpy as np, json
rng = np.random.default_rng(2)
def err_ring(N, V, M=400):   # copied from sibling tracking.py (same model, same seed policy)
    th = np.linspace(0, 2*np.pi, M, endpoint=False); ph = th
    slip = rng.normal(0, np.sqrt(V), M) if V > 0 else np.zeros(M)
    est = ((np.floor(th/(2*np.pi/N))+0.5)*2*np.pi/N)[:, None]+slip[None, :]
    tot = 0
    for p in ph[::8]:
        truth = np.cos(th-p) > 0; ans = np.cos(est-p) > 0
        tot += np.mean(ans != truth[:, None])
    return tot/len(ph[::8])
disk_err = 0.5 - 1/np.pi
Vs = [1e-3, 1e-2, 0.03, 0.1, 0.3, 1, 3, np.inf]
def local_best(N, Theta, q, lam):
    best = 9e9
    for V in Vs:
        Sig = 0 if (Theta == 0 or V == np.inf) else 2*Theta**2/V
        e = 0.5 if (V == np.inf and Theta > 0) else err_ring(N, 0 if Theta == 0 else V)
        best = min(best, q*e + lam*Sig)
    return best
def joint_best(win0, Theta, q, lam, continuous):
    if continuous: return q*(1-win0)
    best = 9e9
    for V in Vs:
        if Theta == 0: e = 1-win0; Sig = 0
        elif V == np.inf: e = 0.5; Sig = 0
        else: e = 0.5 - (win0-0.5)*np.exp(-V/2); Sig = 2*Theta**2/V
        best = min(best, q*e + lam*Sig)
    return best
tsirelson = np.cos(np.pi/8)**2
out = {}
for q, lam in [(4.0, 0.05), (4.0, 0.005)]:
    rows = []
    for Theta in [0, 0.3, 1, 2, 3, 10, 30]:
        J = {
         "classical pair": 2 + 2*local_best(2, Theta, q, lam) + joint_best(0.75, Theta, q, lam, False),
         "boxworld pair": 2 + 2*local_best(4, Theta, q, lam) + joint_best(1.0, Theta, q, lam, False),
         "real-QM pair": 2 + 2*q*disk_err + joint_best(tsirelson, Theta, q, lam, True),
         "QM pair": 2 + 2*q*disk_err + joint_best(tsirelson, Theta, q, lam, True)}
        rows.append(dict(Theta=Theta, **{k: round(v, 3) for k, v in J.items()}, cheapest=min(J, key=J.get)))
    out[f"q={q},lam={lam}"] = rows
# local-only variant (no joint question): pure additivity check, pair = 2 x single
out["local_only_pair_equals_2x_single (lam=0.05, Theta=1)"] = dict(
    boxworld=round(2 + 2*local_best(4, 1, 4.0, 0.05), 3), QM=round(2 + 2*4.0*disk_err, 3))
json.dump(out, open("outputs/t5_bipartite_drift.json", "w"), indent=1)
for k, v in out.items():
    print(k)
    if isinstance(v, list):
        for r in v: print("  ", r)
    else: print("  ", v)
