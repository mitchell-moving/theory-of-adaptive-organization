# P4b results and hostile review: exclusive autocatalytic cores in compartments

*Thursday 26 November 2026 (EST). Prereg PREREG_P4b_2026-11-26.md, SHA-256 c1666f1e90bbc0687a57ef7e700ab9360a450d32502d9a62e3e2917f0d1acf57, locked 23:49:44 EST before the run. Raw output in p4b_test.out. One run, fresh seeds 501–505, no retries. All results are in-model, for a toy with lumped, hand-written cores.*

## Gate (gate.out)
Only 1 of 8 cells passed: τ 2, P 40, c_nat 0.01. In it the reader beat the hedger 4/5. Validity held: with a random cue the reader passed 0/5. Switching was about 0 in every cell, so the gate already showed it.

## Scored results (strict, ≥ 4/5 seeds)
| Prediction | Seeds | Score |
|---|---|---|
| (i-a) alternative stable states: ≥ 0.8 single-core compartments | 5/5 | PASS (0.998), but built in by β > 1 |
| (i-b) heredity: κ_ON ≥ 0.5 and κ_ON − κ_OFF ≥ 0.4 | 5/5 | PASS (κ 1.00 vs 0.00) |
| (i-c) Vasas-2012 core switching ≥ 0.001 per division | 0/5 | **FAIL (open miss)**: switching 0.000 |
| (ii-a) reader ≥ 0.5 and ≥ hedger + 0.1 | 4/5 | PASS (largely gate-implied); seed 503 went to the hedger at 0.96 |
| (ii-b) only with heredity: reader_ON − reader_OFF ≥ 0.25 | 4/5 | PASS (OFF sits at chance, 0.25) |
| (ii-c) only with a timed cue: RANDOM ≤ 0.30 and ON − RANDOM ≥ 0.25 | 4/5 | PASS (RANDOM mean 0.06) |
| (iii) price 10× gives reader ≤ 0.10 | 5/5 | PASS (mean 0.002) |
| (s) growth_ON ≥ 1.02 × growth_SIEVE | 1/5 | FAIL (0.069 vs 0.068) |

Arm means of reader / hedger / κ / switching / growth:

| Arm | reader | hedger | κ | switching | growth |
|---|---|---|---|---|---|
| ON | 0.673 | 0.278 | 1.000 | 0.000 | 0.069 |
| OFF | 0.247 | 0.249 | 0.002 | 0.749 | 0.068 |
| RANDOM | 0.055 | 0.147 | 1.000 | 0.000 | 0.068 |
| PRICE | 0.002 | 0.170 | 0.999 | 0.000 | 0.068 |
| SIEVE | 0.307 | 0.240 | 0.997 | 0.000 | 0.068 |

## Hostile review
1. **The heredity passes are mostly built in.** Cross-inhibition β > 1 makes each compartment one core, and nothing moves it. So κ ≈ 1 follows from the design, and κ_OFF ≈ 0 follows from the permutation. (i-a) and (i-b) check the implementation more than they test a hypothesis. The one informative heredity check, Vasas switching (i-c), **failed**: no new heritable variant appeared in 25 runs. What spread was sorting among the starting variants, not open-ended evolution.
2. **Drift is large.** In SIEVE the "reader" label carries no function, yet it reached 0.79 in seed 504 by drift alone, and one ON seed fixed the hedger. With about 1/4 odds per seed of a label dominating by chance, 4/5 by chance is about 0.02. That is suggestive, not strong.
3. **The fitness edge is tiny.** ON vs SIEVE growth differed by about 1%, so (s) failed. The reader wins by small differences compounded over about 200 generations. That is consistent with selection, but the edge is fragile, and only 1 of 8 gate worlds allowed it.
4. **The price is an upper bound.** It is per nat of per-sample mutual information of a perfect reader (h(duty) ≈ 0.33 nats), charged as decay; it is not measured information. At 10×, the charge (≈ 0.03/time) is comparable to the base decay (0.05), so suppression is unsurprising.
5. **The world is designed.** It is a narrow, reader-friendly corner (τ 2, P 40) chosen by the gate. There are lumped cores, not a polymer RAF chemistry, and one model structure.
6. **(ii-b) is partly mechanical.** OFF puts every label at chance (0.25) by permutation. It shows that selection cannot hold a trait that is not inherited, which is expected, not discovered.

## What it means for "how judgment arises" (M1), in plain words
- **Proved-in-model (toy):** once compartments carry an inherited chemical state, a reader keyed to a timed cue spreads. It does so only when the state is inherited, only when the cue's timing carries information, and only when the reading price is low. The same reader fails with an untimed cue or at 10× price. That matches the GTAO hold rule, stake × need > upkeep, at the level of chemistry, without fitness ever rewarding anticipation.
- **Open miss:** where new heritable states come from below chemistry. The model gave inheritance without novelty. Vasas-style core switching did not occur at the chosen world, so judgment here can only be *selected from* what was there at the start, not *invented*. M1 is now narrowed: heredity of a judging state plus selection by price works in-model, and the source of new variants is the remaining gap.
- **Hypothesis for next (untested):** switching needs crashes deep enough to reach the spontaneous floor (larger τ or longer pulses), or a smaller molecule count. That trades heredity against novelty. Finding the regime with both is the next test.
