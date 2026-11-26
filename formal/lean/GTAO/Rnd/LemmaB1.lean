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
# Lemma B1 (theory/RECORD_COST_CHAIN_2026-11-25.md (source: nocloning route) §3), formalized

Informal (NOTE.md): *Ω has capacity N. Suppose M > N states ω_x and k two-outcome effects
e_j satisfy e_j(ω_x) ∈ {0,1} and x ↦ (e_1(ω_x),…,e_k(ω_x)) is injective. Then {ω_x}
cannot be 1→k cloned, hence not 1→2 cloned (1→2 cloners compose to 1→k).*

The toy model is a GPT "with a composition rule where local channels and product effects
compose". We make that rule explicit as the structure `CopyModel` below. Every field is a
modelling assumption and is listed in formal/lean/README.md, section RND-RECORD-COST. No Hilbert space, no ħ, no heat.

Conventions.
* `St n` is the state set of the n-fold composite A^{⊗n}; `St 1` is the single system Ω.
* A measurement with finite outcome set ι on `St n` is a function `ι → St n → ℝ`
  (outcome probabilities); `Meas n ι` is the set of *allowed* ones.
* A two-outcome effect e is encoded as the allowed two-outcome measurement
  `(u − e, e)`, i.e. a map `Fin 2 → St 1 → ℝ`; outcome `1` is "e fired".
-/

namespace GTAORnd

open Finset

/-- A GPT system with its n-fold composites, allowed measurements, allowed channels,
product states and product measurements. Only the properties used by Lemma B1 are
assumed. -/
structure CopyModel where
  /-- states of the n-fold composite -/
  St : ℕ → Type
  /-- allowed measurements on the n-fold composite with outcome set `ι` -/
  Meas : (n : ℕ) → (ι : Type) → [Fintype ι] → Set (ι → St n → ℝ)
  /-- allowed channels (physical maps) from the m-fold to the n-fold composite -/
  Chan : (m n : ℕ) → Set (St m → St n)
  /-- product state ω₁ ⊗ ⋯ ⊗ ωₙ -/
  prod : (n : ℕ) → (Fin n → St 1) → St n
  /-- the 1-fold product of `ω` is `ω` itself -/
  prod_one : ∀ ω : Fin 1 → St 1, prod 1 ω = ω 0
  /-- allowed measurements are normalized -/
  meas_sum : ∀ {n : ℕ} {ι : Type} [Fintype ι] {m : ι → St n → ℝ},
    m ∈ Meas n ι → ∀ s, ∑ i, m i s = 1
  /-- the identity is a channel -/
  chan_id : ∀ n, (id : St n → St n) ∈ Chan n n
  /-- channels compose -/
  chan_comp : ∀ {a b c : ℕ} {f : St a → St b} {g : St b → St c},
    f ∈ Chan a b → g ∈ Chan b c → g ∘ f ∈ Chan a c
  /-- "a measurement after a channel is a measurement" -/
  meas_pullback : ∀ {m n : ℕ} {ι : Type} [Fintype ι] {M : ι → St n → ℝ} {T : St m → St n},
    M ∈ Meas n ι → T ∈ Chan m n → (fun i s => M i (T s)) ∈ Meas m ι
  /-- product effects: k allowed two-outcome measurements on the factors give an allowed
  measurement on the composite with outcomes `b : Fin n → Fin 2`, whose value on a product
  state is the product of the factor values. -/
  prod_meas : ∀ (n : ℕ) (e : Fin n → Fin 2 → St 1 → ℝ), (∀ j, e j ∈ Meas 1 (Fin 2)) →
    ∃ E ∈ Meas n (Fin n → Fin 2), ∀ b ω, E b (prod n ω) = ∏ j, e j (b j) (ω j)
  /-- local channels: a channel `T : A → A⊗A` acting on the last factor of `A^{⊗(n+1)}`
  (identity on the other factors) is a channel `A^{⊗(n+1)} → A^{⊗(n+2)}`, and on product
  states it acts factorwise. -/
  local_ext : ∀ (n : ℕ) (T : St 1 → St 2), T ∈ Chan 1 2 →
    ∃ T' ∈ Chan (n + 1) (n + 2), ∀ (ω : Fin (n + 1) → St 1) (a b : St 1),
      T (ω (Fin.last n)) = prod 2 ![a, b] →
      T' (prod (n + 1) ω) = prod (n + 2) (Fin.snoc (α := fun _ => St 1)
        (Fin.snoc (α := fun _ => St 1) (Fin.init ω) a) b)

