/-
Copyright (c) 2026 Chad Mitchell. Public domain (CC0).
`#print axioms` for the 62 exported theorems of the record-cost side R&D
(`GTAO/Rnd/`, `theory/RECORD_COST_CHAIN_2026-11-25.md`).
Run from `formal/lean/`:  `lake env lean scripts/RndAxioms.lean`
Expected: each line lists only `propext`, `Classical.choice`, `Quot.sound` (or a subset),
or says the theorem depends on no axioms.
-/
import GTAO
open GTAORnd
#print axioms CopyModel.lemmaB1_k
#print axioms CopyModel.clone2_to_k
#print axioms CopyModel.lemmaB1
#print axioms square_capacity_le_two
#print axioms square_B1_hypotheses
#print axioms square_no_clone
#print axioms discrete_oneParam_trivial
#print axioms dihedral_oneParam_trivial
#print axioms simplexPerm_oneParam_trivial
#print axioms disk_oneParam
#print axioms ring_closed_form
#print axioms ring_bound
#print axioms factor_ge_two
#print axioms ring_ratio_indep
#print axioms ring_cost_lower_bound
#print axioms disk_strictly_cheaper
#print axioms Spekkens.forced
#print axioms Spekkens.no_injective_clone
#print axioms Spekkens.no_perm_clone
#print axioms Spekkens.disjoint_pair_clonable
#print axioms Spekkens.singletons_clonable
#print axioms SelfRef.liar_half
#print axioms SelfRef.sharp_flip_no_fixed
#print axioms SelfRef.exists_fixedPointFree
#print axioms SelfRef.sharpCopy_facts
#print axioms SelfRef.no_linear_clone_orbit
#print axioms SelfRef.no_linear_clone_moved
#print axioms SelfRef.measure_prepare_clones
#print axioms SelfRef.measure_prepare_covariant
#print axioms SelfRef.distinguishable_affineIndependent
#print axioms SelfRef.dim_bound
#print axioms SelfRef.dim_bound_one_bit
#print axioms SelfRef.Jdial_hasDerivAt
#print axioms SelfRef.Jdial_stationary_iff
#print axioms SelfRef.Jdial_midpoint
#print axioms SelfRef.Jdial_midpoint_60
#print axioms SelfRef.inv_sqrt3_bracket
#print axioms SelfRef.Jdial_rho_zero
#print axioms unitModel_clones
#print axioms SelfRef.top_coeff_zero
#print axioms SelfRef.circle_top_zero
#print axioms SelfRef.circle_all_zero
#print axioms SelfRef.no_linear_clone_circle
#print axioms SelfRef.normal_fixer_bot
#print axioms SelfRef.normal_nontrivial_fixes_nothing
#print axioms SelfRefRun.liar_half
#print axioms SelfRefRun.exists_derangement
#print axioms SelfRefRun.four_point
#print axioms SelfRefRun.no_copier_four_point
#print axioms SelfRefRun.perm_periodic
#print axioms SelfRefRun.path_sq_one_const
#print axioms SelfRefRun.midpoint_rho
#print axioms SelfRefRun.no_zero_drift_while_recording
#print axioms SelfRefRun.normal_fixer_trivial
#print axioms SelfRef.fourier_core
#print axioms SelfRef.no_linear_clone_gpt
#print axioms SelfRef.F1_cycle_count
#print axioms SelfRef.R3_full
#print axioms Composition.P1
#print axioms Composition.log_additive_iff
#print axioms Composition.P2_entries
#print axioms Composition.gbit_no_local_write
