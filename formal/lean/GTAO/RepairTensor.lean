/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
The product argument for the repair floor, from
`theory/RECORD_REPAIR_FLOOR_2026-11-23.md:59-65, 73-75`. OPEN_WORK LEAN-PHYS (T63).
-/
module

public import GTAO.RepairFloor
public import GTAO.FiniteFloorPairwise
public import Mathlib.Data.Fin.Tuple.Basic
public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# The product argument on `{0,1}^n`

`theory/RECORD_REPAIR_FLOOR_2026-11-23.md` §3, Step 3. For independent
carriers that each leak at rate at least `Γ`, the leak entropy production
of any strictly positive distribution on `{0,1}^n` is at least
`4 Γ D(p ‖ uniform)`, for every `n`.

The proof here is an induction on `n`. Split off the first carrier. The
divergence from uniform obeys the chain rule. The leak terms of the other
carriers are homogeneous of degree one, so they are the conditional
slices weighted by the first carrier's marginal. The first carrier's
term, summed over the other carriers, is at least its value on that
marginal (superadditivity of `(a-b) log(a/b)`), and on one carrier the
batch 2 comparison `L ≥ 4 (log 2 - h)` applies. This route is not the
entropy-subadditivity route written in the note; it reaches the same
inequality.

Strict positivity of `p` is a hypothesis. A zero atom next to a positive
atom makes the note's `σ` infinite, and `Real.log 0 = 0` would not give
that value.
-/

@[expose] public section

namespace RepairTensor

open HeatFloor RepairFloor FiniteFloor
open scoped BigOperators

/-- Flip carrier `i` of the pattern `x`. -/
def flipAt {n : ℕ} (i : Fin n) (x : Fin n → Bool) : Fin n → Bool :=
  Function.update x i (!x i)

/-- Leak entropy production `σ_Γ[p]`. Each unordered edge `{x, x^(i)}` is
counted once: the ordered sum counts it twice, and the factor `1/2` undoes
that. Lines 59-65. -/
noncomputable def cubeSigma {n : ℕ} (Γ : Fin n → ℝ) (p : (Fin n → Bool) → ℝ) : ℝ :=
  (1 / 2) * ∑ i, Γ i * ∑ x, (p x - p (flipAt i x)) * Real.log (p x / p (flipAt i x))

/-- `D(p ‖ uniform) = Σ p log(p 2^n)` on `{0,1}^n`. -/
noncomputable def cubeD {n : ℕ} (p : (Fin n → Bool) → ℝ) : ℝ :=
  ∑ x, p x * Real.log (p x * 2 ^ n)

lemma flipAt_zero_cons {n : ℕ} (b : Bool) (y : Fin n → Bool) :
    flipAt 0 (Fin.cons b y : Fin (n + 1) → Bool) = Fin.cons (!b) y := by
  unfold flipAt
  rw [Fin.cons_zero, Fin.update_cons_zero]

lemma flipAt_succ_cons {n : ℕ} (i : Fin n) (b : Bool) (y : Fin n → Bool) :
    flipAt i.succ (Fin.cons b y : Fin (n + 1) → Bool) = Fin.cons b (flipAt i y) := by
  unfold flipAt
  rw [Fin.cons_succ, ← Fin.cons_update]

lemma sum_cube_succ {n : ℕ} (f : (Fin (n + 1) → Bool) → ℝ) :
    ∑ x, f x = ∑ b : Bool, ∑ y : Fin n → Bool, f (Fin.cons b y) := by
  rw [← (Fin.consEquiv fun _ => Bool).sum_comp, Fintype.sum_prod_type]
  rfl

/-- Each edge term is homogeneous of degree one. -/
lemma cubeSigma_smul {n : ℕ} (Γ : Fin n → ℝ) {c : ℝ} (hc : 0 < c) {f : (Fin n → Bool) → ℝ}
    (hf : ∀ x, 0 < f x) : cubeSigma Γ (fun x => c * f x) = c * cubeSigma Γ f := by
  unfold cubeSigma
  have hterm : ∀ i x, (c * f x - c * f (flipAt i x)) * Real.log (c * f x / (c * f (flipAt i x))) =
      c * ((f x - f (flipAt i x)) * Real.log (f x / f (flipAt i x))) := by
    intro i x
    have : c * f x / (c * f (flipAt i x)) = f x / f (flipAt i x) := by
      have := hf (flipAt i x)
      field_simp
    rw [this]; ring
  simp_rw [hterm, ← Finset.mul_sum]
  rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  ring

