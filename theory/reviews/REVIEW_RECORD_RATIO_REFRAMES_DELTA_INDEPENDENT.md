# Independent delta review: T75/T76 at 796d8a7

Head `796d8a73c539dada01bbfc9308c2ffd7316dff9e` on `forge-record-ratio-reframes`. Scope is the delta after Ace's review of upstream PR #257 at 21:06 UTC (https://github.com/Chad-Mitchell/theory-of-adaptive-organization/pull/257#issuecomment-7144476241), which covered `bcb6235` and asked for a merge of `main`, the K2 `net_min` fix, the word "draft" dropped from the ready PR, and a pre-check plus an independent review on the new head. The two commits since `bcb6235` are the merge `08d240d` and `796d8a7`. This file does not edit a lock, a stored run, `THEORY.md`, or `CORE.md`.

Gate text used for the labels: `process/PREREG_GATE.md` on upstream draft PR #263 (`8c4b3c0`), with `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at upstream `main` `835ea7c`.

## Result

Two blockers. The merge, the K2 correction, the `FAILS 4` count, the lock hashes, and the append-only logs hold. T75's `CONSISTENCY_CHECK` label holds. T76's `TEST` label holds for the bars that the locked formulas do not already fix, and several other bars are identities. One new ledger row is split by an unescaped pipe. The ready upstream PR still says draft.

## Ace's list

1. Merge `main`, no rebase, conflicts only in `OPEN_WORK.md` and `theory/README.md`, and put the STATUS pointer inside the last-five first-parent window. Holds. Detail below.
2. Stop overwriting `net_min` with the least-squares residual, print both, correct the memo, add a deviations entry, leave the preregistration alone. K2 still misses. Holds. The independent recomputation is below.
3. Drop "draft" from the PR title, and from the body headline if it still says draft. Does not hold. Upstream #257 is marked ready and the title is still "Record-ratio consistency and reframes: 0 and 1 are boundary fixed points, ratio set outside the cost (T75 folded into T76, draft)". The body still opens "Draft, self-check" and still names head `40c4060`. Fork PR #8's title has no "draft"; its body still opens "Draft, self-check" and still names head `bcb6235`.
4. One pre-check and one independent review on the new head. This file is the independent review of `796d8a7`. Fork PR #8 has no pre-check comment on that SHA (the latest pre-check there is `0598334`).

## Claim 1: the merge

