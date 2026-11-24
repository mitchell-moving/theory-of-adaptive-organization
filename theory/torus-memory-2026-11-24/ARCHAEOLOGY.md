# Archaeology for the rational / irrational split

*24 November 2026. Searched this work tree at `e03b5f0`, whose first parent on public upstream is `d2aeb81`. Tools: `rg` over `*.md`, `*.py`, `*.lean`, and `git log --all -S` for Arnold tongue, quasi-periodic, rotation number, KAM, golden ratio, Diophantine, Talbot, small divisor, badly approximable. `git log --all --grep=T83` is empty. No Lean file states a torus, a rotation number, or a KAM lemma.*

Incidental hits are listed once at the end so they are not read as this claim. Each row below is a claim about frequencies, locking, or tori.

## Textbook torus and Arnold tongues

| Where | Commit | Claim | Tested? |
|---|---|---|---|
| `theory/TORUS.md:16` | `d57669d9428585dcadb70dbcd2508c38b99dcc50` (18 Nov 2026) | Two phases live on \(T^2\). An irrational frequency ratio fills the torus. A rational ratio closes. | Stated as textbook. Not given its own numerical test in that file. |
| `theory/TORUS.md:17-18` | `d57669d9` | The sine circle map locks ranges of \(\Omega\) to rational rotation numbers. The 0:1 tongue has width \(K/\pi\). | Yes. `theory/reach_checks/circle_map.py:3-27`, output `circle_map.out`, same introducing commit. Widths 0.0798, 0.1593, 0.2387, 0.3182 against \(K/\pi\) at \(K=0.25,0.5,0.75,1\). |
| `theory/TORUS.md:20` | `d57669d9` | KAM: sufficiently irrational (badly approximable) tori survive small perturbations. The golden ratio is the last to break. | Not tested. Named as textbook. The note says Adler, Pikovsky et al., Arnold, and Greene were not opened. |
| `theory/TORUS.md:45-51` | `d57669d9`, tongue exponents amended `270969889507657ff88dce1ae7dfe6f45b35354c` | N45: locking plateaus in adaptive loops, width tracks coupling cost. A \(p/q\) tongue grows like \(K^q\) at small \(K\). | The circle-map exponent was checked (`theory/reach_checks/independent_review_checks.py:80-94`, commit `27096988`: local exponents about 2 for 1:2 and about 3 for 1:3). The adaptive-loop claim is OPEN. No real pair has been run. |
| `theory/TORUS.md:53-66` | `c683244b13b9029a246e0cff228f2daa97aa7627`, scope fix `e1b23e91a5608812b04dd9cbacd20d7d9af5c28f` | N49: plateau width \(\varepsilon(Z_{\max}-Z_{\min})\), and the optimum is continuous in price iff \(\|\mu\|\le\sigma\). | Yes, in-model, `theory/reach_checks/price_maps.py`. Not a test of rational versus irrational survival. |
| `theory/THEOREMS.md:218-219` | `54ae2ceb8915b68597766ab0a6dddbbbe9b86c95` | Incommensurate frequencies wind densely on \(T^2\). KAM: Diophantine tori survive small perturbations. | Named as known mathematics. The link to the hypothesis is labeled an untested analogy (`theory/THEOREMS.md:215`). |
| `theory/theorems-checks/check_all.py:184-206` | `54ae2ce` | Adler locks iff \(\|\Delta\omega\|\le K\); otherwise the flow is called quasi-periodic on \(T^2\). Kuramoto on \(T^N\) collapses to a point or a cycle when frequencies are identical. | Numerical check inside that script. Not a preregistered rational/irrational grid. |
| `measurement/CLAIM_MAP_v2.md:481` | `d57669d9` | N43, prior art: \(T^2\), Arnold tongues, KAM as textbook support. | Points at the circle-map check. Sources not opened. |

## What the cost did with rational ratios

