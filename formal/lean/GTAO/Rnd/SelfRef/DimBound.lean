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
# Self-reference, piece 3: the dimension bound d ≥ N + 1 (theory/RECORD_COST_CHAIN_2026-11-25.md (source: selfref route) R3)

Informal (NOTE.md R3): *if Ω has a continuous drift (compact connected affine group acting
nontrivially) and N jointly distinguishable pure states that the drift fixes, then
d ≥ N + 1.*

Formal frame. The note's proof uses: (i) jointly distinguishable states are affinely
independent; (ii) a compact group acts orthogonally, under an invariant inner product,
around a fixed point; (iii) a connected group acting orthogonally on a line acts trivially.
We formalize (i) and (iii) and the counting, and take (ii) as the *setting*:

* `V` is a finite-dimensional real inner-product space; `d = finrank V` is the affine
  dimension of Ω (Ω is assumed to span V, with the drift-fixed point at the origin);
* the drift is a set `S` of linear isometries of `V` (continuous linear maps preserving the
  norm) that is **preconnected**, contains the identity, and contains some non-identity map.
  (Any connected group of isometries qualifies; the set form is more general.)

Not formalized: the existence of the invariant inner product and fixed point for a compact
group (Haar averaging, a standard fact), and "pure" (not used by the counting).
-/

namespace GTAORnd.SelfRef

open Module

/-- **R3 (i).** States that are jointly perfectly distinguished by affine effects
(`eᵢ(pⱼ) = δᵢⱼ`) are affinely independent. -/
theorem distinguishable_affineIndependent {V : Type*} [AddCommGroup V] [Module ℝ V] {N : ℕ}
    (p : Fin N → V) (e : Fin N → V →ᵃ[ℝ] ℝ) (hδ : ∀ i j, e i (p j) = if i = j then 1 else 0) :
    AffineIndependent ℝ p := by
  intro s w hw hv i hi
  rw [Finset.weightedVSub_eq_weightedVSubOfPoint_of_sum_eq_zero s w p hw 0,
    Finset.weightedVSubOfPoint_apply] at hv
  simp only [vsub_eq_sub, sub_zero] at hv
  have h := congrArg (e i).linear hv
  rw [map_sum, map_zero] at h
  have hlin : ∀ j, (e i).linear (p j) = e i (p j) - e i 0 := by
    intro j
    have := AffineMap.map_vadd (e i) (0 : V) (p j)
    simp only [vadd_eq_add, add_zero] at this
    rw [this]; ring
  simp only [map_smul, smul_eq_mul, hlin, hδ, mul_sub, Finset.sum_sub_distrib,
    ← Finset.sum_mul, hw, zero_mul, sub_zero, mul_ite, mul_one, mul_zero] at h
  rw [Finset.sum_ite_eq] at h
  simpa [hi] using h

variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V]