/-- Splitting off the first carrier. -/
lemma cubeSigma_succ {n : ℕ} (Γ : Fin (n + 1) → ℝ) (p : (Fin (n + 1) → Bool) → ℝ) :
    cubeSigma Γ p =
      Γ 0 * ∑ y : Fin n → Bool, (p (Fin.cons false y) - p (Fin.cons true y)) *
          Real.log (p (Fin.cons false y) / p (Fin.cons true y)) +
        ∑ b : Bool, cubeSigma (fun i => Γ i.succ) (fun y => p (Fin.cons b y)) := by
  unfold cubeSigma
  rw [Fin.sum_univ_succ]
  simp_rw [sum_cube_succ (fun x => (p x - p (flipAt _ x)) * Real.log (p x / p (flipAt _ x))),
    flipAt_zero_cons, flipAt_succ_cons]
  have hflip : ∀ (u v : ℝ), (v - u) * Real.log (v / u) = (u - v) * Real.log (u / v) := by
    intro u v
    rw [show v / u = (u / v)⁻¹ by rw [inv_div], Real.log_inv]; ring
  simp only [Fintype.sum_bool, Bool.not_true, Bool.not_false]
  simp_rw [hflip (p (Fin.cons false _)) (p (Fin.cons true _))]
  rw [mul_add]
  congr 1
  · ring
  · have key : ∀ f g : Fin n → ℝ, 1 / 2 * ∑ i, Γ i.succ * (f i + g i) =
        1 / 2 * ∑ i, Γ i.succ * f i + 1 / 2 * ∑ i, Γ i.succ * g i := by
      intro f g
      rw [← mul_add, ← Finset.sum_add_distrib]
      congr 1
      exact Finset.sum_congr rfl fun i _ => by ring
    exact key _ _

/-- One carrier with masses `m₀, m₁`: `4 D(m ‖ u) ≤ (m₀ - m₁) log(m₀/m₁)`.
This is `L(ε) ≥ 4 (log 2 - h(ε))` of batch 2 written on both sides of `1/2`.
Line 73. -/
lemma one_carrier_bound {m0 m1 : ℝ} (h0 : 0 < m0) (h1 : 0 < m1) (hs : m0 + m1 = 1) :
    4 * (m0 * Real.log (m0 * 2) + m1 * Real.log (m1 * 2)) ≤
      (m0 - m1) * Real.log (m0 / m1) := by
  have key : ∀ {a b : ℝ}, 0 < a → 0 < b → a + b = 1 → b ≤ 1 / 2 →
      4 * (a * Real.log (a * 2) + b * Real.log (b * 2)) ≤ (a - b) * Real.log (a / b) := by
    intro a b ha hb hab hb2
    have hL := L_ge_four_entropy hb hb2
    have ha' : a = 1 - b := by linarith
    unfold fairInfo binaryEntropy L at hL
    rw [ha', Real.log_mul (by linarith) (by norm_num), Real.log_mul hb.ne' (by norm_num)]
    have : 1 - b - b = 1 - 2 * b := by ring
    rw [this]
    nlinarith [hL]
  rcases le_total m1 (1 / 2) with hm | hm
  · exact key h0 h1 hs hm
  · have := key h1 h0 (by linarith) (by linarith)
    have hflip : (m1 - m0) * Real.log (m1 / m0) = (m0 - m1) * Real.log (m0 / m1) := by
      rw [show m1 / m0 = (m0 / m1)⁻¹ by rw [inv_div], Real.log_inv]; ring
    linarith

