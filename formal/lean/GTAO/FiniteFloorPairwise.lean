/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Pairwise `L` bound for the finite-state learning rate, from
`theory/GENERAL_FLOOR_FINITE_2026-11-23.md:27, 113-115`. OPEN_WORK LEAN-PHYS (T60).
-/
module

public import GTAO.FiniteFloor
public import Mathlib.Algebra.Order.BigOperators.Ring.Finset
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.GCongr

/-!
# Pairwise `L` bound

`theory/GENERAL_FLOOR_FINITE_2026-11-23.md` §4. Lumping two conditionals
onto the set where the first is at least the second does not raise their
Jeffreys divergence (the log-sum inequality), and on that binary pair the
Jeffreys divergence at fixed overlap is at least `2 L(overlap / 2)`. Every
non-top joint mass is part of the Bayes error, so the overlap of a pair is
at most `ε / min(π(i), π(j))`. The two directed fluxes of the pair then
give the pairwise bound.
-/

@[expose] public section

set_option linter.unusedSectionVars false

namespace FiniteFloor

open HeatFloor InformationTheory
open scoped BigOperators ENNReal

/-- Log-sum inequality on positive reals. -/
lemma log_sum_le {ι : Type*} (s : Finset ι) {a b : ι → ℝ} (ha : ∀ i ∈ s, 0 < a i)
    (hb : ∀ i ∈ s, 0 < b i) :
    (∑ i ∈ s, a i) * Real.log ((∑ i ∈ s, a i) / ∑ i ∈ s, b i) ≤
      ∑ i ∈ s, a i * Real.log (a i / b i) := by
  rcases s.eq_empty_or_nonempty with rfl | hne
  · simp
  set A := ∑ i ∈ s, a i with hAdef
  set B := ∑ i ∈ s, b i with hBdef
  have hA : 0 < A := Finset.sum_pos ha hne
  have hB : 0 < B := Finset.sum_pos hb hne
  have key : ∀ i ∈ s, a i * Real.log (A / B) + (a i - b i * (A / B)) ≤
      a i * Real.log (a i / b i) := by
    intro i hi
    have hai := ha i hi
    have hbi := hb i hi
    have hx : 0 < a i * B / (b i * A) := by positivity
    have h1 := Real.one_sub_inv_le_log_of_pos hx
    have hlog : Real.log (a i * B / (b i * A)) = Real.log (a i / b i) - Real.log (A / B) := by
      rw [← Real.log_div (by positivity) (by positivity)]
      congr 1
      field_simp
    have hinv : a i * (1 - (a i * B / (b i * A))⁻¹) = a i - b i * (A / B) := by
      field_simp
    have h2 : a i * (1 - (a i * B / (b i * A))⁻¹) ≤ a i * Real.log (a i * B / (b i * A)) :=
      mul_le_mul_of_nonneg_left h1 hai.le
    rw [hinv, hlog] at h2
    linarith
  have hsum := Finset.sum_le_sum key
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.sum_mul, ← Finset.sum_mul,
    ← hAdef, ← hBdef] at hsum
  have hcancel : B * (A / B) = A := by field_simp
  rw [hcancel] at hsum
  linarith

/-- Superadditivity of the edge term `(a-b) log(a/b)` on positive reals. -/
lemma edge_superadd {ι : Type*} (s : Finset ι) {a b : ι → ℝ} (ha : ∀ i ∈ s, 0 < a i)
    (hb : ∀ i ∈ s, 0 < b i) :
    ((∑ i ∈ s, a i) - ∑ i ∈ s, b i) * Real.log ((∑ i ∈ s, a i) / ∑ i ∈ s, b i) ≤
      ∑ i ∈ s, (a i - b i) * Real.log (a i / b i) := by
  have h1 := log_sum_le s ha hb
  have h2 := log_sum_le s hb ha
  have hflip : ∀ (u v : ℝ), Real.log (v / u) = -Real.log (u / v) := by
    intro u v
    rw [← Real.log_inv, inv_div]
  rw [hflip] at h2
  have hterm : ∀ i ∈ s, (a i - b i) * Real.log (a i / b i) =
      a i * Real.log (a i / b i) + b i * Real.log (b i / a i) := by
    intro i _
    rw [hflip (a i) (b i)]
    ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib]
  linarith

