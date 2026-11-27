"""M4 desk check: is locality CREATED by selecting interaction links under a GTAO-type cost, or INHERITED from the world's need structure?
Cost J = L*(#links) + w * sum_ij need_ij * hops_ij (link upkeep + lateness), greedy edge toggles (selection by cost), N=144.
Spectral dimension d_s from the random-walk return probability of the lazy walk, fit over t in [4, 40], minus 1/N."""
import numpy as np, sys
from scipy.sparse.csgraph import shortest_path
def ds_est(A):
    N = len(A); d = A.sum(1); d[d == 0] = 1; Dm = np.diag(1/np.sqrt(d)); S = Dm @ A @ Dm
    lam = np.linalg.eigvalsh(S); t = np.arange(4, 41); P = np.array([np.mean(((1 + lam)/2)**k) for k in t]) - 1.0/N
    P = np.maximum(P, 1e-12); return float(-2*np.polyfit(np.log(t), np.log(P), 1)[0])
def J(A, need, L, w):
    H = shortest_path(A, unweighted=True, directed=False); H[np.isinf(H)] = 50.0
    return L*A.sum()/2 + w*(need*H).sum()/2, H
def evolve(need, L, w, seed, iters):
    rng = np.random.default_rng(seed); N = len(need); A = np.zeros((N, N))
    for i in range(N): A[i, (i + 1) % N] = A[(i + 1) % N, i] = 1          # start: a ring (connected, 1D, no positions used)
    for _ in range(int(N*0.5)):
        i, j = rng.integers(0, N, 2)
        if i != j: A[i, j] = A[j, i] = 1                                    # plus random chords
    cur, _ = J(A, need, L, w)
    for _ in range(iters):
        i, j = rng.integers(0, N, 2)
        if i == j: continue
        A[i, j] = A[j, i] = 1 - A[i, j]; new, _ = J(A, need, L, w)
        if new <= cur: cur = new
        else: A[i, j] = A[j, i] = 1 - A[i, j]
    H = shortest_path(A, unweighted=True, directed=False); return A, float(H[np.isfinite(H)].max())
if __name__ == "__main__":
    N = 144; side = 12
    G = np.zeros((N, N))
    for x in range(side):
        for y in range(side):
            i = x*side + y
            if x + 1 < side: G[i, i + side] = G[i + side, i] = 1
            if y + 1 < side: G[i, i + 1] = G[i + 1, i] = 1
    rr = np.random.default_rng(1); R = np.zeros((N, N))
    for _ in range(4*N//2):
        i, j = rr.integers(0, N, 2)
        if i != j: R[i, j] = R[j, i] = 1
    print(f"calibration: 12x12 grid d_s = {ds_est(G):.2f} (valid iff in [1.5, 2.5]); random graph d_s = {ds_est(R):.2f}")
    for seed in (1, 2, 3):
        rng = np.random.default_rng(100 + seed)
        U = np.ones((N, N)) - np.eye(N)                                      # uniform need: no hidden geometry
        pos = rng.random((N, 2)); Dd = np.linalg.norm(pos[:, None] - pos[None], axis=2)
        Q = np.exp(-Dd/0.08); np.fill_diagonal(Q, 0); Q *= U.sum()/Q.sum()  # need from hidden 2D positions, same total need
        for name, need in (("uniform", U), ("hidden2D", Q)):
            A, diam = evolve(need, L=40.0, w=1.0, seed=seed, iters=6000)
            print(f"seed {seed} {name}: links {int(A.sum()/2)} diameter {diam:.0f} d_s {ds_est(A):.2f}")
