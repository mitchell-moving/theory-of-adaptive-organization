/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Side R&D, record-cost chain: `theory/RECORD_COST_CHAIN_2026-11-25.md`. Moved from a private Lake project
(library `GTAORnd`, same Lean and Mathlib pins). Statements and proofs unchanged; only this
header, the module lines and doc-comment paths differ. Session labels (R2a′, R3, C3, §R3.4, …)
are mapped to the note's steps S1–S10 in its §3.
-/
module

public import GTAO.Rnd.LemmaB1

@[expose] public section

/-!
# The square bit: the hypotheses of Lemma B1 are satisfiable (non-vacuity witness)

NOTE.md: "the square bit (N = 2) satisfies the hypothesis with M = 4, k = 2".

Here we build a `CopyModel` whose single system is the square [-1,1]², whose allowed
measurements are finite families of *affine* (multi-affine on composites), nonnegative,
normalized functions, and prove:

* `square_capacity_le_two`: the square has capacity ≤ 2 (no 3 states are jointly perfectly
  distinguishable by affine effects). Elementary proof: each coarse-grained effect
  g = A + B p₁ + C p₂ that equals 1 somewhere and is ≥ 0 on the square has A ≥ 1/2, and the
  A's of a measurement sum to 1.
* `square_B1_hypotheses`: the 4 corners and the 2 effects (1 ± p₁)/2, (1 ± p₂)/2 meet every
  hypothesis of `lemmaB1` with N = 2, M = 4, k = 2.

Caveat (stated, not hidden): the channel set of this witness model is identity-only, so the
conclusion "no cloner" is trivially true *in this model*. The model exists only to show that
the capacity and sharpness hypotheses of Lemma B1 can be met together; it is not a model of
the square bit's composite (boxworld) dynamics.
-/

namespace GTAORnd

open Finset

