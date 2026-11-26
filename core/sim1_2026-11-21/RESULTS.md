# T28 official results: PASSED (P1, P2, P3, P4 all 3/3)

*Scored Saturday 21 November 2026, 12:55:09 AM EST (America/New_York), after the lock at 12:54:44 AM EST. In-model. P1–P3 analytic (exact discrete argmin); P4 numerical. Not a field test. Predictions were not patched. Locked files were not edited.*

**OVERALL: PASS.** Three official-valid worlds (the first three candidates; none rejected). P1 passed 3/3, P2 passed 3/3, P3 passed 3/3, P4 passed 3/3. Official P1–P3 PASS 3/3 are implementation-and-box checks of theorems on this model, not stochastic evidence (P1 and P3 could not have failed under the stated model; P2 was pre-verified on all 16 locked-box corners and the 20 published pilots); P4 is the only numerical test. Everything here is in-model only.

Lock (unchanged, and matching `run_sim1.json`):

| File | SHA-256 |
|---|---|
| `PREREG.md` | `f24d54271875a326947c7a17fc6114a0d8b0a7864c5ff17dc0eca2300260de8c` |
| `predictions.json` | `40c14cb4f991bee864b8bf74ab7f4583766cfb2ccab6aaf712deb692d2f33b09` |
| `run_sim1.py` | `9f3f41700aee9335f5f50f6612712fb87dee95b7a56fc732b418df917641181f` |
| `sim1_lib.py` | `2f20672665503aa6b0d48ef907ae3f24edded5ac935d191474b42ee383846559` |

The official runner printed `LOCK ok` before evaluating any official world. Raw output: `run_sim1.json`, `run_sim1.log`. Run time 12.0 s at nice 19.

Official rng seeds: 20261122000, 20261122001, 20261122002. Mixing SANITY passed on every official cell (TV to exact Boltzmann \(0.027\)–\(0.042\), bar \(0.20\)).

---

## P1 — PASS, 3/3 worlds, all four \(K\), both ladders (analytic)

At each locked \(K\in\{0,1,2,3\}\), the least discrete \(m^\star(w)\) was nondecreasing on the locked \(W\)-ladder, and the least discrete \(m^\star(\lambda)\) at \(w=1\) was nondecreasing on the locked \(\lambda\)-ladder. This is the Topkis comparative static at fixed \(K\), with the ruin cap slack (exposure additive). It is a theorem on this model; the official numbers are an exact check that the discrete implementation matches it.

| world | seed | \(m^\star(w)\) at \(K=0\) | \(m^\star(w)\) at \(K=3\) |
|---|---|---|---|
| 0 | 20261122000 | 0,0,0,0,0,3,5,9,14,21 | 0,0,0,0,0,0,0,2,4,7 |
| 1 | 20261122001 | 0,0,0,0,0,2,4,7,10,15 | 0,0,0,0,0,0,0,3,5,8 |
| 2 | 20261122002 | 0,0,0,0,2,3,5,9,13,19 | 0,0,0,0,0,2,3,5,8,11 |

Full \(K=0..3\) ladders, including \(\lambda\), are in `run_sim1.json`.

## P2 — PASS, 3/3 worlds, all four \(K\) (analytic)

At each locked \(K\), \(m^\star(0.02)=0\), \(m^\star(20)\ge 1\), and the exact threshold \(W_{\mathrm{th}}(K)=\inf\{w:m_K^\star(w)\ge 1\}\) sat strictly between those rungs.

| world | \(W_{\mathrm{th}}\) at \(K=0,1,2,3\) |
|---|---|
| 0 | 0.711, 1.910, 3.109, 4.308 |
| 1 | 0.769, 1.271, 1.773, 2.275 |
| 2 | 0.330, 0.503, 0.675, 0.848 |

This is the CT4-style “first model and first rollout must pay” threshold, a theorem on this model, checked exactly.

## P3 — PASS, 3/3 worlds, all four \(K\) (analytic)

At \(w=5\), \(\lambda=0\), the least discrete \(m^\star(c)\) was nonincreasing on the locked \(c\)-ladder at every locked \(K\). Theorem (Topkis in \((m,-c)\)), checked exactly.

Example, world 0 at \(K=0\): \(m^\star(c)=23,16,9,6,3,1,0\) as \(c\) runs \(0.01\) to \(1\).

## P4 — PASS, 3/3 worlds (numerical)

At the locked P4 cell (\(w=20\), \(c=0.05\), \(\lambda=0\), \(\beta=40\)), the pooled Moran occupation (8 chains, 150,000 jumps, 15,000 burn, \(N=201\), reused `run_moran_ct`) satisfied both official clauses: the mode of the marginal on \(m\) equalled the unique discrete \(m^\star\), and \(|\bar m-m^\star|\le 1.5\).

| world | seed | \((K^\star,m^\star)\) | TV | emp \(\bar m\) (exact) | emp \(\lvert\bar m-m^\star\rvert\) | marg. mode |
|---|---|---|---|---|---|---|
| 0 | 20261122000 | (3, 7) | 0.0402 | 7.329 (7.206) | 0.329 | 7 |
| 1 | 20261122001 | (3, 8) | 0.0422 | 8.258 (8.378) | 0.258 | 8 |
| 2 | 20261122002 | (3, 11) | 0.0266 | 11.881 (11.783) | 0.881 | 11 |

Exact Boltzmann values are a validity screen and a diagnostic, not the official bar. All three worlds were unique-min, with \(2\le m^\star<40\), and already satisfied both clauses under exact \(\pi\) before the chain was run.

This is a finite-sample numerical test, not a theorem about Moran trajectories. It supports, in these three worlds, that high-\(\beta\) weak-mutation search on the locked \((K,m)\) graph finds \(m^\star\) within the locked tolerance.

---

## Diagnostic (not a gate)

On all three official \(W\)-ladders, joint \((K^\star,m^\star)\) had nondecreasing \(m\), nondecreasing judgment spend, and nonincreasing expected error (CT33). Joint monotone \(m\) was **not** a locked prediction: layers and rollouts are substitutes, so \(m\) can in principle fall when a new layer is added as stakes rise. It did not fall on these three ladders.

---

## What this does and does not establish

Established **in-model**, on this rehearsal mechanism, with the ruin cap slack and official P1–P3 at **fixed \(K\)**:

- Optimal designs simulate more as stakes or ruin-exposure weight rise, and less as compute gets more expensive (P1, P3; theorems, exact check).
- They simulate zero below a stakes threshold at which the model and the first rollout pay (P2; theorem, exact check).
- At high selection strength, a weak-mutation Moran search finds that \(m^\star\) within the locked tolerance (P4; numerical, 3/3).

Not established: anything about nature; the Lundberg-cap regime, where CT33 can fail; joint monotone \(m^\star\) once \(K\) is also chosen; a field test of SIM-1. The hypothesis in [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md) (SIM-1) and the sentence in `CORE.md` §3 are unchanged. The official record of this prereg is PASS.

World parameters, ladders, occupation summaries, and exact-Boltzmann diagnostics are in `run_sim1.json`.
