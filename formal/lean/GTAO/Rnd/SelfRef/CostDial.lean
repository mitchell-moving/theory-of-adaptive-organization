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
# Self-reference, piece 4: the cost dial (theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route) R4a)

Model (NOTE.md R4, a stated toy; the refresh term is a modelling choice):
`J(α) = qκ·(1 − cos(β − α))/2 + wRD·sin²α`, the record basis at angle α from the conserved
axis, stakes at angle β, R readers, diffusion D.

Informal R4a: *the stationarity condition is ½ sin(β−α) = ρ sinα cosα, with ρ = 2wRD/(qκ);
as ρ → 0, α* → β; as ρ → ∞, α* → 0; α* = β/2 exactly at ρ = 1/(2cos(β/2)); for β = 60°
that is ρ = 0.577.*

Formalized: the derivative of J; stationarity ⇔ the stated condition (for qκ > 0); the
midpoint closed form in both directions (for 0 < β < π); the β = 60° value 1/√3 ∈ (0.577,
0.578); and the ρ = 0 endpoint (the only stationary point in [0, β] is α = β).
Not formalized: the ρ → ∞ limit, and that the stationary point is the *global minimizer*
α* of J (the note's α* is the minimizer). See formal/lean/README.md, section RND-RECORD-COST.
-/

namespace GTAORnd.SelfRef

open Real

/-- the cost dial -/
noncomputable def Jdial (qk wRD β α : ℝ) : ℝ := qk * (1 - Real.cos (β - α)) / 2 + wRD * Real.sin α ^ 2

/-- derivative of the dial in α -/
theorem Jdial_hasDerivAt (qk wRD β α : ℝ) :
    HasDerivAt (Jdial qk wRD β) (-(qk / 2) * Real.sin (β - α) +
      wRD * (2 * Real.sin α * Real.cos α)) α := by
  have h1 : HasDerivAt (fun a => Real.cos (β - a)) (Real.sin (β - α)) α := by
    have := ((hasDerivAt_id α).const_sub β).cos
    simpa using this
  have h2 : HasDerivAt (fun a => Real.sin a ^ 2) (2 * Real.sin α * Real.cos α) α := by
    convert (Real.hasDerivAt_sin α).pow 2 using 1
    push_cast; ring
  have := ((h1.const_sub 1).const_mul qk |>.div_const 2).add (h2.const_mul wRD)
  show HasDerivAt (fun a => qk * (1 - Real.cos (β - a)) / 2 + wRD * Real.sin a ^ 2) _ α
  exact this.congr_deriv (by ring)

/-- **R4a stationarity.** For qκ > 0: `J'(α) = 0 ↔ ½ sin(β−α) = ρ sinα cosα`,
`ρ = 2wRD/(qκ)`. -/
theorem Jdial_stationary_iff (qk wRD β α : ℝ) (hq : 0 < qk) :
    deriv (Jdial qk wRD β) α = 0 ↔
      (1 / 2) * Real.sin (β - α) = (2 * wRD / qk) * Real.sin α * Real.cos α := by
  rw [(Jdial_hasDerivAt qk wRD β α).deriv]
  constructor
  · intro h
    field_simp
    linarith
  · intro h
    field_simp at h
    linarith

/-- **R4a midpoint.** For 0 < β < π: α = β/2 is stationary iff ρ = 1/(2 cos(β/2)). -/
theorem Jdial_midpoint (qk wRD β : ℝ) (hq : 0 < qk) (hβ0 : 0 < β) (hβπ : β < π) :
    deriv (Jdial qk wRD β) (β / 2) = 0 ↔ 2 * wRD / qk = 1 / (2 * Real.cos (β / 2)) := by
  rw [Jdial_stationary_iff qk wRD β (β / 2) hq]
  have hs : 0 < Real.sin (β / 2) := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hc : 0 < Real.cos (β / 2) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hβ : β - β / 2 = β / 2 := by ring
  rw [hβ]
  constructor
  · intro h
    field_simp
    have : Real.sin (β / 2) * (1 - 2 * (2 * wRD / qk) * Real.cos (β / 2)) = 0 := by linarith
    rcases mul_eq_zero.mp this with h' | h'
    · linarith
    · field_simp at h'; linarith
  · intro h
    rw [h]
    field_simp

/-- **R4a, β = 60°.** The midpoint value is ρ = 1/(2 cos 30°) = 1/√3 ≈ 0.577. -/
theorem Jdial_midpoint_60 : 1 / (2 * Real.cos (π / 3 / 2)) = 1 / Real.sqrt 3 := by
  have : π / 3 / 2 = π / 6 := by ring
  rw [this, Real.cos_pi_div_six]
  ring

/-- numerical bracket: 0.577 < 1/√3 < 0.578 -/
theorem inv_sqrt3_bracket : 0.577 < 1 / Real.sqrt 3 ∧ 1 / Real.sqrt 3 < 0.578 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hpos : 0 < Real.sqrt 3 := by positivity
  constructor
  · rw [lt_div_iff₀ hpos]; nlinarith
  · rw [div_lt_iff₀ hpos]; nlinarith

/-- **R4a, ρ = 0 endpoint.** With no refresh cost (wRD = 0) and 0 ≤ β < π, the only
stationary point in [0, β] is α = β (record the stakes). -/
theorem Jdial_rho_zero (qk β α : ℝ) (hq : 0 < qk) (hβπ : β < π) (hα0 : 0 ≤ α) (hαβ : α ≤ β) :
    deriv (Jdial qk 0 β) α = 0 ↔ α = β := by
  rw [Jdial_stationary_iff qk 0 β α hq]
  simp only [mul_zero, zero_div, zero_mul]
  constructor
  · intro h
    have h' : Real.sin (β - α) = 0 := by linarith
    rw [Real.sin_eq_zero_iff_of_lt_of_lt (by linarith [Real.pi_pos]) (by linarith)] at h'
    linarith
  · rintro rfl; simp

end GTAORnd.SelfRef
