# P4-BAND-T results and hostile review: is the low edge a supply limit?

*Friday 27 November 2026 (EST). Prereg PREREG_P4BAND_T_2026-11-27.md (SHA-256 e2b3e3e7ae129cd37937aa35b8e2e49a576da3cc28fbcb1b47da4105766cea88, locked 00:59:37 EST). Amendment PREREG_P4BAND_T_AMENDMENT_2026-11-27.md (29baf43f…, 01:09:40 EST): the locked script crashed on a no-op loop after saving all runs and before printing any result; analysis ran from the saved runs with the rule unchanged. Outputs: supply_runs.json (42897836…), supply_test.out (crash), supply_analysis.out (f558242f…), supply_descriptive.out (post hoc). Fresh seeds 1501–1510, T 12000. In-model toy.*

## Results (mean A, ON)
| μ | 1e-6 | 3e-6 | 1e-5 | 3e-5 | 1e-4 | 3e-4 | 1e-3 | 3e-3 | 1e-2 | 3e-2 | 1e-1 | 3e-1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T 6000 (20 seeds, P4-BAND) | 0.0000 | 0.0008 | 0.0044 | 0.0074 | 0.0146 | 0.0162 | 0.0208 | 0.0232 | 0.0236 | 0.0171 | 0.0054 | 0.0034 |
| T 12000 (10 seeds) | 0.0000 | 0.0038 | 0.0018 | 0.0084 | 0.0147 | 0.0178 | 0.0284 | 0.0227 | 0.0225 | 0.0175 | 0.0052 | 0.0033 |

Edges (log10 μ, half of each run's max mean): T 6000 low −4.20, high −1.29; T 12000 low −4.04, high −1.38.

| Prediction | Numbers | Score |
|---|---|---|
| S1 low edge moves down with 2× run length (shift ≤ −0.15, CI upper < 0) | shift +0.16 (bootstrap 95% −0.50 to +0.83) | **FAIL (open miss)** |
| S2 high edge stays (|shift| < 0.15) | shift −0.10 (bootstrap −0.22 to +0.04) | **PASS** |

Post hoc, no weight: seeds with A > 0.005 at 3e-6, 1e-5, 3e-5, 1e-4, 3e-4 were 1/20, 6/20, 8/20, 16/20, 16/20 at T 6000 and 2/10, 2/10, 5/10, 8/10, 9/10 at T 12000. There is no clear doubling of success at the low side.

## Hostile review
1. **S1 is underpowered.** Ten seeds per μ and a bimodal low side give a bootstrap CI 1.3 decades wide. The point estimate goes the wrong way (+0.16), but a −0.30 shift is inside the CI. As registered, S1 fails; in substance, the supply reading is **not supported and not excluded**.
2. **The relative edge rule moves with the peak.** The T 12000 max mean is higher (0.028 at 1e-3, one μ only), which raises the half-max line and pushes the low edge up. That is a property of the registered rule, disclosed here, not a reason to rescore.
3. **The high edge is stable under 2× run length** (S2), consistent with it being a steady-state property of the toy (identity turnover outruns selection on timing), not a transient.
4. Same toy limits as P4-BAND.

## Plain words
- Doubling the run length did not move the band's top edge, so that edge looks like a real property of the toy.
- The bottom edge did not move the way a pure "readers haven't arrived yet" story predicts. The test was too small to settle it. Why readers fail at low novelty stays an open miss.
