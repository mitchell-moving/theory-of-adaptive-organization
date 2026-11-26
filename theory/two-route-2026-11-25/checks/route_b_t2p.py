#!/usr/bin/env python3
"""B-T2' (PREREG_2.md section 1.6 and 4, procedure of PREREG.md section 3.5) and the B-C3 code gate.

3x3 common team cost J, party 1 picks the row and party 2 the column, entries i.i.d.
Uniform(0,1), 20,000 draws from numpy.random.default_rng(20261125), filled row-major.
A move by party i changes only its own coordinate, to either other value. Resistance
r(x->y) = c_i (J(y)-J(x))_+. Stochastic potential SP(x) = minimum total resistance of a
spanning in-tree rooted at x (Chu-Liu/Edmonds, own implementation, cross-checked by brute
force on the first 200 qualifying draws). A draw qualifies if it has exactly two
unilateral (strict) local minima and a unique SP minimizer; ties are counted and reported.
f = fraction of qualifying draws whose selected state is not the global minimum of J.
Code gate (B-C3): at c=(1,1) f must be 0 on the same draws.
Usage: route_b_t2p.py [N_DRAWS]   (default 20000; JSON to stdout)
"""
import itertools
import json
import sys
import time

import numpy as np

SEED, N_DRAWS, N_BRUTE = 20261125, 20000, 200
TIE = 1e-12
NODES = [(r, s) for r in range(3) for s in range(3)]


def moves(c):
    """Directed edges (u, v, party weight) on the 3x3 product grid."""
    out = []
    for u, (r, s) in enumerate(NODES):
        for r2 in range(3):
            if r2 != r:
                out.append((u, r2 * 3 + s, c[0]))
        for s2 in range(3):
            if s2 != s:
                out.append((u, r * 3 + s2, c[1]))
    return out


def edmonds(n, root, edges):
    """Minimum-weight spanning arborescence directed away from root (Chu-Liu/Edmonds).
    edges: list of (u, v, w) meaning u -> v. Returns total weight."""
    total = 0.0
    while True:
        inw = [np.inf] * n
        pre = [-1] * n
        for u, v, w in edges:
            if u != v and w < inw[v]:
                inw[v], pre[v] = w, u
        inw[root] = 0.0
        if any(np.isinf(inw[v]) for v in range(n) if v != root):
            raise ValueError("no arborescence")
        cid = [-1] * n
        mark = [-1] * n
        k = 0
        for v in range(n):
            total += inw[v]
            x = v
            while mark[x] != v and cid[x] == -1 and x != root:
                mark[x] = v
                x = pre[x]
            if x != root and cid[x] == -1:
                y = pre[x]
                while y != x:
                    cid[y] = k
                    y = pre[y]
                cid[x] = k
                k += 1
        if k == 0:
            return total
        for v in range(n):
            if cid[v] == -1:
                cid[v] = k
                k += 1
        edges = [(cid[u], cid[v], w - inw[v]) for u, v, w in edges if cid[u] != cid[v]]
        n, root = k, cid[root]


def stochastic_potential(J, c):
    """SP(x) for every state x: min in-tree rooted at x = min out-arborescence on reversed edges."""
    rev = [(v, u, wt * max(J[v] - J[u], 0.0)) for u, v, wt in moves(c)]
    return np.array([edmonds(9, x, rev) for x in range(9)])


def brute_sp(J, c):
    """Brute force: each non-root state picks one of its 4 outgoing moves; keep the choices
    in which every state reaches the root."""
    out = {u: [] for u in range(9)}
    for u, v, wt in moves(c):
        out[u].append((v, wt * max(J[v] - J[u], 0.0)))
    sp = np.empty(9)
    for root in range(9):
        others = [u for u in range(9) if u != root]
        choices = np.array(list(itertools.product(range(4), repeat=8)))
        nxt = np.empty((len(choices), 9), dtype=int)
        cost = np.zeros(len(choices))
        nxt[:, root] = root
        for j, u in enumerate(others):
            tgt = np.array([out[u][k][0] for k in range(4)])
            wts = np.array([out[u][k][1] for k in range(4)])
            nxt[:, u] = tgt[choices[:, j]]
            cost += wts[choices[:, j]]
        pos = np.tile(np.arange(9), (len(choices), 1))
        for _ in range(9):
            pos = np.take_along_axis(nxt, pos, axis=1)
        ok = np.all(pos == root, axis=1)
        sp[root] = cost[ok].min()
    return sp


def local_minima(J):
    mins = []
    for u, (r, s) in enumerate(NODES):
        nb = [r2 * 3 + s for r2 in range(3) if r2 != r] + [r * 3 + s2 for s2 in range(3) if s2 != s]
        if all(J[u] < J[v] for v in nb):
            mins.append(u)
    return mins


def main(n_draws):
    t0 = time.process_time()
    rng = np.random.default_rng(SEED)
    draws = rng.uniform(0.0, 1.0, size=(n_draws, 9))  # row-major: entry (r, s) is column 3r+s
    counts = dict(draws=n_draws, two_minima=0, sp_ties=0, qualifying=0, worse_selected=0,
                  not_two_minima=0)
    gate = dict(qualifying_draws_checked=0, sp_ties=0, worse_selected=0)
    brute = dict(checked=0, max_abs_diff=0.0)
    sp_not_at_local_min = 0
    for J in draws:
        mins = local_minima(J)
        if len(mins) != 2:
            counts["not_two_minima"] += 1
            continue
        counts["two_minima"] += 1
        sp = stochastic_potential(J, (1.0, 3.0))
        order = np.sort(sp)
        if order[1] - order[0] <= TIE:
            counts["sp_ties"] += 1
            continue
        counts["qualifying"] += 1
        sel = int(np.argmin(sp))
        if sel not in mins:
            sp_not_at_local_min += 1
        if sel != int(np.argmin(J)):
            counts["worse_selected"] += 1
        if brute["checked"] < N_BRUTE:
            b = brute_sp(J, (1.0, 3.0))
            brute["max_abs_diff"] = max(brute["max_abs_diff"], float(np.max(np.abs(b - sp))))
            brute["checked"] += 1
        # B-C3 code gate on the same draw
        sp1 = stochastic_potential(J, (1.0, 1.0))
        o1 = np.sort(sp1)
        gate["qualifying_draws_checked"] += 1
        if o1[1] - o1[0] <= TIE:
            gate["sp_ties"] += 1
        elif int(np.argmin(sp1)) != int(np.argmin(J)):
            gate["worse_selected"] += 1
    n = counts["qualifying"]
    f = counts["worse_selected"] / n if n else None
    se = float(np.sqrt(f * (1 - f) / n)) if n else None
    gate["f_at_c11"] = gate["worse_selected"] / max(gate["qualifying_draws_checked"] - gate["sp_ties"], 1)
    out = dict(seed=SEED, c=[1, 3], counts=counts, f=f, se=se,
               sp_minimizer_not_a_local_min=sp_not_at_local_min,
               brute_force=brute, code_gate_B_C3=gate,
               cpu_seconds=round(time.process_time() - t0, 1))
    return out


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else N_DRAWS
    json.dump(main(n), sys.stdout, indent=1)
    print()
