# T82e run log

Locked file: `theory/torus-memory-2026-11-24/PREREG_T82E.md`

sha256: `748514c79a5dd1d3393614207f9c0a814f1a49969da453bdf5af4fe37bbb4421`

The scored script has not been run. Scores, when they exist, are appended below this line and this paragraph is not rewritten.

## Ledger, appended 2026-11-24 17:10 ET

Scoreboard `t82e_checks.out`. The paragraph above is unchanged. Odds for a false three-point plateau, under the locked null, are 0 (`PREREG_T82E.md:86`). Location is `model` on every row. Signed size is outcome minus the locked value.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82e-P-width | One 1/1 plateau at each of 0.01, 0.04, 0.09, containing omega_2=1, width within 30 percent of 0.282842712475, 0.565685424949, and 0.848528137424. Null probability of a false three-point plateau is 0. | At 0.01, one plateau, width 0.285000000000. At 0.04, 4 plateaus. At 0.09, 9 plateaus. | The 0.01 width is a hit, signed +0.002157287525. The row misses: +3 plateaus at 0.04, +8 plateaus at 0.09. | model | high | The resonance thread on this toy is shelved. The next look is whether the continuous record is a smooth coordinate of the conserved actions, in a new preregistration. No edit to this lock or this scoreboard. | none |
| T82e-P-scale | W(0.04)/W(0.01) in [1.4, 2.6]. Locked center 2. The linear rival 4 is outside the interval. | The 0.04 width is not one plateau, so the ratio is not formed. | Miss. The ratio minus 2 is undefined. | model | high | Same shelf as T82e-P-width. | none |
| T82e-P-higher | Plateau count 0 for denominators 2, 3, 4, and 5, at each positive coupling. | Counts 0, 0, 0. | HIT. Count residual 0. | model | low | none yet. The extra plateaus are still at 1/1. | none |
| T82e-P-eps0 | At coupling 0, the number of grid values with rotation number within 0.002 of 1 is at most 1. | Count 1. | HIT. Signed size 0. | model | low | none yet | none |
| T82e-P-record | Absolute cost gap at least 0.002 between omega_2=1 and the mean of the first samples outside the one 1/1 plateau, at coupling 0.04 and stake 2. | The gap is not formed. | Miss. There is not one plateau (4 blocks), so the exterior pair is not defined. | model | medium | The cost is not read as a resonance detector from this run. Same shelf as T82e-P-width. | none |
| T82e-P-refine | At coupling 0.04, step 0.025 and grid step 0.0025, one 1/1 plateau contains omega_2=1 and its width is within 30 percent of the coarse width. | 4 fine plateaus. | Miss. +3 fine plateaus. The width comparison is not formed. | model | medium | The finer grid does not restore one plateau. No edit to the lock. | none |
