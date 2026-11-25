/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Lemmas C, P, C on the nonnegative integers, and M, from
`theory/REPRESENTATION.md` §2. OPEN_WORK T19, batch 1.
-/
module

public import Mathlib.Basic.Real.Basic
public import Mathlib.Data.Rat.Cast.Order
public import Mathlib.Order.Monotone.Basic
public import Mathlib.Topology.Order.OrderClosed
public import Mathlib.Analysis.SpecificLimits.Basic
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum

/-!
# Cauchy, Pexider, and sign lemmas

`theory/REPRESENTATION.md` §2. The domain of Lemmas C and P is `(0, ∞)`,
as written there. A discontinuous additive function is excluded by the
monotonicity hypothesis or the continuity hypothesis. Its existence is
not formalized.
-/

@[expose] public section

namespace Representation

open Set Filter Topology

variable {f : ℝ → ℝ}

/-- Additivity on positive reals, the hypothesis of Lemma C. -/
def AdditiveOnPos (f : ℝ → ℝ) : Prop :=
  ∀ ⦃x y : ℝ⦄, 0 < x → 0 < y → f (x + y) = f x + f y

/-- Pexider's equation on positive reals: additivity up to a constant. -/
def Concatenates (f : ℝ → ℝ) (c : ℝ) : Prop :=
  ∀ ⦃x y : ℝ⦄, 0 < x → 0 < y → f (x + y) = f x + f y + c

lemma mul_nat (hadd : AdditiveOnPos f) {x : ℝ} (hx : 0 < x) :
    ∀ n : ℕ, 0 < n → f ((n : ℝ) * x) = (n : ℝ) * f x := by
  intro n hn
  induction n with
  | zero =>
    cases hn
  | succ n ih =>
    cases n with
    | zero =>
      simp
    | succ n =>
      have hn1 : 0 < n.succ := Nat.succ_pos n
      have hx1 : 0 < ((n.succ : ℕ) : ℝ) * x := by positivity
      have hstep := hadd hx1 hx
      have hsum : ((n.succ.succ : ℕ) : ℝ) * x = ((n.succ : ℕ) : ℝ) * x + x := by
        push_cast
        ring
      rw [← hsum] at hstep
      rw [hstep, ih hn1]
      push_cast
      ring

/-- Lemma C, the rational identity. No monotonicity is used, and `f(1)` may
have either sign. `theory/REPRESENTATION.md:70`. -/
theorem cauchy_rat (hadd : AdditiveOnPos f) {q : ℚ} (hq : 0 < q) :
    f (q : ℝ) = (q : ℝ) * f 1 := by
  have hnum : 0 < q.num := Rat.num_pos.mpr hq
  have hden : 0 < q.den := q.den_pos
  have hn : 0 < q.num.toNat := Nat.pos_of_ne_zero <| by
    intro hzero
    have := (Int.toNat_eq_zero).mp hzero
    exact (not_le.mpr hnum) this
  have hrec : 0 < (1 : ℝ) / (q.den : ℝ) := by positivity
  have hden_mul := mul_nat hadd hrec q.den hden
  have hden_one : ((q.den : ℕ) : ℝ) * ((1 : ℝ) / q.den) = 1 := by
    field_simp
  rw [hden_one] at hden_mul
  have hinv : f ((1 : ℝ) / q.den) = f 1 / q.den := by
    have hne : ((q.den : ℕ) : ℝ) ≠ 0 := by exact_mod_cast hden.ne'
    apply mul_left_cancel₀ hne
    calc
      ((q.den : ℕ) : ℝ) * f ((1 : ℝ) / q.den) = f 1 := hden_mul.symm
      _ = ((q.den : ℕ) : ℝ) * (f 1 / q.den) := by field_simp
  have hnum_mul := mul_nat hadd hrec q.num.toNat hn
  have hcast : (q : ℝ) = (q.num.toNat : ℝ) / q.den := by
    rw [Rat.cast_def]
    have hnumcast : (q.num : ℝ) = q.num.toNat := by
      exact_mod_cast (Int.toNat_of_nonneg hnum.le).symm
    rw [hnumcast]
  calc
    f (q : ℝ) = f ((q.num.toNat : ℝ) * ((1 : ℝ) / q.den)) := by
      rw [hcast, div_eq_mul_one_div]
    _ = (q.num.toNat : ℝ) * f ((1 : ℝ) / q.den) := hnum_mul
    _ = (q.num.toNat : ℝ) * (f 1 / q.den) := by rw [hinv]
    _ = (q : ℝ) * f 1 := by
      rw [hcast]
      field_simp

