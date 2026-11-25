/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Path-Pinsker bound for the finite-state learning rate, from
`theory/GENERAL_FLOOR_FINITE_2026-11-23.md:26, 117-129`. OPEN_WORK LEAN-PHYS (T60).
-/
module

public import GTAO.FiniteFloorBounds
public import GTAO.FiniteFloorPairwise
public import Mathlib.Analysis.Calculus.Deriv.MeanValue
public import Mathlib.Analysis.SpecialFunctions.Log.Deriv
public import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.GCongr

/-!
# Path-Pinsker bound

`theory/GENERAL_FLOOR_FINITE_2026-11-23.md` §4. Pinsker's inequality in
nats, `D ≥ 2 TV²`, is proved from the binary case and the log-sum
inequality. Total variation along a walk is at most the sum over its
edges. At a mode `x*`, `ε_0 - ε ≤ Σ_x π(x) TV(p_x, p_{x*})`. Collecting
the walk coefficients and applying Cauchy–Schwarz against the fluxes gives
`(ε_0 - ε)² ≤ K_X I_alt`. The walks are a hypothesis (a `PathSystem`); on
a strongly connected occupied flux graph one exists.
-/

@[expose] public section

set_option linter.unusedSectionVars false

namespace FiniteFloor

open HeatFloor InformationTheory
open scoped BigOperators ENNReal

/-! ### Binary Pinsker -/

/-- Binary divergence `a log(a/b) + (1-a) log((1-a)/(1-b))`. -/
noncomputable def binKl (a b : ℝ) : ℝ :=
  a * Real.log (a / b) + (1 - a) * Real.log ((1 - a) / (1 - b))

/-- `logit t - 4 t`. -/
noncomputable def logitGap (t : ℝ) : ℝ :=
  -Real.log ((1 - t) / t) - 4 * t

