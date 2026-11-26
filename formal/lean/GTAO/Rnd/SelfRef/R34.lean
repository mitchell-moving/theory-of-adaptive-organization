/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Side R&D, record-cost chain: `theory/RECORD_COST_CHAIN_2026-11-25.md`. Moved from a private Lake project
(library `GTAORnd`, same Lean and Mathlib pins). Statements and proofs unchanged; only this
header, the module lines and doc-comment paths differ. Session labels (R2a′, R3, C3, §R3.4, …)
are mapped to the note's steps S1–S10 in its §3.
-/
module

public import GTAO.Rnd.SelfRef.CircleOrbit
public import GTAO.Rnd.SelfRef.DimBound

@[expose] public section

/-!
# The exact Lean targets of theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route) §R3.4

* Item 1 `fourier_core` — R2a′ Fourier core, verbatim form (sums over k = 1..K).
* Item 2 `no_linear_clone_gpt` — R2a′ GPT form, verbatim hypotheses.
* Item 3 `R3_full` — d ≥ N + 1 in the stated affine form, with ONE declared modelling
  hypothesis standing in for "compact ⇒ invariant inner product" (see below).
* Item 4 (C3, ball) — partial; see `Ball.lean`.
* Item 5 `F1_cycle_count` — the finite-cycle counting statement.

Item 1's suggested proof (integrate against cos 2Kt, sin 2Kt) is replaced by an equivalent
polynomial-identity proof (`top_coeff_zero` in `CircleOrbit.lean`); the statement is the same.
-/

namespace GTAORnd.SelfRef

open Finset

lemma sum_Icc_eq_range_succ (K : ℕ) (g : ℕ → ℝ) :
    ∑ k ∈ Icc 1 K, g k = ∑ k ∈ range K, g (k + 1) := by
  induction K with
  | zero => simp
  | succ K ih => rw [Finset.sum_Icc_succ_top (by omega), ih, Finset.sum_range_succ]

/-- **§R3.4 item 1 (R2a′ Fourier core).** Let K ≥ 1. If for all t
`α₀ + Σ_{k=1}^{K} (α_k cos kt + β_k sin kt) = (c₀ + Σ_{k=1}^{K} (a_k cos kt + b_k sin kt))²`,
then `a_K = b_K = 0`. -/
theorem fourier_core (K : ℕ) (hK : 1 ≤ K) (c₀ α₀ : ℝ) (a b α β : ℕ → ℝ)
    (h : ∀ t : ℝ, α₀ + ∑ k ∈ Icc 1 K, (α k * Real.cos (k * t) + β k * Real.sin (k * t)) =
      (c₀ + ∑ k ∈ Icc 1 K, (a k * Real.cos (k * t) + b k * Real.sin (k * t))) ^ 2) :
    a K = 0 ∧ b K = 0 := by
  let u : ℕ → ℝ := fun k => if k = 0 then α₀ else α k
  let v : ℕ → ℝ := fun k => if k = 0 then 0 else β k
  let a' : ℕ → ℝ := fun k => if k = 0 then c₀ else a k
  let b' : ℕ → ℝ := fun k => if k = 0 then 0 else b k
  have conv : ∀ (x₀ : ℝ) (x y : ℕ → ℝ) (t : ℝ),
      trigSum (fun k => if k = 0 then x₀ else x k) (fun k => if k = 0 then 0 else y k) K t =
        x₀ + ∑ k ∈ Icc 1 K, (x k * Real.cos (k * t) + y k * Real.sin (k * t)) := by
    intro x₀ x y t
    rw [trigSum, Finset.sum_range_succ', sum_Icc_eq_range_succ]
    simp [add_comm]
  have := top_coeff_zero K hK u v a' b' (fun t => by
    simp only [u, v, a', b']; rw [conv, conv]; exact h t)
  have hK0 : K ≠ 0 := by omega
  simpa [a', b', hK0] using this

variable {V W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]

/-- **§R3.4 item 2 (R2a′, GPT form).** Let `f : V →ₗ ℝ`, `ℓ : W →ₗ ℝ`, `Φ : V → W` with
`ℓ(Φ v) = (f v)²`. Let `p(t) = c + Σ_{k=1}^{K} (cos(kt)·u_k + sin(kt)·v_k)` with
`(f u_K, f v_K) ≠ (0,0)`. Then there is no linear `T` with `T(p t) = Φ(p t)` for all t. -/
theorem no_linear_clone_gpt (f : V →ₗ[ℝ] ℝ) (ℓ : W →ₗ[ℝ] ℝ) (Φ : V → W)
    (hΦ : ∀ v, ℓ (Φ v) = (f v) ^ 2) (K : ℕ) (hK : 1 ≤ K) (c : V) (u v : ℕ → V)
    (hsee : (f (u K), f (v K)) ≠ (0, 0)) :
    ¬ ∃ T : V →ₗ[ℝ] W, ∀ t : ℝ,
      T (c + ∑ k ∈ Icc 1 K, (Real.cos (k * t) • u k + Real.sin (k * t) • v k)) =
        Φ (c + ∑ k ∈ Icc 1 K, (Real.cos (k * t) • u k + Real.sin (k * t) • v k)) := by
  rintro ⟨T, hT⟩
  have := fourier_core K hK (f c) (ℓ (T c)) (fun k => f (u k)) (fun k => f (v k))
    (fun k => ℓ (T (u k))) (fun k => ℓ (T (v k))) (fun t => by
      have h := congrArg ℓ (hT t)
      rw [hΦ] at h
      simpa [map_add, map_sum, map_smul, smul_eq_mul, mul_comm] using h)
  exact hsee (by simp [this.1, this.2])

/-- **§R3.4 item 5 (F1).** If `σ^P x = x` then for all n,
`#{t < nP : σ^t x ∈ S} = n · #{t < P : σ^t x ∈ S}`. -/
theorem F1_cycle_count {α : Type*} [Fintype α] [DecidableEq α] (σ : Equiv.Perm α) (P : ℕ)
    (x : α) (hP : (σ ^ P) x = x) (S : Set α) [DecidablePred (· ∈ S)] (n : ℕ) :
    ((range (n * P)).filter (fun t => (σ ^ t) x ∈ S)).card =
      n * ((range P).filter (fun t => (σ ^ t) x ∈ S)).card := by
  have hper : ∀ m t : ℕ, (σ ^ (m * P + t)) x = (σ ^ t) x := by
    intro m t
    have hm : (σ ^ (m * P)) x = x := by
      induction m with
      | zero => simp
      | succ m ih => rw [Nat.succ_mul, pow_add, Equiv.Perm.mul_apply, hP, ih]
    rw [add_comm, pow_add, Equiv.Perm.mul_apply, hm]
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.card_filter, Nat.succ_mul, Finset.sum_range_add, ← Finset.card_filter, ih]
    simp only [hper]
    rw [← Finset.card_filter]; ring

