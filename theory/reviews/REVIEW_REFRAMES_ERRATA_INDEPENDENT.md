# Independent re-review of the Q-coh errata

Head `40c40604613e995a11246b389e135bab62672fd5` on `forge-record-ratio-reframes`. The prior review is `theory/reviews/REVIEW_REFRAMES_COMBINED_INDEPENDENT.md` at `22b249f` on `forge-reframes-combined-review`, of head `d117ca6`. That review had one blocker: Q-coh was scored on the dephasing map. This note checks the re-score at `9284624` and the restoration at `40c4060`. `THEORY.md` is unchanged (blob `6caadae569116a94a74563398be94cebf6e99e9b`).

## Result

The projectors named in `PREREG_QUANTUM.md` fix the coherent block. An independent matrix product gives \(\Phi(\rho)=\rho\), so \(P_D=0\) and the cost gap at \(q=1\) against \(q=0\) is \(0\). Both locked bars miss. The appended line `Q-coh FAIL PD=0.000000 cost_gap=0.000000` and the appended `FAILS 2` are the score of that instrument. The live script prints that block.

The five preregistration files and their sha256 sidecars are the blobs from their lock commits. The `00e8dfa` run log is a byte prefix of `quantum_record_checks.out`. Commit `9284624` had replaced the Q-coh line. Commit `40c4060` puts those original bytes back and appends the re-score. `DEVIATIONS.md` D1–D3 are the `00e8dfa` text, D4 is the `9284624` text, and D5 is added.

The three medium items from the prior review are fixed in the memo, the index row, and the open-work cell's later sentences. The strings `Q-coh PASS` that remain are the restored prefix, the test that locks that prefix, and the deviation sentences that quote it.

Two low items remain. D4 names the old subtraction in the reverse order. The T76 row in `OPEN_WORK.md` still opens the fifth lock with `FAILS 1`, and the same cell later says the corrected run is `FAILS 2`.

## What was run

All three checkers from the repo root, on this head, exit 0.

- `python3 tools/check_consistency.py`. `RESULT: PASS`. `FAIL: 0`. `INFO (frozen records): 29`. Maintained docs scanned: 31; wording FAILs: 0. Frozen records scanned: 496. CLAIM_MAP section N: 68 rows (`N1`..`N68`); N references checked: 123; mismatches: 0. CLAIM_MAP rows counted: 392 (tally 392). Tables checked: 124. Process-rule FAILs: 0. Self-reviews found by header: 14. Appendix C and CLAIM_MAP section O: 74 and 74. Core-rule FAILs: 0. Soft length warnings: `THEORY.md` 11325 words, `README.md` 1857 words.
- `python3 tools/check_open_work.py`. `items.json` not-DONE: 62; `QUEUE.md` not-DONE: 90; union missing from `OPEN_WORK.md`: 0. `RESULT: PASS`.
- `python3 tools/check_fresh.py`. `STATUS.md` main is `d592662`; window `0f37918 d592662 f4ec246 341b7de b611a68`. `RESULT: PASS`.

Pytest, after installing NumPy 2.5.5, SciPy 1.18.1, SymPy 1.14.0, and pytest 9.2.0 for the run. Those packages are not added to the tree. `lake` is absent. `numba` is absent (`ModuleNotFoundError`). `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py` was not executed. Its module body writes `test_result.json`.

- `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE`. **301 passed, 1 skipped, 377.52 s, exit 0.** The skip is `tools/test_lean.py:124`, `Lean 4 / lake is not installed`. The extra pass against the prior head's 300 is `test_quantum_original_run_log_preserved`.

The Q-coh arithmetic below does not call the repository script. The script was then run, and its stdout is the appended block.

## Q-coh recomputed

The lock's coherent state and the review instrument are

\[
\rho=\begin{pmatrix}1/2&0&0\\0&1/4&1/8\\0&1/8&1/4\end{pmatrix},
\qquad
P_0=|0\rangle\langle 0|,
\qquad
P_1=|1\rangle\langle 1|+|2\rangle\langle 2|.
\]

