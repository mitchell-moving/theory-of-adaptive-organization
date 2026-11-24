# T82: quasi-periodic worlds and torus memory

*24 November 2026 (UTC). Self-check, not an independent review. Chad's hypothesis, stated in `PREREG.md` and locked before this memo (commit `570c658`, sha256 `d0acb22ecefa52d41d95ca2a20f3fbfb251c237ee2bc9f6aa49549939508b204`; `torus_memory_checks.out:1`). The preregistration was not edited. `THEORY.md` and `CORE.md` are unchanged. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

**Chad's hypothesis.** A world of \(k\) incommensurate phases has minimal sufficient state \(T^k\), and the minimum of the tracking cost is a \(k\)-dimensional phase-only memory on that torus.

**Headline. RELABEL.** The hypothesis as one sentence is false. On a current sum the minimum is one scalar. On a zero-loss forecast the informative dimension is the dimension of the orbit closure, which is classical, and a small phase is dropped when its stake does not pay. Neither cell is a new design. One prediction misses: the joint minimum over the Kuramoto coupling is not the indifference coupling. That miss is a puzzle.

The X post at `https://x.com/mathemetica/status/2125282454110109990` is context only. It is not evidence and it is not an input.

## Scores

| Item | Score | Where |
|---|---|---|
| P1 current sum, dimension 1 | PASS | `torus_memory_checks.out:3` |
| P2 forecast dimension = rank over \(\mathbb{Q}\); radius free | PASS | `:4` |
| P3 \(P_D=I\) | PASS | `:2` |
| P4 symmetric menu, one phase never unique | PASS | `:5` |
| P5 unequal amplitudes, per-mode window | PASS | `:6` |
| P6 Adler boundary, one-bit drop at zero loss | PASS | `:7` |
| P7 minimizer over \(K\) equals the formula | **FAIL** | `:8` |
| P7 beyond-Kuramoto criterion | NOT BEYOND | `:8`, `:9` |
| P8 shared cause with the alignment clause | FAIL, as predicted | `:10` |
| Headline RELABEL | PASS | `:11` |

Checks: `theory/torus_memory_checks/torus_memory_checks.py`. FAILS 1, the scored P7 (`:12-13`).

## The cost

Class QP, exogenous, Haar measure on \(T^k\), memory not moving the world. The cost is the one T74 left open, with \(q=\kappa_D/\kappa\ge 0\):

\[
J=\kappa I+q\kappa P_D+w L.
\]

\(I\) is the classical record (`CORE.md:52`). \(P_D\) is the expected KL of the posterior from Haar, the classical dephasing score, not the quantum pinch. On a uniform prior that KL equals \(I\) (`PREREG.md` §2; `torus_memory_checks.out:2`), so

\[
J=\kappa(1+q)\,I+w L.
\]

\(q\) rescales \(\kappa\). It does not choose a dimension. This does not fix the quantum ratio left open by T74.

The method is: write that cost, minimize, read off the design (`CORE.md:47`).

## Q1. Dimension

**Current sum. Not \(T^k\).** Four equal bins on each circle. The sixteen phase pairs are uniform, entropy \(\ln 16=2.772588722240\). The sum of the bin-center cosines takes three values and has entropy \(1.039720770840\). Both memories output that same sum, so the loss matches, and the scalar memory is strictly cheaper at every \(\kappa(1+q)>0\) (`torus_memory_checks.out:3`). That is the shape of the sum-loss memory: one coordinate for a sum (`CORE.md:93`; Proposition G-sum, `theory/INFO_PHYSICS_GENERAL.md:191`, `:246`). **RELABEL (R-sum).** It is not a \(k\)-dimensional memory. The Gaussian rank-one proof is not reused; the collapse here is that many phases determine one sum.

**Zero-loss forecast. Dimension equals the hull.** \(\cos t+\cos(\sqrt{2}\,t)\) is not periodic, because a common period would make \(\sqrt{2}\) rational, and \(p^2=2q^2\) has no positive integer solution (the 2-adic valuation of the left side is even and of the right side is odd). Rank of \((1,\sqrt{2})\) over \(\mathbb{Q}\) is 2. Rank of \((1,3/2)\) is 1, and \(\cos t+\cos(3t/2)\) has period \(4\pi\) (`torus_memory_checks.out:4`). A coordinate frozen at a constant has mutual information 0, so a radius is not required. Phase-only is a minimizer. It ties with any memory that also stores null coordinates. **RELABEL (R-hull):** the internal model principle already says the regulator carries the generator (`theory/THEOREMS.md:208-210`). This is not the rank-one count.

**A small phase is dropped.** For \(y=\cos\theta_1+0.1\cos\theta_2\) the bit menu separates. Thresholds \(2\ln 2=1.386294361120\) and \(200\ln 2=138.629436111989\). At stake 10 the unique minimizer is the large phase only (`torus_memory_checks.out:6`). Informative dimension 1, not 2. **RELABEL (R-mode):** one coordinate per phase the stake pays for (`CORE.md:92`). On the symmetric menu the one-phase row is never unique (`:5`); identical phases are both kept or both dropped.

## Q2. Rational, irrational, locking

Rational versus irrational matters, and only as the rank above. That is P2. It is not a correction the cost adds on top of the hull.

At zero loss, Adler locking \(\dot\varphi=\Delta\omega-K\sin\varphi\) merges two phases when \(|\Delta\omega|\le K\). The discrete copy then drops one fair bit, and the cost drops by \(\kappa(1+q)\ln 2\) (`torus_memory_checks.out:7`, at \(\kappa=q=1\) the drop is \(1.386294361120\)). The boundary is Adler's. It does not move.

