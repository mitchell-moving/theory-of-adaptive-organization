# Independent review of the lossless island scan (T82e)

*24 November 2026 (ET). Reviewed head `733d78412f8ef20ca9f59b3fde993f1dd1ff845b` on `forge-torus-memory`, fork PR #16. Lock `f8acadca455884ecde55bb97b392a4dc6e786326`. `PREREG_T82E.md` sha256 `748514c79a5dd1d3393614207f9c0a814f1a49969da453bdf5af4fe37bbb4421`. This review is a new branch. It does not edit `forge-torus-memory`, `THEORY.md`, or `CORE.md`. Wording follows upstream `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at `652d936` (the merge of `2ec1858`; that file is not on fork `main`).*

The four misses recompute. Under `PREREG_T82E.md:90` the split of the `1/1` set is a miss. The signed count excesses are `+3` and `+8`. The frequency residual the lock names is formed only at coupling `0.01`, where it is `+0.002157287525`. The split sits inside one separatrix interval of an integrable pendulum. The samples that open the gaps librate and have an endpoint rotation number within `0.002` of `1`, and the Poincaré ratio differs from that endpoint ratio by more than `10^{-3}`.

## Lock

`f8acadc` (2026-11-24 22:01:15 UTC) is the parent of `733d784` (22:16:43 UTC). The lock commit adds three files: `PREREG_T82E.md`, `PREREG_T82E.sha256`, and a seven-line `RUN_LOG_T82E.md` that says the scored script has not been run. It contains no orbit output, no scoreboard, and no scan script. The sha256 of the locked file is the hash above. No later commit edits the preregistration. The score commit appends the ledger and leaves the stub paragraph in place (`git diff f8acadc 733d784` on `RUN_LOG_T82E.md` is insertions only).

`PREREG_T82E.md:5` is "Why this approach". `PREREG_T82E.md:9` is "Can it fail", and line 13 is the cheapest orbit: coupling `0.04`, bare frequency `1`, step `0.05`, `40000` steps, start `(0, π)`, actions `0`. That orbit has endpoint rotation number `1.000000000000`. The cheap miss does not fire. The width row misses by the plateau count.

## Recompute

`theory/reviews/REVIEW_T82E_checks/scan.py` integrates

`H = ω·I + (β/2)|I|² + ε cos(θ1−θ2)`, `β = 0.25`,

with a kick-drift-kick step written from those equations. It does not import the scoreboard. A second pass uses RK4. Time, step, grid, tolerance, and the island rule are the lock's.

Predicted full widths, `W(ε) = 2√2 √ε`:

| Coupling | `W(ε)` |
|---|---|
| `0.01` | `0.282842712475` |
| `0.04` | `0.565685424949` |
| `0.09` | `0.848528137424` |

The reduction is exact. With `ψ = θ1−θ2` and `J = I1−I2`, `ψ̈ = 2βε sin ψ`. Shift the center `ψ = π` to `φ`. Then `φ̈ = −(2βε) sin φ`. Started from `J = 0` at the center, the orbit stays inside the separatrix when `|ω1−ω2| < 2√(2βε)`. At `β = 0.25` the full width in `ω2` is `2√2 √ε`.

Plateaus of the `1/1` rule match `t82e_checks.out`:

| Coupling | Plateaus | Ends | Width |
|---|---|---|---|
| `0` | `0` (near-`1` count `1`) | | |
| `0.01` | `1` | `0.860`–`1.140` | `0.285000000000` |
| `0.04` | `4` | `0.725`–`0.740`, `0.755`–`0.765`, `0.775`–`1.225`, `1.235`–`1.275` | `0.020`, `0.015`, `0.455`, `0.045` |
| `0.09` | `9` | as in `t82e_checks.out:11-19` | longest `0.455` |
| `0.04`, fine | `4` | `0.730`–`0.735`, `0.780`–`1.2275`, `1.2325`–`1.260`, `1.265`–`1.2775` | `0.0075`, `0.450`, `0.030`, `0.015` |

