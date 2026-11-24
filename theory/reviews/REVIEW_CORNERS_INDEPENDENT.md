# Independent review of T80

Head `eb372973a565840a1536211d1b4d1a0a60403ef3` on `forge-record-ratio-corners`. Reviewed against the three-dot diff from `forge-record-ratio-bicausal` (merge-base `2df1925d96f7992b29eb2905fd32b1db36c9e6d8`), the lock commit `4786746bfdcb114e41e3301a2abc7e38a57aa315`, and `main` at `0f3791890078161a1172277162df5ac13ebbff46`. The base tip `a7dd3f29082ffe05f2a2debdb1258ad0d881953e` is not in the head. That commit touches the T79 memo and run log only; the T79 locks, script, and stored stdout are outside it. Those notes are not used here. The scored diff is two commits, 10 files, 1206 insertions.

The recomputation below does not import `corner_checks.py` or the T76 module. The closed form and the four-point ensemble were written out again from the antipodal menu (`γ = 0`, Bloch length `r = 0.6`).

## Checks

| Command | Result |
|---|---|
| `python3 tools/check_consistency.py` | PASS, exit 0. Maintained docs scanned 31, wording FAILs 0. Frozen records scanned 507, INFO hits 29. CLAIM_MAP section N has 68 rows (N1 through N68); N references checked 123, mismatches 0. Rows counted 392, tally 392. Tables checked 124. Process-rule FAILs 0 (self-review headers found 14). Core-rule FAILs 0. Advisory length warnings: THEORY.md main text 11325 words, README.md 1857 words. Summary `FAIL: 0`, `INFO: 29`. |
| `python3 tools/check_open_work.py` | PASS, exit 0. `items.json` not-DONE 62. `QUEUE.md` not-DONE 90. Union missing from `OPEN_WORK.md`: 0. |
| `python3 tools/check_fresh.py` | PASS, exit 0. `STATUS.md` main is `d592662`. Window of `origin/main`: `0f37918 d592662 f4ec246 341b7de b611a68`. |
| `python3 -m pytest -q tools` | `318 passed, 1 skipped in 383.64s`, exit 0. The skip is `tools/test_lean.py::test_lean_build_if_available`: `lake` is not on `PATH`, so the test takes the branch "Lean 4 / lake is not installed". Pytest 9.2.0, NumPy 2.5.5, SciPy 1.18.1, SymPy 1.14.0. |
| `python3 theory/record-ratio-corners-2026-11-24/corner_checks.py` | Exit 0. Stdout is 62 lines and byte-identical to `corner_checks.out`. The file ends `FAILS 3`. |

## Lock, blob, and the 45-versus-46 line

The lock commit `4786746` (2026-11-24 19:34:02 UTC) is the parent of the result commit `eb37297` (2026-11-24 19:45:32 UTC). Its parent is the merge-base `2df1925`. The lock tree contains `PREREG.md` and `PREREG.sha256` only. `corner_checks.py` is absent from that tree.

`sha256sum` of `PREREG.md` is `367adf39a76ef6adebe3881702a8a8f7997099280e10313b66d8f105dba3f69f`. The same digest is the first field of `PREREG.sha256`, the digest named in the result notes, and the digest of `git show 4786746:theory/record-ratio-corners-2026-11-24/PREREG.md`. The git blob `585b0722d21d26fa08a2231e449ce94cdc6866d4` is identical at the lock and at the head. The preregistration was not edited after the lock.

`THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b` is the same object at the lock, the head, local `main`, and `origin/main`.

The family table enumerates 18 + 1 + 3 + 9 + 9 + 1 + 1 + 1 + 3 = 46 cells. The sentence after the table says 45, and the equal-weight paragraph says the sum is over 45 cells. `DEVIATIONS.md` is introduced in `eb37297` and has no later commit. It records that every row was scored and that no family was dropped. The independent cell list has 46 rows, and the stored equal-weight masses match a normalization over 46, not over 45. The deviation file is a single entry. Git shows no rewrite of it and no edit of the lock.

