# Independent review of T81

Reviewed head `f625bb74c2702a6a9b1f7d5b8afff922f90cf8b3` on `forge-record-ratio-measured`. Lock `22993a8a63213db260f55daad402a9bdef0d6e9e` (2026-11-24 20:02:18 UTC). Result commit `f625bb74c2702a6a9b1f7d5b8afff922f90cf8b3` (2026-11-24 20:15:18 UTC). Parent of the lock `eb372973a565840a1536211d1b4d1a0a60403ef3`.

Scope is the diff from that parent to the head, the preregistration, and `main`. Pull-request text was not used.

The scored script reproduces. The lock is intact. Three locked lines fail, and the failures match the recomputation. The comparisons that still carry information are the diffusive collapse, the cosine-series gap, and the closedness failure. On the six locked fixed-point cells the iteration stops on the entrance fraction of one extreme packet width. Between two of those horizons the same map cycles.

## Runs

Python 3.12.3. The clock was recomputed with NumPy 2.5.5 (`eigvalsh`) and with the closed form below. `numba` is not installed, so pytest ignored `reviews/night2/CAUSAL_NULL_INVARIANCE`. That directory defines no test functions. `lake` is not on `PATH`.

| Command | Result |
|---|---|
| `python3 tools/check_consistency.py` | exit 0. `FAIL: 0`, `INFO (frozen records): 29`, maintained docs 31, frozen records 511. `RESULT: PASS` |
| `python3 tools/check_open_work.py` | exit 0. items.json not-DONE 62, QUEUE.md not-DONE 90, missing from OPEN_WORK.md 0. `RESULT: PASS` |
| `python3 tools/check_fresh.py` | exit 0. `RESULT: PASS` |
| `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` | exit 0. **323 passed, 1 skipped**, 386.49s. The skip is `tools/test_lean.py::test_lean_build_if_available`, reason `Lean 4 / lake is not installed` |
| `measured_checks.py`, two runs | stdout identical across the two runs and identical to the stored `measured_checks.out` (153 lines) |

Scored lines in that stdout: 16 checks, 13 `PASS`, 3 `FAIL`, trailer `FAILS 3`, `DIAG deviations 0`. The passes include 2 `holds-by-construction`. The fails are `G-gap`, `M1-scale`, and `M4`. Also present: 12 `PREDICT` lines, 4 `REPORT` lines, 1 `E-pair` line, 10 `CLASS` lines, 109 `DIAG` lines. The first `PREDICT` line precedes the first measured `DIAG m4` line.

## Preregistration lock

The lock commit contains only `PREREG.md` and `PREREG.sha256`. `measured_checks.py` appears first in the result commit, 13 minutes later.

Content sha256 of `PREREG.md`, computed here:

`2e31c41bbc175722a421b7547af1670551cf14d5b912a3158d7085b62dff501c`

That digest is the first field of `PREREG.sha256`, the constant in `tools/test_measured_checks.py`, and the digest named in the memo and the run log. The git blob of `PREREG.md` is `e8ebbc97f435bddac2e0a7ef591b41752ca02d19` at the lock and at the head. The diff of the preregistration between those commits is empty.

`THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b` is the same object at `main`, at the lock's parent, at the lock, and at the head. The result commit does not edit it.

`DEVIATIONS.md` is introduced once, in the result commit, and has no later commit. Its text is the single entry "No deviation." together with the statement that the lock was not edited. There is no rewritten earlier entry. Append-only holds. The script's grids, tolerances, horizons, bins, starts, and eigenvalue limits match the locked text. The script does not read `PREREG.md`. `SEED = 20261124` is assigned and unused. The script imports no random module.

## Independent recomputation

The walk, the Fourier series, the fixed-point iteration, and the histogram were recomputed without importing `measured_checks`. The Jacobi `finished` flag below is the one place their routine was called, as a check of that instrument.

**Decoupled clock.** On the reflecting path of `N` sites the gap clock is

`τ_mix(N) = 1 / sin²(π / (2N))`.

The eigenvector `v_j = cos(π (j + 1/2) / N)` has residual below `2e-16` against `λ = cos²(π / (2N))`. NumPy's symmetric eigensolver agrees with the closed form to `1e-10` or better on every locked `N`.

| N | closed form |
|---|---|
| 12 | 58.695480540981 |
| 16 | 104.086868919817 |
| 24 | 233.777626218406 |
| 32 | 415.345062231902 |
| 48 | 934.109433187964 |

