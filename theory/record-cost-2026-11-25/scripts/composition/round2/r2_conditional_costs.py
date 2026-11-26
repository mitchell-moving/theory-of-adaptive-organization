"""Round 2, script 1: conditional record cost at zero drift (Short & Wehner 2010 entropies, 10.1088/1367-2630/12/3/033023).
Measurement entropy  Hhat(S) = min over fine-grained measurements of the Shannon entropy of the outcomes.
  Box world: fine-grained joint measurements = sequences of fiducial measurements, later inputs may depend on
  earlier outputs (SW sec. V). Quantum: Hhat = von Neumann (SW property 1; we compute vN directly).
Standard conditional:  Hhat(A|B) = Hhat(AB) - Hhat(B).
Alternative:           Hplus(A|B) = min over measurements f on B of sum_j f_j(B) Hhat(A|j).
GTAO reading: kappa * H(A|B) = cost of holding record A when its partner B is kept alongside;
              kappa * I(A;B) = memory term kappa*I_mem (CORE's price per nat of memory).
Pairs: (1) Bell pair (qubits), (2) PR box (gbits), (3) classical perfectly correlated bits, (4) classical independent bits.
Then the record that must persist alongside a partner with TWO answers: SW's state (37), X0 X1 (classical) + Z (gbit),
obtained from a PR box by Alice's local wiring (SW eq. 37-42); compared with the best quantum encoding (qubit RAC)
and the best classical one-bit encoding.
"""
import itertools, json, numpy as np
def H(p):
    p = np.asarray(p, float).ravel(); p = p[p > 1e-15]; return float(-(p*np.log2(p)).sum())
out = {}
# ---------- box-world helpers: a state = dict mapping (inputs tuple) -> prob over outputs tuple, systems binary in/out
def box_entropy(P, nsys):
    """P(outs|ins) as a function; min Shannon entropy over adaptive sequences of fiducial measurements (any order)."""
    best = 9e9
    for order in itertools.permutations(range(nsys)):
        # adaptive strategy: input of k-th measured system is a function of previous outputs
        def rec(k, prefix_outs, ins):
            # returns list of (prob, outcome tuple) leaves
            if k == nsys:
                return [(ins, prefix_outs)]
            leaves = []
            for i in range(2):
                pass
            return None
        # enumerate deterministic adaptive strategies explicitly
        strategies = [[]]
        def strategies_for(k):
            # a strategy at depth k is a map from previous outputs (2^k) to input bit
            return list(itertools.product(range(2), repeat=2**k))
        all_strats = list(itertools.product(*[strategies_for(k) for k in range(nsys)]))
        for strat in all_strats:
            probs = {}
            for outs in itertools.product(range(2), repeat=nsys):
                ins = [0]*nsys; prev = []
                for k, s in enumerate(order):
                    key = int("".join(map(str, prev)), 2) if prev else 0
                    ins[s] = strat[k][key]; prev.append(outs[s])
                probs[outs] = P(tuple(outs), tuple(ins))
            best = min(best, H(list(probs.values())))
    return best
# PR box: P(a,b|x,y) = 1/2 [a xor b = x y]
PR = lambda o, i: 0.5*float((o[0] ^ o[1]) == (i[0]*i[1]))
PR_A = lambda o, i: 0.5
H_PR_AB = box_entropy(PR, 2); H_PR_B = box_entropy(lambda o, i: 0.5, 1)
# Hplus(A|B) for PR: measure B with y, outcome b; A's conditional state: a = b xor x*y deterministic for each x -> a gbit vertex
def hplus_PR():
    best = 9e9
    for y in range(2):
        tot = 0
        for b in range(2):
            pb = sum(PR((a, b), (0, y)) for a in range(2))
            condA = lambda o, i, b=b, y=y, pb=pb: PR((o[0], b), (i[0], y))/pb
            tot += pb*box_entropy(condA, 1)
        best = min(best, tot)
    return best
out["PR_box"] = dict(H_AB=H_PR_AB, H_B=H_PR_B, H_A_given_B=H_PR_AB - H_PR_B, Hplus_A_given_B=hplus_PR(),
                     I_AB=1 + H_PR_B - H_PR_AB)
# Bell pair (qubits)
psi = np.array([1, 0, 0, 1])/np.sqrt(2); rho = np.outer(psi, psi)
vn = lambda r: H(np.clip(np.linalg.eigvalsh(r), 0, 1))
rB = np.trace(rho.reshape(2, 2, 2, 2), axis1=0, axis2=2)
# Hplus: any projective measurement on B leaves A pure -> 0 (checked on random bases)
rng = np.random.default_rng(1); hp = 9
for _ in range(200):
    v = rng.normal(size=2) + 1j*rng.normal(size=2); v /= np.linalg.norm(v)
    tot = 0
    for P in (np.outer(v, v.conj()), np.eye(2) - np.outer(v, v.conj())):
        M = np.kron(np.eye(2), P) @ rho @ np.kron(np.eye(2), P); pb = np.trace(M).real
        rA = np.trace((M/pb).reshape(2, 2, 2, 2), axis1=1, axis2=3); tot += pb*vn(rA)
    hp = min(hp, tot)
