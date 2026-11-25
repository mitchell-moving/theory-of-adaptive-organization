/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Theorem R1 as packaging, and the affine block, from
`theory/REPRESENTATION.md`. OPEN_WORK T19, batch 1.
-/
module

public import GTAO.Cauchy
public import GTAO.Equipartition
public import Mathlib.MeasureTheory.Group.Measure
public import Mathlib.MeasureTheory.Group.MeasurableEquiv
public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith

/-!
# Representation packaging

Debreu's theorem and von Neumann–Morgenstern linearity are hypotheses.
`n ≥ 3` is part of the Debreu hypothesis. A8 and separability of the
layer count are hypotheses. The negative-price declaration is the
arithmetic of `z₀ + z₁ - z₂`. It does not check A6.
-/

@[expose] public section

namespace Representation

open MeasureTheory Set Matrix Real

/-- Debreu's conclusion, taken as a hypothesis: at least three continuous
coordinate functions, summed. -/
structure DebreuAdditive (n : ℕ) (C : (Fin n → ℝ) → ℝ) where
  n_ge : 3 ≤ n
  comp : Fin n → ℝ → ℝ
  continuous : ∀ i, ContinuousOn (comp i) (Ioi 0)
  additive : ∀ z, (∀ i, 0 < z i) → C z = ∑ i, comp i (z i)

/-- Theorem R1, the linear form on positive vectors. Prices are unsigned.
`theory/REPRESENTATION.md:84`, steps at lines 102–110 and the constant at
line 118. -/
theorem r1_linear_components {n : ℕ} {C : (Fin n → ℝ) → ℝ}
    (hD : DebreuAdditive n C) (c : Fin n → ℝ)
    (hcat : ∀ i, Concatenates (hD.comp i) (c i))
    (z : Fin n → ℝ) (hz : ∀ i, 0 < z i) :
    C z = ∑ i, (hD.comp i 1 + c i) * z i - ∑ i, c i := by
  rw [hD.additive z hz]
  simp_rw [fun i => pexider_continuous (hcat i) (hD.continuous i) (hz i)]
  rw [Finset.sum_sub_distrib]

/-- Two positive affine writings of one index agree. Debreu's common scale
does not appear, so this does not identify that scale with the currency
regraduation. `theory/REPRESENTATION.md:100` and line 118. -/
theorem r1_vnm_scale {α : Type*} (C loss : α → ℝ) {a1 b1 a2 b2 : ℝ}
    (h1 : ∀ x, C x = a1 * loss x + b1) (h2 : ∀ x, C x = a2 * loss x + b2)
    (ha1 : 0 < a1) (ha2 : 0 < a2) (x y : α) (hxy : loss x ≠ loss y) :
    a1 = a2 ∧ b1 = b2 ∧ 0 < a1 ∧ 0 < a2 := by
  have hx : a1 * loss x + b1 = a2 * loss x + b2 := by rw [← h1 x, h2 x]
  have hy : a1 * loss y + b1 = a2 * loss y + b2 := by rw [← h1 y, h2 y]
  have hsub : a1 * (loss x - loss y) = a2 * (loss x - loss y) := by
    linear_combination hx - hy
  have ha : a1 = a2 := mul_right_cancel₀ (sub_ne_zero.mpr hxy) hsub
  refine ⟨ha, ?_, ha1, ha2⟩
  rw [ha] at hx
  linarith

/-- A8 gives nonnegative prices. `theory/REPRESENTATION.md:92` and line 120. -/
theorem r1_nonneg_of_A8 {n : ℕ} {C : (Fin n → ℝ) → ℝ}
    (hD : DebreuAdditive n C) (c : Fin n → ℝ)
    (hcat : ∀ i, Concatenates (hD.comp i) (c i))
    (hA8 : ∀ i, MonotoneOn (hD.comp i) (Ioi 0)) :
    ∀ i, 0 ≤ hD.comp i 1 + c i := by
  intro i
  let g : ℝ → ℝ := fun z => hD.comp i z + c i
  have hg : AdditiveOnPos g := by
    intro a b ha hb
    simp only [g]
    linarith [hcat i ha hb]
  have hmon : MonotoneOn g (Ioi 0) := by
    intro a ha b hb hab
    have := hA8 i ha hb hab
    simp only [g]
    linarith
  simpa [g] using f_one_nonneg_of_nondecreasing hg hmon

