# Batch 1 plan

Written before any proof in this batch. Base is upstream `main` at
`d2aeb81` (24 November 2026), which is later than `8c48a5b`. This file
is not revised in place. Later notes are appended at the bottom.

Scope is the packaging in `theory/REPRESENTATION.md` and the
finite-partition and Kullback–Leibler half of
`theory/CONTINUOUS_A6_2026-11-23.md` (OPEN_WORK T48). Debreu's theorem
and the von Neumann–Morgenstern theorem are not proved. The
Gelfand–Yaglom–Dobrushin identification on a general standard Borel
space is not proved. Nothing here is a claim about a real system.

## Statement list

Each row is one declaration family. "Paper" is the sentence being
checked. The Lean name is the one this batch will use.

| Lean name | Paper | What the declaration says |
|---|---|---|
| `cauchy_rat`, `cauchy_monotone`, `cauchy_continuous` | `theory/REPRESENTATION.md:68` Lemma C, both (i) and (ii) through line 74 | On `(0, ∞)`, additivity gives `f(q) = q f(1)` for every positive rational, with no monotonicity. A monotone `f` (either direction) equals `x f(1)`. A continuous `f` equals `x f(1)` with no monotonicity. Both signs of `f(1)` are allowed. |
| `pexider_monotone`, `pexider_continuous` | `theory/REPRESENTATION.md:76` Lemma P | If `f(x+y) = f(x)+f(y)+c` and `f` is monotone or continuous, then `g = f + c` is additive, and `f(z) = p z - c` with `p = g(1)` allowed to be negative. |
| `cauchy_nat` | `theory/REPRESENTATION.md:78` Lemma C on the nonnegative integers | `f(0) = 0` and `f(n) = n f(1)`. No monotonicity and no topology. |
| `slope_nonneg_of_nondecreasing`, `price_zero_of_independent` | `theory/REPRESENTATION.md:80` Lemma M | `z ↦ p z` nondecreasing on `(0, ∞)` implies `p ≥ 0`. If a representing cost does not depend on coordinate `i` through the preorder, then that price is `0`. |
| `r1_linear_components` | `theory/REPRESENTATION.md:84` Theorem R1, proof steps 2–3 at lines 102–110, and the sum of constants at line 118 | **Hypothesis:** Debreu's conclusion, not his theorem. `n ≥ 3` and `C(z) = ∑ f_i(z_i)` with each `f_i` continuous. **Hypothesis:** each concatenating coordinate obeys the Pexider equation. **Conclusion:** `C(z) = ∑ p_i z_i + b`, prices unsigned. |
| `r1_vnm_scale` | `theory/REPRESENTATION.md:100` step 1 and line 118 step 6 | **Hypothesis:** VNM linearity. The same `C` is a positive affine image of one expected-currency index (`C = a · loss + b`, `a > 0`). **Conclusion:** one scale `a > 0` and one real constant, not a second scale. |
| `r1_nonneg_of_A8` | `theory/REPRESENTATION.md:92` and line 120 | **Hypothesis:** A8, each concatenating component nondecreasing. **Conclusion:** each price is `≥ 0`. |
| `r1_zero_of_not_essential` | `theory/REPRESENTATION.md:25` and line 90 | A coordinate the preorder ignores has price `0`. |
| `r1_with_layer_count` | `theory/REPRESENTATION.md:94` and line 112 | **Hypothesis, named as extra:** the integer count is preferentially independent of the interval factors, so `C(z, K) = C_interval(z) + f(K)`. Concatenation of counts then gives `h K`. There is no declaration that drops this hypothesis. |
| `negative_price_example` | `theory/REPRESENTATION.md:90` and line 64 | The cost `z₀ + z₁ - z₂` is continuous and additive and has a negative third price. This is the arithmetic of the example. It does not re-check A6. |
| `affine_argmin_iff`, `strictMono_argmin_iff` | `theory/REPRESENTATION.md:126` | For `a > 0`, `C = a J + b` has the same argmin as `J` on a menu that does not depend on the numerical cost. Any strictly increasing transform does too. |
| `affine_excess_scale`, `affine_excess_eq_iff` | `theory/REPRESENTATION.md:128`–142 | On a fixed measure, `E[C] - C* = a (E[J] - J*)`. The constant `b` cancels. Given `E[J] - J* = d/(2β)` from `Equipartition.gibbs_excess_quadratic`, the excess of `C` equals `d/(2β)` if and only if `a = 1`. |
| `affine_excess_refit` | `theory/REPRESENTATION.md:142` | If the slope is refit by `β_new = β / a`, the excess of `C` under its own Gibbs weight is `d / (2 β_new)`. |
| `fractional_excess_scale`, `fractional_excess_shift` | `theory/REPRESENTATION.md:144`–150 | With `b = 0` the fraction `(E[C]-C*)/C*` equals `(E[J]-J*)/J*`. A nonzero `b` changes the fraction. Concrete rationals, not an estimate. |
| `constrained_argmin_not_affine` | `theory/REPRESENTATION.md:152` | A two-design Lundberg constraint `θ = 2(y - cost) / s² ≥ T`. For `a = 1` and a nonzero shift `b`, the feasible argmin of `J` and of `J + b` are different designs. Variances differ, so this is not an upper bound on the cost alone. |
| `kelly_qstar`, `kelly_foc_sign`, `kelly_not_expected_factor` | `theory/REPRESENTATION.md:160`, with the first-order condition in `theory/DYNAMICS.md:159` | At `β = 1/20`, `a₁ = 13/10`, `b₁ = 21/20`, `b₀ = 9/10`, `a₀ = 0`: the closed form `q* = β a₁ / (a₁ - b₁)` equals `13/50`. It is the unique maximizer of the shared-shock log-growth objective on `(0, 1]`. The per-unit expected factors are `247/200 = 1.235` (lean) and `417/400 = 1.0425` (robust), so the linear objective's unique maximizer is pure lean. The two argmins differ. The printed growth value `0.128` is a rounding in the note and is not given an equality. |
| `expected_cost_interval`, `survival_interval_lt` | `theory/REPRESENTATION.md:162`, exact point in `theory/representation_checks/binding_multiplier.py:16`–21 and `theory/GROWTH_BRIDGE.md:210` | Published point `y = 1`, `c = 1/20`, `α = 1/2`, `β = 1/3`, `s₀² = 9/100`. The expected-cost interval is the unique minimizer `τ_E = √(1/10)` of `c/τ + α τ`. The survival interval is the unique zero `τ_S` of the numerator `φ` of `θ'` on the positive-margin interval, and `τ_S < τ_E`. They are not the same design. The printed four-decimal figures are roundings of these reals; equalities to `0.2362` and `0.3162` are not stated. A rational bracket is added only if it typechecks by exact arithmetic. |
| `klDiv_prob_integral`, `klDiv_nonneg`, `klDiv_zero_iff_eq` | `theory/CONTINUOUS_A6_2026-11-23.md:77` and line 111 | Wrappers on `InformationTheory.klDiv` from `Mathlib.InformationTheory.KullbackLeibler.Basic`. On probability measures the finite-measure correction term is `0`, so the value is the paper's integral, in `[0, ∞]`. It is `0` if and only if the measures are equal. |
| `klDiv_map_le` (used, not re-proved), `mi_swap`, `mi_data_processing` | `theory/CONTINUOUS_A6_2026-11-23.md:145` (symmetry and the data-processing inequality) | Symmetry of mutual information defined as `klDiv` of the joint against the product of the margins, via the coordinate swap. Data processing is Mathlib's `klDiv_map_le`. |
| `klDiv_compProd_chain` | `theory/CONTINUOUS_A6_2026-11-23.md:145` names a chain rule | Mathlib's `klDiv_compProd_eq_add` only. This is not declared to be the mutual-information chain rule `I(X; Y, Z) = I(X; Z) + I(X; Y \| Z)`. That identification is a puzzle if it does not typecheck; it is not replaced by a weaker equation. |
| `partition_mi_le`, `refinement_mono`, `finite_identity_attains` | `theory/CONTINUOUS_A6_2026-11-23.md:99` and line 101 | Finite measurable maps do not raise `klDiv` (`klDiv_map_le`). A finer partition is a measurable function of a coarser one, so the discrete mutual information does not fall. On a finite alphabet the identity map attains the value. |
| `GYDSup` | `theory/CONTINUOUS_A6_2026-11-23.md:91` and line 21 | **Explicit hypothesis.** The reverse inequality: joint `klDiv` is at most the supremum of finite-partition mutual informations. Not constructed and not proved. `gyd_equiv` is the equivalence obtained by adding this hypothesis to the proved inequality. |