The committed thresholds match the lock: floor `5e-3`, wide bar `0.01`, tie-point width `1e-6`, multiplier tolerance `1e-3`, form gap `1e-9`, cone targets `1e-15` and `1e-9`, peak mass `0.10`, neighbor factor `1.5`, concentration mark `0.20` (printed, not a pass rule), 25 bins of width `0.08` on `[0, 2]`, grids `9, 33, 129, 513`, step factor `1.25` and overall factor `8`, scan step `1e-4`, cost tie `1e-12`, slope tie `1e-15`, 17 starts `(π/2)(k/16)^2`, 21 probes `2(i/20)^2`, perturbations `±0.05` and `±0.1`, survival within two grid steps, peak-count band `{1, 2, 3, 4}`, agreement gap `1`, corner distance `0.08`. No later commit moves any of them. The scorer adds `1e-15` of comparison slack on the shrink tests and the neighbor-factor test. That slack is smaller than the reported margins (widest smooth width `2.94e-4` against `5e-3`; robustness max `0.094724` against `0.10`).

## Independent recomputation

Closed form against the four-point ensemble, on the eight G-form angles: maximum gap `5.551e-17`.

At `φ = 0`, `s = 1`: `q_eq = 1 - r^2 = 0.640000000000000`. `q_ptr = 0.688377871167984`, equal to `1 - 1/w*` with `w* = ln((1+r)/(1-r)) / (2 r^3) = 3.209014724815`. The gap to the printed target `0.688377871168` is about `1.6e-14`, inside the locked `1e-9`.

Smooth widths. The classifier marks 22 cells smooth, 23 corner, and 1 tie-point. All 22 smooth cells meet the three shrink lines. The maximum width on the 513-grid is `2.940972e-04`, at the smooth cell `u = 0.7`, `φ = 0`, `s = 2`, installed `θ = 0.794602`. That is the `2.941e-4` figure.

Equator at `φ = 0`, `s = 1`, `θ = π/2`. The 513-grid rationalizing set is `[0, 0.640000203300]`. The four widths are `6.408247e-01`, `6.400520e-01`, `6.400033e-01`, `6.400002e-01`. The analytic cone is `[0, 0.64]`. The excess over `0.64` is `2.033e-07`. The six-decimal statement `[0, 0.640000]` is that upper end.

T79 pin, target `θ = 1.075559`, `φ = 0`, `s = 2`. The 513-grid installs `θ = 1.0768545131`. Widths `1.632027e-02`, `3.682085e-03`, `9.216740e-04`, `2.315009e-04`. The set is `[0.2997425278, 0.2999740287]`. The midpoint is `0.2998582782`, which is the reported `0.299858`. The closed-form multiplier at the installed angle is `0.2998580170`. A central difference of `-A'/B'` at the same angle is `0.2998580176`.

Multiplier match. Differentiating the closed form gives

`λ(u) = 1 - s (2 r^3 cos²φ · u) / ln((1+ru)/(1-ru))`,

with the endpoint limits `q_eq` and `q_ptr`. On the smooth cells the midpoint sits on this `λ`. The largest smooth gap in the stored lines is `3.514546e-07` (the pin gap is `2.612351e-07`, the cap gaps at most `1.458799e-07`, the nine equator gaps at most `4.065995e-07`, the nine pointer gaps at most `5.169751e-07`). The finite-difference residual of the formula, over the smooth midpoints, is at most `3.512e-07`. The scored maximum `9.622730e-05` is the coarse equator cell: a direct scan at step `1e-4` against the three-point crossing, not the smooth residual. The flat tie is the point `{1}`.

The three weightings reproduce the stored histograms to the printed six decimals.

