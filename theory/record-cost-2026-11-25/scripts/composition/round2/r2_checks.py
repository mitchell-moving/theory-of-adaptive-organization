"""Round 2, script 3: (a) stake thresholds q* above which a rival beats the ball under P_rec pricing (zero drift);
(b) cross-check of the self-reference run's C1 (two-system rows): dimension of the connected group of reversible
maps that fixes every state of a complete distinguishable record (a full orthonormal basis), for real QM and complex QM,
N = 2..6 and the 2x2, 2x3, 3x3 composites (N = 4, 6, 9). Lie algebra: real antisymmetric (resp. anti-Hermitian)
generators commuting with every basis projector, modulo the identity (global phase acts trivially on states)."""
import json, numpy as np, itertools
r = json.load(open("r2_record_pricing.json"))
P = {x["n"]: x["sum_I_acc_bits"] for x in r["P_rec_polygons"]}
ball = (1.0, 0.5 - 1/np.pi)
rivals = {"square (gbit)": (P[4], .125), "pentagon": (P[5], .176), "hexagon": (P[6], .167), "octagon": (P[8], .172),
          "classical N=4": (2.0, .125), "classical N=3": (np.log2(3), .167)}
out = {"q_threshold_single_rival_beats_ball": {k: (round((p - ball[0])/(ball[1] - e), 2) if e < ball[1] else "never")
                                                for k, (p, e) in rivals.items()}}
tsir = 1 - np.cos(np.pi/8)**2; d = 0.5 - 1/np.pi
out["q_threshold_boxworld_pair_beats_QM_pair"] = round((2*P[4] - 2)/((2*d + tsir) - 0.25), 2)
def gen_dim(N, field):
    # generators G with G^T = -G (real) or G^dag = -G (complex) commuting with all diag projectors -> G diagonal
    if field == "real": return 0              # antisymmetric diagonal must be zero
    return N - 1                               # i*diag(real), minus global phase
def gen_dim_numeric(N, field):
    basis = []
    for i, j in itertools.combinations_with_replacement(range(N), 2):
        if field == "real":
            if i != j: M = np.zeros((N, N)); M[i, j] = 1; M[j, i] = -1; basis.append(M)
        else:
            M = np.zeros((N, N), complex)
            if i == j: M[i, i] = 1j; basis.append(M)
            else:
                M[i, j] = 1; M[j, i] = -1; basis.append(M.copy())
                M = np.zeros((N, N), complex); M[i, j] = 1j; M[j, i] = 1j; basis.append(M)
    rows = []
    for k in range(N):
        Pk = np.zeros((N, N)); Pk[k, k] = 1
        rows.append(np.array([np.r_[(B@Pk - Pk@B).real.ravel(), (B@Pk - Pk@B).imag.ravel()] for B in basis]).T)
    A = np.vstack(rows)
    null = A.shape[1] - np.linalg.matrix_rank(A)
    return null - (1 if field == "complex" else 0)
out["C1_crosscheck"] = {f"N={N}": dict(real_QM=gen_dim_numeric(N, "real"), complex_QM=gen_dim_numeric(N, "complex"))
                        for N in [2, 3, 4, 6, 9]}
out["C1_note"] = "N=4,6,9 are the 2x2, 2x3, 3x3 composites. real QM: 0 for every N (fails); complex QM: N-1 (passes), matching selfref C1."
json.dump(out, open("r2_checks.json", "w"), indent=1, default=int); print(json.dumps(out, indent=1, default=int))