lemma f_one_nonneg_of_nondecreasing (hadd : AdditiveOnPos f)
    (hmon : MonotoneOn f (Set.Ioi 0)) : 0 ≤ f 1 := by
  have h2 : f (1 + 1) = f 1 + f 1 := hadd one_pos one_pos
  have hle : f 1 ≤ f (1 + 1) := hmon (by norm_num) (by norm_num) (by norm_num)
  linarith

lemma f_one_nonpos_of_nonincreasing (hadd : AdditiveOnPos f)
    (hmon : AntitoneOn f (Set.Ioi 0)) : f 1 ≤ 0 := by
  have h2 : f (1 + 1) = f 1 + f 1 := hadd one_pos one_pos
  have hle : f (1 + 1) ≤ f 1 := hmon (by norm_num) (by norm_num) (by norm_num)
  linarith

lemma below_gap {x : ℝ} (hx : 0 < x) (n : ℕ) :
    x * (n : ℝ) / ((n : ℝ) + 1) < x := by
  have hden : 0 < (n : ℝ) + 1 := by positivity
  rw [div_lt_iff₀ hden]
  nlinarith [hx]

lemma above_gap {x : ℝ} (hx : 0 < x) (n : ℕ) :
    x < x * ((n : ℝ) + 2) / ((n : ℝ) + 1) := by
  have hden : 0 < (n : ℝ) + 1 := by positivity
  rw [lt_div_iff₀ hden]
  nlinarith [hx]

/-- A positive rational strictly below `x`. -/
noncomputable def ratBelow (x : ℝ) (hx : 0 < x) (n : ℕ) : ℚ :=
  Classical.choose (exists_rat_btwn (below_gap hx n))

/-- A positive rational strictly above `x`. -/
noncomputable def ratAbove (x : ℝ) (hx : 0 < x) (n : ℕ) : ℚ :=
  Classical.choose (exists_rat_btwn (above_gap hx n))

lemma ratBelow_bounds {x : ℝ} (hx : 0 < x) (n : ℕ) :
    x * (n : ℝ) / ((n : ℝ) + 1) < (ratBelow x hx n : ℝ) ∧ (ratBelow x hx n : ℝ) < x :=
  Classical.choose_spec (exists_rat_btwn (below_gap hx n))

lemma ratAbove_bounds {x : ℝ} (hx : 0 < x) (n : ℕ) :
    x < (ratAbove x hx n : ℝ) ∧
      (ratAbove x hx n : ℝ) < x * ((n : ℝ) + 2) / ((n : ℝ) + 1) :=
  Classical.choose_spec (exists_rat_btwn (above_gap hx n))

lemma tendsto_mul_div (x : ℝ) :
    Tendsto (fun n : ℕ => x * (n : ℝ) / ((n : ℝ) + 1)) atTop (nhds x) := by
  have h := (tendsto_natCast_div_add_atTop (1 : ℝ)).const_mul x
  have h' : Tendsto (fun n : ℕ => x * ((n : ℝ) / ((n : ℝ) + 1))) atTop (nhds x) := by
    simpa [mul_one] using h
  refine h'.congr fun n => ?_
  ring

lemma tendsto_mul_div_above (x : ℝ) :
    Tendsto (fun n : ℕ => x * ((n : ℝ) + 2) / ((n : ℝ) + 1)) atTop (nhds x) := by
  have hmain := tendsto_mul_div x
  have htail : Tendsto (fun n : ℕ => x * (2 / ((n : ℝ) + 1))) atTop (nhds 0) := by
    have h0 := tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ)
    have h2 := h0.const_mul (2 : ℝ)
    have h3 := h2.const_mul x
    simp only [mul_zero] at h3
    refine h3.congr fun n => ?_
    ring
  have hsplit : ∀ n : ℕ, x * ((n : ℝ) + 2) / ((n : ℝ) + 1) =
      x * (n : ℝ) / ((n : ℝ) + 1) + x * (2 / ((n : ℝ) + 1)) := by
    intro n
    field_simp
  have hsum := hmain.add htail
  have hsum' : Tendsto (fun n : ℕ =>
      x * (n : ℝ) / ((n : ℝ) + 1) + x * (2 / ((n : ℝ) + 1))) atTop (nhds x) := by
    simpa using hsum
  exact hsum'.congr fun n => (hsplit n).symm