Plateau counts for denominators `2` through `5`: `0`, `0`, `0`. Null baseline: `11` reduced rationals `p/q` with `q ≤ 5` in `[0.5, 1.5]`, and `11` of `201` grid values lie within `0.002` of one of them. Fraction `11/201 = 0.054726368159`.

## The split under line 90

`PREREG_T82E.md:90` requires one `1/1` plateau at each positive coupling, containing `ω2 = 1`, with width inside `30` percent. It misses if any coupling has no such plateau. Four plateaus and nine plateaus are not one plateau. The row is a miss. `P-scale`, `P-record`, and `P-refine` miss because the unique width they need is not formed (`PREREG_T82E.md:92`, `:98`, `:100`).

The gaps are inside the separatrix. A grid point is analytically trapped when `|1−ω2| < 2√(2βε)`. Every sample the island rule accepts is trapped. The samples that break the plateau are trapped, librate, and have endpoint `|ν−1| ≤ 0.002`, and the two rotation numbers differ by more than `10^{-3}`, so the lock marks them `OTHER`.

| Coupling | Trapped | On the island rule | Inside and off | Outside and on | Off reason |
|---|---|---|---|---|---|
| `0.01` | `57` | `57` | `0` | `0` | |
| `0.04` | `113` | `107` | `6` | `0` | all `OTHER` |
| `0.09` | `169` | `145` | `24` | `0` | all `OTHER` |
| `0.04` fine | `227` | `214` | `13` | `0` | all `OTHER` |

At `ω2 = 0.720` and coupling `0.04`, the endpoint ratio is `0.998948377806` and the section ratio is `1.000624755822`. The difference is `0.001676378016`. Both sit within `0.002` of `1`. The sample librates. The `10^{-3}` bar is what removes it.

The separatrix interval on the coarse grid, last trapped point minus first plus one step, is `0.565000000000` at coupling `0.04` (signed `−0.000685424949` against `0.565685424949`, relative `0.001211671574`) and `0.845000000000` at coupling `0.09` (signed `−0.003528137424`, relative `0.004157949829`). Both sit inside the `30` percent band. That interval is one run. It is not the locked statistic. The locked statistic is the plateau of the island rule, and that plateau is not unique.

RK4 at step `0.05` on the coupling-`0.04` grid agrees with the Verlet endpoint ratio to `0.000011826720`, and the libration flags agree. Dropping the section test leaves one run, `0.720`–`1.280`, width `0.565000000000`, the separatrix interval. Halving the step on the fine grid leaves four plateaus. The island is `57` to `169` grid steps wide, so the grid resolves it.

The Hamiltonian depends on the angles only through `θ1−θ2`, so the reduced flow is integrable. The extra plateaus are still labeled `1/1`. Denominators `2` through `5` contribute no plateau. Secondary resonances, a chaotic layer, and a grid that is coarser than the island do not account for the gaps. The location is the locked section test.

## Signed sizes

`P-width` at coupling `0.01`: measured `0.285000000000` minus `0.282842712475` is `+0.002157287525`, relative `0.007627163191`, inside `30` percent. The ledger's figure matches.

At couplings `0.04` and `0.09` the lock's signed size is `W_meas − W(ε)`, and `W_meas` is not a single width. The ledger says so and reports the count excess, `4−1 = +3` and `9−1 = +8`. Those counts match the recompute. The longest run is a sensitivity, not a rescore: width `0.455000000000`, signed `−0.110685424949` at `0.04` (relative `0.195666036400`, inside `30` percent) and `−0.393528137424` at `0.09` (relative `0.463777357600`, outside `30` percent). Uniqueness already misses both.

`P-scale`: the ratio minus `2` is undefined, which is the miss line 92 names when either width is undefined. The longest-run ratio `0.455/0.285 = 1.596491228070` lies in `[1.4, 2.6]` (signed `−0.403508771930` against `2`). The linear rival `4` is outside that interval. The ledger does not form this ratio. That is what the lock requires.

`P-refine`: `+3` fine plateaus (`4−1`). The width difference is not formed. The fine longest width `0.450` against the coarse longest width `0.455` is a sensitivity, relative about `0.011`, and it is not the locked comparison.

