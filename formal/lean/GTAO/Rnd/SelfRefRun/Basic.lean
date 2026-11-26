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

-- Copied verbatim from rnd/selfref/lean/SelfRef/Basic.lean (self-reference run), namespace renamed SelfRef → SelfRefRun to avoid clashing with GTAORnd.SelfRef. Source file left untouched.

/-!
# Self-reference route: small machine-checked lemmas (private R&D, not part of the repo)

Each lemma is the algebraic core of a toy claim in `../NOTE.md`. They are NOT physics claims.
- `liar_half`        : R1d, a flip's fixed state gives each outcome exactly 1/2.
- `exists_derangement`: R1b, deterministic worlds with ≥2 states have a process with no fixed state.
- `four_point`, `no_copier_four_point`: R2a single-frequency core (the disk/ball case).
- `perm_periodic`    : round 2, A9: every reversible process of a finite world is periodic.
- `path_sq_one_const`: R3 core, a continuous family of ±1 starting at 1 stays 1
                        (a connected group acting orthogonally on a line acts trivially).
- `midpoint_rho`     : R4a, the closed-form midpoint of the cost dial.
-/

namespace SelfRefRun

/-- R1d. If a flip `T` swaps an outcome effect (`e ∘ T = 1 - e`) and fixes `w`, then `e w = 1/2`. -/
theorem liar_half {Ω : Type*} (e : Ω → ℝ) (T : Ω → Ω)
    (hflip : ∀ w, e (T w) = 1 - e w) (w : Ω) (hfix : T w = w) : e w = 1 / 2 := by
  have h := hflip w
  rw [hfix] at h
  linarith