namespace CopyModel

variable (G : CopyModel)

/-- `ω : Fin M → St 1` is *jointly perfectly distinguishable*: one allowed measurement,
followed by a classical decoding of its outcome, names each `ω j` with certainty. -/
def Distinguishable {M : ℕ} (ω : Fin M → G.St 1) : Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (m : ι → G.St 1 → ℝ) (d : ι → Fin M),
    m ∈ G.Meas 1 ι ∧ ∀ j, ∑ i ∈ univ.filter (fun i => d i = j), m i (ω j) = 1

/-- capacity at most `N`: every jointly perfectly distinguishable family has ≤ N members.
(NOTE.md says "capacity N", i.e. the largest such set has size N; Lemma B1 only uses the
upper bound, which is weaker as a hypothesis, so the formal lemma is stronger.) -/
def CapacityLE (N : ℕ) : Prop :=
  ∀ (M : ℕ) (ω : Fin M → G.St 1), G.Distinguishable ω → M ≤ N

/-- `T` clones the family `ω` into `k` copies: `T(ω_x) = ω_x^{⊗k}` for every `x`. -/
def Clones {M : ℕ} (k : ℕ) (T : G.St 1 → G.St k) (ω : Fin M → G.St 1) : Prop :=
  T ∈ G.Chan 1 k ∧ ∀ x, T (ω x) = G.prod k (fun _ => ω x)

/-- Helper: for a sharp two-outcome measurement, the value at outcome `c` is the indicator
of `c = pattern`. -/
lemma sharp_indicator {G : CopyModel} {e : Fin 2 → G.St 1 → ℝ} (he : e ∈ G.Meas 1 (Fin 2))
    {s : G.St 1} (hs : e 1 s = 0 ∨ e 1 s = 1) (c : Fin 2) :
    e c s = if c = (if e 1 s = 1 then 1 else 0) then 1 else 0 := by
  have hsum := G.meas_sum he s
  rw [Fin.sum_univ_two] at hsum
  rcases hs with h | h
  · fin_cases c
    · simp [h]; linarith
    · simp [h]
  · fin_cases c
    · simp [h]; linarith
    · simp [h]

/-- **Lemma B1 (1→k form).** In a system of capacity ≤ N, if M > N states are each sharp
for k allowed two-outcome effects and the k-bit pattern separates them, then no allowed
channel clones them into k copies. -/
theorem lemmaB1_k (N M k : ℕ) (hcap : G.CapacityLE N) (hMN : N < M)
    (ω : Fin M → G.St 1) (e : Fin k → Fin 2 → G.St 1 → ℝ)
    (he : ∀ j, e j ∈ G.Meas 1 (Fin 2))
    (hsharp : ∀ j x, e j 1 (ω x) = 0 ∨ e j 1 (ω x) = 1)
    (hinj : Function.Injective (fun x => fun j => e j 1 (ω x))) :
    ¬ ∃ T : G.St 1 → G.St k, G.Clones k T ω := by
  rintro ⟨T, hTc, hT⟩
  -- the bit pattern of each state
  set pat : Fin M → (Fin k → Fin 2) := fun x j => if e j 1 (ω x) = 1 then 1 else 0 with hpat
  have hpinj : Function.Injective pat := by
    intro x y hxy
    apply hinj
    funext j
    have := congrFun hxy j
    simp only [hpat] at this
    show e j 1 (ω x) = e j 1 (ω y)
    rcases hsharp j x with hx | hx <;> rcases hsharp j y with hy | hy <;>
      simp only [hx, hy] at this ⊢ <;> norm_num at this
  obtain ⟨E, hEm, hEprod⟩ := G.prod_meas k e he
  -- the pulled-back measurement on Ω
  have hFm := G.meas_pullback hEm hTc
  -- its values on the ω_x are indicators of the pattern
  have hval : ∀ b x, E b (T (ω x)) = if b = pat x then 1 else 0 := by
    intro b x
    rw [hT x, hEprod]
    rw [show (∏ j, e j (b j) (ω x)) = ∏ j, (if b j = pat x j then (1:ℝ) else 0) from
      Finset.prod_congr rfl (fun j _ => sharp_indicator (he j) (hsharp j x) (b j))]
    rw [Finset.prod_boole]
    congr 1
    apply propext
    constructor
    · intro h; funext j; exact h j (mem_univ _)
    · intro h j _; rw [h]
  -- M > N ≥ 0 so Fin M is nonempty; decode by a left inverse of `pat`
  have : Nonempty (Fin M) := ⟨⟨0, by omega⟩⟩
  have hdist : G.Distinguishable ω := by
    refine ⟨Fin k → Fin 2, inferInstance, fun b s => E b (T s), Function.invFun pat, hFm, ?_⟩
    intro j
    simp only [hval]
    rw [Finset.sum_eq_single (pat j)]
    · simp
    · intro b _ hb; simp [hb]
    · intro h
      exact absurd (by simp [Function.leftInverse_invFun hpinj j]) h
  exact absurd (hcap M ω hdist) (by omega)

