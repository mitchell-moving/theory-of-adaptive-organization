# Independent review of Lean batch 1

Reviewed head `ff47adb394e23fced1a279034f3ebaa2b2f8e8ad` on `forge-lean-batch1`, against fork `origin/main` `d2aeb8100e22870dc5aee2529356de970c82a820`. The diff is the three commits `32860b8`, `9f082c8`, and `ff47adb`. Sources used: that diff, `formal/lean/BATCH1_PLAN.md`, `theory/REPRESENTATION.md`, and `theory/CONTINUOUS_A6_2026-11-23.md`. The draft PR description was not used. `THEORY.md` and `CORE.md` are not in the diff. This file does not edit them and does not merge.

## Machine checks

Toolchain `leanprover/lean4:v4.37.0-rc1`, build in `/tmp/gtao-lean` at this head.

`tools/check_lean.sh` exits 0. It runs `lake exe cache get`, then `lake build` (`Build completed successfully (6475 jobs)`), then `scripts/AxiomAudit.lean`. The audit line is `AxiomAudit: OK (925 GTAO declarations; only propext, Classical.choice, Quot.sound)`.

The same script rejects `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, and `implemented_by` in `GTAO.lean` and `GTAO/*.lean` before the build. `tools/test_lean.py` strips comments and scans the same tokens. Both are clean. The only `sorry` string in `formal/lean/` is a comment in `scripts/AxiomAudit.lean`, which the project scan does not read.

A dump of every environment constant whose module starts with `GTAO` has 925 names. Modules other than the four new ones sum to **757**. The four new modules sum to **168** (`Cauchy` 43, `Representation` 42, `Obstruction` 46, `ContinuousA6` 37). That is the audit list before this batch, unchanged, plus the constants this batch adds.

`python3 tools/check_consistency.py`: FAIL 0, INFO 29 on frozen records, RESULT PASS.

`python3 tools/check_open_work.py`: `items.json` not-DONE 62, `QUEUE.md` not-DONE 90, union missing from `OPEN_WORK.md` 0, RESULT PASS.

`python3 tools/check_fresh.py`: RESULT PASS. `STATUS.md` says `main` is `31aa997`. The first-parent window of `origin/main` is `d2aeb81 31aa997 8c48a5b 04e9e5b 0e22302`.

The freshness failure is gone. Before `git fetch origin main`, the remote-tracking ref was `0f37918`. `31aa997` is a descendant of that commit, so it sat outside that tip's five-commit window. The fetch moved `origin/main` from `0f37918` to `d2aeb81`, which is the parent of the batch. `STATUS.md` is not in the diff. The pointer did not move. Fork main did.

`python3 -m pytest -q tools tests`, with the lake rebuild kept out of the long run so it would not share `.lake` with the build above: 290 passed, 1 deselected, 376.85s. The deselected test is `tools/test_lean.py::test_lean_build_if_available`. Run after the build, `python3 -m pytest -q tools/test_lean.py` passed both of its tests in 6.52s. Distinct tests passed: **291**. Skipped: **0**.

## Inventory

`formal/lean/INVENTORY.md` counts the sources that existed on `d2aeb81`. A parse of `theorem`, `lemma`, `def`, `abbrev`, `structure`, and `instance` in those files, excluding the four new modules, is 354 declarations. Every per-file count in the inventory table matches. The 354 declaration rows are 20 Faithful, 6 WEAKER, and 328 unlabeled.

Each of those 354 rows cites a line that holds a declaration of the stated kind. One row uses the wrong identifier: `DriftSelection.trace_mul` at `DriftSelection.lean:150` is the lemma `trace_mul₃_herm`. The line and the kind are right. The other 353 identifiers match.

The batch adds 74 source declarations: 26 in `Cauchy.lean`, 16 in `Representation.lean`, 16 in `Obstruction.lean`, 16 in `ContinuousA6.lean`. All 74 names are among the 168 new constants. The other 94 are generated (`_proof`, `simp`, `casesOn`, and the private lemmas from `field_simp`).

The six pre-batch WEAKER names are the ones the README already marks, at the lines the inventory cites: `DriftSpeed.meanLag_abs`, `ds2_excess`, `halfWindow_diverges`, `Coadaptation.ca1b_team_split`, `ca1c_gap_zero`, `ca1c_fraction`. Their Lean text is unchanged from `origin/main`. They were not re-audited against papers outside the two sources named above.

## Existing declarations

`git diff origin/main...HEAD` for every pre-existing `formal/lean/GTAO/*.lean` is empty. `GTAO.lean` adds four imports. No pre-existing declaration was edited, renamed, or removed. The 757 constants in the old modules are the previous audit list.

## Faithfulness

Labels below are the batch-1 labels in `formal/lean/README.md` and `formal/lean/INVENTORY.md`. The inventory's own sentence is the standard used here: Faithful means the checked statement is the paper sentence, with every extra hypothesis named; WEAKER means a clause of the paper sentence is not in the declaration.

Debreu, von Neumann–Morgenstern, layer-count separability, and Gelfand–Yaglom–Dobrushin are hypotheses, not theorems.

- `DebreuAdditive` is a structure. `r1_linear_components` and `r1_nonneg_of_A8` take it as a hypothesis. Its fields are `n ≥ 3`, a continuous component on `(0, ∞)`, and a sum on the positive orthant. Nothing proves Debreu's theorem.
- `r1_vnm_scale` assumes two positive affine writings of one index. It does not mention Debreu.
- `r1_with_layer_count` assumes `C(z, K) = C_interval(z) + f(K)`. No declaration drops that hypothesis.
- `GYDSup` is a `Prop`. `gyd_equiv` is the only theorem that takes it. The audit does not gain an axiom from it.

Sample compared with the paper sentence. Twenty-four labeled Faithful are listed, then the one new WEAKER declaration.

| Declaration | Paper | Verdict |
|---|---|---|
| `cauchy_rat` | `theory/REPRESENTATION.md:70` | Matches. Positive rationals, no monotonicity, either sign of `f(1)`. |
| `cauchy_monotone` | `:70–71` | Matches `f(x) = x f(1)` for either monotone direction on `(0, ∞)`. The sign of `f(1)` is the separate lemma `f_one_nonneg_of_nondecreasing` / `f_one_nonpos_of_nonincreasing`. |
| `cauchy_continuous` | `:72` | Matches. Continuity on `(0, ∞)`, sequence from below, either sign. |
| `pexider_monotone`, `pexider_continuous` | `:76` | Match. `g = f + c` is additive and `f(z) = (f(1)+c) z - c`. |
| `cauchy_nat` | `:78` | Matches. `f(0) = 0` and `f(n) = n f(1)`, no topology. |
| `slope_nonneg_of_nondecreasing` | `:80` | Matches. A nondecreasing line on `(0, ∞)` has slope `≥ 0`. |
| `r1_linear_components` | `:84`, steps `:102–110` | The shape matches the packaging the plan names: Pexider plus continuity gives `∑ p_i z_i + b` on positive vectors, prices unsigned. `n ≥ 3` is a field of the hypothesis and is not used in the proof. The common scale `a > 0` is not this theorem. |
| `r1_nonneg_of_A8` | `:92`, `:120` | Matches. Monotonicity of each component is a hypothesis and yields `p_i ≥ 0`. |
| `r1_with_layer_count` | `:94`, `:112` | Separability is a hypothesis and concatenation gives `h K`. The sentence at `:112` that A8 makes `h ≥ 0` has no declaration. |
| `affine_argmin_iff`, `strictMono_argmin_iff` | `:126` | Match. `a > 0`, and any strictly increasing transform, preserve `IsArgmin` on a menu that does not depend on the cost. |
| `affine_excess_scale`, `affine_excess_eq_iff` | `:134–142` | Match the fixed-weight reading. The second reuses `Equipartition.gibbs_excess_quadratic` and proves equality with `d/(2β)` if and only if `a = 1`. The constant `b` cancels. |
| `affine_excess_refit` | `:142` | Matches. `β_new = β/a`, `a > 0`, and `(a • H)` positive definite. The excess under the Gibbs weight of `C` is `d/(2 β_new)`. |
| `fractional_excess_scale` | `:146` | Matches the `b = 0` identity. |
| `constrained_argmin_not_affine` | `:152` | The witness is faithful to the plan's two-design margin. Costs `1` and `6/5`, variances `4` and `1`, level `3`, threshold `18/100`, shift `17/10`. Before the shift both designs are feasible and design 0 is cheaper (`θ` is `1` and `18/5`). After the shift, `θ` is `3/20` and `1/5`, so only design 1 stays feasible. |
| `kelly_qstar`, `kelly_foc_sign` | `:160` | Match the published point. `β = 1/20`, `a₁ = 13/10`, `b₁ = 21/20`, `b₀ = 9/10`, lean shock factor `0`. The objective is the one whose first-order condition is the displayed `q*`. `q* = 13/50` is the unique maximizer on `(0, 1]`. The printed growth `0.128` is not an equality. |
| `kelly_not_expected_factor` | `:160` | Matches. Lean factor `247/200 = 1.235`, robust factor `417/400 = 1.0425`. The linear objective on `[0, 1]` is maximized only at pure lean, which is not `13/50`. |
| `expected_cost_interval` | `:162` | Matches the expected-cost half. `c/τ + α τ` at `c = 1/20`, `α = 1/2` has unique positive minimizer `√(1/10)`. That is `LayerLifetime.Tstar` at a coefficient product equal to `α`. |
| `klDiv_zero_iff_eq` | `theory/CONTINUOUS_A6_2026-11-23.md:111` | The Kullback–Leibler biconditional matches the second sentence: for probability measures, `klDiv = 0` if and only if the measures are equal. The mutual-information form that opens the line is not a declaration. |
| `mi_swap`, `mi_data_processing` | `:145` | Symmetry is the coordinate swap. Data processing is `klDiv_map_le` on `Prod.map`. Both match those two clauses. |
| `partition_mi_le`, `refinement_mono`, `finite_identity_attains` | `:99`, `:101` | A measurable labeling does not raise mutual information. A coarser labeling, as a measurable function of a finer one, does not raise it. On a finite alphabet the identity labeling attains `mutualInfo`. The Shannon-sum formula at `:71–75` is not expanded. |
| `GYDSup`, `gyd_equiv` | `:91`, `:21` | `GYDSup` is the reverse inequality, joint divergence at most the supremum over finite measurable labelings. `gyd_equiv` adds that hypothesis to the proved bound. The supremum is not constructed. |

`negative_price_example` is the only new declaration labeled WEAKER. The statement is continuity of `id`, `id`, and `z ↦ -z`, the sum `z₀ + z₁ - z₂`, and third price `-1`. `theory/REPRESENTATION.md:64` and `:90` also say the example satisfies A1–A7, including Shannon, affine loss, and an exogenous world. Those clauses are absent. The WEAKER label says so. The label is not too strong. The last conjunct `(-1) < 0` is arithmetic.

## The two logged gaps

`ContinuousA6.lean:125`, `klDiv_compProd_chain`, is Mathlib's `klDiv_compProd_eq_add`: `klDiv (μ ⊗ₘ κ) (ν ⊗ₘ η) = klDiv μ ν + klDiv (μ ⊗ₘ κ) (μ ⊗ₘ η)`, for finite measures and Markov kernels. The docstring says this is not `I(X; Y, Z) = I(X; Z) + I(X; Y | Z)`. `BATCH1_PLAN.md:172–181` records the same puzzle and does not substitute a weaker mutual-information equation. `theory/CONTINUOUS_A6_2026-11-23.md:145` names "the chain rule" and does not write that conditional formula. The gap is honest. The README's word Faithful is tied, in the same sentence, to the kernel identity.

`Obstruction.lean:284`, `survival_interval_lt`, proves a unique zero of `phi` on `(0, 2]` inside `(23615/100000, 189/800)`, strictly below `√(1/10)`, with `√(1/10)` inside `(31622/100000, 31623/100000)`. An independent expansion gives `6000 t² φ(t)` equal to the shipped quintic, and the real root is about `0.2362075267`, below `√(1/10) ≈ 0.3162277660`. The printed figures are not equalities. `phi` is the numerator `m' s² - m (s²)'` at the published point `y = 1`, `c = 1/20`, `α = 1/2`, `β = 1/3`, `s₀² = 9/100`. The plan, the README, and the new `OPEN_WORK` T19 sentence all say this zero is not proved to maximize `θ = 2m/s²`. That disclosure is accurate: no derivative of `θ` is constructed. The gap text is honest. The label is not. See finding 2.

## Wording and personal information

The added text has no "theory of everything", no "bill", no "solved", and no derivation of holography or general relativity. `check_consistency.py` reports 0 wording failures on maintained docs. The word "law" in the replaced `OPEN_WORK` T19 line is the pre-existing phrase "stationary law", on both sides of the diff.

The four new Lean files carry `Copyright (c) 2026 Chad Mitchell. Public domain (CC0).` That is the header already on the existing modules. The diff has no email address, phone number, or private remark.

## Findings

### BLOCKING

None.

### HIGH

1. **`klDiv_prob_integral` is the real `toReal` identity, and the infinite case collapses to 0.** `formal/lean/GTAO/ContinuousA6.lean:32–35`. `theory/CONTINUOUS_A6_2026-11-23.md:77–80` defines `D_KL` in `[0, ∞]`: the integral of the log-likelihood when `P ≪ Q`, and `+∞` when the integral is infinite. The declaration states `(klDiv μ ν).toReal = ∫ llr μ ν ∂μ` for probability measures with `μ ≪ ν`. Mathlib's `toReal_klDiv_of_measure_eq` (`KullbackLeibler/Basic.lean:158–162` at this pin) proves that by cases. When `llr` is integrable, the correction term vanishes because both measures have mass 1. When it is not, `klDiv` is `⊤` (`klDiv_of_not_integrable`) and both `ENNReal.toReal ⊤` and the Bochner integral of a non-integrable function are `0`. The equality of those two reals holds. It is not the paper's extended value. The docstring, `formal/lean/README.md` on this declaration, and `BATCH1_PLAN.md:38` say the value is the paper's integral in `[0, ∞]`. `klDiv_zero_iff_eq` is unaffected: it uses `klDiv = 0`, and `⊤ ≠ 0`.

2. **`survival_interval_lt` is labeled Faithful, and a clause of the sentence it cites is missing.** `formal/lean/GTAO/Obstruction.lean:284`. `theory/REPRESENTATION.md:162` says the survival-optimal interval and the expected-cost interval are not the same design, with printed values `0.2362` and `0.3162`. The declaration proves a unique zero of `phi` on `(0, 2]` lies below `√(1/10)`. It does not prove that this zero maximizes `θ`. The inventory's definition then calls the declaration WEAKER. The README still prints **Faithful**, with a following sentence that points at the plan. The plan and `OPEN_WORK` tell the truth about the missing derivative. The label does not follow the definition those files set.

### MEDIUM

3. **`r1_vnm_scale` does not identify Debreu's scale with the currency scale.** `formal/lean/GTAO/Representation.lean:57–68`. `theory/REPRESENTATION.md:118` says the currency regraduation and Debreu's common scale are the same `a`, because the cost is already the von Neumann–Morgenstern index, and the constants sum to one `b`. The theorem assumes `C = a₁ · loss + b₁` and `C = a₂ · loss + b₂` with `a₁ > 0`, `a₂ > 0`, and `loss` taking two values, and concludes `a₁ = a₂`, `b₁ = b₂`, and `0 < a₁ ∧ 0 < a₂`. The last two conjuncts are the hypotheses `ha1` and `ha2`. Debreu's `a` does not appear. The README gloss matches this narrower algebra. The cited sentence is wider. Von Neumann–Morgenstern linearity is a hypothesis, which is the right shape. It is not smuggled.

4. **The zero-price lemma is stated on all of `ℝ^ι`, and its witness leaves the positive orthant.** `price_zero_of_independent` (`Cauchy.lean:319–341`) and `r1_zero_of_not_essential` (`Representation.lean:91–95`). Lemma M at `theory/REPRESENTATION.md:80`, and the price-zero sentence at `:25` and `:90`, live on the product of intervals. The proof compares the zero vector with the vector that is `1` in coordinate `i`. `r1_linear_components` gives `C(z) = ∑ p_i z_i + b` only for `z > 0`. That identity does not discharge `∀ z, C z = ∑ p_j z_j + b`. A preorder defined on `(0, ∞)^n` does not, by itself, supply `IndependentOf` at `0`.

### LOW

5. **One inventory identifier is shortened.** `formal/lean/INVENTORY.md` names `DriftSelection.trace_mul` for `trace_mul₃_herm` at `DriftSelection.lean:150`. The 354 / 20 / 6 / 328 counts, the per-file counts, and the other identifiers match the sources. The Lean declaration was not renamed.

6. **`klDiv_nonneg` is the order on `ℝ≥0∞`.** `ContinuousA6.lean:38–40` is `zero_le`. Mathlib's comment on `klDiv` says nonnegativity in that codomain is by definition. The paper's nonnegativity of the integral is a different fact. The declaration is true and has no content past the type.

7. **The fractional excess with a nonzero shift is one rational witness.** `fractional_excess_scale` is the general `b = 0` identity. `fractional_excess_shift` (`Representation.lean:292–294`) is `(2+1-(1+1))/(1+1) ≠ (2-1)/1`, that is `1/2 ≠ 1`, for `E[J] = 2`, `J* = 1`, `b = 1`. `theory/REPRESENTATION.md:146–148` displays the general quotient `(a (E[J]-J*))/(a J* + b)`. The README says the claim is these rationals. The general numerator and denominator are not a theorem.

8. **A8's sign for the integer layer price is not a declaration, and it is not in the gap log.** `theory/REPRESENTATION.md:112` says `h ≥ 0` only under A8. `r1_with_layer_count` stops at `h K`. `slope_nonneg_of_nondecreasing` is the real-line case.

9. **Independence of the two variables is one rewrite short of a theorem.** `mutualInfo μ = 0 ↔ μ = (μ.map Prod.fst).prod (μ.map Prod.snd)` follows from `klDiv_zero_iff_eq` and the definition of `mutualInfo`. `theory/CONTINUOUS_A6_2026-11-23.md:111` leads with that biconditional. It is not declared.

## Attacks tried

- Token scan of the project sources, comment-stripping scan, and the axiom audit. Only `propext`, `Classical.choice`, and `Quot.sound`. Count 925 against a 757 baseline.
- Full constant dump split by defining module. Old modules 757, new modules 168. Compared with `git diff` of every pre-existing Lean file.
- Recount of source declarations against every inventory row: file, line, kind, identifier, and the 20 / 6 / 328 split. The batch's 74 names were checked against the environment.
- Smuggling pass over `DebreuAdditive`, `r1_vnm_scale`, `r1_with_layer_count`, and `GYDSup`. Each is an explicit hypothesis. `n_ge` is required to build `DebreuAdditive` and is not referred to in the Cauchy proof. `[Finite γ] [Finite δ]` on `partition_mi_le` is not used; the inequality is data processing for any measurable maps.
- Triviality pass. `klDiv_nonneg` is `zero_le`. The positivity conjuncts of `r1_vnm_scale` repeat `ha1` and `ha2`. `negative_price_example` ends with `(-1) < 0`. No hypothesis was unsatisfiable. `GYDSup` holds for a product measure and, by the identity labeling plus `finite_partition_le`, on a finite alphabet, though that corollary is not packaged.
- Domain pass on Lemma M. The witness is `0` and `e_i`. The linear form from `r1_linear_components` does not feed `r1_zero_of_not_essential`.
- Extended-real pass on `klDiv_prob_integral`, by reading `toReal_klDiv_of_measure_eq` and `klDiv_of_not_integrable` at this Mathlib pin.
- Independent SymPy check of `phi`, the quintic identity `6000 t² φ(t)`, the bracket signs, the root `≈ 0.2362075267`, and `√(1/10)`. The same script checked the Kelly factors `247/200` and `417/400` and the two Lundberg margins before and after the shift `17/10`.
- Kelly objective checked against the first-order condition printed at `theory/DYNAMICS.md:160`, which `REPRESENTATION.md:160` uses for `q* = 0.26`. The Lean objective is that function at the published point. `0.128` is not asserted.
- Searched for a derivative of `θ`, a Shannon-sum expansion of `klDiv`, and a mutual-information chain rule. None is a declaration.
- Wording and personal-information scan of the added lines. Freshness re-run after `origin/main` moved to `d2aeb81`.

Blockers remaining: 0
