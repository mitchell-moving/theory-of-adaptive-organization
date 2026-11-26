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
# Self-reference, piece 2: drift-moved orbits are not uniformly copyable
(theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route) R2a, R2b)

**Status:** the single-frequency theorem here is correct as stated, but it is the round-1
shortcut. The general statement (any integer weights) is R2a′, formalized in
`CircleOrbit.lean` (`no_linear_clone_circle`), which supersedes `no_linear_clone_orbit`.
R2b (measure-and-prepare) below is unaffected.

Frame (NOTE.md §1): states live in a real vector space `V` (the GPT state cone's span),
effects are linear functionals `f ∈ E` that **separate** states, the composite contains
product states `x ⊗ y` given by a bilinear map `prod`, and every effect `f ∈ E` has a
product effect `f ⊗ f` on the composite with `(f ⊗ f)(x ⊗ y) = f x · f y`.
"The results hold for any composite rule": only these properties are used.

**Formal R2a (single-frequency form).** If the drift moves a state along the orbit
`t ↦ c + cos t • A + sin t • B` (a rotation in one plane, or several planes at the *same*
frequency), then no linear map whatsoever — positive or not — clones every state on that
orbit, unless `A = B = 0`, i.e. the orbit is a single point (the drift fixes the state).

Gap vs the note: the note covers any one-parameter subgroup of a compact connected group,
whose orbit may mix several rotation planes with *different* frequencies. The note's
quarter-phase proof does not go through verbatim in that case (a quarter turn in one plane
is not a quarter turn in the others, so `p₀ + p₂ = p₁ + p₃` can fail). See formal/lean/README.md, section RND-RECORD-COST.
-/

namespace GTAORnd.SelfRef

open Real

variable {V W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup W] [Module ℝ W]

/-- the drift orbit through a moved state -/
noncomputable def orbit (c A B : V) (t : ℝ) : V := c + Real.cos t • A + Real.sin t • B

lemma orbit_sum (c A B : V) (s : ℝ) :
    orbit c A B s + orbit c A B (s + π) =
      orbit c A B (s + π / 2) + orbit c A B (s + π / 2 + π) := by
  simp only [orbit, Real.cos_add_pi, Real.sin_add_pi, Real.cos_add_pi_div_two,
    Real.sin_add_pi_div_two, neg_smul, neg_neg]
  abel

/-- **R2a (single-frequency form).** -/
theorem no_linear_clone_orbit (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) (E : Set (Module.Dual ℝ V))
    (hprod : ∀ f ∈ E, ∃ Ff : Module.Dual ℝ W, ∀ x y, Ff (prod x y) = f x * f y)
    (hsep : ∀ v : V, (∀ f ∈ E, f v = 0) → v = 0)
    (c A B : V) (T : V →ₗ[ℝ] W)
    (hT : ∀ t, T (orbit c A B t) = prod (orbit c A B t) (orbit c A B t)) :
    A = 0 ∧ B = 0 := by
  have key : ∀ f ∈ E, f A = 0 ∧ f B = 0 := by
    intro f hf
    obtain ⟨Ff, hFf⟩ := hprod f hf
    have hs : ∀ s, (f (orbit c A B s)) ^ 2 + (f (orbit c A B (s + π))) ^ 2 =
        (f (orbit c A B (s + π / 2))) ^ 2 + (f (orbit c A B (s + π / 2 + π))) ^ 2 := by
      intro s
      have h := congrArg (fun v => Ff (T v)) (orbit_sum c A B s)
      simp only [map_add, hT, hFf] at h
      nlinarith [h]
    have hf_orb : ∀ t, f (orbit c A B t) = f c + Real.cos t * f A + Real.sin t * f B := by
      intro t; simp [orbit, map_add, map_smul]
    have h0 := hs 0
    have h4 := hs (π / 4)
    simp only [hf_orb, Real.cos_add_pi, Real.sin_add_pi, Real.cos_add_pi_div_two,
      Real.sin_add_pi_div_two, Real.cos_zero, Real.sin_zero, Real.cos_pi_div_four,
      Real.sin_pi_div_four, zero_add, Real.cos_pi, Real.sin_pi, Real.cos_pi_div_two,
      Real.sin_pi_div_two] at h0 h4
    have hsq : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    have e1 : f A ^ 2 = f B ^ 2 := by nlinarith [h0]
    have e2 : f A * f B = 0 := by nlinarith [h4, hsq]
    have hA : f A = 0 := by
      have : f A ^ 2 * f A ^ 2 = 0 := by
        calc f A ^ 2 * f A ^ 2 = f A ^ 2 * f B ^ 2 := by rw [e1]
          _ = (f A * f B) ^ 2 := by ring
          _ = 0 := by rw [e2]; ring
      have : f A ^ 2 = 0 := by simpa using this
      exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
    refine ⟨hA, ?_⟩
    have : f B ^ 2 = 0 := by rw [← e1, hA]; ring
    exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
  exact ⟨hsep A fun f hf => (key f hf).1, hsep B fun f hf => (key f hf).2⟩

/-- R2a, contrapositive form: if the drift actually moves the state (the orbit is not a
single point), no linear map clones the whole orbit. -/
theorem no_linear_clone_moved (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) (E : Set (Module.Dual ℝ V))
    (hprod : ∀ f ∈ E, ∃ Ff : Module.Dual ℝ W, ∀ x y, Ff (prod x y) = f x * f y)
    (hsep : ∀ v : V, (∀ f ∈ E, f v = 0) → v = 0)
    (c A B : V) (hmoved : ∃ t, orbit c A B t ≠ orbit c A B 0) :
    ¬ ∃ T : V →ₗ[ℝ] W, ∀ t, T (orbit c A B t) = prod (orbit c A B t) (orbit c A B t) := by
  rintro ⟨T, hT⟩
  obtain ⟨hA, hB⟩ := no_linear_clone_orbit prod E hprod hsep c A B T hT
  obtain ⟨t, ht⟩ := hmoved
  exact ht (by simp [orbit, hA, hB])

/-- **R2b.** Jointly perfectly distinguishable states are cloned by the measure-and-prepare
map `M x = ∑ᵢ eᵢ(x) · (ωᵢ ⊗ ωᵢ)`, which is linear. -/
theorem measure_prepare_clones (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) {N : ℕ} (ω : Fin N → V)
    (e : Fin N → Module.Dual ℝ V) (hδ : ∀ i j, e i (ω j) = if i = j then 1 else 0) :
    ∃ M : V →ₗ[ℝ] W, ∀ j, M (ω j) = prod (ω j) (ω j) := by
  refine ⟨∑ i, (e i).smulRight (prod (ω i) (ω i)), fun j => ?_⟩
  simp [LinearMap.sum_apply, hδ]

/-- **R2b, covariance.** If a drift element `g` fixes each `ωᵢ`, leaves each effect `eᵢ`
invariant, and acts on the composite as `g ⊗ g` on product states, then the
measure-and-prepare copier commutes with it. (The note says the copier "commutes with G";
the invariance of the effects is an explicit hypothesis here — for a compact G it can be
arranged by Haar-averaging the effects, which is not formalized.) -/
theorem measure_prepare_covariant (prod : V →ₗ[ℝ] V →ₗ[ℝ] W) {N : ℕ} (ω : Fin N → V)
    (e : Fin N → Module.Dual ℝ V) (g : V →ₗ[ℝ] V) (gW : W →ₗ[ℝ] W)
    (hgW : ∀ x y, gW (prod x y) = prod (g x) (g y)) (hfix : ∀ i, g (ω i) = ω i)
    (hinv : ∀ i x, e i (g x) = e i x) (x : V) :
    gW ((∑ i, (e i).smulRight (prod (ω i) (ω i))) x) =
      (∑ i, (e i).smulRight (prod (ω i) (ω i))) (g x) := by
  simp [LinearMap.sum_apply, map_sum, hgW, hfix, hinv]

end GTAORnd.SelfRef