/-- `Fin.snoc (Fin.snoc (Fin.init (const w)) w) w = const w`. -/
lemma snoc_snoc_init_const {α : Type} (n : ℕ) (w : α) :
    (Fin.snoc (α := fun _ => α) (Fin.snoc (α := fun _ => α)
      (Fin.init (fun _ : Fin (n + 1) => w)) w) w : Fin (n + 2) → α) = fun _ => w := by
  funext i
  refine Fin.lastCases ?_ (fun i => ?_) i
  · simp
  · simp only [Fin.snoc_castSucc]
    refine Fin.lastCases ?_ (fun i => ?_) i
    · simp
    · simp [Fin.init]

/-- **"1→2 cloners compose to 1→k"**, proved from the `local_ext` rule: a channel cloning a
family into 2 copies yields, for every k ≥ 1, a channel cloning it into k copies. -/
theorem clone2_to_k {M : ℕ} (ω : Fin M → G.St 1) (T : G.St 1 → G.St 2)
    (hT : G.Clones 2 T ω) : ∀ n : ℕ, ∃ Tk : G.St 1 → G.St (n + 1), G.Clones (n + 1) Tk ω := by
  intro n
  induction n with
  | zero =>
    refine ⟨id, G.chan_id 1, fun x => ?_⟩
    simp [G.prod_one]
  | succ n ih =>
    obtain ⟨Tk, hTkc, hTk⟩ := ih
    obtain ⟨T', hT'c, hT'⟩ := G.local_ext n T hT.1
    refine ⟨T' ∘ Tk, G.chan_comp hTkc hT'c, fun x => ?_⟩
    have h2 := hT.2 x
    have h2' : T ((fun _ : Fin (n + 1) => ω x) (Fin.last n)) = G.prod 2 ![ω x, ω x] := by
      rw [h2]; congr 1; funext i; fin_cases i <;> rfl
    simp only [Function.comp, hTk x]
    rw [hT' _ _ _ h2', snoc_snoc_init_const]

/-- **Lemma B1 (1→2 form, as stated in NOTE.md).** Same hypotheses with k ≥ 1 effects
(written `k + 1`); conclusion: no allowed channel clones the family into 2 copies.
k = 0 is excluded: then injectivity forces M ≤ 1, and in a degenerate model with no allowed
measurements at all (capacity 0) a lone state may be cloneable, so the statement needs at
least one effect. The note's example uses k = 2. -/
theorem lemmaB1 (N M k : ℕ) (hcap : G.CapacityLE N) (hMN : N < M)
    (ω : Fin M → G.St 1) (e : Fin (k + 1) → Fin 2 → G.St 1 → ℝ)
    (he : ∀ j, e j ∈ G.Meas 1 (Fin 2))
    (hsharp : ∀ j x, e j 1 (ω x) = 0 ∨ e j 1 (ω x) = 1)
    (hinj : Function.Injective (fun x => fun j => e j 1 (ω x))) :
    ¬ ∃ T : G.St 1 → G.St 2, G.Clones 2 T ω := by
  rintro ⟨T, hT⟩
  obtain ⟨Tk, hTk⟩ := G.clone2_to_k ω T hT k
  exact G.lemmaB1_k N M (k + 1) hcap hMN ω e he hsharp hinj ⟨Tk, hTk⟩

end CopyModel

end GTAORnd
