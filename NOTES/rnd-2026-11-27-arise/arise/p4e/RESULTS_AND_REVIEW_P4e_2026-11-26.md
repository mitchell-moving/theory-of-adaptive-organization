# P4e results and hostile review: is judgment invented from below? (open-ended cores)

*Thursday 26–27 November 2026 (EST). Prereg PREREG_P4e_2026-11-26.md, SHA-256 54389c7f6c7ae73eca20691d572f833cf336ab6599e78f82b80f32224b2e02ae, locked 2026-11-27 00:01:43 EST before the run. Outputs: p4e_test.out, runs.json (including MI, read-effort and lag-histogram time series per run), descriptive.out (post hoc), gate.out. One run, fresh seeds 801–810. In-model only, for a toy.*

## Gate
Against a zero-read core (μ 0, pilot seeds): lags 2, 4 and 6 won (4/5, 5/5, 5/5), while lags 0, 8 and 12 lost. Random-cue validity: 1/5, so the gate is valid. L_inf = {2, 4, 6}.

## Results by μ (10-seed means; MI in nats)
| μ | MI_final ON | OFF | RANDOM | PRICE | NOCUE | MI_first ON | f_inf ON (L_inf) | f_inf NOCUE | share lags 2–6, ON (post hoc) | read effort ON / PRICE | growth ON / NOCUE | mode lag ON |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1e-5 | 0.010 | 0.002 | 0.001 | 0.010 | 0 | 0.000 | 0.10 | 0.00 | 0.10 | 0.06 / 0.02 | 0.0555 / 0.0543 | scattered; 3 seeds have no reader |
| 1e-4 | 0.089 | 0.001 | 0.002 | 0.079 | 0 | 0.007 | 0.39 | 0.00 | 0.88 | 0.39 / 0.27 | 0.0638 / 0.0543 | 3–6 in 9/10 |
| 1e-3 | 0.099 | 0.017 | 0.004 | 0.099 | 0 | 0.053 | 0.60 | 0.09 | 0.98 | 0.46 / 0.49 | 0.0667 / 0.0544 | 3–6 in 10/10 |
| 1e-2 | 0.099 | 0.080 | 0.003 | 0.099 | 0 | 0.072 | 0.30 | 0.17 | 0.89 | 0.50 / 0.47 | 0.0676 / 0.0559 | 4–5 in 10/10 |

Mean MI over time, ON at μ 1e-4 (600-unit windows): 0.007, 0.033, 0.059, 0.066, 0.074, 0.087, 0.085, 0.087, 0.089, 0.089.

## Scored (Holm over a 20-test family; μ* = 1e-4)
| Prediction | Score |
|---|---|
| (a) information rises with no reader written in (T1–T3 at μ*) | **PASS** (p 0.001–0.002; all three survive Holm; also at μ 1e-3 and 1e-2) |
| (b) convergence on L_inf: T4 rejected and mode lag ∈ L_inf in ≥ 8/10 | **FAIL** (T4 p = 0.32; 4/10) |
| (c) the price caps read strength (T5) | **FAIL** at every μ (p ≥ 0.09) |
| (d) interior optimum μ* ∈ {1e-4, 1e-3} | PASS **by rule, but uninformative**, see review point 1 |

## Hostile review
1. **(d) is a tie-break artifact.** Median MI_final is 0.0992 at 1e-4, 1e-3 and 1e-2 alike, because the median-split MI hits a ceiling. argmax returned the first tied level in list order. The high side of the error threshold is not visible here. Only the low side is real: at μ 1e-5, too few variants arose (3/10 seeds had no reader at all).
2. **The MI measure saturates and is too sensitive.** A few readers move the population-mean detox above its median at the right times. That is why OFF at μ 1e-2 reaches 0.08 while its reader-lag share is only 0.04. The test needed a measure that does not saturate, such as detox at toxin onset per compartment.
3. **(b) failed partly from my own conservative L_inf.** The gate tested even lags only, so lags 3 and 5 counted as non-informative. Post hoc, mode lags were 3–6 in 9/10 (1e-4), 10/10 (1e-3) and 10/10 (1e-2), and the 2–6 share was 0.88–0.98 vs 0.05–0.28 in NOCUE. That is convergence in substance, but it is post hoc and carries no evidential weight. As registered, (b) fails.
4. **(c) failed: the price was too low for the stake.** The 10× per-nat price maxes out at about 0.03 per unit time. Surviving a τ-3 crash is worth far more (stake × need ≫ upkeep), so reading stays. That is consistent with the hold rule, but the prediction as written fails. No price sweep was run.
5. **Selection is not only between compartments.** The toxin acts on cores inside compartments, so readers also win *within* compartments. With frequent nucleation, readers arise in every compartment and spread without compartment heredity. That explains OFF's MI at μ 1e-2 and weakens the "only with heredity" reading at high μ. At μ 1e-4 the OFF arm stays near 0, so heredity matters where novelty is rare.
6. **The design limits "invented".** The variant space (17 lags × θ) and the world are hand-made. "Invented" here means drawn at random from a space where most variants are useless (lag none, 0, 8–15) and finding the useful ones by selection. Nothing outside that space can arise.
7. **The price is a linear proxy,** not measured mutual information.

## Plain words: is judgment invented from below? (in-model)
- **Partly yes:** starting with no reader anywhere, random new cores with random settings arise. Selection keeps the ones that act at the right delay after the cue (lags about 3–6), and the population's chemistry comes to carry information about the coming toxin (MI from about 0 to about 0.09–0.10 nats).
- This happens only with a timed cue (RANDOM about 0). Where novelty is rare (1e-4), it happens only with heredity.
- With too little novelty (1e-5) it mostly does not happen.
- **Not shown:** that a price caps reading (the price was too small for the stake), and an interior optimum (the measure saturated).
