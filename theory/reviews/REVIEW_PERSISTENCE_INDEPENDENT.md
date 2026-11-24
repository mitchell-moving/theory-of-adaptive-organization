# Independent review

Head `5660367007438f6cfa68c4f93cc38a140bebbe97`. The range `forge-record-ratio-dual..forge-record-ratio-persistence` is two commits: preregistration lock `f8ffe82` (parent `e7204dd`) and results `5660367`. Fork `main` is `0f3791890078161a1172277162df5ac13ebbff46`. `THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b` is the same on this head, on the lock, and on `main`.

This review uses the diff, the preregistration file, the stored run, and `main`. The arithmetic below was recomputed in a separate script that does not import `persistence_checks.py` or any other repository module.

## Checks

`python3 tools/check_consistency.py`: `FAIL: 0`, `INFO (frozen records): 29`, `RESULT: PASS`. Maintained docs scanned 31, wording FAILs 0. Frozen records scanned 499. CLAIM_MAP section N: 68 rows, 123 references, 0 mismatches. Process-rule FAILs 0 (CLAIM_MAP rows 392, tables 124). Core-rule FAILs 0. Two length lines are advisory warnings (THEORY.md main text 11325 words, README.md 1857 words).

`python3 tools/check_open_work.py`: items.json not-DONE 62, QUEUE.md not-DONE 90, union missing from OPEN_WORK.md 0, `RESULT: PASS`.

`python3 tools/check_fresh.py`: `RESULT: PASS`. STATUS.md states `d592662`, which is inside the last five first-parent commits of `origin/main` (`0f37918 d592662 f4ec246 341b7de b611a68`). The known freshness FAIL that appears only because the fork's `origin/main` has moved did not appear.

`python3 theory/record-ratio-persistence-2026-11-24/persistence_checks.py`: exit 0, stdout 8557 bytes, byte-identical to `persistence_checks.out`. Lines: `G0 PASS`, `P1 PASS worst_gap=0.000e+00`, `P2 FAIL ties=34 ties_nonflat=25 misses=24`, `A-restore FAIL n=10`, `A-ruin FAIL n=20`, `A-repin PASS Iback_max=5.551e-17`, `G-dyn PASS skip_gap=0 match`, `FAILS 3`.

`python3 -m pytest -q tools`: `308 passed, 1 skipped in 383.75s`, exit 0. The skip is `tools/test_lean.py:124`, Lean 4 / lake is not installed.

## Preregistration

The lock holds.

- `f8ffe82` (author and committer date 2026-11-24 17:54:23 UTC) adds only `PREREG.md` and `PREREG.sha256`. `persistence_checks.py`, the memo, the run log, and the stored stdout are in the child commit `5660367` (2026-11-24 18:13:53 UTC).
- sha256 of `PREREG.md` is `d48a03e1efa2925db460ad3da11aa9f2026f8f6d9d85c4810de09b1d1696cfea`. That is the value in `PREREG.sha256`, in the memo, and in `tools/test_persistence_checks.py`.
- Git blob `edd397fe81ffd351ce367642ca644d36762ae983` is the blob at the lock and at the head. The file's history is that one commit. The sha256 sidecar blob `b0be5aed46c81f67f8b872fdd76d9ceb2cd164c6` is likewise unchanged.
- `RUN_LOG.md` records no deviation: no prediction, margin, stake, ratio, ensemble, or cell was edited after the lock. The misses are results, and every one is in `persistence_checks.out` (24 P2 cells, 10 restoration cells, 20 ruin cells). The memo's counts match that list. An independent recount of the same rules on 65 channels (13 base, 26 restoration, 26 ruin) gives the same 34 ties, 25 non-flat ties, and 24 misses.

## Recomputation

`P_chi(0) = 0.096372378510879`, against the lock's `0.096372378511`.

**P1.** On all 13 base cells the worst gap is `0`. Twelve cells tie at gap `0`. On BIAS, `gamma=0`, `phi=0`, `w=2`, ratio 0 is strictly cheaper by `4.490563e-3`. No `q>0` undercuts `C_0(0)`.

**A-restore cell named in the memo.** ANT, `gamma=0`, `phi=0`, `w=2`, `alpha=1/2`: equator cost `0.408186189255`, pointer cost `0.391572378511`, gap `1.661381074456e-02`. The stored line `1.661381e-02` and the printed costs `0.408186` and `0.391572` match. The endpoint identity

