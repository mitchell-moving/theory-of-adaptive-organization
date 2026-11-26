/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Side R&D, record-cost chain: `theory/RECORD_COST_CHAIN_2026-11-25.md`. Moved from a private Lake project
(library `GTAORnd`, same Lean and Mathlib pins). Statements and proofs unchanged; only this
header, the module lines and doc-comment paths differ. Session labels (R2a′, R3, C3, §R3.4, …)
are mapped to the note's steps S1–S10 in its §3.
-/
module

public import Mathlib

@[expose] public section

/-!
# R2a′: no linear map clones a circle orbit that the drift moves (frequency doubling)
(theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route), Round 2, R2a′; replaces the round-1 four-point shortcut)

Informal (NOTE.md R2a′): *let p(t) be a circle orbit through a moved pure state, with top
frequency k*. For any linear T, (f⊗f)∘T is a linear functional, so its values along p(t)
contain frequencies ≤ k* only. The clone requirement needs f(p(t))². For an effect f that
sees the k* component, that square has a nonzero 2k* component. Contradiction.*

Formal frame (same as `OrbitClone.lean`): states in a real vector space `V`; effects are a
separating set `E` of linear functionals; product states via a bilinear `prod`; each
`f ∈ E` has a product effect `Ff` with `Ff (prod x y) = f x * f y`.

A circle orbit with integer weights `0, 1, …, N` is
`p(t) = ∑_{k=0}^{N} (cos(k t) • A k + sin(k t) • B k)`
(any finite set of weights fits, by letting unused components be 0; `A 0` is the fixed
centre). That a circle action on a finite-dimensional space has orbits of this form (its
representation theory), and that a compact connected drift moving a state contains a
circle subgroup moving it (maximal tori), are standard facts taken as the setting and not
formalized here.

Proof route in Lean: complexify with `z = e^{it}`; a trigonometric sum of degree ≤ N times
`z^N` is a polynomial of degree ≤ 2N with top coefficient `(a_N − i b_N)/2`; the clone
identity becomes a polynomial identity on the unit circle (an infinite set), hence an
identity of polynomials; comparing the coefficient of `z^{4N}` gives `(a_N − i b_N)² = 0`.
-/

namespace GTAORnd.SelfRef

open Polynomial Complex Finset

/-- a real trigonometric sum of degree ≤ N -/
noncomputable def trigSum (a b : ℕ → ℝ) (N : ℕ) (t : ℝ) : ℝ :=
  ∑ k ∈ range (N + 1), (a k * Real.cos (k * t) + b k * Real.sin (k * t))

/-- complex coefficient `(a_k − i b_k)/2` -/
noncomputable def coefC (a b : ℕ → ℝ) (k : ℕ) : ℂ := ((a k : ℂ) - (b k : ℂ) * I) / 2

/-- `z^N · trigSum`, as a polynomial in `z` -/
noncomputable def trigPoly (a b : ℕ → ℝ) (N : ℕ) : ℂ[X] :=
  ∑ k ∈ range (N + 1),
    (C (coefC a b k) * X ^ (N + k) + C (starRingEnd ℂ (coefC a b k)) * X ^ (N - k))

lemma pair_eq (a b θ : ℝ) :
    ((a : ℂ) - b * I) / 2 * cexp (θ * I) + starRingEnd ℂ (((a : ℂ) - b * I) / 2) *
      cexp (((-θ : ℝ) : ℂ) * I) = ((a * Real.cos θ + b * Real.sin θ : ℝ) : ℂ) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I]
  apply Complex.ext <;>
    simp [← Complex.ofReal_cos, ← Complex.ofReal_sin, Complex.mul_re, Complex.mul_im,
      Complex.div_re, Complex.div_im] <;> ring

lemma zpow_split (t : ℝ) (N k : ℕ) (hk : k ≤ N) :
    cexp (t * I) ^ (N - k) = cexp (t * I) ^ N * cexp (((-(k * t) : ℝ) : ℂ) * I) := by
  have hzk : cexp (t * I) ^ k = cexp (((k * t : ℝ) : ℂ) * I) := by
    rw [← Complex.exp_natCast_mul]; congr 1; push_cast; ring
  have hinv : cexp (((k * t : ℝ) : ℂ) * I) * cexp (((-(k * t) : ℝ) : ℂ) * I) = 1 := by
    rw [← Complex.exp_add]; push_cast; simp
  calc cexp (t * I) ^ (N - k) = cexp (t * I) ^ (N - k) *
        (cexp (((k * t : ℝ) : ℂ) * I) * cexp (((-(k * t) : ℝ) : ℂ) * I)) := by rw [hinv, mul_one]
    _ = (cexp (t * I) ^ (N - k) * cexp (t * I) ^ k) * cexp (((-(k * t) : ℝ) : ℂ) * I) := by
        rw [hzk]; ring
    _ = cexp (t * I) ^ N * cexp (((-(k * t) : ℝ) : ℂ) * I) := by
        rw [pow_sub_mul_pow _ hk]

