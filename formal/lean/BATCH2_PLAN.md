# Batch 2 plan

Written before any proof in this batch. The parent is `forge-lean-batch1`
at `d12642b`. This file is not revised in place. Later notes are
appended at the bottom.

Scope is the heat and repair floors in OPEN_WORK T59, T60, and T63.
Nothing here is a claim about a real system. `THEORY.md` and `CORE.md`
are not edited. The cooperative-media gap in dimensions 2 and 3, the
repetition-code table, and a closed form of `Φ_X` for a general
irreducible kernel are not targets. They are recorded as gaps below.

## Statement list

Each row is one declaration family. "Paper" is the sentence being
checked. The Lean name is the one this batch will use.

### T59, two-state JP-heat floor

Source: `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `errorDot`, `steadyEps`, `steadyMu`, `steady_dot_zero`, `steady_mu_of_eps` | lines 45–57 | `errorDot r Γ μ ε = (r+Γ)(1-ε) - ε(r+Γ+μ)`. For `ε ∈ (0,1/2]`, `r,Γ ≥ 0`, not both rates zero when `ε < 1/2`, the unique steady drive is `μ = (r+Γ)(1-2ε)/ε`, and that drive makes the dot zero. |
| `L`, `L_nonneg`, `L_zero_at_half`, `L_pos`, `L_one_fifth` | line 62, and the number at line 144 | `L ε = (1-2ε) log((1-ε)/ε)` on `(0,1/2]`. It is nonnegative, zero only at `1/2`, and positive below `1/2`. `L(1/5) = (3/5) log 4`. The printed decimal `0.831776616672` is not an equality. |
| `binaryEntropy`, `destroyDeriv` | lines 59–65 | For a fair bit, `I(ε) = log 2 - h(ε)` has derivative `-log((1-ε)/ε)`. Along `ε̇ = (r+Γ)(1-2ε)` the derivative of `I` is `-(r+Γ) L(ε)`. This is the transient identity. It is not the JP-heat flow. |
| `copyBracket`, `iAltTwoState`, `bracket_eq_world`, `iAlt_eq_rate_L` | lines 73–82 | With forward flux `ε(Γ+μ)` and back flux `(1-ε)Γ`, `I_alt = (forward - back) log((1-ε)/ε)`. At the steady drive the bracket equals `r(1-2ε)`, so `I_alt = r L(ε)`. `Γ` cancels. |
| `edgeEntropy`, `edgeEntropy_nonneg`, `memoryHeat`, `jp_heat_floor` | lines 19–23 and 70 and 82–85 | The one-edge entropy production `(a-b) log(a/b)` is nonnegative and zero iff `a = b`. Defining `Q̇ = kT (σ + I_alt)` gives `Q̇ ≥ kT I_alt` and, at steady state, `Q̇ ≥ kT r L(ε)`. |
| `frozen_flux_balance`, `frozen_heat_zero` | line 85, and item 1 at lines 15–16 | At `r = 0` the two fluxes match, `σ = 0`, `I_alt = 0`, and `Q̇ = 0` at every `ε ∈ (0,1/2]`. |
| `kramersRate`, `floor_independent_of_barrier` | lines 38–41 and 103, and item 2 at line 16 | `Γ = ν exp(-ΔE/kT)` for `ν > 0`, `kT > 0`, `ΔE ≥ 0`. The steady floor `kT r L(ε)` does not depend on `Γ` or `ΔE`. The survival probability of a metastable well is not derived. |
| `barrierWork`, `barrierWork_zero`, `barrierWork_pos` | line 156, and the display at lines 109–111 | `χ ΔE (r + ν exp(-ΔE/kT)) (1-2ε)` is zero at `ΔE = 0` and strictly positive for `ΔE > 0` when `χ = 1`, `ν > 0`, `r ≥ 0`, and `ε < 1/2`. |
| `copyCapEps`, `copy_cap_near_half` | line 158 | If `0 ≤ μ ≤ c Γ` with `c ≥ 0` and `r > 0`, then `ε ≥ (r+Γ)/(2r+(2+c)Γ)`, which tends to `1/2` as `Γ → 0`. |

Proposition JP-heat for a general bipartite generator is not re-proved.
The two-state decomposition `Q̇ = kT (σ + I_alt)` is the hypothesis that
plays that role, and `σ` is the one edge. A multi-edge memory is T60.

### T60, finite-state learning rate

Source: `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `kl`, `kl_nonneg`, `kl_zero_iff` | the sum inside lines 17–19 | On a finite alphabet, with the usual `0 log 0 = 0` convention, `D_KL` is nonnegative. It is zero iff the vectors agree wherever the first is positive, and infinite when the first is not absolutely continuous with respect to the second. |
| `worldFlow`, `fluxBalance`, `destruction_identity` | lines 89–93 | For a bipartite exogenous world, `I^X` expands into `Σ π W log(π'/π) - Σ π W D_KL`. Stationarity (`Σ_y π(x) W(x→y) = Σ_y π(y) W(y→x)`) kills the first sum, so `I_alt = -I^X` equals `Σ π(x) W(x→x') D_KL(p(·\|x) ‖ p(·\|x'))`. |
| `iAlt_nonneg`, `iAlt_zero_iff_edge` | line 97, first sentence | The sum is nonnegative. It vanishes iff `D_KL = 0` on every edge with `π(x) W(x→x') > 0`. |
| `bayesError`, `chanceError`, `bayes_of_constant` | lines 41–45 and 97 | `ε = 1 - Σ_m max_x π(x,m)` and `ε_0 = 1 - max_x π(x)`. If `p(M\|x)` is the same on the support of `π`, then `ε = ε_0`. |
| `iAlt_zero_stronglyConnected` | line 97 | If the occupied flux graph is strongly connected on `{π > 0}`, then `I_alt = 0` implies `ε = ε_0`. |
| `two_class_counterexample` | line 99 | States `{0,1,2}`, `π = (3/10, 3/10, 2/5)`, rate `1` each way on `{0,1}`, state `2` isolated. A class indicator has `I_alt = 0`, `ε = 3/10`, `ε_0 = 3/5`. The world rate is not identically zero. The printed `0.312590` is the script's soft memory and is not an equality. |
| `telegraph_floor`, `telegraph_symmetric_eq` | lines 107–113 | For the fair telegraph of rate `r > 0` and any finite positive memory, `I_alt ≥ r L(ε)`, with `ε = (1 - TV)/2`. Equality at the symmetric binary copy. |
| `telegraph_zero_iff` | line 21 and line 97, last sentence | On that telegraph, `I_alt = 0` iff `ε = 1/2`. |
| `converse_fails_three` | line 21 and line 97 | A stationary 3-cycle with `π = (1/2, 1/4, 1/4)` and a full-support memory that separates the two non-mode states has `ε = ε_0` and `I_alt > 0`. |
| `frozen_support` | line 103 | If every occupied flux is zero, `I_alt = 0`. The static copy `1/(1+exp 1)` is strictly below `1/2`. |
| `pairwise_L` | line 115 | If `ε < min(π(i), π(j))` and both directed fluxes are positive, `I_alt ≥ min(j_ij, j_ji) · 2 L(ε / (2 min(π(i), π(j))))`. |
| `path_pinsker`, `telegraph_K` | lines 117–129 | On a strongly connected occupied flux graph, with a chosen directed path from each occupied state to a mode, `I_alt ≥ (ε_0 - ε)^2 / K_X` with `K_X` computed from `π` and the fluxes only. On the fair telegraph, `K_X = 1/(4r)`. |

