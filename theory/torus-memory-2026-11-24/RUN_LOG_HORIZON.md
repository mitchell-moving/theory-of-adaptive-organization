# T82c run log

Locked file: `theory/torus-memory-2026-11-24/PREREG_HORIZON.md`

sha256: `abb56169340490e2a420d47f5c0cb556e90e86caf720a2a86d5423a4c5ee85d9`

The scored script has not been run. Scores, when they exist, are appended below this line and this paragraph is not rewritten.

2026-11-24, after the scan. `horizon_checks.out` has FAILS 4: P-res, H-flow, H-walk, H-gamma. P-port and H-label pass. The period-2 horizons are 500-505, 555-558, 613-615, and 674.

## Ledger, appended 2026-11-24 16:50 ET

Independent review, fork PR #16 comment 7145388655. Lock `af44b86`. Breach check: none. Odds were not locked on every row. Location is `model` on every row. Signed size is outcome minus the locked value. The sentences above this heading are unchanged.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82c-P-port | T=500 is a period-2 cycle at 0.288952 and 0.291620, step 2.668522e-3, widths 7 and 8. Odds not locked. | Levels 0.288951536270 and 0.291620058685. Widths 7 and 8. | HIT. Level residuals -4.64e-7 and +5.87e-8. | model | low | none yet | none |
| T82c-P-res | One period-2 block containing 500, length at most 207, with a stopped horizon on each side. Odds not locked. | 4 blocks, 14 cycle horizons, 401 point, 0 set. Longest block length 6. | +3 blocks. The length cap is not crossed (6 versus 207). | model | medium | None to the lock or the scoreboard. The four islands are the boundaries between five width blocks, pairs (8, 7), (6, 5), (4, 3), (2, 1). They move with the floor offset and vanish without the floor. | none |
| T82c-H-label | End separation at least half the start separation. Odds not locked. | Ratio 1. | HIT. Margin +0.5 above the bar of 1/2. | model | low | none yet | none |
| T82c-H-flow | For each family, the smallest gap on t=20,...,100 is at least half the largest, and the rational gap stays at least the sqrt(2) gap. Odds not locked. | Rational smallest 0.193568186357. sqrt(2) smallest 0.047911800530. Golden smallest 0.055431257067. | sqrt(2): -0.066878241365 against half of its maximum. Golden: 0.055431257067 - 0.5*0.206368389085 = -0.0477529374755. Rational clause: HIT, margin +0.027190966732 above half of 0.332754439250. | model | medium | none yet | none |
| T82c-H-walk | At T=83069, each family keeps at least half of its T=415 gap. Odds not locked. | Both gaps are 0. | Rational -0.145933501381. sqrt(2) -0.042608989184. | model | medium | none yet | none |
| T82c-H-gamma | A sample on the locked grid reaches half of G0=0.076988268821, and the half-time sits in the locked window of ln 2 / gamma. Odds not locked. | No sample reaches the half. Last values 0.078924958230 and 0.064446909176. | +0.040430823820 and +0.025952774766 above the half line. The gap stays larger than the locked half. | model | medium | none yet | none |

### Scaled notes, stake medium

**T82c-P-res.** The count residual is +3 blocks. The longest block is length 6, inside the cap of 207. The same four horizons are the menu boundaries named on the resonance ledger. Update: none to the lock or the scoreboard.

**T82c-H-flow, T82c-H-walk, T82c-H-gamma.** The rational flow clause hits. The two irrational flow gaps, both walk gaps, and both damping samples miss by the signed sizes in the table. No update. The review did not move these bars.