| Where | Commit | Claim | Tested? |
|---|---|---|---|
| `theory/spacing_checks/antilock.py:1-10` | `7d8690ce9d58992a27c838f31fdaf61965118474` | Part A: does a linear two-store error have features at simple rationals? Part B: are the widest unlocked gaps of the circle map at the golden mean? | Exploratory. LOCK1 discloses the numbers and does not score them (`tests/LOCK1/PREREG.md:11`). Part A roughness 1.04–1.10. Part B: the widest gaps were not at the golden mean. |
| `tests/LOCK1/PREREG.md:20-28` | `5f9f5bec75c1de303245b5a98976138960ac879e` | Locked before the run. B1: optimal ratios move away from low-order rationals. B2: they are more badly approximable. B3: golden or noble ratios are selected, and B3 was expected to fail. B4: the linear class has no rational structure. | Yes. `tests/LOCK1/RESULTS.md:3-18`, commit `7d8690c`, output `tests/LOCK1/lock1.out`. B1 FAIL (the optimum moved closer to rationals). B2 FAIL at \(K_c=0.6\). B3 FAIL, as expected. B4 PASS. The results say anti-locking stops at a tongue edge and does not pick badly approximable numbers. Golden-mean survival at critical coupling was not reached. |
| `reviews/shannon_2026-11-21/REVIEW.md:227` | `e59fd2039de3d8355e780dce4d72b2eccf226cab` | Records the B2 Diophantine miss. | A review of the LOCK1 number, not a new run. |

LOCK1 is the opposite sign of N45: there, locking to an outside cycle is a benefit; in LOCK1, locking between layers is a cost. Neither test is a Hamiltonian flow, and neither measures a return share.

## This branch, already scored

| Where | Commit | Claim | Tested? |
|---|---|---|---|
| `theory/torus-memory-2026-11-24/PREREG.md:57`, `:89-101` | `570c6583b26906febdbece8a265f252c69401c9e` | Rational \((1,3/2)\) versus irrational \((1,\sqrt{2})\): the zero-loss forecast dimension is the rank over \(\mathbb{Q}\). Adler's merge starts at \(\|\Delta\omega\|\). | Yes. P2 and P6 PASS (`theory/torus_memory_checks/torus_memory_checks.out:4`, `:7`). That is the hull dimension, not KAM survival and not a measured return. |
| `theory/torus-memory-2026-11-24/PREREG_COUPLED.md:77-84` | `0352de59ee3412007065cd95bfc77d5d33ed0054` | Classify the lag map as a fixed point, a limit cycle, or a torus by a tail range, a period, and a rotation number. | Yes. 144/144 FIXED (`coupled_loop_checks.out:3`). The destruction rate sat on the menu endpoints 1 and 9 (`coupled_loop_checks.out:19-30`). The rotation number was computed about a centroid of a contracting orbit. It was not a frequency of a conservative flow. |

## Lean

`formal/lean/` has 23 `.lean` files. None names a torus, a rotation number, Arnold, KAM, a continued fraction, or a frequency ratio. The two matches for "quasi" are not this subject: `formal/lean/GTAO/CT22.lean:29` (quasiconvexity) and `formal/lean/GTAO/Equipartition.lean:190` (`quasiMeasurePreserving`). No lemma is available to reuse.

Natural formalization targets, not started: the rank-over-\(\mathbb{Q}\) statement scored as T82 P2; the 0:1 tongue width \(K/\pi\) already checked in `circle_map.py`; and the statement that a constant-frequency flow on \(T^2\) is periodic exactly when the frequency ratio is rational.

## Searches with no claim

- `git log -S Talbot` and a search for `T_rev`, Talbot, and a Berry fractal returned nothing. The name Berry in this repo is the retinal coauthor in Palmer, Marre, Berry, and Bialek 2015, not the Talbot carpet.
- `git log -S 'small divisor'` returned nothing. Arnold's circle-map paper is cited by title in `PREREG.md:75` as the 2009 reprint, DOI `10.1007/978-3-642-01742-1_10`.
- No file and no commit message names T83. The revival split (periodic revival at a rational fraction of a revival time, fractal filling at an irrational fraction) is not a result in this tree. T82b can name it only as the same rational/irrational dichotomy, not as a theorem found here.
- No file names T84. Dissipation at a rate \(\gamma\) is not a scored result in this tree.
- "Golden section" in `theory/layer-fixed-point-2026-11-23/` is an optimizer. "Fractal" in T54 and N46 is a dimension or a withdrawn framing. Neither is a frequency ratio.

## What the new lock should not repeat

The circle-map tongue width is already checked. LOCK1 already failed the claim that the cost selects the golden mean. A new prediction has to be about a closed reversible flow and about the measured return, and it has to be able to fail without moving those older scores.