/-- R1b. Every finite deterministic world with at least two states has a process with no fixed state. -/
theorem exists_derangement (n : ℕ) (hn : 2 ≤ n) : ∃ f : Fin n → Fin n, ∀ i, f i ≠ i := by
  refine ⟨fun i => ⟨(i.val + 1) % n, Nat.mod_lt _ (by omega)⟩, ?_⟩
  intro i h
  have hv := congrArg Fin.val h
  dsimp only at hv
  have hi := i.isLt
  by_cases hlt : i.val + 1 < n
  · rw [Nat.mod_eq_of_lt hlt] at hv; omega
  · have h' : i.val + 1 = n := by omega
    rw [h', Nat.mod_self] at hv; omega

/-- R2a core. A linear map `T` that agreed with a "clone" map `Φ` on four points with
`p0 + p2 = p1 + p3` forces, through any linear functional `φ` that reads the clone as `f p ^ 2`
(a product effect on a product state), the identity `a^2 = b^2`. -/
theorem four_point {V W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]
    (T : V →ₗ[ℝ] W) (φ : W →ₗ[ℝ] ℝ) (Φ : V → W) (f : V → ℝ)
    (p0 p1 p2 p3 : V) (hsum : p0 + p2 = p1 + p3)
    (hT0 : T p0 = Φ p0) (hT1 : T p1 = Φ p1) (hT2 : T p2 = Φ p2) (hT3 : T p3 = Φ p3)
    (hφ0 : φ (Φ p0) = f p0 ^ 2) (hφ1 : φ (Φ p1) = f p1 ^ 2)
    (hφ2 : φ (Φ p2) = f p2 ^ 2) (hφ3 : φ (Φ p3) = f p3 ^ 2)
    (c a b : ℝ) (h0 : f p0 = c + a) (h1 : f p1 = c + b) (h2 : f p2 = c - a) (h3 : f p3 = c - b) :
    a ^ 2 = b ^ 2 := by
  have key : φ (T (p0 + p2)) = φ (T (p1 + p3)) := by rw [hsum]
  simp only [map_add] at key
  rw [hT0, hT1, hT2, hT3, hφ0, hφ1, hφ2, hφ3, h0, h1, h2, h3] at key
  nlinarith [key]

/-- R2a. Hence no linear copier exists on the four points whenever `a^2 ≠ b^2`. -/
theorem no_copier_four_point {V W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]
    (φ : W →ₗ[ℝ] ℝ) (Φ : V → W) (f : V → ℝ)
    (p0 p1 p2 p3 : V) (hsum : p0 + p2 = p1 + p3)
    (hφ0 : φ (Φ p0) = f p0 ^ 2) (hφ1 : φ (Φ p1) = f p1 ^ 2)
    (hφ2 : φ (Φ p2) = f p2 ^ 2) (hφ3 : φ (Φ p3) = f p3 ^ 2)
    (c a b : ℝ) (h0 : f p0 = c + a) (h1 : f p1 = c + b) (h2 : f p2 = c - a) (h3 : f p3 = c - b)
    (hab : a ^ 2 ≠ b ^ 2) :
    ¬ ∃ T : V →ₗ[ℝ] W, T p0 = Φ p0 ∧ T p1 = Φ p1 ∧ T p2 = Φ p2 ∧ T p3 = Φ p3 := by
  rintro ⟨T, hT0, hT1, hT2, hT3⟩
  exact hab (four_point T φ Φ f p0 p1 p2 p3 hsum hT0 hT1 hT2 hT3 hφ0 hφ1 hφ2 hφ3 c a b h0 h1 h2 h3)

/-- Round 2 (A9). Every reversible process (a permutation) of a finite world is periodic. -/
theorem perm_periodic {α : Type*} [Fintype α] [DecidableEq α] (σ : Equiv.Perm α) :
    ∃ k : ℕ, 0 < k ∧ σ ^ k = 1 :=
  ⟨orderOf σ, orderOf_pos σ, pow_orderOf_eq_one σ⟩

/-- R3 core. A continuous real family with `g t ^ 2 = 1` and `g 0 = 1` is identically `1` on `[0,1]`:
a connected family of orthogonal maps of a line, starting at the identity, never leaves it. -/
theorem path_sq_one_const (g : ℝ → ℝ) (hg : Continuous g) (hsq : ∀ t, g t ^ 2 = 1) (h0 : g 0 = 1) :
    ∀ t ∈ Set.Icc (0:ℝ) 1, g t = 1 := by
  intro t ht
  by_contra hne
  have hm : g t = -1 := by
    have := hsq t
    have : (g t - 1) * (g t + 1) = 0 := by nlinarith
    rcases mul_eq_zero.mp this with h | h
    · exact absurd (by linarith) hne
    · linarith
  have hsub : Set.Icc (g t) (g 0) ⊆ g '' Set.Icc 0 t :=
    intermediate_value_Icc' ht.1 hg.continuousOn
  have h0mem : (0:ℝ) ∈ Set.Icc (g t) (g 0) := by rw [hm, h0]; constructor <;> norm_num
  obtain ⟨s, -, hs⟩ := hsub h0mem
  have := hsq s
  rw [hs] at this
  norm_num at this

/-- R4a. Stationarity of `J(α) = (1 - cos(β-α))/2 + ρ sin²α / 2` at `α = β/2`
(derivative `-(1/2) sin(β-α) + ρ sin α cos α`) holds iff `ρ = 1/(2 cos(β/2))`. -/
theorem midpoint_rho (β ρ : ℝ) (hc : Real.cos (β / 2) ≠ 0) (hs : Real.sin (β / 2) ≠ 0) :
    (-(1 / 2) * Real.sin (β - β / 2) + ρ * Real.sin (β / 2) * Real.cos (β / 2) = 0) ↔
      ρ = 1 / (2 * Real.cos (β / 2)) := by
  have hb : β - β / 2 = β / 2 := by ring
  rw [hb]
  constructor
  · intro h
    have h2 : Real.sin (β / 2) * (ρ * Real.cos (β / 2) - 1 / 2) = 0 := by linarith
    rcases mul_eq_zero.mp h2 with h3 | h3
    · exact absurd h3 hs
    · field_simp; linarith
  · intro h
    rw [h]; field_simp; ring

end SelfRefRun