/-- Overlap `∑ min(p, q)`. For a fair pair it is twice the Bayes error. -/
noncomputable def overlap {α : Type*} [Fintype α] (p q : α → ℝ) : ℝ :=
  ∑ a, min (p a) (q a)

section Divergence

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- Under `p ≪ q`, `klSum p q = ∑ p log(p/q)` with `0 log 0 = 0`. -/
lemma klSum_eq_sum_log_of_ac {p q : α → ℝ} (hp : Prob p) (hq : Prob q) (hac : AC p q) :
    klSum p q = ∑ a, p a * Real.log (p a / q a) := by
  have hterm : ∀ a, (if q a = 0 then 0 else q a * klFun (p a / q a)) =
      p a * Real.log (p a / q a) + (q a - p a) := by
    intro a
    by_cases hqa : q a = 0
    · have hpa : p a = 0 := by
        by_contra hne
        have := hac a hne
        linarith
      simp [hqa, hpa]
    · have hqpos : 0 < q a := lt_of_le_of_ne (hq.1 a) (Ne.symm hqa)
      simp only [hqa, ite_false]
      rw [klTerm_expand hqpos (hp.1 a)]
      ring
  unfold klSum
  simp_rw [hterm, Finset.sum_add_distrib, Finset.sum_sub_distrib, hp.2, hq.2]
  ring

/-- The binary Jeffreys divergence at masses `1 - a` and `b` on one cell
is at least `2 L((a+b)/2)`. Line 113, "minimized at `a = b = ε`". -/
lemma binary_jeffreys {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hab : a + b < 1) :
    2 * L ((a + b) / 2) ≤
      (1 - a - b) * (Real.log ((1 - a) / b) - Real.log (a / (1 - b))) := by
  set δ := (a + b) / 2 with hδ
  have hδ0 : 0 < δ := by rw [hδ]; positivity
  have hδ1 : δ < 1 / 2 := by linarith
  have hc : 0 < 1 - a - b := by linarith
  have h1a : 0 < 1 - a := by linarith
  have h1b : 0 < 1 - b := by linarith
  have hL : L δ = (1 - a - b) * Real.log ((1 - δ) / δ) := by
    unfold L; rw [hδ]; ring_nf
  rw [hL]
  have hlog : Real.log ((1 - a) / b) - Real.log (a / (1 - b)) =
      Real.log ((1 - a) * (1 - b) / (a * b)) := by
    rw [← Real.log_div (by positivity) (by positivity)]
    congr 1
    field_simp
  rw [hlog]
  have hsq : 2 * Real.log ((1 - δ) / δ) = Real.log (((1 - δ) / δ) ^ 2) := by
    rw [Real.log_pow]; norm_num
  have hab2 : a * b ≤ δ ^ 2 := by
    rw [hδ]; nlinarith [sq_nonneg (a - b)]
  have hmono : ((1 - δ) / δ) ^ 2 ≤ (1 - a) * (1 - b) / (a * b) := by
    rw [div_pow, div_le_div_iff₀ (by positivity) (by positivity)]
    have hexp : (1 - a) * (1 - b) = 1 - 2 * δ + a * b := by rw [hδ]; ring
    rw [hexp]
    have : 0 ≤ (1 - 2 * δ) * (δ ^ 2 - a * b) := mul_nonneg (by linarith) (by linarith)
    nlinarith
  have hlogle : Real.log (((1 - δ) / δ) ^ 2) ≤ Real.log ((1 - a) * (1 - b) / (a * b)) :=
    Real.log_le_log (pow_pos (div_pos (by linarith) hδ0) 2) hmono
  have : 2 * ((1 - a - b) * Real.log ((1 - δ) / δ)) =
      (1 - a - b) * (2 * Real.log ((1 - δ) / δ)) := by ring
  rw [this, hsq]
  exact mul_le_mul_of_nonneg_left hlogle hc.le

