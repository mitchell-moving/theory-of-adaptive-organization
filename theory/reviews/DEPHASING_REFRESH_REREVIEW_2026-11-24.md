# Independent re-review 7cba6b6eee654d1e7702bda77c992e99d829c253

*Reviewer: independent. I did not write the preregistrations, the memo, or the scored scripts. Tuesday 24 November 2026. Fork PR #26, pinned head `7cba6b6eee654d1e7702bda77c992e99d829c253`, branch `forge-dephasing-refresh`, base `forge-dephasing-crossover` `853e5a2f76a269df048854f8a593921eca3011ab`. This re-review does not edit that branch, `THEORY.md`, or `CORE.md`. The write-up is `theory/reviews/DEPHASING_REFRESH_REREVIEW_2026-11-24.md` on `cursor/dephasing-refresh-rereview-946a`. Prior review: comment `7145474164`, write-up on fork PR #28, head `067c485dd86517f7ffaad01486cbd696f690842b`.*

**Result label: observed in-model. Consistency check.** This re-review does not clear it. The arithmetic of the new onset bars matches an independent float64 evaluation. Those bars are identities of the formulas in `ONSET_PREREG.md`. The label `CONSISTENCY_CHECK` on `cc4d406`, and the third ledger's `NOT A TEST` rows, match that arithmetic. They do not add a bar that can land off those formulas.

The locks contain the hypothesis sentence of `CORE.md:7`: "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment."

## 1. Lock order, hash, required lines, circularity

| Lock | Commit | Author date | sha256 of the file | Scoring script |
|---|---|---|---|---|
| Parent rate | `612b82e` | `2026-11-24T21:11:32Z` | `b2e96d76234da1e4a2521b990bb9cf456ca1c9c60a334ebf475f49b159dcab8f` | absent; born in `9c1b0f3` |
| Clock addendum | `9619565` | `2026-11-24T21:19:52Z` | `62871c9de3ad1d29046d2f73162139b5f0ae4d897a3204ca05859f3a9c5e63b2` | absent; born in `9c1b0f3` |
| Review fold-in | `6fb397b` | `2026-11-24T21:27:21Z` | `fc82c94bcf0ff3e639d6512475d8060228164b27c0a8f973dc4adc0b1f371dfd` | absent; born in `9c1b0f3` |
| Onset map | `a27520c` | `2026-11-24T21:42:18Z` | `659ed3e67e40bc03aef71bb69c694eb91e3ee0049a7e907570945d9fd42760fb` | absent; born in `9930259` |
| Consistency label | `cc4d406` | `2026-11-24T21:53:27Z` | `347cca6bc1d940decc404963993edde2dc8e4fe0901ad76d045d0c3d9ad1b18f` | none; the lock says there is no script |

Each sha256 is the hash of the blob at the lock commit and again at `7cba6b6`. Author date equals committer date on each of these commits. `a27520c` adds only `ONSET_PREREG.md` and a run log that says no cell has been scored. `9930259` adds the onset script and the stored stdout. `cc4d406` adds only the consistency lock and its run log. `7cba6b6` appends the reclassification and does not add a script. `THEORY.md` and `CORE.md` are absent from `853e5a2..7cba6b6`.

`ONSET_PREREG.md` and `CONSISTENCY_PREREG.md` each contain a `Why this approach` heading, a `Can it fail` line, and a `Cheapest way` line.

The onset bars cannot land off the formulas in that same file.