/-- **R3 (iii)+(counting).** A preconnected set of linear isometries containing the identity
and some non-identity map, all fixing `N ≥ 1` affinely independent points, forces
`finrank V ≥ N + 1`. -/
theorem dim_bound {n : ℕ} (p : Fin (n + 1) → V) (hp : AffineIndependent ℝ p)
    (S : Set (V →L[ℝ] V)) (hS : IsPreconnected S) (hid : ContinuousLinearMap.id ℝ V ∈ S)
    (hiso : ∀ g ∈ S, ∀ x, ‖g x‖ = ‖x‖) (hfix : ∀ g ∈ S, ∀ i, g (p i) = p i)
    (hnt : ∃ g ∈ S, g ≠ ContinuousLinearMap.id ℝ V) :
    (n + 1) + 1 ≤ finrank ℝ V := by
  -- K: span of the differences p i - p 0, of dimension n
  set b : {x : Fin (n + 1) // x ≠ 0} → V := fun i => p i - p 0 with hb
  have hli : LinearIndependent ℝ b := by
    have := (affineIndependent_iff_linearIndependent_vsub ℝ p 0).mp hp
    simpa [vsub_eq_sub] using this
  set K : Submodule ℝ V := Submodule.span ℝ (Set.range b) with hK
  have hKdim : finrank ℝ K = n := by
    rw [hK, finrank_span_eq_card hli]; simp
  -- every g ∈ S fixes K pointwise
  have hKfix : ∀ g ∈ S, K ≤ LinearMap.ker ((g : V →ₗ[ℝ] V) - LinearMap.id) := by
    intro g hg
    rw [hK, Submodule.span_le]
    rintro _ ⟨i, rfl⟩
    simp [hb, hfix g hg]
  -- isometries preserve inner products
  have hinner : ∀ g ∈ S, ∀ x y, inner ℝ (g x) (g y) = inner ℝ x y := by
    intro g hg x y
    let gi : V →ₗᵢ[ℝ] V := ⟨(g : V →ₗ[ℝ] V), fun z => hiso g hg z⟩
    exact gi.inner_map_map x y
  -- g maps Kᗮ into Kᗮ
  have hKperp : ∀ g ∈ S, ∀ v ∈ Kᗮ, g v ∈ Kᗮ := by
    intro g hg v hv
    rw [Submodule.mem_orthogonal]
    intro k hk
    have hgk : g k = k := by
      have := hKfix g hg hk
      simpa [sub_eq_zero] using this
    calc inner ℝ k (g v) = inner ℝ (g k) (g v) := by rw [hgk]
      _ = inner ℝ k v := hinner g hg k v
      _ = 0 := (Submodule.mem_orthogonal K v).mp hv k hk
  -- if g is the identity on Kᗮ then g = id
  have hid_of : ∀ g ∈ S, (∀ v ∈ Kᗮ, g v = v) → g = ContinuousLinearMap.id ℝ V := by
    intro g hg h
    have hsup : K ⊔ Kᗮ ≤ LinearMap.ker ((g : V →ₗ[ℝ] V) - LinearMap.id) := by
      refine sup_le (hKfix g hg) ?_
      intro v hv; simp [h v hv]
    rw [Submodule.sup_orthogonal_of_hasOrthogonalProjection] at hsup
    ext x
    have := hsup (Submodule.mem_top (x := x))
    simpa [sub_eq_zero] using this
  have hsum := Submodule.finrank_add_finrank_orthogonal K
  obtain ⟨g₀, hg₀, hne⟩ := hnt
  -- finrank Kᗮ ≥ 2
  have h2 : 2 ≤ finrank ℝ Kᗮ := by
    by_contra hlt
    push Not at hlt
    interval_cases hk : finrank ℝ Kᗮ
    · -- Kᗮ = ⊥
      have hbot : Kᗮ = ⊥ := Submodule.finrank_eq_zero.mp hk
      exact hne (hid_of g₀ hg₀ fun v hv => by
        rw [hbot, Submodule.mem_bot] at hv; simp [hv])
    · -- Kᗮ is a line spanned by some v ≠ 0
      obtain ⟨v, hv0⟩ : ∃ v : Kᗮ, v ≠ 0 := by
        have : 0 < finrank ℝ Kᗮ := by omega
        have := Module.nontrivial_of_finrank_pos (R := ℝ) this
        exact exists_ne 0
      have hline := (finrank_eq_one_iff_of_ne_zero' v hv0).mp hk
      -- each g acts on v by a scalar c with |c| = 1
      have hscal : ∀ g ∈ S, ∃ c : ℝ, g (v : V) = c • (v : V) := by
        intro g hg
        obtain ⟨c, hc⟩ := hline ⟨g v, hKperp g hg v v.2⟩
        exact ⟨c, by simpa using (congrArg Subtype.val hc).symm⟩
      have hvn : (v : V) ≠ 0 := by simpa using hv0
      have hvpos : 0 < ‖(v : V)‖ ^ 2 := by positivity
      -- the continuous function g ↦ ⟪g v, v⟫ on S takes only the values ±‖v‖²
      let F : (V →L[ℝ] V) → ℝ := fun g => inner ℝ (g v) (v : V)
      have hFc : Continuous F := by
        exact (continuous_id.clm_apply continuous_const).inner continuous_const
      have hFvals : ∀ g ∈ S, F g = ‖(v : V)‖ ^ 2 ∨ F g = -‖(v : V)‖ ^ 2 := by
        intro g hg
        obtain ⟨c, hc⟩ := hscal g hg
        have hn := hiso g hg v
        rw [hc, norm_smul, Real.norm_eq_abs] at hn
        have habs : |c| = 1 := by
          have : 0 < ‖(v : V)‖ := by positivity
          field_simp at hn; linarith [hn]
        simp only [F, hc, inner_smul_left, real_inner_self_eq_norm_sq, RCLike.conj_to_real]
        rcases abs_eq (zero_le_one) |>.mp habs with h | h <;> rw [h] <;> simp
      have hconn := hS.image F hFc.continuousOn
      have hall : ∀ g ∈ S, F g = ‖(v : V)‖ ^ 2 := by
        intro g hg
        rcases hFvals g hg with h | h
        · exact h
        · exfalso
          have hord := hconn.ordConnected
          have hid' : F (ContinuousLinearMap.id ℝ V) = ‖(v : V)‖ ^ 2 := by
            simp [F]
          have hmem : (0 : ℝ) ∈ F '' S := hord.out ⟨g, hg, rfl⟩
            ⟨_, hid, rfl⟩ ⟨by rw [h]; linarith, by rw [hid']; linarith⟩
          obtain ⟨g', hg', hg'0⟩ := hmem
          rcases hFvals g' hg' with h' | h' <;> rw [h'] at hg'0 <;> linarith
      -- so g₀ fixes v, hence fixes Kᗮ, hence is the identity
      apply hne
      apply hid_of g₀ hg₀
      intro w hw
      obtain ⟨c, hc⟩ := hscal g₀ hg₀
      have hc1 : c = 1 := by
        have := hall g₀ hg₀
        simp only [F, hc, inner_smul_left, real_inner_self_eq_norm_sq,
          RCLike.conj_to_real] at this
        nlinarith [this, hvpos]
      obtain ⟨a, ha⟩ := hline ⟨w, hw⟩
      have hw' : w = a • (v : V) := by simpa using (congrArg Subtype.val ha).symm
      rw [hw', map_smul, hc, hc1, one_smul]
  omega

/-- R3 for a one-bit record (N = 2): any such state space has d ≥ 3. The rebit/disk (d = 2)
and the classical bit (d = 1) are excluded; the qubit ball (d = 3) meets it with equality. -/
theorem dim_bound_one_bit (p : Fin 2 → V) (hp : AffineIndependent ℝ p)
    (S : Set (V →L[ℝ] V)) (hS : IsPreconnected S) (hid : ContinuousLinearMap.id ℝ V ∈ S)
    (hiso : ∀ g ∈ S, ∀ x, ‖g x‖ = ‖x‖) (hfix : ∀ g ∈ S, ∀ i, g (p i) = p i)
    (hnt : ∃ g ∈ S, g ≠ ContinuousLinearMap.id ℝ V) : 3 ≤ finrank ℝ V :=
  dim_bound (n := 1) p hp S hS hid hiso hfix hnt

end GTAORnd.SelfRef