`P-record`: the exterior pair is not defined, so the gap minus `0.002` is not formed. Count of blocks is `4`.

`P-higher`: count residual `0` at each positive coupling.

`P-eps0`: count `1`, and the lock's margin is `1` minus the count, which is `0`. The ledger's signed size `0` matches that margin. At zero coupling the force vanishes, the step advances each angle by `h ω`, and `ν = ω2`. On a grid of step `0.005` only `ω2 = 1` lies within `0.002` of `1`. The count is an identity of the free rotation and the grid. Information is zero. This review classifies the row `NOT A TEST`. The lock's own sentence calls a count of `0` or `1` a hit, and the ledger follows that sentence. The classification here does not edit the lock.

## Location

Every T82e row is `model`. No `MV1`–`MV8` gate was declared. The independent step reproduces the scoreboard, so there is no reproducible disagreement with the lock to place in `measurement/code`. The section bar is part of the locked island rule. Placing the split in `model` follows the anti-rescue guardrail in `process/PROCESS.md`.

## Attacks tried

1. Rebuild the step from the Hamiltonian and compare every plateau, the higher-denominator counts, the null fraction, and the fine grid with `t82e_checks.out`. They match.
2. Compare Verlet with RK4 on the coupling-`0.04` grid. Endpoint ratios agree to `1.2×10^{-5}`. The split remains when the step is halved.
3. Mark each grid point by the separatrix inequality. The gaps are trapped samples the section test rejects. No accepted sample lies outside the separatrix.
4. Ask whether a longer contiguous run would have hit the width band and the scaling interval. At `0.04` the longest run is inside `30` percent and the longest-run ratio is inside `[1.4, 2.6]`. At `0.09` the longest run is outside `30` percent. The separatrix interval on the grid is inside `30` percent at both couplings. None of these replacements is the locked statistic, and the ledger does not use them.
5. Ask whether the cost bar can miss when a unique plateau exists. At coupling `0.01`, where there is one plateau, the absolute gap is `0.000001212497`, signed `−0.001998787503` against `0.002`. Information plus destruction is independent of `θ2` in the locked formula, and `θ2` still winds, so the averaged record is flat. The lock scores the cost only at coupling `0.04`, where the plateau is missing. On the longest `0.04` run the counterfactual gap is `0.000003503696`. The shelf does not read this record as a resonance detector (`PREREG_T82E.md:23`).
6. Ask whether the cheap center orbit could have been the whole test. It passes, and the width row still misses. The cheap orbit is a sufficient way to miss the center. The lock also requires one plateau.
7. Rivals named in the lock: the circle-map width linear in `ε`, ratio `4`, outside `[1.4, 2.6]`; a second harmonic, predicted plateau count `0`. The ratio was not formed, so the linear rival did not win. The higher-denominator count is `0`.

The miss is not circular. Line 90 was locked before the orbits, and the score applies it. The update shelves the resonance thread on this toy (`PREREG_T82E.md:17`), which is the sentence the lock attaches to a miss of the width or of the scaling.

## Ledger

