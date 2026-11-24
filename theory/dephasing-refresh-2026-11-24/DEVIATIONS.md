# Deviations

`PREREG.md` is unchanged after commit `612b82e` (sha256 `b2e96d76234da1e4a2521b990bb9cf456ca1c9c60a334ebf475f49b159dcab8f`). No prediction, bar, grid, or sign was edited after the run. No deviation.

`ADDENDUM_PREREG.md` is unchanged after `9619565` (sha256 `62871c9de3ad1d29046d2f73162139b5f0ae4d897a3204ca05859f3a9c5e63b2`). `ADDENDUM_REVIEW_PREREG.md` is unchanged after `6fb397b` (sha256 `fc82c94bcf0ff3e639d6512475d8060228164b27c0a8f973dc4adc0b1f371dfd`).

## Ledger

**Lock reference:** `612b82e`, `9619565`, `6fb397b` on `forge-dephasing-refresh`  
**Logged at (ET):** 2026-11-24 16:28 ET  
**Breach check:** `none` (the three locks are unedited; no post-hoc prediction patching)

Rules: `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` on upstream `652d936`. This table is append-only. Identities of a locked cost are consistency checks: a hit there has almost no information. A hit that excludes a named alternative is the row with information.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| R0 | closed forms, abs gap ≤ 1e-9 | max derivative gap 1.550e-11 | HIT, inside band by 9.8e-10 | model | low | none yet | none |
| R1 | A and B share one boundary | agree to 1.137e-13 | HIT, identity of the locked rate | model | low | none yet | none |
| R2 | Pi_c(0.01) within 1e-6 of the series, and < 4.05; limit 4 | 4.02674456, gap 1.186e-7 | HIT, inside band | model | low | none yet | none |
| R3 | short-period ratios within 5e-3 of 1 | 1.003338 and 0.998337 | HIT, residuals +0.003338 and -0.001663 | model | low | none yet | none |
| R4 | e(0.01)<0.505, e(0.5)<0.55, e(1)>0.55 | 0.50083, 0.54149, 0.58198 | HIT, e(1) is +0.03198 above 0.55 | model | low | none yet | none |
| R5 | accounting C tends to 16, not the finite-hold threshold | 16.001600 at 1e-4; 16.160893 at 0.01 | HIT, inside the locked window | model | low | none yet | none |
| R6 | Gaussian-envelope share = 1/3 within 1e-12 | gap 5.551e-17 | HIT, rival exponent 1/2 excluded by 1/6 | model | medium | none yet | none |
| R7 | unitary H_u=A doubles the small-window Pi, series within 2e-6 | 8.05348913, gap 2.372e-7 | HIT, inside band | model | low | none yet | none |
| R8 | clock heat does not lower the rate; CK onset = 4 kT at kappa=1 | onset 4.0; probe heat positive | HIT, rival "lowers the rate above 4 nats" excluded | model | medium | none yet | none |
| R9 | t falls and Pi_c rises; difference changes sign | t(0.01)=6.300822, Pi=4.026745; t(1)=1.973877, Pi=7.568845 | HIT, not the same boundary | model | medium | none yet | none |
| A0 | stock floor = ln 2; gap to 4 nats ≥ 3; gap to a clock at rest ≥ 0.5 | F=0.693147180560; gap 3.306853 | HIT, +3.306853 nats from the onset | model | medium | none yet | none |
| A1 | alt-onset misses bar B2; alt-frozen misses bar B3 | both miss those bars | HIT, the two readings separate | model | medium | none yet | none |
| K0 | T84 prereg has no `w^{1/2}` and no `T_hold` | both absent | HIT, no square-root exponent was locked in T84 | model | low | none yet | none |
| K1 | t(2, 1/2)=t(1/2, 2)=t(1), and t(0.01)>t(1)>2 ln 2 | 1.973877; floor 1.386294361120 | HIT, depends on gamma and T only through the product | model | medium | none yet | none |
| K2 | elasticity at gamma tau=1, w=2 is within 1e-5 of 0.901222, and ≥ 0.3 from 1/2 | 0.901222 | HIT, residual 0 inside the band; +0.401222 from 1/2 | model | medium | none yet | none |
| K3 | squared Hamming: share = 1/3 within 1e-12; critical Pi at gamma T=0.01 equals 600 and exceeds 100 | share 0.333333; Pi 600 | HIT, share is -0.166667 from 1/2; Pi is +596 from 4 | model | medium | none yet | none |
| K4 | five nearby one-shot costs flip the locked signs | carrier 0.939924; leak threshold 0.193085; squared J_H 0.269071; rent gap 1.239472; coherence threshold 3.436564 | HIT, each sign is the opposite of the locked one-shot sign | model | medium | none yet | none |

