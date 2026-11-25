/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Finite-state learning rate, from `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`.
OPEN_WORK T60, batch 2.
-/
module

public import GTAO.HeatFloor
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.Order.BigOperators.Ring.Finset
public import Mathlib.Analysis.Convex.Jensen
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.Basic.ENNReal.Basic
public import Mathlib.InformationTheory.KullbackLeibler.KLFun
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# Finite-state learning rate

`theory/GENERAL_FLOOR_FINITE_2026-11-23.md`. The learning rate of an
exogenous world is the flux-weighted sum of Kullback–Leibler divergences
of the memory conditionals. A singular conditional has extended value
`⊤`. The real expansion of the joint information flow is stated when
every world state and every conditional atom is strictly positive.
-/

@[expose] public section

set_option linter.unusedSectionVars false

namespace FiniteFloor

open Classical InformationTheory
open scoped BigOperators ENNReal

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- Nonnegative mass. -/
def Nonneg (f : α → ℝ) : Prop := ∀ a, 0 ≤ f a

/-- Absolute continuity of finite mass functions: a positive atom of `p`
sits on a positive atom of `q`. -/
def AC (p q : α → ℝ) : Prop := ∀ a, p a ≠ 0 → 0 < q a

/-- A probability mass function on a finite alphabet. -/
def Prob (p : α → ℝ) : Prop := Nonneg p ∧ ∑ a, p a = 1

/-- Summand `q · klFun(p / q)`, with the value `0` when `q` is zero. -/
noncomputable def klSum (p q : α → ℝ) : ℝ :=
  ∑ a, if q a = 0 then 0 else q a * klFun (p a / q a)

/-- Kullback–Leibler divergence in `ℝ≥0∞`. A negative mass, or a pair that
is not absolutely continuous, gives `⊤`. -/
noncomputable def kl (p q : α → ℝ) : ENNReal :=
  if Nonneg p ∧ Nonneg q ∧ AC p q then ENNReal.ofReal (klSum p q) else ⊤

lemma klSum_nonneg {p q : α → ℝ} (hp : Nonneg p) (hq : Nonneg q) :
    0 ≤ klSum p q := by
  apply Finset.sum_nonneg
  intro a _
  by_cases hqa : q a = 0
  · simp [hqa]
  · have hqpos : 0 < q a := lt_of_le_of_ne (hq a) (Ne.symm hqa)
    have hr : 0 ≤ p a / q a := div_nonneg (hp a) hqpos.le
    simp [hqa, mul_nonneg hqpos.le (klFun_nonneg hr)]

lemma kl_nonneg (p q : α → ℝ) : 0 ≤ kl p q := bot_le

lemma kl_eq_top_of_not_ac {p q : α → ℝ} (_hp : Nonneg p) (_hq : Nonneg q) (hac : ¬ AC p q) :
    kl p q = ⊤ := by
  unfold kl
  rw [ite_eq_right (fun h => hac h.2.2)]

lemma kl_eq_ofReal {p q : α → ℝ} (hp : Nonneg p) (hq : Nonneg q) (hac : AC p q) :
    kl p q = ENNReal.ofReal (klSum p q) := by
  unfold kl
  rw [ite_eq_left ⟨hp, hq, hac⟩]

lemma klTerm_expand {p q : ℝ} (hq : 0 < q) (_hp : 0 ≤ p) :
    q * klFun (p / q) = p * Real.log (p / q) + q - p := by
  unfold klFun
  have hmul : q * ((p / q) * Real.log (p / q)) = p * Real.log (p / q) := by
    field_simp
  have hrest : q * (p / q) = p := by field_simp
  calc
    q * (p / q * Real.log (p / q) + 1 - p / q)
        = q * ((p / q) * Real.log (p / q)) + q * 1 - q * (p / q) := by ring
    _ = p * Real.log (p / q) + q - p := by rw [hmul, hrest]; ring

lemma klSum_eq_sum_log {p q : α → ℝ} (hp : Prob p) (hq : Prob q)
    (hpos : ∀ a, 0 < q a) : klSum p q = ∑ a, p a * Real.log (p a / q a) := by
  have hterm : ∀ a, (if q a = 0 then 0 else q a * klFun (p a / q a)) =
      p a * Real.log (p a / q a) + q a - p a := by
    intro a
    have hq0 : q a ≠ 0 := (hpos a).ne'
    simp only [hq0, ite_false]
    exact klTerm_expand (hpos a) (hp.1 a)
  simp_rw [klSum, hterm, Finset.sum_sub_distrib, Finset.sum_add_distrib]
  simp [hq.2, hp.2]