`F_alpha(pi/2) - F_alpha(0) = (alpha-1) P_chi(0) + w (r^4/4) cos^2 phi`

reproduces that gap. The smallest of the ten misses is a different cell: ANT, `phi=pi/4`, `w=1`, `alpha=1`, gap `1.620000000000e-02`, which is `w (r^4/4) cos^2(pi/4)` and is already the fourth ANT row of the memo table. Nothing in the memo calls `1.661381e-2` the smallest miss.

**Ruin weights at `rho=1`.** ANT, `gamma=0`, `phi=0`, `w=1`, locked map: equator removal probability `1`, growth weight `0`, persistent cost `0.180000000`; pointer removal probability `0`, persistent cost `0.243972378510879`, growth weight `exp(-F) = 0.783509275656911`. The memo's `0.783509` and the stored `7.835093e-01` are that weight. Support on the locked menu is `{1, 2}`.

**`q=2` at `phi=pi/2`.** Under the locked rule (minimize `F` on the charged-cost tie set), grids of 721, 1441, 2881, and 5761 points, both `rho` in `{1/2, 1}`, and `w` in `{1, 2, 10}` all give support `{2}`. Ratio 1's charged cost is flat on the whole grid. The loss range is `0` on every one of those grids. Extending the menu to `{0, 0.25, 0.5, 0.64, 1, 1.01, 1.5, 2, 3, 10}` gives support `{1.01, 1.5, 2, 3, 10}`.

**A-repin.** Maximum absolute conditional information over the 36 angle pairs is `5.551115123125783e-17`, which is `2^{-54}`. The stored `5.551e-17` is that residual. It appears at `w=1`, `q=0.64`, first angle `1.544616`, second angle `pi/4`. The same quantity is identically `0`: the second-outcome entropy depends only on the angle between the axes, so `H(M2|M1) - H(M2|M1,W) = 0` for every ensemble.

`exp(P_chi(0)) = 1.1011690393433329`. The memo's `1.101169` matches. Half of that is `0.5505845196716664`, so a survival factor `1/2` leaves the equator behind the pointer when the persistent-cost gap is the whole ledger.

## Attacks tried

### (a) Restoration identity

`F_alpha = I + alpha P_D + w L` and `J` at ratio `alpha` are the same expression (PREREG §2.5 and §2.3). The absolute difference on the scored grids is `0`. Putting `alpha P_D` back into the stock makes the persistent cost `J` at ratio `alpha` before any angle is minimized. That sentence is an identity. It is the mechanism sentence the lock told the memo to use, and it is not evidence produced by the grid.

The grid's own content is the angle map. On 10 of 26 cells, `q=0` installs the equator and a positive menu ratio installs the pointer, and the gap is the endpoint formula above (or, off the antipodal complete-dephasing slice, the same scoring rule on the ensemble). All ten are tagged `RESTORE`. The gaps run from `1.620000e-02` to `1.882542e-01`. Those gaps are real inside the model. They are what the identity plus the already-scored angle map imply once `alpha` is a menu value whose installed angle differs from `T(0)`.

P1 is the same kind of elementary inequality, and the lock already says so: `C_0(0)` is the minimum of `F` on the grid, so a positive ratio scored at a grid angle cannot undercut it. The recomputed worst gap `0` confirms the implementation. It does not add a separate empirical claim.

### (b) The `q=2` survivor

The locked survivor is stable under refinement. It moves under the tie rule and under the menu.

At `phi=pi/2`, `w=1`, `rho=1`, 721-point grid:

| rule used inside the flat charged-cost set | support |
|---|---|
| locked rule, minimize `F` | `{2}` |
| largest angle | `{2}` |
| maximum `P_D` | `{2}` |
| smallest angle | `{1, 2}` |
| minimum `P_D` | `{1, 2}` |

The smallest-angle rule is the rule the lock already uses when the selection score itself is flat. On this cell the selection score is not flat (its range is the ledger), so the code takes the minimum-`F` branch, installs the equator for ratio 1, and the ruin map then removes that equator. Resolving the same indifference toward the undisturbed end of the grid puts ratio 1 in the support at the same growth weight as ratio 2. On the extended menu that smallest-angle support is `{1, 1.01, 1.5, 2, 3, 10}`.