/-- Chain rule for `D(p ‖ uniform)`, splitting off the first carrier. -/
lemma cubeD_succ {n : ℕ} {p : (Fin (n + 1) → Bool) → ℝ} (hp : ∀ x, 0 < p x) :
    cubeD p = ∑ b : Bool, ((∑ y, p (Fin.cons b y)) * Real.log ((∑ y, p (Fin.cons b y)) * 2) +
      (∑ y, p (Fin.cons b y)) * cubeD (fun y => p (Fin.cons b y) / ∑ y', p (Fin.cons b y'))) := by
  unfold cubeD
  rw [sum_cube_succ]
  refine Finset.sum_congr rfl fun b _ => ?_
  set m := ∑ y, p (Fin.cons b y) with hm
  have hmpos : 0 < m := Finset.sum_pos (fun y _ => hp _) Finset.univ_nonempty
  rw [Finset.mul_sum, hm, Finset.sum_mul, ← hm, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun y _ => ?_
  have hq := hp (Fin.cons b y)
  have h1 : p (Fin.cons b y) * 2 ^ (n + 1) = (m * 2) * (p (Fin.cons b y) / m * 2 ^ n) := by
    field_simp; ring
  rw [h1, Real.log_mul (by positivity) (by positivity)]
  field_simp

/-- Product argument. For a strictly positive probability `p` on `{0,1}^n`
and leak rates `Γ_i ≥ g ≥ 0`, `4 g D(p ‖ uniform) ≤ σ_Γ[p]`, for every `n`.
Line 75. -/
theorem cube_tensorization : ∀ (n : ℕ) (Γ : Fin n → ℝ) {g : ℝ}, 0 ≤ g → (∀ i, g ≤ Γ i) →
    ∀ p : (Fin n → Bool) → ℝ, (∀ x, 0 < p x) → ∑ x, p x = 1 →
      4 * g * cubeD p ≤ cubeSigma Γ p := by
  intro n
  induction n with
  | zero =>
    intro Γ g _ _ p _ hsum
    have hD : cubeD p = 0 := by
      unfold cubeD
      rw [Fintype.sum_unique] at hsum
      rw [Fintype.sum_unique, hsum]
      simp
    have hS : cubeSigma Γ p = 0 := by simp [cubeSigma]
    rw [hD, hS]; simp
  | succ n ih =>
    intro Γ g hg hΓ p hp hsum
    set m : Bool → ℝ := fun b => ∑ y, p (Fin.cons b y) with hmdef
    have hmpos : ∀ b, 0 < m b := fun b =>
      Finset.sum_pos (fun y _ => hp _) Finset.univ_nonempty
    have hmsum : m false + m true = 1 := by
      rw [sum_cube_succ, Fintype.sum_bool] at hsum
      simp only [hmdef]; linarith
    set c : Bool → (Fin n → Bool) → ℝ := fun b y => p (Fin.cons b y) / m b with hcdef
    have hcpos : ∀ b y, 0 < c b y := fun b y => div_pos (hp _) (hmpos b)
    have hcsum : ∀ b, ∑ y, c b y = 1 := by
      intro b
      simp only [hcdef]
      rw [← Finset.sum_div, div_self (hmpos b).ne']
    have hih : ∀ b, 4 * g * cubeD (c b) ≤ cubeSigma (fun i => Γ i.succ) (c b) :=
      fun b => ih (fun i => Γ i.succ) hg (fun i => hΓ i.succ) (c b) (hcpos b) (hcsum b)
    have hslice : ∀ b, cubeSigma (fun i => Γ i.succ) (fun y => p (Fin.cons b y)) =
        m b * cubeSigma (fun i => Γ i.succ) (c b) := by
      intro b
      have : (fun y => p (Fin.cons b y)) = fun y => m b * c b y := by
        funext y
        simp only [hcdef]
        field_simp [(hmpos b).ne']
      rw [this, cubeSigma_smul _ (hmpos b) (hcpos b)]
    -- the first carrier
    set T := ∑ y : Fin n → Bool, (p (Fin.cons false y) - p (Fin.cons true y)) *
      Real.log (p (Fin.cons false y) / p (Fin.cons true y)) with hT
    have hTsup : (m false - m true) * Real.log (m false / m true) ≤ T :=
      edge_superadd Finset.univ (fun y _ => hp _) (fun y _ => hp _)
    have hone := one_carrier_bound (hmpos false) (hmpos true) hmsum
    have hTnn : 0 ≤ (m false - m true) * Real.log (m false / m true) :=
      edgeEntropy_nonneg (hmpos false) (hmpos true)
    have hΓ0 : g * T ≤ Γ 0 * T := mul_le_mul_of_nonneg_right (hΓ 0) (by linarith)
    rw [cubeSigma_succ, cubeD_succ hp, Fintype.sum_bool, Fintype.sum_bool, hslice true,
      hslice false]
    rw [← hT]
    have hc1 := mul_le_mul_of_nonneg_left (hih true) (hmpos true).le
    have hc0 := mul_le_mul_of_nonneg_left (hih false) (hmpos false).le
    have hgT : g * (4 * (m false * Real.log (m false * 2) + m true * Real.log (m true * 2))) ≤
        g * T := mul_le_mul_of_nonneg_left (by linarith) hg
    simp only [hcdef, hmdef] at hc0 hc1 hgT ⊢
    nlinarith [hc0, hc1, hgT, hΓ0]

end RepairTensor