The Lüders map is \(\Phi(\rho)=P_0\rho P_0+P_1\rho P_1\). The product equals \(\rho\). The largest absolute entry of \(\Phi(\rho)-\rho\) is \(0\). Von Neumann entropy is unchanged, so

\[
P_D=S(\Phi(\rho))-S(\rho)=0.
\]

One state, so \(I(W;M)=0\). The outcome probabilities are \(\operatorname{tr}(P_k\rho)\) and do not depend on \(q\). Any loss of those outcomes is the same at \(q=0\) and at \(q=1\). With \(\kappa=1\), the cost gap is \(P_D\). Both numbers are \(0\), and the lock fails the line when either is \(\le 0.01\). The score is `Q-coh FAIL PD=0.000000 cost_gap=0.000000`. Q-reuse stays the other miss, so the run is `FAILS 2`.

The same projectors do move a state that is coherent across the cut. On \((|0\rangle+|1\rangle)/\sqrt{2}\) the largest absolute entry of \(\Phi(\rho)-\rho\) is \(0.5\). The locked state is fixed because its coherence sits inside \(P_1\).

The script's `qutrit_coherent` returns the constant `0.0` after checking that its block copy equals \(\rho\). That copy is the Lüders image for this matrix. The live stdout is

```
Q-comm PASS frobenius=0.176776695297
Q-slope PASS min_PD=0.025450 max_PD=0.025714
Q-pointer PASS PD0=0.025450 PDpi2=0.025450
Q-garble PASS min_gap=0.150000
Q-state PASS trace_distance=0.300000
Q-reuse FAIL I_cond=0.017070 PD_total=0.084896 gap1=0.084896 gap2=0.169791
Q-rank PASS PD=0.000e+00 I=0.000e+00 ledger_gap=0.346573590280 half_ln2=0.346573590280
Q-coh FAIL PD=0.000000 cost_gap=0.000000
FAILS 2
```

Those nine lines are the non-comment lines of the appendix in `quantum_record_checks.out`. The test `test_quantum_record_checks_match_rescore_stdout` byte-compares the script to that appendix.

The stored pass is a different map. At `00e8dfa`, `qutrit_coherent` returns \(S(1/2,1/4,1/4)-S(1/2,3/8,1/8)\). The block eigenvalues are \(1/4\pm 1/8\), so the coherent spectrum is \((1/2,3/8,1/8)\). The difference is `0.06540601797056844`, which prints `0.065406`. That is the gap from this state to \(\mathrm{diag}(1/2,1/4,1/4)\).

## Locks

| Lock | Commit | sha256 | Blob at the lock and at this head |
|---|---|---|---|
| `PREREG.md` | `8563c91` | `8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8` | `01e6a499aa466bde0f8e9a82fa04e00d0a323de5`, same |
| `PREREG_FIXED_POINTS.md` | `c864603` | `82d58bdcefca97218ac4b7587a9246850994eedac1c6c372de8f50a75417017b` | `bcd4121ac432a49adeb50b3dd065c43614b3fc6e`, same |
| `PREREG_MHD.md` | `4ca0322` | `faf04d3d53de980141cbfd57a3dfb30f34af6e6f8d7efb5ce72f5a01e3dc25b6` | `87db4b1c9ba8459ce6d3c6139ce29a8cf10b30d8`, same |
| `PREREG_REPEAT_ASYMPTOTE.md` | `e0b411a` | `5b0846fa823e86d63c71133831ec966ac42f3f3a27f1cff9ec613c392adfa60a` | `8df0fcc1e56df405a222fadb767050a5e4dcb75e`, same |
| `PREREG_QUANTUM.md` | `dba140b` | `1ac92e314705b3378e3b6a1bd665d36ec6dc9f7f812760a20bc4556617b817d3` | `10c83a275222984fe456bc0daf89fcccaa3f7948`, same |