/-- Jeffreys divergence at fixed overlap. For mutually absolutely continuous
probability vectors, `klSum p q + klSum q p ≥ 2 L(overlap/2)`. Line 113. -/
theorem jeffreys_ge_two_L {p q : α → ℝ} (hp : Prob p) (hq : Prob q) (hpq : AC p q)
    (hqp : AC q p) :
    2 * L (overlap p q / 2) ≤ klSum p q + klSum q p := by
  classical
  -- the Jeffreys sum, term by term
  have hflip : ∀ (u v : ℝ), Real.log (v / u) = -Real.log (u / v) := by
    intro u v
    rw [← Real.log_inv, inv_div]
  have hJ : klSum p q + klSum q p = ∑ a, (p a - q a) * Real.log (p a / q a) := by
    rw [klSum_eq_sum_log_of_ac hp hq hpq, klSum_eq_sum_log_of_ac hq hp hqp,
      ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [hflip (p a) (q a)]
    ring
  -- the support, where both masses are positive
  set S := Finset.univ.filter (fun a => 0 < p a) with hS
  have hqS : ∀ a ∈ S, 0 < q a := by
    intro a ha
    have : 0 < p a := (Finset.mem_filter.mp ha).2
    exact hpq a this.ne'
  have hpS : ∀ a ∈ S, 0 < p a := fun a ha => (Finset.mem_filter.mp ha).2
  have hoff : ∀ a, a ∉ S → p a = 0 ∧ q a = 0 := by
    intro a ha
    have hpa : p a = 0 := by
      have : ¬ 0 < p a := fun h => ha (Finset.mem_filter.mpr ⟨Finset.mem_univ a, h⟩)
      exact le_antisymm (not_lt.mp this) (hp.1 a)
    refine ⟨hpa, ?_⟩
    by_contra hne
    have := hqp a hne
    linarith
  set A := S.filter (fun a => q a ≤ p a) with hAdef
  set B := S.filter (fun a => ¬ q a ≤ p a) with hBdef
  have hsplit : ∀ f : α → ℝ, (∀ a, a ∉ S → f a = 0) →
      ∑ a, f a = ∑ a ∈ A, f a + ∑ a ∈ B, f a := by
    intro f hf
    rw [Finset.sum_filter_add_sum_filter_not]
    rw [← Finset.sum_subset (Finset.subset_univ S) (fun a _ ha => hf a ha)]
  have hJS := hsplit (fun a => (p a - q a) * Real.log (p a / q a))
    (fun a ha => by simp [(hoff a ha).1, (hoff a ha).2])
  have hPsum := hsplit p (fun a ha => (hoff a ha).1)
  have hQsum := hsplit q (fun a ha => (hoff a ha).2)
  have hOsum := hsplit (fun a => min (p a) (q a))
    (fun a ha => by simp [(hoff a ha).1, (hoff a ha).2])
  rw [hp.2] at hPsum
  rw [hq.2] at hQsum
  set P := ∑ a ∈ A, p a
  set Q := ∑ a ∈ A, q a
  set P' := ∑ a ∈ B, p a
  set Q' := ∑ a ∈ B, q a
  have hminA : ∑ a ∈ A, min (p a) (q a) = Q :=
    Finset.sum_congr rfl fun a ha => min_eq_right (Finset.mem_filter.mp ha).2
  have hminB : ∑ a ∈ B, min (p a) (q a) = P' :=
    Finset.sum_congr rfl fun a ha => min_eq_left (le_of_lt (not_le.mp (Finset.mem_filter.mp ha).2))
  have hov : overlap p q = Q + P' := by
    unfold overlap; rw [hOsum, hminA, hminB]
  have hAS : A ⊆ S := Finset.filter_subset _ _
  have hBS : B ⊆ S := Finset.filter_subset _ _
  have hlA := edge_superadd A (fun a ha => hpS a (hAS ha)) (fun a ha => hqS a (hAS ha))
  have hlB := edge_superadd B (fun a ha => hpS a (hBS ha)) (fun a ha => hqS a (hBS ha))
  have hPQ : Q ≤ P := Finset.sum_le_sum fun a ha => (Finset.mem_filter.mp ha).2
  rw [hJ, hJS, hov]
  rcases eq_or_lt_of_le hPQ with heq | hlt
  · -- equal masses on `A`: the overlap is `1`, and `L(1/2) = 0`
    have hP' : P' = 1 - P := by linarith
    have hhalf : (Q + P') / 2 = 1 / 2 := by rw [hP', heq]; ring
    rw [hhalf, L_zero_at_half]
    have h0A : 0 ≤ ∑ a ∈ A, (p a - q a) * Real.log (p a / q a) := by
      apply Finset.sum_nonneg
      intro a ha
      exact edgeEntropy_nonneg (hpS a (hAS ha)) (hqS a (hAS ha))
    have h0B : 0 ≤ ∑ a ∈ B, (p a - q a) * Real.log (p a / q a) := by
      apply Finset.sum_nonneg
      intro a ha
      exact edgeEntropy_nonneg (hpS a (hBS ha)) (hqS a (hBS ha))
    linarith
  · -- strict: both cells carry mass of both vectors
    have hQpos : 0 < Q := by
      have hAne : A.Nonempty := by
        by_contra hA
        rw [Finset.not_nonempty_iff_eq_empty] at hA
        have : P = 0 := by simp [P, hA]
        have : Q = 0 := by simp [Q, hA]
        linarith
      exact Finset.sum_pos (fun a ha => hqS a (hAS ha)) hAne
    have hP'pos : 0 < P' := by
      have hBne : B.Nonempty := by
        by_contra hB
        rw [Finset.not_nonempty_iff_eq_empty] at hB
        have h1 : P' = 0 := by simp [P', hB]
        have h2 : Q' = 0 := by simp [Q', hB]
        linarith
      exact Finset.sum_pos (fun a ha => hpS a (hBS ha)) hBne
    have hsum1 : P' + Q < 1 := by linarith
    have hbin := binary_jeffreys hP'pos hQpos hsum1
    have hP : P = 1 - P' := by linarith
    have hQ' : Q' = 1 - Q := by linarith
    have hcomb : (1 - P' - Q) * (Real.log ((1 - P') / Q) - Real.log (P' / (1 - Q))) =
        (P - Q) * Real.log (P / Q) + (P' - Q') * Real.log (P' / Q') := by
      rw [hP, hQ']; ring
    have hcomm : (Q + P') / 2 = (P' + Q) / 2 := by ring
    rw [hcomm]
    linarith [hlA, hlB]

end Divergence

variable {X M : Type*} [Fintype X] [DecidableEq X] [Fintype M] [DecidableEq M]

/-- Every non-top joint mass is part of the Bayes error. For `i ≠ j`,
`∑_m min(π(i,m), π(j,m)) ≤ ε`. Line 115. -/
theorem overlap_le_bayes [Nonempty X] {joint : X → M → ℝ} (hnn : ∀ x m, 0 ≤ joint x m)
    (hsum : ∑ x, ∑ m, joint x m = 1) {i j : X} (hij : i ≠ j) :
    ∑ m, min (joint i m) (joint j m) ≤ bayesError joint := by
  unfold bayesError
  have hm : ∀ m, min (joint i m) (joint j m) +
      Finset.univ.sup' Finset.univ_nonempty (fun x => joint x m) ≤ ∑ x, joint x m := by
    intro m
    obtain ⟨x0, _, hx0⟩ := Finset.exists_mem_eq_sup' (s := Finset.univ) Finset.univ_nonempty
      (fun x => joint x m)
    rw [hx0]
    have hpair : ∀ y, y ≠ x0 → joint y m + joint x0 m ≤ ∑ x, joint x m := by
      intro y hy
      have hsub : ({y, x0} : Finset X) ⊆ Finset.univ := Finset.subset_univ _
      have := Finset.sum_le_sum_of_subset_of_nonneg hsub (fun x _ _ => hnn x m)
      rwa [Finset.sum_pair hy] at this
    by_cases hi : i = x0
    · have hj : j ≠ x0 := fun h => hij (hi.trans h.symm)
      have := hpair j hj
      have : min (joint i m) (joint j m) ≤ joint j m := min_le_right _ _
      linarith
    · have := hpair i hi
      have : min (joint i m) (joint j m) ≤ joint i m := min_le_left _ _
      linarith
  have htot := Finset.sum_le_sum fun m (_ : m ∈ Finset.univ) => hm m
  rw [Finset.sum_add_distrib, Finset.sum_comm] at htot
  rw [hsum] at htot
  linarith

/-- Any set of edges contributes at most the real learning rate. -/
lemma edges_le_iAltReal {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (E : Finset (X × X)) :
    ∑ e ∈ E, flux π W e.1 e.2 * klSum (p e.1) (p e.2) ≤ iAltReal π W p := by
  unfold iAltReal
  rw [← Fintype.sum_prod_type' (fun x x' => flux π W x x' * klSum (p x) (p x'))]
  exact Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ E)
    (fun e _ _ => mul_nonneg (flux_nonneg hπ hW _ _) (klSum_nonneg (hp _).1 (hp _).1))