Reviewed against the appended rows in `RUN_LOG_T82E.md`. Eight fields. Breach check: the lock hash matches and the preregistration is unedited.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82e-P-width | One 1/1 plateau at each of 0.01, 0.04, 0.09, containing omega_2=1, width within 30 percent of 0.282842712475, 0.565685424949, 0.848528137424. Null probability of a false three-point plateau is 0. | One plateau, width 0.285000000000, at 0.01. Four plateaus at 0.04. Nine at 0.09. | Miss. Width residual +0.002157287525 at 0.01. Count excess +3 at 0.04 and +8 at 0.09. The single width residual is unformed at 0.04 and 0.09. | model | high | Shelf matches PREREG_T82E.md:17. No edit to the lock. | none |
| T82e-P-scale | W(0.04)/W(0.01) in [1.4, 2.6], center 2. Linear rival 4 lies outside. | The 0.04 width is not one plateau. | Miss. The ratio minus 2 is undefined. | model | high | Same shelf. | none |
| T82e-P-higher | Plateau count 0 for denominators 2, 3, 4, 5 at each positive coupling. | Counts 0, 0, 0. | HIT. Count residual 0. The extra plateaus are at 1/1. | model | low | none yet | none |
| T82e-P-eps0 | At coupling 0, the number of grid values with rotation number within 0.002 of 1 is at most 1. Margin is 1 minus the count. | Count 1. | NOT A TEST. Signed margin 0. Identity of the free rotation on this grid. | model | low | none yet | none |
| T82e-P-record | Absolute cost gap at least 0.002 at coupling 0.04, stake 2, against the first samples outside the one 1/1 plateau. | The gap is not formed. | Miss. Exterior pair undefined. Block count 4. | model | medium | The cost is not read as a resonance detector. | none |
| T82e-P-refine | At coupling 0.04, one fine 1/1 plateau contains omega_2=1 and its width is within 30 percent of the coarse width. | Four fine plateaus. | Miss. +3 fine plateaus. The width difference is unformed. | model | medium | The finer grid keeps the split. No edit to the lock. | none |

## Strong-resonance row

`RUN_LOG_RESONANCE.md:46`, appended in `8963569`. The diff from `46f8bdc` to `8963569` is `37` insertions and `0` deletions, and no later commit edits the file. The row has the eight fields. Odds were not locked. Signed size `+3` islands (`4` against `1`) matches the four blocks already in the `T82d-P-band` row. Alignment gaps `−0.032130`, `+0.004887`, `−0.014474` repeat the figures in that ledger, inside the stated look-elsewhere probability `0.449`. Location `model (discretization)` keeps the bucket `model`. The parenthetical names the integer width floor, which the lock includes. No `MV` gate was declared, and the row does not place the miss in `measurement/code`. The update sends the next look to T82e and makes no resonance claim from T82d. Breach check `none`.

## Crossref

Queried 24 November 2026 against `api.crossref.org`. All seven DOIs in the torus-memory notes resolve. The claims in `PREREG.md:71-76` and `MEMO.md:90` match the records.

| DOI | Record |
|---|---|
| `10.1007/BFb0013365` | Kuramoto, "Self-entrainment of a population of coupled non-linear oscillators," pages 420–422. Issued field empty. Part of `10.1007/BFb0013294`. |
| `10.1007/BFb0013294` | International Symposium on Mathematical Problems in Theoretical Physics, issued 1975. |
| `10.1007/978-3-642-69689-3` | Kuramoto, *Chemical Oscillations, Waves, and Turbulence*, Springer Series in Synergetics, issued 1984. |
| `10.1016/S0167-2789(00)00094-4` | Strogatz, Physica D 143, pages 1–20, issued 2000. |
| `10.1103/RevModPhys.77.137` | Acebrón, Bonilla, Pérez Vicente, Ritort, and Spigler, Reviews of Modern Physics 77, pages 137–185, issued 2005. |
| `10.1007/978-3-642-01742-1_10` | "Small denominators. I. Mapping of the circumference onto itself," Collected Works, pages 152–223, issued 2009. Author list empty. No 1961 DOI is cited. |
| `10.1016/0005-1098(76)90006-6` | Francis and Wonham, "The internal model principle of control theory," Automatica 12, pages 457–465, issued 1976. |

## Checks

`python3 tools/check_consistency.py`: wording FAILs 0, `RESULT: PASS`. `python3 -m pytest -q`: 296 passed, 1 skipped. Fork `main` is `d2aeb8100e22870dc5aee2529356de970c82a820`. Upstream `main` is `652d936`, which adds `process/PROCESS.md`. That gap is pre-existing. `python3 tools/check_fresh.py` reports `RESULT: PASS`: `STATUS.md` points at `31aa997`, and the window of fork `origin/main` is `d2aeb81 31aa997 8c48a5b 04e9e5b 0e22302`. The freshness script does not record the upstream gap, because `31aa997` is still inside those five commits.

Blockers remaining: 0