Reused, not restated:

- `Equipartition.gibbs_excess_quadratic` (`formal/lean/GTAO/Equipartition.lean`) is the identity `E[J] - J* = d/(2β)` inside `affine_excess_eq_iff` and `affine_excess_refit`.
- `InformationTheory.klDiv`, `klDiv_eq_zero_iff`, `klDiv_map_le`, and `klDiv_compProd_eq_add` are the Kullback–Leibler facts. They are not copied into this repository as new proofs.
- `FiniteDesignMenu.J_affine` is affinity of `S + w E` in the stake. It is a different statement from `a J + b` and is not used as a substitute.
- `LundbergCertified`, `Bmin`, and `Bslack` stay as they are. The constrained-menu witness is a two-design margin calculation. It does not rewrite those declarations.

No existing declaration is deleted or given a new statement.

## Why this approach

The notes already separate known theorems from the packaging. The
formalization follows that split. Lemmas C, P, C on the integers, and M
are elementary and are proved from the field operations, density of the
positive rationals, and the definitions of monotone and continuous.
Pathological additive functions are excluded by those hypotheses, as
the note says at line 74; their existence is not formalized.

Theorem R1 is a packaging of Debreu's conclusion and of von
Neumann–Morgenstern linearity with concatenation. Those two results
stay hypotheses, with `n ≥ 3` on the Debreu side and `a > 0` on the
currency side. One cost function carries both, so the note's "one
scale" (line 118) is one symbol, not a derived coincidence of two
scales. A8 and the mixed-product separability of `h K` stay hypotheses
because the note says the citations do not prove them (lines 94 and
120).