/-- Any set of edges contributes at most the extended learning rate. -/
lemma edges_le_iAlt {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ} (E : Finset (X × X)) :
    ∑ e ∈ E, ENNReal.ofReal (flux π W e.1 e.2) * kl (p e.1) (p e.2) ≤ iAlt π W p := by
  unfold iAlt
  rw [← Fintype.sum_prod_type' (fun x x' => ENNReal.ofReal (flux π W x x') * kl (p x) (p x'))]
  exact Finset.sum_le_sum_of_subset (Finset.subset_univ E)

/-- The extended learning rate dominates the real edge sum whenever every
edge in the set carries an absolutely continuous pair, and is `⊤` when a
positive-flux edge in the set does not. -/
lemma ofReal_edges_le_iAlt {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hW : ∀ x x', 0 ≤ W x x') (hp : ∀ x, Prob (p x))
    (E : Finset (X × X)) (hpos : ∀ e ∈ E, 0 < flux π W e.1 e.2) {c : ℝ}
    (hc : (∀ e ∈ E, AC (p e.1) (p e.2)) →
      c ≤ ∑ e ∈ E, flux π W e.1 e.2 * klSum (p e.1) (p e.2)) :
    ENNReal.ofReal c ≤ iAlt π W p := by
  by_cases hac : ∀ e ∈ E, AC (p e.1) (p e.2)
  · refine le_trans (ENNReal.ofReal_le_ofReal (hc hac)) (le_trans ?_ (edges_le_iAlt E))
    rw [ENNReal.ofReal_sum_of_nonneg
      (fun e _ => mul_nonneg (flux_nonneg hπ hW _ _) (klSum_nonneg (hp _).1 (hp _).1))]
    refine le_of_eq (Finset.sum_congr rfl fun e he => ?_)
    rw [kl_eq_ofReal (hp _).1 (hp _).1 (hac e he),
      ENNReal.ofReal_mul (flux_nonneg hπ hW _ _)]
  · push Not at hac
    obtain ⟨e, he, hne⟩ := hac
    rw [iAlt_eq_top_of_singular hπ hW (hpos e he) (hp _) (hp _) hne]
    exact le_top