lemma kl_zero_iff {p q : α → ℝ} (hp : Prob p) (hq : Prob q) :
    kl p q = 0 ↔ p = q := by
  constructor
  · intro h0
    by_cases hac : AC p q
    · rw [kl_eq_ofReal hp.1 hq.1 hac] at h0
      have hsum0 : klSum p q = 0 :=
        le_antisymm (ENNReal.ofReal_eq_zero.mp h0) (klSum_nonneg hp.1 hq.1)
      have hterm : ∀ a, (if q a = 0 then 0 else q a * klFun (p a / q a)) = 0 := by
        have hnn : ∀ a ∈ Finset.univ,
            0 ≤ (if q a = 0 then (0 : ℝ) else q a * klFun (p a / q a)) := by
          intro a _
          by_cases hqa : q a = 0
          · simp [hqa]
          · have hqpos : 0 < q a := lt_of_le_of_ne (hq.1 a) (Ne.symm hqa)
            have hr : 0 ≤ p a / q a := div_nonneg (hp.1 a) hqpos.le
            simp [hqa, mul_nonneg hqpos.le (klFun_nonneg hr)]
        exact fun a => (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hsum0 a (Finset.mem_univ a)
      funext a
      by_cases hqa : q a = 0
      · have hpa : p a = 0 := by
          by_contra hne
          exact (not_lt.mpr (le_of_eq hqa)) (hac a hne)
        rw [hpa, hqa]
      · have hqpos : 0 < q a := lt_of_le_of_ne (hq.1 a) (Ne.symm hqa)
        have hkl : klFun (p a / q a) = 0 := by
          have hmul := hterm a
          simp only [hqa, ite_false] at hmul
          exact (mul_eq_zero.mp hmul).resolve_left hqa
        have hr : 0 ≤ p a / q a := div_nonneg (hp.1 a) hqpos.le
        have hratio : p a / q a = 1 := (klFun_eq_zero_iff hr).mp hkl
        field_simp at hratio
        exact hratio
    · rw [kl_eq_top_of_not_ac hp.1 hq.1 hac] at h0
      exact absurd h0 ENNReal.top_ne_zero
  · intro h
    subst h
    have hac : AC p p := fun a ha => lt_of_le_of_ne (hp.1 a) (Ne.symm ha)
    rw [kl_eq_ofReal hp.1 hp.1 hac]
    refine ENNReal.ofReal_eq_zero.mpr ?_
    unfold klSum
    apply le_of_eq
    apply Finset.sum_eq_zero
    intro a _
    by_cases hpa : p a = 0
    · simp [hpa]
    · simp [hpa, klFun_one]

/-- Total variation `(1/2) ∑ |p - q|`. -/
noncomputable def totalVariation (p q : α → ℝ) : ℝ :=
  (1 / 2) * ∑ a, |p a - q a|

lemma totalVariation_nonneg (p q : α → ℝ) : 0 ≤ totalVariation p q := by
  unfold totalVariation
  positivity

variable {X M : Type*} [Fintype X] [DecidableEq X] [Fintype M] [DecidableEq M]

/-- Directed flux `π(x) W(x → x')`. -/
noncomputable def flux (π : X → ℝ) (W : X → X → ℝ) (x x' : X) : ℝ :=
  π x * W x x'

/-- Incoming flux equals outgoing flux at every state. -/
def stationary (π : X → ℝ) (W : X → X → ℝ) : Prop :=
  ∀ x, ∑ x', flux π W x x' = ∑ x', flux π W x' x

lemma flux_nonneg {π : X → ℝ} {W : X → X → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (x x' : X) :
    0 ≤ flux π W x x' :=
  mul_nonneg (hπ x) (hW x x')

lemma flux_off_support {π : X → ℝ} {W : X → X → ℝ}
    (hstat : stationary π W) (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x')
    {x x' : X} (h : ¬ (0 < π x ∧ 0 < π x')) : flux π W x x' = 0 := by
  by_cases hx : 0 < π x
  · have hx' : ¬ 0 < π x' := by
      intro hx'
      exact h ⟨hx, hx'⟩
    have hx'0 : π x' = 0 := le_antisymm (le_of_not_gt hx') (hπ x')
    have hin : ∑ y, flux π W y x' = 0 := by
      rw [← hstat x']
      apply Finset.sum_eq_zero
      intro y _
      simp [flux, hx'0]
    have hnn : ∀ y ∈ Finset.univ, 0 ≤ flux π W y x' := fun y _ => flux_nonneg hπ hW y x'
    exact (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hin x (Finset.mem_univ x)
  · have hx0 : π x = 0 := le_antisymm (le_of_not_gt hx) (hπ x)
    simp [flux, hx0]

/-- The world term `∑ π W log(π'/π)`, summed on the occupied support. -/
noncomputable def worldSum (π : X → ℝ) (W : X → X → ℝ) : ℝ :=
  ∑ x, ∑ x', if 0 < π x ∧ 0 < π x' then flux π W x x' * Real.log (π x' / π x) else 0

theorem worldSum_stationary {π : X → ℝ} {W : X → X → ℝ}
    (hstat : stationary π W) (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') :
    worldSum π W = 0 := by
  have hsplit : worldSum π W =
      ∑ x, ∑ x', flux π W x x' * (Real.log (π x') - Real.log (π x)) := by
    unfold worldSum
    refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun x' _ => ?_
    by_cases h : 0 < π x ∧ 0 < π x'
    · rw [ite_eq_left h, Real.log_div h.2.ne' h.1.ne']
    · have hf := flux_off_support hstat hπ hW h
      rw [ite_eq_right h, hf]
      simp
  rw [hsplit]
  simp_rw [mul_sub, Finset.sum_sub_distrib]
  have hfirst : ∑ x, ∑ x', flux π W x x' * Real.log (π x') =
      ∑ x', Real.log (π x') * ∑ x, flux π W x x' := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x' _ => ?_
    have hcomm : ∑ x, flux π W x x' * Real.log (π x') =
        ∑ x, Real.log (π x') * flux π W x x' := by
      refine Finset.sum_congr rfl fun x _ => ?_
      ring
    rw [hcomm, ← Finset.mul_sum]
  have hsecond : ∑ x, ∑ x', flux π W x x' * Real.log (π x) =
      ∑ x, Real.log (π x) * ∑ x', flux π W x x' := by
    refine Finset.sum_congr rfl fun x _ => ?_
    have hcomm : ∑ x', flux π W x x' * Real.log (π x) =
        ∑ x', Real.log (π x) * flux π W x x' := by
      refine Finset.sum_congr rfl fun x' _ => ?_
      ring
    rw [hcomm, ← Finset.mul_sum]
  rw [hfirst, hsecond]
  have hsame : (∑ x', Real.log (π x') * ∑ x, flux π W x x') =
      ∑ x, Real.log (π x) * ∑ x', flux π W x x' := by
    refine Finset.sum_congr rfl fun z _ => ?_
    rw [show ∑ x, flux π W x z = ∑ x', flux π W z x' from (hstat z).symm]
  rw [hsame]
  ring

/-- Real learning rate, the flux-weighted sum of `klSum`. -/
noncomputable def iAltReal (π : X → ℝ) (W : X → X → ℝ) (p : X → M → ℝ) : ℝ :=
  ∑ x, ∑ x', flux π W x x' * klSum (p x) (p x')

/-- Extended learning rate. A positive flux times a singular divergence is `⊤`,
and a zero flux times `⊤` is `0`. -/
noncomputable def iAlt (π : X → ℝ) (W : X → X → ℝ) (p : X → M → ℝ) : ENNReal :=
  ∑ x, ∑ x', ENNReal.ofReal (flux π W x x') * kl (p x) (p x')

lemma ennreal_sum_eq_zero {ι : Type*} {s : Finset ι} {f : ι → ENNReal} :
    ∑ i ∈ s, f i = 0 ↔ ∀ i ∈ s, f i = 0 := by
  constructor
  · intro h i hi
    have hle : f i ≤ ∑ j ∈ s, f j :=
      Finset.single_le_sum (fun _ _ => bot_le) hi
    exact le_antisymm (by simpa [h] using hle) bot_le
  · exact fun h => Finset.sum_eq_zero h

lemma iAlt_nonneg (π : X → ℝ) (W : X → X → ℝ) (p : X → M → ℝ) : 0 ≤ iAlt π W p :=
  bot_le

lemma iAlt_eq_top_of_singular {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (_hπ : ∀ x, 0 ≤ π x) (_hW : ∀ x x', 0 ≤ W x x')
    {x x' : X} (hflux : 0 < flux π W x x')
    (hp : Prob (p x)) (hq : Prob (p x')) (hac : ¬ AC (p x) (p x')) :
    iAlt π W p = ⊤ := by
  have hterm : ENNReal.ofReal (flux π W x x') * kl (p x) (p x') = ⊤ := by
    rw [kl_eq_top_of_not_ac hp.1 hq.1 hac]
    have hne : ENNReal.ofReal (flux π W x x') ≠ 0 := by
      rw [ne_eq, ENNReal.ofReal_eq_zero]
      exact not_le.mpr hflux
    exact ENNReal.mul_top hne
  have hrow : ∑ y, ENNReal.ofReal (flux π W x y) * kl (p x) (p y) = ⊤ := by
    have : ENNReal.ofReal (flux π W x x') * kl (p x) (p x') ≤
        ∑ y, ENNReal.ofReal (flux π W x y) * kl (p x) (p y) :=
      Finset.single_le_sum (s := Finset.univ)
        (f := fun y => ENNReal.ofReal (flux π W x y) * kl (p x) (p y))
        (fun _ _ => bot_le) (Finset.mem_univ x')
    exact top_unique (hterm ▸ this)
  unfold iAlt
  have : (∑ y, ENNReal.ofReal (flux π W x y) * kl (p x) (p y)) ≤
      ∑ z, ∑ y, ENNReal.ofReal (flux π W z y) * kl (p z) (p y) :=
    Finset.single_le_sum (s := Finset.univ)
      (f := fun z => ∑ y, ENNReal.ofReal (flux π W z y) * kl (p z) (p y))
      (fun _ _ => bot_le) (Finset.mem_univ x)
  exact top_unique (hrow ▸ this)

theorem iAlt_zero_iff_edge {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x')
    (hp : ∀ x, Prob (p x)) :
    iAlt π W p = 0 ↔ ∀ x x', 0 < flux π W x x' → p x = p x' := by
  constructor
  · intro h0 x x' hflux
    have hterm : ENNReal.ofReal (flux π W x x') * kl (p x) (p x') = 0 := by
      have hrow : ∑ y, ENNReal.ofReal (flux π W x y) * kl (p x) (p y) = 0 :=
        (ennreal_sum_eq_zero.mp h0) x (Finset.mem_univ x)
      exact (ennreal_sum_eq_zero.mp hrow) x' (Finset.mem_univ x')
    rw [mul_eq_zero] at hterm
    rcases hterm with hflux0 | hkl
    · rw [ENNReal.ofReal_eq_zero] at hflux0
      exact absurd hflux (not_lt.mpr hflux0)
    · exact (kl_zero_iff (hp x) (hp x')).mp hkl
  · intro h
    unfold iAlt
    rw [ennreal_sum_eq_zero]
    intro x _
    rw [ennreal_sum_eq_zero]
    intro x' _
    by_cases hflux : 0 < flux π W x x'
    · have heq : p x = p x' := h x x' hflux
      have hkl : kl (p x) (p x') = 0 := (kl_zero_iff (hp x) (hp x')).mpr heq
      simp [hkl]
    · have hle : flux π W x x' ≤ 0 := not_lt.mp hflux
      have hf : flux π W x x' = 0 := le_antisymm hle (flux_nonneg hπ hW x x')
      simp [hf]

/-- Joint information flow, defined as a real when every atom below is positive. -/
noncomputable def infoX (π : X → ℝ) (W : X → X → ℝ) (p : X → M → ℝ) : ℝ :=
  ∑ x, ∑ x', ∑ m, (π x * p x m * W x x') *
    Real.log ((π x' * p x' m) / (π x * p x m))

theorem destruction_identity {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 < π x) (hp : ∀ x m, 0 < p x m) (hprob : ∀ x, Prob (p x)) :
    infoX π W p = worldSum π W - iAltReal π W p := by
  have hlog : ∀ x x' m, Real.log ((π x' * p x' m) / (π x * p x m)) =
      Real.log (π x' / π x) + Real.log (p x' m / p x m) := by
    intro x x' m
    have hρ : 0 < π x * p x m := mul_pos (hπ x) (hp x m)
    have hρ' : 0 < π x' * p x' m := mul_pos (hπ x') (hp x' m)
    rw [Real.log_div hρ'.ne' hρ.ne', Real.log_mul (hπ x').ne' (hp x' m).ne',
      Real.log_mul (hπ x).ne' (hp x m).ne', Real.log_div (hπ x').ne' (hπ x).ne',
      Real.log_div (hp x' m).ne' (hp x m).ne']
    ring
  unfold infoX
  simp_rw [hlog, mul_add, Finset.sum_add_distrib]
  have hworld : ∑ x, ∑ x', ∑ m, π x * p x m * W x x' * Real.log (π x' / π x) = worldSum π W := by
    unfold worldSum
    refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun x' _ => ?_
    have hpos : 0 < π x ∧ 0 < π x' := ⟨hπ x, hπ x'⟩
    rw [ite_eq_left hpos]
    have hpull : ∀ m, π x * p x m * W x x' * Real.log (π x' / π x) =
        p x m * (flux π W x x' * Real.log (π x' / π x)) := by
      intro m
      unfold flux
      ring
    simp_rw [hpull]
    rw [← Finset.sum_mul, (hprob x).2, one_mul]
  have hmem : ∑ x, ∑ x', ∑ m, π x * p x m * W x x' * Real.log (p x' m / p x m) =
      -iAltReal π W p := by
    unfold iAltReal
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun x' _ => ?_
    have hpull : ∀ m, π x * p x m * W x x' * Real.log (p x' m / p x m) =
        (p x m * Real.log (p x' m / p x m)) * flux π W x x' := by
      intro m
      unfold flux
      ring
    simp_rw [hpull]
    rw [← Finset.sum_mul]
    have hkl := klSum_eq_sum_log (hprob x) (hprob x') (fun m => hp x' m)
    have hsign : ∀ m, p x m * Real.log (p x' m / p x m) =
        -(p x m * Real.log (p x m / p x' m)) := by
      intro m
      have hratio : p x' m / p x m = (p x m / p x' m)⁻¹ := by field_simp
      rw [hratio, Real.log_inv]
      ring
    simp_rw [hsign]
    rw [Finset.sum_neg_distrib, hkl]
    ring
  rw [hworld, hmem]
  ring

theorem stationary_learning_rate {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hstat : stationary π W) (hπ0 : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x')
    (hπ : ∀ x, 0 < π x) (hp : ∀ x m, 0 < p x m) (hprob : ∀ x, Prob (p x)) :
    iAltReal π W p = -infoX π W p := by
  have hinfo := destruction_identity (W := W) hπ hp hprob
  have hworld := worldSum_stationary hstat hπ0 hW
  rw [hinfo, hworld]
  ring

/-- Bayes error `1 - ∑_m max_x joint(x, m)`. Requires a nonempty world. -/
noncomputable def bayesError [Nonempty X] (joint : X → M → ℝ) : ℝ :=
  1 - ∑ m, Finset.univ.sup' Finset.univ_nonempty (fun x => joint x m)

/-- Chance error `1 - max_x π(x)`. -/
noncomputable def chanceError [Nonempty X] (π : X → ℝ) : ℝ :=
  1 - Finset.univ.sup' Finset.univ_nonempty π

lemma sup'_witness_irrelevant {β : Type*} (s : Finset β) (f : β → ℝ) (H H' : s.Nonempty) :
    s.sup' H f = s.sup' H' f := by
  apply WithBot.coe_injective
  simp [Finset.coe_sup']

lemma le_sup'_univ [Nonempty X] (f : X → ℝ) {x : X} :
    f x ≤ Finset.univ.sup' Finset.univ_nonempty f := by
  have h := Finset.le_sup' f (Finset.mem_univ x)
  rwa [sup'_witness_irrelevant (Finset.univ : Finset X) f ⟨x, Finset.mem_univ x⟩
    Finset.univ_nonempty] at h

/-- If the conditional does not depend on the world, the Bayes error equals chance.
Lines 41–45 and 97. -/
theorem bayes_of_constant [Nonempty X] {π : X → ℝ} {p : M → ℝ}
    (_hπ : ∀ x, 0 ≤ π x) (hp : Prob p) (_hsum : ∑ x, π x = 1) :
    bayesError (fun x m => π x * p m) = chanceError π := by
  unfold bayesError chanceError
  have hsup : ∀ m, Finset.univ.sup' Finset.univ_nonempty (fun x => π x * p m) =
      Finset.univ.sup' Finset.univ_nonempty π * p m := by
    intro m
    apply le_antisymm
    · rw [Finset.sup'_le_iff]
      intro x _
      exact mul_le_mul_of_nonneg_right (le_sup'_univ π) (hp.1 m)
    · obtain ⟨x, _, hmax⟩ := Finset.exists_mem_eq_sup' (s := Finset.univ) Finset.univ_nonempty π
      rw [hmax, Finset.le_sup'_iff]
      exact ⟨x, Finset.mem_univ x, le_rfl⟩
  simp_rw [hsup, ← Finset.mul_sum, hp.2, mul_one]

end FiniteFloor
