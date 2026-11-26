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
# Spekkens' elementary system: cloning by ontic permutations (theory/RECORD_COST_CHAIN_2026-11-25.md (source: nocloning route) R(a)1–2)

Ontic states `Fin 4` (the note's 1,2,3,4 are 0,1,2,3 here). An epistemic state is a set of
ontic states; the 6 pure epistemic states are the 2-element subsets. The blank is `{0,1}`
(the note's `{1,2}`), as in `scripts/spekkens_clone.py`. A cloner is a map `f` on joint
ontic states with `f(S × B) = S × S` for every state `S` in the family.

* **R(a)1** no *injective* map (in particular no permutation) clones the 6 pure states; the
  obstruction is local: inputs (0,0) and (0,1) are both forced to (0,0). (We prove the
  stronger statement that only the inclusion `f(S × B) ⊆ S × S` is needed.)
* **R(a)2** the disjoint pair `{0,1}, {2,3}` is cloned by an explicit permutation; the four
  singletons (knowledge balance lifted) are cloned, with blank `{0}`, by the CNOT-like
  permutation `(a, b) ↦ (a, b + a)`.
-/

namespace GTAORnd.Spekkens

abbrev O := Fin 4

/-- the 6 pure epistemic states -/
def pure : Finset (Finset O) := (Finset.univ : Finset O).powersetCard 2

def blank : Finset O := {0, 1}

/-- **R(a)1, local obstruction.** -/
theorem forced (f : O × O → O × O)
    (hf : ∀ S ∈ pure, ∀ a ∈ S, ∀ b ∈ blank, f (a, b) ∈ S ×ˢ S) :
    f (0, 0) = (0, 0) ∧ f (0, 1) = (0, 0) := by
  have key : ∀ p : O × O, p ∈ ({0, 1} : Finset O) ×ˢ ({0, 1} : Finset O) →
      p ∈ ({0, 2} : Finset O) ×ˢ ({0, 2} : Finset O) →
      p ∈ ({0, 3} : Finset O) ×ˢ ({0, 3} : Finset O) → p = (0, 0) := by decide
  have m1 : ({0, 1} : Finset O) ∈ pure := by decide
  have m2 : ({0, 2} : Finset O) ∈ pure := by decide
  have m3 : ({0, 3} : Finset O) ∈ pure := by decide
  constructor
  · exact key _ (hf _ m1 0 (by decide) 0 (by decide)) (hf _ m2 0 (by decide) 0 (by decide))
      (hf _ m3 0 (by decide) 0 (by decide))
  · exact key _ (hf _ m1 0 (by decide) 1 (by decide)) (hf _ m2 0 (by decide) 1 (by decide))
      (hf _ m3 0 (by decide) 1 (by decide))

/-- **R(a)1.** No injective map on joint ontic states satisfies even the inclusion
`f(S × B) ⊆ S × S` for all 6 pure epistemic states. -/
theorem no_injective_clone (f : O × O → O × O) (hinj : Function.Injective f)
    (hf : ∀ S ∈ pure, ∀ a ∈ S, ∀ b ∈ blank, f (a, b) ∈ S ×ˢ S) : False := by
  have h := forced f hf
  have := hinj (h.1.trans h.2.symm)
  simp at this

/-- **R(a)1, permutation form** (as in the note): no permutation `σ` of joint ontic states
satisfies `σ(S × B) = S × S` for all 6 pure states. -/
theorem no_perm_clone (σ : Equiv.Perm (O × O)) :
    ¬ ∀ S ∈ pure, (S ×ˢ blank).image σ = S ×ˢ S := by
  intro h
  have hf : ∀ S ∈ pure, ∀ a ∈ S, ∀ b ∈ blank, σ (a, b) ∈ S ×ˢ S := by
    intro S hS a ha b hb
    rw [← h S hS]
    exact Finset.mem_image_of_mem σ (Finset.mem_product.mpr ⟨ha, hb⟩)
  have := forced σ hf
  have := σ.injective (this.1.trans this.2.symm)
  simp at this

/-- the permutation cloning the disjoint pair {0,1}, {2,3} -/
def σdisj (p : O × O) : O × O := if 2 ≤ p.1.val then (p.1, p.2 + 2) else p

theorem σdisj_involutive : Function.Involutive σdisj := by
  unfold Function.Involutive; decide

/-- **R(a)2, disjoint pair.** -/
theorem disjoint_pair_clonable :
    ∀ S ∈ ({{0, 1}, {2, 3}} : Finset (Finset O)),
      (S ×ˢ blank).image σdisj_involutive.toPerm = S ×ˢ S := by decide

/-- the CNOT-like permutation `(a, b) ↦ (a, b + a)` -/
def cnot : Equiv.Perm (O × O) where
  toFun p := (p.1, p.2 + p.1)
  invFun p := (p.1, p.2 - p.1)
  left_inv p := by simp
  right_inv p := by simp

/-- **R(a)2, singletons (knowledge balance lifted).** With blank `{0}`, the CNOT-like
permutation clones every singleton. -/
theorem singletons_clonable :
    ∀ a : O, (({a} : Finset O) ×ˢ ({0} : Finset O)).image cnot = ({a} : Finset O) ×ˢ ({a} : Finset O) := by decide

end GTAORnd.Spekkens