/-- The pairwise bound on the two directed edges of the pair alone. Line 115. -/
theorem pairwise_L_edges [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hπsum : ∑ x, π x = 1) (_hW : ∀ x x', 0 ≤ W x x')
    (hp : ∀ x, Prob (p x)) {i j : X} (hij : i ≠ j)
    (hfij : 0 < flux π W i j) (hfji : 0 < flux π W j i)
    (hε : bayesError (fun x m => π x * p x m) < min (π i) (π j))
    (hacij : AC (p i) (p j)) (hacji : AC (p j) (p i)) :
    min (flux π W i j) (flux π W j i) *
        (2 * L (bayesError (fun x m => π x * p x m) / (2 * min (π i) (π j)))) ≤
      flux π W i j * klSum (p i) (p j) + flux π W j i * klSum (p j) (p i) := by
  set ε := bayesError (fun x m => π x * p x m) with hεdef
  set μ := min (π i) (π j) with hμ
  have hπi : 0 < π i := by
    by_contra h
    have : π i = 0 := le_antisymm (not_lt.mp h) (hπ i)
    simp [flux, this] at hfij
  have hπj : 0 < π j := by
    by_contra h
    have : π j = 0 := le_antisymm (not_lt.mp h) (hπ j)
    simp [flux, this] at hfji
  have hμpos : 0 < μ := lt_min hπi hπj
  -- the overlap of the two conditionals is at most `ε / μ`
  have hjoint_nn : ∀ x m, 0 ≤ π x * p x m := fun x m => mul_nonneg (hπ x) ((hp x).1 m)
  have hjoint_sum : ∑ x, ∑ m, π x * p x m = 1 := by
    simp_rw [← Finset.mul_sum, (hp _).2, mul_one, hπsum]
  have hob := overlap_le_bayes hjoint_nn hjoint_sum hij
  have hscale : μ * overlap (p i) (p j) ≤ ∑ m, min (π i * p i m) (π j * p j m) := by
    unfold overlap
    rw [Finset.mul_sum]
    refine Finset.sum_le_sum fun m _ => ?_
    have hpi := (hp i).1 m
    have hpj := (hp j).1 m
    rw [le_min_iff]
    constructor
    · exact mul_le_mul (min_le_left _ _) (min_le_left _ _) (le_min hpi hpj) hπi.le
    · exact mul_le_mul (min_le_right _ _) (min_le_right _ _) (le_min hpi hpj) hπj.le
  have hov_le : overlap (p i) (p j) / 2 ≤ ε / (2 * μ) := by
    rw [div_le_div_iff₀ (by norm_num) (by positivity)]
    nlinarith
  -- the overlap is positive under mutual absolute continuity
  have hov_pos : 0 < overlap (p i) (p j) := by
    obtain ⟨m, hm⟩ : ∃ m, 0 < p i m := by
      by_contra h
      push Not at h
      have : ∑ m, p i m ≤ 0 := Finset.sum_nonpos fun m _ => h m
      rw [(hp i).2] at this
      norm_num at this
    have hjm : 0 < p j m := hacij m hm.ne'
    unfold overlap
    have hnn : ∀ m ∈ Finset.univ, 0 ≤ min (p i m) (p j m) :=
      fun m _ => le_min ((hp i).1 m) ((hp j).1 m)
    exact lt_of_lt_of_le (lt_min hm hjm)
      (Finset.single_le_sum (f := fun m => min (p i m) (p j m)) hnn (Finset.mem_univ m))
  have hη : ε / (2 * μ) < 1 / 2 := by
    rw [div_lt_iff₀ (by positivity)]
    linarith
  have hLmono : L (ε / (2 * μ)) ≤ L (overlap (p i) (p j) / 2) :=
    L_antitone ⟨by positivity, by linarith⟩ ⟨lt_of_lt_of_le (by positivity) hov_le, hη.le⟩
      hov_le
  have hJ := jeffreys_ge_two_L (hp i) (hp j) hacij hacji
  -- the two directed edges
  set m0 := min (flux π W i j) (flux π W j i)
  have hm0 : 0 ≤ m0 := le_min hfij.le hfji.le
  have hk1 := klSum_nonneg (hp i).1 (hp j).1
  have hk2 := klSum_nonneg (hp j).1 (hp i).1
  have h1 : m0 * klSum (p i) (p j) ≤ flux π W i j * klSum (p i) (p j) :=
    mul_le_mul_of_nonneg_right (min_le_left _ _) hk1
  have h2 : m0 * klSum (p j) (p i) ≤ flux π W j i * klSum (p j) (p i) :=
    mul_le_mul_of_nonneg_right (min_le_right _ _) hk2
  have h3 : m0 * (2 * L (ε / (2 * μ))) ≤ m0 * (klSum (p i) (p j) + klSum (p j) (p i)) :=
    mul_le_mul_of_nonneg_left (by linarith) hm0
  linarith

