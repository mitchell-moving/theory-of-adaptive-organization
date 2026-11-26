/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Side R&D, record-cost chain: `theory/RECORD_COST_CHAIN_2026-11-25.md`. Moved from a private Lake project
(library `GTAORnd`, same Lean and Mathlib pins). Statements and proofs unchanged; only this
header, the module lines and doc-comment paths differ. Session labels (R2a′, R3, C3, §R3.4, …)
are mapped to the note's steps S1–S10 in its §3.
-/
module

public import Mathlib

@[expose] public section

/-!
# Polygon irreversibility bound vs the disk (theory/RECORD_COST_CHAIN_2026-11-25.md (source: nocloning route) §4, C2 + C3)

Informal (NOTE.md / session log): *a polygon state space with any number of corners pays at
least 2Θ²/V under continuous drift, while the disk pays zero.*

In the note this rests on two items:

* **C2** a finite reversible symmetry group (simplex permutations, D_n) has no non-trivial
  continuous one-parameter subgroup, so a polygon can follow continuous-time change only by
  stochastic jumps; the disk has SO(2) and can follow reversibly.
* **C3** in the n-site ring Markov model with hop rates k₊, k₋ over horizon τ, with
  `V = (2π/n)²·2D·τ`, `D = (k₊+k₋)/2`, `Σ = (k₊−k₋)·ln(k₊/k₋)·τ`, `Θ = (2π(k₊−k₋)/n)·τ`,
  one has `V·Σ = Θ²·(x+1)ln x/(x−1) ≥ 2Θ²` (x = k₊/k₋), independent of n.

