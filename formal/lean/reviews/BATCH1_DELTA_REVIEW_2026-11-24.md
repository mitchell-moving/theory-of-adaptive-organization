# Delta review of Lean batch 1

Reviewed head `d12642bae87f3bc2cb8ce39de882fa2dd35301f2` on `forge-lean-batch1`. The range is `ff47adb..d12642b`. That range is the one commit `d12642b` ("Correct the batch 1 labels that overclaimed the paper sentences"). `git rev-parse origin/forge-lean-batch1` is the same SHA. Nothing on the branch sits after it. The prior review is the comment on fork pull request 17 at `ff47adb394e23fced1a279034f3ebaa2b2f8e8ad`. This file does not edit `THEORY.md` or `CORE.md`, and it does not edit `forge-lean-batch1`.

The diff is 8 files, 122 insertions and 54 deletions: `OPEN_WORK.md`, `formal/lean/BATCH1_PLAN.md`, `formal/lean/README.md`, `formal/lean/INVENTORY.md`, and the four modules `GTAO/Cauchy.lean`, `GTAO/ContinuousA6.lean`, `GTAO/Obstruction.lean`, and `GTAO/Representation.lean`.

## Machine checks

Toolchain `leanprover/lean4:v4.37.0-rc1`. Mathlib pin `31ce06eaadf4a200c0e1407c5f10953cf606b8f8`. Build checkout `/tmp/gtao-lean` at this head.

`tools/check_lean.sh` exits 0. It runs `lake exe cache get`, then `lake build` (`Build completed successfully (6475 jobs)`), then `scripts/AxiomAudit.lean`. The audit line is `AxiomAudit: OK (926 GTAO declarations; only propext, Classical.choice, Quot.sound)`.

The same script's token scan, before the build, rejects `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, and `implemented_by` in `GTAO.lean` and `GTAO/*.lean`. A separate search of `formal/lean/**/*.lean` for `opaque`, `sorry`, `admit`, and `native_decide` finds one `sorry`, in a comment in `scripts/AxiomAudit.lean:10`. No `opaque`. No `native_decide`. No `admit`.

The audit count at `ff47adb`, as recorded in the prior review comment, was 925. This head is 926. The signed difference is +1. The only source declaration added in the range is `r1_layer_price_nonneg_of_A8`. A parse of `theorem`, `lemma`, `def`, `abbrev`, `structure`, and `instance` gives 26 names in `Cauchy.lean`, 17 in `Representation.lean`, 16 in `Obstruction.lean`, and 16 in `ContinuousA6.lean`, which is 75. Against `ff47adb` the same parse adds one name and removes none. The inventory's three **WEAKER** rows are `r1_vnm_scale`, `negative_price_example`, and `survival_interval_lt`. 75 − 3 = 72 **Faithful**. Those two sentences in `formal/lean/INVENTORY.md` match the parse.

`python3 tools/check_consistency.py` exits 0. Maintained documents scanned: 31. Wording misses in those documents: 0. Frozen-record INFO hits: 29. Process-rule misses: 0. Core-rule misses: 0. The length notes are the advisory already printed for `THEORY.md` (11325 words, advisory reference 5500) and `README.md` (1857 words, advisory reference 900).

`python3 -m pytest -q` from the same checkout exits 0. 291 passed in 491.77s. Skipped: 0. `tools/test_lean.py` is in that run: lake is installed, and the dedicated checkout is this head, so the build test runs rather than skipping.

## How a label is read

`formal/lean/INVENTORY.md` states the rule used here. **Faithful** means the checked statement is the paper sentence, with every extra hypothesis named. **WEAKER** means a clause of the paper sentence is absent from the declaration. The Lean comments cite `theory/REPRESENTATION.md` and `theory/CONTINUOUS_A6_2026-11-23.md`. `CORE.md:50` points the priced-sum claim at the representation note. `CORE.md:155` points the continuous A6 claim at the divergence note. `THEORY.md:39` is the one-paragraph form of the same representation claim. `THEORY.md:404` (Lemma B9) is the survival-versus-cost sentence. Those four locations are the `THEORY.md` / `CORE.md` sentences checked below.