/-- Pairwise `L` bound. If `i ≠ j`, both directed fluxes are positive,
`ε < min(π(i), π(j))`, and the two conditionals are mutually absolutely
continuous, then `I_alt ≥ min(j_ij, j_ji) · 2 L(ε / (2 min(π(i), π(j))))`.
Lines 27 and 115. -/
theorem pairwise_L [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hπsum : ∑ x, π x = 1) (hW : ∀ x x', 0 ≤ W x x')
    (hp : ∀ x, Prob (p x)) {i j : X} (hij : i ≠ j)
    (hfij : 0 < flux π W i j) (hfji : 0 < flux π W j i)
    (hε : bayesError (fun x m => π x * p x m) < min (π i) (π j))
    (hacij : AC (p i) (p j)) (hacji : AC (p j) (p i)) :
    min (flux π W i j) (flux π W j i) *
        (2 * L (bayesError (fun x m => π x * p x m) / (2 * min (π i) (π j)))) ≤
      iAltReal π W p := by
  have hE := edges_le_iAltReal hπ hW hp {(i, j), (j, i)}
  have hne : (i, j) ≠ (j, i) := fun h => hij (Prod.mk.inj h).1
  rw [Finset.sum_pair hne] at hE
  exact le_trans (pairwise_L_edges hπ hπsum hW hp hij hfij hfji hε hacij hacji) hE