lemma trigPoly_eval (a b : ℕ → ℝ) (N : ℕ) (t : ℝ) :
    (trigPoly a b N).eval (cexp (t * I)) = cexp (t * I) ^ N * (trigSum a b N t : ℂ) := by
  simp only [trigPoly, trigSum, eval_finsetSum, eval_add, eval_mul, eval_C, eval_pow, eval_X,
    Complex.ofReal_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hkN : k ≤ N := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  have hzk : cexp (t * I) ^ k = cexp (((k * t : ℝ) : ℂ) * I) := by
    rw [← Complex.exp_natCast_mul]; congr 1; push_cast; ring
  rw [pow_add, zpow_split t N k hkN, hzk, ← pair_eq (a k) (b k) (k * t), coefC]
  ring

lemma trigPoly_natDegree (a b : ℕ → ℝ) (N : ℕ) : (trigPoly a b N).natDegree ≤ 2 * N := by
  unfold trigPoly
  apply Polynomial.natDegree_sum_le_of_forall_le
  intro k hk
  have hkN : k ≤ N := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  refine (natDegree_add_le _ _).trans (max_le ?_ ?_)
  · exact (natDegree_C_mul_X_pow_le _ _).trans (by omega)
  · exact (natDegree_C_mul_X_pow_le _ _).trans (by omega)

lemma trigPoly_coeff_top (a b : ℕ → ℝ) (N : ℕ) (hN : 1 ≤ N) :
    (trigPoly a b N).coeff (2 * N) = coefC a b N := by
  simp only [trigPoly, finsetSum_coeff, coeff_add, coeff_C_mul, coeff_X_pow]
  rw [Finset.sum_eq_single N]
  · have h1 : 2 * N = N + N := by ring
    have h2 : 2 * N ≠ N - N := by omega
    rw [ite_eq_left_of_eq_true (h := eq_true h1), ite_eq_right_of_eq_false (h := eq_false h2)]
    ring
  · intro k hk hkN
    have hkN' : k ≤ N := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have h1 : 2 * N ≠ N + k := by omega
    have h2 : 2 * N ≠ N - k := by omega
    simp [h1, h2]
  · intro h; exact absurd (Finset.mem_range.mpr (by omega)) h

/-- the unit circle (points `e^{it}`) is infinite -/
lemma circle_infinite (P : ℂ[X]) (h : ∀ t : ℝ, P.eval (cexp (t * I)) = 0) :
    Set.Infinite {x | IsRoot P x} := by
  refine Set.infinite_of_injective_forall_mem (f := fun n : ℕ => cexp (((1 / (n + 2) : ℝ) : ℂ) * I))
    ?_ (fun n => h _)
  intro n m hnm
  simp only at hnm
  have hr : ∀ j : ℕ, (1 / ((j : ℝ) + 2)) ∈ Set.Ioc (-Real.pi) Real.pi := by
    intro j
    have hj : (0 : ℝ) < 1 / ((j : ℝ) + 2) := by positivity
    have hj2 : 1 / ((j : ℝ) + 2) ≤ 1 / 2 := by
      apply one_div_le_one_div_of_le (by norm_num); linarith [(j.cast_nonneg : (0:ℝ) ≤ j)]
    constructor <;> linarith [Real.pi_gt_three]
  have := congrArg Complex.arg hnm
  rw [Complex.exp_mul_I, Complex.exp_mul_I] at this
  rw [Complex.arg_cos_add_sin_mul_I (hr n), Complex.arg_cos_add_sin_mul_I (hr m)] at this
  have h' : ((n : ℝ) + 2) = (m : ℝ) + 2 := by
    have hn : (0:ℝ) < n + 2 := by positivity
    have hm : (0:ℝ) < m + 2 := by positivity
    field_simp at this; linarith
  exact_mod_cast (by linarith : (n : ℝ) = m)

/-- **Frequency doubling (scalar core).** If a trigonometric sum of degree ≤ N equals the
square of another one of degree ≤ N for every t (N ≥ 1), the second has no degree-N part. -/
theorem top_coeff_zero (N : ℕ) (hN : 1 ≤ N) (u v a b : ℕ → ℝ)
    (h : ∀ t, trigSum u v N t = trigSum a b N t ^ 2) : a N = 0 ∧ b N = 0 := by
  set P : ℂ[X] := X ^ N * trigPoly u v N - (trigPoly a b N) ^ 2 with hP
  have hroot : ∀ t : ℝ, P.eval (cexp (t * I)) = 0 := by
    intro t
    simp only [hP, eval_sub, eval_mul, eval_pow, eval_X, trigPoly_eval, h t]
    push_cast; ring
  have hP0 : P = 0 := Polynomial.eq_zero_of_infinite_isRoot P (circle_infinite P hroot)
  have hc := congrArg (fun Q : ℂ[X] => Q.coeff (4 * N)) hP0
  simp only [hP, coeff_sub, coeff_zero] at hc
  rw [coeff_X_pow_mul', ite_eq_left_of_eq_true (h := eq_true (by omega : N ≤ 4 * N)),
    coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt (trigPoly_natDegree u v N) (by omega)),
    pow_two, show 4 * N = 2 * N + 2 * N by ring,
    coeff_mul_add_eq_of_natDegree_le (trigPoly_natDegree a b N) (trigPoly_natDegree a b N),
    trigPoly_coeff_top a b N hN] at hc
  have hz : coefC a b N = 0 := by
    have : coefC a b N * coefC a b N = 0 := by linear_combination -hc
    exact mul_self_eq_zero.mp this
  have hre := congrArg Complex.re hz
  have him := congrArg Complex.im hz
  simp [coefC] at hre him
  exact ⟨hre, him⟩

