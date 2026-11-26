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
# Composition route: proved-in-model items (theory/RECORD_COST_CHAIN_2026-11-25.md (source: composition route))

* **Lemma P1** (§8): a nondecreasing price `f` on positive integers with
  `f(mn) = f(m) + f(n)` is `f(n) = f(2)·log₂ n`.
* **Q1a** (§3) and the additivity half of **P2** (§8): an additive price `c·log` with c > 0
  forces the count to multiply (`N_AB = N_A·N_B`; for `K`, that is local tomography), and
  the table's failures `log 10 ≠ 2 log 3`, linear K: `16 ≠ 8`, `9 ≠ 6`.
* **Gbit write lemma** (§6, "a proof that sits behind t3"): in a gbit, no linear map can
  write the x = 0 answer onto a blank B while leaving A unchanged.

Not formalized (NUM or LP-based in the note): Q2a's optimal shrink r* = cos(π/n), Q2b's
positivity check of rotations on n-gons, the t2 parameter counts (rebit K_AB = 10), Q3a/Q3b
entropy facts, t3's 128 symmetries.
-/

namespace GTAORnd.Composition

open Real

/-- **Lemma P1.** `f : ℕ → ℝ` nondecreasing on positive integers, completely additive on
positive integers ⇒ `f n = f 2 * log₂ n` for every `n ≥ 1`. -/
theorem P1 (f : ℕ → ℝ) (hmono : ∀ m n, 1 ≤ m → m ≤ n → f m ≤ f n)
    (hadd : ∀ m n, 1 ≤ m → 1 ≤ n → f (m * n) = f m + f n) (n : ℕ) (hn : 1 ≤ n) :
    f n = f 2 * Real.logb 2 n := by
  have h1 : f 1 = 0 := by have := hadd 1 1 le_rfl le_rfl; simp at this; linarith
  have hpow : ∀ m k : ℕ, 1 ≤ m → f (m ^ k) = k * f m := by
    intro m k hm
    induction k with
    | zero => simp [h1]
    | succ k ih =>
      rw [pow_succ, hadd _ _ (Nat.one_le_pow _ _ hm) hm, ih]; push_cast; ring
  have hf2 : 0 ≤ f 2 := by have := hmono 1 2 le_rfl (by norm_num); linarith
  -- for every k ≥ 1: |k f n − k log₂ n f 2| ≤ f 2
  have key : ∀ k : ℕ, 1 ≤ k → |f n - f 2 * Real.logb 2 n| ≤ f 2 / k := by
    intro k hk
    set a := Nat.log 2 (n ^ k) with ha
    have hnk : 1 ≤ n ^ k := Nat.one_le_pow _ _ hn
    have hlo : 2 ^ a ≤ n ^ k := Nat.pow_log_le_self 2 (by omega)
    have hhi : n ^ k < 2 ^ (a + 1) := Nat.lt_pow_succ_log_self (by norm_num) _
    -- price bounds
    have p1 : a * f 2 ≤ k * f n := by
      rw [← hpow 2 a (by norm_num), ← hpow n k hn]
      exact hmono _ _ (Nat.one_le_two_pow) hlo
    have p2 : k * f n ≤ (a + 1) * f 2 := by
      rw [← hpow n k hn]
      have := hmono _ _ hnk hhi.le
      rw [hpow 2 (a + 1) (by norm_num)] at this; push_cast at this; linarith
    -- log bounds
    have hnr : (0 : ℝ) < n := by exact_mod_cast hn
    have l1 : (a : ℝ) ≤ k * Real.logb 2 n := by
      have := Real.logb_le_logb_of_le (b := 2) (by norm_num) (by positivity)
        (show ((2 ^ a : ℕ) : ℝ) ≤ ((n ^ k : ℕ) : ℝ) by exact_mod_cast hlo)
      push_cast at this
      rwa [Real.logb_pow, Real.logb_pow, Real.logb_self_eq_one (by norm_num), mul_one] at this
    have l2 : k * Real.logb 2 n < a + 1 := by
      have := Real.logb_lt_logb (b := 2) (by norm_num) (by positivity)
        (show ((n ^ k : ℕ) : ℝ) < ((2 ^ (a + 1) : ℕ) : ℝ) by exact_mod_cast hhi)
      push_cast at this
      rw [Real.logb_pow, Real.logb_pow, Real.logb_self_eq_one (by norm_num), mul_one] at this
      exact_mod_cast this
    have hk' : (0 : ℝ) < k := by exact_mod_cast hk
    have u1 : (f n - f 2 * Real.logb 2 n) * k ≤ f 2 := by
      nlinarith [mul_nonneg hf2 (sub_nonneg.mpr l1)]
    have u2 : -f 2 ≤ (f n - f 2 * Real.logb 2 n) * k := by
      nlinarith [mul_le_mul_of_nonneg_left l2.le hf2]
    rw [abs_le]; constructor
    · have e : -(f 2 / k) = (-f 2) / k := by ring
      rw [e, div_le_iff₀ hk']; linarith
    · rw [le_div_iff₀ hk']; linarith
  -- conclude
  by_contra hne
  have hpos : 0 < |f n - f 2 * Real.logb 2 n| := abs_pos.mpr (sub_ne_zero.mpr hne)
  obtain ⟨k, hk⟩ := exists_nat_gt (f 2 / |f n - f 2 * Real.logb 2 n|)
  have hk1 : 1 ≤ k := by
    rcases Nat.eq_zero_or_pos k with h | h
    · subst h; simp at hk; linarith [div_nonneg hf2 hpos.le]
    · exact h
  have := key k hk1
  have hk' : (0 : ℝ) < k := by exact_mod_cast hk1
  rw [div_lt_iff₀ hpos] at hk
  rw [le_div_iff₀ hk'] at this
  linarith

/-- **Q1a / P2 (additivity half).** With c > 0, the price `c·log` is additive on a pair iff
the count multiplies. (For N this is Hardy's `N_AB = N_A·N_B`; for K it is local
tomography.) -/
theorem log_additive_iff (c : ℝ) (hc : 0 < c) (nA nB nAB : ℕ) (hA : 0 < nA) (hB : 0 < nB)
    (hAB : 0 < nAB) :
    c * Real.log nAB = c * Real.log nA + c * Real.log nB ↔ nAB = nA * nB := by
  rw [← mul_add, ← Real.log_mul (by positivity) (by positivity)]
  constructor
  · intro h
    have h' := mul_left_cancel₀ hc.ne' h
    have := Real.log_injOn_pos (Set.mem_Ioi.mpr (by positivity : (0:ℝ) < nAB))
      (Set.mem_Ioi.mpr (by positivity : (0:ℝ) < (nA : ℝ) * nB)) h'
    exact_mod_cast this
  · intro h; subst h; push_cast; rfl

/-- **P2 table entries.** rebit pair: `log 10 ≠ 2·log 3`; linear-K pricing fails for the
qubit (16 ≠ 4 + 4) and the gbit (9 ≠ 3 + 3); linear K happens to work at K = 2 (4 = 2 + 2). -/
theorem P2_entries :
    Real.log 10 ≠ 2 * Real.log 3 ∧ (16 : ℕ) ≠ 4 + 4 ∧ (9 : ℕ) ≠ 3 + 3 ∧ (2 * 2 : ℕ) = 2 + 2 := by
  refine ⟨?_, by norm_num, by norm_num, by norm_num⟩
  intro h
  rw [← Real.log_rpow (by norm_num)] at h
  have := Real.log_injOn_pos (Set.mem_Ioi.mpr (by norm_num : (0:ℝ) < 10))
    (Set.mem_Ioi.mpr (by positivity : (0:ℝ) < (3:ℝ) ^ (2:ℝ))) h
  norm_num at this

/-- **Gbit write lemma (behind t3).** States of A in `V`, of B in `U`, composite in `W` with a
bilinear `prod` such that `x ≠ 0 → prod x y = 0 → y = 0` (true for the algebraic tensor
product over a field). The gbit's four deterministic states satisfy the affine dependence
`D₀₀ + D₁₁ = D₀₁ + D₁₀` with `D₁₀ − D₁₁ ≠ 0`. If a linear `T` maps `D_{st} ⊗ β` to
`D_{st} ⊗ B_s` (A unchanged, B gets the x = 0 answer s), then `B₀ = B₁`: the record carries
nothing. -/
theorem gbit_no_local_write {V U W : Type*} [AddCommGroup V] [Module ℝ V] [AddCommGroup U]
    [Module ℝ U] [AddCommGroup W] [Module ℝ W] (prod : V →ₗ[ℝ] U →ₗ[ℝ] W)
    (hprod : ∀ x y, x ≠ 0 → prod x y = 0 → y = 0)
    (D : Fin 2 → Fin 2 → V) (hdep : D 0 0 + D 1 1 = D 0 1 + D 1 0) (hw : D 1 0 - D 1 1 ≠ 0)
    (β : U) (B : Fin 2 → U) (T : W →ₗ[ℝ] W)
    (hT : ∀ s t, T (prod (D s t) β) = prod (D s t) (B s)) : B 0 = B 1 := by
  have h := congrArg (fun v => T (prod v β)) hdep
  simp only [map_add, LinearMap.add_apply, hT] at h
  -- (D00 − D01) ⊗ B0 = (D10 − D11) ⊗ B1, and D00 − D01 = D10 − D11 =: w
  have hw' : D 0 0 - D 0 1 = D 1 0 - D 1 1 := by
    have := hdep; rw [← sub_eq_zero] at this ⊢; rw [← this]; abel
  have h2 : prod (D 1 0 - D 1 1) (B 0 - B 1) = 0 := by
    have e1 : prod (D 0 0 - D 0 1) (B 0) = prod (D 1 0 - D 1 1) (B 1) := by
      simp only [map_sub, LinearMap.sub_apply]
      rw [sub_eq_sub_iff_add_eq_add, h, add_comm]
    rw [hw'] at e1
    simp only [map_sub] at e1 ⊢
    rw [e1, sub_self]
  exact sub_eq_zero.mp (hprod _ _ hw h2)

end GTAORnd.Composition