- **M1** is the integer match. \(c^*=2\kappa kT\,b/a\). At \(a=1\), \(b=2\), \(\kappa=kT=1\), that is 4. \(\Pi_c(0.01)=4.026744563040\), residual \(+0.026744563040\) from 4, inside the band 0.05. The first term of the parent series is \((8/3)\times 0.01=0.0266\ldots\), so the band is wider than the term the series already fixes. M1 holds while the parent formula stands.
- **M2** is the stake derivative of \(A_c=w\gamma T^2/\Pi_c(\gamma T)\). \(\Pi_c\) has no \(w\), so \(A_c\propto w\) and the elasticity is 1. A centered difference in float64 returns \(0.9999999999951152\), which prints as \(+1.00000000\). The distance from the identity 1 is \(4.885\times 10^{-12}\). The locked band is \(|e_A-0|\le 0.05\). The miss from 0 is \(+1\). The prereg already states the reason: \(\Pi_c\) carries no \(w\). The bar cannot pass while that definition stands.
- **M3** compares two limits the lock names. The uniform-age slope of the locked Hamming average is \(1/4\). The Poisson-age coefficient, with the factor \(f/\gamma\) written in the lock, is \(\lim f/(2(f+\gamma))=1/2\). The script's trapezoid and Richardson step return \(0.249999999979\) and \(0.499999998333\). The uniform slope is inside \(10^{-9}\) of \(1/4\) (residual \(-2.057\times 10^{-11}\)). The exponential slope misses \(1/4\) by \(+0.249999998333\) on that grid, and by \(+1/4\) in the limit. The logged gap \(+0.2499999984\) is \(\alpha_E-\alpha_U\) printed to ten digits (\(0.249999998353\)). Neither integral can move.
- **M4** sets \(\beta=1/8\) and scores \(1/\beta\). That is 8, residual \(+4\) from 4. \(c^*=4\) stays put because \((a,b)\) stays \((1,2)\). The cheapest-way line is this substitution. The bar \(|8-4|\le 0.05\) cannot pass.

The named rival, a shared integer 4, is the reading the algebra leaves. Prior odds 4:1 for that rival are written in the lock, and the outcome is fixed by the same lock, so the odds do not measure a risk. Information is about 0 (`process/PROCESS.md` item 5 on upstream `652d936`). Headline `MISS_COINCIDENCE` is the label of that identity. `cc4d406` states the same fact and labels `CONSISTENCY_CHECK`.

## 2. Float64 recomputation

Independent script: `theory/reviews/dephasing_refresh_rereview_checks/recompute.py`. It does not import the scoring scripts. Signed size is the independent value minus the locked point. The stored stdout of all four scoring scripts matches a fresh run.