**G-decouple.** The environment block of the full lazy path and the decoupled reflecting matrix differ in one entry, index `(0, 0)`, by `0.25`. The contact row of the block sums to `0.75`. At `N = 32` the spectral radius of that block gives decay time `1712.661376`, while the decoupled gap clock is `415.345062`.

**M2.** All 40 cells pair. All 8 nominal `x` stay in the collapse. `ρ = 0.052051664190`, attained at nominal `x = 2`, where the five returns run from `0.379772952863` (`N = 12`) to `0.431824617054` (`N = 48`). Shape gap `0.006720277156` on 20 cells. The worst cell is `N = 12`, `x = 2`: return `0.379772952863`, series `0.373052675708`. Interior, `N = 32`: `q(0.5) = 0.095799965060`, `q(1) = 0.239059227845`.

**M1-scale.** Fixed `T = 32`, closed kernel, midpoint start:

| N | return |
|---|---|
| 12 | 0.081686009166 |
| 16 | 0.024811974888 |
| 24 | 0.001090083804 |
| 32 | 0.000015717030 |
| 48 | 4.2705e-11 |

Successive gaps: `5.6874e-2`, `2.3722e-2`, `1.0744e-3`, `1.5716987e-5`. The last gap is the memo's `1.572e-5`. It lies under the locked `1e-4`. The five returns decrease, the `N = 12` return is above `0.01`, and the `N = 48` return is below `0.20`.

**M3.** Five starts on each locked cell, terminals equal to 12 decimals:

| cell | T | terminal | which return |
|---|---|---|---|
| m3-a | 208 | 0.106409485164 | width 9 |
| m3-b | 415 | 0.246706007043 | width 9 |
| m3-c | 831 | 0.422916079022 | width 1 |
| m3-d | 415 | 0.246706007043 | width 9 |
| m3-e | 21 | 0.000005868622 | width 9 |
| m3-f | 3323 | 0.866153244874 | width 1 |

The span of returns across widths 1 through 9 is `0.010610`, `0.007647`, `0.004687`, `0.007647`, `5.84e-6`, and `0.001040`. Each span is under the `0.02` diameter bar.

**M4.** Total variation `0.909090909091 = 10/11`. Ten of the eleven predictions lie in `[0, 0.2)` and one lies in `[0.2, 0.4)`. All eleven fixed points lie in `[0.2, 0.4)`. Raw midpoint returns at the same horizon move from `0.237535898178` at `c = 0` to `0.239059227845` at `c = 1`.

**G-gap.** Their Jacobi run reports `finished = True` and `τ(48) = 934.109433200061`, which is `1.2097e-8` above the closed form. Their 4000-step power value is `934.109433187855`, `1.1e-10` below the closed form. The method difference is `1.2206e-8`, the memo's `1.221e-8`.

**E-pair.** Same `T = 415`, `N = 32`, `c = 1`: midpoint `0.239059227845`, far site `0.048343059332`, difference `0.190716168513`.

## Attacks tried

### (a) Circularity

These hold by construction in the closed, conserving path the preregistration writes down.

1. M1-closed. The contact is reachable on a finite path. At `200 τ_mix` the entrance fraction is `1` at `N = 12` and `1 - 2e-13` at `N = 48`. The preregistration marks the match as construction.
2. M1-sink. The contact quarter is sent to the sink. Both horizons return `0`. Marked as construction.
3. A continuous self-map of `[0, 1]` has a fixed point by the intermediate-value theorem. The preregistration leaves this unscored and says the stepwise map does not inherit that root.
4. The entrance fraction is monotone in `T` for this kernel. Unscored.
5. G-rev. The generator is built symmetric and row-stochastic. The symmetry residual is `0` and every row sums to `1`.
6. G-cons. Twenty steps of that matrix keep mass `1`.
7. G-start. The reference start is a point mass. On the length-16 path its total variation from uniform is `15/16 = 0.9375` and its entropy is `0`.
8. G-decouple as the script executes it. The compared "return restriction" is the decoupled matrix after `0.25` is subtracted from entry `(0, 0)`. The contact row sum in the test is the literal `0.75`. The G-decouple finding below records the independent comparison. The stochastic check of the decoupled matrix can still fail.
9. G-equiv at the locked cell `N = 12`, `T = 5`, start index `6`. The entrance takes 7 steps, so both accountings are `0`.
10. On the six locked cells, once the iteration stops, the POINT diameter and the `Φ` spread are inside `0.02`. Every value of `Φ` lies in the width band, and the widest of those bands is `0.01061`.

