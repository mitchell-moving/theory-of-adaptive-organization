# Independent review

Head `9af966c3fbea33f15608ec04931ce0ef3160f9b0` (`mitchell-moving:forge-composite-contest`).
Commits under review: `ecf45b27acf9bba3b8e91562ae8035868dd703cb` (parent `b2ff239dc2b4dbac169c3d99fad65051dcb14ee8`) and `9af966c3fbea33f15608ec04931ce0ef3160f9b0`.
Contest PR base `04e9e5baef53ed1793116ea8e85468571ea08da5`.
Upstream `main` fetched at `835ea7c082928be081a3ef1ba2c60eaa1fc3a742`. Process text read at `652d936f3f6c9a97a0cfec60fb99a209db0f015b`, which is on that `main`.
Scope: those two commits, the preregistrations on the branch, the scored menu3 output, and the checks named below. Working notes and chat context were not used. This review does not rewrite `forge-composite-contest`.

Ace's comment on the upstream PR (issuecomment-7140067721) asks for coverage of `ecf45b2` before a normal merge commit, and leaves LOW 3 and LOW 7 as notes. `9af966c` is the further commit on the same tip: D12 at `theory/menu3_checks/DEVIATIONS.md:16`, ledger row at line 20.

## Checks

| Command | Result |
|---|---|
| `python3 tools/check_consistency.py` | exit 1. `FAIL: 1`. `INFO` 30. `RESULT: FAIL`. The one fail is freshness (below). Wording FAILs 0 on 31 maintained docs. Frozen records scanned 518. Section N: 68 rows, 0 mismatches. Process-rule FAILs 0. Core-rule FAILs 0. Advisory length warnings on `THEORY.md` (11325 words) and `README.md` (1857 words). |
| `python3 tools/check_fresh.py` | exit 1. `RESULT: FAIL`. Pointer `3418781`. The printed window is fork `origin/main` `d2aeb81`. The function also loaded `upstream/main` `835ea7c`, and that window excludes the pointer too. Detail under check 8. |
| `python3 tools/check_open_work.py` | exit 0. `RESULT: PASS`. `items.json` not-DONE 62. `QUEUE.md` not-DONE 90. Union missing from `OPEN_WORK.md`: 0. |
| `python3 -m pytest -q --continue-on-collection-errors` | exit 1. **294 passed, 1 failed, 1 skipped, 1 error**, 684.75 s. Failure: `tools/test_check_fresh.py::test_real_repo_status_is_in_window_after_fix` (same freshness miss). Skip: `tools/test_lean.py:124` (Lean 4 / lake is not installed). Collection error: `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py` imports `numba`, which is not installed. That file is a locked module-level script. It was not executed. |

NumPy 2.5.5, SciPy 1.18.1, pytest 9.2.0. The headline expression was evaluated in a separate four-row table. The contest modules were not imported for that table.

### 1. Preregistrations since their lock commits

Each contest preregistration's sha256 at the head equals its sha256 at the commit that introduced it. `f774ca3509f6` renames the first four with similarity 100. No later commit changes those blobs. `9af966c` and `ecf45b2` do not touch them.

| File | Lock commit | sha256 (lock and head) |
|---|---|---|
| `theory/composite-contest-2026-11-24/PREREG.md` | `e271ea971a10fbff4d58484cd2942c98dca12518` | `499c430f2ef89e17ecd9397e785cbfaa4e65c0148222a6ff19c8a3f781c537eb` |
| `PREREG_R2.md` | `18a36c0ee9610fb8ef8fef20e07b7c83ab0c2656` | `6b4c611eb7c8e423361432b9b770242b8f35429008f586fd5c521446d1db1451` |
| `PREREG_2.md` | `e1d8af844d766d11bac37a38734bd031f2996d5b` | `879bcc1211013f29bf1a43bb23858086d24401283bea9dd02a601b4e575911c9` |
| `PREREG_3.md` | `f8af0787beaa6c6ad284b04ca897e559d8bfbf36` | `0cc68fd18c1698b5cd2817805d7bb4218b3f191360626bafa5846cf8aa5758ba` |
| `PREREG_4.md` | `82a803dd5fc266c8778dfb80f35cbd1fe7c294d6` | `98d52daee6c3382aeb609c0b7f9e9e9f971c21a1512ada13237b6c3c5d94092b` |

There is no `PREREG.sha256` sidecar beside these five files. The lock witness is the git blob. The output sidecars do match the files they name:

- `theory/menu3_checks/SHA256SUMS`: `decisions.out` `a22aa42540ea1d9680f5745345a433f9345575fb6d2afa2e1269b17330448af8`
- `theory/composite_contest_checks/SHA256SUMS`: `lemmas.out`, `envelope.txt`, `decisions.out`, `control.out`, `crossref.out` all match
- `theory/pivot_worst_checks/SHA256SUMS`: `decisions.out` matches

### 2. Append-only across `ecf45b2` and `9af966c`

Diffed each commit against its parent. For every run log, deviations file, and preregistration, the parent text is a byte prefix of the child, or the file is absent from the diff.

| Commit | Log / prereg file | Parent lines | Child lines | Prefix |
|---|---|---|---|---|
| `ecf45b2` | `theory/menu3_checks/RUN_LOG.md` | 19 | 21 | yes |
| `ecf45b2` | `theory/menu3_checks/DEVIATIONS.md` | 14 | 15 | yes |
| `9af966c` | `theory/menu3_checks/DEVIATIONS.md` | 15 | 20 | yes |

No preregistration path is in either diff. `theory/composite_contest_checks/DEVIATIONS.md` and `theory/pivot_worst_checks/` are unchanged across both commits.

`c59741862619`'s `RUN_LOG.md` is 1400 bytes and is a byte prefix of the file at `4514d39c8f96`, at `ecf45b2`, and at `9af966c`. Line 17 at the head is the `c597418` sentence, including "the 25 product-effect probabilities of the singlet." `c539110acd8a2868aa3b1ab5f19e6f2d7865b012` is still an ancestor. At that commit, line 17 says "the 100 signed menu effects of the singlet." The disclosure appended at `RUN_LOG.md:21` and `DEVIATIONS.md:15` names both clauses and both commits. That account matches the blobs.

The one rewritten line in these two commits is `OPEN_WORK.md` T45. `ecf45b2` restores it. The restored line is byte-identical to T45 at `04e9e5b` and at `upstream/main` `835ea7c`. It is a task-ledger row, and it cites `PREREG.md` and commit `40232f6` again.

### 3. Scored run and the unfired arm

`theory/menu3_checks/decisions.out` sha256 is `a22aa42540ea1d9680f5745345a433f9345575fb6d2afa2e1269b17330448af8`, the same digest as `theory/menu3_checks/SHA256SUMS` and the digest written on the D12 ledger row.

| Line | Text |
|---|---|
| 61 | `P-win FAIL` |
| 65 | `P-gmax PASS min_prob -8.3266726846886728e-17 loss 0.0000000000000000e+00` |
| 105 | `headline Model implication conditional_on Hardy_ln_K_AB TIE ...` |

The file contains no `P-gmax FAIL` line and no headline line that ends in WIN. `run_menu3.py` blob `263889c7cdb9d0daf50b8988f2a5b17ccc1f8d8c` is the same at `71a4e3042580` (the commit that wrote this `decisions.out`) and at `9af966c`. Line 416 is the line that scored this file:

```python
headline = "TIE" if (p_gmax and not p_win) else ("WIN" if p_win else "RE-READ")
```

`P-gmax PASS` and `P-win FAIL` make the first clause true, so the stored headline is TIE. The WIN arm and the RE-READ arm did not run.

`PREREG_4.md:38` is one paragraph: if P-gmax holds, the positive-price cell is not WIN; if P-gmax fails, that headline is withdrawn and the cell is re-read. Evaluating the expression:

| P-gmax | P-win | Code prints | Locked paragraph |
|---|---|---|---|
| holds | fails | TIE | "not WIN". This is the scored run. |
| holds | holds | WIN | "not WIN". The WIN token contradicts that sentence. This input did not occur. |
| fails | holds | WIN | re-read. The WIN token contradicts that sentence. This is the input D12 names. It did not occur. |
| fails | fails | RE-READ | re-read. This input did not occur. |

D12's sentence that the arm prints WIN when P-gmax fails and P-win holds is true of that input. The same else-arm also prints WIN when both hold. Both of those inputs are outside the scored file.

### 4. D12 location under `process/PROCESS.md` at `652d936`

Item 6 of that file, the guardrail:

> for a locked scientific test, attributing a miss to `measurement/code` or `process` is admissible only when a pre-declared validity gate (`MV1`–`MV8`) or reproducible bug actually fired (`measurement/FRAMEWORK.md:89`), never as a post-hoc rescue.