Every ratio strictly above 1 installs the pointer, with `P_D=0` and the same growth weight. Ratio 2 is the only such point on the locked menu `{0, 0.25, 0.5, 0.64, 1, 2}`. The six flat-loss ruin cells keep 2 because of that menu and because ratio 1 is assigned the equator. A finer grid does not change the assignment: the pointer and the equator are on every grid that includes the endpoints, and the loss is exactly flat.

### (c) Removal-probability form

The locked map is `p = min(1, rho P_D / P_max)`. At a most-disturbed angle this is `p = rho`, so `rho=1` sets the growth weight to 0 by the cap. The equator beats a safe pointer only when its removal probability is below `1 - exp(-(F_pointer - F_equator))`. On ANT at `gamma=0` that threshold is `6.196909e-2` (`phi=0`, `w=1`), `3.107918e-2` (`phi=0`, `w=2`), `7.704277e-2` (`phi=pi/4`, `w=1`), `6.196909e-2` (`phi=pi/4`, `w=2`), and `9.187421e-2` at `phi=pi/2` for every scored stake. The locked `p` at the equator is `0.5` or `1`, above all of those thresholds. That is why 20 of 26 cells drop ratio 0.

Shapes that keep a large value at `P_max` do not change the count. On the same 26 cells:

| monotone map | cells that exclude 0 |
|---|---:|
| locked `min(1, rho P_D/P_max)` | 20 |
| `1 - exp(-rho P_D/P_max)` | 20 |
| `rho P_D / (P_D + P_max)` | 20 |
| `min(1, rho (P_D/P_max)^2)` | 20 |
| `min(1, rho P_D)` with `P_D` in nats | 13 |

The square map agrees with the locked map at both endpoints, and the installed angles on these misses are endpoints, so the interior shape never gets scored. The absolute map `min(1, rho P_D)` puts 0 back into the support on all seven `rho=1/2` cells where the locked map had excluded it, including the three flat-loss cells. On those three the absolute support is `{0, 0.25, 0.5, 0.64, 1}` and ratio 2 is absent (`g` about `0.795022` against `0.758530` at `w=1`). At `rho=1` the absolute map still keeps `{2}` on the flat-loss axis, by a thin margin (`0.754773` against `0.758530` at `w=1`).

A second monotone alternative, `p = 1 - exp(-rho P_D)` with no division by `P_max`, was scored on the flat-loss cell `w=1`. At `rho=1/2` the support is `{0, 0.25, 0.5, 0.64, 1}` and ratio 2 is out. At `rho=1`, `p` at the equator equals `1 - exp(-P_chi(0)) = 0.09187421343017743`, which is the threshold, so the growth weights agree through `1e-16` and the locked tolerance ties the whole menu, including 0 and 2.

The locked weights `0` and `0.783509` are correct for the locked map. They are the cap at `p=1` and `exp(-F)` at the pointer. A removal probability that is monotone in `P_D` and is not normalized by the menu maximum does not produce those weights, and on the flat-loss axis it does not leave `{2}`.

### (d) Classical-record assumptions

The base selector states them. A nat is persistent when it sits in the classical record or in the loss, and `P_D` is omitted from `F` (PREREG §2.2). `I` is the Shannon mutual information `H(M) - H(M|W)` of the binary outcome. `P_D` is the average of outcome entropy minus the von Neumann entropy of the pre-measurement state. On ANT at `gamma=0` the ledger `I + P_D` has range `0` and value `P_chi(0)`, so dropping `P_D` prices one side of a constant sum.

The Holevo quantity of the pre-measurement ensemble was recomputed at the endpoints of every scored `(ensemble, gamma, phi)`. It does not depend on the angle (maximum absolute change `0`). Omitting it does not hide an angle-dependent quantum term.

The second pinch is a projective update: given the first outcome, the post-measurement state is the corresponding pure projector, and the second-outcome law depends only on the angle between the axes. Conditional information is then an identity, for every ensemble, not a recovery bound that this grid could have failed. The printed `5.551e-17` is one unit in the last place. The population step is an infinite classical replicator on a finite menu of heritable ratios, with a classical survival probability multiplied onto `exp(-C_0)`. The classical record is assumed to persist in full. No decay of `M` is in the model.

### (e) Strength of the claims

The new prose stays inside the model. The hypothesis sentence in `CORE.md`, `PREREG.md`, and `MEMO.md` is the sentence at `CORE.md:7`. A scan of the added lines finds no `theory of everything`, no `solved`, no `bill`, no `kill`, no `verdict`, and no `law` outside that hypothesis sentence. The memo, the preregistration, and the index row say that nothing here derives general relativity, quantum mechanics, holography, or gravity. `THEORY.md` is unchanged. The labels used are the lock's labels: PROVED (in-model), NUMERICAL, PUZZLE.

