/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
Finite partitions and Kullback–Leibler divergence, from
`theory/CONTINUOUS_A6_2026-11-23.md`. OPEN_WORK T48, batch 1.
-/
module

public import Mathlib.InformationTheory.KullbackLeibler.DataProcessing
public import Mathlib.InformationTheory.KullbackLeibler.ChainRule
public import Mathlib.MeasureTheory.Measure.Prod
public import Mathlib.MeasureTheory.MeasurableSpace.Embedding

/-!
# Finite partitions and Kullback–Leibler divergence

`klDiv` is Mathlib's. On probability measures with an integrable
log-likelihood the finite-measure correction is zero, so the divergence
equals `ENNReal.ofReal` of the integral. Without integrability Mathlib
sets the divergence to `⊤`. The chain rule re-exported here is Mathlib's
kernel identity. It is not the mutual-information chain rule. The
Gelfand–Yaglom–Dobrushin reverse inequality is a hypothesis.
-/

@[expose] public section

namespace ContinuousA6

open MeasureTheory InformationTheory ProbabilityTheory
open scoped ENNReal ProbabilityTheory

/-- On probability measures with an integrable log-likelihood, the correction
`ν(univ) - μ(univ)` vanishes, so `klDiv` equals `ENNReal.ofReal` of the
integral. Integrability is required. Without it Mathlib sets `klDiv` to `⊤`,
and `toReal` of that value is `0`, which is not the extended value.
`theory/CONTINUOUS_A6_2026-11-23.md:77`. -/
theorem klDiv_prob_integral {α : Type*} [MeasurableSpace α] {μ ν : Measure α}
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (h : μ ≪ ν) (hint : Integrable (llr μ ν) μ) :
    klDiv μ ν = ENNReal.ofReal (∫ a, llr μ ν a ∂μ) := by
  have hcorr : (∫ a, llr μ ν a ∂μ) + ν.real Set.univ - μ.real Set.univ =
      ∫ a, llr μ ν a ∂μ := by
    simp [measureReal_def, measure_univ]
  simpa [hcorr] using klDiv_of_ac_of_integrable h hint

/-- The divergence takes values in `[0, ∞]`. -/
theorem klDiv_nonneg {α : Type*} [MeasurableSpace α] (μ ν : Measure α) :
    0 ≤ klDiv μ ν :=
  zero_le

/-- Zero if and only if the probability measures are equal.
`theory/CONTINUOUS_A6_2026-11-23.md:111`. -/
theorem klDiv_zero_iff_eq {α : Type*} [MeasurableSpace α] {μ ν : Measure α}
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] :
    klDiv μ ν = 0 ↔ μ = ν :=
  klDiv_eq_zero_iff

/-- Mutual information of a joint measure: divergence from the product of
its margins. -/
noncomputable def mutualInfo {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) : ℝ≥0∞ :=
  klDiv μ ((μ.map Prod.fst).prod (μ.map Prod.snd))