## Changed declarations

Seven declarations change text. Five change a statement or a proof. Two change the docstring that carries the label. One of the five is new.

### `IndependentOf`, `price_zero_of_independent`, `r1_zero_of_not_essential`

Locations: `formal/lean/GTAO/Cauchy.lean:314`, `:320`, and `formal/lean/GTAO/Representation.lean:92`.

Cited sentence: `theory/REPRESENTATION.md:80`, Lemma M, second sentence: a coordinate that is not essential has price zero, because the preorder does not depend on it. The same sentence is at `:25` and `:90`. `CORE.md:52` states the priced sum, one positive scale, A8 for nonnegative prices, and separability for the integer layer count. It does not state the zero-price sentence. `THEORY.md:39` states additivity on a product of intervals, and that nonnegative prices need each concatenating coordinate to be a bad. The zero-price sentence is in the note those two lines point at.

`IndependentOf` is now: for all vectors `x` and `y`, if every coordinate of each is strictly positive, and `x` and `y` agree off `i`, then the preorder ranks them both ways. The quantifier is universal on the strict positive orthant. That is the domain of Lemma C at `theory/REPRESENTATION.md:68`, the interval `(0, ∞)`. It is not an existential.

The linear-form hypothesis is `∀ z, (∀ j, 0 < z j) → C z = ∑ j, p j * z j + b`. The orthant guard is in the signature.

The witnesses are the constant-`1` vector and the vector that is `2` in coordinate `i`. Both are strictly positive. The coordinatewise difference is `1` at `i` and `0` elsewhere, so the summed difference is `p i`. The conclusion is `p i = 0`.

`Represents` at `Cauchy.lean:310` is still `∀ x y, R x y ↔ C x ≤ C y`, with no positivity guard. The proof instantiates it at the two positive witnesses and nowhere else. The extra instances sit in that named hypothesis. The README sentence says the preorder is used on the positive orthant. That matches the two instantiations. The hypothesis still asks for the biconditional off the orthant. That extra width makes the hypothesis stronger than the product-of-intervals sentence, which is the safe direction: the conclusion stays `p i = 0`. Signed size of the use: 2 vectors, both strictly positive, against a hypothesis that quantifies over every real vector. This is not a swapped quantifier in `IndependentOf` or in the linear form. The label **Faithful** matches Lemma M's second sentence on `(0, ∞)`. The witness that left the orthant, at the zero vector, is gone.

### `klDiv_prob_integral`

Location: `formal/lean/GTAO/ContinuousA6.lean:36`.

Cited sentence: `theory/CONTINUOUS_A6_2026-11-23.md:77`. For probability measures, `D_KL` in `[0, ∞]` is the integral of the log-likelihood when one measure is absolutely continuous with respect to the other, and `+∞` otherwise. `CORE.md:155` states the finite-integral case: when the densities exist and the integral is finite, the memory coordinate agrees with the differential mutual information. The infinite case is the boundary at `theory/CONTINUOUS_A6_2026-11-23.md:139`. Theorem R1 is not applied there.

The declaration assumes probability measures, `μ ≪ ν`, and `Integrable (llr μ ν) μ`, and concludes `klDiv μ ν = ENNReal.ofReal (∫ llr ∂μ)`. Integrability is named in the signature, the docstring, `formal/lean/README.md`, `formal/lean/INVENTORY.md`, and the appended paragraph of `formal/lean/BATCH1_PLAN.md`.

At this Mathlib pin, `klDiv` is `ENNReal.ofReal` of `∫ llr + ν.real univ − μ.real univ` when absolute continuity and integrability both hold, and `⊤` otherwise (`klDiv_of_ac_of_integrable`, `klDiv_of_not_ac`, `klDiv_of_not_integrable` in `Mathlib/InformationTheory/KullbackLeibler/Basic.lean`). For probability measures both masses are 1, so the correction term is 0. The local equality in the proof is that cancellation, and `simpa` rewrites `klDiv_of_ac_of_integrable`. The build accepts the proof.

