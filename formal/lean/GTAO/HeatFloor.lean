/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Two-state JP-heat floor, from `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`.
OPEN_WORK T59, batch 2.
-/
module

public import Mathlib.Analysis.SpecialFunctions.Log.Deriv
public import Mathlib.Analysis.Calculus.Deriv.Add
public import Mathlib.Analysis.Calculus.Deriv.Mul
public import Mathlib.Analysis.Calculus.Deriv.MeanValue
public import Mathlib.Analysis.SpecialFunctions.Exp
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum

/-!
# Two-state heat floor

`theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`. The error velocity is the
balance of the four transitions of a telegraph world and a two-state
record. The steady drive, the cancellation of the leak in `I_alt`, the
frozen equilibrium, and the sign of the irreversible-lowering work are
algebra. The transient destruction rate is the derivative of
`log 2 - h(ε)`. The one-edge entropy production is the thermodynamic
budget for this pair of states. A general bipartite generator is not
derived here.
-/

@[expose] public section

namespace HeatFloor

/-- Error velocity from a world flip rate `r`, a leak `Γ`, and a copy
drive `μ`. `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md:47`. -/
noncomputable def errorDot (r Γ μ ε : ℝ) : ℝ :=
  (r + Γ) * (1 - ε) - ε * (r + Γ + μ)

/-- Steady error at those three rates. Line 53. -/
noncomputable def steadyEps (r Γ μ : ℝ) : ℝ :=
  (r + Γ) / (2 * (r + Γ) + μ)

/-- Steady copy drive at a given error. Line 53. -/
noncomputable def steadyMu (r Γ ε : ℝ) : ℝ :=
  (r + Γ) * (1 - 2 * ε) / ε

/-- `L(ε) = (1-2ε) log((1-ε)/ε)`. Line 62. -/
noncomputable def L (ε : ℝ) : ℝ :=
  (1 - 2 * ε) * Real.log ((1 - ε) / ε)

/-- Binary entropy in nats, `h(ε) = -ε log ε - (1-ε) log(1-ε)`. Line 59. -/
noncomputable def binaryEntropy (ε : ℝ) : ℝ :=
  -ε * Real.log ε - (1 - ε) * Real.log (1 - ε)

/-- Mutual information of a fair bit observed at error `ε`. Line 59. -/
noncomputable def fairInfo (ε : ℝ) : ℝ :=
  Real.log 2 - binaryEntropy ε

/-- Net probability current of the copy-plus-leak pair. Line 75. -/
noncomputable def copyBracket (ε Γ μ : ℝ) : ℝ :=
  ε * (Γ + μ) - (1 - ε) * Γ

/-- Two-state information flow of that pair. Line 75. -/
noncomputable def iAltTwoState (ε Γ μ : ℝ) : ℝ :=
  copyBracket ε Γ μ * Real.log ((1 - ε) / ε)

/-- One-edge entropy production `(a-b) log(a/b)`. -/
noncomputable def edgeEntropy (a b : ℝ) : ℝ :=
  (a - b) * Real.log (a / b)

/-- Memory-bath heat in the two-state split `Q̇ = kT (σ + I_alt)`.
Line 70, with temperature restored. -/
noncomputable def memoryHeat (kT σ iAlt : ℝ) : ℝ :=
  kT * (σ + iAlt)

/-- Kramers rate `ν exp(-ΔE / kT)`. Line 40. The 1940 derivation is not
given; this is the rate the note uses. -/
noncomputable def kramersRate (ν ΔE kT : ℝ) : ℝ :=
  ν * Real.exp (-ΔE / kT)

/-- Irreversible-lowering work. Line 111. -/
noncomputable def barrierWork (χ ΔE r ν kT ε : ℝ) : ℝ :=
  χ * ΔE * (r + ν * Real.exp (-ΔE / kT)) * (1 - 2 * ε)