| Printed quantity | Independent float64 | Stored print | Signed residual of the print |
|---|---|---|---|
| \(\Pi_c(0.01)\) | \(4.026744563040\) | \(4.02674456\) | \(+3.0\times 10^{-9}\) |
| series gap | \(1.18595193\times 10^{-7}\) | \(1.186\times 10^{-7}\) | \(-4.8\times 10^{-12}\) |
| M1 from 4 | \(+0.026744563040\) | \(+2.67445630\times 10^{-2}\) | inside the last printed digit |
| \(e_A\) | \(0.9999999999951152\) | \(+1.00000000\) | print of the identity \(+1\) |
| \(\alpha_U\), \(\alpha_E\) | \(0.249999999979\), \(0.499999998333\) | \(0.2500000000\), \(0.4999999983\) | ten-digit print |
| gap \(\alpha_E-\alpha_U\) | \(+0.249999998353\) | \(+0.2499999984\) | \(+4.7\times 10^{-11}\) |
| M4 | \(8\), residual \(+4\) | \(8.00000000\), \(+4.00000000\) | \(0\) |
| short-period ratios | \(1.0033375009\), \(0.9983374940\) | \(1.003338\), \(0.998337\) | residuals from 1: \(+0.0033375009\), \(-0.0016625060\) |
| elasticities | \(0.5008333319\), \(0.5414940825\), \(0.5819767069\) | \(0.50083\), \(0.54149\), \(0.58198\) | last printed digit |
| accounting C | \(16.00160008884\), \(16.1608927558\) | \(16.001600\), \(16.160893\) | \(+8.9\times 10^{-8}\), \(-2.4\times 10^{-7}\) |
| R0 derivative gap | \(1.550429\times 10^{-11}\) | \(1.550\times 10^{-11}\) | inside \(10^{-9}\) by \(9.845\times 10^{-10}\) |
| R6 monomial share gap | \(5.551115\times 10^{-17}\) | \(5.551\times 10^{-17}\) | float noise of the identity \(1/3\) |
| doubled \(\Pi_c\) | \(8.05348912608\), gap \(2.371904\times 10^{-7}\) | \(8.05348913\), \(2.372\times 10^{-7}\) | last printed digit |
| \(\ln 2\), gap to 4 | \(0.693147180559945\), \(3.306852819440055\) | \(0.693147180560\), \(3.306853\) | \(-4.5\times 10^{-14}\), \(-1.8\times 10^{-7}\) |
| \(t(0.01)\), \(t(1)\), \(\Pi_c(1)\) | \(6.3008215228\), \(1.9738768354\), \(7.5688447647\) | \(6.300822\), \(1.973877\), \(7.568845\) | last printed digit |
| printed-cell elasticity | \(0.901222193631\) | \(0.901222\) | \(+1.9\times 10^{-7}\) |
| squared-Hamming \(\Pi\) | \(600\) | \(600.0\) | \(0\) |
| five one-shot cells | \(0.9399243436\), \(0.1930853882\), \(0.2690713169\), \(1.2394716336\), \(3.4365636569\) | \(0.939924\), \(0.193085\), \(0.269071\), \(1.239472\), \(3.436564\) | last printed digit |
| Gaussian envelope, \(s=20\) | \(0.35480226\) | ledger \(0.354802\) | \(+0.02146893\) from \(1/3\), prints \(+0.021469\) |
| same envelope, \(s=10^4\) | \(0.33363267\) | prior review \(0.333633\) | \(+0.00029933\) from \(1/3\) |

The parent identities that the third ledger marks `NOT A TEST` reproduce as algebra. Accountings A and B differ by the constant \(-A/T\), so the agreement \(1.137\times 10^{-13}\) is float noise of one expression. The monomial share is \(1/3\) for every stake once \(u^3=3/s\). The squared-Hamming critical value is \(6/0.01=600\). The clock-onset arithmetic in R8 is \(2\cdot b/a=4\). The holding-floor gap is \(4-\ln 2\).

## 3. Ledger rows and locations

`DEVIATIONS.md` at `7cba6b6` has 65 data rows. Each row has the eight fields `prediction_id`, `locked_prediction`, `outcome`, `miss`, `location`, `stake_x_info`, `update`, `breach_check`. The file at `b0a2eb4` is a prefix of the file at `9930259`, and that file is a prefix of the file at `7cba6b6`. The onset and consistency run logs grow by an appended section. The five preregistration files are unchanged after their lock commits.

M2, M3, and M4 are located `model`. That location fits: the formulas differ, and no measurement gate fired. The second block records the signed misses \(+1\), \(+0.2499999984\), and \(+4\). The third block keeps those magnitudes and labels the rows `NOT A TEST`, with information about 0. Both blocks stand. The third block is the operative gate.

The GAUSS row is the exception. It locates the envelope gap at `measurement/code`. No `MV1`–`MV8` gate is named. The locked bar R6 is the short-time monomial, and the script's gap on that monomial is \(5.551\times 10^{-17}\). The script implements that bar. The envelope at \(s=20\) is a different loss, \(+0.021469\) from \(1/3\). The admissible location for that gap is `model`.

`ACE-16` and `CLOCK-FLOOR` in the second block are differences from candidates the locks did not state as the prediction. The symmetric threshold's locked reading is 4, and the holding floor's locked bars are the separation from 4 and from 0. The differences \(4-16=-12\) and \(\ln 2-4=-3.306853\) match the arithmetic. The third block relabels the separation bars `NOT A TEST` and leaves the earlier rows in place.

## 4. Append-only