/-- A coordinate the preorder ignores has price zero. The linear form and
the preorder are used only on the positive orthant.
`theory/REPRESENTATION.md:25` and line 90. -/
theorem r1_zero_of_not_essential {ι : Type*} [Fintype ι] [DecidableEq ι] {i : ι}
    {p : ι → ℝ} {b : ℝ} {C : (ι → ℝ) → ℝ} {R : (ι → ℝ) → (ι → ℝ) → Prop}
    (hC : ∀ z, (∀ j, 0 < z j) → C z = ∑ j, p j * z j + b) (hR : Represents C R)
    (hind : IndependentOf R i) : p i = 0 :=
  price_zero_of_independent hC hR hind

/-- The layer count separates, as an extra hypothesis, and concatenation
on the count gives a multiple of `K`. `theory/REPRESENTATION.md:94` and
line 112. There is no declaration that drops the separability hypothesis. -/
theorem r1_with_layer_count {n : ℕ} {C : (Fin n → ℝ) → ℕ → ℝ}
    {Cint : (Fin n → ℝ) → ℝ} {fn : ℕ → ℝ}
    (hsep : ∀ z K, C z K = Cint z + fn K)
    (hadd : ∀ m n, fn (m + n) = fn m + fn n) (z : Fin n → ℝ) (K : ℕ) :
    C z K = Cint z + (K : ℝ) * fn 1 := by
  rw [hsep, (cauchy_nat fn hadd).2 K]

/-- A8 on the integer count: a nondecreasing concatenating count has
`h = fn 1 ≥ 0`. `theory/REPRESENTATION.md:112`. -/
theorem r1_layer_price_nonneg_of_A8 (fn : ℕ → ℝ)
    (hadd : ∀ m n, fn (m + n) = fn m + fn n)
    (hmono : ∀ m n, m ≤ n → fn m ≤ fn n) : 0 ≤ fn 1 := by
  have h0 : fn 0 = 0 := (cauchy_nat fn hadd).1
  have h01 : fn 0 ≤ fn 1 := hmono 0 1 (by norm_num)
  linarith [h0, h01]

/-- Arithmetic of the negative-price example. This does not check A6.
`theory/REPRESENTATION.md:90` and line 64. -/
theorem negative_price_example :
    let f0 : ℝ → ℝ := id
    let f1 : ℝ → ℝ := id
    let f2 : ℝ → ℝ := fun z => -z
    (∀ z : Fin 3 → ℝ, f0 (z 0) + f1 (z 1) + f2 (z 2) = z 0 + z 1 - z 2) ∧
      Continuous f0 ∧ Continuous f1 ∧ Continuous f2 ∧ f2 1 = -1 ∧ (-1 : ℝ) < 0 := by
  refine ⟨fun z => by simp; abel, continuous_id, continuous_id, continuous_id.neg, by simp, by norm_num⟩

/-- A design is an argmin when its cost is at most every other design. -/
def IsArgmin {α : Type*} (J : α → ℝ) (d : α) : Prop :=
  ∀ d', J d ≤ J d'

/-- `a > 0` does not move the argmin of a menu that does not depend on the
numerical cost. `theory/REPRESENTATION.md:126`. -/
theorem affine_argmin_iff {α : Type*} (J : α → ℝ) {a b : ℝ} (ha : 0 < a) (d : α) :
    IsArgmin (fun x => a * J x + b) d ↔ IsArgmin J d := by
  constructor
  · intro h d'
    have := h d'
    nlinarith
  · intro h d'
    have := h d'
    nlinarith