/-- Lower bound on the steady error when the copy drive is at most `c Γ`.
Line 158. -/
noncomputable def copyCapEps (r Γ c : ℝ) : ℝ :=
  (r + Γ) / (2 * r + (2 + c) * Γ)

lemma L_zero_at_half : L (1 / 2) = 0 := by
  unfold L
  norm_num

lemma L_one_fifth : L (1 / 5) = (3 / 5) * Real.log 4 := by
  unfold L
  have harg : (1 - (1 : ℝ) / 5) / (1 / 5) = 4 := by norm_num
  have hcoef : (1 : ℝ) - 2 * (1 / 5) = 3 / 5 := by norm_num
  rw [harg, hcoef]

lemma L_nonneg {ε : ℝ} (hε0 : 0 < ε) (hε : ε ≤ 1 / 2) : 0 ≤ L ε := by
  unfold L
  have hden : 0 < ε := hε0
  have hnum : 0 < 1 - ε := by linarith
  have hratio : 0 < (1 - ε) / ε := div_pos hnum hden
  have hge : 1 ≤ (1 - ε) / ε := by
    rw [one_le_div hden]
    linarith
  have hlog : 0 ≤ Real.log ((1 - ε) / ε) := Real.log_nonneg hge
  have hcoef : 0 ≤ 1 - 2 * ε := by linarith
  exact mul_nonneg hcoef hlog

lemma L_pos {ε : ℝ} (hε0 : 0 < ε) (hε : ε < 1 / 2) : 0 < L ε := by
  unfold L
  have hnum : 0 < 1 - ε := by linarith
  have hratio : 1 < (1 - ε) / ε := by
    rw [one_lt_div hε0]
    linarith
  have hlog : 0 < Real.log ((1 - ε) / ε) := Real.log_pos hratio
  have hcoef : 0 < 1 - 2 * ε := by linarith
  exact mul_pos hcoef hlog

lemma steady_mu_dot_zero {r Γ ε : ℝ} (hε : ε ≠ 0) :
    errorDot r Γ (steadyMu r Γ ε) ε = 0 := by
  unfold errorDot steadyMu
  field_simp
  ring

lemma steady_unique {r Γ μ ε : ℝ} (hε : ε ≠ 0)
    (hden : 2 * (r + Γ) + μ ≠ 0) (hsteady : ε = steadyEps r Γ μ) :
    μ = steadyMu r Γ ε := by
  have hmul : ε * (2 * (r + Γ) + μ) = r + Γ := by
    rw [hsteady]
    unfold steadyEps
    exact (eq_div_iff hden).mp rfl
  unfold steadyMu
  rw [eq_div_iff hε]
  nlinarith [hmul]

/-- The four transitions. `a, b, c, d` are the masses of
`(X,M) = (0,0), (0,1), (1,0), (1,1)`. World flips exchange `a` with `c`
and `b` with `d` at rate `r`. A correct record leaks at `Γ`; an incorrect
record is restored at `Γ+μ`. Line 47. -/
theorem kolmogorov_error_dot (r Γ μ a b c d : ℝ) (hsum : a + b + c + d = 1) :
    (d * r + a * Γ - b * (r + Γ + μ)) + (a * r + d * Γ - c * (r + Γ + μ)) =
      errorDot r Γ μ (b + c) := by
  have hcorr : a + d = 1 - (b + c) := by linarith
  have hflow :
      (d * r + a * Γ - b * (r + Γ + μ)) + (a * r + d * Γ - c * (r + Γ + μ)) =
        (a + d) * (r + Γ) - (b + c) * (r + Γ + μ) := by ring
  rw [hflow, hcorr]
  unfold errorDot
  ring

lemma bracket_eq_world {r Γ ε : ℝ} (hε : ε ≠ 0) :
    copyBracket ε Γ (steadyMu r Γ ε) = r * (1 - 2 * ε) := by
  unfold copyBracket steadyMu
  field_simp
  ring

