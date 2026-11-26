/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
The general diffusion heat step, Proposition EQ-heat, from
`theory/GENERALITY_2026-11-22.md:31-68`. OPEN_WORK LEAN-PHYS.
-/
module

public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# The diffusion heat step

`theory/GENERALITY_2026-11-22.md`, Proposition EQ-heat. The memory
coordinate obeys `dM = F dt + √(2 D) dW`. The note's proof is: the
entropy production `Σ = ∫ J² / (D p)` is nonnegative; substituting
`J / p = F - D ∂ log p` and integrating by parts gives
`Σ = Sr - İ + dS/dt`; in a steady state `İ ≤ Sr`.

This file checks that proof on an arbitrary measure space. The density,
the drift, and their memory derivatives are functions on that space. The
analytic inputs are the fields of `EQHeatHyp`. Two of them are integral
identities that the note obtains from vanishing boundary terms and from
the continuity equation of the memory marginal. They are hypotheses here
and are not derived from the SDE.
-/

@[expose] public section

namespace DiffusionHeat

open MeasureTheory

variable {Ω : Type*} [MeasurableSpace Ω]

/-- Probability current of the memory coordinate, `J = F p - D ∂_M p`.
Line 39. -/
noncomputable def current (D : ℝ) (F p dp : Ω → ℝ) : Ω → ℝ :=
  fun ω => F ω * p ω - D * dp ω

/-- Net learning rate of the memory, `İ = ∫ J ∂_M log p(X | M)`. Line 42. -/
noncomputable def learningRate (μ : Measure Ω) (D : ℝ) (F p dp sCond : Ω → ℝ) : ℝ :=
  ∫ ω, current D F p dp ω * sCond ω ∂μ

/-- `Sr = E[F² + D ∂_M F] / D`. Line 42. -/
noncomputable def shannonRate (μ : Measure Ω) (D : ℝ) (F p dF : Ω → ℝ) : ℝ :=
  (∫ ω, (F ω ^ 2 + D * dF ω) * p ω ∂μ) / D

/-- Entropy production of the memory, `Σ = ∫ J² / (D p)`. Line 52. -/
noncomputable def entropyProduction (μ : Measure Ω) (D : ℝ) (F p dp : Ω → ℝ) : ℝ :=
  ∫ ω, current D F p dp ω ^ 2 / (D * p ω) ∂μ

/-- The assumptions of Proposition EQ-heat, each a named field.

* `D_pos`: constant noise strength `D > 0` (line 39).
* `p_pos`: a positive density (line 29, "regular").
* `score_split`: `∂_M log p = ∂_M log p(X | M) + ∂_M log p_M`, the
  logarithm of the joint density as conditional plus marginal (line 62).
* `ibp`: integration by parts with vanishing boundary terms,
  `∫ F ∂_M p = -∫ p ∂_M F` (line 62).
* `marginal`: `∫ J ∂_M log p_M = -dS`, where `dS` is the rate of change
  of the marginal entropy; the note gets it from `∂_t p_M = -∂_M j_M`
  and a vanishing boundary term (line 62).
* the five `int_` fields: the integrands used are integrable. -/
structure EQHeatHyp (μ : Measure Ω) (D : ℝ) (F p dF dp sCond sMarg : Ω → ℝ) (dS : ℝ) :
    Prop where
  D_pos : 0 < D
  p_pos : ∀ ω, 0 < p ω
  score_split : ∀ ω, dp ω / p ω = sCond ω + sMarg ω
  ibp : ∫ ω, F ω * dp ω ∂μ = -∫ ω, p ω * dF ω ∂μ
  marginal : ∫ ω, current D F p dp ω * sMarg ω ∂μ = -dS
  int_F2p : Integrable (fun ω => F ω ^ 2 * p ω) μ
  int_pdF : Integrable (fun ω => p ω * dF ω) μ
  int_Fdp : Integrable (fun ω => F ω * dp ω) μ
  int_Jcond : Integrable (fun ω => current D F p dp ω * sCond ω) μ
  int_Jmarg : Integrable (fun ω => current D F p dp ω * sMarg ω) μ

/-- `Σ ≥ 0`: the integrand `J² / (D p)` is nonnegative. Line 52. -/
theorem entropyProduction_nonneg {μ : Measure Ω} {D : ℝ} {F p dp : Ω → ℝ}
    (hD : 0 < D) (hp : ∀ ω, 0 < p ω) : 0 ≤ entropyProduction μ D F p dp := by
  unfold entropyProduction
  apply integral_nonneg
  intro ω
  have := hp ω
  positivity