`Q̇_M ≥ kT I_alt` for a general memory stays a hypothesis
(`jp_heat_compose`, lines 53 and 133–136). Composing it with the
telegraph bound gives `Q̇_M ≥ kT r L(ε)`. A closed form of `Φ_X` for a
general kernel is open in the note (line 129) and is not stated.

### T63, repair floor

Source: `theory/RECORD_REPAIR_FLOOR_2026-11-23.md`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `L_ge_four_entropy` | line 73 | For `ε ∈ (0,1/2]`, `L(ε) ≥ 4 (log 2 - h(ε))`, with equality only in the limit `ε → 1/2`. |
| `oneCarrierSigma` | lines 73 and 85 | For one carrier with mass `ε` on the wrong state, `σ_Γ = Γ L(ε)`. |
| `decoderMass` | line 77 | `D(p_0‖u) + D(p_1‖u) ≥ 2 (log 2 - h(ε))` once each decoded error is at most `ε`, by the binary divergence of the decoder masses. |
| `repairFloor` | lines 79–85 | If the horizon average of dissipated power satisfies `Q̄ ≥ (kT/τ) ∫ σ - kT S_max/τ` and the bit-averaged `σ` is at least `4 Γ (log 2 - h(ε))` at every time, then `Q̄ ≥ 4 kT Γ (log 2 - h(ε)) - kT S_max/τ`. |
| `oneCarrierFloor` | line 85 | The same packaging with `σ = Γ L(ε)` in place of the factor `4`. |
| `longHorizon` | line 85, "for long horizons the second term vanishes" | `S_max/τ → 0` as `τ → ∞`, so the liminf of the floor's right-hand side is the rate term. |
| `rf_forget_stationary` | line 89 | A state that does not depend on the vanished bit has the two decoded errors summing to `1`. For `ε < 1/2` they cannot both be `≤ ε`. |
| `rf_cap` | lines 124–128 | Given `N kT Γ g ≤ q A` and `g ≥ 4 (log 2 - h(ε))`, `N ≤ q A / (kT Γ g) ≤ q A / (4 kT Γ (log 2 - h(ε)))`. The shedding density `q` is an input. |