/-- Swapping the two coordinates does not change mutual information.
`theory/CONTINUOUS_A6_2026-11-23.md:145`. -/
theorem mi_swap {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] :
    mutualInfo μ = mutualInfo (μ.map Prod.swap) := by
  let π : Measure (α × β) := (μ.map Prod.fst).prod (μ.map Prod.snd)
  have hswap2 : Prod.swap ∘ Prod.swap = (id : (α × β) → α × β) := by
    funext p
    change Prod.swap (Prod.swap p) = p
    exact Prod.swap_swap p
  have hμ : (μ.map Prod.swap).map Prod.swap = μ := by
    rw [Measure.map_map measurable_swap measurable_swap, hswap2, Measure.map_id]
  have hπinv : (π.map Prod.swap).map Prod.swap = π := by
    rw [Measure.map_map measurable_swap measurable_swap, hswap2, Measure.map_id]
  have hleft : klDiv (μ.map Prod.swap) (π.map Prod.swap) ≤ klDiv μ π :=
    klDiv_map_le (μ := μ) (ν := π) measurable_swap
  have hright : klDiv μ π ≤ klDiv (μ.map Prod.swap) (π.map Prod.swap) := by
    simpa [hμ, hπinv] using
      klDiv_map_le (μ := μ.map Prod.swap) (ν := π.map Prod.swap) measurable_swap
  have heq : klDiv μ π = klDiv (μ.map Prod.swap) (π.map Prod.swap) :=
    le_antisymm hright hleft
  have hfst : (μ.map Prod.swap).map Prod.fst = μ.map Prod.snd := by
    rw [Measure.map_map measurable_fst measurable_swap]
    have : Prod.fst ∘ Prod.swap = (Prod.snd : α × β → β) := by
      funext p
      change (Prod.swap p).1 = p.2
      exact Prod.fst_swap
    rw [this]
  have hsnd : (μ.map Prod.swap).map Prod.snd = μ.map Prod.fst := by
    rw [Measure.map_map measurable_snd measurable_swap]
    have : Prod.snd ∘ Prod.swap = (Prod.fst : α × β → α) := by
      funext p
      change (Prod.swap p).2 = p.1
      exact Prod.snd_swap
    rw [this]
  have hprod : ((μ.map Prod.swap).map Prod.fst).prod ((μ.map Prod.swap).map Prod.snd) =
      π.map Prod.swap := by
    rw [hfst, hsnd]
    simpa [π] using (Measure.prod_swap (μ := μ.map Prod.fst) (ν := μ.map Prod.snd)).symm
  simp only [mutualInfo]
  rw [heq]
  congr 1
  exact hprod.symm

/-- A measurable map on each coordinate does not raise mutual information.
This is Mathlib's data-processing inequality. `theory/CONTINUOUS_A6_2026-11-23.md:145`. -/
theorem mi_data_processing {α β α' β' : Type*}
    [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace α'] [MeasurableSpace β']
    {f : α → α'} {g : β → β'} (hf : Measurable f) (hg : Measurable g)
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] :
    mutualInfo (μ.map (Prod.map f g)) ≤ mutualInfo μ := by
  let π : Measure (α × β) := (μ.map Prod.fst).prod (μ.map Prod.snd)
  have hmap : Measurable (Prod.map f g) := hf.prodMap hg
  have hfst : (μ.map (Prod.map f g)).map Prod.fst = (μ.map Prod.fst).map f := by
    rw [Measure.map_map measurable_fst hmap, Measure.map_map hf measurable_fst]
    congr 1
  have hsnd : (μ.map (Prod.map f g)).map Prod.snd = (μ.map Prod.snd).map g := by
    rw [Measure.map_map measurable_snd hmap, Measure.map_map hg measurable_snd]
    congr 1
  have hprod : ((μ.map (Prod.map f g)).map Prod.fst).prod
      ((μ.map (Prod.map f g)).map Prod.snd) = π.map (Prod.map f g) := by
    rw [hfst, hsnd]
    simpa [π] using Measure.map_prod_map (μ.map Prod.fst) (μ.map Prod.snd) hf hg
  have hle := klDiv_map_le (μ := μ) (ν := π) hmap
  simp only [mutualInfo, π] at hle ⊢
  simpa [hprod] using hle

/-- Mathlib's chain rule for composition-products. This is not the
mutual-information identity `I(X; Y, Z) = I(X; Z) + I(X; Y | Z)`.
`theory/CONTINUOUS_A6_2026-11-23.md:145`. -/
theorem klDiv_compProd_chain {𝓧 𝓨 : Type*} [MeasurableSpace 𝓧] [MeasurableSpace 𝓨]
    {μ ν : Measure 𝓧} {κ η : Kernel 𝓧 𝓨}
    [IsFiniteMeasure μ] [IsFiniteMeasure ν] [IsMarkovKernel κ] [IsMarkovKernel η] :
    klDiv (μ ⊗ₘ κ) (ν ⊗ₘ η) = klDiv μ ν + klDiv (μ ⊗ₘ κ) (μ ⊗ₘ η) :=
  klDiv_compProd_eq_add μ ν κ η

/-- Mutual information after labeling each coordinate. -/
noncomputable def partitionMI {α β γ δ : Type*}
    [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace γ] [MeasurableSpace δ]
    (μ : Measure (α × β)) (φ : α → γ) (ψ : β → δ) : ℝ≥0∞ :=
  mutualInfo (μ.map (Prod.map φ ψ))

