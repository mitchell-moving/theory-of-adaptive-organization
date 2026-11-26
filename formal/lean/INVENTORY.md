# Inventory of Lean declarations

**Current audit count: 1370** (LEAN-PHYS, build at `07bffb7` on branch `forge-lean-phys`; `formal/lean/README.md:37-54`). On `main` before LEAN-PHYS it was 1185 (batch 2, build at `6663d0e`, merged as PR #266). The 757 below is the baseline counted before batch 1, kept as the record of that count; the batch 1, batch 2 and LEAN-PHYS sections at the end give 926, 1185 and 1370.

Counted on upstream `main` `d2aeb81` before the batch 1 proofs.
The axiom audit (`formal/lean/scripts/AxiomAudit.lean`) reports **757**
environment constants in modules whose names start with `GTAO`, and every
one of them depends only on `propext`, `Classical.choice`, and `Quot.sound`.
That run is the baseline for this branch.

Those 757 constants are not 757 handwritten theorems. The sources
`formal/lean/GTAO.lean` and `formal/lean/GTAO/*.lean` contain **354**
named declarations (`theorem`, `lemma`, `def`, `abbrev`, `structure`,
`instance`). Lean then generates the remaining constants (equation lemmas,
projections, and recursors) from those 354. `GTAO.lean` itself declares
nothing; it imports the modules. `scripts/AxiomAudit.lean` is not a `GTAO`
module and is not in either count.

Faithful and WEAKER below are used only where `formal/lean/README.md`
already uses those words for that declaration. Every other source
declaration is marked **unlabeled**. Unlabeled does not mean the proof
is incomplete. It means this inventory found no Faithful or WEAKER label
on that name. The README states hypotheses and conclusions for the
unlabeled group without using either word.

Of the 354 source declarations, **20** are labeled Faithful, **6** are
labeled WEAKER, and **328** are unlabeled.

## Counts by file

| File | Source declarations | Faithful | WEAKER | unlabeled |
|---|---:|---:|---:|---:|
| `formal/lean/GTAO/BandCounterexample.lean` | 19 | 0 | 0 | 19 |
| `formal/lean/GTAO/BandMonge.lean` | 42 | 0 | 0 | 42 |
| `formal/lean/GTAO/CT10.lean` | 3 | 0 | 0 | 3 |
| `formal/lean/GTAO/CT20.lean` | 4 | 0 | 0 | 4 |
| `formal/lean/GTAO/CT22.lean` | 11 | 0 | 0 | 11 |
| `formal/lean/GTAO/CT33.lean` | 6 | 0 | 0 | 6 |
| `formal/lean/GTAO/CT34.lean` | 22 | 0 | 0 | 22 |
| `formal/lean/GTAO/CT4.lean` | 12 | 0 | 0 | 12 |
| `formal/lean/GTAO/Coadaptation.lean` | 12 | 0 | 0 | 12 |
| `formal/lean/GTAO/CoadaptationDrift.lean` | 30 | 11 | 0 | 19 |
| `formal/lean/GTAO/CoadaptationExcess.lean` | 9 | 5 | 3 | 1 |
| `formal/lean/GTAO/CoadaptationUnique.lean` | 37 | 4 | 0 | 33 |
| `formal/lean/GTAO/Cost.lean` | 12 | 0 | 0 | 12 |
| `formal/lean/GTAO/DriftSelection.lean` | 17 | 0 | 0 | 17 |
| `formal/lean/GTAO/DriftSpeed.lean` | 9 | 0 | 3 | 6 |
| `formal/lean/GTAO/Equipartition.lean` | 18 | 0 | 0 | 18 |
| `formal/lean/GTAO/Hull.lean` | 18 | 0 | 0 | 18 |
| `formal/lean/GTAO/HullWalk.lean` | 30 | 0 | 0 | 30 |
| `formal/lean/GTAO/LayerLifetime.lean` | 15 | 0 | 0 | 15 |
| `formal/lean/GTAO/LocalShared.lean` | 13 | 0 | 0 | 13 |
| `formal/lean/GTAO/N60Exact.lean` | 15 | 0 | 0 | 15 |
| **Total** | **354** | **20** | **6** | **328** |

## By paper claim

The claim names are the ones in `formal/lean/README.md`. Batch 1 does
not restate these proofs and does not delete or rename any of them.

### Finite menu, CT33, CT20, CT10

CORE §1 and THEORY CT33, CT20, CT10. Stake-split cost on a finite menu.

25 source declarations: 0 Faithful, 0 WEAKER, 25 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `effortJ` | def | `CT10.lean:32` | unlabeled |
| `effortJ_decreasing_differences` | theorem | `CT10.lean:37` | unlabeled |
| `effort_nondecreasing` | theorem | `CT10.lean:48` | unlabeled |
| `FiniteDesignMenu.J_ge_hK` | lemma | `CT20.lean:40` | unlabeled |
| `FiniteDesignMenu.layer_count_bound` | theorem | `CT20.lean:51` | unlabeled |
| `FiniteDesignMenu.spendIsLayerUpkeep` | def | `CT20.lean:60` | unlabeled |
| `FiniteDesignMenu.layer_count_nondecreasing` | theorem | `CT20.lean:67` | unlabeled |
| `FiniteDesignMenu.optimality_inequalities` | theorem | `CT33.lean:40` | unlabeled |
| `FiniteDesignMenu.error_diff_sign` | theorem | `CT33.lean:48` | unlabeled |
| `FiniteDesignMenu.error_nonincreasing` | theorem | `CT33.lean:57` | unlabeled |
| `FiniteDesignMenu.spend_ge_stake_times_error_drop` | theorem | `CT33.lean:67` | unlabeled |
| `FiniteDesignMenu.spend_nondecreasing` | theorem | `CT33.lean:77` | unlabeled |
| `FiniteDesignMenu.spend_nondecreasing_in_R` | theorem | `CT33.lean:88` | unlabeled |
| `FiniteDesignMenu` | structure | `Cost.lean:43` | unlabeled |
| `FiniteDesignMenu.J` | def | `Cost.lean:55` | unlabeled |
| `FiniteDesignMenu.IsOptimal` | def | `Cost.lean:58` | unlabeled |
| `FiniteDesignMenu.exists_minimizer` | theorem | `Cost.lean:62` | unlabeled |
| `FiniteDesignMenu.Jstar` | def | `Cost.lean:70` | unlabeled |
| `FiniteDesignMenu.isOptimal_choose` | lemma | `Cost.lean:73` | unlabeled |
| `FiniteDesignMenu.Jstar_le` | lemma | `Cost.lean:77` | unlabeled |
| `FiniteDesignMenu.IsOptimal.Jstar_eq` | lemma | `Cost.lean:80` | unlabeled |
| `FiniteDesignMenu.exists_eq_Jstar` | lemma | `Cost.lean:84` | unlabeled |
| `FiniteDesignMenu.Jstar_le_affine` | lemma | `Cost.lean:90` | unlabeled |
| `FiniteDesignMenu.J_affine` | lemma | `Cost.lean:97` | unlabeled |
| `FiniteDesignMenu.Jstar_concave` | theorem | `Cost.lean:108` | unlabeled |

### CT34 nesting and weak coupling

THEORY CT34 (i)–(iii). The converse of (ii) and (iv) are not in this tree.

22 source declarations: 0 Faithful, 0 WEAKER, 22 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `parentTeamJ` | def | `CT34.lean:47` | unlabeled |
| `IsTeamMin` | def | `CT34.lean:51` | unlabeled |
| `exists_teamMin` | lemma | `CT34.lean:54` | unlabeled |
| `JstarT` | def | `CT34.lean:60` | unlabeled |
| `isTeamMin_choose` | lemma | `CT34.lean:63` | unlabeled |
| `JstarT_le` | lemma | `CT34.lean:67` | unlabeled |
| `IsTeamMin.JstarT_eq` | lemma | `CT34.lean:70` | unlabeled |
| `JointOptimal` | def | `CT34.lean:75` | unlabeled |
| `ParentOptimal` | def | `CT34.lean:79` | unlabeled |
| `parentReduced` | def | `CT34.lean:83` | unlabeled |
| `parentReduced_le` | lemma | `CT34.lean:87` | unlabeled |
| `jointOptimal_iff` | theorem | `CT34.lean:96` | unlabeled |
| `exact_nesting_value` | theorem | `CT34.lean:123` | unlabeled |
| `parentOptimal_of_constant_theta` | theorem | `CT34.lean:133` | unlabeled |
| `strongConvex_lipschitz_nonneg` | lemma | `CT34.lean:154` | unlabeled |
| `strongConvex_lipschitz_gap` | lemma | `CT34.lean:165` | unlabeled |
| `frozenCost` | def | `CT34.lean:194` | unlabeled |
| `coupledJ` | def | `CT34.lean:198` | unlabeled |
| `weak_coupling_pointwise` | theorem | `CT34.lean:203` | unlabeled |
| `frozen_ge_min` | theorem | `CT34.lean:234` | unlabeled |
| `weak_coupling_gap` | theorem | `CT34.lean:242` | unlabeled |
| `weak_coupling_parent_regret` | theorem | `CT34.lean:260` | unlabeled |

### CT4 convex lower bound and first-bit sign

THEORY CT4, right-slope form. `L` as a lower bound on a cost is not formalized.

12 source declarations: 0 Faithful, 0 WEAKER, 12 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `affine_mul_combo` | lemma | `CT4.lean:55` | unlabeled |
| `convexOn_affine_mul'` | lemma | `CT4.lean:59` | unlabeled |
| `D_comp_IB_convex` | theorem | `CT4.lean:65` | unlabeled |
| `L_convex` | theorem | `CT4.lean:72` | unlabeled |
| `zero_isMinOn_iff` | theorem | `CT4.lean:88` | unlabeled |
| `not_minOn_zero_iff_neg_right_slope` | theorem | `CT4.lean:104` | unlabeled |
| `pos_min_of_neg_right_slope` | theorem | `CT4.lean:118` | unlabeled |
| `exists_neg_right_slope_of_not_min` | theorem | `CT4.lean:131` | unlabeled |
| `right_slope_add_linear` | lemma | `CT4.lean:140` | unlabeled |
| `L_right_slope` | lemma | `CT4.lean:148` | unlabeled |
| `first_bit_sign` | theorem | `CT4.lean:160` | unlabeled |
| `first_bit_positive_minimizer` | theorem | `CT4.lean:176` | unlabeled |

### CT22 Lundberg certificate comparisons

THEORY CT22, `B_min` and `B_slack`. The binding multiplier is not formalized.

11 source declarations: 0 Faithful, 0 WEAKER, 11 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `LundbergCertified` | def | `CT22.lean:38` | unlabeled |
| `thetaMax` | def | `CT22.lean:42` | unlabeled |
| `theta_le_max` | lemma | `CT22.lean:46` | unlabeled |
| `Bmin` | def | `CT22.lean:50` | unlabeled |
| `Bslack` | def | `CT22.lean:54` | unlabeled |
| `log_one_div_pos` | lemma | `CT22.lean:57` | unlabeled |
| `Bmin_pos` | lemma | `CT22.lean:63` | unlabeled |
| `not_certified_below_Bmin` | theorem | `CT22.lean:72` | unlabeled |
| `certified_at_Bslack` | theorem | `CT22.lean:90` | unlabeled |
| `expected_cost_opt_at_or_above_Bslack` | theorem | `CT22.lean:106` | unlabeled |
| `Bmin_le_Bslack` | theorem | `CT22.lean:118` | unlabeled |

### Lower hull and from-0 count

KEYSTONE_NOTE §4 and `theory/LAYER_CONVEXITY.md` Lemma L1 / N64.

63 source declarations: 0 Faithful, 0 WEAKER, 63 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `phi` | def | `Hull.lean:34` | unlabeled |
| `OnLowerHull` | def | `Hull.lean:40` | unlabeled |
| `phi_sum` | lemma | `Hull.lean:47` | unlabeled |
| `exists_phi_lt_of_combo_lt` | lemma | `Hull.lean:75` | unlabeled |
| `combo_of_zero` | lemma | `Hull.lean:92` | unlabeled |
| `minimizer_on_lower_hull` | theorem | `Hull.lean:117` | unlabeled |
| `DiscreteConvexOn` | def | `Hull.lean:160` | unlabeled |
| `DiscreteConvexOn.adjacent` | lemma | `Hull.lean:163` | unlabeled |
| `DiscreteConvexOn.mono_increment` | lemma | `Hull.lean:168` | unlabeled |
| `IncrementPays` | def | `Hull.lean:187` | unlabeled |
| `incrementPays_iff` | lemma | `Hull.lean:190` | unlabeled |
| `phi_diff` | lemma | `Hull.lean:195` | unlabeled |
| `DiscreteConvexOn.mono_phi_diff` | lemma | `Hull.lean:199` | unlabeled |
| `DiscreteConvexOn.pays_of_later` | lemma | `Hull.lean:211` | unlabeled |
| `phi_strict_decrease_chain` | lemma | `Hull.lean:219` | unlabeled |
| `phi_nondecreasing_after` | lemma | `Hull.lean:234` | unlabeled |
| `n60_from_zero_leftmost` | theorem | `Hull.lean:261` | unlabeled |
| `n60_as_written_zero_hole` | theorem | `Hull.lean:280` | unlabeled |
| `HullWalk.HullVertices` | structure | `HullWalk.lean:38` | unlabeled |
| `HullWalk.HullVertices.slope` | def | `HullWalk.lean:48` | unlabeled |
| `HullWalk.HullVertices.IsLowerHull` | structure | `HullWalk.lean:53` | unlabeled |
| `HullWalk.HullVertices.Pays` | def | `HullWalk.lean:59` | unlabeled |
| `HullWalk.len_pos` | lemma | `HullWalk.lean:64` | unlabeled |
| `HullWalk.slope_mul_len` | lemma | `HullWalk.lean:69` | unlabeled |
| `HullWalk.phi_step` | lemma | `HullWalk.lean:74` | unlabeled |
| `HullWalk.pays_iff` | lemma | `HullWalk.lean:81` | unlabeled |
| `HullWalk.phi_ge_line` | lemma | `HullWalk.lean:98` | unlabeled |
| `HullWalk.slope_mono` | lemma | `HullWalk.lean:105` | unlabeled |
| `HullWalk.exists_edge` | lemma | `HullWalk.lean:113` | unlabeled |
| `HullWalk.hull_walk_stop_exists` | theorem | `HullWalk.lean:134` | unlabeled |
| `HullWalk.hull_walk_leftmost_argmin` | theorem | `HullWalk.lean:147` | unlabeled |
| `HullWalk.chord` | def | `HullWalk.lean:249` | unlabeled |
| `HullWalk.exists_next` | lemma | `HullWalk.lean:251` | unlabeled |
| `HullWalk.next` | def | `HullWalk.lean:256` | unlabeled |
| `HullWalk.next_spec` | lemma | `HullWalk.lean:259` | unlabeled |
| `HullWalk.gv` | def | `HullWalk.lean:270` | unlabeled |
| `HullWalk.gv_lt_succ` | lemma | `HullWalk.lean:274` | unlabeled |
| `HullWalk.gv_strictMono` | lemma | `HullWalk.lean:280` | unlabeled |
| `HullWalk.gv_succ_of_lt` | lemma | `HullWalk.lean:282` | unlabeled |
| `HullWalk.exists_gv_ge` | lemma | `HullWalk.lean:286` | unlabeled |
| `HullWalk.gm` | def | `HullWalk.lean:290` | unlabeled |
| `HullWalk.gv_lt_of_lt_gm` | lemma | `HullWalk.lean:293` | unlabeled |
| `HullWalk.gv_gm` | lemma | `HullWalk.lean:299` | unlabeled |
| `HullWalk.greedy` | def | `HullWalk.lean:315` | unlabeled |
| `HullWalk.greedy_slope` | lemma | `HullWalk.lean:322` | unlabeled |
| `HullWalk.chord_add` | lemma | `HullWalk.lean:325` | unlabeled |
| `HullWalk.greedy_isLowerHull` | theorem | `HullWalk.lean:334` | unlabeled |
| `HullWalk.hull_increment_test_eq_argmin` | theorem | `HullWalk.lean:381` | unlabeled |
| `N60Exact.count` | def | `N60Exact.lean:50` | unlabeled |
| `N60Exact.IsLeftmostArgmin` | def | `N60Exact.lean:54` | unlabeled |
| `N60Exact.count_isLeftmostArgmin` | theorem | `N60Exact.lean:59` | unlabeled |
| `N60Exact.not_min_of_rise` | lemma | `N60Exact.lean:90` | unlabeled |
| `N60Exact.exists_threshold` | lemma | `N60Exact.lean:106` | unlabeled |
| `N60Exact.threshold_pos` | lemma | `N60Exact.lean:141` | unlabeled |
| `N60Exact.exists_R_interval_count_not_argmin` | theorem | `N60Exact.lean:160` | unlabeled |
| `N60Exact.exists_R_count_not_argmin` | theorem | `N60Exact.lean:337` | unlabeled |
| `N60Exact.exists_R_count_not_argmin_of_pos` | theorem | `N60Exact.lean:350` | unlabeled |
| `N60Exact.count_exact_iff_convex` | theorem | `N60Exact.lean:368` | unlabeled |
| `N60Exact.epsCE` | def | `N60Exact.lean:387` | unlabeled |
| `N60Exact.epsCE_not_convex` | lemma | `N60Exact.lean:389` | unlabeled |
| `N60Exact.epsCE_count_zero` | lemma | `N60Exact.lean:395` | unlabeled |
| `N60Exact.epsCE_zero_min` | lemma | `N60Exact.lean:411` | unlabeled |
| `N60Exact.exists_nonconvex_count_exact` | theorem | `N60Exact.lean:432` | unlabeled |

### Layer lifetime

CORE §3 and `theory/LAYER_LIFETIME_2026-11-21.md`. The cost expression is an input.

15 source declarations: 0 Faithful, 0 WEAKER, 15 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `LayerLifetime.cost` | def | `LayerLifetime.lean:40` | unlabeled |
| `LayerLifetime.Tstar` | def | `LayerLifetime.lean:43` | unlabeled |
| `LayerLifetime.amgm_identity` | lemma | `LayerLifetime.lean:47` | unlabeled |
| `LayerLifetime.cost_ge` | lemma | `LayerLifetime.lean:56` | unlabeled |
| `LayerLifetime.Tstar_pos` | lemma | `LayerLifetime.lean:63` | unlabeled |
| `LayerLifetime.sqrt_a_mul_Tstar` | lemma | `LayerLifetime.lean:66` | unlabeled |
| `LayerLifetime.cost_Tstar` | theorem | `LayerLifetime.lean:72` | unlabeled |
| `LayerLifetime.Tstar_isMin` | theorem | `LayerLifetime.lean:82` | unlabeled |
| `LayerLifetime.Tstar_unique` | theorem | `LayerLifetime.lean:87` | unlabeled |
| `LayerLifetime.layer_lifetime` | theorem | `LayerLifetime.lean:103` | unlabeled |
| `LayerLifetime.fixed_period_lifetime` | theorem | `LayerLifetime.lean:119` | unlabeled |
| `LayerLifetime.barrier_eq_sqrt3_fixed` | theorem | `LayerLifetime.lean:134` | unlabeled |
| `LayerLifetime.Tstar_scale_k` | theorem | `LayerLifetime.lean:141` | unlabeled |
| `LayerLifetime.lifetime_ratio` | theorem | `LayerLifetime.lean:147` | unlabeled |
| `LayerLifetime.barrier_band_identities` | theorem | `LayerLifetime.lean:159` | unlabeled |

### Local versus shared (D5)

LAYER_LIFETIME §5. The cost expressions are inputs.

13 source declarations: 0 Faithful, 0 WEAKER, 13 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `LocalShared.localCost` | def | `LocalShared.lean:51` | unlabeled |
| `LocalShared.sharedCost` | def | `LocalShared.lean:54` | unlabeled |
| `LocalShared.sigma2Star` | def | `LocalShared.lean:57` | unlabeled |
| `LocalShared.localCost_eq` | lemma | `LocalShared.lean:64` | unlabeled |
| `LocalShared.sharedCost_eq` | lemma | `LocalShared.lean:68` | unlabeled |
| `LocalShared.const_lt_iff` | lemma | `LocalShared.lean:74` | unlabeled |
| `LocalShared.crossing_root_eq` | lemma | `LocalShared.lean:85` | unlabeled |
| `LocalShared.no_switch_without_delay` | theorem | `LocalShared.lean:96` | unlabeled |
| `LocalShared.shared_never_wins` | theorem | `LocalShared.lean:105` | unlabeled |
| `LocalShared.crossing` | theorem | `LocalShared.lean:118` | unlabeled |
| `LocalShared.switch_iff` | theorem | `LocalShared.lean:140` | unlabeled |
| `LocalShared.equal_delay_no_switch` | theorem | `LocalShared.lean:171` | unlabeled |
| `LocalShared.barrier_crossing_eq_fixed_div_three` | theorem | `LocalShared.lean:182` | unlabeled |

### Equipartition, SA1b

`theory/SELECTION_AXIOMS.md` SA1b. SA1's Boltzmann weight is an input.

18 source declarations: 0 Faithful, 0 WEAKER, 18 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `Equipartition.Z` | def | `Equipartition.lean:55` | unlabeled |
| `Equipartition.Nm` | def | `Equipartition.lean:58` | unlabeled |
| `Equipartition.HomogCost` | structure | `Equipartition.lean:63` | unlabeled |
| `Equipartition.scale_eq` | lemma | `Equipartition.lean:73` | unlabeled |
| `Equipartition.pow_finrank_inv` | lemma | `Equipartition.lean:78` | unlabeled |
| `Equipartition.Z_scale` | theorem | `Equipartition.lean:84` | unlabeled |
| `Equipartition.Nm_scale` | theorem | `Equipartition.lean:94` | unlabeled |
| `Equipartition.exists_lower_bound` | lemma | `Equipartition.lean:109` | unlabeled |
| `Equipartition.integrable_exp_neg_norm_rpow` | lemma | `Equipartition.lean:128` | unlabeled |
| `Equipartition.integrable_exp` | lemma | `Equipartition.lean:138` | unlabeled |
| `Equipartition.integrable_moment` | lemma | `Equipartition.lean:147` | unlabeled |
| `Equipartition.inner_ftc` | lemma | `Equipartition.lean:164` | unlabeled |
| `Equipartition.Z_sub_eq_integral_Nm` | lemma | `Equipartition.lean:181` | unlabeled |
| `Equipartition.Nm_one` | theorem | `Equipartition.lean:207` | unlabeled |
| `Equipartition.gibbs_mean_homog` | theorem | `Equipartition.lean:241` | unlabeled |
| `Equipartition.gibbs_excess` | theorem | `Equipartition.lean:253` | unlabeled |
| `Equipartition.homogCost_quadratic` | lemma | `Equipartition.lean:289` | unlabeled |
| `Equipartition.gibbs_excess_quadratic` | theorem | `Equipartition.lean:319` | unlabeled |

### Drift selection DS1

`theory/DRIFT_SELECTION.md` DS1. The Langevin limit is an input.

17 source declarations: 0 Faithful, 0 WEAKER, 17 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `DriftSelection.driftMatrix` | def | `DriftSelection.lean:56` | unlabeled |
| `DriftSelection.driftMatrix_posDef` | lemma | `DriftSelection.lean:60` | unlabeled |
| `DriftSelection.driftMatrix_add_posDef` | lemma | `DriftSelection.lean:65` | unlabeled |
| `DriftSelection.OUMoments` | structure | `DriftSelection.lean:73` | unlabeled |
| `DriftSelection.BMMoments` | structure | `DriftSelection.lean:87` | unlabeled |
| `DriftSelection.card_fin` | lemma | `DriftSelection.lean:94` | unlabeled |
| `DriftSelection.trace_one_fin` | lemma | `DriftSelection.lean:97` | unlabeled |
| `DriftSelection.sub_two_smul` | lemma | `DriftSelection.lean:100` | unlabeled |
| `DriftSelection.isHermitian_transpose` | lemma | `DriftSelection.lean:108` | unlabeled |
| `DriftSelection.ou_C_eq` | lemma | `DriftSelection.lean:113` | unlabeled |
| `DriftSelection.trace_mul₃_herm` | lemma | `DriftSelection.lean:150` | unlabeled |
| `DriftSelection.ou_excess` | theorem | `DriftSelection.lean:166` | unlabeled |
| `DriftSelection.bm_excess` | theorem | `DriftSelection.lean:259` | unlabeled |
| `DriftSelection.bm_excess_isotropic` | theorem | `DriftSelection.lean:287` | unlabeled |
| `DriftSelection.bm_excess_static` | theorem | `DriftSelection.lean:298` | unlabeled |
| `DriftSelection.velocity_mean_excess` | theorem | `DriftSelection.lean:309` | unlabeled |
| `DriftSelection.ou_excess_fast_remainder` | theorem | `DriftSelection.lean:371` | unlabeled |

### Drift speed DS2

`theory/DRIFT_SELECTION.md` DS2. The README labels the three named theorems WEAKER.

9 source declarations: 0 Faithful, 3 WEAKER, 6 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `DriftSpeed.vMax` | def | `DriftSpeed.lean:40` | unlabeled |
| `DriftSpeed.vMax_pos` | lemma | `DriftSpeed.lean:43` | unlabeled |
| `DriftSpeed.meanLag` | def | `DriftSpeed.lean:54` | unlabeled |
| `DriftSpeed.meanLag_decomp` | lemma | `DriftSpeed.lean:57` | unlabeled |
| `DriftSpeed.meanLag_of_faster` | theorem | `DriftSpeed.lean:65` | unlabeled |
| `DriftSpeed.meanLag_of_faster_neg` | theorem | `DriftSpeed.lean:95` | unlabeled |
| `DriftSpeed.meanLag_abs` | theorem | `DriftSpeed.lean:129` | WEAKER |
| `DriftSpeed.ds2_excess` | theorem | `DriftSpeed.lean:177` | WEAKER |
| `DriftSpeed.halfWindow_diverges` | theorem | `DriftSpeed.lean:209` | WEAKER |

### Band model, Lemmas M, Z, X and Theorem B

`theory/LAYER_CONVEXITY.md`, finite cells, plus the peak counterexample.

61 source declarations: 0 Faithful, 0 WEAKER, 61 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `BandCounterexample.mu` | def | `BandCounterexample.lean:40` | unlabeled |
| `BandCounterexample.W` | def | `BandCounterexample.lean:47` | unlabeled |
| `BandCounterexample.segSum` | def | `BandCounterexample.lean:52` | unlabeled |
| `BandCounterexample.bandCost` | def | `BandCounterexample.lean:56` | unlabeled |
| `BandCounterexample.termCost` | def | `BandCounterexample.lean:61` | unlabeled |
| `BandCounterexample.listMin` | def | `BandCounterexample.lean:64` | unlabeled |
| `BandCounterexample.clusterE` | def | `BandCounterexample.lean:70` | unlabeled |
| `BandCounterexample.clusterE_values` | theorem | `BandCounterexample.lean:76` | unlabeled |
| `BandCounterexample.muR` | def | `BandCounterexample.lean:82` | unlabeled |
| `BandCounterexample.WR` | def | `BandCounterexample.lean:83` | unlabeled |
| `BandCounterexample.bandH` | def | `BandCounterexample.lean:86` | unlabeled |
| `BandCounterexample.cost` | def | `BandCounterexample.lean:90` | unlabeled |
| `BandCounterexample.cost_eq` | lemma | `BandCounterexample.lean:93` | unlabeled |
| `BandCounterexample.bandE0` | theorem | `BandCounterexample.lean:98` | unlabeled |
| `BandCounterexample.bandE1_lower` | theorem | `BandCounterexample.lean:102` | unlabeled |
| `BandCounterexample.bandE1_attained` | theorem | `BandCounterexample.lean:119` | unlabeled |
| `BandCounterexample.bandE2_attained` | theorem | `BandCounterexample.lean:123` | unlabeled |
| `BandCounterexample.cost_nonneg` | lemma | `BandCounterexample.lean:126` | unlabeled |
| `BandCounterexample.not_convex` | theorem | `BandCounterexample.lean:131` | unlabeled |
| `BandMonge.f` | def | `BandMonge.lean:34` | unlabeled |
| `BandMonge.merge_gain` | lemma | `BandMonge.lean:37` | unlabeled |
| `BandMonge.merge_gain_nonneg` | lemma | `BandMonge.lean:44` | unlabeled |
| `BandMonge.quadrangle_core` | lemma | `BandMonge.lean:53` | unlabeled |
| `BandMonge.terminal_core` | lemma | `BandMonge.lean:80` | unlabeled |
| `BandMonge.M` | def | `BandMonge.lean:101` | unlabeled |
| `BandMonge.S` | def | `BandMonge.lean:103` | unlabeled |
| `BandMonge.Q` | def | `BandMonge.lean:105` | unlabeled |
| `BandMonge.w` | def | `BandMonge.lean:109` | unlabeled |
| `BandMonge.z` | def | `BandMonge.lean:112` | unlabeled |
| `BandMonge.linkCost` | def | `BandMonge.lean:117` | unlabeled |
| `BandMonge.w_self` | lemma | `BandMonge.lean:121` | unlabeled |
| `BandMonge.M_add` | lemma | `BandMonge.lean:123` | unlabeled |
| `BandMonge.S_add` | lemma | `BandMonge.lean:125` | unlabeled |
| `BandMonge.Q_add` | lemma | `BandMonge.lean:127` | unlabeled |
| `BandMonge.M_pos` | lemma | `BandMonge.lean:132` | unlabeled |
| `BandMonge.S_nonneg` | lemma | `BandMonge.lean:135` | unlabeled |
| `BandMonge.mean_le` | lemma | `BandMonge.lean:141` | unlabeled |
| `BandMonge.quadrangle` | theorem | `BandMonge.lean:161` | unlabeled |
| `BandMonge.terminal` | theorem | `BandMonge.lean:203` | unlabeled |
| `BandMonge.linkCost_monge` | theorem | `BandMonge.lean:224` | unlabeled |
| `BandMonge.IsPath` | def | `BandMonge.lean:245` | unlabeled |
| `BandMonge.pathCost` | def | `BandMonge.lean:248` | unlabeled |
| `BandMonge.Monge` | def | `BandMonge.lean:251` | unlabeled |
| `BandMonge.swapP` | def | `BandMonge.lean:254` | unlabeled |
| `BandMonge.swapQ` | def | `BandMonge.lean:256` | unlabeled |
| `BandMonge.sum_split` | lemma | `BandMonge.lean:260` | unlabeled |
| `BandMonge.exchange_at` | lemma | `BandMonge.lean:265` | unlabeled |
| `BandMonge.exchange` | theorem | `BandMonge.lean:342` | unlabeled |
| `BandMonge.convex_of_monge` | theorem | `BandMonge.lean:367` | unlabeled |
| `BandMonge.path_le` | lemma | `BandMonge.lean:374` | unlabeled |
| `BandMonge.isPath_congr` | lemma | `BandMonge.lean:385` | unlabeled |
| `BandMonge.pathCost_congr` | lemma | `BandMonge.lean:391` | unlabeled |
| `BandMonge.exists_optimal` | theorem | `BandMonge.lean:397` | unlabeled |
| `BandMonge.trivial_path` | lemma | `BandMonge.lean:418` | unlabeled |
| `BandMonge.exists_path` | lemma | `BandMonge.lean:427` | unlabeled |
| `BandMonge.band_convex` | theorem | `BandMonge.lean:440` | unlabeled |
| `BandMonge.bandE` | def | `BandMonge.lean:455` | unlabeled |
| `BandMonge.bandE_is_min` | theorem | `BandMonge.lean:463` | unlabeled |
| `BandMonge.bandE_eq` | theorem | `BandMonge.lean:476` | unlabeled |
| `BandMonge.bandE_second_difference` | theorem | `BandMonge.lean:486` | unlabeled |
| `BandMonge.terminal_needs_nonneg` | theorem | `BandMonge.lean:506` | unlabeled |

### CA1 and uniqueness

`theory/COADAPTATION.md` CA1, CA1a, and the elementary uniqueness argument.

49 source declarations: 4 Faithful, 0 WEAKER, 45 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `Coadaptation.IsMove` | def | `Coadaptation.lean:59` | unlabeled |
| `Coadaptation.LogLinearChain` | structure | `Coadaptation.lean:63` | unlabeled |
| `Coadaptation.IsExactPotential` | def | `Coadaptation.lean:72` | unlabeled |
| `Coadaptation.DetailedBalance` | def | `Coadaptation.lean:76` | unlabeled |
| `Coadaptation.isMove_symm` | lemma | `Coadaptation.lean:82` | unlabeled |
| `Coadaptation.detailedBalance_of_potential` | theorem | `Coadaptation.lean:91` | unlabeled |
| `Coadaptation.potential_of_detailedBalance` | theorem | `Coadaptation.lean:106` | unlabeled |
| `Coadaptation.ca1_iff` | theorem | `Coadaptation.lean:140` | unlabeled |
| `Coadaptation.gibbs_form` | lemma | `Coadaptation.lean:154` | unlabeled |
| `Coadaptation.stationary_of_detailedBalance` | theorem | `Coadaptation.lean:161` | unlabeled |
| `Coadaptation.ca1a_weighted` | theorem | `Coadaptation.lean:169` | unlabeled |
| `Coadaptation.ca1a_square` | theorem | `Coadaptation.lean:181` | unlabeled |
| `Coadaptation.IsRowStochastic` | def | `CoadaptationUnique.lean:49` | unlabeled |
| `Coadaptation.IsStationaryProb` | def | `CoadaptationUnique.lean:53` | unlabeled |
| `Coadaptation.IsIrreducibleStochastic` | def | `CoadaptationUnique.lean:57` | unlabeled |
| `Coadaptation.stationary_pos` | theorem | `CoadaptationUnique.lean:62` | unlabeled |
| `Coadaptation.exists_edge_into` | lemma | `CoadaptationUnique.lean:87` | unlabeled |
| `Coadaptation.unique_stationary_prob` | theorem | `CoadaptationUnique.lean:102` | Faithful |
| `Coadaptation.exitRate` | def | `CoadaptationUnique.lean:191` | unlabeled |
| `Coadaptation.uniformize` | def | `CoadaptationUnique.lean:195` | unlabeled |
| `Coadaptation.exitRate_eq_erase` | lemma | `CoadaptationUnique.lean:198` | unlabeled |
| `Coadaptation.uniformize_row_sum` | lemma | `CoadaptationUnique.lean:215` | unlabeled |
| `Coadaptation.IsGlobalBalance` | def | `CoadaptationUnique.lean:236` | unlabeled |
| `Coadaptation.global_balance_of_detailed` | lemma | `CoadaptationUnique.lean:239` | unlabeled |
| `Coadaptation.sum_offdiag_eq_erase` | lemma | `CoadaptationUnique.lean:244` | unlabeled |
| `Coadaptation.sum_split_at` | lemma | `CoadaptationUnique.lean:260` | unlabeled |
| `Coadaptation.IsGlobalBalance_of_inflow` | lemma | `CoadaptationUnique.lean:265` | unlabeled |
| `Coadaptation.inflow_of_IsGlobalBalance` | lemma | `CoadaptationUnique.lean:277` | unlabeled |
| `Coadaptation.uniformize_invariant` | lemma | `CoadaptationUnique.lean:289` | unlabeled |
| `Coadaptation.uniformize_stationary` | theorem | `CoadaptationUnique.lean:327` | unlabeled |
| `Coadaptation.unifRate` | def | `CoadaptationUnique.lean:350` | unlabeled |
| `Coadaptation.unifRate_pos` | lemma | `CoadaptationUnique.lean:353` | unlabeled |
| `Coadaptation.unifRate_gt_exit` | lemma | `CoadaptationUnique.lean:359` | unlabeled |
| `Coadaptation.exitRate_nonneg` | lemma | `CoadaptationUnique.lean:366` | unlabeled |
| `Coadaptation.uniformize_stochastic` | lemma | `CoadaptationUnique.lean:373` | unlabeled |
| `Coadaptation.unique_global_balance` | theorem | `CoadaptationUnique.lean:395` | Faithful |
| `Coadaptation.isMove_path_one_party` | lemma | `CoadaptationUnique.lean:415` | unlabeled |
| `Coadaptation.isMove_path_to_update` | lemma | `CoadaptationUnique.lean:426` | unlabeled |
| `Coadaptation.joint_connected` | theorem | `CoadaptationUnique.lean:435` | Faithful |
| `Coadaptation.gibbsProb` | def | `CoadaptationUnique.lean:467` | unlabeled |
| `Coadaptation.gibbsProb_Z_pos` | lemma | `CoadaptationUnique.lean:471` | unlabeled |
| `Coadaptation.gibbsProb_pos` | lemma | `CoadaptationUnique.lean:480` | unlabeled |
| `Coadaptation.gibbsProb_nonneg` | lemma | `CoadaptationUnique.lean:484` | unlabeled |
| `Coadaptation.gibbsProb_sum` | lemma | `CoadaptationUnique.lean:488` | unlabeled |
| `Coadaptation.detailedBalance_gibbsProb` | lemma | `CoadaptationUnique.lean:494` | unlabeled |
| `Coadaptation.q_nonneg` | lemma | `CoadaptationUnique.lean:509` | unlabeled |
| `Coadaptation.isMove_imp_q_pos` | lemma | `CoadaptationUnique.lean:515` | unlabeled |
| `Coadaptation.uniformize_irreducible` | lemma | `CoadaptationUnique.lean:520` | unlabeled |
| `Coadaptation.unique_gibbs_stationary` | theorem | `CoadaptationUnique.lean:546` | Faithful |

### CA1b and CA1c

CLAIM_MAP U2. The README labels some of these Faithful and some WEAKER.

9 source declarations: 5 Faithful, 3 WEAKER, 1 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `Coadaptation.potential_shift_independent` | theorem | `CoadaptationExcess.lean:56` | Faithful |
| `Coadaptation.conditional_boltzmann` | theorem | `CoadaptationExcess.lean:65` | Faithful |
| `Coadaptation.trace_mul_eq_sum` | lemma | `CoadaptationExcess.lean:75` | unlabeled |
| `Coadaptation.ca1b_potential_excess` | theorem | `CoadaptationExcess.lean:83` | Faithful |
| `Coadaptation.ca1b_team_split` | theorem | `CoadaptationExcess.lean:96` | WEAKER |
| `Coadaptation.ca1c_potential` | theorem | `CoadaptationExcess.lean:114` | Faithful |
| `Coadaptation.ca1c_summed_cost` | theorem | `CoadaptationExcess.lean:130` | Faithful |
| `Coadaptation.ca1c_gap_zero` | theorem | `CoadaptationExcess.lean:141` | WEAKER |
| `Coadaptation.ca1c_fraction` | theorem | `CoadaptationExcess.lean:154` | WEAKER |

### CA7 potential excess and the s8b datum

CLAIM_MAP U11. Lyapunov equation as input. The README labels the named results Faithful.

30 source declarations: 11 Faithful, 0 WEAKER, 19 unlabeled.

| Declaration | Kind | Line | Status |
|---|---|---:|---|
| `CoadaptationDrift.card_fin` | lemma | `CoadaptationDrift.lean:44` | unlabeled |
| `CoadaptationDrift.trace_one_fin` | lemma | `CoadaptationDrift.lean:47` | unlabeled |
| `CoadaptationDrift.isHermitian_eq_transpose` | lemma | `CoadaptationDrift.lean:50` | unlabeled |
| `CoadaptationDrift.trace_antisymm_symm` | lemma | `CoadaptationDrift.lean:56` | unlabeled |
| `CoadaptationDrift.virial_trace` | theorem | `CoadaptationDrift.lean:74` | Faithful |
| `CoadaptationDrift.ca7_potential_excess` | theorem | `CoadaptationDrift.lean:133` | Faithful |
| `CoadaptationDrift.mul2` | def | `CoadaptationDrift.lean:153` | unlabeled |
| `CoadaptationDrift.s8bS` | def | `CoadaptationDrift.lean:165` | unlabeled |
| `CoadaptationDrift.s8bW` | def | `CoadaptationDrift.lean:169` | unlabeled |
| `CoadaptationDrift.s8bGamma` | def | `CoadaptationDrift.lean:171` | unlabeled |
| `CoadaptationDrift.s8bBeta` | def | `CoadaptationDrift.lean:173` | unlabeled |
| `CoadaptationDrift.s8bV` | def | `CoadaptationDrift.lean:175` | unlabeled |
| `CoadaptationDrift.s8bQ` | def | `CoadaptationDrift.lean:178` | unlabeled |
| `CoadaptationDrift.s8bP` | def | `CoadaptationDrift.lean:183` | unlabeled |
| `CoadaptationDrift.s8bM` | def | `CoadaptationDrift.lean:190` | unlabeled |
| `CoadaptationDrift.s8bQuad` | def | `CoadaptationDrift.lean:194` | unlabeled |
| `CoadaptationDrift.s8bRegret` | def | `CoadaptationDrift.lean:199` | unlabeled |
| `CoadaptationDrift.s8bNaive` | def | `CoadaptationDrift.lean:203` | unlabeled |
| `CoadaptationDrift.s8b_lyapunov` | theorem | `CoadaptationDrift.lean:208` | Faithful |
| `CoadaptationDrift.s8b_regret_party0` | theorem | `CoadaptationDrift.lean:214` | Faithful |
| `CoadaptationDrift.s8b_regret_party1` | theorem | `CoadaptationDrift.lean:217` | Faithful |
| `CoadaptationDrift.s8b_naive_party0` | theorem | `CoadaptationDrift.lean:220` | Faithful |
| `CoadaptationDrift.s8b_naive_party1` | theorem | `CoadaptationDrift.lean:223` | Faithful |
| `CoadaptationDrift.s8bP0` | def | `CoadaptationDrift.lean:227` | unlabeled |
| `CoadaptationDrift.s8bP0_right_inv` | theorem | `CoadaptationDrift.lean:234` | Faithful |
| `CoadaptationDrift.s8bP0_lyapunov` | theorem | `CoadaptationDrift.lean:240` | Faithful |
| `CoadaptationDrift.s8bQuad0` | def | `CoadaptationDrift.lean:247` | unlabeled |
| `CoadaptationDrift.s8bStaticRegret` | def | `CoadaptationDrift.lean:252` | unlabeled |
| `CoadaptationDrift.s8b_static_regret` | theorem | `CoadaptationDrift.lean:258` | Faithful |
| `CoadaptationDrift.ca7_regret_not_naive` | theorem | `CoadaptationDrift.lean:278` | Faithful |

## What batch 1 reuses

Batch 1 does not prove these again.

- `Equipartition.gibbs_excess_quadratic` and `Equipartition.homogCost_quadratic`
  (`formal/lean/GTAO/Equipartition.lean`) supply `E[J] − J* = d/(2β)` for the
  affine excess of `aJ+b`. `Matrix.PosDef.smul` scales the quadratic form
  when the slope is refit. The fixed-measure reading and the refitted-slope
  reading stay separate statements, as in `theory/REPRESENTATION.md:134`.
- `LayerLifetime.Tstar`, `LayerLifetime.Tstar_isMin`, and
  `LayerLifetime.Tstar_unique` (`formal/lean/GTAO/LayerLifetime.lean`) are the
  unique positive minimizer of `k/T + a T`. The expected-cost interval at the
  published Lundberg point is that minimizer at `k = 1/20`, `a = 1/2`.
- `InformationTheory.klDiv`, `klDiv_eq_zero_iff`, `klDiv_map_le`, and
  `klDiv_compProd_eq_add` come from `Mathlib.InformationTheory.KullbackLeibler`.
  They are not copied.
- `FiniteDesignMenu.J_affine` is affinity of `S + w E` in the stake. It is not
  the invariance of `aJ + b`, and it is not used as a substitute.
- `LundbergCertified`, `Bmin`, and `Bslack` stay as they are. The menu that
  moves with the numerical cost is a separate two-design witness.

## Paper claims with no formalization, by later batch

Batches after batch 2 have no declaration in `formal/lean/GTAO/`.
Batch 2 is listed under **Batch 2 declarations**. Naming a nearby lemma
in the list above is not a formalization of a later claim.

### Batch 2: heat and repair floors, T59, T60, T63

- **T59** ([`OPEN_WORK.md:110`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L110)). Under Proposition JP-heat with local detailed
  balance, memory-bath heat satisfies `Q̇_M ≥ kT · r · L(ε)` in that class.
  At `r = 0` a static bias is at equilibrium and the ongoing floor is 0.
  Metastable retention is a lifetime, not a steady heat floor.
- **T60** ([`OPEN_WORK.md:111`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L111)). For an exogenous finite-state world,
  `I_alt = ∑ π(x) W_X(x→x') D_KL(p(M|x) ‖ p(M|x'))`. The claim that this flow
  is strictly positive whenever the world is not frozen and the Bayes error
  is below `ε_0` is false. On a strongly connected occupied flux graph,
  `I_alt = 0` implies `ε = ε_0`. On the telegraph, `I_alt ≥ r L(ε)`.
- **T63** ([`OPEN_WORK.md:114`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L114)). Repair floor in class RF: averaged dissipated
  power is at least `4 kT Γ (ln 2 − h(ε)) − kT S_max/τ` for carriers that each
  leak at rate at least `Γ`. One carrier gives the telegraph floor. A finite
  fully leaky scheme forgets. The cooperative-media loophole in `d = 2, 3` is
  part of the claim and is not formalized.

Update (LEAN-PHYS): the T60 pairwise and path bounds, the telegraph lower
bound, and the T63 product inequality on `{0,1}^n` now have declarations;
see **LEAN-PHYS declarations** at the end. The telegraph equality and its
converse, the decoder bound for two record distributions, and the
Schnakenberg integral are still not declarations.

### Batch 3: T58, T50, T68, the OU lift, and the clock

- **T58** ([`OPEN_WORK.md:109`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L109)). For an overdamped Einstein spring coupled to a
  random walk, the Kalman–Bucy-matched choice pays bath heat `2 kT r̄`. A fast
  spring at the same error drives the heat to the infimum `kT σ²/(2ε)`, where
  that identification does not hold. `DriftSelection` is not this statement:
  it takes the OU moment equations as inputs and proves a trace identity.
- **T50** ([`OPEN_WORK.md:101`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L101)). Joining the predict-act-correct loop:
  AF-scale, AF-convex, the bet-class value, AF-homeostatic, and AF-rate, in
  the named class. Not as a general claim outside that class.
- **T68** ([`OPEN_WORK.md:119`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L119)). Class CK: an internal clock is optimal if and
  only if the look price exceeds a stated multiple of `κ kT b/a` (6, 4, or
  the Poisson variant). The onset is a scoring convention inside that class.
  `LayerLifetime` is a refresh interval for a lumpy layer, not this clock.

### Batch 4: T73 and T74, quantum record price

- **T73** ([`OPEN_WORK.md:123`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L123)). Class PB, one projective record of a dephased
  qubit. At complete dephasing the relative-entropy minimizer is `θ = 0` for
  every stake. The Holevo predicate is false. A stake off the dephasing axis
  moves the relative-entropy minimizer only in the partial-dephasing numerical
  case. At equal coefficients the record terms are flat in `θ`.
- **T74** ([`OPEN_WORK.md:124`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L124)). No route among the five fixes `κ_D/κ`. The
  one-scale sentence multiplies the whole sum. The ratio stays a free
  nonnegative price. Batch 1's one-scale declaration is that multiplier. It
  is not a formalization of T74, and it does not set the ratio.

### Batch 5: structural lemmas T32, T33, T44, T51, T64, T65

- **T32** ([`OPEN_WORK.md:83`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L83)). Lyapunov lemma for the general form under
  H1–H3. Occupation of the front is not proved. GF5 is not a certificate.
  This is not CT32; CT32 is a different item and is also not formalized.
- **T33** ([`OPEN_WORK.md:84`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L84)). Growth bridge: on a gapped finite menu, weak
  selection recovers the ranking only; the diffusion limit keeps `μ − σ²/2`;
  an interior stake separates the argmaxes. GB2, GB3, GB5, and GB6 are false
  as unscoped identities. This T33 is not THEORY CT33. CT33 is already in
  `GTAO/CT33.lean`.
- **T44** ([`OPEN_WORK.md:95`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L95)). In the equilibrium Gaussian field, the
  conditional distribution of the exterior given the region and the blanket
  equals the distribution given the blanket. Interior decisions are not
  boundary-sufficient.
- **T51** ([`OPEN_WORK.md:102`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L102)). Swarm rule in the telegraph class: stay
  condition `λ s c < w Φ`, alignment `s = w/W`, and tampering priced as one
  more action. Unshared collateral or a binding ruin cap is outside that case.
- **T64** ([`OPEN_WORK.md:115`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L115)). Barrier route: retention error is at least
  `π(A1) (1 − e^{−λ₂ τ})` for a reversible medium, and the Eyring–Kramers
  reading needs a barrier at least `kT ln(ν τ / ε)`. A1 is not automatic.
- **T65** ([`OPEN_WORK.md:116`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L116)). A1 fails in the destruction channel for a
  sphaleron-protected record, under the stated Standard Model inputs. The
  cap without A1 stays open in the transport channel.

## Batch 1 declarations

These are the declarations added in this batch. They reuse
`Equipartition.gibbs_excess_quadratic`, `Equipartition.homogCost_quadratic`,
`Equipartition.integrable_exp`, `Equipartition.integrable_moment`,
`LayerLifetime.Tstar`, `LayerLifetime.Tstar_isMin`, `LayerLifetime.Tstar_unique`,
and Mathlib's `klDiv`, `klDiv_eq_zero_iff`, `klDiv_map_le`,
`klDiv_compProd_eq_add`. None of those is restated. The 354 declarations
above are unchanged.

Labels match `formal/lean/README.md`. **Faithful** means the checked
statement is the paper sentence, with every extra hypothesis named.
**WEAKER** means a clause of the paper sentence is not in the declaration.

### `GTAO/Cauchy.lean` (26)

Lemma C, Lemma P, Lemma C on the nonnegative integers, and Lemma M.
All **Faithful**. The auxiliary names (`mul_nat`, the rational bounds,
the squeeze) are the proof of Lemma C, not a second statement.
`IndependentOf` and `price_zero_of_independent` quantify over strictly
positive vectors. The witnesses are the constant-`1` vector and the
vector that is `2` in the ignored coordinate.

`AdditiveOnPos`, `Concatenates`, `mul_nat`, `cauchy_rat`,
`f_one_nonneg_of_nondecreasing`, `f_one_nonpos_of_nonincreasing`,
`below_gap`, `above_gap`, `ratBelow`, `ratAbove`, `ratBelow_bounds`,
`ratAbove_bounds`, `tendsto_mul_div`, `tendsto_mul_div_above`,
`tendsto_ratBelow`, `tendsto_ratAbove`, `eq_of_squeeze`,
`cauchy_monotone`, `cauchy_continuous`, `pexider_monotone`,
`pexider_continuous`, `cauchy_nat`, `slope_nonneg_of_nondecreasing`,
`Represents`, `IndependentOf`, `price_zero_of_independent`.

### `GTAO/Representation.lean` (17)

| Name | Label |
|---|---|
| `DebreuAdditive`, `r1_linear_components` | **Faithful** packaging. Debreu's conclusion, `n ≥ 3`, and Pexider are hypotheses. |
| `r1_vnm_scale` | **WEAKER.** Two writings of one index agree. Debreu's scale is not identified with the currency scale. |
| `r1_nonneg_of_A8` | **Faithful.** A8 gives nonnegative prices. |
| `r1_zero_of_not_essential` | **Faithful.** Wraps `price_zero_of_independent` on the positive orthant. |
| `r1_with_layer_count` | **Faithful.** Separability of `K` is a hypothesis. |
| `r1_layer_price_nonneg_of_A8` | **Faithful.** A nondecreasing concatenating count has `fn 1 ≥ 0`. |
| `negative_price_example` | **WEAKER.** Arithmetic and continuity of `z₀ + z₁ − z₂` only. A1–A7 are not checked. |
| `IsArgmin`, `affine_argmin_iff`, `strictMono_argmin_iff` | **Faithful.** |
| `affine_excess_scale`, `affine_excess_eq_iff` | **Faithful.** Reuses `gibbs_excess_quadratic` on the fixed weight of `J`. |
| `affine_excess_refit` | **Faithful.** Refit `β/a` on `a • H`. |
| `fractional_excess_scale`, `fractional_excess_shift` | **Faithful** for `b = 0` and for the rationals `E[J] = 2`, `J* = 1`, `b = 1`. The general quotient is not a theorem. |
| `constrained_argmin_not_affine` | **Faithful.** The two-design margin witness. Does not rewrite `LundbergCertified`. |

### `GTAO/Obstruction.lean` (16)

| Name | Label |
|---|---|
| `sharedGrowth`, `kelly_qstar`, `log_le_tangent`, `log_lt_tangent`, `kelly_foc_sign` | **Faithful.** `q* = 13/50` is the unique maximizer on `(0, 1]`. |
| `kelly_not_expected_factor` | **Faithful.** `247/200` against `417/400`. Pure lean is the linear maximizer. |
| `intervalCost`, `expected_cost_interval` | **Faithful.** Unique minimizer `√(1/10)`, via `LayerLifetime.Tstar`. |
| `phi`, `quintic`, `cubic`, `quintic_eq_phi`, `hasDerivAt_quintic`, `cubic_neg`, `quintic_anti` | **Faithful** polynomial arithmetic for the numerator of the interval comparison. |
| `survival_interval_lt` | **WEAKER.** The unique zero of `φ` on `(0, 2]` lies below `√(1/10)` inside the rational brackets. Maximality of `θ` is not proved. See `BATCH1_PLAN.md`. |

### `GTAO/ContinuousA6.lean` (16)

| Name | Label |
|---|---|
| `klDiv_prob_integral` | **Faithful.** Absolute continuity and integrability of the log-likelihood give `ENNReal.ofReal` of the integral. |
| `klDiv_nonneg` | **Faithful** to `0 ≤ klDiv` in `ℝ≥0∞`. The integral's nonnegativity is a different fact. |
| `klDiv_zero_iff_eq` | **Faithful** for the divergence. The mutual-information biconditional is not a separate declaration. |
| `mutualInfo`, `mi_swap`, `mi_data_processing` | **Faithful.** Swap and `klDiv_map_le`. |
| `klDiv_compProd_chain` | **Faithful** to Mathlib's kernel chain rule. Not the mutual-information chain rule. |
| `partitionMI`, `partition_mi_le`, `refinement_mono`, `finite_identity_attains` | **Faithful.** |
| `FiniteLabel`, `finitePartitionMI`, `finite_partition_le` | **Faithful.** |
| `GYDSup`, `gyd_equiv` | **Faithful** hypothesis. The reverse inequality is assumed. `gyd_equiv` is that assumption plus the proved bound. |

Batch 1 adds 75 source declarations: 72 **Faithful** and 3 **WEAKER**
(`negative_price_example`, `r1_vnm_scale`, `survival_interval_lt`).
The axiom audit on this tree reports 926 `GTAO` constants, up from 757,
and only `propext`, `Classical.choice`, and `Quot.sound`. The audit
counts every generated constant, so 926 is larger than 354 + 75.

## Batch 2 declarations

These are the declarations added for the heat and repair floors.
The 354 declarations and the 75 batch 1 declarations above are unchanged.
Labels match `formal/lean/README.md`. **Faithful** means the checked
statement is the paper sentence, with every extra hypothesis named.
**WEAKER** means a clause of the paper sentence is not in the declaration.
Each WEAKER row is also a miss in the appendix of `formal/lean/BATCH2_PLAN.md`.

Batch 2 adds 125 source declarations: 121 **Faithful** and 4 **WEAKER**.

### `GTAO/HeatFloor.lean` (45)

All **Faithful**. The two-state floor, the cancellation of the leak, the
frozen equilibrium, the barrier sign, and the copy-cap comparison.
`jp_heat_floor` is the one-edge budget `Q̇ = kT (σ + I_alt)` with `σ`
the entropy production of that edge. A general bipartite generator is
not a declaration.

`errorDot`, `steadyEps`, `steadyMu`, `L`, `binaryEntropy`, `fairInfo`,
`copyBracket`, `iAltTwoState`, `edgeEntropy`, `memoryHeat`, `kramersRate`,
`barrierWork`, `copyCapEps`, `L_zero_at_half`, `L_one_fifth`, `L_nonneg`,
`L_pos`, `steady_mu_dot_zero`, `steady_unique`, `kolmogorov_error_dot`,
`bracket_eq_world`, `iAlt_eq_rate_L`, `floor_independent_of_barrier`,
`edgeEntropy_nonneg`, `edgeEntropy_eq_zero_iff`, `memoryHeat_ge_info`,
`jp_heat_floor`, `frozen_flux_balance`, `frozen_heat_zero`,
`hasDerivAt_mul_log`, `hasDerivAt_one_sub`, `hasDerivAt_compl_log`,
`hasDerivAt_binaryEntropy`, `hasDerivAt_fairInfo`, `destroyDeriv`,
`kramersRate_pos`, `iAlt_of_kramers`, `barrierWork_zero`, `barrierWork_pos`,
`steady_ge_copyCap`, `copy_cap_gap`, `copy_cap_near_half`,
`hasDerivAt_log_ratio`, `hasDerivAt_L`, `L_antitone`.

### `GTAO/FiniteFloor.lean` (34)

| Name | Label |
|---|---|
| `Nonneg`, `AC`, `Prob`, `klSum`, `kl`, `klSum_nonneg`, `kl_nonneg`, `kl_eq_top_of_not_ac`, `kl_eq_ofReal`, `klTerm_expand`, `klSum_eq_sum_log`, `kl_zero_iff` | **Faithful.** `kl` is `⊤` when a positive atom meets a zero atom. |
| `totalVariation`, `totalVariation_nonneg`, `flux`, `stationary`, `flux_nonneg`, `flux_off_support` | **Faithful.** |
| `worldSum`, `worldSum_stationary` | **Faithful.** Stationarity cancels the world sum, including states with zero mass. |
| `iAltReal`, `iAlt`, `ennreal_sum_eq_zero`, `iAlt_nonneg`, `iAlt_eq_top_of_singular`, `iAlt_zero_iff_edge` | **Faithful.** A positive flux into a singular pair makes `iAlt = ⊤`. Zero iff every positive-flux edge has `kl = 0`. |
| `infoX`, `destruction_identity` | **WEAKER.** The real expansion requires every world mass and every conditional atom to be strictly positive. The note's `0 log 0` extension of that expansion is not this identity. `FiniteFloor.lean:320`. |
| `stationary_learning_rate` | **WEAKER.** Same missing clause: `iAltReal = -infoX` only under that strict positivity. `FiniteFloor.lean:373`. |
| `bayesError`, `chanceError`, `sup'_witness_irrelevant`, `le_sup'_univ`, `bayes_of_constant` | **Faithful.** A constant conditional gives `ε = ε_0`. |

### `GTAO/FiniteFloorBounds.lean` (19)

All **Faithful**. `frozen_support`, `boltzmann_below_half` (`1/(1+exp 1) < 1/2`; the printed soft-memory decimal is not an equality), `PosFlux`, `Reach`, `stronglyConnected`, `reach_same_conditional`, `iAlt_zero_stronglyConnected`, `sup_fin3`, `classπ`, `classW`, `classP`, `classP_prob`, `classP_same`, `two_class_counterexample` (`ε = 3/10`, `ε_0 = 3/5`, `I_alt = 0`), `cycleπ`, `cycleW`, `cycleP`, `cycle_flux01`, `converse_fails_three` (`ε = ε_0` and `I_alt > 0`).

The telegraph lower bound, the pairwise `L` bound, and the path bound are not declarations.

### `GTAO/RepairFloor.lean` (27)

| Name | Label |
|---|---|
| `log_sub_log_le`, `log_sub_log_lt`, `infoDeriv`, `infoDeriv_nonpos`, `infoDeriv_neg`, `hasDerivAt_infoGap`, `infoGap_half`, `infoGap_anti`, `infoGap_strictAnti`, `L_ge_four_entropy`, `L_eq_four_entropy_iff`, `fairInfo_half`, `fairInfo_antitone`, `fairInfo_strictAnti`, `fairInfo_nonneg` | **Faithful.** `L(ε) ≥ 4 (log 2 - h(ε))` on `(0, 1/2]`, with equality exactly at `1/2`. |
| `oneCarrierSigma`, `one_carrier_floor` | **Faithful.** One carrier, `σ = Γ L(ε)`. |
| `repair_floor_of_average` | **WEAKER.** The algebra of an assumed average `σbar`. The Schnakenberg integral is not constructed. `RepairFloor.lean:303`. |
| `long_horizon` | **Faithful.** `S_max / τ` can be made smaller than any positive allowance. |
| `rf_forget_stationary` | **WEAKER.** The two decoded errors of a bit-independent state sum to 1, so they cannot both be `≤ ε < 1/2`. The trajectory limit is not this theorem. `RepairFloor.lean:336`. |
| `rf_cap`, `rf_cap_entropy`, `rf_cap_chain` | **Faithful.** `q` is an input. |
| `bernoulli`, `decoder_half`, `decoder_pair`, `decoder_pair_lower` | **Faithful** for one binary source. The sum of two record distributions against the uniform, after data processing, is not a declaration. |

The axiom audit after these declarations reports 1185 `GTAO` constants,
up from 926, and only `propext`, `Classical.choice`, and `Quot.sound`.
The audit counts every generated constant, so 1185 is larger than 354 + 75 + 125.

## LEAN-PHYS declarations

Planned in `formal/lean/LEAN_PHYS_PLAN.md` before any proof (commit
`07ce4e5`). Labels as in the batch 2 section. Each **WEAKER** row is a miss
in the miss log of that plan. The aggregate audit count is not per-claim
coverage; the rows below are.

LEAN-PHYS adds 71 source declarations: 67 **Faithful** and 4 **WEAKER**.

### `GTAO/DiffusionHeat.lean` (10)

| Name | Label |
|---|---|
| `current`, `learningRate`, `shannonRate`, `entropyProduction`, `EQHeatHyp` | **Faithful** definitions. `EQHeatHyp` names every assumption: `D > 0`, `p > 0`, the score split, integration by parts, the marginal-entropy identity, and five integrability facts. |
| `entropyProduction_nonneg`, `integrand_eq` | **Faithful.** |
| `eq_heat_identity`, `eq_heat_steady`, `eq_heat_floor` | **WEAKER.** `Σ = Sr − İ + dS`, `İ ≤ Sr` when `dS = 0`, and `kT İ ≤ D Sr` when `kT = D`, on any measure space. Integration by parts and the marginal-entropy identity are hypotheses, not derived from the SDE. Miss LP-eqheat. `DiffusionHeat.lean:102`. |

### `GTAO/FiniteFloorPairwise.lean` (16)

All **Faithful**. `log_sum_le`, `edge_superadd`, `overlap`,
`klSum_eq_sum_log_of_ac`, `binary_jeffreys`, `jeffreys_ge_two_L`,
`overlap_le_bayes`, `edges_le_iAltReal`, `edges_le_iAlt`,
`ofReal_edges_le_iAlt`, `pairwise_L_edges`, `pairwise_L`,
`pairwise_L_ennreal`, `telegraphπ`, `telegraphW`, `pairwise_telegraph`.
`pairwise_L_ennreal` is the paper's pairwise bound on `iAlt` with no
extra hypothesis; `pairwise_L` is its real form under absolute
continuity in both directions. `pairwise_telegraph` is the telegraph
lower bound `r L(ε) ≤ I_alt` for `ε < 1/2`; equality and the converse are
not declarations.

### `GTAO/FiniteFloorPath.lean` (34)

All **Faithful**. `binKl`, `logitGap`, `logitGap_mono`, `pinskerGap`,
`binKl_eq_gap`, `continuous_pinskerGap`, `hasDerivAt_pinskerGap`,
`binary_pinsker`, `mul_log_div_anti`, `pinsker`, `totalVariation_self`,
`totalVariation_triangle`, `totalVariation_eq_sum_pos`, `walkEdges`,
`walkEnd`, `tv_walk_le`, `list_sum_eq_count`, `joint_sum`,
`bayes_le_chance`, `chance_sub_bayes_le`, `PathSystem`, `pathWeight`,
`pathK`, `pathWeight_nonneg`, `flux_pos_of_weight`,
`chance_sub_bayes_le_weights`, `path_pinsker_edges`, `path_pinsker`,
`path_pinsker_ennreal`, `walk_of_reach`, `pathSystem_exists`,
`path_pinsker_stronglyConnected`, `telegraphPaths`, `telegraph_K`.
`pathWeight` counts an edge with its multiplicity in a walk; on walks
with no repeated edge it is `√2 c_e`. `path_pinsker` takes absolute
continuity on used edges; `path_pinsker_ennreal` takes none.

### `GTAO/RepairTensor.lean` (11)

| Name | Label |
|---|---|
| `flipAt`, `cubeSigma`, `cubeD`, `flipAt_zero_cons`, `flipAt_succ_cons`, `sum_cube_succ`, `cubeSigma_smul`, `cubeSigma_succ`, `one_carrier_bound`, `cubeD_succ` | **Faithful.** |
| `cube_tensorization` | **WEAKER.** `4 g D(p‖u) ≤ σ_Γ[p]` for every `n` and leak rates `Γ_i ≥ g ≥ 0`, for strictly positive `p`. The zero-atom case, where the note's `σ` is `+∞`, is miss LP-tensor-zero. `RepairTensor.lean:162`. |

The axiom audit after these declarations reports 1370 `GTAO` constants,
up from 1185, and only `propext`, `Classical.choice`, and `Quot.sound`.
The audit counts every generated constant, so 1370 is larger than
354 + 75 + 125 + 71.