lemma logitGap_mono : MonotoneOn logitGap (Set.Ioo (0 : ℝ) 1) := by
  refine monotoneOn_of_hasDerivWithinAt_nonneg (f' := fun x => (x * (1 - x))⁻¹ - 4)
    (convex_Ioo 0 1) ?_ ?_ ?_
  · intro x hx
    exact ((hasDerivAt_log_ratio hx.1 hx.2).neg.sub
      ((hasDerivAt_id x).const_mul 4)).continuousAt.continuousWithinAt
  · intro x hx
    rw [interior_Ioo] at hx
    have h := (hasDerivAt_log_ratio hx.1 hx.2).neg.sub ((hasDerivAt_id x).const_mul 4)
    have h' : HasDerivAt logitGap ((x * (1 - x))⁻¹ - 4) x := by
      convert h using 1
      · funext t; simp [logitGap]
      · ring
    exact h'.hasDerivWithinAt
  · intro x hx
    rw [interior_Ioo] at hx
    have h0 := hx.1
    have h1 := hx.2
    have hden : 0 < x * (1 - x) := mul_pos h0 (by linarith)
    have hq : x * (1 - x) ≤ 1 / 4 := by nlinarith [sq_nonneg (x - 1 / 2)]
    have : 4 ≤ (x * (1 - x))⁻¹ := by
      rw [le_inv_comm₀ (by norm_num) hden]
      linarith
    linarith

/-- The function `a ↦ binKl a b - 2 (a-b)²`, written with `negMulLog`. -/
noncomputable def pinskerGap (b a : ℝ) : ℝ :=
  -binaryEntropy a - a * Real.log b - (1 - a) * Real.log (1 - b) - 2 * (a - b) ^ 2

lemma binKl_eq_gap {a b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) :
    binKl a b - 2 * (a - b) ^ 2 = pinskerGap b a := by
  unfold binKl pinskerGap binaryEntropy
  have h1 : a * Real.log (a / b) = a * Real.log a - a * Real.log b := by
    by_cases ha : a = 0
    · simp [ha]
    · rw [Real.log_div ha hb0.ne']; ring
  have h2 : (1 - a) * Real.log ((1 - a) / (1 - b)) =
      (1 - a) * Real.log (1 - a) - (1 - a) * Real.log (1 - b) := by
    by_cases ha : 1 - a = 0
    · simp [ha]
    · rw [Real.log_div ha (by linarith)]; ring
  rw [h1, h2]
  ring

lemma continuous_pinskerGap (b : ℝ) : Continuous (pinskerGap b) := by
  unfold pinskerGap binaryEntropy
  have h1 : Continuous fun t : ℝ => t * Real.log t := Real.continuous_mul_log
  have h2 : Continuous fun t : ℝ => (1 - t) * Real.log (1 - t) :=
    h1.comp (continuous_const.sub continuous_id)
  have : (fun a => -(-a * Real.log a - (1 - a) * Real.log (1 - a)) - a * Real.log b -
      (1 - a) * Real.log (1 - b) - 2 * (a - b) ^ 2) =
      fun a => a * Real.log a + (1 - a) * Real.log (1 - a) - a * Real.log b -
        (1 - a) * Real.log (1 - b) - 2 * (a - b) ^ 2 := by
    funext a; ring
  rw [this]
  fun_prop

lemma hasDerivAt_pinskerGap {a b : ℝ} (ha0 : 0 < a) (ha1 : a < 1) (hb0 : 0 < b) (hb1 : b < 1) :
    HasDerivAt (pinskerGap b) (logitGap a - logitGap b) a := by
  have hH := (hasDerivAt_binaryEntropy ha0 ha1).neg
  have hlin1 := (hasDerivAt_id a).mul_const (Real.log b)
  have hlin2 := (hasDerivAt_one_sub a).mul_const (Real.log (1 - b))
  have hsq : HasDerivAt (fun t => 2 * (t - b) ^ 2) (2 * (2 * (a - b))) a := by
    have := ((hasDerivAt_id a).sub_const b).pow 2
    convert this.const_mul 2 using 1
    all_goals simp [id]
  have h := ((hH.sub hlin1).sub hlin2).sub hsq
  have hfun : pinskerGap b = fun t =>
      -binaryEntropy t - id t * Real.log b - (1 - t) * Real.log (1 - b) - 2 * (t - b) ^ 2 := by
    funext t; rfl
  rw [hfun]
  convert h using 1
  unfold logitGap
  rw [Real.log_div (by linarith : (1 - b) ≠ 0) hb0.ne']
  simp
  ring

/-- Pinsker's inequality for one binary cell, in nats. -/
theorem binary_pinsker {a b : ℝ} (ha0 : 0 ≤ a) (ha1 : a ≤ 1) (hb0 : 0 < b) (hb1 : b < 1) :
    2 * (a - b) ^ 2 ≤ binKl a b := by
  have hgap0 : pinskerGap b b = 0 := by
    unfold pinskerGap binaryEntropy; ring
  suffices h : 0 ≤ pinskerGap b a by
    have := binKl_eq_gap (a := a) hb0 hb1; linarith
  rcases le_total b a with hba | hab
  · -- `a ∈ [b, 1]`: the gap is nondecreasing
    have hmono : MonotoneOn (pinskerGap b) (Set.Icc b 1) := by
      refine monotoneOn_of_hasDerivWithinAt_nonneg
        (f' := fun x => logitGap x - logitGap b) (convex_Icc b 1)
        (continuous_pinskerGap b).continuousOn ?_ ?_
      · intro x hx
        rw [interior_Icc] at hx
        exact (hasDerivAt_pinskerGap (by linarith [hx.1]) hx.2 hb0 hb1).hasDerivWithinAt
      · intro x hx
        rw [interior_Icc] at hx
        have := logitGap_mono ⟨hb0, hb1⟩ ⟨by linarith [hx.1], hx.2⟩ hx.1.le
        linarith
    have := hmono ⟨le_rfl, hb1.le⟩ ⟨hba, ha1⟩ hba
    linarith
  · -- `a ∈ [0, b]`: the gap is nonincreasing
    have hanti : AntitoneOn (pinskerGap b) (Set.Icc 0 b) := by
      refine antitoneOn_of_hasDerivWithinAt_nonpos
        (f' := fun x => logitGap x - logitGap b) (convex_Icc 0 b)
        (continuous_pinskerGap b).continuousOn ?_ ?_
      · intro x hx
        rw [interior_Icc] at hx
        exact (hasDerivAt_pinskerGap hx.1 (by linarith [hx.2]) hb0 hb1).hasDerivWithinAt
      · intro x hx
        rw [interior_Icc] at hx
        have := logitGap_mono ⟨hx.1, by linarith [hx.2]⟩ ⟨hb0, hb1⟩ hx.2.le
        linarith
    have := hanti ⟨ha0, hab⟩ ⟨hb0.le, le_rfl⟩ hab
    linarith

/-! ### Pinsker on a finite alphabet -/

section Divergence

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- `p log(p/Q') ≥ p log(p/Q)` when `0 < Q' ≤ Q` and `p ≥ 0`. -/
lemma mul_log_div_anti {P Q Q' : ℝ} (hP : 0 ≤ P) (hQ' : 0 < Q') (hle : Q' ≤ Q) :
    P * Real.log (P / Q) ≤ P * Real.log (P / Q') := by
  rcases eq_or_lt_of_le hP with h | h
  · simp [← h]
  · apply mul_le_mul_of_nonneg_left _ hP
    apply Real.log_le_log (div_pos h (lt_of_lt_of_le hQ' hle))
    exact div_le_div_of_nonneg_left hP hQ' hle

/-- Pinsker's inequality in nats: `2 TV(p,q)² ≤ D(p‖q)` for probability
vectors with `p ≪ q`. Line 117. -/
theorem pinsker {p q : α → ℝ} (hp : Prob p) (hq : Prob q) (hac : AC p q) :
    2 * totalVariation p q ^ 2 ≤ klSum p q := by
  classical
  rw [klSum_eq_sum_log_of_ac hp hq hac]
  set S := Finset.univ.filter (fun a => 0 < p a) with hS
  have hpS : ∀ a ∈ S, 0 < p a := fun a ha => (Finset.mem_filter.mp ha).2
  have hqS : ∀ a ∈ S, 0 < q a := fun a ha => hac a (hpS a ha).ne'
  have hp0 : ∀ a, a ∉ S → p a = 0 := by
    intro a ha
    have : ¬ 0 < p a := fun h => ha (Finset.mem_filter.mpr ⟨Finset.mem_univ a, h⟩)
    exact le_antisymm (not_lt.mp this) (hp.1 a)
  set A := S.filter (fun a => q a ≤ p a)
  set B := S.filter (fun a => ¬ q a ≤ p a)
  have hAS : A ⊆ S := Finset.filter_subset _ _
  have hBS : B ⊆ S := Finset.filter_subset _ _
  have hsplitS : ∀ f : α → ℝ, ∑ a ∈ S, f a = ∑ a ∈ A, f a + ∑ a ∈ B, f a := fun f =>
    (Finset.sum_filter_add_sum_filter_not S _ f).symm
  have hsplitU : ∀ f : α → ℝ, ∑ a, f a = ∑ a ∈ S, f a + ∑ a ∈ Finset.univ \ S, f a := by
    intro f
    rw [← Finset.sum_sdiff (Finset.subset_univ S)]; ring
  set P := ∑ a ∈ A, p a
  set Q := ∑ a ∈ A, q a
  set P' := ∑ a ∈ B, p a
  set Q' := ∑ a ∈ B, q a
  set Qn := ∑ a ∈ Finset.univ \ S, q a
  have hPsum : P + P' = 1 := by
    have h := hsplitU p
    rw [hsplitS, hp.2] at h
    have : ∑ a ∈ Finset.univ \ S, p a = 0 :=
      Finset.sum_eq_zero fun a ha => hp0 a (Finset.mem_sdiff.mp ha).2
    linarith
  have hQsum : Q + Q' + Qn = 1 := by
    have h := hsplitU q
    rw [hsplitS, hq.2] at h
    linarith
  have hQn : 0 ≤ Qn := Finset.sum_nonneg fun a _ => hq.1 a
  -- total variation on the split
  have hTV : totalVariation p q = P - Q := by
    unfold totalVariation
    have h := hsplitU (fun a => |p a - q a|)
    rw [hsplitS] at h
    have hA : ∑ a ∈ A, |p a - q a| = P - Q := by
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun a ha =>
        abs_of_nonneg (sub_nonneg.mpr (Finset.mem_filter.mp ha).2)
    have hB : ∑ a ∈ B, |p a - q a| = Q' - P' := by
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun a ha => by
        rw [abs_of_neg (sub_neg.mpr (not_le.mp (Finset.mem_filter.mp ha).2))]; ring
    have hN : ∑ a ∈ Finset.univ \ S, |p a - q a| = Qn := by
      exact Finset.sum_congr rfl fun a ha => by
        rw [hp0 a (Finset.mem_sdiff.mp ha).2, zero_sub, abs_neg, abs_of_nonneg (hq.1 a)]
    rw [h, hA, hB, hN]
    linarith
  -- the divergence on the split
  have hD : ∑ a, p a * Real.log (p a / q a) =
      ∑ a ∈ A, p a * Real.log (p a / q a) + ∑ a ∈ B, p a * Real.log (p a / q a) := by
    rw [hsplitU, hsplitS]
    have : ∑ a ∈ Finset.univ \ S, p a * Real.log (p a / q a) = 0 :=
      Finset.sum_eq_zero fun a ha => by simp [hp0 a (Finset.mem_sdiff.mp ha).2]
    rw [this, add_zero]
  have hlA := log_sum_le A (fun a ha => hpS a (hAS ha)) (fun a ha => hqS a (hAS ha))
  have hlB := log_sum_le B (fun a ha => hpS a (hBS ha)) (fun a ha => hqS a (hBS ha))
  have hlA' : P * Real.log (P / Q) ≤ ∑ a ∈ A, p a * Real.log (p a / q a) := hlA
  have hlB' : P' * Real.log (P' / Q') ≤ ∑ a ∈ B, p a * Real.log (p a / q a) := hlB
  have hPQ : Q ≤ P := Finset.sum_le_sum fun a ha => (Finset.mem_filter.mp ha).2
  have hP'nn : 0 ≤ P' := Finset.sum_nonneg fun a ha => (hpS a (hBS ha)).le
  have hQnn : 0 ≤ Q := Finset.sum_nonneg fun a ha => (hqS a (hAS ha)).le
  have hQ'nn : 0 ≤ Q' := Finset.sum_nonneg fun a ha => (hqS a (hBS ha)).le
  have hk0 : 0 ≤ ∑ a, p a * Real.log (p a / q a) := by
    rw [← klSum_eq_sum_log_of_ac hp hq hac]
    exact klSum_nonneg hp.1 hq.1
  rw [hTV]
  rcases eq_or_lt_of_le hPQ with heq | hlt
  · rw [heq, sub_self]; simpa using hk0
  have hPpos : 0 < P := lt_of_le_of_lt hQnn hlt
  have hAne : A.Nonempty := by
    by_contra hA
    rw [Finset.not_nonempty_iff_eq_empty] at hA
    have : P = 0 := by simp [P, hA]
    linarith
  have hQpos : 0 < Q := Finset.sum_pos (fun a ha => hqS a (hAS ha)) hAne
  have hQ1 : Q < 1 := by linarith
  have hBpart : P' * Real.log (P' / (1 - Q)) ≤ ∑ a ∈ B, p a * Real.log (p a / q a) := by
    rcases eq_or_lt_of_le hP'nn with h0 | h0
    · rw [← h0, zero_mul]
      rw [← h0, zero_mul] at hlB'
      exact hlB'
    · have hBne : B.Nonempty := by
        by_contra hB
        rw [Finset.not_nonempty_iff_eq_empty] at hB
        have : P' = 0 := by simp [P', hB]
        linarith
      have hQ'pos : 0 < Q' := Finset.sum_pos (fun a ha => hqS a (hBS ha)) hBne
      exact le_trans (mul_log_div_anti hP'nn hQ'pos (by linarith)) hlB'
  have hbin := binary_pinsker hPpos.le (by linarith) hQpos hQ1
  have hP' : 1 - P = P' := by linarith
  unfold binKl at hbin
  rw [hP'] at hbin
  rw [hD]
  linarith

end Divergence

/-! ### Total variation along a walk -/

section Walk

variable {α : Type*} [Fintype α]

lemma totalVariation_self (p : α → ℝ) : totalVariation p p = 0 := by
  simp [totalVariation]

lemma totalVariation_triangle (p q r : α → ℝ) :
    totalVariation p r ≤ totalVariation p q + totalVariation q r := by
  unfold totalVariation
  rw [← mul_add, ← Finset.sum_add_distrib]
  apply mul_le_mul_of_nonneg_left _ (by norm_num)
  exact Finset.sum_le_sum fun a _ => abs_sub_le (p a) (q a) (r a)

/-- `TV(p,q) = ∑ (p - q)⁺` for probability vectors. -/
lemma totalVariation_eq_sum_pos {p q : α → ℝ} (hp : Prob p) (hq : Prob q) :
    totalVariation p q = ∑ a, max (p a - q a) 0 := by
  unfold totalVariation
  have h : ∀ a, |p a - q a| = 2 * max (p a - q a) 0 - (p a - q a) := by
    intro a
    rcases le_total 0 (p a - q a) with h | h
    · rw [abs_of_nonneg h, max_eq_left h]; ring
    · rw [abs_of_nonpos h, max_eq_right h]; ring
  simp_rw [h, Finset.sum_sub_distrib, ← Finset.mul_sum, hp.2, hq.2]
  ring

end Walk

variable {X M : Type*} [Fintype X] [DecidableEq X] [Fintype M] [DecidableEq M]

/-- Edges of the walk that starts at `u` and visits the listed states. -/
def walkEdges : X → List X → List (X × X)
  | _, [] => []
  | u, v :: l => (u, v) :: walkEdges v l

/-- Last state of that walk. -/
def walkEnd : X → List X → X
  | u, [] => u
  | _, v :: l => walkEnd v l

/-- Triangle inequality along a walk. Line 117. -/
lemma tv_walk_le (p : X → M → ℝ) (x : X) (l : List X) :
    totalVariation (p x) (p (walkEnd x l)) ≤
      ((walkEdges x l).map fun e => totalVariation (p e.1) (p e.2)).sum := by
  induction l generalizing x with
  | nil => simp [walkEnd, walkEdges, totalVariation_self]
  | cons v l ih =>
    simp only [walkEnd, walkEdges, List.map_cons, List.sum_cons]
    exact le_trans (totalVariation_triangle _ (p v) _) (by linarith [ih v])

/-- A list sum as a sum over the alphabet weighted by multiplicities. -/
lemma list_sum_eq_count {β : Type*} [Fintype β] [DecidableEq β] (l : List β) (f : β → ℝ) :
    (l.map f).sum = ∑ e, (l.count e : ℝ) * f e := by
  induction l with
  | nil => simp
  | cons a l ih =>
    simp only [List.map_cons, List.sum_cons, ih, List.count_cons]
    have : ∑ e, ((List.count e l + if (a == e) = true then 1 else 0 : ℕ) : ℝ) * f e =
        ∑ e, (List.count e l : ℝ) * f e + ∑ e, (if a = e then f e else 0) := by
      rw [← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun e _ => ?_
      by_cases h : a = e
      · simp [h]; ring
      · simp [h]
    rw [this, Finset.sum_ite_eq]
    simp
    ring

/-! ### Bayes error against chance -/

lemma joint_sum [Nonempty X] {π : X → ℝ} (hπsum : ∑ x, π x = 1) {p : X → M → ℝ}
    (hp : ∀ x, Prob (p x)) : ∑ x, ∑ m, π x * p x m = 1 := by
  simp_rw [← Finset.mul_sum, (hp _).2, mul_one, hπsum]

/-- `ε ≤ ε_0`. -/
theorem bayes_le_chance [Nonempty X] {π : X → ℝ} {p : X → M → ℝ}
    (_hπ : ∀ x, 0 ≤ π x) (hp : ∀ x, Prob (p x)) :
    bayesError (fun x m => π x * p x m) ≤ chanceError π := by
  unfold bayesError chanceError
  obtain ⟨x0, _, hx0⟩ := Finset.exists_mem_eq_sup' (s := Finset.univ) Finset.univ_nonempty π
  rw [hx0]
  have : π x0 = ∑ m, π x0 * p x0 m := by rw [← Finset.mul_sum, (hp x0).2, mul_one]
  have hle : ∑ m, π x0 * p x0 m ≤
      ∑ m, Finset.univ.sup' Finset.univ_nonempty (fun x => π x * p x m) :=
    Finset.sum_le_sum fun m _ => le_sup'_univ (fun x => π x * p x m)
  linarith

/-- At a mode `x*`, `ε_0 - ε ≤ Σ_x π(x) TV(p_x, p_{x*})`. Lines 119-121. -/
theorem chance_sub_bayes_le [Nonempty X] {π : X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hp : ∀ x, Prob (p x)) {xs : X} (hmode : ∀ x, π x ≤ π xs) :
    chanceError π - bayesError (fun x m => π x * p x m) ≤
      ∑ x, π x * totalVariation (p x) (p xs) := by
  unfold bayesError chanceError
  have hsup : Finset.univ.sup' Finset.univ_nonempty π = π xs :=
    le_antisymm (Finset.sup'_le _ _ fun x _ => hmode x) (le_sup'_univ π)
  rw [hsup]
  have hm : ∀ m, Finset.univ.sup' Finset.univ_nonempty (fun x => π x * p x m) ≤
      π xs * p xs m + ∑ x, π x * max (p x m - p xs m) 0 := by
    intro m
    obtain ⟨x0, _, hx0⟩ := Finset.exists_mem_eq_sup' (s := Finset.univ) Finset.univ_nonempty
      (fun x => π x * p x m)
    rw [hx0]
    have hnn : ∀ x ∈ Finset.univ, 0 ≤ π x * max (p x m - p xs m) 0 :=
      fun x _ => mul_nonneg (hπ x) (le_max_right _ _)
    have hone := Finset.single_le_sum hnn (Finset.mem_univ x0)
    have h1 : π x0 * p x0 m ≤ π x0 * p xs m + π x0 * max (p x0 m - p xs m) 0 := by
      rw [← mul_add]
      exact mul_le_mul_of_nonneg_left (by linarith [le_max_left (p x0 m - p xs m) 0]) (hπ x0)
    have h2 : π x0 * p xs m ≤ π xs * p xs m :=
      mul_le_mul_of_nonneg_right (hmode x0) ((hp xs).1 m)
    linarith
  have htot := Finset.sum_le_sum fun m (_ : m ∈ Finset.univ) => hm m
  rw [Finset.sum_add_distrib, ← Finset.mul_sum, (hp xs).2, mul_one, Finset.sum_comm] at htot
  have hTV : ∀ x, π x * totalVariation (p x) (p xs) = ∑ m, π x * max (p x m - p xs m) 0 := by
    intro x
    rw [totalVariation_eq_sum_pos (hp x) (hp xs), Finset.mul_sum]
  simp_rw [hTV]
  linarith

/-! ### Path systems and the constant `K_X` -/

/-- A system of walks of positive-flux edges, one from each occupied state
to a target. Line 117. -/
structure PathSystem (π : X → ℝ) (W : X → X → ℝ) where
  target : X
  path : X → List X
  ends : ∀ x, 0 < π x → walkEnd x (path x) = target
  pos : ∀ x, 0 < π x → ∀ e ∈ walkEdges x (path x), 0 < flux π W e.1 e.2

/-- `Σ_x π(x) · #uses of e`, over occupied states. `c_e = pathWeight/√2`. -/
noncomputable def pathWeight {π : X → ℝ} {W : X → X → ℝ} (P : PathSystem π W) (e : X × X) : ℝ :=
  ∑ x, if 0 < π x then π x * ((walkEdges x (P.path x)).count e : ℝ) else 0

/-- `K_X = Σ_e c_e² / j_e = Σ_e pathWeight² / (2 j_e)` over positive-flux edges. Line 127. -/
noncomputable def pathK {π : X → ℝ} {W : X → X → ℝ} (P : PathSystem π W) : ℝ :=
  ∑ e : X × X, if 0 < flux π W e.1 e.2 then pathWeight P e ^ 2 / (2 * flux π W e.1 e.2) else 0

lemma pathWeight_nonneg {π : X → ℝ} {W : X → X → ℝ} (P : PathSystem π W) (e : X × X) :
    0 ≤ pathWeight P e := by
  unfold pathWeight
  refine Finset.sum_nonneg fun x _ => ?_
  split_ifs with h
  · exact mul_nonneg h.le (Nat.cast_nonneg _)
  · exact le_rfl

lemma flux_pos_of_weight {π : X → ℝ} {W : X → X → ℝ} (P : PathSystem π W) {e : X × X}
    (hw : 0 < pathWeight P e) : 0 < flux π W e.1 e.2 := by
  by_contra hneg
  have hzero : pathWeight P e = 0 := by
    unfold pathWeight
    refine Finset.sum_eq_zero fun x _ => ?_
    split_ifs with h
    · have hc : (walkEdges x (P.path x)).count e = 0 := by
        rw [List.count_eq_zero]
        intro he
        exact hneg (P.pos x h e he)
      simp [hc]
    · rfl
  linarith

/-- `ε_0 - ε ≤ Σ_e pathWeight(e) TV_e`. -/
lemma chance_sub_bayes_le_weights [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hp : ∀ x, Prob (p x)) (P : PathSystem π W)
    (hmode : ∀ x, π x ≤ π P.target) :
    chanceError π - bayesError (fun x m => π x * p x m) ≤
      ∑ e : X × X, pathWeight P e * totalVariation (p e.1) (p e.2) := by
  refine le_trans (chance_sub_bayes_le hπ hp hmode) ?_
  have hx : ∀ x, π x * totalVariation (p x) (p P.target) ≤
      if 0 < π x then π x * ∑ e : X × X, ((walkEdges x (P.path x)).count e : ℝ) *
        totalVariation (p e.1) (p e.2) else 0 := by
    intro x
    split_ifs with h
    · have hw := tv_walk_le p x (P.path x)
      rw [P.ends x h, list_sum_eq_count] at hw
      exact mul_le_mul_of_nonneg_left hw h.le
    · have : π x = 0 := le_antisymm (not_lt.mp h) (hπ x)
      simp [this]
  refine le_trans (Finset.sum_le_sum fun x _ => hx x) (le_of_eq ?_)
  unfold pathWeight
  simp_rw [Finset.sum_mul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun x _ => ?_
  split_ifs <;> simp [Finset.mul_sum, mul_assoc]

/-- The squared Path-Pinsker bound on the edges a path system uses. -/
lemma path_pinsker_edges [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hp : ∀ x, Prob (p x)) (P : PathSystem π W)
    (hmode : ∀ x, π x ≤ π P.target)
    (hac : ∀ e : X × X, 0 < pathWeight P e → AC (p e.1) (p e.2)) :
    (chanceError π - bayesError (fun x m => π x * p x m)) ^ 2 ≤
      pathK P * ∑ e ∈ Finset.univ.filter (fun e => 0 < pathWeight P e),
        flux π W e.1 e.2 * klSum (p e.1) (p e.2) := by
  classical
  set E := Finset.univ.filter (fun e : X × X => 0 < pathWeight P e)
  have hlow := chance_sub_bayes_le_weights hπ hp P hmode (W := W)
  have hdiff : 0 ≤ chanceError π - bayesError (fun x m => π x * p x m) :=
    sub_nonneg.mpr (bayes_le_chance hπ hp)
  -- restrict to the used edges
  have hrestrict : ∑ e : X × X, pathWeight P e * totalVariation (p e.1) (p e.2) =
      ∑ e ∈ E, pathWeight P e * totalVariation (p e.1) (p e.2) := by
    rw [Finset.sum_filter]
    refine Finset.sum_congr rfl fun e _ => ?_
    split_ifs with h
    · rfl
    · have : pathWeight P e = 0 := le_antisymm (not_lt.mp h) (pathWeight_nonneg P e)
      simp [this]
  have hK : pathK P = ∑ e ∈ E, pathWeight P e ^ 2 / (2 * flux π W e.1 e.2) := by
    unfold pathK
    rw [Finset.sum_filter]
    refine Finset.sum_congr rfl fun e _ => ?_
    by_cases hw : 0 < pathWeight P e
    · simp [hw, flux_pos_of_weight P hw]
    · have : pathWeight P e = 0 := le_antisymm (not_lt.mp hw) (pathWeight_nonneg P e)
      simp [this]
  -- Cauchy–Schwarz with Pinsker on each used edge
  have hCS : (∑ e ∈ E, pathWeight P e * totalVariation (p e.1) (p e.2)) ^ 2 ≤
      (∑ e ∈ E, pathWeight P e ^ 2 / (2 * flux π W e.1 e.2)) *
        ∑ e ∈ E, flux π W e.1 e.2 * klSum (p e.1) (p e.2) := by
    apply Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul
    · intro e he
      have hw := (Finset.mem_filter.mp he).2
      have hf := flux_pos_of_weight P hw
      positivity
    · intro e he
      have hw := (Finset.mem_filter.mp he).2
      exact mul_nonneg (flux_pos_of_weight P hw).le (klSum_nonneg (hp _).1 (hp _).1)
    · intro e he
      have hw := (Finset.mem_filter.mp he).2
      have hf := flux_pos_of_weight P hw
      have hpin := pinsker (hp e.1) (hp e.2) (hac e hw)
      have heq : pathWeight P e ^ 2 / (2 * flux π W e.1 e.2) *
          (flux π W e.1 e.2 * klSum (p e.1) (p e.2)) =
          pathWeight P e ^ 2 * (klSum (p e.1) (p e.2) / 2) := by
        field_simp
      rw [heq, mul_pow]
      exact mul_le_mul_of_nonneg_left (by linarith) (sq_nonneg _)
  rw [hK]
  refine le_trans ?_ hCS
  rw [← hrestrict]
  exact pow_le_pow_left₀ hdiff hlow 2

/-- Path-Pinsker bound. With every used edge carrying an absolutely
continuous pair, `(ε_0 - ε)² ≤ K_X · I_alt`. Lines 26 and 127. -/
theorem path_pinsker [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (P : PathSystem π W) (hmode : ∀ x, π x ≤ π P.target)
    (hac : ∀ e : X × X, 0 < pathWeight P e → AC (p e.1) (p e.2)) :
    (chanceError π - bayesError (fun x m => π x * p x m)) ^ 2 ≤ pathK P * iAltReal π W p := by
  have h := path_pinsker_edges hπ hp P hmode hac
  have hKnn : 0 ≤ pathK P := by
    unfold pathK
    refine Finset.sum_nonneg fun e _ => ?_
    split_ifs with hf
    · positivity
    · exact le_rfl
  exact le_trans h (mul_le_mul_of_nonneg_left (edges_le_iAltReal hπ hW hp _) hKnn)

/-- Path-Pinsker on the extended learning rate, `I_alt ≥ (ε_0 - ε)² / K_X`,
with no absolute-continuity hypothesis. Lines 26 and 127. -/
theorem path_pinsker_ennreal [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (P : PathSystem π W) (hmode : ∀ x, π x ≤ π P.target) :
    ENNReal.ofReal ((chanceError π - bayesError (fun x m => π x * p x m)) ^ 2 / pathK P) ≤
      iAlt π W p := by
  classical
  refine ofReal_edges_le_iAlt hπ hW hp (Finset.univ.filter (fun e => 0 < pathWeight P e))
    (fun e he => flux_pos_of_weight P (Finset.mem_filter.mp he).2) ?_
  intro hac
  have h := path_pinsker_edges hπ hp P hmode
    (fun e hw => hac e (Finset.mem_filter.mpr ⟨Finset.mem_univ e, hw⟩))
  have hS : 0 ≤ ∑ e ∈ Finset.univ.filter (fun e => 0 < pathWeight P e),
      flux π W e.1 e.2 * klSum (p e.1) (p e.2) :=
    Finset.sum_nonneg fun e _ => mul_nonneg (flux_nonneg hπ hW _ _)
      (klSum_nonneg (hp _).1 (hp _).1)
  have hKnn : 0 ≤ pathK P := by
    unfold pathK
    refine Finset.sum_nonneg fun e _ => ?_
    split_ifs with hf
    · positivity
    · exact le_rfl
  rcases eq_or_lt_of_le hKnn with hK0 | hKpos
  · rw [← hK0, div_zero]; exact hS
  · rw [div_le_iff₀ hKpos, mul_comm]; exact h

/-! ### Existence on a strongly connected graph -/

lemma walk_of_reach {π : X → ℝ} {W : X → X → ℝ} {x z : X} (h : Reach π W x z) :
    ∃ l : List X, walkEnd x l = z ∧ ∀ e ∈ walkEdges x l, 0 < flux π W e.1 e.2 := by
  induction h with
  | refl x => exact ⟨[], rfl, by simp [walkEdges]⟩
  | @tail x y z hxy _ ih =>
    obtain ⟨l, hl, hpos⟩ := ih
    refine ⟨y :: l, hl, ?_⟩
    intro e he
    simp only [walkEdges, List.mem_cons] at he
    rcases he with rfl | he
    · exact hxy
    · exact hpos e he

/-- On a strongly connected occupied flux graph, a path system to any
occupied target exists. Line 117. -/
theorem pathSystem_exists {π : X → ℝ} {W : X → X → ℝ} (hsc : stronglyConnected π W)
    {xs : X} (hxs : 0 < π xs) : ∃ P : PathSystem π W, P.target = xs := by
  classical
  have hwalk : ∀ x, 0 < π x → ∃ l : List X, walkEnd x l = xs ∧
      ∀ e ∈ walkEdges x l, 0 < flux π W e.1 e.2 :=
    fun x hx => walk_of_reach (hsc x xs hx hxs)
  refine ⟨{ target := xs
            path := fun x => if h : 0 < π x then Classical.choose (hwalk x h) else []
            ends := ?_
            pos := ?_ }, rfl⟩
  · intro x hx
    simp only [hx, dite_true]
    exact (Classical.choose_spec (hwalk x hx)).1
  · intro x hx
    simp only [hx, dite_true]
    exact (Classical.choose_spec (hwalk x hx)).2

/-- Path-Pinsker as the note states it: on a strongly connected occupied
flux graph, at an occupied mode `x*`, some path system to `x*` gives
`I_alt ≥ (ε_0 - ε)² / K_X`. Lines 26 and 117-127. -/
theorem path_pinsker_stronglyConnected [Nonempty X] {π : X → ℝ} {W : X → X → ℝ}
    {p : X → M → ℝ} (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (hsc : stronglyConnected π W) {xs : X} (hxs : 0 < π xs) (hmode : ∀ x, π x ≤ π xs) :
    ∃ P : PathSystem π W, P.target = xs ∧
      ENNReal.ofReal ((chanceError π - bayesError (fun x m => π x * p x m)) ^ 2 / pathK P) ≤
        iAlt π W p := by
  obtain ⟨P, hP⟩ := pathSystem_exists hsc hxs
  exact ⟨P, hP, path_pinsker_ennreal hπ hW hp P (hP ▸ hmode)⟩

/-! ### The fair telegraph -/

/-- The path system of the fair telegraph: state `1` steps to the mode `0`. -/
noncomputable def telegraphPaths {r : ℝ} (hr : 0 < r) : PathSystem telegraphπ (telegraphW r) where
  target := 0
  path := fun x => if x = 1 then [0] else []
  ends := by
    intro x _
    fin_cases x <;> simp [walkEnd]
  pos := by
    intro x _ e he
    fin_cases x
    · simp [walkEdges] at he
    · simp [walkEdges] at he
      subst he
      simp [flux, telegraphπ, telegraphW]
      positivity

/-- On the fair telegraph, `K_X = 1/(4r)`. Line 129. -/
theorem telegraph_K {r : ℝ} (hr : 0 < r) : pathK (telegraphPaths hr) = 1 / (4 * r) := by
  unfold pathK pathWeight
  rw [Fintype.sum_prod_type]
  simp [Fin.sum_univ_two, telegraphPaths, walkEdges, flux, telegraphπ, telegraphW, hr]
  field_simp
  ring

end FiniteFloor