/-- The pairwise bound on the extended learning rate, with no
absolute-continuity hypothesis. -/
theorem pairwise_L_ennreal [Nonempty X] {π : X → ℝ} {W : X → X → ℝ} {p : X → M → ℝ}
    (hπ : ∀ x, 0 ≤ π x) (hπsum : ∑ x, π x = 1) (hW : ∀ x x', 0 ≤ W x x')
    (hp : ∀ x, Prob (p x)) {i j : X} (hij : i ≠ j)
    (hfij : 0 < flux π W i j) (hfji : 0 < flux π W j i)
    (hε : bayesError (fun x m => π x * p x m) < min (π i) (π j)) :
    ENNReal.ofReal (min (flux π W i j) (flux π W j i) *
        (2 * L (bayesError (fun x m => π x * p x m) / (2 * min (π i) (π j))))) ≤
      iAlt π W p := by
  have hne : (i, j) ≠ (j, i) := fun h => hij (Prod.mk.inj h).1
  refine ofReal_edges_le_iAlt hπ hW hp {(i, j), (j, i)} ?_ ?_
  · intro e he
    rcases Finset.mem_insert.mp he with rfl | he'
    · exact hfij
    · rw [Finset.mem_singleton.mp he']; exact hfji
  · intro hac
    have hacij := hac (i, j) (by simp)
    have hacji := hac (j, i) (by simp)
    rw [Finset.sum_pair hne]
    exact pairwise_L_edges hπ hπsum hW hp hij hfij hfji hε hacij hacji

/-- The fair telegraph of rate `r`. -/
noncomputable def telegraphπ : Fin 2 → ℝ := fun _ => 1 / 2

/-- Flip rate `r` each way, zero on the diagonal. -/
noncomputable def telegraphW (r : ℝ) : Fin 2 → Fin 2 → ℝ := fun x x' => if x = x' then 0 else r

/-- On the fair telegraph the pairwise bound is `r L(ε)`, for any finite
memory, when `ε < 1/2`. Line 27, "On the telegraph this is again `r L(ε)`". -/
theorem pairwise_telegraph {r : ℝ} (hr : 0 < r) {p : Fin 2 → M → ℝ} (hp : ∀ x, Prob (p x))
    (hε : bayesError (fun x m => telegraphπ x * p x m) < 1 / 2) :
    ENNReal.ofReal (r * L (bayesError (fun x m => telegraphπ x * p x m))) ≤
      iAlt telegraphπ (telegraphW r) p := by
  have hπ : ∀ x, 0 ≤ telegraphπ x := fun _ => by norm_num [telegraphπ]
  have hπsum : ∑ x, telegraphπ x = 1 := by simp [telegraphπ]
  have hW : ∀ x x', 0 ≤ telegraphW r x x' := by
    intro x x'; unfold telegraphW; split_ifs <;> linarith
  have h01 : flux telegraphπ (telegraphW r) 0 1 = r / 2 := by
    simp [flux, telegraphπ, telegraphW]; ring
  have h10 : flux telegraphπ (telegraphW r) 1 0 = r / 2 := by
    simp [flux, telegraphπ, telegraphW]; ring
  have hmin : min (telegraphπ 0) (telegraphπ 1) = 1 / 2 := by simp [telegraphπ]
  have hb := pairwise_L_ennreal hπ hπsum hW hp (i := 0) (j := 1) (by decide)
    (by rw [h01]; positivity) (by rw [h10]; positivity) (by rw [hmin]; exact hε)
  rw [h01, h10, hmin, min_self] at hb
  have heq : r / 2 * (2 * L (bayesError (fun x m => telegraphπ x * p x m) / (2 * (1 / 2)))) =
      r * L (bayesError (fun x m => telegraphπ x * p x m)) := by
    rw [show (2 : ℝ) * (1 / 2) = 1 by norm_num, div_one]; ring
  rwa [heq] at hb

end FiniteFloor