lemma tendsto_ratBelow {x : ℝ} (hx : 0 < x) :
    Tendsto (fun n => (ratBelow x hx n : ℝ)) atTop (nhds x) :=
  tendsto_of_tendsto_of_tendsto_of_le_of_le (tendsto_mul_div x) tendsto_const_nhds
    (fun n => (ratBelow_bounds hx n).1.le) (fun n => (ratBelow_bounds hx n).2.le)

lemma tendsto_ratAbove {x : ℝ} (hx : 0 < x) :
    Tendsto (fun n => (ratAbove x hx n : ℝ)) atTop (nhds x) :=
  tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds (tendsto_mul_div_above x)
    (fun n => (ratAbove_bounds hx n).1.le) (fun n => (ratAbove_bounds hx n).2.le)

lemma eq_of_squeeze {a b : ℝ} {u v : ℕ → ℝ}
    (hu : Tendsto u atTop (nhds a)) (hv : Tendsto v atTop (nhds a))
    (hub : ∀ n, u n ≤ b) (hbv : ∀ n, b ≤ v n) : b = a := by
  have h1 : a ≤ b :=
    le_of_tendsto_of_tendsto hu (tendsto_const_nhds (x := b)) (Eventually.of_forall hub)
  have h2 : b ≤ a :=
    le_of_tendsto_of_tendsto (tendsto_const_nhds (x := b)) hv (Eventually.of_forall hbv)
  exact le_antisymm h2 h1

/-- Lemma C (i), both directions. `theory/REPRESENTATION.md:70`. -/
theorem cauchy_monotone (hadd : AdditiveOnPos f) {x : ℝ} (hx : 0 < x)
    (hmon : MonotoneOn f (Set.Ioi 0) ∨ AntitoneOn f (Set.Ioi 0)) :
    f x = x * f 1 := by
  have hq_pos : ∀ n, 0 < (ratBelow x hx n : ℝ) := by
    intro n
    exact lt_of_le_of_lt (by positivity) (ratBelow_bounds hx n).1
  have hr_pos : ∀ n, 0 < (ratAbove x hx n : ℝ) := by
    intro n
    exact lt_trans hx (ratAbove_bounds hx n).1
  have hratq : ∀ n, f (ratBelow x hx n) = (ratBelow x hx n : ℝ) * f 1 :=
    fun n => cauchy_rat hadd (Rat.cast_pos.mp (hq_pos n))
  have hratr : ∀ n, f (ratAbove x hx n) = (ratAbove x hx n : ℝ) * f 1 :=
    fun n => cauchy_rat hadd (Rat.cast_pos.mp (hr_pos n))
  rcases hmon with hmon | hmon
  · have hleft : ∀ n, (ratBelow x hx n : ℝ) * f 1 ≤ f x := by
      intro n
      rw [← hratq n]
      exact hmon (mem_Ioi.mpr (hq_pos n)) (mem_Ioi.mpr hx) (ratBelow_bounds hx n).2.le
    have hright : ∀ n, f x ≤ (ratAbove x hx n : ℝ) * f 1 := by
      intro n
      rw [← hratr n]
      exact hmon (mem_Ioi.mpr hx) (mem_Ioi.mpr (hr_pos n)) (ratAbove_bounds hx n).1.le
    exact eq_of_squeeze ((tendsto_ratBelow hx).mul_const (f 1))
      ((tendsto_ratAbove hx).mul_const (f 1)) hleft hright
  · have hleft : ∀ n, f x ≤ (ratBelow x hx n : ℝ) * f 1 := by
      intro n
      rw [← hratq n]
      exact hmon (mem_Ioi.mpr (hq_pos n)) (mem_Ioi.mpr hx) (ratBelow_bounds hx n).2.le
    have hright : ∀ n, (ratAbove x hx n : ℝ) * f 1 ≤ f x := by
      intro n
      rw [← hratr n]
      exact hmon (mem_Ioi.mpr hx) (mem_Ioi.mpr (hr_pos n)) (ratAbove_bounds hx n).1.le
    exact eq_of_squeeze ((tendsto_ratAbove hx).mul_const (f 1))
      ((tendsto_ratBelow hx).mul_const (f 1)) hright hleft

