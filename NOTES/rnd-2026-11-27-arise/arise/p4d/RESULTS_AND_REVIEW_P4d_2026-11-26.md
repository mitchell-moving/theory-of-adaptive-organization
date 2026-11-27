# P4d results and hostile review: the novelty–heredity transect

*Thursday 26 November 2026 (EST).*
- Prereg: PREREG_P4d_2026-11-26.md, SHA-256 57825b9d89e50c86bd966c35fcf2b456ed46eb6f6ac1bc8099bba837ec94ae85, locked 23:55:14 EST.
- Amendment: PREREG_P4d_AMENDMENT_2026-11-26.md, SHA-256 1bf8fb56284e35611dec24d36265508e530c589617446181c7e870b50b57f9d2, 23:55:24 EST. It fixes a one-character syntax error; the first launch computed nothing.
- Outputs: p4d_test.out, runs.json, series.json (reader and hedger identity frequency every 10 time units, all 250 runs), summary.out.
- One run, fresh seeds 701–710. In-model only, for a lumped toy chemistry.

## Results by μ (means over 10 seeds; reader = share of compartments with reader identity, last 50%)
| μ | switch/div | κ_ON | reader ON | NOCUE (drift) | OFF | RANDOM | PRICE | hedger ON | S = ON − NOCUE | appears (ON) | median first seen |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | 0.003 | 0.993 | **0.625** | 0.129 | 0.244 | 0.104 | 0.220 | 0.073 | **+0.496** | 10/10 | t 74 (max 391) |
| 0.003 | 0.010 | 0.982 | 0.577 | 0.243 | 0.246 | 0.179 | 0.249 | 0.122 | +0.334 | 10/10 | t 49 |
| 0.01 | 0.029 | 0.959 | 0.359 | 0.234 | 0.243 | 0.228 | 0.257 | 0.208 | +0.125 | 10/10 | t 42 |
| 0.03 | 0.074 | 0.901 | 0.283 | 0.237 | 0.242 | 0.229 | 0.235 | 0.233 | +0.046 | 10/10 | t 40 |
| 0.1 | 0.135 | 0.820 | 0.243 | 0.230 | 0.236 | 0.227 | 0.219 | 0.227 | +0.012 | 10/10 | t 38 |

Time series (mean reader frequency, ON):

| μ | t 100 | t 500 | t 1000 | t 2000 | t 3000 |
|---|---|---|---|---|---|
| 0.001 | 0.01 | 0.08 | 0.21 | 0.57 | 0.78 (still rising) |
| 0.003 | 0.03 | 0.30 | 0.52 | 0.56 | 0.59 |
| 0.01 | 0.07 | 0.28 | 0.35 | 0.39 | 0.37 |
| 0.1 | flat at about 0.24 | | | | |

## Scored predictions
| Prediction | Result | Score |
|---|---|---|
| P1: interior μ maximizes S | μ* = 0.001, the lowest level; S falls monotonically | **FAIL (open miss)** |
| P2: the reader arises at μ* in ≥ 8/10 seeds | 10/10, absent at start, entered by nucleation | PASS |
| P3: at μ*, ON beats hedger, NOCUE, OFF, RANDOM and PRICE (Holm over a 25-test family) | all 5 rejected, p ≤ 0.0011 | PASS |

All 25 tests in the family survived Holm.

## Hostile review
1. **P1 failed because the range was mis-chosen.** I proposed the μ grid in P4c. The low-novelty penalty never applied: with 200 compartments the reader needs to nucleate only once somewhere, and even at μ 0.001 it appeared in all 10 seeds (latest at t 391). The optimum, if any, is at or below 0.001. Only the high-novelty side of an error-threshold shape was seen. That side is consistent with Eigen 1971 (doi 10.1007/BF00623322) in shape only.
2. **"Arises" means entering from a fixed menu.** The reader is one of 4 cores written in advance; nucleation draws it from that menu. Nothing new is *invented*. This is the main limit on what P2 means.
3. **Significance without size at high μ.** At μ 0.1, 0.243 vs 0.227 is Holm-significant only because between-seed variance is tiny over 200 compartments. Read effect sizes, not p-values, there.
4. **Non-stationary at μ*.** The reader was still rising at T 3000, so the window mean understates the plateau. This favors P3 being conservative, but it means S(0.001) is not an equilibrium value.
5. **Growth edge is small:** ON 0.0566 vs NOCUE 0.0552 (+2.5%) at μ 0.001. Selection compounds a small edge.
6. **No gate this round.** The world (P 40, c_nat 0.01) came from the P4b gate; τ 3 and M 20 came from P4c. There is one model structure, lumped cores and a hand-written toxin world.
7. **NOCUE at μ 0.001 is below 0.25** (0.129) because the reader starts absent and drift alone has not caught up. The drift baseline is valid for comparison but is not "chance = 0.25".

## Plain-words meaning (how judgment arises), in-model
- A priced, timed reader that is **absent at the start** enters through rare side reactions in every seed.
- It then spreads over an untimed hedger, over drift, and over the same reader with heredity scrambled, an untimed cue, or a 10× price.
- It spreads most when novelty is **rarest** and heredity most faithful (κ 0.99).
- The edge fades smoothly as novelty rises, and is near neutral at about one identity change per 7 divisions.
- In this toy, then, judgment arises from: rare entry, faithful inheritance, a first nat that pays, and a low reading price. Too much novelty erases it.
- What it does **not** show is judgment being *invented*. The reader was on a menu.