/-! ### §R3.4 item 3 (R3 full) -/

/-- **§R3.4 item 3 (R3, stated affine form).**

Ω ⊆ V (V ≅ ℝ^d, `d = finrank V`) compact, convex, nonempty interior. A connected topological
group `H` acts by affine maps `ρ h` preserving Ω, nontrivially on Ω, and fixes N ≥ 1 points
`ω j ∈ Ω` that are jointly perfectly distinguishable (affine `e i` with values in [0,1] on Ω,
`e i (ω j) = δ_ij`, `Σ e i = 1` on Ω). Then `d ≥ N + 1`.

**Declared modelling hypothesis `hinv`** (replaces "H compact"): the linear parts of the
`ρ h` are isometries of the inner product of `V`, and `h ↦ linear part` is continuous. For a
compact `H` such an inner product exists by Haar averaging (standard, not formalized here).
Also: the effects are taken as affine maps on all of `V` (on a set with nonempty interior,
affine maps on Ω extend uniquely, so nothing is lost). Compactness, convexity, the interior,
`[0,1]`-valuedness and `Σ e i = 1` are carried as hypotheses for fidelity but are not needed
by the proof once `hinv` is assumed. -/
theorem R3_full {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    [FiniteDimensional ℝ V] (Ω : Set V) (_hΩc : IsCompact Ω) (_hΩv : Convex ℝ Ω)
    (_hΩi : (interior Ω).Nonempty)
    {H : Type*} [Group H] [TopologicalSpace H] [ConnectedSpace H]
    (ρ : H → V →ᵃ[ℝ] V) (_hpres : ∀ h, ρ h '' Ω = Ω)
    (hone : ρ 1 = AffineMap.id ℝ V)
    (hnt : ∃ h, ∃ x ∈ Ω, ρ h x ≠ x)
    {n : ℕ} (ω : Fin (n + 1) → V) (_hωΩ : ∀ j, ω j ∈ Ω) (hfix : ∀ h j, ρ h (ω j) = ω j)
    (e : Fin (n + 1) → V →ᵃ[ℝ] ℝ) (_he01 : ∀ i, ∀ x ∈ Ω, e i x ∈ Set.Icc (0 : ℝ) 1)
    (_hesum : ∀ x ∈ Ω, ∑ i, e i x = 1) (hδ : ∀ i j, e i (ω j) = if i = j then 1 else 0)
    (lin : H → V →L[ℝ] V) (hlin : ∀ h, ((lin h) : V →ₗ[ℝ] V) = (ρ h).linear)
    (hinv : (∀ h x, ‖lin h x‖ = ‖x‖) ∧ Continuous lin) :
    (n + 1) + 1 ≤ Module.finrank ℝ V := by
  -- distinguishable ⇒ affinely independent
  have hai := distinguishable_affineIndependent ω e hδ
  have hl : ∀ h y, lin h y = (ρ h).linear y := fun h y => by rw [← hlin h]; rfl
  -- move the origin to the fixed point ω 0: work with q j = ω j - ω 0
  let q : Fin (n + 1) → V := fun j => ω j - ω 0
  have hq : AffineIndependent ℝ q := by
    have := hai.map' (AffineEquiv.vaddConst ℝ (-ω 0)).toAffineMap
      (AffineEquiv.vaddConst ℝ (-ω 0)).injective
    convert this using 1
    funext j; simp [q, sub_eq_add_neg]
  -- the linear parts fix every q j
  have hlinfix : ∀ h j, lin h (q j) = q j := by
    intro h j
    have := (ρ h).linear_apply_vsub (ω j) (ω 0)
    rw [hfix, hfix] at this
    simp only [vsub_eq_sub] at this
    rw [hl]; exact this
  refine dim_bound q hq (Set.range lin) (isPreconnected_range hinv.2) ⟨1, ?_⟩ ?_ ?_ ?_
  · ext x; rw [hl, hone]; simp
  · rintro _ ⟨h, rfl⟩ x; exact hinv.1 h x
  · rintro _ ⟨h, rfl⟩ j; exact hlinfix h j
  · obtain ⟨h, x, -, hx⟩ := hnt
    refine ⟨lin h, ⟨h, rfl⟩, fun heq => hx ?_⟩
    have hdecomp : ρ h x = (ρ h).linear (x - ω 0) + ρ h (ω 0) := by
      have := (ρ h).linear_apply_vsub x (ω 0)
      simp only [vsub_eq_sub] at this
      rw [this]; abel
    rw [hdecomp, hfix, ← hl, heq]
    simp

end GTAORnd.SelfRef