The finite absolutely continuous case, with integrability named, is the paper's integral in `[0, ∞)`. `ENNReal.ofReal` is the embedding of a nonnegative real; Mathlib's Gibbs lemma at this pin shows the corrected integral is nonnegative, and here the correction is 0. The `⊤` branch, when absolute continuity fails or the log-likelihood is not integrable, is Mathlib's definition and is not a second declaration. The docstring records that branch: without integrability Mathlib sets `klDiv` to `⊤`, and `toReal` of that value is `0`, which is the real collapse the previous statement equated. That statement is no longer the theorem. The label **Faithful** is the finite case. It matches `CORE.md:155`'s finite-integral clause.

### `r1_layer_price_nonneg_of_A8`

Location: `formal/lean/GTAO/Representation.lean:110`. New in this commit.

Cited sentence: `theory/REPRESENTATION.md:112`. The sign of `h` is nonnegative under A8. A8 at `:64` says each concatenating coordinate is a bad: at fixed values of the others, a larger value is weakly worse. `CORE.md:52` and `THEORY.md:39` state the same extra assumption for nonnegative prices.

The statement assumes `∀ m n, fn (m + n) = fn m + fn n` and `∀ m n, m ≤ n → fn m ≤ fn n`, and concludes `0 ≤ fn 1`. Both quantifiers are universal. Additivity is Lemma C on the nonnegative integers (`theory/REPRESENTATION.md:78`). Monotonicity is A8 read as a cost: `Represents` at `Cauchy.lean:310` puts the smaller cost on the preferred side, so weakly worse is a larger or equal cost. The direction is nondecreasing. It is not nonincreasing.

The proof takes `fn 0 = 0` from `cauchy_nat`, then `fn 0 ≤ fn 1` from monotonicity at `0 ≤ 1`. The build accepts it. Separability of the layer count is the hypothesis of `r1_with_layer_count`, which this range does not change. The sign of `fn 1` does not use it. The label **Faithful** matches the sufficient direction of `:112`. The word "only" in that sentence is the caveat that A1–A7 do not give the sign. The theorem assumes the monotonicity and concludes the sign. A necessity claim, that every additive count without monotonicity takes a negative value at 1, is not this declaration.

### `survival_interval_lt`

Location: `formal/lean/GTAO/Obstruction.lean:285`. The statement is unchanged. The docstring no longer calls the zero the survival interval. It says maximality of `θ` is outside the declaration. The README and the inventory now mark the declaration **WEAKER**.

Cited sentence: `theory/REPRESENTATION.md:162`. On the published point the survival-optimal interval is `0.2362` and the expected-cost interval is `0.3162`, and they are not the same design. `THEORY.md:404`, Lemma B9 (L2), says the survival-optimal interval is shorter than the cost-optimal one.

The declaration proves a unique zero of `φ` on `(0, 2]` inside `(23615/100000, 189/800)`, strictly below `√(1/10)`, with `√(1/10)` inside `(31622/100000, 31623/100000)`. An expansion in exact rationals gives `6000 t² φ(t)` equal to the shipped quintic at both bracket ends and at three further positive rationals. `φ(23615/100000) > 0` and `φ(189/800) < 0`. Bisection puts a root at `0.2362075267`. The signed gap from that root to the printed `0.2362` is `+7.53×10⁻⁶`. `√(1/10) − 0.3162 = +2.78×10⁻⁵`. The declaration does not equate the printed four-decimal figures. The clause that is absent is maximality of `θ`: the zero is not shown to be the survival-optimal interval of `:162` or of Lemma B9 (L2). **WEAKER** matches the inventory's rule. The previous **Faithful** label is the one this commit removes.

### `r1_vnm_scale`

Location: `formal/lean/GTAO/Representation.lean:57`. The statement is unchanged. The docstring and the label now say **WEAKER**.