The affine block is algebra plus one call to the existing Gibbs
excess. The fixed-measure reading and the refitted-slope reading are
separate declarations, matching lines 134–142.

Theorem R2 is two witnesses. Kelly is the closed form and the sign of
the derivative of shared-shock log growth, against a linear expected
factor. Lundberg is the unique positive critical point of `c/τ + α τ`
against the unique zero of `φ` on `{m > 0}`. Both are exact rationals
and one square root. No decimal equality is asserted.

T48 uses Mathlib's Kullback–Leibler divergence rather than a second
definition. The data-processing inequality already in that module gives
monotone refinement and the finite-alphabet attainment. The direction
Mathlib does not have, the general Borel supremum, is a hypothesis
named `GYDSup`.

## Can it fail, and the cheapest repair

Can it fail: the monotone Cauchy argument needs a rational sequence on
each side of `x` and a sign for `f(1)`. A proof that imports a Mathlib
additive-function theorem on all of `ℝ` would change the domain and
would silently drop the note's split between (i) and (ii).

Cheapest way: prove `f(n x) = n f(x)` by induction for positive
integers, build the rational sequences with `exists_rat_btwn` and
`Classical.choose`, and squeeze. Do not cite a stronger theorem in
place of (i) or (ii).

Can it fail: `InformationTheory.klDiv` adds `ν(univ) - μ(univ)` for
finite measures. That is not the integral in
`theory/CONTINUOUS_A6_2026-11-23.md:77` unless both measures are
probabilities.

Cheapest way: state the integral identity only for probability
measures, where `toReal_klDiv_of_measure_eq` kills the correction.
Do not claim the paper's formula for a general finite measure.

Can it fail: the mutual-information chain rule needs a regular
conditional, and `klDiv_compProd_eq_add` is a kernel identity. Forcing
them to be the same definition may not typecheck.

Cheapest way: keep `klDiv_compProd_chain` as Mathlib's statement. If
the conditional mutual-information chain rule does not typecheck from
it, append a puzzle here and do not declare a substitute.

Can it fail: `Matrix.PosDef` of `a • H` may not be a one-line lemma in
this Mathlib pin, which blocks `affine_excess_refit`.

Cheapest way: prove `0 < a → H.PosDef → (a • H).PosDef` from
`dotProduct_mulVec_pos`. If that fails, keep the fixed-measure
statement, which only calls `gibbs_excess_quadratic` for `H`, and
record the refit as a puzzle rather than changing its statement.