theorem iAlt_eq_rate_L {r Γ ε : ℝ} (hε : ε ≠ 0) :
    iAltTwoState ε Γ (steadyMu r Γ ε) = r * L ε := by
  unfold iAltTwoState L
  rw [bracket_eq_world hε]
  ring

theorem floor_independent_of_barrier {r Γ₁ Γ₂ ε : ℝ} (hε : ε ≠ 0) :
    iAltTwoState ε Γ₁ (steadyMu r Γ₁ ε) = iAltTwoState ε Γ₂ (steadyMu r Γ₂ ε) := by
  rw [iAlt_eq_rate_L hε, iAlt_eq_rate_L hε]

lemma edgeEntropy_nonneg {a b : ℝ} (ha : 0 < a) (hb : 0 < b) : 0 ≤ edgeEntropy a b := by
  unfold edgeEntropy
  have hratio : 0 < a / b := div_pos ha hb
  rcases le_or_gt a b with h | h
  · have hle : a / b ≤ 1 := (div_le_one hb).2 h
    have hlog : Real.log (a / b) ≤ 0 := by
      rw [← Real.log_one]
      exact Real.log_le_log hratio hle
    exact mul_nonneg_of_nonpos_of_nonpos (by linarith) hlog
  · have hge : 1 ≤ a / b := (one_le_div hb).2 h.le
    have hlog : 0 ≤ Real.log (a / b) := Real.log_nonneg hge
    exact mul_nonneg (by linarith) hlog