### Scaled notes (medium only)

1. **R6, R8, A0, A1, K3, K4.** Locked against a named alternative: Gaussian or squared Hamming keeps exponent 1/2; a clock heat lowers the refresh rate once the look exceeds 4 nats; the noiseless floor equals that onset; accounting C's 16 is the finite-hold threshold; the one-shot signs survive a nearby cost. Outcomes sit on the other side of each of those rivals. Location is the model. No formula was changed after the lock.
2. **K1, K2, R9.** The T84 threshold is the endpoint comparison \(R(D)=\ln 2-h(D)\) under Hamming loss. It moves only with \(\gamma T\). The printed-cell elasticity is 0.901222, not \(1/2\). The square-root refresh balance is a separate rate, and its \(w^{1/2}\) is the elementary reset balance, not a lock inside T84.
3. **Update.** None yet. The hits match the locks. Repeating them would not move a formula. Parent identities of the linear time average stay consistency checks.

## Ledger, onset lock and reclassification

**Lock reference:** `a27520c` (sha256 `659ed3e67e40bc03aef71bb69c694eb91e3ee0049a7e907570945d9fd42760fb`) for M1–M4. The 16-versus-4 and holding-floor rows restate candidate claims already scored above. Those earlier rows are not edited.  
**Logged at (ET):** 2026-11-24 16:45 ET  
**Breach check:** `none`

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| ACE-16 | candidate small-window threshold ~16 (odds not stated by the candidate) | symmetric \(\Pi_c\to 4\); accounting C \(\to 16\) | miss \(-12\): the symmetric threshold is 12 below the candidate | model | medium | score class RF on the symmetric limit; 16 is accounting C only | none |
| CLOCK-FLOOR | holding floor identified with the 4-nat onset | \(\ln 2=0.693147180560\) | miss \(-3.306853\) nats | model | medium | the two expressions stay distinct | none |
| M1 | both pure numbers within 0.05 of 4; \(c^*\) within 1e-12 of 4 | \(\Pi_c(0.01)=4.02674456\), \(c^*=4\) | HIT, residual \(+0.02674456\); this is the integer match and does not exclude the rival | model | low | none yet | none |
| M2 | stake elasticity of \(A_c\) within 0.05 of 0; rival weight 4:1 | \(e_A=+1.00000000\) | miss \(+1.00000000\) | model | medium | do not identify \(\Pi_c\to 4\) with \(c^*\) | none |
| M3 | both age slopes within 1e-9 of \(1/4\); rival weight 4:1 | uniform \(0.2500000000\); exponential \(0.4999999983\) | miss \(+0.2499999984\) on the exponential slope; uniform slope is inside the band | model | medium | the Poisson age is not the refresh age | none |
| M4 | half-slope limit within 0.05 of 4; rival weight 4:1 | limit \(8\) | miss \(+4\) | model | medium | the refresh 4 follows the loss slope | none |
| R0 | closed forms, abs gap ≤ 1e-9 | max derivative gap 1.550e-11 | HIT, unchanged | model | low | none yet | none |
| R1 | A and B share one boundary | agree to 1.137e-13 | HIT, unchanged | model | low | none yet | none |
| R2 | \(\Pi_c(0.01)\) inside the series band; limit 4 | 4.02674456 | HIT, unchanged; the limit 4 is the Hamming expansion | model | low | none yet | none |
| R3-tau | short-period \(\tau^*\) ratio within 5e-3 of 1 | 1.003338 | `NOT A TEST`; residual \(+0.003338\); square-root/EOQ identity | model | low | gate corrected below the earlier HIT row | none |
| R3-J | short-period \(J^*\) ratio within 5e-3 of 1 | 0.998337 | `NOT A TEST`; residual \(-0.001663\); same identity | model | low | gate corrected below the earlier HIT row | none |
| R4 | elasticity bars \(e(0.01)<0.505\), \(e(0.5)<0.55\), \(e(1)>0.55\) | 0.50083, 0.54149, 0.58198 | HIT, unchanged | model | low | none yet | none |
| R5 | accounting C tends to 16 and is not the finite-hold threshold | 16.001600 and 16.160893 | HIT, unchanged; this is the same split as ACE-16 | model | low | none yet | none |
| R6 | Gaussian-envelope share = 1/3 within 1e-12 | gap 5.551e-17 | HIT, rival exponent 1/2 excluded by 1/6 | model | medium | none yet | none |
| R7 | unitary heat doubles the small-window \(\Pi\) | 8.05348913 | HIT, unchanged | model | low | none yet | none |
| R8 | clock heat does not lower the refresh rate | onset 4.0; probe heat positive | HIT, unchanged | model | medium | none yet | none |
| R9 | \(t\) falls and \(\Pi_c\) rises | sign change between 0.01 and 1 | HIT, unchanged | model | medium | none yet | none |
| A0 | stock floor \(\ln 2\); gap to 4 nats ≥ 3 | gap 3.306853 | HIT on the separation bars; the identification those bars reject is CLOCK-FLOOR | model | medium | none yet | none |
| A1 | the two alternative readings miss their bars | both miss those bars | HIT, unchanged | model | medium | none yet | none |
| K0 | T84 prereg has no \(w^{1/2}\) and no \(T_{\mathrm{hold}}\) | both absent | HIT, unchanged | model | low | none yet | none |
| K1 | \(t\) depends on \(\gamma T\) only | 1.973877; floor 1.386294361120 | HIT, unchanged | model | medium | none yet | none |
| K2 | printed-cell elasticity within 1e-5 of 0.901222 | 0.901222 | HIT, unchanged | model | medium | none yet | none |
| K3 | squared Hamming share 1/3 and critical \(\Pi=600\) | share 0.333333; \(\Pi=600\) | HIT, unchanged | model | medium | none yet | none |
| K4 | five nearby one-shot costs flip the signs | five flipped cells | HIT, unchanged | model | medium | none yet | none |

### Scaled notes for this block

1. **ACE-16 and CLOCK-FLOOR.** The candidate 16 is 12 above the symmetric threshold and matches accounting C only. The holding floor is 3.306853 nats below the 4-nat onset. Both sit in the model. The update is the label, not a new formula: class RF keeps \(\Pi_c\to 4\), and the holding floor stays \(\ln 2\).
2. **M2, M3, M4.** Prediction weight on the identity was 0.2 against the rival. The boundary price moves one-for-one with the stake. The Poisson age changes the slope from \(1/4\) to \(1/2\). Halving that slope moves the refresh limit from 4 to 8 and leaves \(c^*=4\kappa kT\) where it was. Location is the model. No measurement gate fired. The update is to stop calling the symmetric 4 the Poisson onset.
3. **R3-tau and R3-J.** The short-time loss is linear in the age, so the rate is the square-root/EOQ balance (`theory/INTERNAL_MODEL.md:45`, `:180`; `theory/CLOCK_TERM_2026-11-23.md:55`), not the CK lag balance (`theory/CLOCK_TERM_2026-11-23.md:40-47`, `:55`). Those two ratios are `NOT A TEST`. The earlier R3 row stays as it was written.