Can it fail: a rational bracket for `τ_S` around `0.2362` is a large
exact-arithmetic goal even though `φ` at a rational point is rational.

Cheapest way: the inequality `τ_S < τ_E` is the claim that the designs
differ (line 162). Ship that. Add the bracket only if `norm_num` closes
it. Do not assert `τ_S = 0.2362`.

Can it fail: product-map measurability for `partition_mi_le` can stall
on the module system's `public` visibility.

Cheapest way: quantify over measurable maps into finite types and apply
`klDiv_map_le` to the product map. If the product map will not
typecheck, stop that declaration and append the goal that failed. Do
not replace refinement by a finite-sum inequality that is not the
note's statement.

Can it fail: a new `axiom`, `sorry`, or `native_decide` would fail
`scripts/AxiomAudit.lean`. `Classical.choose` is already in the allowed
set (`Classical.choice`).

Cheapest way: no new axiom. Sequences and existentials use `choose`.

## What either outcome changes

If these declarations typecheck with only `propext`, `Classical.choice`,
and `Quot.sound`, batch 1 has machine-checked the packaging it claims
and nothing past it. The next representation batch can take
`C = a (∑ p_i z_i) + b` and the probability-measure `klDiv` API as
inputs. It still has to supply Debreu, von Neumann–Morgenstern, and
`GYDSup` where a later statement needs the missing direction. Batch 4
(T73, T74) asks what fixes the ratio of two record prices. The one-scale
declaration here multiplies the whole sum by one `a`. It does not fix a
ratio of prices, and it should be cited that way rather than re-proved.
Batches 2, 3, and 5 are about heat, repair, the clock, and other
structural lemmas. They do not depend on this packaging, and this batch
does not start them.

If a statement will not typecheck, or typechecks only after an
assumption the paper does not name, that assumption is appended below
as a puzzle with file and line. The declaration is not weakened to make
the build pass, and it is not left out without a line in this file. The
next step is to name the assumption in the note that states the claim,
or to mark the Lean declaration WEAKER in `formal/lean/README.md` and
`OPEN_WORK.md` with the reason, before any later batch uses it.
`THEORY.md` and `CORE.md` stay untouched either way.

## Appendix (appended only)

The conditional mutual-information chain rule does not typecheck from
`klDiv_compProd_eq_add`. Mathlib's `KullbackLeibler/ChainRule.lean` at
pin `v4.37.0-rc1` proves
`klDiv (μ ⊗ₘ κ) (ν ⊗ₘ η) = klDiv μ ν + klDiv (μ ⊗ₘ κ) (μ ⊗ₘ η)`
and records that the integral form `μ[x ↦ klDiv (κ x) (η x)]` is not
proved. `ContinuousA6.klDiv_compProd_chain`
(`formal/lean/GTAO/ContinuousA6.lean`) is that kernel identity.
`theory/CONTINUOUS_A6_2026-11-23.md:145` also names
`I(X; Y, Z) = I(X; Z) + I(X; Y | Z)`. No declaration equates the two,
and no weaker equation is substituted.

`survival_interval_lt` proves that the unique zero of `φ` on `(0, 2]`
lies in `(23615/100000, 189/800)` and is strictly below `√(1/10)`.
It does not prove that this zero is a maximizer of `θ = 2m/s²`.
A derivative of `θ` was not constructed, so the sign link from `φ` to
`θ'` is not a theorem. The shipped comparison is the one in
`theory/REPRESENTATION.md:162`: the two intervals are not the same
design. The printed figures `0.2362` and `0.3162` are not equalities.
The declaration is labeled **WEAKER** for that missing maximality.

`klDiv_prob_integral` now takes `Integrable (llr μ ν) μ` and concludes
`klDiv μ ν = ENNReal.ofReal (∫ llr ∂μ)` on probability measures.
Without that hypothesis, `toReal` of `klDiv` and the Bochner integral
are both `0` when the log-likelihood is not integrable. That equality
of reals is not the extended value, so it is not the statement.

`price_zero_of_independent` uses the linear form only on strictly
positive vectors. The two witnesses are the constant-`1` vector and the
vector that is `2` in the ignored coordinate.

`r1_vnm_scale` is labeled **WEAKER**. It equates two positive affine
writings of one index. Debreu's scale is not in the statement.
