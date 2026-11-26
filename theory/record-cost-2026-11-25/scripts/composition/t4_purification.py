"""Toy 4 (Q3): is 'every mixed record is part of a pure record of a larger whole' (purification) the same
as 'no information is lost for free' (every process has a lossless, reversible dilation)?
(a) Classical: a noisy update (bit flip with prob p) has a reversible dilation: a permutation (CNOT) of system+ancilla,
    with the ancilla MIXED (a coin with bias p). Global Shannon entropy is conserved: no information destroyed.
(b) Classical: any joint distribution whose marginal is mixed is itself mixed: H(SE) >= H(S). So 'whole pure, part mixed' is impossible.
(c) Quantum: the Bell state has H(SE)=0 < H(S)=1; conditional entropy H(S|E) = -1 (erasure of S given E as memory
    has negative cost in the del Rio et al. 2011 accounting, 10.1038/nature10123).
"""
import numpy as np, json, itertools
def H(p):
    p = np.asarray(p, float).ravel(); p = p[p > 1e-15]; return float(-(p*np.log2(p)).sum())
out = {}
p = 0.2
# (a) system bit S uniform, ancilla coin E~Bern(p); reversible map (s,e)->(s xor e, e)
joint_in = {(s, e): 0.5*(p if e else 1-p) for s, e in itertools.product(range(2), repeat=2)}
joint_out = {}
for (s, e), w in joint_in.items(): joint_out[(s ^ e, e)] = joint_out.get((s ^ e, e), 0) + w
# information the system keeps about its input (reference R = copy of input s)
RS_out = {}
for (s, e), w in joint_in.items(): RS_out[(s, s ^ e)] = RS_out.get((s, s ^ e), 0) + w
I_RS = 1 + H([sum(w for (r, x), w in RS_out.items() if x == k) for k in range(2)]) - H(list(RS_out.values()))
out["classical_dilation"] = dict(p=p, H_global_in=H(list(joint_in.values())), H_global_out=H(list(joint_out.values())),
    info_system_keeps_about_input_bits=round(I_RS, 6), info_moved_into_SE_correlation_bits=round(1 - I_RS, 6),
    reading="the system keeps 1-h(p) bits and loses h(p) bits of its own record, but nothing is destroyed globally; the ancilla must be a mixed coin, i.e. randomness is supplied, not derived")
# (b) classical: exhaustive check on a grid that H(SE) >= H(S)
worst = 9
for a in np.linspace(0, 1, 11):
    for b in np.linspace(0, 1-a, 11):
        for c in np.linspace(0, 1-a-b, 11):
            d = 1-a-b-c; P = np.array([[a, b], [c, d]])
            worst = min(worst, H(P) - H(P.sum(1)))
out["classical_min_H(SE)-H(S)_over_grid"] = round(worst, 12)
# (c) quantum Bell state
psi = np.array([1, 0, 0, 1])/np.sqrt(2); rho = np.outer(psi, psi)
rS = np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)
vn = lambda r: H(np.clip(np.linalg.eigvalsh(r), 0, 1))
out["quantum_bell"] = dict(H_SE=round(vn(rho), 9), H_S=round(vn(rS), 9), H_S_given_E=round(vn(rho)-vn(rS), 9))
json.dump(out, open("outputs/t4_purification.json", "w"), indent=1); print(json.dumps(out, indent=1))
