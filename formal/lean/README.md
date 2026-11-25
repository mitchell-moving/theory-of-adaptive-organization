# Lean 4 formalization of the GTAO core (OPEN_WORK T19)

This directory is a Lean 4 + Mathlib project.  It machine-checks a
finite-menu fragment of the core in `THEORY.md` (canonical) and `CORE.md`,
and (since 21 November 2026, PR #147) four further core results: the
layer-lifetime optimum `T* = √(6k/(wσ²))` as the minimizer of the
repository's zero-discount average cost, the local-vs-shared crossing
(D5), the selection-axioms stationary excess `E_π[J] − J* = d/(2β)`
(equipartition, SA1b), and the lower-hull increment test equals argmin
for an arbitrary `ε` (KEYSTONE_NOTE §4).  This branch adds the
from-0 layer-count exactness lemma (L1 / N64), the finite-cell band-model
convexity theorems (M, Z, X, B) with the `W ≥ 0` necessity check, a
finite-state CA1 / CA1a statement, the Lyapunov-trace identity for
the drift-selection excess DS1, including `d/(2β)(1+D/D_m)`, and
(this branch, batch 2) the DS2 lag and cost bounds, uniqueness of
the CA1 stationary law, CA1b/CA1c (U2), and CA7 (U11) on the
load-bearing chain.
Formalization cannot establish the hypothesis at the top of CORE.md, which is a claim
about the real world.

- Toolchain: `lean-toolchain` pins `leanprover/lean4:v4.37.0-rc1`.
- Mathlib: `lakefile.toml` and `lake-manifest.json` pin `v4.37.0-rc1`.
  This is a release candidate, not a stable tag.  It is pinned because
  this formalization uses Lean 4.37's module system (`module`,
  `public import`, `@[expose] public section`), which is not in the
  previous stable (`v4.36.0`); Mathlib's published `lean-toolchain` at
  the time of the formalization resolved to `v4.37.0-rc1`, and the
  Mathlib olean cache at `cache.mathlib.org` serves that pin.  A later
  bump to the next stable Lean/Mathlib tag is open work.
- Build: from the repo root, `tools/check_lean.sh` (or, in this
  directory, `lake exe cache get` then `lake build`).