The sentences that reach past the locked objects are the ones in (a), (b), and (c): the restoration identity offered as the mechanism, the index line that the flat-loss removal channel keeps ratio 2, and the memo's closing conditional "removal proportional to `P_D`" with support `{2}`. Those are scope sentences. They are not a claim to a physical law or to a derived ratio outside this menu.

### (f) DOIs

No DOI was added. The diff hunks that display `10.1126/sciadv.aee0802` and `10.1088/1367-2630/16/10/103011` are pre-existing T77 and T75 rows carried as context. Crossref was not queried.

## Findings

### BLOCKING

None. The locked counts, the five recomputed numbers, the preregistration hash, and the wording bounds hold.

### HIGH

1. **Restoration is an identity plus an angle map.** `F_alpha` is `J` at ratio `alpha` by the definition in PREREG §2.5. The ten `RESTORE` misses are the cells where `T(0)` and `T(alpha)` differ, with gaps from `1.620000e-02` to `1.882542e-01`. The memo should label the equality as an identity. The evidence is the angle separation and those gaps.

2. **`{2}` is the locked menu under one resolution of a flat charged cost.** On `phi=pi/2` the minimizer for every `q>1` is the pointer, and those ratios tie. Ratio 2 is the only menu point above 1. Grids through 5761 points leave the support at `{2}`. The smallest-angle rule and the minimum-`P_D` rule, applied to ratio 1's flat charged cost, put ratio 1 in the support with the same weight. `theory/README.md` says the removal channel keeps ratio 2 on the flat-loss axis. That sentence needs the menu and the tie rule in the same sentence.

3. **The ruin exclusion is the size of `p` at maximum disturbance.** The locked map sets that probability to `rho` and, at `rho=1`, the growth weight to 0. Thresholds on ANT are between about `0.031` and `0.092`. Maps that stay large at `P_max` keep all 20 exclusions. The monotone map `min(1, rho P_D)` returns 0 to the support on 7 cells, all at `rho=1/2`, and on the flat-loss axis it drops ratio 2. The hazard `1-exp(-rho P_D)` does the same at `rho=1/2` and ties the whole menu at `rho=1`. The weights `0` and `0.783509` are correct for the locked cap. The memo's closing conditional, removal proportional to `P_D` with flat-loss support `{2}`, is broader than the map that was scored.

### MEDIUM

4. **The base split and the second pinch are modeling choices with identities behind them.** Persistent cost `I + w L` declares the classical record permanent and `P_D` absent. On the antipodal complete-dephasing ensemble that drops one side of a constant ledger. A-repin passes because a projective second measurement has conditional information `0`; `5.551e-17` is roundoff, reproduced as `2^{-54}`. The memo attributes the pass to `second_pinch`. The pass does not constrain a recovery that keeps the pre-measurement system or reverses the pinch. Holevo `chi` was checked and is angle-independent, so it is not an extra design term hiding in the same objects.

### LOW

5. **The branch does not contain dual tip `2e656b0`.** That commit is the T77 errata (binding-cap price exactly 1 at `phi=pi/2`), dated 17:45 UTC, nine minutes before the lock. The lock's parent is `e7204dd`, as the preregistration says. A merge into current `forge-record-ratio-dual` conflicts in `OPEN_WORK.md` and `theory/README.md`. `RECORD_RATIO_DUAL_2026-11-24.md` is untouched by these two commits; a two-dot diff of the tips shows the errata text as absent only because the branch point is the pre-errata commit. The T78 numbers do not depend on editing that file. The preregistration already records, as prior exposure, that every binding upper cap at `phi=pi/2` has shadow price 1.

## What stands

On the base selector, ratio 0 weakly dominates on the 13 cells, worst gap `0`, and the finite replicator matches the support (`G-dyn`, `skip_gap=0`). The second-pinch residual is roundoff on an identity. Restoration misses on 10 cells because `F_alpha` is `J_alpha` and the installed angles differ. Ruin misses on 20 cells for the locked removal map, and the flat-loss support on that map and this menu is `{2}`. All three fails are inside the objects the lock defined. None of them is a value of `kappa_D/kappa` outside that menu, that tie rule, and that removal map.

Blockers remaining: 0