/-- points of the square [-1,1]² -/
abbrev Sq : Type := {p : ℝ × ℝ // |p.1| ≤ 1 ∧ |p.2| ≤ 1}

/-- `f` is affine in each coordinate separately (on the n-fold composite). -/
def MultiAff {n : ℕ} (f : (Fin n → Sq) → ℝ) : Prop :=
  ∀ (j : Fin n) (s : Fin n → Sq), ∃ a b c : ℝ, ∀ p : Sq,
    f (Function.update s j p) = a + b * p.1.1 + c * p.1.2

/-- allowed measurements: nonnegative, normalized, multi-affine -/
def SqMeas (n : ℕ) (ι : Type) [Fintype ι] : Set (ι → (Fin n → Sq) → ℝ) :=
  {m | (∀ i s, 0 ≤ m i s) ∧ (∀ s, ∑ i, m i s = 1) ∧ ∀ i, MultiAff (m i)}

/-- identity-only channels -/
def SqChan (m n : ℕ) : Set ((Fin m → Sq) → (Fin n → Sq)) :=
  {f | ∃ h : m = n, ∀ s, f s = h ▸ s}

lemma one_update (s : Fin 1 → Sq) (p : Sq) : (fun _ : Fin 1 => p) = Function.update s 0 p := by
  funext i; fin_cases i; simp

/-- A single-system affine function, in coordinates. -/
lemma aff_one {f : (Fin 1 → Sq) → ℝ} (hf : MultiAff f) (s₀ : Fin 1 → Sq) :
    ∃ a b c : ℝ, ∀ s : Fin 1 → Sq, f s = a + b * (s 0).1.1 + c * (s 0).1.2 := by
  obtain ⟨a, b, c, h⟩ := hf 0 s₀
  refine ⟨a, b, c, fun s => ?_⟩
  have : s = Function.update s₀ 0 (s 0) := by
    funext i; fin_cases i; simp
  rw [this, h]; simp

noncomputable def squareModel : CopyModel where
  St n := Fin n → Sq
  Meas n ι _ := SqMeas n ι
  Chan := SqChan
  prod n ω := fun j => ω j 0
  prod_one ω := by funext i; fin_cases i; rfl
  meas_sum hm s := hm.2.1 s
  chan_id n := ⟨rfl, fun _ => rfl⟩
  chan_comp := by
    rintro a b c f g ⟨rfl, hf⟩ ⟨rfl, hg⟩
    exact ⟨rfl, fun s => by simp [hf, hg]⟩
  meas_pullback := by
    rintro m n ι _ M T hM ⟨rfl, hT⟩
    have : (fun i s => M i (T s)) = M := by funext i s; rw [hT]
    rw [this]; exact hM
  prod_meas := by
    intro n e he
    refine ⟨fun b s => ∏ j, e j (b j) (fun _ => s j), ⟨?_, ?_, ?_⟩, ?_⟩
    · intro b s; exact Finset.prod_nonneg fun j _ => (he j).1 _ _
    · intro s
      have := Finset.prod_univ_sum (fun _ : Fin n => (univ : Finset (Fin 2)))
        (fun j c => e j c (fun _ => s j))
      rw [Fintype.piFinset_univ] at this
      rw [← this]
      exact Finset.prod_eq_one fun j _ => (he j).2.1 _
    · intro b j s
      obtain ⟨a, bb, c, h⟩ := aff_one ((he j).2.2 (b j)) (fun _ => s j)
      set K := ∏ i ∈ univ.erase j, e i (b i) (fun _ => s i)
      refine ⟨a * K, bb * K, c * K, fun p => ?_⟩
      show ∏ i, e i (b i) (fun _ => Function.update s j p i) = _
      rw [← Finset.mul_prod_erase univ _ (mem_univ j)]
      have hK : ∏ i ∈ univ.erase j, e i (b i) (fun _ => Function.update s j p i) = K :=
        Finset.prod_congr rfl fun i hi => by
          rw [Function.update_of_ne (Finset.ne_of_mem_erase hi)]
      simp only [Function.update_self] at *
      rw [hK, h]; ring
    · intro b ω
      refine Finset.prod_congr rfl fun j _ => ?_
      congr 1; funext i; fin_cases i; rfl
  local_ext := by
    rintro n T ⟨h, -⟩
    exact absurd h (by decide)

/-- **Capacity of the square is at most 2.** -/
theorem square_capacity_le_two : squareModel.CapacityLE 2 := by
  intro M ω ⟨ι, _, m, d, hm, hdist⟩
  by_contra hM
  push Not at hM
  obtain ⟨hnn, hsum, haff⟩ := hm
  -- coordinates of every outcome function
  have hco : ∀ i, ∃ a b c : ℝ, ∀ s : Fin 1 → Sq, m i s = a + b * (s 0).1.1 + c * (s 0).1.2 :=
    fun i => aff_one (haff i) (ω ⟨0, by omega⟩)
  choose a b c hc using hco
  -- coarse-grained coefficients
  let A : Fin M → ℝ := fun j => ∑ i ∈ univ.filter (fun i => d i = j), a i
  let B : Fin M → ℝ := fun j => ∑ i ∈ univ.filter (fun i => d i = j), b i
  let C : Fin M → ℝ := fun j => ∑ i ∈ univ.filter (fun i => d i = j), c i
  have hg : ∀ j (s : Fin 1 → Sq), ∑ i ∈ univ.filter (fun i => d i = j), m i s
      = A j + B j * (s 0).1.1 + C j * (s 0).1.2 := by
    intro j s
    simp only [hc, A, B, C, Finset.sum_add_distrib, Finset.sum_mul]
  -- a point of the square as a state
  let pt : (x y : ℝ) → |x| ≤ 1 → |y| ≤ 1 → (Fin 1 → Sq) := fun x y hx hy _ => ⟨(x, y), hx, hy⟩
  -- each A j ≥ 1/2
  have hA : ∀ j, 1 / 2 ≤ A j := by
    intro j
    -- value 1 at ω j
    have h1 : A j + B j * (ω j 0).1.1 + C j * (ω j 0).1.2 = 1 := by
      rw [← hg j (ω j)]; exact hdist j
    have hb1 : |(ω j 0).1.1| ≤ 1 := (ω j 0).2.1
    have hb2 : |(ω j 0).1.2| ≤ 1 := (ω j 0).2.2
    have e1 : B j * (ω j 0).1.1 ≤ |B j| := by
      calc B j * (ω j 0).1.1 ≤ |B j * (ω j 0).1.1| := le_abs_self _
        _ = |B j| * |(ω j 0).1.1| := abs_mul _ _
        _ ≤ |B j| * 1 := by gcongr
        _ = |B j| := mul_one _
    have e2 : C j * (ω j 0).1.2 ≤ |C j| := by
      calc C j * (ω j 0).1.2 ≤ |C j * (ω j 0).1.2| := le_abs_self _
        _ = |C j| * |(ω j 0).1.2| := abs_mul _ _
        _ ≤ |C j| * 1 := by gcongr
        _ = |C j| := mul_one _
    -- nonneg at the worst corner
    let x : ℝ := if 0 ≤ B j then -1 else 1
    let y : ℝ := if 0 ≤ C j then -1 else 1
    have hx : |x| ≤ 1 := by simp only [x]; split_ifs <;> norm_num
    have hy : |y| ≤ 1 := by simp only [y]; split_ifs <;> norm_num
    have h0 : 0 ≤ A j + B j * x + C j * y := by
      have := Finset.sum_nonneg (s := univ.filter (fun i => d i = j))
        (fun i _ => hnn i (pt x y hx hy))
      rw [hg] at this; simpa [pt] using this
    have hBx : B j * x = -|B j| := by
      simp only [x]; split_ifs with hB
      · rw [abs_of_nonneg hB]; ring
      · rw [abs_of_neg (not_le.mp hB)]; ring
    have hCy : C j * y = -|C j| := by
      simp only [y]; split_ifs with hC
      · rw [abs_of_nonneg hC]; ring
      · rw [abs_of_neg (not_le.mp hC)]; ring
    linarith
  -- the A's sum to 1 (evaluate the measurement at the centre)
  have hA1 : ∑ j, A j = 1 := by
    have h := hsum (pt 0 0 (by simp) (by simp))
    rw [← Finset.sum_fiberwise univ d] at h
    simp only [hg] at h
    simpa [pt] using h
  have hle : ∑ _j : Fin M, (1 / 2 : ℝ) ≤ ∑ j, A j := Finset.sum_le_sum fun j _ => hA j
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul] at hle
  have : (3 : ℝ) ≤ M := by exact_mod_cast hM
  linarith