Each sidecar's first token is that sha256, and each sidecar blob equals the blob at its lock commit. `git diff` from each lock commit to this head is empty on that file and its sidecar. `00e8dfa` is an ancestor of this head. `dba140b` is the parent of the first quantum-record result.

## Run log

`quantum_record_checks.out` at `00e8dfa` is 404 bytes, sha256 `fabfb73c51eb76de7b4aa22806e823726a5a0891a1eb38d5379de55e980b6dfb`. The current file starts with those bytes. The nine lines are `Q-comm` through `Q-coh PASS PD=0.065406 cost_gap=0.065406` and `FAILS 1`.

`9284624` is the child of `d117ca6`. Its `quantum_record_checks.out` is also 404 bytes, contains no `Q-coh PASS`, and ends `Q-coh FAIL PD=0.000000 cost_gap=0.000000` / `FAILS 2`. The other seven check lines were already the `00e8dfa` lines. That commit replaced the Q-coh line and the count.

`40c4060` is the child of `9284624`. The diff puts `Q-coh PASS` and `FAILS 1` back after `Q-rank`, then a blank line, then the dated note of 24 November 2026 (America/New_York), then the re-score. The re-score's last two lines are the `9284624` lines. D4's paragraph is unchanged between those two commits. D5 is the only addition to `DEVIATIONS.md`.

`DEVIATIONS.md` at `00e8dfa` is a byte prefix of the current file. D1, D2, and D3 are that prefix. D4 still records that `9284624` replaced the run log, and D5 records that the original nine lines are restored and the re-score is appended.

## Medium items from the prior review

**Fifth lock in the index.** `theory/README.md:51` names `PREREG_QUANTUM.md`, states `FAILS 2`, and says the coherent block is fixed by the projectors so the line does not select ratio 0.

**Entropy increase and the Umegaki divergence.** The memo at line 87, the same README sentence, and the T76 row state that this menu's \(P_D\) is \(\mathbb{E}[S(\Phi(\rho))-S(\rho)]\). An independent Bloch calculation on the 721 angles and the four antipodal states gives a largest absolute gap of `0.04628655193940512`, at \(\theta=0\) on the \(+x\) state. The entropy increase there is `0.05089915429094205`. The divergence is `0.004612602351536932`. The printed `0.050899`, `0.004613`, and `0.046287` are those values. The ensemble entropy increase on that grid stays between `0.025450` and `0.025714`. Both functionals are nonnegative on the grid. The gap is larger than the ensemble value at the pointer.

**Sequential remeasurement.** The answer bullet at memo line 11 says the fixed-point claim is the projective menu, and that the unsharp pair is a different composition whose cost at \(q=1\) exceeds the cost at \(q=0\) by `0.084896`. That figure is the stored `gap1` on the Q-reuse line. `sequential` is unchanged since `00e8dfa`.

## Claims

The memo's answer bullet and the Q-coh paragraph call the coherent block a miss, with \(P_D=0\) and equal costs at \(q=0\) and \(q=1\). The model implication says the rank-2 projectors, on the diagonal state and on the coherent state, do not select the ratio. The README row says the run is `FAILS 2`. The tests require the restored `Q-coh PASS` prefix, the appended `Q-coh FAIL PD=0.000000 cost_gap=0.000000`, and an appendix that ends `FAILS 2`. The script prints `FAIL`.

`Q-coh PASS` occurs in the restored prefix (`quantum_record_checks.out:8`), in the test that locks that prefix (`tools/test_quantum_record_checks.py:55`), and in D4 and D5, which quote the original line. `Q-coh matches` does not occur. The sentence that the coherent state has \(P_D=0.065406\) and selects ratio 0 is gone from the memo and from the T76 row.