Formalized here: C2 exactly (in the slightly more general form "any group with the discrete
topology", which covers every finite group), the disk's non-trivial continuous rotation
subgroup, the C3 closed form, the inequality, n-independence, and the cost corollary
`λ·Σ ≥ λ·2Θ²/V`.

Modelling inputs taken as definitions, **not derived in Lean** (see formal/lean/README.md, section RND-RECORD-COST):
the formulas for V (variance of a Skellam/Poisson difference) and for the irreversibility
rate σ = (k₊−k₋)ln(k₊/k₋) (KL rate of forward vs time-reversed path measure); the step
"polygon tracker = nearest-neighbour ring chain"; and "the disk pays zero", which is the
definition Σ = 0 for a deterministic invertible flow.
-/

namespace GTAORnd

open Real

/-! ## C2: discrete groups have no non-trivial continuous one-parameter subgroup -/

/-- **C2.** If `G` carries the discrete topology (e.g. any finite group of reversible
symmetries: the permutations of a simplex's vertices, the dihedral group of a polygon), then
every continuous one-parameter subgroup `φ : ℝ → G` (`φ (s + t) = φ s * φ t`) is trivial. -/
theorem discrete_oneParam_trivial {G : Type*} [Group G] [TopologicalSpace G]
    [DiscreteTopology G] (φ : ℝ → G) (hφ : Continuous φ)
    (hadd : ∀ s t, φ (s + t) = φ s * φ t) : ∀ t, φ t = 1 := by
  have h0 : φ 0 = 1 := by
    have := hadd 0 0
    rw [add_zero] at this
    exact (mul_eq_left.mp this.symm)
  intro t
  have hc : φ t = φ 0 := hφ.isConst_of_preconnectedSpace t 0
  rw [hc, h0]

/-- C2 instantiated: the dihedral group `D_n` (symmetries of a regular n-gon, discrete). -/
theorem dihedral_oneParam_trivial (n : ℕ) (φ : ℝ → DihedralGroup n)
    (hφ : @Continuous _ _ _ ⊥ φ) (hadd : ∀ s t, φ (s + t) = φ s * φ t) : ∀ t, φ t = 1 :=
  letI : TopologicalSpace (DihedralGroup n) := ⊥
  haveI : DiscreteTopology (DihedralGroup n) := ⟨rfl⟩
  discrete_oneParam_trivial φ hφ hadd

/-- C2 instantiated: the permutations of the N vertices of a simplex (discrete). -/
theorem simplexPerm_oneParam_trivial (N : ℕ) (φ : ℝ → Equiv.Perm (Fin N))
    (hφ : @Continuous _ _ _ ⊥ φ) (hadd : ∀ s t, φ (s + t) = φ s * φ t) : ∀ t, φ t = 1 :=
  letI : TopologicalSpace (Equiv.Perm (Fin N)) := ⊥
  haveI : DiscreteTopology (Equiv.Perm (Fin N)) := ⟨rfl⟩
  discrete_oneParam_trivial φ hφ hadd

/-- The disk's rotation group SO(2) ≅ `Circle` *does* have a continuous one-parameter
subgroup following any angular velocity ω, and it is non-trivial for ω ≠ 0. -/
theorem disk_oneParam (ω : ℝ) (hω : ω ≠ 0) :
    ∃ φ : ℝ → Circle, Continuous φ ∧ (∀ s t, φ (s + t) = φ s * φ t) ∧ ∃ t, φ t ≠ 1 := by
  refine ⟨fun t => Circle.exp (ω * t), by fun_prop, fun s t => by simp only [mul_add, Circle.exp_add],
    π / ω, ?_⟩
  simp only
  rw [mul_div_cancel₀ _ hω]
  exact Circle.exp_pi_ne_one

/-! ## C3: the ring-clock bound -/

/-- phase variance of the n-site ring clock after horizon τ: `(2π/n)²·2D·τ`, `D=(k₊+k₋)/2` -/
noncomputable def ringV (n : ℕ) (kp km τ : ℝ) : ℝ := (2 * π / n) ^ 2 * (2 * ((kp + km) / 2)) * τ

/-- total irreversibility (KL quantity, no heat): `(k₊−k₋)·ln(k₊/k₋)·τ` -/
noncomputable def ringSigma (kp km τ : ℝ) : ℝ := (kp - km) * log (kp / km) * τ

/-- total tracked angle `Θ = ωτ`, `ω = 2π(k₊−k₋)/n` -/
noncomputable def ringTheta (n : ℕ) (kp km τ : ℝ) : ℝ := (2 * π * (kp - km) / n) * τ

/-- the scalar inequality: `2(x−1) ≤ (x+1)·log x` for `x ≥ 1` -/
lemma two_mul_sub_le_log_of_one_le {x : ℝ} (hx : 1 ≤ x) : 2 * (x - 1) ≤ (x + 1) * log x := by
  have hy0 : 0 ≤ (x - 1) / (x + 1) := div_nonneg (by linarith) (by linarith)
  have hy1 : (x - 1) / (x + 1) < 1 := by rw [div_lt_one (by linarith)]; linarith
  have h := Real.sum_range_le_artanh hy0 hy1 1
  simp only [Finset.range_one, Finset.sum_singleton, mul_zero, zero_add, pow_one,
    Nat.cast_zero, div_one] at h
  rw [Real.log_eq_two_mul_artanh (by linarith)]
  have hx1 : 0 < x + 1 := by linarith
  have : (x + 1) * ((x - 1) / (x + 1)) = x - 1 := by field_simp
  nlinarith

/-- the companion: `(x+1)·log x ≤ 2(x−1)` for `0 < x ≤ 1` (apply the above to 1/x) -/
lemma log_le_two_mul_sub_of_le_one {x : ℝ} (hx0 : 0 < x) (hx : x ≤ 1) :
    (x + 1) * log x ≤ 2 * (x - 1) := by
  have h := two_mul_sub_le_log_of_one_le (one_le_inv_iff₀.mpr ⟨hx0, hx⟩)
  rw [Real.log_inv] at h
  have hxi : x * x⁻¹ = 1 := mul_inv_cancel₀ hx0.ne'
  -- multiply through by x > 0
  have := mul_le_mul_of_nonneg_left h hx0.le
  nlinarith [this]

/-- `(k₊−k₋)·((k₊+k₋)·ln(k₊/k₋) − 2(k₊−k₋)) ≥ 0` for positive rates -/
lemma rate_key {kp km : ℝ} (hp : 0 < kp) (hm : 0 < km) :
    0 ≤ (kp - km) * ((kp + km) * log (kp / km) - 2 * (kp - km)) := by
  set x := kp / km with hx
  have hx0 : 0 < x := div_pos hp hm
  have hkp : kp = x * km := by rw [hx]; field_simp
  rw [hkp]
  have e : (x * km - km) * ((x * km + km) * log x - 2 * (x * km - km))
      = km ^ 2 * ((x - 1) * ((x + 1) * log x - 2 * (x - 1))) := by ring
  rw [e]
  apply mul_nonneg (by positivity)
  rcases le_total 1 x with h1 | h1
  · exact mul_nonneg (by linarith) (by linarith [two_mul_sub_le_log_of_one_le h1])
  · exact mul_nonneg_of_nonpos_of_nonpos (by linarith)
      (by linarith [log_le_two_mul_sub_of_le_one hx0 h1])

/-- **C3 closed form.** For k₊ ≠ k₋ (and n ≥ 1, positive rates):
`V·Σ = Θ²·(x+1)·ln x/(x−1)` with `x = k₊/k₋`. The right side has no `n`. -/
theorem ring_closed_form (n : ℕ) (hn : 0 < n) {kp km : ℝ} (hp : 0 < kp) (hm : 0 < km)
    (hne : kp ≠ km) (τ : ℝ) :
    ringV n kp km τ * ringSigma kp km τ =
      ringTheta n kp km τ ^ 2 * ((kp / km + 1) * log (kp / km) / (kp / km - 1)) := by
  have hn' : (n : ℝ) ≠ 0 := by exact_mod_cast hn.ne'
  have hsub : kp - km ≠ 0 := sub_ne_zero.mpr hne
  have hsub' : kp / km - 1 ≠ 0 := by
    rw [div_sub_one hm.ne']; exact div_ne_zero hsub hm.ne'
  unfold ringV ringSigma ringTheta
  rw [div_add_one hm.ne', div_sub_one hm.ne']
  field_simp

/-- **C3 bound (polygon irreversibility bound).** For every ring size n ≥ 1, all positive
hop rates and every horizon τ: `V·Σ ≥ 2·Θ²`. (Includes k₊ = k₋, where Θ = Σ = 0.) -/
theorem ring_bound (n : ℕ) (hn : 0 < n) {kp km : ℝ} (hp : 0 < kp) (hm : 0 < km) (τ : ℝ) :
    2 * ringTheta n kp km τ ^ 2 ≤ ringV n kp km τ * ringSigma kp km τ := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have e : ringV n kp km τ * ringSigma kp km τ - 2 * ringTheta n kp km τ ^ 2
      = (2 * π / n) ^ 2 * τ ^ 2 * ((kp - km) * ((kp + km) * log (kp / km) - 2 * (kp - km))) := by
    unfold ringV ringSigma ringTheta; field_simp
  have := mul_nonneg (by positivity : (0:ℝ) ≤ (2 * π / n) ^ 2 * τ ^ 2) (rate_key hp hm)
  linarith

/-- the factor `(x+1)ln x/(x−1)` is ≥ 2 for every `x > 0, x ≠ 1` -/
theorem factor_ge_two {x : ℝ} (hx : 0 < x) (h1 : x ≠ 1) : 2 ≤ (x + 1) * log x / (x - 1) := by
  rcases lt_or_gt_of_ne h1 with h | h
  · rw [le_div_iff_of_neg (by linarith)]
    linarith [log_le_two_mul_sub_of_le_one hx h.le]
  · rw [le_div_iff₀ (by linarith)]
    linarith [two_mul_sub_le_log_of_one_le h.le]

/-- **n-independence.** The ratio `V·Σ/Θ²` is the same for every ring size. -/
theorem ring_ratio_indep (n m : ℕ) (hn : 0 < n) (hm' : 0 < m) {kp km : ℝ} (hp : 0 < kp)
    (hm : 0 < km) (hne : kp ≠ km) (τ : ℝ) :
    ringV n kp km τ * ringSigma kp km τ / ringTheta n kp km τ ^ 2 =
      ringV m kp km τ * ringSigma kp km τ / ringTheta m kp km τ ^ 2 := by
  by_cases hτ : τ = 0
  · subst hτ; simp [ringTheta]
  have ht : ∀ k : ℕ, 0 < k → ringTheta k kp km τ ^ 2 ≠ 0 := by
    intro k hk
    have : (k : ℝ) ≠ 0 := by exact_mod_cast hk.ne'
    unfold ringTheta
    have : 2 * π * (kp - km) / k * τ ≠ 0 := by
      apply mul_ne_zero (div_ne_zero (mul_ne_zero (by positivity) (sub_ne_zero.mpr hne)) this) hτ
    positivity
  rw [ring_closed_form n hn hp hm hne, ring_closed_form m hm' hp hm hne,
    mul_div_cancel_left₀ _ (ht n hn), mul_div_cancel_left₀ _ (ht m hm')]

/-- **Cost corollary.** With irreversibility price λ ≥ 0 and V > 0, a ring (polygon) tracker
of any size pays an irreversibility cost `λ·Σ ≥ λ·2Θ²/V`. -/
theorem ring_cost_lower_bound (n : ℕ) (hn : 0 < n) {kp km : ℝ} (hp : 0 < kp) (hm : 0 < km)
    (τ lam : ℝ) (hlam : 0 ≤ lam) (hV : 0 < ringV n kp km τ) :
    lam * (2 * ringTheta n kp km τ ^ 2 / ringV n kp km τ) ≤ lam * ringSigma kp km τ := by
  apply mul_le_mul_of_nonneg_left _ hlam
  rw [div_le_iff₀ hV]
  linarith [ring_bound n hn hp hm τ, mul_comm (ringV n kp km τ) (ringSigma kp km τ)]

/-- In the toy model the disk tracker's irreversibility is *defined* as 0 (deterministic
invertible flow). Its cost is then strictly below the ring's whenever λ > 0, Θ ≠ 0, V > 0. -/
theorem disk_strictly_cheaper (n : ℕ) (hn : 0 < n) {kp km : ℝ} (hp : 0 < kp) (hm : 0 < km)
    (τ lam : ℝ) (hlam : 0 < lam) (hV : 0 < ringV n kp km τ) (hΘ : ringTheta n kp km τ ≠ 0) :
    lam * 0 < lam * ringSigma kp km τ := by
  have h := ring_cost_lower_bound n hn hp hm τ lam hlam.le hV
  have : 0 < lam * (2 * ringTheta n kp km τ ^ 2 / ringV n kp km τ) := by positivity
  linarith

end GTAORnd