/-- the four corners of the square, as single-system states -/
def corner (x : Fin 4) : Fin 1 → Sq := fun _ =>
  ⟨((if x.val % 2 = 0 then 1 else -1), (if x.val / 2 = 0 then 1 else -1)),
    by split_ifs <;> norm_num, by split_ifs <;> norm_num⟩

/-- the two sharp effects (1 + p₁)/2 and (1 + p₂)/2, as two-outcome measurements -/
noncomputable def sqEffect (j : Fin 2) : Fin 2 → (Fin 1 → Sq) → ℝ := fun c s =>
  let v := if j = 0 then (s 0).1.1 else (s 0).1.2
  if c = 1 then (1 + v) / 2 else (1 - v) / 2

/-- **The square bit meets every hypothesis of Lemma B1 with N = 2, M = 4, k = 2.** -/
theorem square_B1_hypotheses :
    squareModel.CapacityLE 2 ∧ (2 < 4) ∧
    (∀ j, sqEffect j ∈ squareModel.Meas 1 (Fin 2)) ∧
    (∀ j x, sqEffect j 1 (corner x) = 0 ∨ sqEffect j 1 (corner x) = 1) ∧
    Function.Injective (fun x => fun j => sqEffect j 1 (corner x)) := by
  refine ⟨square_capacity_le_two, by norm_num, ?_, ?_, ?_⟩
  · intro j
    refine ⟨?_, ?_, ?_⟩
    · intro c s
      have h1 := (s 0).2.1; have h2 := (s 0).2.2
      rw [abs_le] at h1 h2
      simp only [sqEffect]; split_ifs <;> linarith
    · intro s; simp [sqEffect, Fin.sum_univ_two]; ring
    · intro c i s
      refine ⟨1 / 2, (if c = 1 then 1 else -1) * (if j = 0 then 1 / 2 else 0),
        (if c = 1 then 1 else -1) * (if j = 0 then 0 else 1 / 2), fun p => ?_⟩
      have : i = 0 := Subsingleton.elim _ _
      subst this
      simp only [sqEffect, Function.update_self]
      split_ifs <;> ring
  · intro j x
    fin_cases j <;> fin_cases x <;> simp [sqEffect, corner]
  · intro x y hxy
    have h0 := congrFun hxy 0
    have h1 := congrFun hxy 1
    fin_cases x <;> fin_cases y <;> simp [sqEffect, corner] at h0 h1 ⊢

/-- Instantiating Lemma B1 on the witness (conclusion is trivial here because the witness
has identity-only channels; see the module caveat). -/
theorem square_no_clone : ¬ ∃ T, squareModel.Clones 2 T corner := by
  obtain ⟨hcap, -, he, hs, hinj⟩ := square_B1_hypotheses
  exact squareModel.lemmaB1 2 4 1 hcap (by norm_num) corner sqEffect he hs hinj

end GTAORnd