/-- Any strictly increasing transform preserves the argmin.
`theory/REPRESENTATION.md:126`. -/
theorem strictMono_argmin_iff {α : Type*} (J : α → ℝ) {φ : ℝ → ℝ}
    (hφ : StrictMono φ) (d : α) :
    IsArgmin (φ ∘ J) d ↔ IsArgmin J d := by
  constructor
  · intro h d'
    exact (hφ.le_iff_le).mp (h d')
  · intro h d'
    exact hφ.monotone (h d')

/-- On one fixed integrable weight, the excess of `a J + b` is `a` times
the excess of `J`. The constant `b` cancels. `theory/REPRESENTATION.md:128`. -/
theorem affine_excess_scale {E : Type*} [MeasurableSpace E] {μ : Measure E}
    {J : E → ℝ} {w : E → ℝ} {a b Jstar : ℝ}
    (hJ : Integrable (fun x => J x * w x) μ) (hw : Integrable w μ) :
    (∫ x, (a * J x + b) * w x ∂μ) - (a * Jstar + b) * (∫ x, w x ∂μ) =
      a * ((∫ x, J x * w x ∂μ) - Jstar * (∫ x, w x ∂μ)) := by
  have hsplit : (fun x => (a * J x + b) * w x) =
      fun x => a * (J x * w x) + b * w x := by
    ext x
    ring
  rw [hsplit, integral_add (hJ.const_mul a) (hw.const_mul b), integral_const_mul, integral_const_mul]
  ring

/-- The fixed Gibbs weight of `J`. The excess of `C = a J + b` equals
`d/(2β)` if and only if `a = 1`. `theory/REPRESENTATION.md:134`–142. -/
theorem affine_excess_eq_iff {d : ℕ} [NeZero d] (H : Matrix (Fin d) (Fin d) ℝ)
    (hH : H.PosDef) (Jstar β : ℝ) (xstar : Fin d → ℝ) (hβ : 0 < β) {a b : ℝ} :
    let J : (Fin d → ℝ) → ℝ :=
      fun x => Jstar + (1 / 2) * ((x - xstar) ⬝ᵥ (H *ᵥ (x - xstar)))
    let w : (Fin d → ℝ) → ℝ := fun x => exp (-(β * J x))
    (∫ x, (a * J x + b) * w x) / (∫ x, w x) - (a * Jstar + b) = d / (2 * β) ↔ a = 1 := by
  intro J w
  let q : (Fin d → ℝ) → ℝ := fun x => (1 / 2) * (x ⬝ᵥ (H *ᵥ x))
  have hq : Equipartition.HomogCost q 2 := Equipartition.homogCost_quadratic H hH
  have hintq : Integrable (fun x => exp (-(β * q x))) (volume : Measure (Fin d → ℝ)) :=
    Equipartition.integrable_exp (μ := volume) hq hβ
  have hmomq : Integrable (fun x => q x * exp (-(β * q x))) (volume : Measure (Fin d → ℝ)) :=
    Equipartition.integrable_moment (μ := volume) hq hβ
  have hpres : MeasurePreserving (fun x : Fin d → ℝ => x + (-xstar)) volume volume :=
    measurePreserving_add_right volume (-xstar)
  have hJeq : ∀ x, J x = Jstar + q (x - xstar) := by
    intro x
    simp only [J, q]
  have hexp : ∀ x, w x = exp (-(β * Jstar)) * exp (-(β * q (x - xstar))) := by
    intro x
    have hsum : -(β * J x) = -(β * Jstar) + -(β * q (x - xstar)) := by
      rw [hJeq]
      ring
    have hw : w x = exp (-(β * Jstar) + -(β * q (x - xstar))) :=
      congrArg exp hsum
    rw [hw, exp_add]
  have hshift : Integrable (fun x => exp (-(β * q (x - xstar)))) volume := by
    refine (hpres.integrable_comp_of_integrable hintq).congr ?_
    filter_upwards with x
    rw [Function.comp_apply, sub_eq_add_neg]
  have hint : Integrable w volume :=
    (hshift.const_mul (exp (-(β * Jstar)))).congr (ae_of_all _ fun x => (hexp x).symm)
  have hden_pos : 0 < ∫ x, w x ∂volume := by
    have hpos := integral_exp_pos (μ := volume) hintq
    have heqI : ∫ x, exp (-(β * q (x - xstar))) ∂volume =
        ∫ x, exp (-(β * q x)) ∂volume := by
      have hcomp := hpres.integral_comp (measurableEmbedding_addRight (-xstar))
        (fun x => exp (-(β * q x)))
      simpa [Function.comp_apply, sub_eq_add_neg] using hcomp
    have hshift_pos : 0 < ∫ x, exp (-(β * q (x - xstar))) ∂volume := by linarith
    have hmul : 0 < exp (-(β * Jstar)) * ∫ x, exp (-(β * q (x - xstar))) ∂volume :=
      mul_pos (exp_pos _) hshift_pos
    have heq : ∫ x, w x ∂volume =
        exp (-(β * Jstar)) * ∫ x, exp (-(β * q (x - xstar))) ∂volume := by
      rw [integral_congr_ae (ae_of_all _ hexp), integral_const_mul]
    linarith
  have hJ : Integrable (fun x => J x * w x) volume := by
    have hmom : Integrable (fun x => q (x - xstar) * exp (-(β * q (x - xstar)))) volume := by
      refine (hpres.integrable_comp_of_integrable hmomq).congr ?_
      filter_upwards with x
      rw [Function.comp_apply, sub_eq_add_neg]
    have hlin : Integrable (fun x =>
        Jstar * exp (-(β * q (x - xstar))) +
          q (x - xstar) * exp (-(β * q (x - xstar)))) volume :=
      (hshift.const_mul Jstar).add hmom
    have heq : ∀ x, J x * w x = exp (-(β * Jstar)) *
        (Jstar * exp (-(β * q (x - xstar))) +
          q (x - xstar) * exp (-(β * q (x - xstar)))) := by
      intro x
      rw [hJeq, hexp]
      ring
    exact (hlin.const_mul _).congr (ae_of_all _ fun x => (heq x).symm)
  have hgibbs := Equipartition.gibbs_excess_quadratic H hH Jstar β xstar hβ
  have hscale := affine_excess_scale (μ := volume) (J := J) (w := w)
    (a := a) (b := b) (Jstar := Jstar) hJ hint
  have hden_ne : (∫ x, w x ∂volume) ≠ 0 := hden_pos.ne'
  have hexcess :
      (∫ x, (a * J x + b) * w x ∂volume) / (∫ x, w x ∂volume) - (a * Jstar + b) =
        a * ((∫ x, J x * w x ∂volume) / (∫ x, w x ∂volume) - Jstar) := by
    have hdiv := hscale
    apply mul_right_cancel₀ hden_ne
    field_simp
    linear_combination hdiv
  have hunit : (∫ x, J x * w x ∂volume) / (∫ x, w x ∂volume) - Jstar = d / (2 * β) := by
    simpa [J, w] using hgibbs
  rw [hexcess, hunit]
  have hc : (d : ℝ) / (2 * β) ≠ 0 :=
    div_ne_zero (Nat.cast_ne_zero.mpr (NeZero.ne d)) (mul_pos two_pos hβ).ne'
  constructor
  · intro h
    have : a * ((d : ℝ) / (2 * β)) = 1 * ((d : ℝ) / (2 * β)) := by simpa using h
    exact mul_right_cancel₀ hc this
  · intro ha
    rw [ha, one_mul]

/-- Refit the slope as `β / a`. The excess of `C` under its own Gibbs weight
is `d / (2 β_new)`. `theory/REPRESENTATION.md:142`. -/
theorem affine_excess_refit {d : ℕ} [NeZero d] (H : Matrix (Fin d) (Fin d) ℝ)
    (hH : H.PosDef) (Jstar β : ℝ) (xstar : Fin d → ℝ) (hβ : 0 < β) {a b : ℝ}
    (ha : 0 < a) :
    let βnew := β / a
    let Cstar := a * Jstar + b
    let C : (Fin d → ℝ) → ℝ := fun x =>
      a * (Jstar + (1 / 2) * ((x - xstar) ⬝ᵥ (H *ᵥ (x - xstar)))) + b
    (∫ x, C x * exp (-(βnew * C x))) / (∫ x, exp (-(βnew * C x))) - Cstar =
      d / (2 * βnew) := by
  intro βnew Cstar C
  have hH' : (a • H).PosDef := by
    refine PosDef.of_dotProduct_mulVec_pos ?_ ?_
    · simpa [IsHermitian, hH.isHermitian, star_trivial] using
        congrArg (fun M => a • M) hH.isHermitian
    · intro x hx
      have hpos := hH.dotProduct_mulVec_pos hx
      simp only [star_trivial] at hpos ⊢
      rw [smul_mulVec, dotProduct_smul, smul_eq_mul]
      exact mul_pos ha hpos
  have hβ' : 0 < β / a := div_pos hβ ha
  have hquad : ∀ x, (x - xstar) ⬝ᵥ ((a • H) *ᵥ (x - xstar)) =
      a * ((x - xstar) ⬝ᵥ (H *ᵥ (x - xstar))) := by
    intro x
    rw [smul_mulVec, dotProduct_smul, smul_eq_mul]
  have hC : ∀ x, C x =
      Cstar + (1 / 2) * ((x - xstar) ⬝ᵥ ((a • H) *ᵥ (x - xstar))) := by
    intro x
    simp only [C, Cstar]
    rw [hquad]
    ring
  have h := Equipartition.gibbs_excess_quadratic (a • H) hH' Cstar (β / a) xstar hβ'
  have hfun : C = fun x =>
      Cstar + (1 / 2) * ((x - xstar) ⬝ᵥ ((a • H) *ᵥ (x - xstar))) := by
    ext x
    exact hC x
  simpa [βnew, hfun] using h

/-- With `b = 0` the fractional excess is unchanged.
`theory/REPRESENTATION.md:144`. -/
theorem fractional_excess_scale {eJ jStar a : ℝ} (hj : jStar ≠ 0) (ha : a ≠ 0) :
    (a * eJ - a * jStar) / (a * jStar) = (eJ - jStar) / jStar := by
  field_simp

/-- A nonzero shift changes the fraction. Concrete rationals: expected
cost `2`, minimum `1`, shift `1`. `theory/REPRESENTATION.md:148`. -/
theorem fractional_excess_shift :
    ((2 : ℝ) + 1 - (1 + 1)) / (1 + 1) ≠ ((2 : ℝ) - 1) / 1 := by
  norm_num

/-- A Lundberg constraint that sees the variance can move the feasible
argmin under a pure shift. Variances differ, so this is not an upper bound
on the cost alone. `theory/REPRESENTATION.md:152`.

Design `0` has cost `1` and variance `4`. Design `1` has cost `6/5` and
variance `1`. The level is `y = 3` and the threshold is `18/100`. The
shift is `17/10`. -/
theorem constrained_argmin_not_affine :
    let cost : Fin 2 → ℝ := fun d => if d = 0 then 1 else 6 / 5
    let var : Fin 2 → ℝ := fun d => if d = 0 then 4 else 1
    let theta (c : Fin 2 → ℝ) (d : Fin 2) : ℝ := 2 * (3 - c d) / var d
    let feasible (c : Fin 2 → ℝ) (d : Fin 2) : Prop := 18 / 100 ≤ theta c d
    feasible cost 0 ∧ feasible cost 1 ∧ cost 0 < cost 1 ∧
      ¬ feasible (fun d => cost d + 17 / 10) 0 ∧
      feasible (fun d => cost d + 17 / 10) 1 := by
  intro cost var theta feasible
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simp [feasible, theta, cost, var]
    norm_num
  · simp [feasible, theta, cost, var]
    norm_num
  · simp [cost]
    norm_num
  · simp [feasible, theta, cost, var]
    norm_num
  · simp [feasible, theta, cost, var]
    norm_num

end Representation