`measurement/FRAMEWORK.md:89` at the same commit: a later claim that the instrument missed is inadmissible unless it names a gate the test actually failed. The diff of `process/PROCESS.md` from `652d936` to `upstream/main` `835ea7c` adds a vocabulary sentence in section 2. Item 6 is unchanged.

Decision: a code path that contradicts locked prereg text counts as that reproducible bug when the path has executed and the stored output shows the contradicting label. An unexecuted branch that a reader can see in the source has not fired.

D12 puts location `measurement/code` on a row whose outcome is "Not triggered" and whose miss is "signed size 0; not triggered." The justification in the cell is "Reproducible: the code path is verifiable by reading `run_menu3.py:416`." Reading the source is not a run of the WIN arm. The scored file shows P-gmax PASS, P-win FAIL, and headline TIE. The row names no MV1–MV8 gate. The location is not admissible.

The row leaves the scored headline as TIE, says the prereg text governs, and sets the update to `none yet`. That is consistent with the scored arm. It does not supply the fired gate or the fired bug the guardrail requires before this location is used.

### 5. Eight-field ledger rows

`process/MISS_LOG_TEMPLATE.md` at `652d936` asks for eight fields: `prediction_id`, `locked_prediction`, `outcome`, `miss`, `location`, `stake_x_info`, `update`, `breach_check`.

The new table's header matches that list. The data row at `DEVIATIONS.md:20` splits into eight cells:

1. `` `PREREG_4:38` ``
2. The re-read sentence, with "Odds not stated."
3. Not triggered, plus the sha256 and the three output lines.
4. `signed size 0; not triggered`
5. `` `measurement/code` `` plus the reading claim.
6. `` `low` ``
7. `none yet; the prereg text governs`
8. `none`

`stake_x_info` is `low`, so the template stops at the row and asks for no scaled write-up. Field count and order match. The location value is the defect in check 4. `breach_check` `none` matches the prereg blobs: `PREREG_4.md` is unchanged since `82a803d`.

D11 at line 15 is the prose disclosure of the reachable run-log edit. It is not a prediction-outcome row. The eight-field requirement checked here is the new ledger row.

### 6. Wording

Search terms on lines added by `ecf45b2` and `9af966c`: `puzzle`, `kill`, `failure`, `verdict`, `bill`, `solved`, `theory of everything`.

The errata paragraph in `theory/COMPOSITE_CONTEST_2026-11-24.md`, D11, the new `RUN_LOG.md` paragraph, the test comment in `tools/test_composite_contest_checks.py`, and all of D12 are free of those strings. The assertion that still requires `P1 PASS` is the pre-existing line. The comment above it points at the errata.

The one added line the search marked is the restored T45 row in `OPEN_WORK.md`. That line is byte-identical to current `upstream/main`, and the row it replaced already carried the same outcome-label word. `check_consistency.py` on this tree reports 0 wording FAILs.

`THEORY.md` and `CORE.md` are untouched, so the hypothesis sentence in those files is the upstream sentence.

### 7. `THEORY.md` and `CORE.md`

Blob ids at `9af966c`, at PR base `04e9e5b`, at `652d936`, and at `upstream/main` `835ea7c`:

- `THEORY.md` `6caadae569116a94a74563398be94cebf6e99e9b`
- `CORE.md` `dbf0d2322ce9fe751a5359e85859ca6f9448ec66`

`git diff` of those two paths against each of those commits is empty.

### 8. Freshness against fork `main` and against upstream `main`

`STATUS.md` on this branch says `` `main` is `3418781` `` (`3418781592aa4e7042ef984e0f4910914e39a493`). `tools/check_fresh.py` passes when that commit sits in the last 5 first-parent commits of `origin/main` or of `upstream/main`. On this clone both refs were present.

| Tip | Role | Last 5 first-parent | Pointer inside? |
|---|---|---|---|
| `04e9e5b` | contest PR base | `04e9e5b 0e22302 3418781 26e1490 28db5ce` | yes (3rd) |
| `d2aeb81` | fork `origin/main` | `d2aeb81 31aa997 8c48a5b 04e9e5b 0e22302` | no (6th) |
| `652d936` | process commit on upstream | `652d936 d2aeb81 31aa997 8c48a5b 04e9e5b` | no (7th) |
| `835ea7c` | fetched `upstream/main` | `835ea7c 652d936 d2aeb81 31aa997 8c48a5b` | no (8th) |

`check_fresh.history_tips` returned `d2aeb81` and `835ea7c`. `check()` is empty only if either window contains the pointer. Both exclude it, so `check()` returns the freshness string. The printed sentence names only the first tip, which is why the tool output looks like a fork-only miss. Evaluated against fetched upstream `main`, the check still exits 1. It passes when the tip under test is the PR base `04e9e5b`.