`PREREG.md`, `ADDENDUM_PREREG.md`, `ADDENDUM_REVIEW_PREREG.md`, `ONSET_PREREG.md`, and `CONSISTENCY_PREREG.md` each have a single commit. `DEVIATIONS.md` only grows. This re-review does not treat the older outcome word inside the three early locks as a breach. Upstream process leaves locked preregistrations unrewritten.

## 5. Crossref

The only DOI added on this branch since `853e5a2` is `10.1109/9780470544242.ch21`, in `ADDENDUM_REVIEW_PREREG.md`. Crossref on 24 November 2026 returned HTTP 200. The record is a book chapter, issued 2009, publisher IEEE, ISBN `9780470544242`. The title field begins "Coding Theorems for a Discrete Source With a Fidelity Criterion" and continues, in the same string, with the 1959 convention-record note. The container-title field is "Claude E. Shannon". The author array is empty. No abstract was returned, so no sentence is quoted. The refresh notes cite no other DOI.

## 6. What was rerun

Head `7cba6b6eee654d1e7702bda77c992e99d829c253`, in a detached worktree. Pytest and the checkers do not import this review.

| Check | Result |
|---|---|
| Five lock blobs at the lock commit and at `7cba6b6` | the five sha256 values above, each file unchanged |
| Onset script present in `a27520c` | absent |
| Rerun of the four scoring scripts | stdout matches the stored `.out` files |
| `python3 tools/check_consistency.py` | `RESULT: PASS`. Wording FAILs 0. 29 INFO hits on frozen records |
| `python3 tools/check_fresh.py` | `RESULT: PASS`. `origin/main` window contains `31aa997` |
| `python3 tools/check_open_work.py` | `RESULT: PASS` |
| `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` | 295 passed, 1 skipped, 385.02s, exit 0 |

`numba` is not installed. `reviews/night2/CAUSAL_NULL_INVARIANCE/core.py` imports it, so that path is ignored, as in the PR's own pre-check. Pytest was absent at the start of this re-review and was installed in the user site (pytest 9.2.0, NumPy 2.5.5, SciPy 1.18.1, SymPy 1.14.0). The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed).

## 7. Wording

`ONSET_PREREG.md`, `CONSISTENCY_PREREG.md`, and the appended ledger blocks call a prediction error a miss and give it a signed size. They call the record price a cost. They do not claim a derivation of general relativity, quantum mechanics, holography, or gravity. The hypothesis sentence matches `CORE.md:7`.

The three early locks still contain the older outcome word and the retired headline token. `MEMO.md:41` still names that locked section by its older title. Those lines are inside the locked record. The new locks do not copy them.

Two maintained sentences still contradict the reclassification:

- `MEMO.md:51` says the addendum headline is not a consistency check. The consistency section at `MEMO.md:89` says every scored bar of the three earlier locks is `NOT A TEST`.
- The T84b cell in `OPEN_WORK.md` still says the addendum pass is not a consistency check, and later in the same cell says the scored bars are `NOT A TEST`.

The later sentence is the one that matches the arithmetic. `7cba6b6` edited both files and left the earlier sentence standing.

No email address and no phone number appear in the refresh notes or the scoring scripts.

## Findings

### High

**H1. The identification of the symmetric 4 with \(c^*=4\kappa kT\) is an identity. The prior blocker stands.** Comment `7145474164` blocked head `067c485` because no scored bar could miss while the closed forms stood. The response is a lock (`a27520c`), a score (`9930259`), a consistency lock (`cc4d406`), and a reclassification (`7cba6b6`). The new bars miss by \(+1\), \(+1/4\), and \(+4\), and the shared integer holds. Each of those four outcomes is fixed by a definition in `ONSET_PREREG.md`, as section 1 calculates. A rival that is the algebra of the lock cannot lose. `cc4d406` says so, and the third ledger labels the rows `NOT A TEST`. That label is the right gate for a sure-thing comparison. It is not a bar that can miss. The head stays a consistency check.