The prior review's low items in the prose are addressed where a lock did not freeze them. The T75 memo cites Debreu at `theory/REPRESENTATION.md:108`, which is the contour-set sentence. The Davidson dates in the T76 memo name 9 February 2017 online and 22 December 2016 in print. The repeated H2 sentence is gone. The large-\(n\) paragraph says the shared objects are the ceiling \(I_\infty=\tfrac32\ln 2\) and \(L_\infty=0\), and that the outcome probabilities still depend on \(\theta\). The post-hoc endpoint \(w=1.60\) is described as a tie. `unsharp x law` is gone from the T76 row, and `outcome law` is gone from the memo's quantum paragraph. `PREREG_QUANTUM.md:53` still says `outcome law`. That file is the lock.

## Wording

Scanned the memo, `theory/README.md`, `OPEN_WORK.md`, `DEVIATIONS.md`, the quantum script, the quantum stdout, the T75 memo, and the quantum test.

- No phrase `theory of everything` in those files.
- `solved` occurs in the locks' refusal sentences (`PREREG.md:129`, `PREREG_FIXED_POINTS.md:148`, `PREREG_MHD.md:65`, `PREREG_REPEAT_ASYMPTOTE.md:69`, `PREREG_QUANTUM.md:73`). The memo, the deviations, and the script have none.
- No `bill` in the errata surfaces. The script no longer contains `kill`. The comment `Φ kills the coherence` was removed with the dephasing return.
- `law` in `theory/README.md` is on older rows (area law, power law, and the learning-rate row). The T76 sentence has none. `OPEN_WORK.md` hits are other rows. The T76 row has none. The maintained-doc checker reports wording FAILs 0.
- The sentences that mention general relativity, quantum mechanics, or holography say that nothing here derives them.

## Attacks tried

- Multiplied the locked projectors into the coherent block and into a state coherent across the cut.
- Computed \(S(1/2,1/4,1/4)-S(1/2,3/8,1/8)\) and compared it with the `00e8dfa` return `s_phi - s_rho`.
- Compared D4's subtraction sentence with that return.
- Hashed each preregistration and each sidecar at its lock commit and at this head.
- Compared the `00e8dfa` stdout, byte for byte, with the prefix of the current stdout file, and read the `9284624` file for the absence of `Q-coh PASS`.
- Diffed `9284624` against `40c4060` on the run log and on `DEVIATIONS.md`.
- Recomputed the unsharp commutator norm \(\eta^2/\sqrt{2}\), the garble gap \(0.15\), the \(+x\) trace distance \(0.5\times 0.6\), and the entropy-increase versus Umegaki gap on all 721 angles and all four states.
- Ran the live script and compared its stdout with the appendix.
- Grepped the errata surfaces for `Q-coh PASS`, `Q-coh matches`, `0.065406 and selects`, and the banned tokens above.
- Confirmed `import numba` fails, and left `run_test.py` un-run.
- Ran the three checkers and the ignored pytest suite.

## Findings

### BLOCKING

None.

### HIGH

None.

### MEDIUM

None.

### LOW

**L1. D4 states the old subtraction in the reverse order.** The code at `00e8dfa` returns \(S(1/2,1/4,1/4)-S(1/2,3/8,1/8)=+0.06540601797\). D4 says the run subtracted the entropy of \((1/2,1/4,1/4)\) from the entropy of \((1/2,3/8,1/8)\), which is the negative of that difference. The next sentence identifies the printed `0.065406` as the gap to the dephased diagonal, and the re-score itself is \(P_D=0\). D4 was left byte-intact, which is what D5 says. The operand order is the slip.

**L2. The T76 row still opens the fifth lock with `FAILS 1`.** `OPEN_WORK.md` gives the fifth lock the same shape as the fourth lock's `FAILS 2`, then says the corrected run is `FAILS 2`, that the projectors fix the coherent state, and that \(P_D=0\). The memo, the README row, the tests, and the appended stdout use `FAILS 2`. The lead token is the original count.

Blockers remaining: 0
