/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Theorem R2 witnesses, from `theory/REPRESENTATION.md:158`.
OPEN_WORK T19, batch 1.
-/
module

public import GTAO.LayerLifetime
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Analysis.Real.Sqrt
public import Mathlib.Analysis.Calculus.Deriv.Pow
public import Mathlib.Analysis.Calculus.Deriv.Add
public import Mathlib.Analysis.Calculus.Deriv.MeanValue
public import Mathlib.Topology.Order.IntermediateValue
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith

/-!
# Two obstructions

Kelly: the shared-shock log-growth stake is not the stake that maximises
the expected factor. Lundberg: the interval that minimises expected cost
is not the interval that maximises the exponent on this published point.

The note prints `0.128`, `0.2362`, and `0.3162`. Those are four-decimal
roundings. No equality to them is stated.
-/

@[expose] public section

namespace Obstruction

open Real Set Filter

/-! ### Kelly -/

/-- Shared-shock log growth at the published point
`β = 1/20`, `a₁ = 13/10`, `b₁ = 21/20`, `b₀ = 9/10`.
`theory/REPRESENTATION.md:160` and `theory/DYNAMICS.md:159`. -/
noncomputable def sharedGrowth (q : ℝ) : ℝ :=
  (1 - (1 / 20)) * log ((13 / 10) - ((13 / 10) - 21 / 20) * q) +
    (1 / 20) * log (q * (9 / 10))

/-- The closed form `q* = β a₁ / (a₁ - b₁)` equals `13/50`. -/
theorem kelly_qstar : (1 / 20 : ℝ) * (13 / 10) / ((13 / 10) - 21 / 20) = 13 / 50 := by
  norm_num

lemma log_le_tangent {y y0 : ℝ} (hy : 0 < y) (hy0 : 0 < y0) :
    log y ≤ log y0 + (y - y0) / y0 := by
  have h := log_le_sub_one_of_pos (div_pos hy hy0)
  rw [log_div hy.ne' hy0.ne'] at h
  have hdiv : (y - y0) / y0 = y / y0 - 1 := by field_simp
  linarith