The class sentence in the consistency lock matches the files it cites. One reset, loss linear in the gap, no clock rate, is the slow-drift square-root/EOQ case at `theory/INTERNAL_MODEL.md:45` and `:180`, the same exponent as the continuous-diffusive balance at `theory/CLOCK_TERM_2026-11-23.md:55` and the square-root minimum at `CORE.md:91`. The \(w^{1/3}\) branch is the deterministic lag at `theory/CLOCK_TERM_2026-11-23.md:40-47`. Scoring the short-period ratios against that square-root balance is `NOT A TEST`.

### Medium

**M1. Two sentences still deny the consistency label the new section applies.** `MEMO.md:51` and the addendum clause in the T84b cell of `OPEN_WORK.md` say the addendum headline is not a consistency check. The prior review recorded that the addendum bars cannot miss. The third ledger now says the same, and the memo's new section says it too. The older sentence remains in both places. Location of that leftover is `process`. No formula changes.

**M2. The GAUSS row's location is not admissible.** The signed gap \(+0.021469\) at \(s=20\) reproduces. The row calls the location `measurement/code` and names no `MV` gate. The locked script scores the monomial, and that score holds. The envelope is a different loss. Location: `model`. Stake of the gap is medium as a description of the finite envelope, and it does not move a locked bar.

### Low

**L1. The second ledger's candidate rows are differences from unlocked readings.** `ACE-16` records \(4-16=-12\). `CLOCK-FLOOR` records \(\ln 2-4=-3.306853\). The locks predicted the symmetric limit 4 and the separation of \(\ln 2\) from 4. The third block relabels those bars and does not rewrite the earlier rows. The signed differences match the two numbers.

**L2. The ten-digit M3 miss is the gap between the slopes.** \(\alpha_E-1/4=+0.249999998333\) on the script's grid, and the exact limit is \(+1/4\). The logged \(+0.2499999984\) is \(\alpha_E-\alpha_U\). The uniform slope's own residual from \(1/4\) is \(-2.057\times 10^{-11}\), inside the locked \(10^{-9}\). The third ledger's statement, \(1/4\) and \(1/2\), is the exact pair.

## Ledger

**Lock reference:** `7cba6b6eee654d1e7702bda77c992e99d829c253` on `forge-dephasing-refresh`, reviewing locks `612b82e`, `9619565`, `6fb397b`, `a27520c`, `cc4d406`
**Logged at (ET):** 2026-11-24 17:16 ET
**Breach check:** `none` (the five locks are the blobs named above; this re-review does not patch them)

Rules: `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` on upstream `652d936`. Signed size is the independent value minus the locked point.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| HASH | five sha256 values, each file unedited, each lock before its script | all five match; onset script born in `9930259`; consistency lock has no script | HIT, residual 0 | process | low | none yet | none |
| M1 | both pure numbers within 0.05 of 4; \(c^*\) within \(10^{-12}\) of 4 | \(\Pi_c(0.01)=4.026744563040\), \(c^*=4\) | `NOT A TEST`; residual \(+0.026744563040\); information ~0 | model | low | none yet | none |
| M2 | elasticity of \(A_c\) within 0.05 of 0; rival weight 4:1 | float64 \(0.9999999999951152\), print \(+1.00000000\) | `NOT A TEST`; miss \(+1\) from 0; \(A_c\propto w\) | model | low | none yet | none |
| M3 | both age slopes within \(10^{-9}\) of \(1/4\); rival weight 4:1 | uniform \(0.249999999979\); exponential limit \(1/2\) | `NOT A TEST`; miss \(+1/4\) on the exponential slope; uniform residual \(-2.057\times 10^{-11}\) | model | low | none yet | none |
| M4 | half-slope limit within 0.05 of 4; rival weight 4:1 | \(1/(1/8)=8\) | `NOT A TEST`; miss \(+4\) | model | low | none yet | none |
| PARENT | printed parent, addendum, and fold-in digits | the float64 column in section 2 | HIT on the digits; identity rows are `NOT A TEST`; information ~0 | model | low | none yet | none |
| GAUSS | short-time monomial share \(1/3\) stands in for the envelope | envelope share \(0.35480226\) at \(s=20\) | signed \(+0.02146893\) from \(1/3\); their row locates this at `measurement/code` with no MV gate | model | medium | none yet | none |
| MEMO51 | scored bars of the addendum labeled as a consistency check after the prior review | `MEMO.md:51` still says the headline is not a consistency check; `MEMO.md:89` says `NOT A TEST` | process miss: the older sentence remains beside the reclassification | process | medium | none yet | none |
| DOI | the one added DOI resolves | Crossref HTTP 200, issued 2009, no abstract | HIT, no sentence quoted | process | low | none yet | none |
| WORD | new locks avoid the retired outcome words | `ONSET_PREREG.md` and `CONSISTENCY_PREREG.md` are clean; early locks keep their text | HIT on the new locks | process | low | none yet | none |