/-- Pointwise form of the substitution `J / p = F - D ∂ log p`. -/
lemma integrand_eq {D Fω pω dpω sc sm : ℝ} (hD : 0 < D) (hp : 0 < pω)
    (hsplit : dpω / pω = sc + sm) :
    (Fω * pω - D * dpω) ^ 2 / (D * pω) =
      (Fω ^ 2 * pω - D * (Fω * dpω)) / D - ((Fω * pω - D * dpω) * sc +
        (Fω * pω - D * dpω) * sm) := by
  have hsplit' : sc + sm = dpω / pω := hsplit.symm
  rw [← mul_add, hsplit']
  field_simp

/-- `Σ = Sr - İ + dS`. Line 65. -/
theorem eq_heat_identity {μ : Measure Ω} {D : ℝ} {F p dF dp sCond sMarg : Ω → ℝ} {dS : ℝ}
    (h : EQHeatHyp μ D F p dF dp sCond sMarg dS) :
    entropyProduction μ D F p dp =
      shannonRate μ D F p dF - learningRate μ D F p dp sCond + dS := by
  have hD := h.D_pos
  have hpt : ∀ ω, current D F p dp ω ^ 2 / (D * p ω) =
      (F ω ^ 2 * p ω - D * (F ω * dp ω)) / D -
        (current D F p dp ω * sCond ω + current D F p dp ω * sMarg ω) := by
    intro ω
    exact integrand_eq hD (h.p_pos ω) (h.score_split ω)
  have hA : Integrable (fun ω => (F ω ^ 2 * p ω - D * (F ω * dp ω)) / D) μ :=
    (h.int_F2p.sub (h.int_Fdp.const_mul D)).div_const D
  have hB : Integrable (fun ω =>
      current D F p dp ω * sCond ω + current D F p dp ω * sMarg ω) μ :=
    h.int_Jcond.add h.int_Jmarg
  have hS : entropyProduction μ D F p dp =
      (∫ ω, F ω ^ 2 * p ω ∂μ - D * ∫ ω, F ω * dp ω ∂μ) / D -
        (learningRate μ D F p dp sCond + ∫ ω, current D F p dp ω * sMarg ω ∂μ) := by
    unfold entropyProduction learningRate
    simp_rw [hpt]
    rw [integral_sub hA hB, integral_div, integral_sub h.int_F2p (h.int_Fdp.const_mul D),
      integral_const_mul, integral_add h.int_Jcond h.int_Jmarg]
  have hSr : shannonRate μ D F p dF =
      (∫ ω, F ω ^ 2 * p ω ∂μ + D * ∫ ω, p ω * dF ω ∂μ) / D := by
    unfold shannonRate
    have heq : (fun ω => (F ω ^ 2 + D * dF ω) * p ω) =
        fun ω => F ω ^ 2 * p ω + D * (p ω * dF ω) := by
      funext ω; ring
    rw [heq, integral_add h.int_F2p (h.int_pdF.const_mul D), integral_const_mul]
  rw [hS, hSr, h.ibp, h.marginal]
  ring

/-- Steady state: `İ ≤ Sr`. Lines 46 and 68. -/
theorem eq_heat_steady {μ : Measure Ω} {D : ℝ} {F p dF dp sCond sMarg : Ω → ℝ}
    (h : EQHeatHyp μ D F p dF dp sCond sMarg 0) :
    learningRate μ D F p dp sCond ≤ shannonRate μ D F p dF := by
  have hid := eq_heat_identity h
  have hnn := entropyProduction_nonneg (μ := μ) (F := F) (dp := dp) h.D_pos h.p_pos
  linarith

/-- Energy flow into the memory bath at mobility `1` with the Einstein unit
`kT = D`: `D Sr ≥ kT İ`. Line 46. -/
theorem eq_heat_floor {μ : Measure Ω} {D kT : ℝ} {F p dF dp sCond sMarg : Ω → ℝ}
    (h : EQHeatHyp μ D F p dF dp sCond sMarg 0) (hkT : kT = D) :
    kT * learningRate μ D F p dp sCond ≤ D * shannonRate μ D F p dF := by
  subst hkT
  exact mul_le_mul_of_nonneg_left (eq_heat_steady h) h.D_pos.le

end DiffusionHeat