- Equal weight on the 46 sets. Peaks in bins 8 and 10, masses `0.148430` and `0.146252`. Diffuse. Heaviest bin `0.148430`.
- Dynamics. Peaks in bins 3, 8, and 10, masses `0.108696`, `0.217391`, and `0.260870`. Concentrated. Heaviest bin `0.260870`.
- Robustness. No peak. Heaviest bin, bin 24, mass `0.094724`, under the floor `0.10`.

Agreed medians: none. `P4a` and `P4b` pass the count band. `P4c`, `P4-agree`, and `P4-corner` fail. That is the `FAILS 3`.

## Attacks tried

### (a) Is P1–P3 a tautology?

On a one-dimensional menu the set of `q` for which a fixed interior angle minimizes `A + q B` is the interval between the chord slopes to the other actions. Under refinement that interval shrinks to `-A'/B'` wherever `B` is strictly monotone and `A` is smooth. At an endpoint the same crossing arithmetic is the one-sided normal cone, cut by the report window `[0, 2]`. Both statements are the envelope theorem, or the KKT condition for `min A` at a fixed disturbance, in one variable.

On this closed form they are identities, not a discovery. `dB/du = -(r/4) ln((1+ru)/(1-ru))` is strictly negative on `(0, 1)`, so `B` increases from the pointer to the equator. For every locked `(φ, s)`, `λ(u) ≥ q_eq ≥ 0.28 > 0`. Sampling `dA/dθ` at 399 interior angles on each of the ten locked pairs gave 399 negative slopes and 0 positive slopes. There is no interior kink for the classifier to miss. A smooth cell on this menu cannot keep a width above `5e-3` on a 513-point grid, and a corner cell cannot be narrow, except by an arithmetic error. The run did not make an arithmetic error. The pass is the discrete set tracking the derivative.

The cap cells do not add a second object. The rationalizing set is a property of the installed angle and the menu. A cap `P_D ≤ D` only chooses the angle. An interior angle chosen that way has the same singleton structure as any other interior angle. The lock says so, and the three cap rows are three more interior points (`θ` about `0.457`, `0.786`, and `1.132`).

What H-corner adds, beyond restating that fact, is a sorting of this menu and a reading of the T79 table. The sorting is: interior and not flat, endpoint, flat interior, or one of the three coarse actions. The reading is that the wide T79 rows are the endpoint cones of this menu, and that the displayed singleton `{0.30}` is the interior multiplier near `0.299858` rather than the parent value `0.6`. That reading is numerical bookkeeping on a menu the repository already had. It does not select a value of the ratio inside a cone, and it does not constrain any menu whose disturbance is non-monotone or whose cost has an interior kink. For the theory, the content is the narrow sentence: on this antipodal menu, an interval of ratios is the normal cone at an endpoint, and a smooth interior angle does not leave one. That sentence is the envelope theorem applied here. It is not a new identification, and the secondary weighting does not replace it with one.

The parent stdout supports the bookkeeping and is wider than the memo's sentence. Of 171 `PAIR` rows in `bicausal_checks.out`: 72 are `[0, 0.640000]` at the equator, 24 are `[0, 0.820000]` at the equator, 6 are `[0, 0.280000]` at the equator, 26 are `[0.700000, 2]` at the pointer, 9 are `[0.380000, 2]` at the pointer, 8 are `[0.860000, 2]` at the pointer, 24 are `[0, 2]` at the pointer with stake 10 (the pointer multiplier is negative there, and the window fills the cone), and 2 are the pin `[0.300000, 0.300000]` at `θ = 1.075559`. No other shape appears. The equator rows match `1 - s r^2` at `s ∈ {0.5, 1, 2}` and `φ = 0`. The pointer rows are the other cone. T80 refines the pin and recomputes both cones on its own grid. It does not re-solve the two-level game.

### (b) Was the classifier fixed before the run?