### Scaled notes (medium and high)

1. **M1 through M4, and the blocker.** The locked prediction on M2–M4 was the identification. The outcome sits on the rival side by \(+1\), \(+1/4\), and \(+4\), and M1 sits \(+0.026744563040\) from 4 inside a band the series already fills. Location is the model. No formula was changed. The update that would make a separation test is a later lock whose inputs these closed forms do not fix. This re-review does not build that lock. Information of the present comparison is about 0, so the stake of each numeric row is low. The clearance question is the high-stake item, and it stays open.
2. **GAUSS.** The envelope share at \(s=20\) is \(0.35480226\), signed \(+0.02146893\) from the monomial \(1/3\). The locked bar remains the monomial. No `MV` gate fired, and the script matches R6, so `measurement/code` is not an admissible location. The gap sits in the model, as a different loss. No update to a formula.
3. **MEMO51.** The prior review recorded that the addendum bars cannot miss. The new section agrees. Line 51 still says the headline is not a consistency check. Location is the process. The correcting sentence is already later in the same memo. No formula update.

## What holds

The printed digits match float64 to the last printed place, including the onset printout \(+1.00000000\), \(0.4999999983\), and \(+4.00000000\). The five hashes, the commit order, and the append-only growth of the ledger hold. The new locks have the required lines and the hypothesis sentence. The class citations at `INTERNAL_MODEL.md:45`, `:180`, `CLOCK_TERM:55`, and `CORE.md:91` are the sentences the consistency lock attributes to them. The single added DOI resolves at Crossref with no abstract.

## Attacks tried

1. Hash and order. Each stated sha256 matches the lock blob and the blob at `7cba6b6`. The onset script is absent from `a27520c` and present in `9930259`. The consistency lock has no script. Author dates equal committer dates. `THEORY.md` and `CORE.md` are untouched.
2. Circularity of the \(c^*=4\kappa kT\) identification. Expanded M1 as the parent series plus \(2b/a\), M2 as \(\partial\ln w/\partial\ln w\), M3 as the closed limits \(1/4\) and \(1/2\), and M4 as \(1/(1/8)=8\). The named rival cannot lose while `ONSET_PREREG.md` stands. The comparison is `NOT A TEST`.
3. Float64 recomputation of every stored print, including the parent ratios, accounting C, the holding-floor gap \(4-\ln 2\), the fold-in cells, and the Gaussian envelope at \(s=20\) and \(s=10^4\).
4. Ledger shape. Counted eight fields on all 65 rows, checked the append-only prefixes, and checked locations against the rule that `measurement/code` needs an `MV` gate or a reproducible bug in the locked script.
5. Wording scan of the new locks and the appended ledger, and a read of the two sentences that still deny the consistency label.
6. Crossref on the one DOI this branch adds since the PR base.
7. Consistency, freshness, open-work, and pytest with the numba path ignored.

The blocker from comment `7145474164` remains. No scored bar at this head can miss while the closed forms in the five locks stand.

Blockers remaining: 1
