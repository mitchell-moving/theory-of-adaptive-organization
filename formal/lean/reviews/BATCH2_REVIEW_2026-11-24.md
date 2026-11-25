# Independent review of Lean batch 2

Reviewed head `caea9c0007f666afc1af4ccabd07253b4e4f608e` on `forge-lean-batch2`, stacked on `forge-lean-batch1` at `d12642bae87f3bc2cb8ce39de882fa2dd35301f2`. Sources read before this note: `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at upstream `652d936f3f6c9a97a0cfec60fb99a209db0f015b`; `formal/lean/BATCH2_PLAN.md` (lock `303696f`); `formal/lean/INVENTORY.md`; `formal/lean/GTAO/HeatFloor.lean`, `FiniteFloor.lean`, `FiniteFloorBounds.lean`, and `RepairFloor.lean`; `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`; `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`; `theory/RECORD_REPAIR_FLOOR_2026-11-23.md`. `THEORY.md` and `CORE.md` were not edited. `forge-lean-batch2` was not moved.

**Lock reference:** plan commit `303696f`.
**Logged at (ET):** 2026-11-24.
**Breach check:** `none`. The plan file's miss appendix is the text at that commit. This note does not patch it.

Faithful, in the inventory's own sentence, means the checked statement is the paper sentence, with every extra hypothesis named. WEAKER means a clause of the paper sentence is not in the declaration. A miss below is a signed gap, with a location and an update.

## Machine checks

Toolchain `leanprover/lean4:v4.37.0-rc1`. The build ran in `/tmp/gtao-lean` at this head, which is the checkout `tools/test_lean.py` allows.

`tools/check_lean.sh` exits 0. It rejects `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, and `implemented_by` in `GTAO.lean` and `GTAO/*.lean`, then runs `lake exe cache get`, `lake build`, and `scripts/AxiomAudit.lean`. The build line is `Build completed successfully (6483 jobs)`. The audit line is `AxiomAudit: OK (1185 GTAO declarations; only propext, Classical.choice, Quot.sound)`.

A second scan, the comment-stripping scan in `tools/test_lean.py`, is clean on the same tokens. There is no `opaque` declaration in the four new modules. No declaration in those modules adds an axiom. The 1185 count is the generated-constant count the inventory states, up from 926, and it matches this run.

`python3 tools/check_consistency.py`: wording counter 0 on maintained documents, 29 INFO hits on frozen records, `RESULT: PASS`.

`python3 -m pytest -q tools tests`: **291 passed** in 394.92s, exit 0. That includes `tools/test_lean.py` (the same build and audit) and `tools/test_check_fresh.py::test_real_repo_status_is_in_window_after_fix`. A default `pytest` from the repository root also collects `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py`, which stops at import because `numba` is not installed. That script is outside the 291 and is not part of this diff.

## Freshness

`STATUS.md` on this head says ``main`` is ``31aa997``. The blob is `1d6ef6cd8362642b0dbcb4768d483a96e7d5534e`, identical on the parent `d12642b`. The batch does not touch the file.

`tools/check_fresh.py` grades that pointer against `refs/remotes/origin/main` when the ref exists. Two tips were checked.

