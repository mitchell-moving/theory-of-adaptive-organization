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

-- Copied verbatim from rnd/selfref/lean/SelfRef/Round2.lean (self-reference run), namespace renamed SelfRef → SelfRefRun to avoid clashing with GTAORnd.SelfRef. Source file left untouched.

/-!
# Round 2 lemmas (private R&D)
- `no_zero_drift_while_recording`: 3c. A tracker whose writes distinguish two data values has no state left
  unchanged by both writes: acquiring information forces self-drift.
- `normal_fixer_trivial`: 3b. If a group acts transitively and a normal subgroup fixes one point, that normal
  subgroup fixes every point. Used with the identity component (normal) of the reversible group.
-/

namespace SelfRefRun

/-- 3c. If writing datum `d` and datum `d'` always leave the tracker in different states
(the write records which datum arrived), no tracker state is a fixed point of both writes. -/
theorem no_zero_drift_while_recording {R D : Type*} (w : D → R → R) (d d' : D)
    (hrec : ∀ x, w d x ≠ w d' x) : ¬ ∃ x, w d x = x ∧ w d' x = x := by
  rintro ⟨x, h1, h2⟩
  exact hrec x (h1.trans h2.symm)

/-- 3b. Transitive action + a normal subgroup fixing one point ⇒ that subgroup fixes all points. -/
theorem normal_fixer_trivial {G X : Type*} [Group G] [MulAction G X] (H : Subgroup G) [H.Normal]
    (htrans : ∀ x y : X, ∃ g : G, g • x = y) (x0 : X) (hfix : ∀ h ∈ H, h • x0 = x0) :
    ∀ h ∈ H, ∀ y : X, h • y = y := by
  intro h hh y
  obtain ⟨g, rfl⟩ := htrans x0 y
  have hconj : g⁻¹ * h * g ∈ H := by
    have := (inferInstance : H.Normal).conj_mem h hh g⁻¹
    simpa [mul_assoc] using this
  have := hfix _ hconj
  calc h • g • x0 = g • ((g⁻¹ * h * g) • x0) := by simp [mul_smul]
    _ = g • x0 := by rw [this]

end SelfRefRun
