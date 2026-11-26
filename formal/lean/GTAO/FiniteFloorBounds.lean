/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Witnesses for the finite-state learning rate.
`theory/GENERAL_FLOOR_FINITE_2026-11-23.md`, OPEN_WORK T60, batch 2.
-/
module

public import GTAO.FiniteFloor
public import Mathlib.Analysis.Convex.Jensen
public import Mathlib.Analysis.SpecialFunctions.Exp
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# Witnesses

The learning-rate sum is zero on a frozen world and on a two-class memory
whose occupied flux graph is disconnected. It stays positive on a stationary
3-cycle whose Bayes error equals chance.
-/

@[expose] public section

set_option linter.unusedSectionVars false

namespace FiniteFloor

open InformationTheory
open scoped BigOperators ENNReal

variable {X M : Type*} [Fintype X] [DecidableEq X] [Fintype M] [DecidableEq M]

theorem frozen_support {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (_hπ : ∀ x, 0 ≤ π x) (_hW : ∀ x x', 0 ≤ W x x')
    (hflux : ∀ x x', flux π W x x' = 0) : iAlt π W p = 0 := by
  unfold iAlt
  rw [ennreal_sum_eq_zero]
  intro x _
  rw [ennreal_sum_eq_zero]
  intro x' _
  simp [hflux x x', ENNReal.ofReal_zero, zero_mul]

theorem boltzmann_below_half : 1 / (1 + Real.exp 1) < (1 : ℝ) / 2 := by
  have hexp : (1 : ℝ) < Real.exp 1 := by
    have := Real.add_one_lt_exp (by norm_num : (1 : ℝ) ≠ 0)
    linarith
  rw [div_lt_iff₀ (by positivity : (0 : ℝ) < 1 + Real.exp 1)]
  linarith

/-- A positive-flux step. -/
def PosFlux (π : X → ℝ) (W : X → X → ℝ) (x x' : X) : Prop :=
  0 < flux π W x x'

inductive Reach (π : X → ℝ) (W : X → X → ℝ) : X → X → Prop where
  | refl (x : X) : Reach π W x x
  | tail {x y z : X} : PosFlux π W x y → Reach π W y z → Reach π W x z

def stronglyConnected (π : X → ℝ) (W : X → X → ℝ) : Prop :=
  ∀ x x', 0 < π x → 0 < π x' → Reach π W x x'

lemma reach_same_conditional {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (h0 : iAlt π W p = 0) {x z : X} (hr : Reach π W x z) : p x = p z := by
  have hedge : ∀ a b, PosFlux π W a b → p a = p b := by
    intro a b he
    exact (iAlt_zero_iff_edge hπ hW hp).mp h0 a b he
  induction hr with
  | refl => rfl
  | tail he _ ih => rw [hedge _ _ he, ih]

theorem iAlt_zero_stronglyConnected [Nonempty X] {π : X → ℝ} {W : X → X → ℝ}
    {p : X → M → ℝ} (hπ : ∀ x, 0 ≤ π x) (hsum : ∑ x, π x = 1)
    (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (hconn : stronglyConnected π W) (h0 : iAlt π W p = 0) :
    bayesError (fun x m => π x * p x m) = chanceError π := by
  have hpos : ∃ x, 0 < π x := by
    by_contra hall
    push Not at hall
    have hzero : ∑ x, π x = 0 :=
      Finset.sum_eq_zero fun x _ => le_antisymm (hall x) (hπ x)
    linarith
  obtain ⟨x0, hx0⟩ := hpos
  let q : M → ℝ := p x0
  have hsame : ∀ x, 0 < π x → p x = q := by
    intro x hx
    exact reach_same_conditional hπ hW hp h0 (hconn x x0 hx hx0)
  have hjoint : (fun x m => π x * p x m) = fun x m => π x * q m := by
    funext x m
    by_cases hx : 0 < π x
    · rw [hsame x hx]
    · have hxzero : π x = 0 := le_antisymm (not_lt.mp hx) (hπ x)
      simp [hxzero]
  have hq : Prob q := hp x0
  simpa [hjoint] using bayes_of_constant hπ hq hsum

lemma sup_fin3 (f : Fin 3 → ℝ) :
    (Finset.univ : Finset (Fin 3)).sup' Finset.univ_nonempty f =
      max (max (f 0) (f 1)) (f 2) := by
  apply le_antisymm
  · rw [Finset.sup'_le_iff]
    intro i _
    fin_cases i
    · exact le_trans (le_max_left (f 0) (f 1)) (le_max_left _ (f 2))
    · exact le_trans (le_max_right (f 0) (f 1)) (le_max_left _ (f 2))
    · exact le_max_right (max (f 0) (f 1)) (f 2)
  · refine max_le (max_le ?_ ?_) ?_
    · exact le_sup'_univ (f := f) (x := 0)
    · exact le_sup'_univ (f := f) (x := 1)
    · exact le_sup'_univ (f := f) (x := 2)

/-- Class indicator on `{0,1}` versus `{2}`. The printed soft-memory value
`0.312590` is not this witness. -/
noncomputable def classπ : Fin 3 → ℝ
  | 0 => 3 / 10
  | 1 => 3 / 10
  | 2 => 2 / 5

noncomputable def classW : Fin 3 → Fin 3 → ℝ
  | 0, 1 => 1
  | 1, 0 => 1
  | _, _ => 0

noncomputable def classP : Fin 3 → Fin 2 → ℝ
  | 0, 0 => 1
  | 1, 0 => 1
  | 2, 1 => 1
  | _, _ => 0

lemma classP_prob (x : Fin 3) : Prob (classP x) := by
  fin_cases x <;> refine ⟨?_, ?_⟩ <;>
    first
      | intro m; fin_cases m <;> norm_num [classP]
      | rw [Fin.sum_univ_two]; norm_num [classP]

lemma classP_same : classP 0 = classP 1 := by
  funext m
  fin_cases m <;> rfl

theorem two_class_counterexample :
    iAlt classπ classW classP = 0 ∧
      bayesError (fun x m => classπ x * classP x m) = 3 / 10 ∧
      chanceError classπ = 3 / 5 ∧ classW 0 1 ≠ 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold iAlt
    rw [ennreal_sum_eq_zero]
    intro x _
    rw [ennreal_sum_eq_zero]
    intro y _
    fin_cases x <;> fin_cases y
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · have hkl : kl (classP 0) (classP 1) = 0 :=
        (kl_zero_iff (classP_prob 0) (classP_prob 1)).mpr classP_same
      simp [flux, classπ, classW, hkl]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · have hkl : kl (classP 1) (classP 0) = 0 :=
        (kl_zero_iff (classP_prob 1) (classP_prob 0)).mpr classP_same.symm
      simp [flux, classπ, classW, hkl]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
    · simp [flux, classπ, classW, ENNReal.ofReal_zero, zero_mul]
  · have hm0 : Finset.univ.sup' Finset.univ_nonempty (fun x : Fin 3 => classπ x * classP x 0) =
        3 / 10 := by
      rw [sup_fin3]
      norm_num [classπ, classP]
    have hm1 : Finset.univ.sup' Finset.univ_nonempty (fun x : Fin 3 => classπ x * classP x 1) =
        2 / 5 := by
      rw [sup_fin3]
      norm_num [classπ, classP]
    unfold bayesError
    rw [Fin.sum_univ_two, hm0, hm1]
    norm_num
  · unfold chanceError
    rw [sup_fin3]
    norm_num [classπ]
  · norm_num [classW]

noncomputable def cycleπ : Fin 3 → ℝ
  | 0 => 1 / 2
  | 1 => 1 / 4
  | 2 => 1 / 4

noncomputable def cycleW : Fin 3 → Fin 3 → ℝ
  | 0, 1 => 1
  | 1, 2 => 2
  | 2, 0 => 2
  | _, _ => 0

noncomputable def cycleP : Fin 3 → Fin 2 → ℝ
  | 0, 0 => 1 / 2
  | 0, 1 => 1 / 2
  | 1, 0 => 4 / 5
  | 1, 1 => 1 / 5
  | 2, 0 => 1 / 5
  | 2, 1 => 4 / 5

lemma cycle_flux01 : flux cycleπ cycleW 0 1 = 1 / 2 := by
  simp [flux, cycleπ, cycleW]

theorem converse_fails_three :
    bayesError (fun x m => cycleπ x * cycleP x m) = chanceError cycleπ ∧
      0 < iAlt cycleπ cycleW cycleP := by
  constructor
  · have hm0 : Finset.univ.sup' Finset.univ_nonempty (fun x : Fin 3 => cycleπ x * cycleP x 0) =
        1 / 4 := by
      rw [sup_fin3]
      norm_num [cycleπ, cycleP]
    have hm1 : Finset.univ.sup' Finset.univ_nonempty (fun x : Fin 3 => cycleπ x * cycleP x 1) =
        1 / 4 := by
      rw [sup_fin3]
      norm_num [cycleπ, cycleP]
    unfold bayesError chanceError
    rw [Fin.sum_univ_two, hm0, hm1, sup_fin3]
    norm_num [cycleπ]
  · have hpos : 0 < klSum (cycleP 0) (cycleP 1) := by
      unfold klSum
      rw [Fin.sum_univ_two]
      simp only [cycleP]
      have hr : 0 ≤ (1 / 2 : ℝ) / (4 / 5) := by norm_num
      have hne : (1 / 2 : ℝ) / (4 / 5) ≠ 1 := by norm_num
      have hfun : 0 < klFun ((1 / 2) / (4 / 5)) :=
        lt_of_le_of_ne (klFun_nonneg hr) (by
          intro hzero
          exact hne ((klFun_eq_zero_iff hr).mp hzero.symm))
      have hterm : 0 < (4 / 5) * klFun ((1 / 2) / (4 / 5)) := mul_pos (by norm_num) hfun
      have hother : 0 ≤ (1 / 5 : ℝ) * klFun ((1 / 2) / (1 / 5)) := by
        have hr' : 0 ≤ (1 / 2 : ℝ) / (1 / 5) := by norm_num
        exact mul_nonneg (by norm_num) (klFun_nonneg hr')
      have hne0 : (4 / 5 : ℝ) ≠ 0 := by norm_num
      have hne1 : (1 / 5 : ℝ) ≠ 0 := by norm_num
      simp only [hne0, hne1, ite_false]
      linarith
    have hac : AC (cycleP 0) (cycleP 1) := by
      intro a ha
      fin_cases a <;> norm_num [cycleP] at ha ⊢
    have hp0 : Prob (cycleP 0) := by
      refine ⟨?_, ?_⟩
      · intro a; fin_cases a <;> norm_num [cycleP]
      · rw [Fin.sum_univ_two]; norm_num [cycleP]
    have hp1 : Prob (cycleP 1) := by
      refine ⟨?_, ?_⟩
      · intro a; fin_cases a <;> norm_num [cycleP]
      · rw [Fin.sum_univ_two]; norm_num [cycleP]
    have hterm : 0 < ENNReal.ofReal (flux cycleπ cycleW 0 1) * kl (cycleP 0) (cycleP 1) := by
      rw [kl_eq_ofReal hp0.1 hp1.1 hac, cycle_flux01]
      rw [← ENNReal.ofReal_mul (by norm_num : (0 : ℝ) ≤ 1 / 2), ENNReal.ofReal_pos]
      exact mul_pos (by norm_num) hpos
    have hle : ENNReal.ofReal (flux cycleπ cycleW 0 1) * kl (cycleP 0) (cycleP 1) ≤
        iAlt cycleπ cycleW cycleP := by
      unfold iAlt
      refine le_trans ?_ (Finset.single_le_sum (s := Finset.univ)
        (f := fun x : Fin 3 => ∑ y, ENNReal.ofReal (flux cycleπ cycleW x y) * kl (cycleP x) (cycleP y))
        (fun _ _ => bot_le) (Finset.mem_univ 0))
      exact Finset.single_le_sum (s := Finset.univ)
        (f := fun y : Fin 3 => ENNReal.ofReal (flux cycleπ cycleW 0 y) * kl (cycleP 0) (cycleP y))
        (fun _ _ => bot_le) (Finset.mem_univ 1)
    exact lt_of_lt_of_le hterm hle

end FiniteFloor