out["Bell_pair"] = dict(H_AB=vn(rho), H_B=vn(rB), H_A_given_B=vn(rho) - vn(rB), Hplus_A_given_B=round(hp, 9), I_AB=2*vn(rB) - vn(rho))
out["classical_correlated_bits"] = dict(H_AB=1.0, H_B=1.0, H_A_given_B=0.0, Hplus_A_given_B=0.0, I_AB=1.0)
out["classical_independent_bits"] = dict(H_AB=2.0, H_B=1.0, H_A_given_B=1.0, Hplus_A_given_B=1.0, I_AB=0.0)
# ---------- record with two answers held alongside a partner: X0 X1 classical uniform, partner Z
# box world: Z = gbit vertex D(x0,x1): z_out = x_{z_in}  (SW eq. 37)
def SW(o, i, keep):   # systems: X0, X1 (classical: single input, ignore it), Z ; keep = which of (X0,X1,Z) are present
    pass
def sw_state(o, i, present):
    # o, i over present systems in order (X0, X1, Z)
    tot = 0
    for x0, x1 in itertools.product(range(2), repeat=2):
        vals = {"X0": x0, "X1": x1}; ok = 1.0; k = 0
        for s in present:
            if s in ("X0", "X1"): ok *= float(o[k] == vals[s])
            else: ok *= float(o[k] == (x0 if i[k] == 0 else x1))
            k += 1
        tot += 0.25*ok
    return tot
def Hsw(present): return box_entropy(lambda o, i: sw_state(o, i, present), len(present))
sw = {k: Hsw(v) for k, v in {"X0X1Z": ("X0", "X1", "Z"), "Z": ("Z",), "X0Z": ("X0", "Z"), "X1Z": ("X1", "Z"), "X0": ("X0",), "X0X1": ("X0", "X1")}.items()}
box = dict(H_X0_given_Z=sw["X0Z"] - sw["Z"], H_X1_given_Z=sw["X1Z"] - sw["Z"], H_X0X1_given_Z=sw["X0X1Z"] - sw["Z"],
           I_X0_Z=sw["X0"] + sw["Z"] - sw["X0Z"], I_X1_Z=sw["X0"] + sw["Z"] - sw["X1Z"], I_X0X1_Z=sw["X0X1"] + sw["Z"] - sw["X0X1Z"])
box["subadditivity_gap_H(X0X1|Z)-H(X0|Z)-H(X1|Z)"] = box["H_X0X1_given_Z"] - box["H_X0_given_Z"] - box["H_X1_given_Z"]
box["per_record_info_sum_minus_joint_info"] = box["I_X0_Z"] + box["I_X1_Z"] - box["I_X0X1_Z"]
out["two_answer_record_boxworld_SW37"] = {k: round(v, 9) for k, v in box.items()}
# quantum: best 2->1 qubit RAC, Z in state with Bloch vector ((-1)^x0, 0, (-1)^x1)/sqrt2 ; cq state, vN entropies
X = np.array([[0, 1], [1, 0]]); Zp = np.diag([1, -1])
def rz(x0, x1): return 0.5*(np.eye(2) + ((-1)**x0*X + (-1)**x1*Zp)/np.sqrt(2))
def cq(keep):  # returns entropy of joint (classical part keep subset of {0,1}) with Z
    blocks = {}
    for x0, x1 in itertools.product(range(2), repeat=2):
        key = tuple([x0, x1][j] for j in keep)
        blocks[key] = blocks.get(key, 0) + 0.25*rz(x0, x1)
    return sum(vn(b/np.trace(b).real)*np.trace(b).real + H([np.trace(b).real]) * 0 for b in blocks.values()) + H([np.trace(b).real for b in blocks.values()])
HZ = vn(sum(0.25*rz(a, b) for a, b in itertools.product(range(2), repeat=2)))
q = dict(H_X0_given_Z=cq([0]) - HZ, H_X1_given_Z=cq([1]) - HZ, H_X0X1_given_Z=cq([0, 1]) - HZ)
q["I_X0_Z"] = 1 - q["H_X0_given_Z"]; q["I_X1_Z"] = 1 - q["H_X1_given_Z"]; q["I_X0X1_Z"] = 2 - q["H_X0X1_given_Z"]
# accessible (measured) information per answer, for the GTAO memory term read operationally
p_succ = 0.5*(1 + 1/np.sqrt(2)); q["I_acc_per_answer"] = 1 - H([p_succ, 1 - p_succ])
q["subadditivity_gap_H(X0X1|Z)-H(X0|Z)-H(X1|Z)"] = q["H_X0X1_given_Z"] - q["H_X0_given_Z"] - q["H_X1_given_Z"]
q["per_record_info_sum_minus_joint_info"] = q["I_X0_Z"] + q["I_X1_Z"] - q["I_X0X1_Z"]
out["two_answer_record_qubit_RAC"] = {k: round(float(v), 6) for k, v in q.items()}
out["two_answer_record_classical_1bit_Z=x0"] = dict(H_X0_given_Z=0, H_X1_given_Z=1, H_X0X1_given_Z=1, I_X0_Z=1, I_X1_Z=0, I_X0X1_Z=1,
    subadditivity_gap=0, per_record_info_sum_minus_joint_info=0)
json.dump(out, open("r2_conditional_costs.json", "w"), indent=1); print(json.dumps(out, indent=1))