lemma log_lt_tangent {y y0 : ℝ} (hy : 0 < y) (hy0 : 0 < y0) (hne : y ≠ y0) :
    log y < log y0 + (y - y0) / y0 := by
  have hne' : y / y0 ≠ 1 := by
    intro h
    apply hne
    have := (div_eq_iff hy0.ne').mp h
    linarith
  have h := log_lt_sub_one_of_pos (div_pos hy hy0) hne'
  rw [log_div hy.ne' hy0.ne'] at h
  have hdiv : (y - y0) / y0 = y / y0 - 1 := by field_simp
  linarith

/-- `13/50` is the unique maximizer of shared-shock log growth on `(0, 1]`.
The printed value `0.128` is not given an equality. -/
theorem kelly_foc_sign {q : ℝ} (hq0 : 0 < q) (hq1 : q ≤ 1) :
    sharedGrowth q ≤ sharedGrowth (13 / 50) ∧
      (sharedGrowth q = sharedGrowth (13 / 50) ↔ q = 13 / 50) := by
  let q0 : ℝ := 13 / 50
  let δ : ℝ := 1 / 4
  let y : ℝ → ℝ := fun t => 13 / 10 - δ * t
  have hδ : (13 / 10 : ℝ) - 21 / 20 = δ := by norm_num
  have hy_pos : ∀ t, 0 < t → t ≤ 1 → 0 < y t := by
    intro t ht0 ht1
    have : δ * t ≤ δ := by nlinarith [show 0 < δ by norm_num]
    have : y t ≥ 13 / 10 - δ := by
      simp only [y]
      linarith
    have : 13 / 10 - δ = 21 / 20 := by norm_num
    linarith
  have hy0 : 0 < y q0 := hy_pos q0 (by norm_num) (by norm_num)
  have hyq : 0 < y q := hy_pos q hq0 hq1
  have hq0b : 0 < q0 * (9 / 10) := by norm_num
  have hqb : 0 < q * (9 / 10) := by positivity
  have hy_sub : y q - y q0 = -δ * (q - q0) := by simp only [y]; ring
  have hy0_val : y q0 = 247 / 200 := by norm_num
  have hlin : (1 - (1 / 20 : ℝ)) * ((y q - y q0) / y q0) +
      (1 / 20) * ((q * (9 / 10) - q0 * (9 / 10)) / (q0 * (9 / 10))) = 0 := by
    rw [hy_sub, hy0_val]
    field_simp
    ring
  have hle1 := log_le_tangent hyq hy0
  have hle2 := log_le_tangent hqb hq0b
  have hbound : sharedGrowth q - sharedGrowth q0 ≤
      (1 - (1 / 20 : ℝ)) * ((y q - y q0) / y q0) +
        (1 / 20) * ((q * (9 / 10) - q0 * (9 / 10)) / (q0 * (9 / 10))) := by
    unfold sharedGrowth
    rw [hδ]
    have hmul1 := mul_le_mul_of_nonneg_left hle1 (show 0 ≤ (1 - (1 / 20 : ℝ)) by norm_num)
    have hmul2 := mul_le_mul_of_nonneg_left hle2 (show 0 ≤ (1 / 20 : ℝ) by norm_num)
    linarith
  refine ⟨?_, ?_⟩
  · linarith
  · constructor
    · intro heq
      by_contra hne
      have hyne : y q ≠ y q0 := by
        intro hyeq
        have : -δ * (q - q0) = 0 := by linarith
        have : q - q0 = 0 := by
          have hδ0 : δ ≠ 0 := by norm_num
          exact mul_left_cancel₀ (by simpa using hδ0) (by linarith)
        have hqeq : q = q0 := sub_eq_zero.mp this
        simp only [q0] at hqeq
        exact hne hqeq
      have hlt1 := log_lt_tangent hyq hy0 hyne
      have hmul1 := mul_lt_mul_of_pos_left hlt1 (show 0 < (1 - (1 / 20 : ℝ)) by norm_num)
      have hmul2 := mul_le_mul_of_nonneg_left hle2 (show 0 ≤ (1 / 20 : ℝ) by norm_num)
      have hstrict : sharedGrowth q - sharedGrowth q0 <
          (1 - (1 / 20 : ℝ)) * ((y q - y q0) / y q0) +
            (1 / 20) * ((q * (9 / 10) - q0 * (9 / 10)) / (q0 * (9 / 10))) := by
        unfold sharedGrowth
        rw [hδ]
        linarith
      linarith
    · intro hq
      subst hq
      rfl

/-- The per-unit expected factors are `247/200` (lean) and `417/400`
(robust). The linear objective on `[0, 1]` is maximised only at pure lean,
which is not `13/50`. -/
theorem kelly_not_expected_factor :
    (1 - (1 / 20 : ℝ)) * (13 / 10) = 247 / 200 ∧
      (1 - (1 / 20 : ℝ)) * (21 / 20) + (1 / 20) * (9 / 10) = 417 / 400 ∧
      417 / 400 < (247 / 200 : ℝ) ∧ (13 / 50 : ℝ) ≠ 0 ∧
      ∀ q : ℝ, 0 ≤ q → q ≤ 1 →
        (1 - q) * (247 / 200) + q * (417 / 400) ≤ 247 / 200 ∧
          ((1 - q) * (247 / 200) + q * (417 / 400) = 247 / 200 ↔ q = 0) := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, ?_⟩
  intro q hq0 hq1
  have hlin : (1 - q) * (247 / 200 : ℝ) + q * (417 / 400) =
      247 / 200 - q * (247 / 200 - 417 / 400) := by ring
  have hgap : 0 < (247 / 200 : ℝ) - 417 / 400 := by norm_num
  constructor
  · rw [hlin]
    have : 0 ≤ q * ((247 / 200 : ℝ) - 417 / 400) := mul_nonneg hq0 hgap.le
    linarith
  · constructor
    · intro heq
      rw [hlin] at heq
      have : q * ((247 / 200 : ℝ) - 417 / 400) = 0 := by linarith
      exact (mul_eq_zero.mp this).resolve_right hgap.ne'
    · intro hq
      subst hq
      ring

/-! ### Lundberg -/

/-- Expected-cost interval objective `c/τ + α τ` at `c = 1/20`, `α = 1/2`. -/
noncomputable def intervalCost (t : ℝ) : ℝ := (1 / 20) / t + (1 / 2) * t

/-- Numerator of `θ'` on the published point. `s₂ = 9/100 + (1/3) t³`,
margin `1 - c/t - α t`. -/
noncomputable def phi (t : ℝ) : ℝ :=
  ((1 / 20) / t ^ 2 - 1 / 2) * (9 / 100 + (1 / 3) * t ^ 3) -
    (1 - (1 / 20) / t - (1 / 2) * t) * (3 * (1 / 3) * t ^ 2)

/-- The polynomial `2000 t⁵ - 6000 t⁴ + 400 t³ - 270 t² + 27`. -/
def quintic (t : ℝ) : ℝ :=
  2000 * t ^ 5 - 6000 * t ^ 4 + 400 * t ^ 3 - 270 * t ^ 2 + 27

/-- `20 t` times this cubic is the derivative of `quintic`. -/
def cubic (t : ℝ) : ℝ := 500 * t ^ 3 - 1200 * t ^ 2 + 60 * t - 27

lemma quintic_eq_phi {t : ℝ} (ht : t ≠ 0) : 6000 * t ^ 2 * phi t = quintic t := by
  unfold phi quintic
  field_simp
  ring

lemma hasDerivAt_quintic (t : ℝ) : HasDerivAt quintic (20 * t * cubic t) t := by
  have hfun : quintic = fun s =>
      2000 * s ^ 5 + (-6000) * s ^ 4 + 400 * s ^ 3 + (-270) * s ^ 2 + 27 := by
    ext s
    unfold quintic
    ring_nf
  rw [hfun]
  have h5 := (hasDerivAt_pow 5 t).const_mul (2000 : ℝ)
  have h4 := (hasDerivAt_pow 4 t).const_mul (-(6000 : ℝ))
  have h3 := (hasDerivAt_pow 3 t).const_mul (400 : ℝ)
  have h2 := (hasDerivAt_pow 2 t).const_mul (-(270 : ℝ))
  have h0 := hasDerivAt_const t (27 : ℝ)
  have h := (((h5.add h4).add h3).add h2).add h0
  convert h using 1
  simp only [Nat.add_one_sub_one]
  norm_num
  unfold cubic
  ring_nf

lemma cubic_neg {t : ℝ} (ht0 : 0 ≤ t) (ht2 : t ≤ 2) : cubic t < 0 := by
  by_cases ht : t ≤ 1
  · have hup : cubic t ≤ -700 * t ^ 2 + 60 * t - 27 := by
      unfold cubic
      nlinarith [sq_nonneg t, ht0, ht]
    have hsq : -700 * t ^ 2 + 60 * t - 27 = -700 * (t - 3 / 70) ^ 2 - 180 / 7 := by ring
    have hneg : -700 * (t - 3 / 70) ^ 2 - 180 / 7 < 0 := by
      have := sq_nonneg (t - 3 / 70)
      nlinarith
    linarith
  · have ht1 : 1 < t := lt_of_not_ge ht
    have ht := ht1
    have hup : cubic t ≤ -200 * t ^ 2 + 60 * t - 27 := by
      unfold cubic
      nlinarith [ht0, ht, ht2]
    have hbound : -200 * t ^ 2 + 60 * t - 27 =
        -167 - 20 * (t - 1) * (10 * t + 7) := by ring
    have hpos : 0 < (t - 1) * (10 * t + 7) := by nlinarith
    linarith

lemma quintic_anti {s t : ℝ} (hs0 : 0 ≤ s) (ht2 : t ≤ 2) (hst : s < t) :
    quintic t < quintic s := by
  have hcont : ContinuousOn quintic (Icc s t) := by
    unfold quintic
    fun_prop
  have hderiv : ∀ u ∈ Ioo s t, HasDerivAt quintic (20 * u * cubic u) u :=
    fun u _ => hasDerivAt_quintic u
  obtain ⟨c, hc, hslope⟩ := exists_hasDerivAt_eq_slope quintic
    (fun u => 20 * u * cubic u) hst hcont hderiv
  have hc0 : 0 < c := by
    have : s < c := hc.1
    linarith
  have hc2 : c ≤ 2 := by
    have : c < t := hc.2
    linarith
  have hcub : cubic c < 0 := cubic_neg hc0.le hc2
  have hneg : 20 * c * cubic c < 0 := by nlinarith
  have hden : 0 < t - s := by linarith
  have hquot : (quintic t - quintic s) / (t - s) < 0 := by
    rw [← hslope]
    exact hneg
  rcases div_neg_iff.mp hquot with hlt | hgt
  · linarith
  · linarith

/-- `√(1/10)` is the unique positive minimizer of `c/τ + α τ`.
`LayerLifetime.Tstar` is the same point. `theory/REPRESENTATION.md:162`. -/
theorem expected_cost_interval :
    LayerLifetime.Tstar 1 (1 / 20) 1 (1 / 2) = √(1 / 10) ∧
      (∀ t, 0 < t → intervalCost (√(1 / 10)) ≤ intervalCost t) ∧
      (∀ t, 0 < t → intervalCost t ≤ intervalCost (√(1 / 10)) → t = √(1 / 10)) := by
  have ha : 0 < (1 : ℝ) * 1 * (1 / 2) := by norm_num
  have hk : 0 < (1 / 20 : ℝ) := by norm_num
  have hT : LayerLifetime.Tstar 1 (1 / 20) 1 (1 / 2) = √(1 / 10) := by
    unfold LayerLifetime.Tstar
    congr 1
    field_simp
    norm_num
  refine ⟨hT, ?_, ?_⟩
  · intro t ht
    have hcost : ∀ u, intervalCost u = LayerLifetime.cost 1 (1 / 20) 1 (1 / 2) u := by
      intro u
      unfold intervalCost LayerLifetime.cost
      ring
    rw [hcost, hcost, ← hT]
    exact LayerLifetime.Tstar_isMin ha hk ht
  · intro t ht hle
    have hcost : ∀ u, intervalCost u = LayerLifetime.cost 1 (1 / 20) 1 (1 / 2) u := by
      intro u
      unfold intervalCost LayerLifetime.cost
      ring
    rw [hcost, hcost, ← hT] at hle
    rw [← hT]
    exact LayerLifetime.Tstar_unique ha hk ht hle

/-- The unique positive zero of `φ` on `(0, 2]` lies in
`(23615/100000, 189/800)` and is strictly below `√(1/10)`.
The note's `0.2362` and `0.3162` are roundings of these brackets.
This does not prove that the zero maximizes `θ`. -/
theorem survival_interval_lt :
    ∃ τ, 23615 / 100000 < τ ∧ τ < 189 / 800 ∧ phi τ = 0 ∧
      (∀ τ', 0 < τ' → τ' ≤ 2 → phi τ' = 0 → τ' = τ) ∧
      τ < √(1 / 10) ∧
      (31622 / 100000 : ℝ) < √(1 / 10) ∧ √(1 / 10) < 31623 / 100000 := by
  let a : ℝ := 23615 / 100000
  let b : ℝ := 189 / 800
  have hab : a < b := by norm_num
  have ha0 : 0 < a := by norm_num
  have hphi_a : 0 < phi a := by
    have hquint : 0 < quintic a := by
      unfold quintic
      norm_num
    have hid := quintic_eq_phi (t := a) ha0.ne'
    have hcoef : 0 < 6000 * a ^ 2 := by positivity
    have hprod : 0 < 6000 * a ^ 2 * phi a := by linarith
    rcases mul_pos_iff.mp hprod with hpos | hneg
    · exact hpos.2
    · exact absurd hneg.1 (not_lt.mpr hcoef.le)
  have hphi_b : phi b < 0 := by
    have hquint : quintic b < 0 := by
      unfold quintic
      norm_num
    have hid := quintic_eq_phi (t := b) (by norm_num)
    have hcoef : 0 < 6000 * b ^ 2 := by positivity
    have hprod : 6000 * b ^ 2 * phi b < 0 := by linarith
    rcases mul_neg_iff.mp hprod with hpos | hneg
    · exact hpos.2
    · exact absurd hneg.1 hcoef.not_gt
  have hcont : ContinuousOn phi (Icc a b) := by
    have hphi : ∀ t ∈ Icc a b, phi t = quintic t / (6000 * t ^ 2) := by
      intro t ht
      have ht0 : t ≠ 0 := (lt_of_lt_of_le ha0 ht.1).ne'
      have hid := quintic_eq_phi ht0
      field_simp [ht0] at hid ⊢
      linarith
    refine ContinuousOn.congr ?_ hphi
    refine ContinuousOn.div ?_ ?_ ?_
    · unfold quintic
      fun_prop
    · fun_prop
    · intro t ht
      have ht0 : 0 < t := lt_of_lt_of_le ha0 ht.1
      positivity
  have hzero : (0 : ℝ) ∈ phi '' Icc a b := by
    refine intermediate_value_Icc' hab.le hcont ?_
    constructor
    · exact hphi_b.le
    · exact hphi_a.le
  obtain ⟨τ, hτ, hphi⟩ := hzero
  have hb2 : b ≤ 2 := by norm_num
  have hτa : a < τ := by
    rcases eq_or_lt_of_le hτ.1 with h | h
    · exact absurd (by simpa [h] using hphi) hphi_a.ne'
    · exact h
  have hτb : τ < b := by
    rcases eq_or_lt_of_le hτ.2 with h | h
    · exact absurd (by simpa [h] using hphi) hphi_b.ne
    · exact h
  have hsqrt_b : b < √(1 / 10) := by
    rw [lt_sqrt (by norm_num : (0 : ℝ) ≤ b)]
    norm_num
  have hlo : (31622 / 100000 : ℝ) < √(1 / 10) := by
    rw [lt_sqrt (by norm_num)]
    norm_num
  have hhi : √(1 / 10) < 31623 / 100000 := by
    rw [sqrt_lt (by norm_num : (0 : ℝ) ≤ 1 / 10) (by norm_num)]
    norm_num
  refine ⟨τ, hτa, hτb, hphi, ?_, hτb.trans hsqrt_b, hlo, hhi⟩
  intro τ' hτ'0 hτ'2 hzero'
  rcases lt_trichotomy τ' τ with hlt | hEq | hgt
  · have hanti := quintic_anti hτ'0.le (hτb.le.trans hb2) hlt
    have hτne : τ ≠ 0 := by linarith
    have hqτ : quintic τ = 0 := by
      rw [← quintic_eq_phi hτne, hphi]
      ring
    have hqτ' : quintic τ' = 0 := by
      rw [← quintic_eq_phi hτ'0.ne', hzero']
      ring
    linarith
  · exact hEq
  · have hanti := quintic_anti (by linarith : 0 ≤ τ) hτ'2 hgt
    have hτne : τ ≠ 0 := by linarith
    have hqτ : quintic τ = 0 := by
      rw [← quintic_eq_phi hτne, hphi]
      ring
    have hqτ' : quintic τ' = 0 := by
      rw [← quintic_eq_phi hτ'0.ne', hzero']
      ring
    linarith