`08d240d` has parents `bcb62358abb9aa74f3cbcc2800643c1500100f97` and `835ea7c082928be081a3ef1ba2c60eaa1fc3a742`. `835ea7c` is upstream `main`, and `652d936` (PR #261, the miss-vocabulary merge) is its first parent. The first-parent chain of `796d8a7` is `796d8a7`, `08d240d`, `bcb6235`, then the earlier branch commits. The five lock commits are the original objects and are ancestors of `796d8a7`. That is a merge. The branch history was not rewritten.

The only paths that differ from both parents of `08d240d` are `OPEN_WORK.md` and `theory/README.md`. On those files the merge keeps the rows `main` had and the rows this branch had:

- T69, T70, T71, T73, and T74 in `OPEN_WORK.md` at `08d240d` are byte-identical to `835ea7c`. T72 has no row on `835ea7c` either (the composite question is still the open fork draft, which the T74 cell already says).
- T75 and T76 at `08d240d` are byte-identical to `bcb6235`. `796d8a7` then adds the G2 labels and the corrected K2 numbers.
- `theory/README.md` at `08d240d` carries the T73 and T74 index lines from `main` and the T75 and T76 index lines from the branch. `796d8a7` adds the two G2 words (`theory/README.md:52`, `:53`).
- `STATUS.md` at `796d8a7` is identical to `835ea7c`. Line 3 says `main` is `d2aeb81`. That commit is inside the last five first parents of `835ea7c` (`835ea7c`, `652d936`, `d2aeb81`, `31aa997`, `8c48a5b`). `tools/check_fresh.py` on this tree compares against `origin/main`, which in this clone is the fork tip `d2aeb81`, and passes with window `d2aeb81 31aa997 8c48a5b 04e9e5b 0e22302`.

## Claim 2: K2 `net_min`

The bug at `bcb6235` was the assignment after the least-squares fit (`record_ratio_reframes_checks.py` lines 353–355 on that commit): if the least-squares max residual was smaller than the net minimum, it replaced `net_min` and `net_at`. `796d8a7` deletes that assignment. The comment that the least-squares point is not a net point is now at `theory/record_ratio_reframes_checks/record_ratio_reframes_checks.py:353`. `net_min` stays the minimum of `max |alpha I + beta P_D - chi|` on `alpha, beta in {-2, -1.95, ..., 4}` (`:331-346`). The pass test is still both residuals above `0.005` (`:355`).

Independent recomputation, stdlib only, not importing the module. BIAS weights `0.8/0.2` on Bloch vectors `(0,0,±0.6)`, `gamma = 0`, 721 angles with step `(pi/2)/720`, binary entropy in nats, Holevo `chi = S(rho_bar) - E[S(rho)]`.

- `chi = 0.126467034034`, constant on the grid.
- `max |I + P_D - chi| = 0.06627772`, which prints as the stored `0.066278`.
- Least squares of `chi` on `(I, P_D)`, no intercept: `alpha = 1.0033319156709783`, `beta = 0.6581687266183742`, max residual `0.0004213774925606`. The stored print `1.0033319156709788` and `0.6581687266183737` differs in the last bit. Gram determinant `3.835855e1`.
- The 121 by 121 net has 14641 points. The unique minimum is `0.0014997828907532262` at `(1.0, 0.65)`. The four adjacent net points are `0.006323` at beta `0.65` and `0.008454` or `0.010820` at the other neighbors, all above `0.005`.
- Putting the least-squares residual back into `net_min` whenever it is smaller reproduces the stored original line: `net_min=0.0004213774925606595 at=(1.0033319156709788, 0.6581687266183737)` (`record_ratio_reframes_checks.out:10`).

Both numbers are below `0.005`, so `K2-bound-weight` still fails. The live script's stdout is exactly the non-comment lines of the appendix. That block's K2 line is `record_ratio_reframes_checks.out:34`:

`K2-bound-weight FAIL net_min=0.0014997828907532262 at=(1.0, 0.65) n_net=14641 ls_alpha=1.003332 ls_beta=0.658169 ls_max=0.000421`

The four miss lines in that block are `K2-bound-weight`, `G5`, `C1`, and `C2`. The block ends `FAILS 4` (`:43`). The original block ends `FAILS 4` (`:19`) for the same four names. `FAILS 4` is the right count. The memo correction is `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:160`. D7 is `theory/record_ratio_reframes_checks/DEVIATIONS.md:33`. The preregistration blob is unchanged (hash below).

## Claim 3: G2 labels

`process/PREREG_GATE.md` §2: if the scored value follows from the starting formulas, a definition, or a known theorem, the item is a `CONSISTENCY_CHECK` and is not run as a test. §4: work already scored keeps its lock and states `TEST` or `CONSISTENCY_CHECK` at the top of the memo and the `OPEN_WORK.md` row.

The labels are where the builder says:

- T75 `CONSISTENCY_CHECK`: `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:3`, `OPEN_WORK.md:125`, `theory/README.md:52`.
- T76 `TEST`: `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:3`, `OPEN_WORK.md:126`, `theory/README.md:53`. The T76 sentence says a clause whose value is a hand computation of the cost is a consistency check inside the test.

T75 holds. Routes A, B, and D are algebra on the closed form already locked on draft #252. Route C is Reeb and Wolf 2014, which resolves on Crossref (below). The five ledger rows say the information is about 0. The headline does not claim support from those hits.

T76 holds as a `TEST` because these scored bars are not fixed by a hand evaluation of the locked cost:

- K2's net minimum and least-squares residual, recomputed above. The bar `f > 0.005` misses on both.
- G4, partial dephasing, non-commuting stake: the ratio-1 and ratio-100 minimizers differ by `0.464694` rad (`record_ratio_reframes_checks.out:14`). The first lock does not give that angle in closed form.
- The `gamma = 1/2` cell in `PREREG_FIXED_POINTS.md:90`. The lock says the `gamma = 0` root is not claimed there. The stored gap is `0.704255` rad.
- R-low and R-high. The locked predictions are the collision angle `pi/4` and the pointer. The stored minimizers are the equator at `w = 1`, and grid nodes `1.468258` and `1.005746` at `w = 4` and `w = 10`.
- F-span's two-copy residual `2.078781e-5` against the bar `0.01`, and Q-reuse's conditional information `0.017070` against the bar `0.05`. Neither number is a closed form written in the lock. This pass did not recompute the quantum grid; the earlier independent review of `40c4060` covers the instrument. The G2 question for those two bars is whether the lock already fixes them. It does not.

These T76 bars are identities, so they are consistency checks inside the test. The memo's second sentence covers them. The ledger marks some of them "information about 0" and leaves others as ordinary hits:

- H1-lin. At fixed angle, `J = kappa I + q kappa P_D + w L` and `(I, P_D, L)` do not depend on `q` (`mhd_analogy_checks.py:37-39`). The second difference is an algebraic zero. The stored residue is `2.776e-17`. The ledger row says the information is about 0.
- H1-joint. For `q >= 0` and `P_D >= 0`, `J(q, theta) >= J(0, theta)` at every angle, so the minimized cost at `q` sits at or above `J*(0)`. The ledger row `H1-joint` records a HIT and does not say the information is about 0.
- G5. On the antipodal complete-dephasing ensemble, `I + P_D = chi` is constant (K1 residual `5.551e-17`) and `chi = P_chi(0) = 0.096372378511`. The two price vectors `(1, 0.5)` and `(1.5, 1)` differ by `(0.5, 0.5)`, so the cost gap at every angle is `0.5 chi = 0.048186189255`. The live script prints that same gap at all six stakes, and `literal_miss = 4.819e-2`, which is the other half. The minimizers agree because the gap does not depend on the angle. The locked symbol asked for the full `P_chi(0)`. The miss of that symbol was fixed by the identity before the grid. Ace's 17:10 UTC note said to keep the literal FAIL, and the run does. The ledger row calls the location `model`. Under G2 this bar is a consistency check of a mis-stated multiple.
- G1, G3, C3, and the antipodal endpoint switch. The locks already say these check a published closed form (`PREREG.md:94`, `:118`; `PREREG_FIXED_POINTS.md:23`, `:85`). With `r = 0.6`, `w_pi = 1/r^2 = 2.777777777778` and `w_0 = ln((1+r)/(1-r))/(2 r^3) = 3.209014724815`. For `|delta| = 0.5` the interior window is `(1.388888888889, 1.604507362407)`. C1's stake list `{0.5, 1, 2, 4, 8}` has no point in that window, so "at least one interior stake" misses by arithmetic on the closed form. C2 is the biased ensemble, where that antipodal window is not the formula, and the stored run has one interior stake.
- F-menu (Route A), R-class (the three-rate identity), Q-rank (the named projectors fix the block, so `P_D = 0`), and the antipodal half of D-value. The ledger already marks these as information about 0.

The `TEST` label on the whole item stands. The support the memo is allowed to carry is the bars in the first list, including the K2 miss, the repeated-record misses, and Q-reuse. The identity clauses do not add a support headline.

## Claim 4: eight-field rows

`DEVIATIONS.md:41` is the ledger heading. The eight column names are at `:49`: `prediction_id`, `locked_prediction`, `outcome`, `miss`, `location`, `stake_x_info`, `update`, `breach_check`. `RECORD_RATIO_CONSISTENCY_2026-11-24.md:195` is the T75 ledger heading, and the same eight names are at `:201`. The five T75 rows each have eight cells. The T76 ledger has a row for every `PASS`/`FAIL` name in the five stored `.out` logs, plus `K2-print` and `Q-coh-script` for the two code misses. Medium rows have a scaled block under `:102`. D1–D6 are a byte prefix of the `bcb6235` file; D7 and the ledger are appended.

One row does not have eight cells. `DEVIATIONS.md:69`:

`| T-mono | \(w_{\mathrm{crit}}/|\delta|\) strictly decreasing on fifty angles | ...`

The pipe in `|\delta|` is a column break. Splitting that line on `|` yields ten cells, and the HIT, the location, the stake, the update, and the breach check shift one column to the right. The other forty-nine T76 rows have eight cells.

## Locks and logs

| Lock | Commit | sha256, matches the sidecar and the bytes at HEAD |
|---|---|---|
| `PREREG.md` | `8563c91` | `8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8` |
| `PREREG_FIXED_POINTS.md` | `c864603` | `82d58bdcefca97218ac4b7587a9246850994eedac1c6c372de8f50a75417017b` |
| `PREREG_MHD.md` | `4ca0322` | `faf04d3d53de980141cbfd57a3dfb30f34af6e6f8d7efb5ce72f5a01e3dc25b6` |
| `PREREG_REPEAT_ASYMPTOTE.md` | `e0b411a` | `5b0846fa823e86d63c71133831ec966ac42f3f3a27f1cff9ec613c392adfa60a` |
| `PREREG_QUANTUM.md` | `dba140b` | `1ac92e314705b3378e3b6a1bd665d36ec6dc9f7f812760a20bc4556617b817d3` |

Each lock blob at HEAD equals the blob at the lock commit. `record_ratio_reframes_checks.out` at `bcb6235` is a byte prefix of the file at HEAD (19 lines, ending `FAILS 4`). `fixed_point_checks.out`, `mhd_analogy_checks.out`, `posthoc_windows.out`, `quantum_record_checks.out`, and `repeat_asymptote_checks.out` are the same blobs as at `bcb6235`.

## THEORY.md and CORE.md

`git rev-parse 796d8a7:THEORY.md` and `835ea7c:THEORY.md` are both `6caadae569116a94a74563398be94cebf6e99e9b`. `CORE.md` is `dbf0d2322ce9fe751a5359e85859ca6f9448ec66` at both. `835ea7c` is upstream `main`. The diff of those two paths from `835ea7c` to `796d8a7` is empty.

## Checks

Run from `/tmp` worktree of `796d8a7`, after installing packages for the suite (pytest 9.2.0, NumPy 2.5.5, SciPy, SymPy, numba 0.68.1). Those packages are not in the tree.

- `python3 tools/check_consistency.py`. Exit 0. `RESULT: PASS`. `FAIL: 0`. Wording FAILs 0 on 34 maintained docs. INFO hits on frozen records: 29. CLAIM_MAP section N: 68 rows, 126 references, 0 mismatches. Process-rule FAILs 0. Core-rule FAILs 0. Soft length warnings only (`THEORY.md` 11325 words, `README.md` 1880).
- `python3 tools/check_open_work.py`. Exit 0. `RESULT: PASS`. Union missing from `OPEN_WORK.md`: 0.
- `python3 tools/check_fresh.py`. Exit 0. `RESULT: PASS`. Pointer `d2aeb81`, as above.
- `python3 -m pytest -q`. **307 passed, 1 skipped, 499.58 s, exit 0.** The skip is `tools/test_lean.py:124`, Lean 4 / lake is not installed. With numba installed, `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py` collected and passed. `tools/test_record_ratio_reframes_checks.py` is in that pass: the original log is preserved, and the live stdout matches the appendix.

Added lines in `08d240d..796d8a7` were scanned for `puzzle`, `kill`, `failure`, `bill`, `solved`, `verdict`, `law`, and `theory of everything`. No hits. The new sentences use `miss` for the K2 bound clause and `measurement/code` for the overwritten field.

## Crossref

DOIs in the files `796d8a7` changes, looked up on 24 November 2026. `OPEN_WORK.md` contains further DOIs on rows this commit does not edit.

| DOI | Crossref | Matches the note |
|---|---|---|
| `10.1088/1367-2630/16/10/103011` | Reeb, Wolf, "An improved Landauer principle with finite-size corrections", New Journal of Physics 16, 103011, issued 8 October 2014 | `RECORD_RATIO_CONSISTENCY_2026-11-24.md:144` and the T75 row |
| `10.1002/j.1538-7305.1956.tb03809.x` | Kelly, "A New Interpretation of Information Rate", Bell System Technical Journal 35, pages 917–926, issued July 1956 | `RECORD_RATIO_REFRAMES_2026-11-24.md:154`, `:234` |
| `10.1017/9781316672853` | Davidson, "Introduction to Magnetohydrodynamics", Cambridge University Press, print 22 December 2016, online 9 February 2017 | `:39` |
| `10.1115/1.3625105` | Sutton, Sherman, Cohen, "Engineering Magnetohydrodynamics", Journal of Applied Mechanics 33, page 478, issued June 1966 | `:39`, the one-page notice |

## Attacks tried

- Recomputed the biased K2 curve, the least-squares fit, and all 14641 net points in a separate script. The unique net minimum and the least-squares residual match the appendix. Re-applying the deleted assignment reproduces line 10 of the original log. Both residuals miss `0.005`, so the corrected run still fails and the count stays 4.
- Ran the author's script and compared stdout, byte for byte, with the non-comment lines of the appendix.
- Hand-evaluated G5 from K1: the gap is `P_chi(0)/2` at every angle. The live gaps match that number at all six stakes.
- Hand-evaluated the antipodal switch window `w_pi = 2.777777777778`, `w_0 = 3.209014724815`, and the `|delta| = 0.5` window that C1's stake list misses.
- Checked H1-lin and H1-joint from the definition of `J` in `q`.
- Split every new ledger row on `|` and counted cells. T-mono is the row that breaks.
- Compared lock blobs, sha256 sidecars, `.out` prefixes, and the merge parents. Compared `THEORY.md` and `CORE.md` to upstream `main`.
- Ran `check_consistency.py`, `check_open_work.py`, `check_fresh.py`, and the full pytest suite.
- Resolved the four DOIs above on Crossref.

Blockers remaining: 2