What remains, and is evidence about this walk:

- M2-collapse. `ρ = 0.052051664190` against a bar of `0.08`. The range is a finite-`N` remainder of diffusive scaling for the midpoint start. It is large enough that the comparison can fail.
- M2-shape. The 40-term cosine series, with diffusivity `1/4` fixed by the per-step variance, tracks the chain to `0.006720277156`. The preregistration is right that the series is an approximation.
- M2-interior. The two `N = 32` returns sit in `(0.05, 0.95)`.
- M1-scale's miss. The decrease is real and the last step is under the locked floor.
- M4's miss. At this horizon the far-end leak does not move the midpoint entrance fraction through the clock `x(c)`.

Those five statements are statements about a lazy path's hitting probability. The fixed points move with the horizon (`0.1064`, `0.2467`, `0.4229` at nominal `x = 0.5, 1, 2`). Each one is the entrance fraction of width 9 or width 1.

### (b) Closedness and the returning flow

The eigenvalue routine reads the decoupled matrix. It does not read the accumulated entrance mass. The shared input is the boundary parameter `c`.

At `c = 1` the clock is the gap above, closed form `1/sin²(π/(2N))`. At `c < 1` the clock is `1/(1 - λ_max)` of the leaky matrix. On the locked grid that leak time runs from `1712.66` to `2740.65`, and at `c = 1` the definition switches to the gap `415.35`. Off the grid, at `c = 0.999`, the same definition gives `τ = 129305` and `x = 0.0032`, while the raw entrance fraction is still `0.23905`. As `c` approaches 1 from below, this clock diverges, and the prediction `f(x(c))` is driven toward the small-`x` end of the curve.

The entrance fraction at `T = 415` moves by `0.00152` from `c = 0` to `c = 1`. The leak time and the hitting fraction answer different questions. The matrix difference of `0.25` is real when the full-path block is built on its own. The committed check edits one copy of the decoupled matrix and then reads the edit back. The G-decouple finding records that.

At `N = 32` the decay time of the killed environment block equals the `c = 0` leak time through the six decimals printed (`1712.661376`). Reflecting at the contact and leaking at the far end is the reverse of absorbing at the contact and reflecting at the far end.

### (c) The E-pair

At the locked horizon the two returns differ by `0.190716168513`. The state of each world is the site of one excitation. The worlds differ by the initial site: index `16` and index `31`.

Absolute difference against multiples of `τ_mix(32)`:

| x | T | difference |
|---|---|---|
| 0.25 | 104 | 0.018455 |
| 0.50 | 208 | 0.092906 |
| 1 | 415 | 0.190716 |
| 2 | 831 | 0.200853 |
| 4 | 1661 | 0.128932 |
| 8 | 3323 | 0.048884 |
| 16 | 6646 | 0.007019 |
| 32 | 13291 | 1.448e-4 |
| 64 | 26582 | 6.16e-8 |
| 200 | 83069 | 3.6e-15 |

Both returns are `1` at `x = 200`. The difference rises from the locked horizon to about `x = 2`, then falls to `0`. It is the transient of two deterministic initial conditions on a chain whose closed-world entrance fraction tends to `1`. The memo records the locked difference and says the scored collapse uses one start rule. The limit is the rest of the fact.

### (d) The fixed-point map

The map is a step function of `q`. For stake `w = 2` the minimizing width is 9 on `[0, 0.28)` and 1 from about `0.365` upward, with the intermediate widths packed into an interval of width about `0.085`. For stake `w = 1` that window sits near `0.64` to `0.685`. A step function on `[0, 1]` has an unbounded Lipschitz constant at each jump, so the Banach hypothesis fails on that interval.

On every locked cell the band of entrance fractions lies wholly below that window or wholly above it.

- Below the window, `Φ` equals the width-9 return. Cells m3-a, m3-b, m3-d, and m3-e stop there. At `T = 415` the band is `[0.23906, 0.24671]`, under the `w = 2` window and under the `w = 1` window, so the two stakes print the same point.
- Above the window, `Φ` equals the width-1 return. Cells m3-c and m3-f stop there.

Every start reaches that constant in at most three updates. The five terminals agree because they are the same constant.

Off the locked grid, at `N = 32`, `w = 2`, `φ = 0`, `T = 500` (between the locked horizons 415 and 831), all five starts enter a 2-cycle: width 7 returns `0.288952`, width 8 returns `0.291620`, and the step is `2.668522e-3`, above the stop tolerance `1e-4`. The locked rule labels that run `CYCLE`. The same rule's diameter test cannot fail on the six locked cells once a run has stopped, because the width band is at most `0.01061`.