Cited sentence: `theory/REPRESENTATION.md:118`. The currency regraduation and Debreu's common scale are the same `a`, because the cost is already the von Neumann–Morgenstern index, and the constants sum to one `b`. `CORE.md:52` states one positive scale and one additive constant.

The theorem assumes two positive affine writings of one index, `a1 > 0` and `a2 > 0`, and a pair of points where the index takes different values, and concludes `a1 = a2`, `b1 = b2`, and `0 < a1 ∧ 0 < a2`. The last two conjuncts are the hypotheses `ha1` and `ha2`. They were already in the conclusion at `ff47adb`. Debreu's scale does not appear. The missing clause is that identification. **WEAKER** matches `:118` and the "one positive scale" clause of `CORE.md:52`.

### Label text that does not change a declaration

`fractional_excess_scale` and `fractional_excess_shift` are unchanged as Lean statements. The inventory and the README now say the general quotient `(a (E[J] − J*)) / (a J* + b)` is not a theorem, and that the checked cases are `b = 0` and the rationals `E[J] = 2`, `J* = 1`, `b = 1`. That is the scope the statements have.

`DriftSelection.trace_mul₃_herm` is the lemma at `formal/lean/GTAO/DriftSelection.lean:150`. The inventory row now uses that name. The declaration was not renamed.

`negative_price_example` at `Representation.lean:119` is unchanged. It stays **WEAKER**: arithmetic and continuity of `z₀ + z₁ − z₂`, with the third price equal to `-1`. `theory/REPRESENTATION.md:64` and `:90` also say the example satisfies A1–A7. Those clauses stay outside the declaration.

`OPEN_WORK.md`'s T19 sentence records the same four label moves: integrability on `klDiv_prob_integral`, orthant witnesses for the zero price, the new layer-price declaration, and the **WEAKER** marks on `survival_interval_lt` and `r1_vnm_scale`. It does not say the zero of `φ` maximizes `θ`.

## Attacks tried

- Rebuilt at this head with `tools/check_lean.sh` in `/tmp/gtao-lean`. Audit count 926, allowed axioms only. Signed difference from the recorded 925 at `ff47adb` is +1, against one new source declaration.
- Token search of `formal/lean/**/*.lean` for `opaque`, `sorry`, `admit`, and `native_decide`, in addition to the script's scan.
- Parsed source declarations in the four modules at both ends of the range. One name added, none removed. 26 + 17 + 16 + 16 = 75. Three **WEAKER** rows, so 72 **Faithful**.
- Read `klDiv_of_ac_of_integrable`, `klDiv_of_not_ac`, and `klDiv_of_not_integrable` at Mathlib `31ce06ea`. The probability-measure correction is `1 − 1`. The finite-case statement matches that lemma. The previous `toReal` collapse is not the conclusion.
- Quantifier check on `IndependentOf`, the orthant linear form, and `r1_layer_price_nonneg_of_A8`. Universals stay universal. The monotonicity direction is nondecreasing cost, which is A8 at `theory/REPRESENTATION.md:64` under `Represents`.
- Counted instantiations of `Represents` inside `price_zero_of_independent`: the constant-`1` vector and the vector that is `2` at the ignored coordinate. Difference `+1` in that coordinate.
- Exact-rational check of `6000 t² φ(t)` against the quintic, the bracket signs, a bisection root `0.2362075267`, and `√(1/10)`. Signed gaps to the printed four-decimal figures: `+7.53×10⁻⁶` and `+2.78×10⁻⁵`, at `theory/REPRESENTATION.md:162`. The declaration does not assert those equalities.
- Compared each changed statement with the sentence at `theory/REPRESENTATION.md` or `theory/CONTINUOUS_A6_2026-11-23.md`, and with `CORE.md:52`, `CORE.md:155`, `THEORY.md:39`, and `THEORY.md:404`.
- `python3 tools/check_consistency.py` and `python3 -m pytest -q` on this head, as recorded above.

Blockers remaining: 0
