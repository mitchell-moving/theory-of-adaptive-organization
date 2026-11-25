/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Record repair floor, from `theory/RECORD_REPAIR_FLOOR_2026-11-23.md`.
OPEN_WORK T63, batch 2.
-/
module

public import GTAO.HeatFloor
public import GTAO.FiniteFloor
public import Mathlib.Analysis.SpecificLimits.Normed
public import Mathlib.Analysis.Calculus.Deriv.MeanValue
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.GCongr

/-!
# Record repair floor

`theory/RECORD_REPAIR_FLOOR_2026-11-23.md`. One carrier produces `Γ L(ε)`,
and `L` is at least four times `log 2 - h(ε)`. The comparison is the
power series of `log(1+t) - log(1-t)` against the geometric series, which
is the termwise bound in the note, together with the derivatives of `L`
and of `log 2 - h` already checked for the two-state floor. A decoder
that reports one bit is bounded by the same information. The Schnakenberg
time integral is a hypothesis of the averaged floor. The stationary
obstruction to forgetting a bit is proved; a trajectory limit is not.
-/

@[expose] public section

namespace RepairFloor

open HeatFloor InformationTheory

/-- `log(1+t) - log(1-t) ≤ 2t/(1-t^2)` for `t ∈ [0,1)`.
Each series term `2 t^{2k+1}/(2k+1)` is at most `2 t^{2k+1}`. -/
lemma log_sub_log_le {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t < 1) :
    Real.log (1 + t) - Real.log (1 - t) ≤ 2 * t / (1 - t ^ 2) := by
  have habs : |t| < 1 := by rwa [abs_of_nonneg ht0]
  have hlog := Real.hasSum_log_sub_log_of_abs_lt_one habs
  have hsq : |t ^ 2| < 1 := by
    rw [abs_of_nonneg (sq_nonneg t)]
    nlinarith
  have hgeom := (hasSum_geometric_of_abs_lt_one hsq).mul_left (2 * t)
  have hterm :
      ∀ n : ℕ, 2 * (1 / (2 * (n : ℝ) + 1)) * t ^ (2 * n + 1) ≤ 2 * t * (t ^ 2) ^ n := by
    intro n
    have hpow : t ^ (2 * n + 1) = t * (t ^ 2) ^ n := by
      rw [pow_succ', ← pow_mul]
    rw [hpow]
    have hcoef : 1 / (2 * (n : ℝ) + 1) ≤ 1 := by
      rw [div_le_one (by positivity)]
      linarith
    calc
      2 * (1 / (2 * (n : ℝ) + 1)) * (t * (t ^ 2) ^ n)
          ≤ 2 * 1 * (t * (t ^ 2) ^ n) := by gcongr
      _ = 2 * t * (t ^ 2) ^ n := by ring
  have htsum :=
    Summable.tsum_le_tsum hterm hlog.summable hgeom.summable
  rw [hlog.tsum_eq, hgeom.tsum_eq] at htsum
  simpa [div_eq_mul_inv] using htsum

/-- The same comparison is strict for `t ∈ (0,1)`, because the `k = 1` coefficients
`2/3` and `2` differ and `t^3 > 0`. -/
lemma log_sub_log_lt {t : ℝ} (ht0 : 0 < t) (ht1 : t < 1) :
    Real.log (1 + t) - Real.log (1 - t) < 2 * t / (1 - t ^ 2) := by
  have habs : |t| < 1 := by rwa [abs_of_pos ht0]
  have hlog := Real.hasSum_log_sub_log_of_abs_lt_one habs
  have hsq : |t ^ 2| < 1 := by
    rw [abs_of_nonneg (sq_nonneg t)]
    nlinarith
  have hgeom := (hasSum_geometric_of_abs_lt_one hsq).mul_left (2 * t)
  let f : ℕ → ℝ := fun n => 2 * (1 / (2 * (n : ℝ) + 1)) * t ^ (2 * n + 1)
  let g : ℕ → ℝ := fun n => 2 * t * (t ^ 2) ^ n
  have hterm : ∀ n : ℕ, f n ≤ g n := by
    intro n
    have hpow : t ^ (2 * n + 1) = t * (t ^ 2) ^ n := by
      rw [pow_succ', ← pow_mul]
    dsimp [f, g]
    rw [hpow]
    have hcoef : 1 / (2 * (n : ℝ) + 1) ≤ 1 := by
      rw [div_le_one (by positivity)]
      linarith
    calc
      2 * (1 / (2 * (n : ℝ) + 1)) * (t * (t ^ 2) ^ n)
          ≤ 2 * 1 * (t * (t ^ 2) ^ n) := by gcongr
      _ = 2 * t * (t ^ 2) ^ n := by ring
  have h0 : ∀ n : ℕ, 0 ≤ f n := by
    intro n
    dsimp [f]
    positivity
  have hi : f 1 < g 1 := by
    dsimp [f, g]
    have hcoe : 1 / (2 * (1 : ℝ) + 1) = 1 / 3 := by norm_num
    have hpos : 0 < t ^ (2 * 1 + 1) := by positivity
    have hlt : 2 * (1 / (2 * (1 : ℝ) + 1)) * t ^ (2 * 1 + 1) < 2 * t ^ (2 * 1 + 1) := by
      rw [hcoe]
      have hcoef : (2 : ℝ) * (1 / 3) < 2 := by norm_num
      exact mul_lt_mul_of_pos_right hcoef hpos
    have heq : 2 * t ^ (2 * 1 + 1) = 2 * t * (t ^ 2) ^ 1 := by
      rw [pow_succ', ← pow_mul]
      ring
    linarith
  have htsum :=
    Summable.tsum_lt_tsum_of_nonneg (i := 1) h0 hterm hi hgeom.summable
  rw [show ∑' n, f n = Real.log (1 + t) - Real.log (1 - t) from hlog.tsum_eq,
    show ∑' n, g n = 2 * t * (1 - t ^ 2)⁻¹ from hgeom.tsum_eq] at htsum
  simpa [div_eq_mul_inv] using htsum

noncomputable def infoDeriv (x : ℝ) : ℝ :=
  2 * Real.log ((1 - x) / x) - (1 - 2 * x) / (x * (1 - x))

lemma infoDeriv_nonpos {x : ℝ} (hx0 : 0 < x) (hx : x ≤ 1 / 2) : infoDeriv x ≤ 0 := by
  set t : ℝ := 1 - 2 * x with ht
  have ht0 : 0 ≤ t := by linarith
  have ht1 : t < 1 := by linarith
  have hlog := log_sub_log_le ht0 ht1
  have hr : (1 - x) / x = (1 + t) / (1 - t) := by
    rw [ht]
    field_simp
    ring
  have hden : (1 - 2 * x) / (x * (1 - x)) = 4 * t / (1 - t ^ 2) := by
    have hsq : 1 - t ^ 2 = 4 * x * (1 - x) := by
      rw [ht]
      ring
    rw [← ht, hsq]
    field_simp
  unfold infoDeriv
  rw [hr, Real.log_div (by linarith : (1 + t) ≠ 0) (by linarith : (1 - t) ≠ 0), hden]
  have hdenpos : 0 < 1 - t ^ 2 := by nlinarith
  rw [sub_nonpos]
  rw [le_div_iff₀ hdenpos]
  have hmul := mul_le_mul_of_nonneg_right hlog hdenpos.le
  have hcancel : 2 * t / (1 - t ^ 2) * (1 - t ^ 2) = 2 * t := by field_simp
  nlinarith

lemma infoDeriv_neg {x : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2) : infoDeriv x < 0 := by
  set t : ℝ := 1 - 2 * x with ht
  have ht0 : 0 < t := by linarith
  have ht1 : t < 1 := by linarith
  have hlog := log_sub_log_lt ht0 ht1
  have hr : (1 - x) / x = (1 + t) / (1 - t) := by
    rw [ht]
    field_simp
    ring
  have hden : (1 - 2 * x) / (x * (1 - x)) = 4 * t / (1 - t ^ 2) := by
    have hsq : 1 - t ^ 2 = 4 * x * (1 - x) := by
      rw [ht]
      ring
    rw [← ht, hsq]
    field_simp
  unfold infoDeriv
  rw [hr, Real.log_div (by linarith : (1 + t) ≠ 0) (by linarith : (1 - t) ≠ 0), hden]
  have hdenpos : 0 < 1 - t ^ 2 := by nlinarith
  rw [sub_neg]
  rw [lt_div_iff₀ hdenpos]
  have hmul := mul_lt_mul_of_pos_right hlog hdenpos
  have hcancel : 2 * t / (1 - t ^ 2) * (1 - t ^ 2) = 2 * t := by field_simp
  nlinarith

lemma hasDerivAt_infoGap {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt (fun t => L t - 4 * fairInfo t) (infoDeriv x) x := by
  have hL := hasDerivAt_L hx0 hx1
  have hI := (hasDerivAt_fairInfo hx0 hx1).const_mul 4
  have h := hL.sub hI
  have hfun :
      (fun t => L t - 4 * fairInfo t) =ᶠ[nhds x] (L - fun t => 4 * fairInfo t) := by
    filter_upwards with t
    simp [Pi.sub_apply]
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  unfold infoDeriv
  ring

lemma infoGap_half : L (1 / 2) - 4 * fairInfo (1 / 2) = 0 := by
  rw [L_zero_at_half]
  unfold fairInfo binaryEntropy
  rw [show (1 / 2 : ℝ) = (2 : ℝ)⁻¹ by norm_num]
  rw [Real.log_inv]
  have hone : (1 : ℝ) - (2 : ℝ)⁻¹ = (2 : ℝ)⁻¹ := by norm_num
  rw [hone, Real.log_inv]
  ring

lemma infoGap_anti : AntitoneOn (fun t => L t - 4 * fairInfo t) (Set.Ioc (0 : ℝ) (1 / 2)) := by
  refine antitoneOn_of_hasDerivWithinAt_nonpos (f' := infoDeriv)
    (convex_Ioc (0 : ℝ) (1 / 2)) ?_ ?_ ?_
  · intro x hx
    exact (hasDerivAt_infoGap hx.1 (by linarith [hx.2])).continuousAt.continuousWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact (hasDerivAt_infoGap hx'.1 (by linarith)).hasDerivWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact infoDeriv_nonpos hx'.1 (le_of_lt hx'.2)

lemma infoGap_strictAnti :
    StrictAntiOn (fun t => L t - 4 * fairInfo t) (Set.Ioc (0 : ℝ) (1 / 2)) := by
  refine strictAntiOn_of_hasDerivWithinAt_neg (f' := infoDeriv)
    (convex_Ioc (0 : ℝ) (1 / 2)) ?_ ?_ ?_
  · intro x hx
    exact (hasDerivAt_infoGap hx.1 (by linarith [hx.2])).continuousAt.continuousWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact (hasDerivAt_infoGap hx'.1 (by linarith)).hasDerivWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact infoDeriv_neg hx'.1 hx'.2

/-- `L(ε) ≥ 4 (log 2 - h(ε))` on `(0, 1/2]`. Line 73. -/
theorem L_ge_four_entropy {ε : ℝ} (hε0 : 0 < ε) (hε : ε ≤ 1 / 2) :
    4 * fairInfo ε ≤ L ε := by
  have hanti := infoGap_anti ⟨hε0, hε⟩ ⟨by norm_num, le_rfl⟩ hε
  have hhalf := infoGap_half
  linarith

theorem L_eq_four_entropy_iff {ε : ℝ} (hε0 : 0 < ε) (hε : ε ≤ 1 / 2) :
    L ε = 4 * fairInfo ε ↔ ε = 1 / 2 := by
  constructor
  · intro h
    by_contra hne
    have hlt : ε < 1 / 2 := lt_of_le_of_ne hε hne
    have hstrict := infoGap_strictAnti ⟨hε0, le_of_lt hlt⟩ ⟨by norm_num, le_rfl⟩ hlt
    have hfun : (fun t => L t - 4 * fairInfo t) ε = 0 := by
      show L ε - 4 * fairInfo ε = 0
      rw [h, sub_self]
    have hhalf0 : (fun t => L t - 4 * fairInfo t) (1 / 2) = 0 := by
      simpa using infoGap_half
    rw [hfun, hhalf0] at hstrict
    exact lt_irrefl _ hstrict
  · rintro rfl
    linarith [infoGap_half]

lemma fairInfo_half : fairInfo (1 / 2) = 0 := by
  have h := infoGap_half
  rw [L_zero_at_half, sub_eq_zero] at h
  linarith

lemma fairInfo_antitone : AntitoneOn fairInfo (Set.Ioc (0 : ℝ) (1 / 2)) := by
  refine antitoneOn_of_hasDerivWithinAt_nonpos
    (f' := fun x => -Real.log ((1 - x) / x)) (convex_Ioc (0 : ℝ) (1 / 2)) ?_ ?_ ?_
  · intro x hx
    exact (hasDerivAt_fairInfo hx.1 (by linarith [hx.2])).continuousAt.continuousWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact (hasDerivAt_fairInfo hx'.1 (by linarith)).hasDerivWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    have hr : 1 ≤ (1 - x) / x := by
      rw [one_le_div hx'.1]
      linarith
    have hlog : 0 ≤ Real.log ((1 - x) / x) := Real.log_nonneg hr
    linarith

lemma fairInfo_strictAnti : StrictAntiOn fairInfo (Set.Ioc (0 : ℝ) (1 / 2)) := by
  refine strictAntiOn_of_hasDerivWithinAt_neg
    (f' := fun x => -Real.log ((1 - x) / x)) (convex_Ioc (0 : ℝ) (1 / 2)) ?_ ?_ ?_
  · intro x hx
    exact (hasDerivAt_fairInfo hx.1 (by linarith [hx.2])).continuousAt.continuousWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    exact (hasDerivAt_fairInfo hx'.1 (by linarith)).hasDerivWithinAt
  · intro x hx
    have hx' : 0 < x ∧ x < 1 / 2 := by
      simpa [interior_Ioc, Set.mem_Ioo] using hx
    have hr : 1 < (1 - x) / x := by
      rw [one_lt_div hx'.1]
      linarith
    linarith [Real.log_pos hr]

lemma fairInfo_nonneg {ε : ℝ} (hε0 : 0 < ε) (hε : ε ≤ 1 / 2) : 0 ≤ fairInfo ε := by
  have hanti := fairInfo_antitone ⟨hε0, hε⟩ ⟨by norm_num, le_rfl⟩ hε
  rw [fairInfo_half] at hanti
  exact hanti

/-- One carrier, `σ = Γ L(ε)`. Line 73. -/
noncomputable def oneCarrierSigma (Γ ε : ℝ) : ℝ :=
  Γ * L ε

theorem one_carrier_floor {kT Γ ε : ℝ} (hkT : 0 ≤ kT) (hΓ : 0 ≤ Γ) (hε0 : 0 < ε)
    (hε : ε ≤ 1 / 2) :
    4 * kT * Γ * fairInfo ε ≤ kT * oneCarrierSigma Γ ε := by
  unfold oneCarrierSigma
  have hL := L_ge_four_entropy hε0 hε
  have hmul : (4 * fairInfo ε) * (kT * Γ) ≤ L ε * (kT * Γ) :=
    mul_le_mul_of_nonneg_right hL (mul_nonneg hkT hΓ)
  calc
    4 * kT * Γ * fairInfo ε = (4 * fairInfo ε) * (kT * Γ) := by ring
    _ ≤ L ε * (kT * Γ) := hmul
    _ = kT * (Γ * L ε) := by ring

/-- Averaged repair floor. `σbar` is the time average of entropy production.
The Schnakenberg integral that would produce `σbar` is a hypothesis, so this
declaration is the algebra of that budget. Lines 67–71. -/
theorem repair_floor_of_average {kT τ Smax σbar Γ ε : ℝ} (_hkT : 0 ≤ kT) (_hτ : 0 < τ)
    (_hε0 : 0 < ε) (_hε : ε ≤ 1 / 2) (hσ : 4 * Γ * fairInfo ε ≤ σbar) :
    kT * (4 * Γ * fairInfo ε) - kT * Smax / τ ≤ kT * σbar - kT * Smax / τ := by
  have hmul : kT * (4 * Γ * fairInfo ε) ≤ kT * σbar :=
    mul_le_mul_of_nonneg_left hσ _hkT
  linarith

/-- The boundary term `S_max / τ` can be made smaller than any positive allowance. -/
theorem long_horizon {Smax δ : ℝ} (hδ : 0 < δ) :
    ∃ T : ℝ, 0 < T ∧ ∀ τ : ℝ, T ≤ τ → Smax / τ < δ := by
  by_cases hS : Smax ≤ 0
  · refine ⟨1, by norm_num, ?_⟩
    intro τ hτ
    have hτ0 : 0 < τ := by linarith
    have hle : Smax / τ ≤ 0 := div_nonpos_of_nonpos_of_nonneg hS (le_of_lt hτ0)
    linarith
  · have hSpos : 0 < Smax := lt_of_not_ge hS
    refine ⟨Smax / δ + 1, by positivity, ?_⟩
    intro τ hτ
    have hτ0 : 0 < τ := by
      have : 0 < Smax / δ + 1 := by positivity
      linarith
    rw [div_lt_iff₀ hτ0]
    have hbound : Smax < δ * (Smax / δ + 1) := by
      rw [mul_add, mul_div_cancel₀ _ hδ.ne']
      linarith
    have hmul : δ * (Smax / δ + 1) ≤ δ * τ :=
      mul_le_mul_of_nonneg_left hτ (le_of_lt hδ)
    linarith

/-- A state independent of the stored bit has the two decoded errors summing
to 1, so they cannot both sit at or below `ε < 1/2`. Line 89, the stationary
obstruction. The trajectory statement is not this theorem. -/
theorem rf_forget_stationary {ε0 ε1 ε : ℝ} (hsum : ε0 + ε1 = 1) (hε : ε < 1 / 2) :
    ¬ (ε0 ≤ ε ∧ ε1 ≤ ε) := by
  intro h
  linarith

/-- Transport cap `N ≤ q A / (kT Γ g)`. Lines 124–128. `q` is an input. -/
theorem rf_cap {N q A kT Γ g : ℝ} (hden : 0 < kT * Γ * g)
    (hbudget : N * kT * Γ * g ≤ q * A) :
    N ≤ q * A / (kT * Γ * g) := by
  have hbudget' : N * (kT * Γ * g) ≤ q * A := by
    simpa [mul_assoc] using hbudget
  exact (le_div_iff₀ hden).mpr hbudget'

theorem rf_cap_entropy {N q A kT Γ ε : ℝ} (hkT : 0 < kT) (hΓ : 0 < Γ) (hε0 : 0 < ε)
    (hε : ε < 1 / 2) (hbudget : N * kT * Γ * (4 * fairInfo ε) ≤ q * A) :
    N ≤ q * A / (kT * Γ * (4 * fairInfo ε)) := by
  have hinfo : 0 < fairInfo ε := by
    have hstrict := fairInfo_strictAnti ⟨hε0, le_of_lt hε⟩ ⟨by norm_num, le_rfl⟩ hε
    rw [fairInfo_half] at hstrict
    exact hstrict
  have hden : 0 < kT * Γ * (4 * fairInfo ε) := by positivity
  exact rf_cap hden hbudget

/-- The two caps in lines 124–128. A larger conductance gap only tightens the count. -/
theorem rf_cap_chain {N q A kT Γ g ε : ℝ} (hkT : 0 < kT) (hΓ : 0 < Γ) (hε0 : 0 < ε)
    (hε : ε < 1 / 2) (hg : 4 * fairInfo ε ≤ g) (hnum : 0 ≤ q * A)
    (hbudget : N * kT * Γ * g ≤ q * A) :
    N ≤ q * A / (kT * Γ * g) ∧
      q * A / (kT * Γ * g) ≤ q * A / (kT * Γ * (4 * fairInfo ε)) := by
  have hinfo : 0 < fairInfo ε := by
    have hstrict := fairInfo_strictAnti ⟨hε0, le_of_lt hε⟩ ⟨by norm_num, le_rfl⟩ hε
    rw [fairInfo_half] at hstrict
    exact hstrict
  have hgpos : 0 < g := by linarith
  have hden : 0 < kT * Γ * g := by positivity
  refine ⟨rf_cap hden hbudget, ?_⟩
  have hdenInfo : 0 < kT * Γ * (4 * fairInfo ε) := by positivity
  have hle : kT * Γ * (4 * fairInfo ε) ≤ kT * Γ * g := by
    gcongr
  exact div_le_div_of_nonneg_left hnum hdenInfo hle

/-- Bernoulli mass `a` on outcome `0`. -/
noncomputable def bernoulli (a : ℝ) : Fin 2 → ℝ
  | 0 => a
  | 1 => 1 - a

theorem decoder_half {ε : ℝ} (hε0 : 0 < ε) (hε1 : ε < 1) :
    FiniteFloor.klSum (bernoulli (1 - ε)) (fun _ : Fin 2 => 1 / 2) = fairInfo ε := by
  unfold FiniteFloor.klSum bernoulli
  rw [Fin.sum_univ_two]
  have hne : (1 / 2 : ℝ) ≠ 0 := by norm_num
  simp only [hne, ite_false]
  have hrest : 1 - (1 - ε) = ε := by ring
  rw [hrest]
  have h1 : (1 - ε) / (1 / 2) = 2 * (1 - ε) := by ring
  have h2 : ε / (1 / 2) = 2 * ε := by ring
  rw [h1, h2]
  unfold klFun fairInfo binaryEntropy
  have hlog1 : Real.log (2 * (1 - ε)) = Real.log 2 + Real.log (1 - ε) :=
    Real.log_mul (by norm_num) (by linarith)
  have hlog2 : Real.log (2 * ε) = Real.log 2 + Real.log ε :=
    Real.log_mul (by norm_num) hε0.ne'
  rw [hlog1, hlog2]
  ring

theorem decoder_pair {a δ : ℝ} (ha0 : 0 < a) (ha1 : a < 1) (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    FiniteFloor.klSum (bernoulli a) (bernoulli δ) +
        FiniteFloor.klSum (bernoulli a) (bernoulli (1 - δ)) =
      -2 * binaryEntropy a - Real.log (δ * (1 - δ)) := by
  unfold FiniteFloor.klSum bernoulli
  rw [Fin.sum_univ_two, Fin.sum_univ_two]
  have hδ : δ ≠ 0 := hδ0.ne'
  have hδc : 1 - δ ≠ 0 := by linarith
  have ha : a ≠ 0 := ha0.ne'
  have hac : 1 - a ≠ 0 := by linarith
  have hback : 1 - (1 - δ) = δ := by ring
  simp only [hback, hδ, hδc, ite_false]
  unfold klFun binaryEntropy
  rw [Real.log_div ha hδ, Real.log_div hac hδc, Real.log_div ha hδc, Real.log_div hac hδ]
  have hprod : Real.log (δ * (1 - δ)) = Real.log δ + Real.log (1 - δ) :=
    Real.log_mul hδ hδc
  rw [hprod]
  field_simp [hδ, hδc]
  ring

theorem decoder_pair_lower {a δ : ℝ} (ha0 : 0 < a) (ha1 : a ≤ 1 / 2) (hδ0 : 0 < δ)
    (hδ1 : δ < 1) :
    2 * fairInfo a ≤
      FiniteFloor.klSum (bernoulli a) (bernoulli δ) +
        FiniteFloor.klSum (bernoulli a) (bernoulli (1 - δ)) := by
  have ha1' : a < 1 := by linarith
  rw [decoder_pair ha0 ha1' hδ0 hδ1]
  have hquart : δ * (1 - δ) ≤ 1 / 4 := by
    nlinarith [sq_nonneg (δ - 1 / 2)]
  have hpos : 0 < δ * (1 - δ) := mul_pos hδ0 (by linarith)
  have hlog : Real.log (δ * (1 - δ)) ≤ Real.log (1 / 4) :=
    Real.log_le_log hpos hquart
  have h14 : Real.log ((1 : ℝ) / 4) = -(2 * Real.log 2) := by
    rw [Real.log_div (by norm_num) (by norm_num), Real.log_one, zero_sub]
    have hpow : (4 : ℝ) = 2 ^ 2 := by norm_num
    rw [hpow, Real.log_pow]
    ring
  unfold fairInfo
  linarith

end RepairFloor