/-- Lemma C (ii). Continuity replaces the squeeze. `theory/REPRESENTATION.md:72`. -/
theorem cauchy_continuous (hadd : AdditiveOnPos f) (hcont : ContinuousOn f (Set.Ioi 0))
    {x : ℝ} (hx : 0 < x) : f x = x * f 1 := by
  have hq_pos : ∀ n, 0 < (ratBelow x hx n : ℝ) := by
    intro n
    exact lt_of_le_of_lt (by positivity) (ratBelow_bounds hx n).1
  have hmem : ∀ n, (ratBelow x hx n : ℝ) ∈ Set.Ioi 0 := fun n => mem_Ioi.mpr (hq_pos n)
  have htend : Tendsto (fun n => (ratBelow x hx n : ℝ)) atTop (nhdsWithin x (Set.Ioi 0)) :=
    tendsto_nhdsWithin_iff.mpr ⟨tendsto_ratBelow hx, Eventually.of_forall hmem⟩
  have hcomp : Tendsto (fun n => f (ratBelow x hx n)) atTop (nhds (f x)) :=
    (hcont.continuousWithinAt (mem_Ioi.mpr hx)).tendsto.comp htend
  have hrat : Tendsto (fun n => f (ratBelow x hx n)) atTop (nhds (x * f 1)) := by
    refine ((tendsto_ratBelow hx).mul_const (f 1)).congr fun n => ?_
    exact (cauchy_rat hadd (Rat.cast_pos.mp (hq_pos n))).symm
  exact tendsto_nhds_unique hcomp hrat