**Kuramoto.** For the Lorentzian of width \(\gamma=1/2\), \(g(0)=1/(\pi\gamma)\) and \(K_c=2/(\pi g(0))=1\), which is also \(2\gamma\). The amplitude \(r^2=1-K_c/K\) for \(K>K_c\) is the standard reduction those reviews record. Blind loss of the mean field is \(w r^2/2\). One phase bit costs \(\kappa(1+q)\ln 2\).

At fixed \(K\), the designs trade at

\[
K=\frac{K_c}{1-2\kappa(1+q)\ln 2/w}=1.383621274020
\]

for \(\kappa=1\), \(q=1\), \(w=10\). The bisection matches that expression with relative gap 0 (`torus_memory_checks.out:8-9`). Relative to \(K_c=1\) the gap is \(0.383621274020\). By the criterion locked in `PREREG.md` §0, this is the blind corner (`CORE.md:91`) with Kuramoto's \(r(K)\) substituted in. **NOT BEYOND.** Kuramoto already gives \(r(K)\) and \(K_c\). The repository already gives the blind corner. The cost does not force a third number.

**P7 fails.** The minimizer over \(K\) of the better design is not \(1.383621274020\). The cost is 0 for every \(K\in[0,K_c]\), where the mean field is already 0, and positive above \(K_c\) (`torus_memory_checks.out:8`). **Puzzle:** under this loss a coherent mean field is only a signal you can miss. Choosing the coupling, the minimum stays incoherent. The cost does not pay to lock. The indifference \(1.383621274020\) answers a different question, whether a memory is worth buying at a coupling the world already has, and that question is the blind corner.

## Q3. The alignment term

If the phase memory and the swarm rule shared a cause, three things had to match, locked before the run:

- M1. The part's choice equals the whole's optimum if and only if \(s_i=w_i/W\) (`theory/SWARM_RULE_2026-11-23.md:47`; `THEORY.md:486`).
- M2. At that share the part's cost is \((w_i/W)\) times the whole's cost (`theory/SWARM_RULE_2026-11-23.md:73`; `THEORY.md:491`).
- M3. Equal shares fail M1 at stakes \((1,4)\).

Adler's bound and \(K_c=2/(\pi g(0))\) do not contain a stake. Moving the stake ratio from \((1,1)\) to \((1,4)\) leaves both thresholds where they were (`torus_memory_checks.out:10`, `Kc_stakes_moved False`). **The shared cause fails.**

Copying the CT29 payment rule onto a shared coupling budget does satisfy M1–M3. At \(q_{\mathrm{world}}=c=1\) and stakes \((1,4)\), the joint total is \(1.581138830084\). Equal shares prefer totals \(1\) and \(2\). Stake shares \(1/5\) and \(4/5\) both prefer the joint total, and at total \(1.7\) the part's cost equals \((w_i/W)\) times the joint cost (`torus_memory_checks.out:10`). That copy is a **RELABEL** of CT29. It is not a consequence of the phase flow, and it is not support for a shared cause.

## Model implication

Inside class QP, with the classical \(P_D\) above and a slack ruin cap: the informative memory is a sufficient statistic of the loss. For a current sum that statistic is one scalar. For a zero-loss forecast it is the phase on the orbit closure, and phases the stake does not pay for are not stored. A radius that does not vary is free and not required. A coupling chosen inside this cost does not lock a Kuramoto mean field, because the incoherent field already has loss 0. None of this is a claim about a cell, a firm, a swarm, or a learned representation.

## Prior art

Crossref on 24 November 2026 (`theory/torus_memory_checks/crossref.out`). Kuramoto 1975, DOI `10.1007/BFb0013365`, pages 420–422, in the 1975 symposium volume `10.1007/BFb0013294` (the chapter's own issued field is empty). Kuramoto 1984, DOI `10.1007/978-3-642-69689-3`. Strogatz 2000, DOI `10.1016/S0167-2789(00)00094-4`, *Physica D* 143:1–20. Acebrón, Bonilla, Pérez Vicente, Ritort, and Spigler 2005, DOI `10.1103/RevModPhys.77.137`, *Rev. Mod. Phys.* 77:137–185. The circle-map reprint, DOI `10.1007/978-3-642-01742-1_10`, title "Small denominators. I. Mapping of the circumference onto itself," *Collected Works*, pages 152–223, issued 2009. That record's author list is empty; the locking file already names it as Arnold, and no 1961 DOI was verified (`DEVIATIONS.md`). Francis and Wonham 1976, DOI `10.1016/0005-1098(76)90006-6`.

`theory/TORUS.md` already records the torus as the state of two phases and leaves N45 open. This note does not rescore N45 and does not edit that file. `theory/THEOREMS.md:236-238` already checks Adler and \(K_c=2\gamma\).

## Checks

`python3 tools/check_open_work.py` passes. `python3 -m pytest -q` is 290 passed, 1 skipped (`tools/test_lean.py`, lake is not installed), and 1 failed: `tools/test_check_fresh.py::test_real_repo_status_is_in_window_after_fix`. `tools/check_consistency.py` reports that same freshness failure and no wording failure. `STATUS.md` is the file from upstream `d2aeb81`. Its pointer `31aa997` is inside the last 5 first-parent commits of that upstream main. The check judges the pointer against this fork's `origin/main` `0f37918`, which does not contain `31aa997`. This note does not edit `STATUS.md`.

## What remains

The P7 puzzle is the objective, not the algebra: a loss that punishes a missed mean field cannot reward creating one. A benefit of coherence that is not "match this mean field" would be a different preregistration. The quantum ratio \(q\) stays the open number of T74; on this classical torus it is not a second coordinate.