| Tip used as `origin/main` | First-parent window | `31aa997` inside it? | What `check` returns |
|---|---|---|---|
| `0f3791890078161a1172277162df5ac13ebbff46` (the tip the builder named, and the stack base recorded on fork PR #30) | `0f37918 d592662 f4ec246 341b7de b611a68` | no | one freshness line |
| `d2aeb8100e22870dc5aee2529356de970c82a820` (fork `main` after `git fetch origin main` during this review; GitHub's fork `main` at the same time) | `d2aeb81 31aa997 8c48a5b 04e9e5b 0e22302` | yes, second commit | empty list |

On the commit `0f37918` itself, `STATUS.md` points at `d592662`, and that pointer sits inside the window above. Fork `main` at that commit passes its own check. Current fork `main` `d2aeb81` also passes, because `31aa997` is its parent. The nonempty check appears only when this branch's `STATUS.md`, inherited unchanged from `d12642b`, is graded against a remote-tracking tip that is still `0f37918`.

That is pre-existing on the parent. It is not introduced by `303696f` or `caea9c0`. It is fork-versus-upstream drift of the remote-tracking ref: `31aa997` is upstream PR #258, and it is newer than `0f37918` (it is not an ancestor of that commit). After the fetch, the pytest assertion holds.

**Recommended update, not applied.** Do not edit `STATUS.md`. Fetch `origin main` so the remote-tracking tip is `d2aeb81`. The page already names the upstream commit the window is supposed to contain. Rewriting the pointer to `0f37918` would point the page at a commit that is not the main it describes.

| prediction_id | locked_prediction | outcome | miss | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| R2-fresh | `STATUS.md`'s ``main`` pointer lies in the five-commit window of fork `origin/main` | pointer `31aa997`; live fork tip `d2aeb81` contains it; stale tip `0f37918` does not | one window step newer than the stale tip, and inside the live window; same blob as `d12642b` | process | low | none yet; fetch the ref; do not edit `STATUS.md` | none |

## Counts

Source declarations, counted from `theorem`, `lemma`, `def`, and `inductive` in the four modules: `HeatFloor.lean` 45, `FiniteFloor.lean` 34, `FiniteFloorBounds.lean` 19, `RepairFloor.lean` 27. Total 125. The inventory's split is 121 Faithful and 4 WEAKER. The four WEAKER names are the four in the plan's miss appendix. No fifth declaration is marked WEAKER, and none of the 121 is unmarked.

## The four WEAKER labels

Each missing clause is the one the inventory names. The statements were compared with the cited lines.

| Declaration | Paper sentence | What the declaration has | Missing clause | Label |
|---|---|---|---|---|
| `destruction_identity` (`FiniteFloor.lean:320`) | `GENERAL_FLOOR_FINITE_2026-11-23.md:89–93`. `I^X` expands as the world sum minus the flux-weighted KL sum, with the note's `0 log 0` extension. | `infoX = worldSum - iAltReal`, and only when every world mass and every conditional atom is strictly positive. The sign matches: `iAltReal` is `Σ flux · klSum(p(·\|x), p(·\|x'))`. | The zero-atom extension. A positive flux into a singular pair is the separate statement `iAlt_eq_top_of_singular`, which sends `iAlt` to `⊤`. `iAltReal` itself uses `klSum`, which puts `0` on a zero atom, so the real identity is not the singular case. | WEAKER, and the miss `B2-destruction` matches. |
| `stationary_learning_rate` (`FiniteFloor.lean:373`) | Line 93: under stationarity, `I_alt = -I^X`, same extension. | `iAltReal = -infoX` after `worldSum_stationary`. Same strict-positivity hypotheses. | Same shortfall as `B2-destruction`. `worldSum_stationary` itself does cancel zeros, including states with zero mass (`flux_off_support`). The rate identity does not inherit that. | WEAKER. `B2-stationary-rate` matches. Stake in the plan is low; the clause is the same one. |
| `repair_floor_of_average` (`RepairFloor.lean:303`) | `RECORD_REPAIR_FLOOR_2026-11-23.md:67–71` and the packaging at `:79–85`. The horizon average of dissipated power is at least `(kT/τ) ∫ σ - kT S_max/τ`, and a pointwise bound on `σ` passes inside the integral. | If `4 Γ (log 2 - h(ε)) ≤ σbar` and `kT ≥ 0`, then `kT` times the lower bound, minus `kT S_max/τ`, is at most `kT σbar` minus the same term. | The Schnakenberg integral is not constructed. Dissipated power is not a variable. The hypotheses on `τ` and on `ε` are unused. The proved step is monotonicity in `σbar`. | WEAKER. `B2-repair-average` matches, and the missing clause is at least as large as that row says. |
| `rf_forget_stationary` (`RepairFloor.lean:336`) | Line 89. A finite irreducible leaky chain has one stationary state, independent of the vanished bit, and the decoded error tends to `1/2`. | If `ε0 + ε1 = 1` and `ε < 1/2`, then the two errors are not both `≤ ε`. | The sum-to-1 hypothesis is not derived from a bit-independent state. The trajectory limit is absent. | WEAKER. `B2-forget-trajectory` matches. The checked clause is the arithmetic obstruction. |

## Five locked statements with no declaration

Searched the four modules for a telegraph lower bound on a general finite memory, a pairwise `L` bound, a path bound, a product inequality on `{0,1}^n`, and a two-distribution decoder bound. None is a declaration. Each is a row in the plan's miss appendix. The "not targets" list in the plan (metastable survival, the Kramers derivation, the Ornstein–Uhlenbeck reduction, a Landauer reset, the tiny-leak modulus, repetition numerics, `ρ ≤ 2λ`, cooperative media, attainment, a closed form of `Φ_X`) stays at the file:line already written there. Those were not locked as declarations.

| prediction_id | Locked sentence | Outcome in the modules | Miss row |
|---|---|---|---|
| B2-telegraph | `GENERAL_FLOOR_FINITE_2026-11-23.md:107–113`. Fair telegraph, any finite memory, `I_alt ≥ r L(ε)`, equality at the symmetric copy, and `I_alt = 0` iff `ε = 1/2`. | No declaration. `iAlt_eq_rate_L` is the two-state copy, which is the equality case of T59, not this bound. `totalVariation` is defined and not used in a lower bound. | Present. Short by the whole bound, including the biconditional at line 21 and line 97. |
| B2-pairwise | Line 115. `I_alt ≥ min(j_ij, j_ji) · 2 L(ε / (2 min π))` when `ε < min(π(i), π(j))`. | No declaration. | Present. |
| B2-path | Lines 117–129. `I_alt ≥ (ε_0 - ε)^2 / K_X`, and `K_X = 1/(4r)` on the fair telegraph. | No declaration. No Pinsker lemma. | Present. Not replaced by a different quadratic. |
| B2-decoder | `RECORD_REPAIR_FLOOR_2026-11-23.md:77`. `D(p_0‖u) + D(p_1‖u) ≥ 2(log 2 - h(ε))` once both decoded errors are at most `ε`. | `decoder_half`, `decoder_pair`, and `decoder_pair_lower` are one Bernoulli source. `decoder_pair_lower` gives `2 fairInfo(a)` for one mass `a ≤ 1/2` against `δ` and `1-δ`. Binary entropy is symmetric, so the sum at `a` equals the sum at `1-a`, but there is still one source. Data processing from two record laws is absent. | Present. |
| B2-tensor | Line 75. `σ_Γ[p] ≥ 4 Γ D(p‖u)` for every distribution on `{0,1}^n`. | `L_ge_four_entropy` and `one_carrier_floor` are one carrier. No product, no induction on `n`. | Present. The uniform bound over every code is not claimed in the inventory. |

## The 121 Faithful declarations

The statements below were compared with the cited line. Extra hypotheses that the paper does not need are named in the declaration. None of these 121 drops a clause of the sentence the inventory assigns to it, and none swaps a quantifier (`∀` edges versus `∃`, support versus the whole alphabet, or `ε < ε_0 ⇒ I_alt > 0` versus the converse).

### `HeatFloor.lean` (45)

Paper: `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`. All 45 are Faithful.

| Declaration | Paper | Comparison |
|---|---|---|
| `errorDot` | `:47` | `(r+Γ)(1-ε) - ε(r+Γ+μ)`. |
| `steadyEps`, `steadyMu` | `:53` | The two steady-state rearrangements. |
| `L` | `:62` | `(1-2ε) log((1-ε)/ε)`. |
| `binaryEntropy`, `fairInfo` | `:59` | `h` in nats, and `log 2 - h`. |
| `copyBracket`, `iAltTwoState` | `:75–77` | Bracket `ε(Γ+μ) - (1-ε)Γ`, times `log((1-ε)/ε)`. |
| `edgeEntropy` | `:70`, `:82–85` | `(a-b) log(a/b)`. |
| `memoryHeat` | `:70`, units restored | `kT (σ + I_alt)`. The general bipartite generator is not a declaration, as the plan says. |
| `kramersRate` | `:40` | `ν exp(-ΔE/kT)`. The 1940 derivation is not claimed. |
| `barrierWork` | `:111` | `χ ΔE (r + ν exp(-ΔE/kT)) (1-2ε)`. |
| `copyCapEps` | `:158` | `(r+Γ)/(2r+(2+c)Γ)`. |
| `L_zero_at_half`, `L_nonneg`, `L_pos` | `:62` | Zero at `1/2`, nonnegative on `(0,1/2]`, positive below `1/2`. |
| `L_one_fifth` | `:144` | `L(1/5) = (3/5) log 4`. The printed decimal `0.831776616672` is not an equality. |
| `steady_mu_dot_zero` | `:45–57` | The steady drive makes `errorDot` zero for `ε ≠ 0`. |
| `steady_unique` | `:53` | If `ε` equals `steadyEps` and the denominator is nonzero, the drive is `steadyMu`. |
| `kolmogorov_error_dot` | `:47` | The four masses `(a,b,c,d)` with `a+b+c+d = 1` regroup to `errorDot` of `b+c`. The world-flip and leak signs match the master equation in the docstring. |
| `bracket_eq_world`, `iAlt_eq_rate_L` | `:79–82` | At the steady drive, the bracket is `r(1-2ε)` and `I_alt = r L(ε)`. `Γ` cancels. Hypothesis `ε ≠ 0` is the division in `steadyMu`. |
| `floor_independent_of_barrier` | `:103`, item 2 at `:16` | The steady `I_alt` at `Γ₁` equals the steady `I_alt` at `Γ₂`. Both equal `r L(ε)`, so the floor expression does not contain `Γ`. |
| `edgeEntropy_nonneg`, `edgeEntropy_eq_zero_iff` | `:82–85` | For `a > 0` and `b > 0`, the edge term is nonnegative and zero iff `a = b`. |
| `memoryHeat_ge_info` | `:70` | `kT ≥ 0` and `σ ≥ 0` give `kT I_alt ≤ kT(σ + I_alt)`. |
| `jp_heat_floor` | `:19–23`, `:82–85` | At the steady drive, with both fluxes strictly positive and `0 < ε ≤ 1/2`, `kT r L(ε) ≤ memoryHeat`. The positive-flux hypotheses are named. `Γ = 0` makes the back flux zero, so that boundary is outside this theorem; the note attributes it to IP3. `iAlt_eq_rate_L` still holds there. |
| `frozen_flux_balance`, `frozen_heat_zero` | `:85` | At `r = 0`, the two fluxes match. For `0 < ε < 1` and `Γ > 0`, `σ = 0`, `I_alt = 0`, and the heat is `0`. |
| `hasDerivAt_mul_log`, `hasDerivAt_one_sub`, `hasDerivAt_compl_log`, `hasDerivAt_binaryEntropy`, `hasDerivAt_fairInfo` | `:59–65` | The derivative of `log 2 - h(ε)` is `-log((1-ε)/ε)` on `(0,1)`. |
| `destroyDeriv` | `:59–65` | That derivative, times `ε̇ = (r+Γ)(1-2ε)`, equals `-(r+Γ) L(ε)`. The docstring says this is not the steady JP-heat flow. |
| `kramersRate_pos`, `iAlt_of_kramers` | `:40`, `:82` | `ν > 0` makes the rate positive. Substituting it into the steady identity still gives `r L(ε)`. |
| `barrierWork_zero`, `barrierWork_pos` | `:109–111`, `:156` | Zero at `ΔE = 0`. For `χ = 1`, `ΔE > 0`, `r ≥ 0`, `ν > 0`, and `ε < 1/2`, the work is positive. `kT > 0` is not required, because `Real.exp` is positive for every real argument. |
| `steady_ge_copyCap`, `copy_cap_gap`, `copy_cap_near_half` | `:158` | If `0 ≤ μ ≤ c Γ`, the steady error is at least `copyCapEps`. The distance from that bound to `1/2` is `c Γ / (2(2r+(2+c)Γ))`, and the bound can be put within any positive allowance of `1/2` by taking `Γ` small. The plan's "which tends to `1/2`" is this bound, not a separate squeeze of `steadyEps`. |
| `hasDerivAt_log_ratio`, `hasDerivAt_L`, `L_antitone` | `:62` | `L` is antitone on `(0,1/2]`. The derivative used on the interior is nonpositive. |

### `FiniteFloor.lean` (32 Faithful, plus the two WEAKER above)

Paper: `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`. Alphabet is a `Fintype`, which is the note's finite state set.

| Declaration | Paper | Comparison |
|---|---|---|
| `Nonneg`, `AC`, `Prob` | the sums at `:17–19` | Nonnegative mass, absolute continuity (`p a ≠ 0` implies `q a > 0`), and a probability (nonnegative and total mass 1). |
| `klSum`, `kl` | `:17–19` | `klSum` is the real sum, with the summand `0` when `q a = 0`. `kl` is `ENNReal.ofReal` of that sum when both are nonnegative and `AC`, and `⊤` otherwise. |
| `klSum_nonneg`, `kl_nonneg` | `:17–19` | The real sum is nonnegative for nonnegative masses. `kl_nonneg` is `0 ≤ kl` in `ℝ≥0∞`, which is the order on that codomain. |
| `kl_eq_top_of_not_ac`, `kl_eq_ofReal` | `:17–19` | Not absolutely continuous gives `⊤`. Absolute continuity gives the `ofReal` of the real sum. |
| `klTerm_expand`, `klSum_eq_sum_log` | `:89–93` | The summand expands to `p log(p/q) + q - p`. For probabilities with every `q a > 0`, the `q - p` terms cancel and `klSum` is `Σ p log(p/q)`. |
| `kl_zero_iff` | `:97` | For probabilities, `kl = 0` iff `p = q`. On a probability that is absolutely continuous, agreement on `{p > 0}` plus total mass 1 is the same conclusion. A singular pair is `⊤`, not `0`. |
| `totalVariation`, `totalVariation_nonneg` | `:111` | `(1/2) Σ \|p - q\|`, nonnegative. The telegraph identity `ε = (1 - TV)/2` is not a theorem. That absence is `B2-telegraph`, not a second statement. |
| `flux`, `stationary` | `:89–93` | Directed flux `π(x) W(x→x')`. Stationarity is incoming flux equal to outgoing flux at every state. |
| `flux_nonneg`, `flux_off_support` | `:89–93` | Nonnegative `π` and `W` give nonnegative flux. Under stationarity, a pair that is not jointly in the support has flux `0`. |
| `worldSum`, `worldSum_stationary` | `:89–93` | The world sum, restricted to pairs with both masses positive, is `0` under stationarity. Zero-mass states are included: their flux is `0`. |
| `iAltReal`, `iAlt` | `:17–19`, `:93` | The real rate is the flux-weighted `klSum`. The extended rate uses `ofReal(flux) * kl`, so a positive flux times `⊤` is `⊤` and a zero flux times `⊤` is `0`. |
| `ennreal_sum_eq_zero`, `iAlt_nonneg` | `:97` | A finite sum of `ENNReal` is `0` iff every term is `0`. `iAlt_nonneg` is `bot_le`: the extended rate sits in `ℝ≥0∞`. |
| `iAlt_eq_top_of_singular` | `:17–19` | One positive-flux edge whose conditionals are probabilities and not absolutely continuous makes `iAlt = ⊤`. |
| `iAlt_zero_iff_edge` | `:97`, first sentence | For nonnegative `π` and `W`, and a probability conditional at every state, `iAlt = 0` iff `p(·\|x) = p(·\|x')` on every edge with positive flux. The quantifier is over every such edge. |
| `infoX` | `:89–93` | `Σ π(x) p(m\|x) W log( (π(x') p(m\|x')) / (π(x) p(m\|x)) )`. Defined as a real. The identity that expands it is the WEAKER theorem above. |
| `bayesError`, `chanceError` | `:41–45` | `1 - Σ_m max_x joint(x,m)` and `1 - max_x π(x)`, on a nonempty finite world. The `min_f` decoder form in the same display is not a separate theorem. The inventory's sentence is the sum. |
| `sup'_witness_irrelevant`, `le_sup'_univ` | `:41–45` | The finite maximum does not depend on which witness of nonemptiness is supplied, and each value is `≤` that maximum. |
| `bayes_of_constant` | `:97` | A single conditional `p`, independent of `x`, gives Bayes error equal to chance error. The support-restricted form used by the connectivity theorem rewrites zero-mass states before calling this one. |

### `FiniteFloorBounds.lean` (19)

Paper: the same note. All 19 are Faithful to the sentences the inventory states. The telegraph, pairwise, and path bounds are not among them.

| Declaration | Paper | Comparison |
|---|---|---|
| `frozen_support` | `:103` | If every flux is `0`, then `iAlt = 0`. Under nonnegative `π`, "every flux is zero" is "every occupied flux is zero". |
| `boltzmann_below_half` | `:103` | `1/(1+exp 1) < 1/2`. The printed soft-memory decimal is not an equality. The Boltzmann construction of that copy is not a theorem; the inventory claims the inequality. |
| `PosFlux`, `Reach`, `stronglyConnected` | `:97` | A positive-flux step, directed reachability along those steps (including the length-zero step), and mutual reachability on `{π > 0}`. That is the occupied flux graph, not the whole alphabet. |
| `reach_same_conditional` | `:97` | `iAlt = 0` sends equal conditionals along every positive-flux path. |
| `iAlt_zero_stronglyConnected` | `:97` | Strong connectivity on the support, plus `iAlt = 0`, gives Bayes error equal to chance error. Zero-mass states are rewritten by `π(x) = 0` before `bayes_of_constant`. The converse is not claimed. |
| `sup_fin3` | the witnesses | `sup'` on `Fin 3` is the nested `max`. |
| `classπ`, `classW`, `classP`, `classP_prob`, `classP_same` | `:99` | `π = (3/10, 3/10, 2/5)`, rate `1` each way on `{0,1}`, state `2` isolated, and a class indicator. `classP 0 = classP 1`. Atoms are `0` or `1`; the cross-class pair is singular and carries no flux. |
| `two_class_counterexample` | `:99` | `iAlt = 0`, Bayes error `3/10`, chance error `3/5`, and `classW 0 1 ≠ 0`. The printed `0.312590` is not this witness. Flux balance holds numerically (exchange flux `3/10` each way, state `2` at rest) and is not a conjunct of the theorem. The inventory's sentence is the four conjuncts that are proved. |
| `cycleπ`, `cycleW`, `cycleP`, `cycle_flux01` | `:21`, `:97` | `π = (1/2, 1/4, 1/4)`, cycle rates `1, 2, 2`, full-support conditionals that separate states `1` and `2`. The edge `0 → 1` has flux `1/2`. |
| `converse_fails_three` | `:21`, `:97` | Bayes error equals chance error, and `iAlt > 0`. Each of the three directed fluxes equals `1/2`, so the chain is stationary, and `stationary cycleπ cycleW` is not a conjunct. The inventory claims the two proved conjuncts. The separation of the non-mode states is the data of `cycleP`, used to make one KL term positive. |

### `RepairFloor.lean` (25 Faithful, plus the two WEAKER above)

Paper: `theory/RECORD_REPAIR_FLOOR_2026-11-23.md`.

| Declaration | Paper | Comparison |
|---|---|---|
| `log_sub_log_le`, `log_sub_log_lt` | `:73` | `log(1+t) - log(1-t) ≤ 2t/(1-t^2)` on `[0,1)`, strict on `(0,1)`. The series majorant is the geometric series (coefficient `1`), which is coarser than the note's `1/(k(2k-1))`. It is enough for the next two lemmas. |
| `infoDeriv`, `infoDeriv_nonpos`, `infoDeriv_neg` | `:73` | With `t = 1-2ε`, the derivative of `L - 4(log 2 - h)` equals `2 log((1+t)/(1-t)) - 4t/(1-t^2)`, which is `≤ 0` on `(0,1/2]` and `< 0` on `(0,1/2)`. |
| `hasDerivAt_infoGap`, `infoGap_half`, `infoGap_anti`, `infoGap_strictAnti` | `:73` | The gap is antitone on `(0,1/2]`, strictly antitone, and `0` at `1/2`. |
| `L_ge_four_entropy` | `:73` | `L(ε) ≥ 4(log 2 - h(ε))` on `(0,1/2]`. |
| `L_eq_four_entropy_iff` | `:73` | Equality iff `ε = 1/2`. Both sides are `0` there. The note's "tends to `4Γ` as `ε → 1/2`" is the ratio `σ/D`, whose limit is the constant. The closed interval attains equality at the endpoint. The inventory's "exactly at `1/2`" matches the theorem. |
| `fairInfo_half`, `fairInfo_antitone`, `fairInfo_strictAnti`, `fairInfo_nonneg` | `:73` | `log 2 - h(1/2) = 0`, and `fairInfo` decreases to that value on `(0,1/2]`. |
| `oneCarrierSigma`, `one_carrier_floor` | `:73`, `:85` | `σ` is defined as `Γ L(ε)`. For `kT ≥ 0` and `Γ ≥ 0`, `4 kT Γ (log 2 - h(ε)) ≤ kT σ`. The edge-sum derivation that a two-state leak equals `Γ L(ε)` is not a separate expansion; the name is the formula. The heat packaging with `S_max/τ` is the WEAKER theorem, not this one. |
| `long_horizon` | `:85` | For any `S_max` and any `δ > 0` there is a `T` such that `τ ≥ T` gives `S_max/τ < δ`. The plan's liminf of the whole floor needs the integral, which is the logged miss, and is not claimed here. |
| `rf_cap` | `:124–128` | If `N kT Γ g ≤ q A` and the denominator is positive, then `N ≤ q A / (kT Γ g)`. `q` is an input. |
| `rf_cap_entropy` | `:124–128` | The same with `g = 4(log 2 - h(ε))` and `ε < 1/2`, so the denominator is positive. |
| `rf_cap_chain` | `:124–128` | If also `g ≥ 4(log 2 - h(ε))`, then `N ≤ q A / (kT Γ g)` and that upper bound is `≤ q A / (4 kT Γ (log 2 - h(ε)))`. A larger `g` tightens the count. The direction matches the display. |
| `bernoulli` | `:77` | Mass `a` on outcome `0` and `1-a` on outcome `1`. |
| `decoder_half` | `:77` | `klSum(Bernoulli(1-ε), uniform) = fairInfo(ε)` for `ε ∈ (0,1)`. |
| `decoder_pair` | `:77` | One mass `a` against `δ` and against `1-δ` sums to `-2 h(a) - log(δ(1-δ))`. |
| `decoder_pair_lower` | `:77` | For `a ∈ (0,1/2]` that sum is at least `2 fairInfo(a)`. One source. The two-distribution bound remains `B2-decoder`. |

## One process miss in a module comment

`FiniteFloorBounds.lean:19–24` introduces the file as the witnesses and the telegraph bound, and then states that on the fair telegraph the learning-rate sum is at least `r L(ε)`. The three sentences before that one match theorems in the file (frozen support, the class indicator, the 3-cycle). The telegraph sentence does not. The inventory and `B2-telegraph` already say there is no such declaration. The comment contradicts that record.

| prediction_id | locked_prediction | outcome | miss | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| R2-telegraph-comment | The module comment states only bounds that are declarations. | `FiniteFloorBounds.lean:23–24` states `I_alt ≥ r L(ε)` for the fair telegraph. | one asserted bound with no declaration; the same absence as `B2-telegraph` | process | medium | none yet; delete that sentence and the words "and the telegraph bound" from the header. Not applied. | none |

This does not change the 121 labels. No declaration is marked Faithful for that bound.

## Attacks tried

- Token scan before the build, comment-stripping scan, and the axiom audit. Only `propext`, `Classical.choice`, and `Quot.sound`, across 1185 `GTAO` constants. No `sorry`, `admit`, `native_decide`, `unsafe`, `implemented_by`, or `opaque` in the four modules.
- Recount of source declarations against the inventory: 45 + 34 + 19 + 27 = 125, and the 121 / 4 split. Each WEAKER name sits at the line the inventory cites.
- Sign check on `destruction_identity`. `log((π' p')/(π p)) = log(π'/π) + log(p'/p)`, and `D(p(·\|x) ‖ p(·\|x')) = -Σ p log(p'/p)`, so `infoX = worldSum - iAltReal`. The strict-positivity hypothesis is exactly the missing `0 log 0` extension. The singular positive-flux case is `⊤`, not a silent zero, in `iAlt`.
- Quantifier check on `iAlt_zero_iff_edge` and `iAlt_zero_stronglyConnected`. Zero learning rate means every positive-flux edge has equal conditionals, and strong connectivity is mutual reachability on `{π > 0}`. The class indicator is the disconnected case (`I_alt = 0` and `ε < ε_0`). The 3-cycle is the converse (`ε = ε_0` and `I_alt > 0`). Neither direction is swapped.
- Extended-real check. `kl` and `iAlt` use `ℝ≥0∞`. `kl_nonneg` and `iAlt_nonneg` are `bot_le`. `iAltReal` is not given a nonnegativity theorem, and `klSum` writes `0` on a zero atom. The theorems that quote the real identity assume every atom is positive and are labeled WEAKER. `ofReal` of a nonpositive flux is `0`, so a negative rate cannot make the extended sum negative; the theorems that conclude `iAlt = 0` assume nonnegative `π` and `W`.
- Vacuous-conclusion check. `repair_floor_of_average` is monotonicity in an assumed average, labeled WEAKER, with `τ` and `ε` unused. `rf_forget_stationary` is the arithmetic of two numbers that sum to `1`. `jp_heat_floor` needs both fluxes positive; that hypothesis is named, and `Γ = 0` stays outside it. `kramersRate_pos` and `barrierWork_pos` use positivity of `Real.exp` and do not need `kT > 0`.
- Equality check on `L` against four times `log 2 - h`. The gap is strictly antitone on `(0,1/2]` and zero at `1/2`, so equality holds at `1/2` and nowhere else in the interval. The note's limit statement is the ratio. The series used on the derivative is the geometric majorant, not the note's coefficient `1/(k(2k-1))`. The inequality proved is the one at line 73.
- Witness arithmetic. Class indicator: Bayes `3/10`, chance `3/5`, flux `3/10` each way on `{0,1}`, state `2` at rest. Cycle: each directed flux `1/2`, Bayes error `1/2`, chance error `1/2`, one KL term strictly positive. Stationarity is true of both matrices and is not a conjunct. The inventory does not claim that conjunct.
- Decoder check. `decoder_pair_lower` is one Bernoulli. Symmetry of `h` makes the sum at `ε` equal the sum at `1-ε`. Two record distributions, data processing, and the product over `{0,1}^n` are absent and are the logged rows `B2-decoder` and `B2-tensor`.
- Search for `telegraph_floor`, `pairwise`, `Pinsker`, `K_X`, and a product on `n` carriers. The only `r * L(ε)` theorems are the two-state identities in `HeatFloor.lean`.
- Freshness, both tips. Parent blob identical. Live fork `main` `d2aeb81` puts `31aa997` in the window. Stale tip `0f37918` does not. Pytest after the fetch: 291 passed.
- Wording of this note against the process rule: a miss is recorded with a sign, a location, and an update. `THEORY.md` and `CORE.md` are untouched.

## Miss ledger for this review

| prediction_id | locked_prediction | outcome | miss | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| R2-fresh | pointer inside the fork window | holds for `d2aeb81`; does not hold for stale `0f37918` | see the freshness section; pre-existing on `d12642b` | process | low | none yet; fetch; do not edit `STATUS.md` | none |
| R2-telegraph-comment | module comment matches the declarations | one telegraph sentence with no theorem | short by that sentence | process | medium | none yet; delete the sentence | none |
| R2-faithful-121 | each Faithful label is the paper sentence, extra hypotheses named | 121 statements compared above | HIT. No missing hypothesis, no swapped quantifier, and no conclusion that holds only because a hypothesis is unsatisfiable. The extended-real order facts are the codomain the plan asked for. | model | high | none | none |
| R2-weaker-4 | the four WEAKER rows name the missing clause | each clause confirmed in the table above | HIT on the labels. `repair_floor_of_average` is smaller than a heat bound by the whole integral, which is the logged size. | model | high | none | none |
| R2-five-absent | the five locked sentences with no declaration are logged misses | all five rows present; no silent substitute | HIT | model | high | none | none |

Blockers remaining: 0
