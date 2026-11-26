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
# Positive control for `CopyModel`: the axioms do not forbid cloning by themselves

Adversarial check for Lemma B1: if the `CopyModel` fields alone ruled out every cloner, the
lemma would say nothing. Here is a model (one-point state space, all channels allowed) in
which a cloner exists. So "no cloner" in Lemma B1 really comes from its hypotheses
(capacity < M plus sharp separating effects), not from the frame.
-/

namespace GTAORnd

/-- a one-state system: every n-fold composite is a single point -/
def unitModel : CopyModel where
  St _ := Unit
  Meas _ ι _ := {m | ∀ s, ∑ i, m i s = 1}
  Chan _ _ := Set.univ
  prod _ _ := ()
  prod_one _ := rfl
  meas_sum hm s := hm s
  chan_id _ := trivial
  chan_comp _ _ := trivial
  meas_pullback hM _ := fun s => hM _
  prod_meas n e he := ⟨fun b _ => ∏ j, e j (b j) (), fun _ => by
      have := Finset.prod_univ_sum (fun _ : Fin n => (Finset.univ : Finset (Fin 2)))
        (fun j c => e j c ())
      rw [Fintype.piFinset_univ] at this
      rw [← this]
      exact Finset.prod_eq_one fun j _ => he j (), fun _ _ => rfl⟩
  local_ext _ _ _ := ⟨fun _ => (), trivial, fun _ _ _ _ => rfl⟩

/-- In `unitModel` the (only) state is cloned into 2 copies by an allowed channel. -/
theorem unitModel_clones : ∃ T, unitModel.Clones 2 T (fun _ : Fin 1 => ()) :=
  ⟨fun _ => (), trivial, fun _ => rfl⟩

end GTAORnd