The integral comparison of dissipated power with `σ` is the
Schnakenberg budget in step 1 (lines 67–71). It is a hypothesis of
`repairFloor`, not a derivation from a general jump generator.

## Not proved in this batch

These are part of the notes and are gaps, not silent omissions.

- Metastable survival. `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md:16` and
  `:103` say a symmetric well holds a small error for a time of order
  `1/Γ`. No hitting-time bound is a target.
- The Kramers high-barrier derivation. Line 41 defines the rate that
  this batch uses. The 1940 argument is not a target.
- Ornstein–Uhlenbeck reduction at line 144. That identity is T38, which
  this batch does not start.
- A Landauer cost per irreversible reset. Line 105 leaves it open.
- The tiny-leak numerical value `0.00025706` at line 101. The
  counterexample that positivity needs a connected flux graph is the
  target. A uniform modulus "every leak of size `λ` costs at least `f(λ)`"
  is not.
- Repetition-code values at lines 97–101 of the repair note. They are
  marked numerical there.
- `ρ ≤ 2λ` for a reversible generator (`theory/RECORD_REPAIR_FLOOR_2026-11-23.md:87`).
  The spectral expansion is not a target. The modified-log-Sobolev
  packaging is stated only as the one-carrier and independent-carrier
  bound `4Γ`, which is what Proposition RF uses.
- Convergence to the unique stationary state (`:89`, "tends to `1/2`").
  The stationary obstruction is the target. The limit of a trajectory
  is a gap.
- Cooperative media in dimensions 2 and 3, and the quantum rows
  (`:107–116`). The inventory already says this loophole is part of the
  claim and is not formalized.
- Attainment of the repair floor (`:91`) and a closed form of `Φ_X`
  (`theory/GENERAL_FLOOR_FINITE_2026-11-23.md:129`). Both are open in
  the notes.

## Why this approach

The notes already split a thermodynamic budget from an information
bound. The formalization follows that split. T59's two-state arithmetic,
the cancellation of `Γ`, the frozen equilibrium, and the barrier work
are field operations and one derivative of `log`. T60's destruction
identity is the expansion of `Σ ρ W log(ρ'/ρ)` plus flux balance. The
telegraph bound is the log-sum inequality on the Bayes partition,
followed by the elementary minimum of the binary Jeffreys divergence at
fixed total variation. Path-Pinsker is Pinsker's inequality, the
triangle inequality for total variation, and Cauchy–Schwarz along one
chosen system of paths. T63's factor `4` is the comparison of `L` with
`4(log 2 - h)`, proved by differentiating twice. The decoder step is
the same binary divergence. The heat integrals stay hypotheses, in the
same way batch 1 kept Debreu's theorem as a hypothesis.

## Can it fail, and the cheapest repair

Can it fail: a zero atom makes `log(p/q)` undefined. The notes' sums use
the convention `0 log 0 = 0`, and a singular pair has infinite divergence.

Cheapest way: define the term by cases, and use `ℝ≥0∞` for a pair that
is not absolutely continuous. Do not replace the inequality by a
version that assumes every conditional is strictly positive, unless
that hypothesis is labeled and the singular case is a separate
statement. If the extended codomain will not typecheck, keep the
positive case, label it WEAKER, and append the singular goal here.

Can it fail: Pinsker's inequality is not a one-line lemma at this
Mathlib pin.

Cheapest way: prove `D_KL(p‖q) ≥ 2 TV(p,q)^2` for a finite alphabet from
the binary case and the log-sum inequality, or cite the Mathlib lemma
if its statement is exactly that. If neither closes, keep the telegraph
and pairwise `L` bounds, and append path-Pinsker as a puzzle. Do not
replace it by a different quadratic.

Can it fail: tensorization of `σ_Γ ≥ 4Γ D(p‖uniform)` over `{0,1}^n`
needs a chain rule for every `n`.

Cheapest way: prove the one-carrier comparison first, which is
Proposition RF for `n = 1` and is the telegraph number. Prove the
product inequality by induction if it typechecks. If the induction
stalls, ship `n = 1` and the decoder-mass step, label the general-`n`
declaration WEAKER, and append the failed goal. Do not claim the
uniform bound over every code without the tensorization step.

Can it fail: `exists_hasDerivAt_eq_slope` needs continuity on a compact
interval, and `log` blows up at `0` and at `1`.