variable {V W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]

/-- a circle orbit with integer weights 0, …, N -/
noncomputable def circleOrbit (A B : ℕ → V) (N : ℕ) (t : ℝ) : V :=
  ∑ k ∈ range (N + 1), (Real.cos (k * t) • A k + Real.sin (k * t) • B k)

/-- **R2a′, top component.** A linear map cloning every point of the orbit forces the
top-weight component to vanish. -/
theorem circle_top_zero (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) (E : Set (Module.Dual ℝ V))
    (hprod : ∀ f ∈ E, ∃ Ff : Module.Dual ℝ W, ∀ x y, Ff (prod x y) = f x * f y)
    (hsep : ∀ v : V, (∀ f ∈ E, f v = 0) → v = 0)
    (N : ℕ) (hN : 1 ≤ N) (A B : ℕ → V) (T : V →ₗ[ℝ] W)
    (hT : ∀ t, T (circleOrbit A B N t) = prod (circleOrbit A B N t) (circleOrbit A B N t)) :
    A N = 0 ∧ B N = 0 := by
  have key : ∀ f ∈ E, f (A N) = 0 ∧ f (B N) = 0 := by
    intro f hf
    obtain ⟨Ff, hFf⟩ := hprod f hf
    apply top_coeff_zero N hN (fun k => Ff (T (A k))) (fun k => Ff (T (B k)))
      (fun k => f (A k)) (fun k => f (B k))
    intro t
    have h := congrArg Ff (hT t)
    rw [hFf, ← pow_two] at h
    simpa [trigSum, circleOrbit, map_sum, map_add, map_smul, smul_eq_mul, mul_comm] using h
  exact ⟨hsep _ fun f hf => (key f hf).1, hsep _ fun f hf => (key f hf).2⟩

/-- **R2a′, all moving components.** Every component of weight ≥ 1 vanishes. -/
theorem circle_all_zero (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) (E : Set (Module.Dual ℝ V))
    (hprod : ∀ f ∈ E, ∃ Ff : Module.Dual ℝ W, ∀ x y, Ff (prod x y) = f x * f y)
    (hsep : ∀ v : V, (∀ f ∈ E, f v = 0) → v = 0) (T : V →ₗ[ℝ] W) :
    ∀ (N : ℕ) (A B : ℕ → V),
      (∀ t, T (circleOrbit A B N t) = prod (circleOrbit A B N t) (circleOrbit A B N t)) →
      ∀ k, 1 ≤ k → k ≤ N → A k = 0 ∧ B k = 0 := by
  intro N
  induction N with
  | zero => intro A B _ k hk hkN; omega
  | succ N ih =>
    intro A B hT k hk hkN
    obtain ⟨hA, hB⟩ := circle_top_zero prod E hprod hsep (N + 1) (by omega) A B T hT
    have heq : ∀ t, circleOrbit A B (N + 1) t = circleOrbit A B N t := by
      intro t
      rw [circleOrbit, Finset.sum_range_succ, hA, hB]
      simp [circleOrbit]
    rcases Nat.lt_or_ge k (N + 1) with h | h
    · exact ih A B (fun t => by rw [← heq]; exact hT t) k hk (by omega)
    · have : k = N + 1 := by omega
      subst this; exact ⟨hA, hB⟩

/-- **R2a′.** If the drift moves the state (the orbit is not constant), no linear map —
positive or not — clones every state on the orbit. -/
theorem no_linear_clone_circle (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) (E : Set (Module.Dual ℝ V))
    (hprod : ∀ f ∈ E, ∃ Ff : Module.Dual ℝ W, ∀ x y, Ff (prod x y) = f x * f y)
    (hsep : ∀ v : V, (∀ f ∈ E, f v = 0) → v = 0)
    (N : ℕ) (A B : ℕ → V) (hmoved : ∃ t, circleOrbit A B N t ≠ circleOrbit A B N 0) :
    ¬ ∃ T : V →ₗ[ℝ] W,
      ∀ t, T (circleOrbit A B N t) = prod (circleOrbit A B N t) (circleOrbit A B N t) := by
  rintro ⟨T, hT⟩
  have hz := circle_all_zero prod E hprod hsep T N A B hT
  have hconst : ∀ t, circleOrbit A B N t = A 0 := by
    intro t
    unfold circleOrbit
    rw [Finset.sum_eq_single 0]
    · simp
    · intro k hk hk0
      obtain ⟨h1, h2⟩ := hz k (by omega) (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))
      simp [h1, h2]
    · intro h; exact absurd (Finset.mem_range.mpr (by omega)) h
  obtain ⟨t, ht⟩ := hmoved
  exact ht (by rw [hconst, hconst])

end GTAORnd.SelfRef