- There is no `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, or
  `implemented_by` in the project sources (`GTAO.lean`, `GTAO/*.lean`).
  The checker searches only those files, not `.lake/` or
  `lake-packages/`.  Anything not listed as proved below is
  **not formalized**, not “proved with a hole.”
- Axiom audit: `scripts/AxiomAudit.lean` (run by `tools/check_lean.sh`
  after the build) checks that every declaration in a `GTAO.*` module
  depends only on `propext`, `Classical.choice` and `Quot.sound`.  A
  `sorry` anywhere would show up as `sorryAx` and fail the check.  Last
  run (22 November 2026, branch `lean-batch2-2026-11-21`, after the
  batch-2 confirm nits): 757 declarations, OK
  (635 after the lean-layer-drift review should-fixes, plus batch 2,
  its should-fixes, and the confirm nits).
  Batch 1 (24 November 2026, branch `forge-lean-batch1`, after the
  label corrections): 926 declarations, OK. The 169 constants above 757
  are the four new modules. 75 of them are the source declarations in
  the batch 1 table; the rest are generated.
  Batch 2 (24 November 2026, branch `forge-lean-batch2` at `6663d0e`,
  merged as PR #266): 1185 declarations, OK. The 259 constants above 926
  are the four batch 2 modules.

## How to build

Lean 4 is installed with [elan](https://github.com/leanprover/elan).
Then, from this directory:

```bash
lake exe cache get   # cached Mathlib oleans; do not compile Mathlib from source
lake build
```

`tools/check_lean.sh` does the same and also rejects `sorry`, `admit`,
`axiom`, `native_decide`, `unsafe`, and `implemented_by` in project
sources (not in `.lake/` or `lake-packages/`), then runs the axiom audit
(`lake env lean scripts/AxiomAudit.lean`).  Builds run at `nice -n 19`.
The pytest wrapper `tools/test_lean.py` runs that script whenever `lake`
is on `PATH` or in `~/.elan/bin`, and skips cleanly if Lean is not
installed.

## Mapping: Lean declarations to THEORY CT numbers

Hypotheses are part of the claim.  A finite nonempty design set, and a
stake-independent menu (ruin slack or absent), are standing hypotheses
wherever `FiniteDesignMenu` is used.

"CORE §" numbers below refer to earlier versions of the one-pager, kept in `history/` (`2026-11-21_CORE_before_onepage.md`, `2026-11-21_CORE_before_shannon.md`, `2026-11-22_CORE_before_front.md`). The current `CORE.md` was rewritten on 22 November 2026 and has different section numbers.

| Lean name | THEORY / source | What is assumed | What is proved |
|---|---|---|---|
| `FiniteDesignMenu.J` | CORE §1, THEORY §3 | Finite menu; `J = S + w E`; ruin slack or absent, so the menu does not depend on `w` | Definition of the split cost |
| `FiniteDesignMenu.exists_minimizer` | CT20 (i), finite case | `𝒟` nonempty and finite | A minimizer exists at every stake |
| `FiniteDesignMenu.Jstar`, `Jstar_concave`, `IsOptimal.Jstar_eq`, `Jstar_le_affine` | CT33 envelope | Same finite menu | `J*` is the min of affine functions of `w`, hence concave on `ℝ`, with supporting slope `E` at an optimum |
| `FiniteDesignMenu.optimality_inequalities`, `error_diff_sign` | CT33 | Same; two optima at `w₁`, `w₂` | The two revealed-preference inequalities, and `(w₂−w₁)(E₂−E₁) ≤ 0` |
| `FiniteDesignMenu.error_nonincreasing` | CT33 | `w₁ < w₂` (strict: at a tie, two optima may differ in error) | `E*` is nonincreasing |
| `FiniteDesignMenu.spend_nondecreasing` | CT33 | `0 ≤ w₁ < w₂`; ruin slack or absent | `S*` is nondecreasing |
| `FiniteDesignMenu.spend_nondecreasing_in_R` | CT33 | `h > 0` and the same stake hypotheses | `S*/h` is nondecreasing in `w` (equivalently in `R = w/h` at fixed `h`) |
| `FiniteDesignMenu.layer_count_bound` | CT20 (i) bound | `h > 0`, `h K ≤ S`, `0 ≤ w E` (so `J ≥ h K`) | Any design matching or beating a reference `d₁` has `K ≤ J(d₁;w)/h` |
| `FiniteDesignMenu.layer_count_nondecreasing` | CT20 (ii), sensing fixed | Spend is exactly `h K` with `h > 0`; `0 ≤ w₁ < w₂`; menu independent of `w` | The layer count itself is nondecreasing.  This fails once reads are also chosen (THEORY's counterexample); total spend still obeys CT33 |
| `effortJ_decreasing_differences`, `effort_nondecreasing` | CT10 | Error is nonincreasing along a frequency coordinate; check price `c > 0`; `w₁ < w₂` | Decreasing differences, and the discrete Topkis conclusion: optimal effort does not fall as stakes rise |
| `jointOptimal_iff`, `exact_nesting_value` | CT34 (i) | Parent and team design sets finite and nonempty; `J(x,y)=F(x)+G(y;θ(x))` | Partial minimization is exact, and the minimizers agree |
| `parentOptimal_of_constant_theta` | CT34 (ii) | `θ` does not depend on the parent's design | The team's optimized cost is a constant (an upkeep); the parent's argmin is the argmin of `F` alone |
| `strongConvex_lipschitz_gap`, `weak_coupling_pointwise`, `weak_coupling_gap`, `weak_coupling_parent_regret` | CT34 (iii) | `μ > 0`, `ε ≥ 0`; `G` satisfies the strong-convexity inequality in a distance `dist`; `Φ` is `L`-Lipschitz in `y` in the one-sided sense used in THEORY | Freezing the team at a `G`-minimizer overshoots by at most `(ε L)²/(2μ)`, and the parent's regret from optimizing the frozen cost is at most that bound.  The coupling sign `ε ≥ 0` is stated (needed to keep the Lipschitz bound's direction) |
| `D_comp_IB_convex`, `L_convex` | CT4, convex lower bound | `D` convex and nonincreasing on the image of `IB`; `IB` concave on `s` | `D ∘ IB` is convex, and `L(I)=D(IB(I))+κ I` is convex (the `κ I` term is affine at every sign of `κ`).  That `L` is a lower bound on cost is not formalized |
| `zero_isMinOn_iff`, `not_minOn_zero_iff_neg_right_slope`, `pos_min_of_neg_right_slope`, `exists_neg_right_slope_of_not_min` | helpers (right slopes of an arbitrary `L`) | None beyond `L : ℝ → ℝ` and the stated point in `[0, ∞)` | `0` is a minimizer iff every right slope from `0` is nonnegative; hence `0` fails to minimize iff some right slope is negative, and any minimizer is then strictly positive.  These are not the CT4 first-bit criterion |
| `L_right_slope`, `first_bit_sign`, `first_bit_positive_minimizer` | CT4, first-bit sign | `L(I)=D(IB(I))+κ I`; stated with right slopes from `0` on `[0, ∞)`, not a two-sided derivative | Every right slope of `L` from `0` equals the corresponding right slope of `D ∘ IB` plus `κ`.  Therefore `0` fails to minimize `L` iff `∃ x > 0, (D(IB x)−D(IB 0))/x + κ < 0`.  This is THEORY's `κ < -(D∘IB)'(0⁺)` in slope form: if the right derivative exists, it is the infimum of those slopes (for convex `D∘IB`).  A minimizer, if one exists, is then strictly positive.  Existence of a minimizer on `[0, ∞)` is not proved |
| `not_certified_below_Bmin` | CT22, certified `B_min` | `0 < max θ`, `0 ≤ B < B_min` | No design is Lundberg-certified (THEORY's wording: the bound is sufficient, not that every design ruins).  THEORY also takes `0 < ε < 1`, which makes `B_min` positive (`Bmin_pos`) so that the interval is inhabited; the comparison itself is algebraic in `log(1/ε)` |
| `certified_at_Bslack` | CT22, `B_slack` | `θ(d_E) > 0`, `B ≥ B_slack` | The expected-cost optimum is certified |
| `expected_cost_opt_at_or_above_Bslack` | CT22, slack case | `d_E` minimizes `J` over all designs; `θ(d_E) > 0`; `B ≥ B_slack` | `d_E` is Lundberg-certified and is therefore optimal among certified designs; the cap is slack.  Composes `certified_at_Bslack` with that restriction.  No KKT is used |
| `Bmin_le_Bslack` | CT22 | `0 < ε < 1`, `0 < θ(d_E)` (hence `0 < max θ`) | `B_min ≤ B_slack` |
| `minimizer_on_lower_hull` | KEYSTONE_NOTE §4, first sentence | `R ≥ 0`; `φ(K)=K+R(1+ε_K)` on `{0,…,n}` | Every minimizer of `φ` lies on the lower convex hull of `{(K, ε_K)}` |
| `n60_from_zero_leftmost` | KEYSTONE_NOTE §4, adjacent test | `R ≥ 0` and discrete convexity of `ε` (first differences nondecreasing) | Walking from `0` and taking every paying adjacent step returns a leftmost minimizer of `φ` |
| `n60_as_written_zero_hole` | N60 as written; the `K*=0` hole | Same, and the first step does not pay | No later step pays, and the true leftmost minimizer is `0`.  The cardinality formula `1 + #{k ≥ 2 : step k−1 pays}` is not defined in Lean, so the theorem does not conclude that N60 as written equals `1` (those two ingredients are what would make it equal `1`) |
| `LayerLifetime.cost`, `Tstar`, `cost_ge`, `Tstar_isMin`, `Tstar_unique`, `cost_Tstar` | CORE §3; `theory/LAYER_LIFETIME_2026-11-21.md` §2 (CL19 (a)) | The zero-discount average cost of a lumpy layer is `C(T) = k/T + c·wσ²·T` with `c·wσ² > 0`, `k > 0`; the stochastic derivation of that expression (mean exit time `b²/σ²`, time-average square gap `b²/6`; Dixit 1991, exact at zero discount per Chalkley 1997) is **assumed**, not formalized | On `T > 0`, `C` has the unique minimizer `T* = √(k/(c wσ²))`, with minimum `2√(c k wσ²)` (AM–GM identity `C(T) − 2√(k a) = (√a T − √k)²/T`) |
| `LayerLifetime.layer_lifetime` | CORE §3, `T* = √(6k/(wσ²))` | Barrier coefficient `c = 1/6`; `k, w, σ² > 0` | `T* = √(6k/(wσ²))` is the unique minimizer of `k/T + wσ²T/6` on `T > 0`, with minimum `2√(kwσ²/6)` |
| `LayerLifetime.fixed_period_lifetime`, `barrier_eq_sqrt3_fixed` | LAYER_LIFETIME §2, fixed-period cousin | `c = 1/2`; `k, w, σ² > 0` | `T*_fix = √(2k/(wσ²))` minimizes `k/T + wσ²T/2`, minimum `√(2kwσ²)`; the barrier lifetime is `√3` times the fixed-period one |
| `LayerLifetime.Tstar_scale_k`, `lifetime_ratio` | CORE §3 (`√k` scaling); LAYER_LIFETIME §3a (Model LS spacing) | `r ≥ 0`; for the ratio, `c, w > 0`, `k_j > 0`, `σ_i², σ_j² > 0`, equal stakes | `T*(r k) = √r · T*(k)`; `T*_i/T*_j = √((k_i/k_j)(σ_j²/σ_i²))` |
| `LayerLifetime.barrier_band_identities` | `theory/SELECTION_AXIOMS.md` SA2 proof | `k, w, σ² > 0`; `b*² = √(6kσ²/w)` | `w b*²/6 = kσ²/b*² = √(kwσ²/6)`, and `b*²/σ² = T*` |
| `LocalShared.localCost`, `sharedCost`, `sigma2Star`, `const_lt_iff` | CORE §1/§4; LAYER_LIFETIME §5 (D5) | Costs taken from the repository as given: local `N e √(k_L w σ²)`, shared `e √(k_S N w σ²) + N w σ² ℓ` (delay floor on the shared observation only), `e > 0` the excess coefficient (`√2` fixed period, `2/√6` barrier); `N, w > 0`, `k_S, k_L ≥ 0`.  The stochastic derivation of these costs is not formalized | `e√(k_S N w) < N e √(k_L w)` iff `k_S < N k_L` |
| `LocalShared.no_switch_without_delay`, `shared_never_wins` | D5 | As above; `σ² > 0`; `ℓ = 0`, resp. `ℓ ≥ 0` and `k_S ≥ N k_L` | At `ℓ = 0`, shared wins iff `k_S < N k_L`, at every drift (no switch); if `k_S ≥ N k_L`, shared never wins |
| `LocalShared.crossing` | D5, the crossing `σ²*` | As above; `ℓ > 0`; `k_S < N k_L`; `σ² > 0` | Shared is strictly cheaper iff `σ² < σ²* = ((√(k_L w) − √(k_S w/N)) e/(wℓ))²` |
| `LocalShared.switch_iff` | D5 / CORE §1 "needs delay on the shared channel only, and a shared lump cheaper than `N` local ones" | As above; `ℓ ≥ 0` | A drift switch (shared strictly cheaper at some `σ² > 0`, not cheaper at another) exists **iff** `ℓ > 0` and `k_S < N k_L` |
| `LocalShared.equal_delay_no_switch`, `barrier_crossing_eq_fixed_div_three` | LAYER_LIFETIME §5 | As above | An equal delay floor on both sides cancels (comparison is the `ℓ = 0` one at every drift); the barrier crossing is the fixed-period crossing divided by exactly 3 |
| `Equipartition.HomogCost`, `Z_scale`, `Nm_scale`, `Nm_one`, `gibbs_mean_homog` | SA1b, general form | `E` a finite-dimensional real normed space of dimension `d ≥ 1`, `μ` any additive Haar measure (Lebesgue); `q` continuous, `q ≥ 0`, `q(x) > 0` for `x ≠ 0`, `q(r x) = r^p q(x)` for `r > 0`, `p > 0`; `β > 0` | `e^{−βq}` and `q e^{−βq}` are integrable, `Z(β) = β^{−d/p} Z(1)`, and `∫ q e^{−βq} / ∫ e^{−βq} = d/(pβ)` (proof: scaling plus Fubini on `β ∈ [1,2]`) |
| `Equipartition.gibbs_excess` | SA1b, `E[J] − J* = d/(pβ)` | As above, with `J(x) = J* + q(x − x*)` | For `π ∝ e^{−βJ}`, `E_π[J] − J* = d/(pβ)` exactly |
| `Equipartition.homogCost_quadratic`, `gibbs_excess_quadratic` | SA1b / Corollary SA1c, `d/(2β)`; CORE §8, THEORY §4 | `J(x) = J* + ½(x − x*)ᵀH(x − x*)` on `ℝ^d` (`Fin d → ℝ`, Lebesgue), `d ≥ 1`, `H` positive definite (Mathlib `Matrix.PosDef`, so symmetric), `β > 0`; π is the Gibbs/Boltzmann law `∝ e^{−βJ}` on all of `ℝ^d` | `E_π[J] − J* = d/(2β)` exactly.  SA1 (that the stationary law of the origination–fixation chain is this Boltzmann weight, Sella–Hirsh), SA1b's "treat the measure as supported on the quadratic well", and the per-model `β` (Moran `α(N−1)`, Wright–Fisher `α(2N−1)`) are **not** formalized; they are the inputs that make this identity the selection result |
| `HullWalk.HullVertices`, `IsLowerHull`, `Pays`, `hull_walk_stop_exists`, `hull_walk_leftmost_argmin` | KEYSTONE_NOTE §4, the hull-vertex walk (edges may skip integers) | `R ≥ 0`; `ε : ℕ → ℝ` arbitrary (no convexity); vertex data `v 0 = 0 < v 1 < ⋯ < v m = n` with every point on or above its hull edge and nondecreasing edge slopes | The walk that jumps from `v i` to `v(i+1)` iff `R(ε(v i) − ε(v(i+1))) > v(i+1) − v i` stops, and the stopping vertex is a minimizer of `φ(K) = K + R(1+ε_K)` on `{0,…,n}`, strictly below `φ` at every `K` to its left (leftmost minimizer) |
| `HullWalk.greedy`, `greedy_isLowerHull`, `hull_increment_test_eq_argmin` | KEYSTONE_NOTE §4 Proposition, unconditional | `R ≥ 0`; `ε` arbitrary | Every `ε` has lower-hull vertex data (greedy minimum-slope chords), so the hull increment test returns the leftmost argmin of `φ` for **every** `ε`, with no convexity hypothesis |
| `N60Exact.count`, `count_isLeftmostArgmin` | `theory/LAYER_CONVEXITY.md` L1 / CLAIM_MAP N64, "if" | Finite domain `{0,…,n}`; `R ≥ 0`; `ε` discrete-convex (decrements non-increasing) | The from-0 count `K*_0(R) = #{K≥1 : R d_K > 1}` is the leftmost minimizer of `K + R(1+ε_K)` |
| `N60Exact.not_min_of_rise`, `exists_threshold`, `threshold_pos`, `exists_R_interval_count_not_argmin`, `exists_R_count_not_argmin`, `exists_R_count_not_argmin_of_pos`, `count_exact_iff_convex` | L1, converse and the iff | Pairwise distinct decrements; the threshold decrement `d_{(m)}` positive (equivalently at least `m` positive decrements) suffices; all-positive is the special case used by the iff | If some `d_m < d_{m+1}`, there is an open interval of `R > 0` on which `K*_0(R) = m` (with `m` one past the rise) and the count is not a minimizer (`exists_R_interval_count_not_argmin`); the single-`R` form is a projection of that statement. Hence with positive distinct decrements, (count = leftmost argmin for all `R > 0`) ⇔ discrete convexity |
| `N60Exact.exists_nonconvex_count_exact` | L1, counterexample to a bare iff | `d = (−2, −1)`, i.e. `ε = (−3, −1, 0)` on `{0,1,2}` | The sequence is not discrete-convex, yet `K*_0(R) = 0` is the unique minimizer for every `R ≥ 0` (`φ(0) < φ(j)` for `j = 1, 2`) |
| `BandCounterexample.clusterE_values`, `bandE0`, `bandE1_lower`, `bandE1_attained`, `bandE2_attained`, `not_convex` | LAYER_CONVEXITY minimal counterexample | `W = (0,1,0)`, weights `(2,1,1)`; bands of a non-monotone profile with a terminal zero band | Optimal band costs `E = (1, 2/3, 0)` (exact ℚ check by kernel `decide`, and over all real cutoffs and levels), so `E_0 − E_1 < E_1 − E_2`: not convex |
| `BandMonge.merge_gain`, `quadrangle_core`, `terminal_core` | LAYER_CONVEXITY §3, the algebra behind Lemmas M and Z | Positive block masses; non-increasing block means; for Z also `m_B ≥ 0` | Merge-gain identity `f(X)+f(Y)−f(X∪Y) = M_XM_Y/(M_X+M_Y)·(m_X−m_Y)²`, the three-block quadrangle, and the terminal bound |
| `BandMonge.quadrangle`, `terminal`, `linkCost_monge`, `terminal_needs_nonneg` | Lemma M, Lemma Z | Finitely many cells `0,…,n−1`, weights `μ > 0`, `W` non-increasing; Lemma Z also needs `W ≥ 0` | `w(a,c)+w(b,d) ≤ w(a,d)+w(b,c)` for `a ≤ b ≤ c ≤ d ≤ n` (`w` = weighted within-band variance); `w(a,c)+z(b) ≤ z(a)+w(b,c)`; the combined cost on `0,…,n+1` is Monge.  `W ≥ 0` is necessary: `W = (0,−1)` with equal weights gives `w(0,2)+z(1)=3/2 ≰ 1 = z(0)+w(1,2)` |
| `BandMonge.exchange`, `convex_of_monge`, `exists_optimal`, `exists_path`, `band_convex`, `bandE`, `bandE_is_min`, `bandE_second_difference` | Lemma X; Theorem B (finite-cell form) | Any Monge link cost; `k ≥ 1` links; for `bandE_second_difference`, also `μ > 0` and `W` nonincreasing and nonnegative | Tail swap at the first crossing turns a `k`- and a `(k+2)`-link path into two `(k+1)`-link paths of no larger total cost; a feasible path exists for every `k ≥ 1`, so an optimal path exists; `E_k` is defined as that minimum path cost and satisfies `2 E_{k+1} ≤ E_k + E_{k+2}` |
| `DriftSelection.ou_excess` | `theory/DRIFT_SELECTION.md` DS1(a); CLAIM_MAP section S | The OU stationary moment equations of (L) (Itô at stationarity) as inputs; `H` positive definite, `Q` Hermitian, `D_m, β, γ > 0` | `½ Tr(H P) = d/(2β) + ½ Tr[H (A+γI)⁻¹ Q]` with `A = D_m β H`.  The derivation of (L) from the origination–fixation chain, and existence/ergodicity of the stationary law, are **not** formalized |
| `DriftSelection.bm_excess`, `bm_excess_isotropic`, `bm_excess_static` | DS1(b) and the `Q=0` case of DS1(d) | Brownian lag-covariance equation (`γ = 0`); same `H`, `D_m, β > 0` | `½ Tr(H P) = d/(2β) + Tr(Q)/(2β D_m)`; with `Q = D I` this is `d/(2β)(1+D/D_m)`; with `Q = 0` this is the SA1b excess `d/(2β)` |
| `DriftSelection.velocity_mean_excess` | DS1(c), the mean-lag term | `A μ = −v` with `A = D_m β H`; `H` positive definite, `D_m, β > 0` | `½ μᵀ H μ = vᵀ H⁻¹ v / (2 β² D_m²)`.  The fluctuation contribution `d/(2β)` is SA1b / `Equipartition` and is added outside this identity |
| `DriftSelection.ou_excess_fast_remainder` | DS1(d), exact remainder to the fast-`γ` floor | `γ > 0`, `H` positive definite | `½ Tr[H (A+γI)⁻¹ Q] − ½ Tr[H (Q/γ)] = −½ Tr[H (A+γI)⁻¹ A (Q/γ)]` (the topological limit `γ→∞` is not formalized) |
| `Coadaptation.LogLinearChain`, `detailedBalance_of_potential`, `potential_of_detailedBalance`, `ca1_iff`, `stationary_of_detailedBalance` | `theory/COADAPTATION.md` (PR #148) CA1 | One party moves at a time; symmetric move graphs, each party's graph connected; positive rates with `q(x→y)/q(y→x) = e^{−β_i ΔJ_i}`.  Finiteness of the product state space is used only by `stationary_of_detailedBalance` | Some positive `π` satisfies detailed balance ⇔ the `β`-scaled game has an exact potential `Ψ`; then `π x = exp(-Ψ x)` (`detailedBalance_of_potential`) and `Ψ = -log π` (`potential_of_detailedBalance`).  Global balance (`stationary_of_detailedBalance`) is on a finite product |
| `Coadaptation.ca1a_weighted`, `ca1a_square` | CA1a | Weighted potential `Δ_i J_i = ω_i Δ_i Φ` | If `β_iω_i = γ` for all `i`, `γΦ` is an exact potential; if a potential exists, `(β_iω_i − β_jω_j)` times every mixed difference of `Φ` is `0` (so unequal `β_iω_i` with a nonzero mixed difference rules out detailed balance) |
| `DriftSpeed.meanLag_abs`, `ds2_excess`, `halfWindow_diverges` | CLAIM_MAP S2 / DS2 | Mean-speed bound `|E[θ(t)−θ(0)]| < v_max t` as input (jump-process construction not formalized); `v_max` is a free parameter, not identified with `Nμδ/(2d)`; equality `|v_k|=v_max` excluded; `λ_min > 0` is a Rayleigh lower bound on a free quadratic | **WEAKER.**  The lag theorem bounds `|E[L]|`, not S2's `E[|L|]`.  The cost theorem is a free-real Rayleigh/CS lower bound `½ λ_min B²`, not `E[J−J*]`.  There is no time-average statement.  The half-window lower bound `(c/2)(αT/2−β)²` diverges |
| `Coadaptation.unique_stationary_prob`, `unique_global_balance`, `joint_connected`, `unique_gibbs_stationary` | CA1 uniqueness (U1) | Finite joint state space; irreducibility of the move graph, which follows from connectedness of each party's graph; uniformization rate strictly larger than every exit rate.  Mathlib has no spectral Perron–Frobenius theorem; uniqueness is the elementary max-ratio argument | At most one stationary probability; when an exact potential `Ψ` exists it is the normalized Gibbs law `exp(−Ψ)/∑exp(−Ψ)`, independent of the clocks.  Faithful |
| `Coadaptation.potential_shift_independent`, `conditional_boltzmann`, `ca1b_potential_excess`, `ca1b_team_split` | CLAIM_MAP U2 / CA1b | Exact potential; for the Gibbs excess, a quadratic PD potential at strength `1`; for the team split, the mean of `½ δᵀ H_T δ` is supplied as the entrywise contraction `∑_{i,j} (H_T)_{ij} P_{ji}`, and `HΨ P = I` | `Ψ−β_i J_i` is independent of party `i`'s design, so the Gibbs law is conditionally Boltzmann (`potential_shift_independent`, `conditional_boltzmann`: Faithful).  `ca1b_potential_excess` is the Gibbs quadratic excess `d/2` at `β=1`, wrapping `Equipartition.gibbs_excess_quadratic` (Faithful).  `ca1b_team_split` identifies the entrywise contraction with `½ Tr(H_T (∇²Ψ)⁻¹)` (**WEAKER**: the identification of that mean with the contraction against `P` is an input).  U2's per-party `E[R_i]=d_i/(2β_i)` is not a declaration |
| `Coadaptation.ca1c_potential`, `ca1c_summed_cost`, `ca1c_gap_zero`, `ca1c_fraction` | CLAIM_MAP U2 / CA1c | `J_i = s_i J_T + h_i(x_{-i})`; `β_i s_i = γ`; `ca1c_summed_cost` uses `h_i=0` and `∑ s_i=1`; `ca1c_gap_zero` additionally takes `J_T(x^Ψ)=min` as input; `ca1c_fraction` takes `E[J_T]−J_T*=d/(2γ)` and `γ = σ N_e / J_T*` as inputs | `ca1c_potential` and `ca1c_summed_cost` (`∑_i J_i = J_T` at every state) are Faithful.  `ca1c_gap_zero` is **WEAKER** (`J_T(x^Ψ)=min` is an input; the coincidence of minimizers is not proved).  `ca1c_fraction` is **WEAKER**: it cancels `J_T*` between those two inputs (A2-L and the potential excess `d/(2γ)` are not proved here).  U2's `E[Φ]−Φ*=d/(2γ)` is not a declaration |
| `CoadaptationDrift.virial_trace`, `ca7_potential_excess` | CLAIM_MAP U11 / CA7 (1) | Lyapunov equation `V K Σ + Σ Kᵀ V = 2V+2Q` as input; `V` invertible, `Σ` symmetric, `Aᵀ=−A`, `K=S+A`; excess identified with `½ Tr(S Σ)`.  Symmetry of `S` is not a hypothesis | `E[Ψ]−Ψ* = ½(d + Tr(V⁻¹ Q))`.  Faithful with the Lyapunov equation as input.  The Hurwitz half of CA7 (1) (`−VK` is Hurwitz) is not formalized |
| `CoadaptationDrift.s8b_lyapunov`, `s8b_regret_party0`, `s8b_regret_party1`, `s8b_naive_party0`, `s8b_naive_party1`, `s8bP0_right_inv`, `s8bP0_lyapunov`, `s8b_static_regret`, `ca7_regret_not_naive` | CLAIM_MAP U11 / CA7 (4) | The exact s8b datum of `tools/coadaptation_checks.py` (`S=[[2,9/10],[9/10,1]]`, `w=[1,2]`, `γ=5`, `V=diag(1,2/5)`, `Q=diag(3/10,3/10)`, `M_{ij}=S_{ij} w_i/γ`); regrets are `½ (g_iᵀ P g_i)/M_{ii}` on a symmetric Lyapunov solution `P` (uniqueness of that symmetric solution is outside Lean) | Lyapunov `V S P + P S V = 2V+2Q` holds for `P=[[2323/1904,−603/476],[−603/476,13757/4760]]`; drift regrets are `10643/80000` and `2557/8000`, against naive uncoupled `13/100` and `7/20`.  At `Q=0`, the quadratic form on `P₀=S⁻¹=[[100/119,−90/119],[−90/119,200/119]]` gives regrets `1/10` and `1/5`, i.e. `1/(2β_i)`.  Faithful for the negative finding on the note's s8b covariance |


## Batch 1: representation, the two obstructions, finite partitions

Every declaration added in `GTAO/Cauchy.lean`, `GTAO/Representation.lean`,
`GTAO/Obstruction.lean`, and `GTAO/ContinuousA6.lean` is labeled against
the sentence it checks. Debreu's theorem, von Neumann–Morgenstern
linearity, and the Gelfand–Yaglom–Dobrushin reverse inequality are
hypotheses. They are not proofs.

| Lean name | Paper | Label |
|---|---|---|
| `AdditiveOnPos`, `Concatenates`, `mul_nat`, `below_gap`, `above_gap`, `ratBelow`, `ratAbove`, `ratBelow_bounds`, `ratAbove_bounds`, `tendsto_mul_div`, `tendsto_mul_div_above`, `tendsto_ratBelow`, `tendsto_ratAbove`, `eq_of_squeeze`, `f_one_nonneg_of_nondecreasing`, `f_one_nonpos_of_nonincreasing` | `theory/REPRESENTATION.md:68`–74, the estimates inside Lemma C | **Faithful.** Auxiliary definitions and bounds for the squeeze. The domain stays `(0, ∞)`. |
| `cauchy_rat`, `cauchy_monotone`, `cauchy_continuous` | Lemma C, lines 68–74 | **Faithful.** Positive rationals need no monotonicity. Either monotone direction gives `f(x) = x f(1)`. Continuity gives the same line. Both signs of `f(1)` are allowed. |
| `pexider_monotone`, `pexider_continuous` | Lemma P, line 76 | **Faithful.** `g = f + c` is additive, and `f(z) = p z - c` with `p` allowed to be negative. |
| `cauchy_nat` | Lemma C on the nonnegative integers, line 78 | **Faithful.** `f(0) = 0` and `f(n) = n f(1)`, with no topology. |
| `slope_nonneg_of_nondecreasing`, `price_zero_of_independent`, `Represents`, `IndependentOf` | Lemma M, line 80 | **Faithful.** A nondecreasing line has nonnegative slope. A coordinate the preorder ignores, on the positive orthant, has price 0. The witnesses are the constant-`1` vector and the vector that is `2` in that coordinate. The linear form is a hypothesis only for strictly positive vectors. |
| `DebreuAdditive`, `r1_linear_components` | Theorem R1, lines 84 and 102–118 | **Faithful** as packaging. `n ≥ 3`, a sum of continuous coordinate functions, and the Pexider equation are hypotheses. The conclusion is `C(z) = ∑ p_i z_i + b` on positive vectors, prices unsigned. Debreu's theorem is not proved. |
| `r1_vnm_scale` | lines 100 and 118 | **WEAKER.** Two positive affine writings of one index agree when that index takes two values. Von Neumann–Morgenstern linearity is a hypothesis. Debreu's common scale does not appear, so the declaration does not identify it with the currency regraduation. |
| `r1_nonneg_of_A8` | lines 92 and 120 | **Faithful.** A8, each concatenating component nondecreasing, gives each price `≥ 0`. |
| `r1_zero_of_not_essential` | lines 25 and 90 | **Faithful.** Same statement as `price_zero_of_independent`. The linear form and the preorder are used only on the positive orthant. |
| `r1_with_layer_count` | lines 94 and 112 | **Faithful.** Separability `C(z, K) = C_interval(z) + f(K)` is a hypothesis. Concatenation of counts then gives `h K`. No declaration drops it. |
| `r1_layer_price_nonneg_of_A8` | line 112 | **Faithful.** A8 on the integer count is the hypothesis that `fn` is nondecreasing. Then `h = fn 1 ≥ 0`. |
| `negative_price_example` | lines 90 and 64 | **WEAKER.** The declaration is the arithmetic of `z₀ + z₁ - z₂`: the components are continuous and the third price is `-1`. Line 90 also says the example satisfies A1–A7. That check is not in the declaration. |
| `IsArgmin`, `affine_argmin_iff`, `strictMono_argmin_iff` | line 126 | **Faithful.** For `a > 0`, and for any strictly increasing transform, the argmin on a menu that does not depend on the numerical cost is unchanged. |
| `affine_excess_scale`, `affine_excess_eq_iff` | lines 128–142 | **Faithful.** On one weight, `E[C] - C* = a (E[J] - J*)` and `b` cancels. Against the fixed Gibbs weight of `J`, `Equipartition.gibbs_excess_quadratic` gives equality with `d/(2β)` if and only if `a = 1`. |
| `affine_excess_refit` | line 142 | **Faithful.** `β_new = β / a` and `(a • H)` positive definite. The excess of `C` under its own Gibbs weight is `d / (2 β_new)`. |
| `fractional_excess_scale`, `fractional_excess_shift` | lines 144–150 | **Faithful** for `b = 0`, and for the rationals `E[J] = 2`, `J* = 1`, `b = 1`, which change the fraction from `1` to `1/2`. The general quotient `(a (E[J] - J*)) / (a J* + b)` is not a theorem. |
| `constrained_argmin_not_affine` | line 152 | **Faithful.** Two designs, costs `1` and `6/5`, variances `4` and `1`, level `3`, threshold `18/100`, shift `17/10`. Both designs are feasible before the shift and the cheaper one is design 0. After the shift only design 1 is feasible. |
| `sharedGrowth`, `kelly_qstar`, `log_le_tangent`, `log_lt_tangent`, `kelly_foc_sign` | line 160 and `theory/DYNAMICS.md:159` | **Faithful.** `q* = 13/50` is the unique maximizer of shared-shock log growth on `(0, 1]`. The printed growth value `0.128` is not an equality. |
| `kelly_not_expected_factor` | line 160 | **Faithful.** Lean expected factor `247/200`, robust `417/400`. The linear objective on `[0, 1]` is maximised only at pure lean, which is not `13/50`. |
| `intervalCost`, `expected_cost_interval` | line 162 | **Faithful.** `LayerLifetime.Tstar 1 (1/20) 1 (1/2) = √(1/10)` is the unique positive minimizer of `c/τ + α τ`. |
| `phi`, `quintic`, `cubic`, `quintic_eq_phi`, `hasDerivAt_quintic`, `cubic_neg`, `quintic_anti` | the numerator identity behind line 162 | **Faithful.** Exact polynomial arithmetic. `6000 t² φ(t)` is the quintic, and the quintic is strictly decreasing on `[0, 2]`. |
| `survival_interval_lt` | line 162 | **WEAKER.** The unique zero of `φ` on `(0, 2]` lies in `(23615/100000, 189/800)` and is strictly below `√(1/10)`, which itself lies in `(31622/100000, 31623/100000)`. The printed figures `0.2362` and `0.3162` are not equalities. The sentence also says this zero is the survival-optimal interval. Maximality of `θ` is not proved. That gap is appended in `BATCH1_PLAN.md`. |
| `klDiv_prob_integral` | `theory/CONTINUOUS_A6_2026-11-23.md:77` | **Faithful.** Probability measures, absolute continuity, and integrability of the log-likelihood are hypotheses. The divergence then equals `ENNReal.ofReal` of the integral. Without integrability Mathlib sets the divergence to `⊤`. |
| `klDiv_nonneg` | line 77, the interval `[0, ∞]` | **Faithful** to `0 ≤ klDiv` in `ℝ≥0∞`. That order is the codomain. Nonnegativity of the integral is a different fact. |
| `klDiv_zero_iff_eq` | line 111 | **Faithful** for the divergence: on probability measures it is `0` if and only if the measures are equal. The mutual-information form of that biconditional is not a separate declaration. |
| `mutualInfo`, `mi_swap`, `mi_data_processing` | line 145, symmetry and data processing | **Faithful.** Symmetry is the coordinate swap. Data processing is Mathlib's `klDiv_map_le` on the product map. |
| `klDiv_compProd_chain` | line 145 names a chain rule | **Faithful** to Mathlib's kernel identity `klDiv_compProd_eq_add`. It is not the mutual-information chain rule. That identification is a puzzle in `BATCH1_PLAN.md`, not a weaker equation. |
| `partitionMI`, `partition_mi_le`, `refinement_mono`, `finite_identity_attains`, `FiniteLabel`, `finitePartitionMI`, `finite_partition_le` | lines 99 and 101 | **Faithful.** A finite labeling does not raise mutual information. A coarser labeling, being a measurable function of a finer one, does not raise it either. On a finite alphabet the identity labeling attains the value. |
| `GYDSup`, `gyd_equiv` | lines 91 and 21 | **Faithful** as a hypothesis. `GYDSup` is the reverse inequality, joint divergence at most the supremum of finite-partition mutual informations. `gyd_equiv` adds that hypothesis to the proved inequality. The supremum is not constructed. |

## Batch 2: heat and repair floors

Declarations in `GTAO/HeatFloor.lean`, `GTAO/FiniteFloor.lean`,
`GTAO/FiniteFloorBounds.lean`, and `GTAO/RepairFloor.lean`. The two-state
floor, the finite-alphabet divergence, the class-indicator and 3-cycle
witnesses, and the one-carrier comparison `L ≥ 4 (log 2 - h)` are checked.
Four declarations are **WEAKER**, each with the missing clause in
`INVENTORY.md` and a miss row in `BATCH2_PLAN.md`. The telegraph lower
bound, the pairwise bound, the path bound, the product inequality on
`{0,1}^n`, and the two-distribution decoder bound are not declarations.

## What is not formalized

None of the following is claimed as proved in Lean.

- The hypothesis at the top of CORE.md (a claim about the real world).
- Convexity of `ε_K` in Model S, still unproved on paper (CORE §4, KEYSTONE_NOTE).  The increment *formula* in N60 is formalized only as a consequence of discrete convexity, which is an assumption here.
- The stochastic derivations behind the layer-lifetime and local-vs-shared cost expressions (Brownian exit times, the time-average square gap `b²/6`, the delay floor `N w σ² ℓ`, and Chalkley's exactness at zero discount).  The optimization and comparison on those expressions are formalized; the expressions are inputs.
- The OU (mean-reverting) version of D5 and the `T*`-versus-correlation-time failure regime (NUMERICAL in the repository).
- SA1 (the Sella–Hirsh stationary weight of the origination–fixation chain), the per-process `β` (Moran, Wright–Fisher), SA1b's well-supported approximation, SA2's lag term as a selection statement, and the fractional form `≈ d/(2σN_e)`.  Only the exact equipartition identity for a Gibbs law on a homogeneous (in particular positive definite quadratic) cost is formalized.
- The Model-S hull is formalized for any measured `ε`; what stays open is a formula for `ε_K` from the world's time scales and its convexity (above).
- The N60-as-written cardinality `1 + #{k ≥ 2 : step k−1 pays}` (and the equality of that cardinality to `1` in the zero-hole case).  The ingredients (no later step pays; leftmost minimizer is `0`) are proved.
- CT4 as a lower bound on cost: only the convexity of `L(I)=D(IB(I))+κ I` is proved, not that `L` bounds a cost functional.  Monotonicity of the information-bottleneck curve `IB` is not used and not formalized.
- CT4's Gaussian AR(1) closed form `I* = ½ log₂(2 ln 2 · a² · Var / κ)`.
- The right derivative `(D∘IB)'(0⁺)` as a real (or extended-real) number; the first-bit sign condition is proved in right-slope form.
- CT20 (i) in a continuous parameter set (Weierstrass on a compact rate set).  Only the finite-menu existence result and the `K ≤ J(d₁)/h` bound are formalized.
- CT20 (ii)'s second clause: for one layer whose error grows with the age of its reading, `f*` is nondecreasing in `w/c`.  The sensing-fixed layer-count clause is formalized.
- CT34 (ii)'s "generically only if" converse (only the "if `θ` is independent of `x`" direction is proved).
- CT34 (iv): a shared driver is not weak coupling (the numerical illustration).
- CT21 (L1–L3): Kalman–Bucy, Wiener spectral factorization, interlacing, degree.
- CT22's in-between binding region, the multiplier `μ_s = −m'/θ'`, and the quasiconvexity / uniqueness hypotheses that justify it.
- CT1–CT3 (rate–distortion, ergodic theorem, lead-time cap).
- CT5, CT6, CT7, CT8, CT9 (Blackwell/garbling, hold-or-fade, and the neighbouring short CTs).
- CT11–CT19, CT23, CT24, CT25, CT26–CT32, CT35–CT43, and the Master Theorem in the class `𝓜_LG`.
- Any information-theoretic construction of `D` or `IB`; they enter CT4 as functions with the stated convexity and monotonicity.
- LAYER_CONVEXITY: N60 started from `k_0 > 0` (the from-1 formula); Theorem B for a continuous frequency measure (only finitely many cells with positive weights are formalized); the identification of the finite-cell minimum `bandE` with the staircase cost `BandCounterexample.cost`; the corollary that `K*_0` equals the leftmost argmin in 𝓑; the Wiener-gain reading `W = 1/(1+N/S)`; Model S convexity for `J≥3`; Model S convexity for `J≤2` (N64(iii); Kalman/Wiener, not formalized in this batch).
- DRIFT_SELECTION: the generator expansion from the origination–fixation chain to the Langevin equation (L), existence and uniqueness of the stationary law and the ergodic theorem (time average = stationary mean); DS1(b) for a general mutation matrix `M` (`d/(2β) + Tr(M^{-1} Q)/(2β)`); DS1(c) as the single excess `d/(2β) + vᵀH⁻¹v/(2 β² D_m²)` (only the mean-lag term is formalized; the fluctuation `d/(2β)` is not supplied here by `Equipartition`); the jump-process construction behind the DS2 mean-speed bound; S2's `E[|L|]`, `E[J−J*]`, and time average (the formalized DS2 lag, cost, and half-window theorems are WEAKER: they bound `|E[L]|`, give a Rayleigh lower bound on a free quadratic, and have no time-average statement); DS3; Corollary DS1c (the fractional form with `β = σ N_e / J*`); the topological limit `γ→∞` in DS1(d).
- COADAPTATION: the origination–fixation derivation of the log-linear rate ratio; CA2–CA4 and CA5–CA6; CA7 (2) the blockwise virial and CA7 (3) the team mismatch bracket (order-preserving Lyapunov inverse from CA3); the Hurwitz half of CA7 (1) (`−VK` is Hurwitz); the §6 counterexamples; U2's per-party `E[R_i]=d_i/(2β_i)` and `E[Φ]−Φ*=d/(2γ)` (not declarations); the A2-L identification `γ = σ N_e / J_T*` and the derivation of equal-`σ N_e`; uniqueness of the symmetric s8b Lyapunov solution.  CA1 uniqueness and the CA7 (1) excess identity are Faithful in this batch.  CA1b's shift, Boltzmann, and Gibbs quadratic excess are Faithful; the team split is WEAKER (the second-moment contraction is an input).  CA1c's potential and summed-cost identity are Faithful; `ca1c_gap_zero` and `ca1c_fraction` are WEAKER (`J_T(x^Ψ)=min`, and cancellation of `J_T*` between `d/(2γ)` and `γ = σ N_e / J_T*`).  CA7 (4) is the s8b negative finding, Faithful on that datum, including the `Q=0` quadratic-form static regrets.

## Layout

```
formal/lean/
  lakefile.toml         # package `gtao`, library `GTAO`, Mathlib pin
  lean-toolchain
  lake-manifest.json
  GTAO.lean             # root import
  GTAO/Cost.lean        # J, argmin, J*
  GTAO/CT33.lean
  GTAO/CT20.lean
  GTAO/CT10.lean
  GTAO/CT34.lean
  GTAO/CT4.lean
  GTAO/CT22.lean
  GTAO/Hull.lean
  GTAO/LayerLifetime.lean   # T* = √(6k/(wσ²)) and the fixed-period cousin
  GTAO/LocalShared.lean     # D5 crossing; switch iff ℓ > 0 and k_S < N k_L
  GTAO/Equipartition.lean   # E_π[J] − J* = d/(pβ); d/(2β) for PD quadratics
  GTAO/DriftSelection.lean  # DS1 Lyapunov identity, including d/(2β)(1+D/D_m)
  GTAO/HullWalk.lean        # hull increment test = leftmost argmin, any ε
  GTAO/N60Exact.lean        # L1: from-0 count = argmin for all R ⇔ convex
  GTAO/BandCounterexample.lean  # W=(0,1,0), μ=(2,1,1): E=(1,2/3,0)
  GTAO/BandMonge.lean       # Lemmas M, Z, X; Theorem B (finite cells, 2E_{k+1}≤E_k+E_{k+2}); Z needs W≥0
  GTAO/Coadaptation.lean    # CA1 (finite state), CA1a
  GTAO/DriftSpeed.lean      # DS2 lag, cost, half-window divergence
  GTAO/CoadaptationUnique.lean  # CA1 uniqueness (max-ratio + uniformization)
  GTAO/CoadaptationExcess.lean  # CA1b / CA1c (U2)
  GTAO/CoadaptationDrift.lean   # CA7 (U11): potential excess and regret counterexample
  GTAO/Cauchy.lean          # Lemmas C, P, C on the nonnegative integers, M
  GTAO/Representation.lean  # R1 packaging and the affine block
  GTAO/Obstruction.lean     # R2: Kelly and the Lundberg interval comparison
  GTAO/ContinuousA6.lean    # probability-measure klDiv, finite partitions, GYDSup
  GTAO/HeatFloor.lean       # two-state heat floor, T59
  GTAO/FiniteFloor.lean     # finite-alphabet learning rate, T60
  GTAO/FiniteFloorBounds.lean  # connectivity, class indicator, 3-cycle
  GTAO/RepairFloor.lean     # one-carrier repair comparison, T63
  scripts/AxiomAudit.lean   # every GTAO declaration uses only standard axioms
```

Build artifacts under `.lake/` are gitignored.