lemma edgeEntropy_eq_zero_iff {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    edgeEntropy a b = 0 ↔ a = b := by
  unfold edgeEntropy
  constructor
  · intro h
    have hratio : 0 < a / b := div_pos ha hb
    by_cases hab : a = b
    · exact hab
    · have hdiff : a - b ≠ 0 := sub_ne_zero.mpr hab
      have hlog0 : Real.log (a / b) = 0 := (mul_eq_zero.mp h).resolve_left hdiff
      rw [Real.log_eq_zero] at hlog0
      rcases hlog0 with h0 | h1 | hneg
      · exact absurd h0 hratio.ne'
      · have : a = b := by
          have hdiv : a / b = 1 := h1
          field_simp [hb.ne'] at hdiv
          linarith
        exact absurd this hab
      · exact absurd (by linarith : a / b < 0) (not_lt.mpr hratio.le)
  · rintro rfl
    simp

lemma memoryHeat_ge_info {kT σ iAlt : ℝ} (hkT : 0 ≤ kT) (hσ : 0 ≤ σ) :
    kT * iAlt ≤ memoryHeat kT σ iAlt := by
  unfold memoryHeat
  nlinarith

/-- Steady memory-bath heat is at least `kT r L(ε)`.
Lines 19–23 and 82–85. -/
theorem jp_heat_floor {kT r Γ ε : ℝ} (hkT : 0 ≤ kT) (hε0 : 0 < ε) (hε : ε ≤ 1 / 2)
    (hforward : 0 < ε * (Γ + steadyMu r Γ ε))
    (hback : 0 < (1 - ε) * Γ) :
    kT * r * L ε ≤
      memoryHeat kT (edgeEntropy (ε * (Γ + steadyMu r Γ ε)) ((1 - ε) * Γ))
        (iAltTwoState ε Γ (steadyMu r Γ ε)) := by
  have _ : 0 ≤ L ε := L_nonneg hε0 hε
  have hinfo := iAlt_eq_rate_L (r := r) (Γ := Γ) (ε := ε) hε0.ne'
  have hσ := edgeEntropy_nonneg hforward hback
  rw [hinfo]
  have hge :=
    memoryHeat_ge_info (kT := kT)
      (σ := edgeEntropy (ε * (Γ + steadyMu r Γ ε)) ((1 - ε) * Γ)) (iAlt := r * L ε) hkT hσ
  calc
    kT * r * L ε = kT * (r * L ε) := by ring
    _ ≤ memoryHeat kT (edgeEntropy (ε * (Γ + steadyMu r Γ ε)) ((1 - ε) * Γ)) (r * L ε) := hge

theorem frozen_flux_balance {Γ ε : ℝ} (hε : 0 < ε) :
    ε * (Γ + steadyMu 0 Γ ε) = (1 - ε) * Γ := by
  unfold steadyMu
  field_simp
  ring

theorem frozen_heat_zero {kT Γ ε : ℝ} (hε0 : 0 < ε) (hε : ε < 1) (hΓ : 0 < Γ) :
    memoryHeat kT (edgeEntropy (ε * (Γ + steadyMu 0 Γ ε)) ((1 - ε) * Γ))
        (iAltTwoState ε Γ (steadyMu 0 Γ ε)) =
      0 := by
  have hbal := frozen_flux_balance (Γ := Γ) (ε := ε) hε0
  have hback : 0 < (1 - ε) * Γ := by nlinarith
  have hσ : edgeEntropy (ε * (Γ + steadyMu 0 Γ ε)) ((1 - ε) * Γ) = 0 := by
    rw [hbal]
    exact (edgeEntropy_eq_zero_iff hback hback).2 rfl
  have hi : iAltTwoState ε Γ (steadyMu 0 Γ ε) = 0 := by
    rw [iAlt_eq_rate_L hε0.ne']
    ring
  unfold memoryHeat
  rw [hσ, hi]
  ring

lemma hasDerivAt_mul_log {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun t => t * Real.log t) (Real.log x + 1) x := by
  have hlog : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hx.ne'
  have h := (hasDerivAt_id x).mul hlog
  have hfun : (fun t => t * Real.log t) =ᶠ[nhds x] (id * Real.log) := by
    filter_upwards with t
    simp [Pi.mul_apply, id]
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  simp [id_eq]
  field_simp

lemma hasDerivAt_one_sub (x : ℝ) : HasDerivAt (fun t : ℝ => 1 - t) (-1) x := by
  have h := (hasDerivAt_const x (1 : ℝ)).add ((hasDerivAt_id x).const_mul (-1))
  have hfun : (fun t : ℝ => 1 - t) =ᶠ[nhds x] ((fun _ => (1 : ℝ)) + fun t => (-1) * id t) := by
    filter_upwards with t
    simp [id, Pi.add_apply]
    ring
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  simp

lemma hasDerivAt_compl_log {x : ℝ} (hx0 : x < 1) :
    HasDerivAt (fun t => (1 - t) * Real.log (1 - t)) (-(Real.log (1 - x)) - 1) x := by
  have hsub := hasDerivAt_one_sub x
  have hne : 1 - x ≠ 0 := sub_ne_zero.mpr (ne_of_gt hx0)
  have hlog := (Real.hasDerivAt_log hne).comp x hsub
  have h := hsub.mul hlog
  have hfun :
      (fun t => (1 - t) * Real.log (1 - t)) =ᶠ[nhds x]
        ((fun t => 1 - t) * (Real.log ∘ fun t => 1 - t)) := by
    filter_upwards with t
    simp [Function.comp, Pi.mul_apply]
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  simp [Function.comp]
  field_simp
  ring_nf

lemma hasDerivAt_binaryEntropy {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt binaryEntropy (Real.log ((1 - x) / x)) x := by
  have h1 := (hasDerivAt_mul_log hx0).const_mul (-1)
  have h2 := (hasDerivAt_compl_log hx1).const_mul (-1)
  have h := h1.add h2
  have hfun :
      binaryEntropy =ᶠ[nhds x]
        ((fun t => -1 * (t * Real.log t)) + fun t => -1 * ((1 - t) * Real.log (1 - t))) := by
    filter_upwards with t
    unfold binaryEntropy
    simp [Pi.add_apply]
    ring
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  rw [Real.log_div (sub_pos.mpr hx1).ne' hx0.ne']
  ring_nf

lemma hasDerivAt_fairInfo {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt fairInfo (-Real.log ((1 - x) / x)) x := by
  have hconst : HasDerivAt (fun _ => Real.log 2) 0 x := hasDerivAt_const _ _
  have h := hconst.sub (hasDerivAt_binaryEntropy hx0 hx1)
  convert h using 1
  · ext t
    rfl
  · ring

/-- Transient destruction rate at zero copy drive. Lines 59–65.
This is not the steady JP-heat flow. -/
theorem destroyDeriv {ε r Γ : ℝ} (hε0 : 0 < ε) (hε1 : ε < 1) :
    HasDerivAt fairInfo (-Real.log ((1 - ε) / ε)) ε ∧
      (-Real.log ((1 - ε) / ε)) * ((r + Γ) * (1 - 2 * ε)) = -((r + Γ) * L ε) := by
  refine ⟨hasDerivAt_fairInfo hε0 hε1, ?_⟩
  unfold L
  ring

lemma kramersRate_pos {ν ΔE kT : ℝ} (hν : 0 < ν) : 0 < kramersRate ν ΔE kT := by
  unfold kramersRate
  exact mul_pos hν (Real.exp_pos _)

theorem iAlt_of_kramers {r ν ΔE kT ε : ℝ} (hε : ε ≠ 0) :
    iAltTwoState ε (kramersRate ν ΔE kT) (steadyMu r (kramersRate ν ΔE kT) ε) = r * L ε :=
  iAlt_eq_rate_L hε

theorem barrierWork_zero {χ r ν kT ε : ℝ} :
    barrierWork χ 0 r ν kT ε = 0 := by
  unfold barrierWork
  ring

theorem barrierWork_pos {ΔE r ν kT ε : ℝ} (hΔ : 0 < ΔE) (hr : 0 ≤ r) (hν : 0 < ν)
    (hε : ε < 1 / 2) :
    0 < barrierWork 1 ΔE r ν kT ε := by
  unfold barrierWork
  have hexp : 0 < Real.exp (-ΔE / kT) := Real.exp_pos _
  have hsum : 0 < r + ν * Real.exp (-ΔE / kT) := by nlinarith
  have hrest : 0 < 1 - 2 * ε := by linarith
  have h := mul_pos (mul_pos (mul_pos (by norm_num : (0 : ℝ) < 1) hΔ) hsum) hrest
  simpa using h

theorem steady_ge_copyCap {r Γ μ c : ℝ} (hr : 0 ≤ r) (hΓ : 0 ≤ Γ) (_hμ : 0 ≤ μ)
    (_hc : 0 ≤ c) (hcap : μ ≤ c * Γ) (hden : 0 < 2 * (r + Γ) + μ) :
    copyCapEps r Γ c ≤ steadyEps r Γ μ := by
  have hnum : 0 ≤ r + Γ := by linarith [hr, hΓ]
  have hle : 2 * (r + Γ) + μ ≤ 2 * r + (2 + c) * Γ := by nlinarith [hcap]
  unfold copyCapEps steadyEps
  have hdiv :
      (r + Γ) / (2 * r + (2 + c) * Γ) ≤ (r + Γ) / (2 * (r + Γ) + μ) := by
    apply div_le_div_of_nonneg_left hnum hden hle
  simpa using hdiv

theorem copy_cap_gap {r Γ c : ℝ} (hr : 0 < r) (hΓ : 0 ≤ Γ) (hc : 0 ≤ c) :
    |copyCapEps r Γ c - 1 / 2| = c * Γ / (2 * (2 * r + (2 + c) * Γ)) := by
  have hden : 0 < 2 * r + (2 + c) * Γ := by nlinarith
  unfold copyCapEps
  have hdiff :
      (r + Γ) / (2 * r + (2 + c) * Γ) - 1 / 2 =
        -(c * Γ) / (2 * (2 * r + (2 + c) * Γ)) := by
    field_simp
    ring
  rw [hdiff]
  have hnonneg : 0 ≤ c * Γ / (2 * (2 * r + (2 + c) * Γ)) :=
    div_nonneg (by nlinarith) (by nlinarith)
  have hneg :
      -(c * Γ) / (2 * (2 * r + (2 + c) * Γ)) =
        -(c * Γ / (2 * (2 * r + (2 + c) * Γ))) := by ring
  rw [hneg, abs_neg, abs_of_nonneg hnonneg]

/-- A copy drive capped by a multiple of the leak cannot hold the error
away from `1/2` once the barrier makes `Γ` small. Line 158. -/
theorem copy_cap_near_half {r c δ : ℝ} (hr : 0 < r) (hc : 0 ≤ c) (hδ : 0 < δ) :
    ∃ γ : ℝ, 0 < γ ∧ ∀ Γ : ℝ, 0 < Γ → Γ < γ → |copyCapEps r Γ c - 1 / 2| < δ := by
  refine ⟨δ * (4 * r) / (c + 1), by positivity, ?_⟩
  intro Γ hΓ0 hΓ
  have hgap := copy_cap_gap hr hΓ0.le hc
  rw [hgap]
  have hden : 0 < 2 * (2 * r + (2 + c) * Γ) := by nlinarith
  have hle : c * Γ / (2 * (2 * r + (2 + c) * Γ)) ≤ c * Γ / (4 * r) := by
    have hden' : 4 * r ≤ 2 * (2 * r + (2 + c) * Γ) := by nlinarith
    exact div_le_div_of_nonneg_left (by nlinarith) (by positivity : (0 : ℝ) < 4 * r) hden'
  have hsmall : c * Γ / (4 * r) < δ := by
    by_cases hc0 : c = 0
    · rw [hc0, zero_mul, zero_div]
      exact hδ
    · have hcpos : 0 < c := lt_of_le_of_ne hc (Ne.symm hc0)
      have hc1 : 0 < c + 1 := by linarith
      have hΓδ : Γ < δ * (4 * r) / (c + 1) := hΓ
      have hmul : c * Γ < c * (δ * (4 * r) / (c + 1)) :=
        mul_lt_mul_of_pos_left hΓδ hcpos
      have hfrac : c * (δ * (4 * r) / (c + 1)) ≤ δ * (4 * r) := by
        have : c / (c + 1) ≤ 1 := by
          rw [div_le_one hc1]
          linarith
        have := mul_le_mul_of_nonneg_right this (by positivity : (0 : ℝ) ≤ δ * (4 * r))
        calc
          c * (δ * (4 * r) / (c + 1)) = (c / (c + 1)) * (δ * (4 * r)) := by field_simp
          _ ≤ 1 * (δ * (4 * r)) := this
          _ = δ * (4 * r) := by ring
      have hnum : c * Γ < δ * (4 * r) := lt_of_lt_of_le hmul hfrac
      rw [div_lt_iff₀ (by positivity : (0 : ℝ) < 4 * r)]
      exact hnum
  exact lt_of_le_of_lt hle hsmall

lemma hasDerivAt_log_ratio {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt (fun t => Real.log ((1 - t) / t)) (-(x * (1 - x))⁻¹) x := by
  have hsub : HasDerivAt (fun t => 1 - t) (-1) x := hasDerivAt_one_sub x
  have hid : HasDerivAt id 1 x := hasDerivAt_id x
  have hne1 : 1 - x ≠ 0 := sub_ne_zero.mpr (ne_of_gt hx1)
  have hlog1 := (Real.hasDerivAt_log hne1).comp x hsub
  have hlog2 := (Real.hasDerivAt_log hx0.ne').comp x hid
  have h := hlog1.sub hlog2
  have hfun :
      (fun t => Real.log ((1 - t) / t)) =ᶠ[nhds x]
        ((Real.log ∘ fun t => 1 - t) - (Real.log ∘ id)) := by
    filter_upwards [eventually_gt_nhds hx0, eventually_lt_nhds hx1] with t ht0 ht1
    have hden : t ≠ 0 := ht0.ne'
    have hnum : 1 - t ≠ 0 := sub_ne_zero.mpr (ne_of_gt ht1)
    simp [Function.comp, Pi.sub_apply, Real.log_div hnum hden]
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  field_simp
  ring

lemma hasDerivAt_L {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    HasDerivAt L (-(2 * Real.log ((1 - x) / x)) - (1 - 2 * x) / (x * (1 - x))) x := by
  have hcoef : HasDerivAt (fun t => 1 - 2 * t) (-2) x := by
    have h := (hasDerivAt_const x (1 : ℝ)).add ((hasDerivAt_id x).const_mul (-2))
    have hfun : (fun t => 1 - 2 * t) =ᶠ[nhds x] ((fun _ => (1 : ℝ)) + fun t => -2 * id t) := by
      filter_upwards with t
      simp [id, Pi.add_apply]
      ring
    refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
    simp
  have hlog := hasDerivAt_log_ratio hx0 hx1
  have h := hcoef.mul hlog
  have hfun : L =ᶠ[nhds x] ((fun t => 1 - 2 * t) * fun t => Real.log ((1 - t) / t)) := by
    filter_upwards with t
    unfold L
    simp [Pi.mul_apply]
  refine (h.congr_of_eventuallyEq hfun).congr_deriv ?_
  field_simp
  ring

/-- `L` decreases on `(0, 1/2]`. -/
lemma L_antitone : AntitoneOn L (Set.Ioc (0 : ℝ) (1 / 2)) := by
  have hD : Convex ℝ (Set.Ioc (0 : ℝ) (1 / 2)) := convex_Ioc 0 (1 / 2)
  refine antitoneOn_of_hasDerivWithinAt_nonpos
    (f' := fun x => -(2 * Real.log ((1 - x) / x)) - (1 - 2 * x) / (x * (1 - x))) hD ?_ ?_ ?_
  · intro x hx
    have hx0 : 0 < x := hx.1
    have hx1 : x ≤ 1 / 2 := hx.2
    have hcont : ContinuousAt (fun t => Real.log ((1 - t) / t)) x := by
      apply ContinuousAt.log
      · apply ContinuousAt.div
        · exact (continuousAt_const.sub continuousAt_id)
        · exact continuousAt_id
        · exact hx0.ne'
      · have : 0 < (1 - x) / x := by
          apply div_pos
          · linarith
          · exact hx0
        exact this.ne'
    have hcoef : ContinuousAt (fun t => 1 - 2 * t) x :=
      (continuousAt_const.sub (continuousAt_id.const_mul 2))
    have : ContinuousAt L x := by
      unfold L
      exact hcoef.mul hcont
    exact this.continuousWithinAt
  · intro x hx
    have hx0 : 0 < x := by
      simp only [interior_Ioc, Set.mem_Ioo] at hx
      exact hx.1
    have hx1 : x < 1 / 2 := by
      simp only [interior_Ioc, Set.mem_Ioo] at hx
      exact hx.2
    exact (hasDerivAt_L hx0 (by linarith : x < 1)).hasDerivWithinAt
  · intro x hx
    have hx0 : 0 < x := by
      simp only [interior_Ioc, Set.mem_Ioo] at hx
      exact hx.1
    have hx1 : x < 1 / 2 := by
      simp only [interior_Ioc, Set.mem_Ioo] at hx
      exact hx.2
    have hlog : 0 ≤ Real.log ((1 - x) / x) := by
      apply Real.log_nonneg
      rw [one_le_div hx0]
      linarith
    have hden : 0 < x * (1 - x) := by
      apply mul_pos hx0
      linarith
    have hcoef : 0 ≤ 1 - 2 * x := by linarith
    have : 0 ≤ 2 * Real.log ((1 - x) / x) + (1 - 2 * x) / (x * (1 - x)) := by
      exact add_nonneg (mul_nonneg (by norm_num) hlog) (div_nonneg hcoef hden.le)
    linarith

end HeatFloor