`POINT` on the locked cells is the correct label for those six horizons. It is the entrance fraction of the extreme width on the side of the decision window where the minimizer does not depend on `q`. The memo, the `CLASS` line, `theory/README.md`, and the T81 row of `OPEN_WORK.md` call this a match and call it evidence.

### (e) G-gap and M4

G-gap is a tolerance. Jacobi meets its off-diagonal test (`finished = True`, threshold `1e-12`) and the resulting `τ(48)` still sits `1.2097e-8` above `1/sin²(π/96)`. Power iteration and a dense eigensolver agree with the closed form near `1e-10`. The gap is about `1.07e-3`, and `dτ ≈ τ² dλ` with `τ² ≈ 8.73e5`, so an eigenvalue error near `1.4e-14` moves `τ` by `1.2e-8`. The integer horizons used in M2 are unchanged between the Jacobi clock and the closed form. Smaller locked `N` sit under the bar because `τ²` is smaller.

M4 is a substantive miss. The predicted curve sits under `0.015` for every `c < 1` and at `0.226` for `c = 1`. The measured fixed points sit near `0.245` for every `c`. Half the `ℓ1` distance of the bin masses is exactly `10/11`. The raw entrance fraction is almost flat in `c`, so the histogram is the flat return against a clock that jumps from a leak time near `2700` to a mixing time of `415`.

### (f) Return channel and time symmetry

The full-path generator has the lazy neighbor steps and the holding reflection at the two endpoints. The symmetry residual is `0`. The entrance into the agent is the neighbor step off environment index `0`. There is no second copy of an edge and no edge that skips a neighbor.

The generator is symmetric, and section 2 of the preregistration says the walk is reversible. With the uniform measure, the rate on an edge equals the rate on the reversed edge. Section 9 says the run will not set a reverse rate equal to a forward rate. The script builds one matrix. It does not build a reverse table. The starts are point masses, at index `N//2` and, for the E-pair, at index `N - 1`. Those starts are out of stationarity. G-start records total variation `0.9375` and entropy `0`.

### (g) Classical-record assumptions

Stated in the preregistration, and doing real work:

- The destroyed record is a classical excitation on a path, or `W` independent copies. The scored `q` has no alphabet and no entropy term. The Landauer citation supplies the motivation for placing the excitation outside the agent. The factor `kT ln 2` does not enter the arithmetic. The behavioral cost that receives this `q` is the qubit functional `closed_form_ant` (binary entropy of an ANT ensemble, `R = 0.6`).
- The scored functional is first entrance. The sentence before the formula says an excitation in the agent has to be removed before the blank record is back. At `T = 415` from the midpoint, the entrance fraction is `0.23906` and the probability the excitation occupies the agent is `0.08197`. The stationary occupation is `4/36 = 1/9`. The closed-world entrance fraction tends to `1`. The occupation tends to `1/9`.
- The floor formula gives widths 2 and 3 the same three sites, and likewise for each even width and the next odd width. Five distinct blocks are scored as nine widths.
- The fixed-point loop sets the coefficient in `J` equal to an entrance fraction. On the locked cells that coefficient comes back as the extreme-width fraction in (d).

The one-dimensional recurrence that forces M1-closed is stated and marked as construction.

### (h) Banned wording

In `PREREG.md`, `MEMO.md`, `RUN_LOG.md`, `DEVIATIONS.md`, `measured_checks.py`, and `measured_checks.out`, the substrings `theory of everything`, `solved`, `bill`, `kill`, and `verdict` are absent. The word `law` occurs on the hypothesis line of the preregistration and the memo, and nowhere else in those six files. `check_consistency.py` reports 0 wording failures on the maintained documents. The new sentences in `theory/README.md` and `OPEN_WORK.md` are inside that pass.

The preregistration says the memo uses the labels PROVED, NUMERICAL, and PUZZLE. The memo has a NUMERICAL section and a puzzle paragraph. It has no PROVED label. `DEVIATIONS.md` records no deviation. The G-equiv finding records the missing label.

### (i) Crossref

Each DOI was requested from `https://api.crossref.org/works/{doi}` on this review. All four returned HTTP 200.

