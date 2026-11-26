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
# Self-reference, piece 1 (theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route) R1b, R1d, R1e)

* **R1d** (the liar-loop / flipped self-referential bit): if a flip `T` swaps the two
  outcomes of a two-outcome effect (`e ∘ T = 1 − e`) and `ω` is a fixed state (`T ω = ω`),
  then `e ω = 1/2`. Stated for an arbitrary state set and an arbitrary real-valued effect:
  no convexity, no linearity, no physics.
* **R1b** deterministic finite worlds with ≥ 2 states have a fixed-point-free process, so
  they cannot close every feedback loop consistently.
* **R1e** the sharp-record copier, extended linearly, does not clone the fair coin
  `u = (½, ½)`, yet both of its marginals equal `u` (classical broadcasting survives).
-/

namespace GTAORnd.SelfRef

/-- **R1d.** A state fixed by an outcome-flipping process has outcome probability 1/2. -/
theorem liar_half {Ω : Type*} (e : Ω → ℝ) (T : Ω → Ω) (hflip : ∀ x, e (T x) = 1 - e x)
    (ω : Ω) (hfix : T ω = ω) : e ω = 1 / 2 := by
  have h := hflip ω
  rw [hfix] at h
  linarith

/-- R1d, consequence: a flip on a deterministic (sharp, values in {0,1}) record has no fixed
state. -/
theorem sharp_flip_no_fixed {Ω : Type*} (e : Ω → ℝ) (T : Ω → Ω)
    (hflip : ∀ x, e (T x) = 1 - e x) (hsharp : ∀ x, e x = 0 ∨ e x = 1) (ω : Ω) :
    T ω ≠ ω := by
  intro hfix
  have := liar_half e T hflip ω hfix
  rcases hsharp ω with h | h <;> rw [h] at this <;> norm_num at this

/-- **R1b.** For every n ≥ 2 there is a process on n deterministic states with no fixed
state (a cyclic shift; NOT for n = 2). -/
theorem exists_fixedPointFree (n : ℕ) (hn : 2 ≤ n) : ∃ f : Fin n → Fin n, ∀ x, f x ≠ x := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  refine ⟨fun x => x + 1, fun x h => ?_⟩
  have : (1 : Fin (m + 2)) = 0 := by
    have := congrArg (· - x) h
    simp at this
  exact absurd this (by simp)

/-- the linear extension of the sharp copier `δᵢ ↦ δᵢ ⊗ δᵢ` on a classical bit -/
def sharpCopy (p : Fin 2 → ℝ) : Fin 2 → Fin 2 → ℝ := fun i j => if i = j then p i else 0

/-- **R1e.** `sharpCopy` clones the sharp states, does not clone `u = (½,½)`, and both
marginals of `sharpCopy u` equal `u`. -/
theorem sharpCopy_facts :
    (∀ k : Fin 2, sharpCopy (fun i => if i = k then 1 else 0) =
        fun i j => (if i = k then (1:ℝ) else 0) * (if j = k then 1 else 0)) ∧
    sharpCopy (fun _ => 1 / 2) ≠ (fun _ _ => (1 / 2 : ℝ) * (1 / 2)) ∧
    (∀ i, ∑ j, sharpCopy (fun _ => 1 / 2) i j = 1 / 2) ∧
    (∀ j, ∑ i, sharpCopy (fun _ => 1 / 2) i j = 1 / 2) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro k; funext i j; unfold sharpCopy
    by_cases hij : i = j
    · subst hij; by_cases hik : i = k <;> simp [hik]
    · by_cases hik : i = k
      · subst hik; simp [hij, Ne.symm hij]
      · simp [hij, hik]
  · intro h
    have := congrFun (congrFun h 0) 1
    simp [sharpCopy] at this
  · intro i; fin_cases i <;> simp [sharpCopy]
  · intro j; fin_cases j <;> simp [sharpCopy]

end GTAORnd.SelfRef