Yes, as far as the git objects go. Section 2 of the lock defines `corner`, `tie-point`, and `smooth` from the installed angle and the menu: an endpoint, a coarse action, or `|cos φ| ≤ 1e-12` in the interior. The rule does not read the width. The same text is the blob that the sha256 locks, and the scorer does not exist in that commit. `mark_of` implements that rule. The reclass count is 0: all 46 expected marks match. The classifier was not fitted to the T80 widths.

It was written after the T79 stdout, and the opening of the lock describes the pattern that stdout already shows (wide sets at the ends, one near-point in the interior). That is a confirmatory design, and the lock says so. The 11 minutes between the lock timestamp and the result timestamp do not contain another commit. Git cannot show an uncommitted pilot, and it cannot rule one out.

The coarse middle action is an interior angle of a three-point menu. The lock calls all three coarse actions corners. That stipulation is in the lock. The middle width is `0.024149`, above the bar `0.01`. The bar was not moved after the stored run. The width itself is fixed by three closed-form points and does not need the 513-grid.

### (c) Are the ensemble schemes assumption-independent, and were they tuned after T79 or from 0.6?

They are in the lock, and the result commit does not change the lock. They were written with the T79 table already in the parent, which the lock cites (the angle `1.075559`, the displayed singleton, the equator-end formula). The width `1.65e-4` is not a bin width, a floor, or a weight. No probe equals `0.6`. The probe mean is `0.683333`. The scorer has no standalone literal `0.6`; the Bloch length arrives as `base.R` inside the cost and the multiplier. It is not a histogram center, a target, or a weight.

The three schemes are not three assumption-free readings of one object.

Equal weight is the uniform measure on each rationalizing set, summed over the 46 cells. This one does read `R`. Its two peaks are real properties of that measure. They are diffuse, and the heaviest mass is `0.148430`.

Dynamics does not read `R`. It descends on `C = I + s L`, then records `q_eq` at an equator landing, `q_ptr` at a pointer landing, and `λ` otherwise. Because `A` is strictly decreasing in `θ` on every locked pair, every trajectory ends at the equator. All 782 landings (46 cells, 17 starts) are the equator end. There are 0 splits, so `G-dyn` cannot fail on this menu. The recorded prices are nine copies of `q_eq(φ, s)`, with multiplicity equal to the number of cells at that pair. Bins 3, 8, and 10 are the heavy values of that list (`0.28`, `0.64`, and the cluster near `0.82`). Calling those peaks corner values restates the definition of the recorded price. The scheme assumes the multiplier formulas it then finds.

Robustness does not read `R` either. It histograms the probe coordinate, with Voronoi weight times survival of the argmin under `(φ, s)` perturbations. Survival is `9/9` on 199 of the 210 pair-probe cells. If survival is identically 1, the normalized histogram is the probe measure alone, and its heaviest bin is bin 24 at `0.092857`, already under `0.10`. The menu moves that mass to `0.094724`. The failure of `P4c` is available from the locked probe list before any cell is scored. The end-probe weights are the full neighbor gap, and the interior weights are half the two-neighbor span; the weights sum to `2.1` rather than to the length of `[0, 2]`. Normalization removes the scale. The lock's wording matches that end rule.

So: not fitted to the T79 width, and not centered on `0.6`. Also not independent of the hypothesis, in the dynamics case, and not a probe of the rationalizing set, in the robustness case. The equal-weight histogram is the one scheme that weighs `R`.

### (d) Return channel, time symmetry, asymmetric starts

The scorer imports the closed form and the ensemble functional. It has no delay, no parent cost, no reverse-rate table, and no second channel. The 17 starts are present: `θ = (π/2) (k/16)^2` for `k = 0, …, 16`. The only mirror pairs about `π/4` are the two endpoints, `0` and `π/2`. None of the 15 interior starts has its mirror in the list. There is no time-symmetric rate table.

### (e) Classical-record assumptions