/-- A finite labeling does not raise the divergence. `theory/CONTINUOUS_A6_2026-11-23.md:99`. -/
theorem partition_mi_le {α β γ δ : Type*}
    [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace γ] [MeasurableSpace δ]
    [Finite γ] [Finite δ]
    {φ : α → γ} {ψ : β → δ} (hφ : Measurable φ) (hψ : Measurable ψ)
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] :
    partitionMI μ φ ψ ≤ mutualInfo μ :=
  mi_data_processing hφ hψ μ

/-- A coarser labeling is a measurable function of a finer one, so the
discrete mutual information does not fall. `theory/CONTINUOUS_A6_2026-11-23.md:101`. -/
theorem refinement_mono {α β γ δ γ' δ' : Type*}
    [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace γ] [MeasurableSpace δ]
    [MeasurableSpace γ'] [MeasurableSpace δ']
    {φ : α → γ} {ψ : β → δ} {r : γ → γ'} {s : δ → δ'}
    (hφ : Measurable φ) (hψ : Measurable ψ) (hr : Measurable r) (hs : Measurable s)
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] :
    partitionMI μ (r ∘ φ) (s ∘ ψ) ≤ partitionMI μ φ ψ := by
  have hμ : IsProbabilityMeasure (μ.map (Prod.map φ ψ)) := by
    infer_instance
  have hmap : μ.map (Prod.map (r ∘ φ) (s ∘ ψ)) =
      (μ.map (Prod.map φ ψ)).map (Prod.map r s) := by
    rw [Measure.map_map (hr.prodMap hs) (hφ.prodMap hψ)]
    congr 1
  simp only [partitionMI, hmap]
  exact mi_data_processing hr hs (μ.map (Prod.map φ ψ))

/-- On a finite alphabet the identity labeling attains the mutual information.
`theory/CONTINUOUS_A6_2026-11-23.md:99`. -/
theorem finite_identity_attains {α β : Type*} [Fintype α] [Fintype β]
    [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] :
    partitionMI μ (id : α → α) (id : β → β) = mutualInfo μ := by
  have hid : Prod.map (id : α → α) (id : β → β) = id := by
    ext p
    · exact congrFun (Prod.map_fst' (id : α → α) (id : β → β)) p
    · exact congrFun (Prod.map_snd' (id : α → α) (id : β → β)) p
  simp only [partitionMI, hid, Measure.map_id]

/-- A measurable label with a finite carrier. -/
structure FiniteLabel (α : Type*) [MeasurableSpace α] where
  carrier : Type
  [toFinite : Finite carrier]
  [toMeasurableSpace : MeasurableSpace carrier]
  toFun : α → carrier
  measurable' : @Measurable _ _ _ toMeasurableSpace toFun

attribute [instance] FiniteLabel.toFinite FiniteLabel.toMeasurableSpace

/-- Mutual information of one finite labeling of each coordinate. -/
noncomputable def finitePartitionMI {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) (L : FiniteLabel α) (M : FiniteLabel β) : ℝ≥0∞ :=
  partitionMI μ L.toFun M.toFun

theorem finite_partition_le {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] (L : FiniteLabel α) (M : FiniteLabel β) :
    finitePartitionMI μ L M ≤ mutualInfo μ :=
  partition_mi_le L.measurable' M.measurable' μ

/-- The missing direction of Gelfand–Yaglom–Dobrushin: joint divergence is at
most the supremum of finite-partition mutual informations. Not constructed.
`theory/CONTINUOUS_A6_2026-11-23.md:91` and line 21. -/
def GYDSup {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) : Prop :=
  mutualInfo μ ≤ ⨆ p : FiniteLabel α × FiniteLabel β, finitePartitionMI μ p.1 p.2

/-- Adding the hypothesis to the proved inequality gives equality. The finite
alphabet does not need this hypothesis: the identity labeling attains the value. -/
theorem gyd_equiv {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (μ : Measure (α × β)) [IsProbabilityMeasure μ] (h : GYDSup μ) :
    mutualInfo μ = ⨆ p : FiniteLabel α × FiniteLabel β, finitePartitionMI μ p.1 p.2 :=
  le_antisymm h (iSup_le (fun p : FiniteLabel α × FiniteLabel β =>
    finite_partition_le μ p.1 p.2))

end ContinuousA6