/-- Lemma P, monotone case. `theory/REPRESENTATION.md:76`. -/
theorem pexider_monotone {c : ℝ} (h : Concatenates f c) {x : ℝ} (hx : 0 < x)
    (hmon : MonotoneOn f (Set.Ioi 0) ∨ AntitoneOn f (Set.Ioi 0)) :
    f x = (f 1 + c) * x - c := by
  let g : ℝ → ℝ := fun z => f z + c
  have hg : AdditiveOnPos g := by
    intro a b ha hb
    simp only [g]
    linarith [h ha hb]
  have hmon' : MonotoneOn g (Set.Ioi 0) ∨ AntitoneOn g (Set.Ioi 0) := by
    rcases hmon with hmon | hmon
    · exact Or.inl fun a ha b hb hab => by
        have := hmon ha hb hab
        simp only [g]
        linarith
    · exact Or.inr fun a ha b hb hab => by
        have := hmon ha hb hab
        simp only [g]
        linarith
  have hlin : g x = x * g 1 := cauchy_monotone hg hx hmon'
  have hlin' : f x + c = x * (f 1 + c) := by simpa [g] using hlin
  calc
    f x = (f x + c) - c := by ring
    _ = x * (f 1 + c) - c := by rw [hlin']
    _ = (f 1 + c) * x - c := by ring

/-- Lemma P, continuous case. `theory/REPRESENTATION.md:76`. -/
theorem pexider_continuous {c : ℝ} (h : Concatenates f c)
    (hcont : ContinuousOn f (Set.Ioi 0)) {x : ℝ} (hx : 0 < x) :
    f x = (f 1 + c) * x - c := by
  let g : ℝ → ℝ := fun z => f z + c
  have hg : AdditiveOnPos g := by
    intro a b ha hb
    simp only [g]
    linarith [h ha hb]
  have hcont' : ContinuousOn g (Set.Ioi 0) := hcont.add continuousOn_const
  have hlin : g x = x * g 1 := cauchy_continuous hg hcont' hx
  have hlin' : f x + c = x * (f 1 + c) := by simpa [g] using hlin
  calc
    f x = (f x + c) - c := by ring
    _ = x * (f 1 + c) - c := by rw [hlin']
    _ = (f 1 + c) * x - c := by ring

/-- Lemma C on the nonnegative integers. `theory/REPRESENTATION.md:78`. -/
theorem cauchy_nat (fn : ℕ → ℝ) (hadd : ∀ m n, fn (m + n) = fn m + fn n) :
    fn 0 = 0 ∧ ∀ n, fn n = (n : ℝ) * fn 1 := by
  have h0 : fn 0 = 0 := by
    have := hadd 0 0
    linarith
  refine ⟨h0, fun n => ?_⟩
  induction n with
  | zero => simp [h0]
  | succ n ih =>
    rw [hadd n 1, ih]
    push_cast
    ring

/-- Lemma M, the sign of a nondecreasing linear function.
`theory/REPRESENTATION.md:80`. This is the A8 step, not a conclusion of
additivity alone. -/
theorem slope_nonneg_of_nondecreasing {p : ℝ}
    (h : MonotoneOn (fun z : ℝ => p * z) (Set.Ioi 0)) : 0 ≤ p := by
  have hle : p * 1 ≤ p * 2 := h (by norm_num) (by norm_num) (by norm_num)
  linarith

/-- A cost represents a preorder when smaller cost is the preferred side. -/
def Represents {α : Type*} (C : α → ℝ) (R : α → α → Prop) : Prop :=
  ∀ x y, R x y ↔ C x ≤ C y

/-- Coordinate `i` is not essential when the preorder on the positive orthant ignores it. -/
def IndependentOf {ι : Type*} (R : (ι → ℝ) → (ι → ℝ) → Prop) (i : ι) : Prop :=
  ∀ x y, (∀ j, 0 < x j) → (∀ j, 0 < y j) → (∀ j, j ≠ i → x j = y j) → R x y ∧ R y x

/-- Lemma M, second sentence. A coordinate the preorder ignores has price 0.
Both witnesses lie in the positive orthant, and the linear form is used only
there. `theory/REPRESENTATION.md:80`. -/
theorem price_zero_of_independent {ι : Type*} [Fintype ι] [DecidableEq ι] {i : ι}
    {p : ι → ℝ} {b : ℝ} {C : (ι → ℝ) → ℝ} {R : (ι → ℝ) → (ι → ℝ) → Prop}
    (hC : ∀ z, (∀ j, 0 < z j) → C z = ∑ j, p j * z j + b) (hR : Represents C R)
    (hind : IndependentOf R i) : p i = 0 := by
  let z : ι → ℝ := fun _ => 1
  let z' : ι → ℝ := Function.update z i 2
  have hz : ∀ j, 0 < z j := by
    intro j
    simp [z]
  have hz' : ∀ j, 0 < z' j := by
    intro j
    by_cases hj : j = i
    · subst hj
      simp [z', z, Function.update_self]
    · simp [z', z, Function.update_of_ne hj]
  have hagree : ∀ j, j ≠ i → z j = z' j := by
    intro j hj
    simp [z, z', Function.update_of_ne hj]
  have hboth := hind z z' hz hz' hagree
  have hle : C z ≤ C z' := (hR z z').mp hboth.1
  have hge : C z' ≤ C z := (hR z' z).mp hboth.2
  have heq : C z = C z' := le_antisymm hle hge
  have hCz : C z = ∑ j, p j * z j + b := hC z hz
  have hCz' : C z' = ∑ j, p j * z' j + b := hC z' hz'
  have hsum : ∑ j, p j * z j = ∑ j, p j * z' j := by linarith
  have hdiff : ∑ j, p j * (z' j - z j) = 0 := by
    have hsub : ∑ j, p j * z' j - ∑ j, p j * z j = ∑ j, p j * (z' j - z j) := by
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun j _ => by ring
    linarith [hsum, hsub]
  have hstep : ∀ j, z' j - z j = if j = i then (1 : ℝ) else 0 := by
    intro j
    by_cases hj : j = i
    · subst hj
      simp only [z, z', Function.update_self, ite_true]
      norm_num
    · have hzj : z' j = z j := by
        change Function.update z i 2 j = z j
        exact Function.update_of_ne hj (2 : ℝ) z
      rw [hzj, sub_self]
      exact (ite_eq_right hj).symm
  have hp : ∑ j, p j * (z' j - z j) = p i := by
    rw [Finset.sum_eq_single i
      (fun j _ hj => by simp [hstep j, hj])
      (fun hi => (hi (Finset.mem_univ i)).elim)]
    simp [hstep]
  linarith [hdiff, hp]

end Representation