Cheapest way: run the mean-value argument on `[0, 1-δ]` and then let
the endpoint be any `ε ∈ (0,1/2]`, which corresponds to `x = 1-2ε ∈ [0,1)`.
Do not evaluate `h` at `0`.

Can it fail: a new `axiom`, `sorry`, or `native_decide` would fail
`scripts/AxiomAudit.lean`.

Cheapest way: no new axiom.

## What either outcome changes

If these declarations typecheck with only `propext`, `Classical.choice`,
and `Quot.sound`, batch 2 has machine-checked the arithmetic the notes
call elementary, and the thermodynamic budgets they take as input.
Later batches can cite `iAlt_eq_rate_L`, `telegraph_floor`, and
`L_ge_four_entropy`. They still have to supply a general bipartite
generator, a hitting time, and the spectral gap where a later statement
needs those.

If a statement will not typecheck, the assumption that blocked it is
appended below with file and line. The declaration is not weakened
without a WEAKER label in `formal/lean/INVENTORY.md`.

## Miss log

Appended after the proofs. Lock: plan commit `303696f` on
`forge-lean-batch2`. Logged 2026-11-24 ET. Breach check: `none`.

The items under "Not proved in this batch" were not locked as
declarations. They stay at the file:line already written above.
A locked statement that is absent, and every **WEAKER** declaration,
is a row here. Formal labels stay in `INVENTORY.md`.

| prediction_id | locked_prediction | outcome | miss | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| B2-destruction | `infoX = worldSum - iAltReal` with the note's `0 log 0` extension. `theory/GENERAL_FLOOR_FINITE_2026-11-23.md:89` | `destruction_identity` at `FiniteFloor.lean:320`, every world mass and every conditional atom strictly positive | short by the zero-atom extension; the singular positive-flux case is the separate statement `iAlt_eq_top_of_singular` | model | medium | strict-positivity hypothesis named; singular edges recorded apart | none |
| B2-stationary-rate | under stationarity, `I_alt = -I^X` with that same extension. Line 93 | `stationary_learning_rate` at `FiniteFloor.lean:373` | same shortfall as B2-destruction | model | low | inherits the strict-positivity hypothesis | none |
| B2-repair-average | `Q̄ ≥ (kT/τ) ∫ σ − kT S_max/τ` once the pointwise bound holds. `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:67` | `repair_floor_of_average` at `RepairFloor.lean:303` takes the average `σbar` as an input | short by the integral; the passage from a pointwise bound to the time average is not constructed | model | medium | algebra of the assumed average is checked | none |
| B2-forget-trajectory | a bit-independent state cannot keep both decoded errors `≤ ε < 1/2`, and the trajectory tends to `1/2`. Line 89 | `rf_forget_stationary` at `RepairFloor.lean:336` | short by the trajectory limit; the stationary obstruction is the checked clause | model | low | stationary obstruction checked; the limit stays a gap at the line cited above | none |
| B2-telegraph | fair telegraph, any finite memory, `I_alt ≥ r L(ε)`, equality for the symmetric copy, and `I_alt = 0` iff `ε = 1/2`. `theory/GENERAL_FLOOR_FINITE_2026-11-23.md:107` | no declaration | short by the whole bound | model | medium | not substituted by a different quadratic | none |
| B2-telegraph-comment | a module comment states only bounds that have a declaration | `FiniteFloorBounds.lean` said the fair-telegraph sum is at least `r L(ε)` | the comment was larger than the file by that sentence | process | low | sentence removed; B2-telegraph is unchanged | none |
| B2-pairwise | `I_alt ≥ min(fluxes) · 2 L(ε / (2 min π))` when `ε < min π`. Line 115 | no declaration | short by the whole bound | model | medium | not substituted | none |
| B2-path | `I_alt ≥ (ε_0 − ε)^2 / K_X`, and `K_X = 1/(4r)` on the fair telegraph. Lines 117–129 | no declaration | short by the whole bound | model | medium | not substituted by a different quadratic | none |
| B2-decoder | `D(p_0‖u) + D(p_1‖u) ≥ 2 (log 2 − h(ε))` when both decoded errors are at most `ε`. `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:77` | `decoder_half`, `decoder_pair`, and `decoder_pair_lower` for one binary source | short by the data-processing step from two record distributions to their decoded masses | model | medium | one-source identities checked | none |
| B2-tensor | `σ_Γ[p] ≥ 4 Γ D(p‖u)` for every distribution on `{0,1}^n`. `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:75` | `L_ge_four_entropy` and `one_carrier_floor` for one carrier | short by every `n > 1`; the product inequality is not a declaration | model | medium | `n = 1` checked; the uniform bound over every code is not claimed | none |