`ecf45b2` and `9af966c` do not edit `STATUS.md`. The pointer was inside the window of the main this branch merged (`04e9e5b`). It has since fallen out of fork `main` and out of upstream `main`.

### 9. DOIs

Lines added by `ecf45b2` and by `9af966c` contain no DOI (`10.` / registrant pattern). No Crossref query. The fifteen works in `PREREG.md:215-229` are outside these two diffs. The prior independent review (issuecomment-7139642485) already queried them.

## Attacks tried

1. **Four corners of line 416.** The expression was evaluated for every pair of booleans. The scored pair (P-gmax holds, P-win fails) prints TIE, matching `decisions.out:105`. The two pairs that print WIN each contradict one sentence of `PREREG_4.md:38`. Neither pair is the scored file: there is no `P-gmax FAIL` line, and line 61 is `P-win FAIL`. Forcing the booleans in the expression does not move the stored headline.

2. **Sidecar recomputation.** sha256 of `theory/menu3_checks/decisions.out` and of every file named by the three `SHA256SUMS` sidecars was recomputed from the blobs at `9af966c`. Each digest matches its sidecar line. A byte-level change in the scored file would have broken `a22aa425…`. It matches, and the headline line is TIE.

3. **Prefix attack on the two commits.** Every pre-existing line of `RUN_LOG.md` and of `theory/menu3_checks/DEVIATIONS.md` is still present, in order, after `ecf45b2` and after `9af966c`. The `c597418` run log is a 1400-byte prefix of the head. The five preregistration sha256 values at the head equal the lock-commit values. The reachable rewrite remains at `c539110`, and the appended disclosure names it.

4. **Freshness tips.** The same pointer was tested against four tips. It sits in the window of `04e9e5b` and outside the windows of fork `d2aeb81`, of `652d936`, and of upstream `835ea7c`. Calling `check()` with both remotes present returns the freshness string. The upstream window does not clear it.

## Findings

### BLOCKING

1. **D12's location `measurement/code` is not admissible.** `process/PROCESS.md` item 6 at `652d936` allows that location only when an MV1–MV8 gate or a reproducible bug actually fired. A code path that contradicts `PREREG_4.md:38` counts only once that path has run and the stored label is the contradicting one. The scored run took the TIE arm (`decisions.out:61`, `:65`, `:105`). The WIN arm at `run_menu3.py:416` did not run. The row's "verifiable by reading" clause does not meet the guardrail. The eight cells are present; the location cell is the one to correct, by an append, before this row is the ledger entry on main. The prereg bytes stay as locked.

2. **`check_consistency.py` and `test_real_repo_status_is_in_window_after_fix` exit 1 against fetched upstream `main`.** `STATUS.md` points at `3418781`. That commit is inside the last 5 first-parent commits of the PR base `04e9e5b`. It is the 6th first-parent of fork `origin/main` `d2aeb81` and the 8th of upstream `main` `835ea7c`. `check_fresh.py` loaded both remotes and failed. The tool's one-line message names only `d2aeb81`. The upstream window was checked and also excludes the pointer. `652d936`, read as a tip, excludes it as well. These two commits did not edit `STATUS.md`. A merge onto current upstream `main` still carries a pointer outside the window the checker enforces.

### HIGH

None.

### MEDIUM

None.

### LOW

3. **`PREREG.md:15` says "readout law"** for the one-system generator. The phrase sits outside the hypothesis sentence. The file's sha256 is the lock digest above. Left as a note, as Ace asked.

7. **`tools/check_fresh.py` still treats `origin/main` and `upstream/main` as alternative windows of width 5.** That design is unchanged. Left as a note. The current pointer is outside both windows; that gate result is blocking item 2, and it is separate from the design note.

## What holds

- `ecf45b2` discloses the reachable `RUN_LOG` rewrite by appending `RUN_LOG.md:21` and `DEVIATIONS.md:15`. The `c597418` text is the prefix. `c539110` stays in the history. A normal merge commit keeps that pair. This review did not rewrite history.
- The T45 row matches `04e9e5b` and current `upstream/main`.
- The five preregistrations are byte-identical to their lock commits.
- The scored menu3 run is P-gmax PASS, P-win FAIL, headline TIE. The WIN arm did not fire. `decisions.out` matches its sidecar.
- `THEORY.md` and `CORE.md` match upstream `main`.

Blockers remaining: 2