| DOI | Crossref | Locked citation |
|---|---|---|
| `10.1147/rd.53.0183` | R. Landauer, Irreversibility and Heat Generation in the Computing Process, IBM Journal of Research and Development 5(3), pages 183–191, issued 1961-07 | matches |
| `10.1090/s0002-9904-1947-08927-8` | M. Kac, On the notion of recurrence in discrete stochastic processes, Bulletin of the American Mathematical Society 53, pages 1002–1010, 1947 | matches |
| `10.1007/bf02392508` | H. Poincaré, Chapitre II. Théorie des invariants intégraux, Acta Mathematica 13, pages 46–88, 1890 | matches, including the chapter page range |
| `10.1090/mbk/058` | David Levin, Yuval Peres, Elizabeth Wilmer, Markov Chains and Mixing Times, American Mathematical Society monograph, issued 2008-12-09 | matches; the preregistration claims no page |

No number in the run is taken from these works.

## Findings

### BLOCKING

None.

### HIGH

**The locked POINT cells are the extreme-width return, and the map cycles off that grid.** For `w = 2` the minimizing width depends on `q` only on an interval of width about `0.085` near `0.28`. For `w = 1` the interval is near `0.64`. On m3-a, m3-b, m3-d, and m3-e the entrance band lies below the interval, so `Φ` is the constant width-9 return (`0.106409485164`, `0.246706007043`, `0.246706007043`, `0.000005868622`). On m3-c and m3-f the band lies above it, so `Φ` is the constant width-1 return (`0.422916079022`, `0.866153244874`). Five starts agree because each start lands on that constant within three updates. The width band is at most `0.01061`, so a stopped run meets the `0.02` diameter bar on these cells. At `T = 500`, `N = 32`, `w = 2`, between locked horizons 415 and 831, all five starts 2-cycle between `0.288952` (width 7) and `0.291620` (width 8), step `2.668522e-3`, which the locked rule calls `CYCLE`. The `CLASS` line marks M3-conv as evidence. The memo, `theory/README.md`, and the T81 row of `OPEN_WORK.md` state the fixed point as a match. The six cells are computed correctly. The match is the corner of the menu at which the width no longer depends on `q`. The Banach hypothesis fails on `[0, 1]`.

### MEDIUM

**G-decouple, as executed, builds the difference it reports.** The script copies the decoupled matrix, subtracts `0.25` from entry `(0, 0)`, and sets the contact row sum to the literal `0.5 + 0.25`. The memo cites the passing line, difference `0.25` and row sum `0.75`, as the demonstration that the clock is not the return. An independent environment block of the full path differs from the decoupled matrix by `0.25` at that single entry and has contact row sum `0.75`. The spectral clocks differ: gap `415.345062` against killed-block decay `1712.661376` at `N = 32`. The fact holds. The committed check does not compare the two operators.

**The E-pair difference is a finite-horizon transient.** Locked value `0.190716168513` at `x = 1`. The difference peaks near `x = 2` at `0.200853` and is `1.448e-4` at `x = 32` and `0` at `x = 200`, with both entrance fractions equal to `1`. The memo records the locked pair and the single start rule of the scored collapse. The closed chain's long-time limit is the rest of the comparison.

### LOW

**G-gap is the reciprocal of a small gap.** Jacobi finishes and remains `1.2097e-8` above `1/sin²(π/96)`. Power iteration is within `1.1e-10` of that closed form. The printed method gap `1.221e-8` is this conditioning. It sits in the memo next to the M4 miss. The horizons used downstream do not move.

**G-equiv's locked cell compares two zeros, and the memo omits the PROVED label.** From environment index 6 the first entrance takes 7 steps, so at `T = 5` both sides are `0`. The memo says so. At `T = 7` both sides equal `(1/4)^7 = 6.103515625e-5`, and at `T = 12, 20, 40` they agree to `1e-16`. Separately, the preregistration says the memo uses PROVED, NUMERICAL, and PUZZLE. The memo has NUMERICAL and a puzzle paragraph and no PROVED label. `DEVIATIONS.md` records no deviation.

**The symmetric generator equates forward and reverse rates under the uniform measure.** Section 2 states reversibility. Section 9 says a reverse rate will not be set equal to a forward rate. The implementation has one symmetric matrix, no reverse table, and point-mass starts (total variation `15/16` from uniform).

**First entrance and occupation have different limits.** The formula scores first entrance. At the locked `T = 415` the entrance fraction is `0.23906` and the agent's occupation probability is `0.08197`. Stationary occupation is `1/9`. The closed-world entrance fraction tends to `1`, which is the construction result M1-closed. Occupation tends to `1/9`.

Blockers remaining: 0
