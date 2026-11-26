/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Side R&D, record-cost chain: `theory/RECORD_COST_CHAIN_2026-11-25.md`. Moved from a private Lake project
(library `GTAORnd`, same Lean and Mathlib pins). Statements and proofs unchanged; only this
header, the module lines and doc-comment paths differ. Session labels (R2a′, R3, C3, §R3.4, …)
are mapped to the note's steps S1–S10 in its §3.
-/
module

public import GTAO.Rnd.SelfRefRun.Round2

@[expose] public section

/-!
# C3 (Round 2): in d = 3, transitivity + a record that survives the drift leaves only the ball
(theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route), Round 2, C3) — **partial**

Informal (NOTE.md C3): *in d = 3, suppose the reversible group is transitive on pure states
and has a connected drift fixing a distinguishable pure pair. Then Ω is a ball. Proof: the
identity component is normal. If it were SO(2), transitivity would make it fix every pure
state. So it is SO(3).*

What is formalized here: the group-theoretic step, in a sharpened form.
`normal_fixer_bot`: if a group acts **transitively and faithfully** on the pure states, then
any normal subgroup that fixes one pure state is trivial. Applied to the identity component
G₀ (normal in G): G₀ cannot fix any pure state, unless it is trivial; but G₀ contains the
non-trivial connected drift, so G₀ fixes no pure state.

Named assumption NA1 (theory/RECORD_COST_CHAIN_2026-11-25.md §5): the SO(3) classification below is not in
Mathlib and is assumed, not proved, for "Ω is a ball".

Not formalized (open items, see formal/lean/README.md, section RND-RECORD-COST):
* the classification of closed connected subgroups of SO(3) ({1}, conjugates of SO(2),
  SO(3)), which turns "G₀ fixes no pure state" into "G₀ = SO(3)";
* SO(3)-orbit of a pure state = a sphere, and Ω = conv(pure states) (Krein–Milman), giving
  "Ω is a ball" (an ellipsoid; a round ball in the invariant inner product);
* faithfulness on pure states (follows from faithfulness on Ω and Ω = conv(pure states)).
-/

namespace GTAORnd.SelfRef

/-- **C3, group step.** Transitive + faithful action, normal subgroup fixing one point ⇒ the
subgroup is trivial. (Uses the self-reference run's `normal_fixer_trivial`.) -/
theorem normal_fixer_bot {G X : Type*} [Group G] [MulAction G X] [FaithfulSMul G X]
    (H : Subgroup G) [H.Normal] (htrans : ∀ x y : X, ∃ g : G, g • x = y) (x0 : X)
    (hfix : ∀ h ∈ H, h • x0 = x0) : H = ⊥ := by
  rw [Subgroup.eq_bot_iff_forall]
  intro h hh
  apply FaithfulSMul.eq_of_smul_eq_smul (α := X)
  intro y
  rw [one_smul]
  exact SelfRefRun.normal_fixer_trivial H htrans x0 hfix h hh y

/-- **C3, as used.** If the identity component `G₀` (any normal subgroup) contains a
non-identity element, it fixes no pure state. -/
theorem normal_nontrivial_fixes_nothing {G X : Type*} [Group G] [MulAction G X]
    [FaithfulSMul G X] (G₀ : Subgroup G) [G₀.Normal] (htrans : ∀ x y : X, ∃ g : G, g • x = y)
    (hnt : ∃ g ∈ G₀, g ≠ 1) : ∀ x0 : X, ¬ ∀ h ∈ G₀, h • x0 = x0 := by
  intro x0 hfix
  obtain ⟨g, hg, hne⟩ := hnt
  have := normal_fixer_bot G₀ htrans x0 hfix
  rw [this, Subgroup.mem_bot] at hg
  exact hne hg

end GTAORnd.SelfRef