The inherited menu is a classical binary record of a qubit measurement. `I` is the Shannon information of the two-outcome Born probability, `P_D` is that binary entropy minus the qubit entropy, and `L` is the mean squared error of a classical conditional mean. The lock cites that closed form. The scorer adds no further classical ledger, no return share, and no extra binary channel. The lock's phrase "no binary-entropy channel" is the absence of a parent channel. The cost itself is built from binary entropy. That is the menu, and it is cited. It is not a hidden extra assumption in the scorer.

### (f) Banned wording

Searched the ten-file diff, including the added `OPEN_WORK.md` row and the added `theory/README.md` row.

| Term | Count |
|---|---|
| theory of everything | 0 |
| solved | 0 |
| bill | 0 |
| kill | 0 |
| verdict | 0 |
| `law` as a word | 3 lines, each the hypothesis sentence: `PREREG.md:5`, `MEMO.md:5`, `tools/test_corner_checks.py:12`. The added `OPEN_WORK.md` and `theory/README.md` lines have none. |
| general relativity, quantum mechanics, holography, gravity | Denial sentences only: `PREREG.md:7`, `PREREG.md:174`, `MEMO.md:7`, and the added `OPEN_WORK.md` row. The added README row has none. No sentence claims a derivation of any of them. |

### (g) DOI

No DOI, and no `10.` identifier, appears in the ten-file diff. There is nothing to look up on Crossref.

## Findings

### BLOCKING

None.

### HIGH

1. P1–P3 restate the one-dimensional envelope theorem on a menu where `B` is strictly monotone and `λ` stays at least `0.28`. The pass is a correct discretization check. It is not a new identification, and the cap rows do not test a different object. The content that is about T79 is a reading of an existing table: the wide rows are endpoint cones, and the singleton refines to `0.299858`, which is `λ` at that angle and is not `0.6`. That reading does not select a ratio. The memo's sentence that the wide T79 sets are the equator cone covers 102 of the 171 pair rows. Another 67 are pointer cones, including 24 copies of the full window `[0, 2]` at stake 10. The remaining 2 are the pin.

2. Two of the three schemes do not weigh the rationalizing set, and one of them cannot fail. Dynamics records `q_eq` on all 782 landings, because `A` is strictly decreasing in `θ`. Its peaks are the cell-list histogram of `q_eq`. `G-dyn` passes because a split is impossible on this closed form. Robustness histograms the probe coordinate. With flat survival its heaviest bin is `0.092857`, under the floor `0.10`; the scored mass is `0.094724`. The `P4c` failure is a property of the locked probe grid. Equal weight is the scheme that weighs `R`, and it does not share a peak with a scheme that has no peak. The reported `FAILS 3` is the right call for the locked rules. It is not evidence that three independent weightings disagree about a corner.

### MEDIUM

1. The scored P3 maximum, `9.622730e-05`, is the coarse equator scan against its own crossing endpoints. The smooth, pin, cap, equator, and pointer residuals are at most `5.17e-07`. On the coarse menu the pointer chord starts at `0.675446` against the fine-grid `q_ptr = 0.688378` (gap `0.01293`), and the coarse equator ends at `0.651296` against `0.64` (gap `0.01130`). The lock scores the scan for coarse cells, and that scan passes. The headline gap is not the KKT residual.

2. The memo says robustness survival dips to `1/3` at one probe when `s = 2`. There is a `3/9` cell at `φ = 0`, `s = 2`, `q = 0.32`. The minimum is `2/9`, at `φ = π/6`, `s = 2`, `q = 0.5`. The stored histogram is unaffected.

### LOW

1. The shrink tests and the peak-factor test add `1e-15` of slack that the lock does not write down. The slack does not change a call.
2. The eleven minutes between the lock and the result leave room for an uncommitted pilot. The committed classifier does not read the width, and the preregistration blob is unchanged.
3. Robustness end weights sum to `2.1`. The lock describes that end rule, and normalization removes the scale.

Blockers remaining: 0
