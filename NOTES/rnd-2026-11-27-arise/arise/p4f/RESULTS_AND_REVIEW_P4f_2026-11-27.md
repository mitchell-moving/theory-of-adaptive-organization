# P4f results and hostile review: tightening P4e

*Friday 27 November 2026 (EST). Prereg PREREG_P4f_2026-11-27.md, SHA-256 847a5827e5e7647c433025810bffdbdc35e8af5971cf41bb7e6198da63586371, locked 00:13:25 EST before the run. Outputs: p4f_test.out, runs.json, gate.out. One run, fresh seeds 901–910. In-model only, for a toy.*

## Gate (all 16 lags)
Lags 2–6 beat a zero-read core (4/5 to 5/5). Lags 0–1 and 7–15 lost. Validity at lag 5 with a random cue: 2/5, the edge of the rule. L_inf = {2, 3, 4, 5, 6}.

## Results (10-seed means)
A = detox at toxin onset minus mean detox: the anticipation excess.

| μ | A: ON | OFF | RANDOM | NOCUE | C0.1 | C1 | C10 | f_inf ON / NOCUE / OFF | read effort ON / C0.1 / C1 / C10 | mode lag ∈ L_inf |
|---|---|---|---|---|---|---|---|---|---|---|
| 1e-5 | 0.0024 | – | – | – | – | – | – | 0.118 | 0.064 | 3/10 |
| 1e-4 | 0.0121 | 0.0000 | 0.0000 | 0.0000 | 0.0113 | 0.0000 | 0.0000 | 0.705 / 0.006 / 0.000 | 0.363 / 0.258 / 0.001 / 0.000 | 9/10 |
| 1e-3 | 0.0201 | 0.0001 | −0.0002 | 0.0000 | 0.0254 | 0.0003 | 0.0000 | 0.980 / 0.282 / 0.004 | 0.500 / 0.413 / 0.008 / 0.000 | 10/10 |
| 1e-2 | 0.0226 | 0.0007 | −0.0000 | 0.0000 | 0.0326 | 0.0034 | 0.0000 | 0.902 / 0.278 / 0.044 | 0.508 / 0.492 / 0.070 / 0.002 | 10/10 |

## Scored (Holm over a 15-test family; all 15 rejected, p ≤ 0.013)
| Prediction | Score |
|---|---|
| F1: anticipation needs heredity and a timed cue (A ON > OFF and > RANDOM at all 3 μ) | **PASS** |
| F2: converges on informative lags (f_inf ON > NOCUE at all 3 μ) | **PASS** |
| F3: the price caps reading (effort ON > C1 and > C10 at all 3 μ) | **PASS** |
| F4: interior optimum of median A over μ | **FAIL**: A rises with μ through 1e-2 (0, 0.011, 0.017, 0.022) |
| F5: mode lag ∈ L_inf in ≥ 8/10 at each μ | **PASS** (9, 10, 10) |

## Hostile review
1. **F4 failed, so no band was found.** Only the low side of a novelty band was seen (μ 1e-5 ≈ 0). The high side, where too much novelty erases the edge, was not reached by 1e-2. P4d saw that side at μ 0.03–0.1 in a different model (fixed menu), so the two cannot be combined into one curve.
2. **The price cap is coarse.** Reading vanished between c 0.1 and c 1 (maximum charge about 0.03 vs 0.33 per unit time). The threshold is bracketed, not located, and the price is still a linear per-nat proxy.
3. **Post hoc, carrying no weight:** a moderate price (C0.1) gave *higher* A than ON at μ ≥ 1e-3 (0.025 vs 0.020; 0.033 vs 0.023). A plausible reading is that a price weeds out readers that pay but read at useless lags. Untested.
4. **P4e's review point 5 is corrected.** Heredity-off gives A ≈ 0 at every μ, so the high heredity-off MI in P4e was the saturating measure, not within-compartment selection. Detox is a public good inside a compartment, so selection there works against readers.
5. **Gate validity was at the edge** (2/5). The world and the variant space are hand-made (17 lags × θ), with lumped cores. L_inf came from a pilot gate in the same world.
6. **A is a population-mean measure** in arbitrary detox units, not nats. It is continuous and did not saturate.

## Plain words
- With the P4e flaws fixed, the picture holds and tightens. Starting from no reader, random new cores arise, and selection finds the ones that act 2–6 time units after the cue (9–10 of 10 seeds).
- The population comes to raise its detox **before** the toxin arrives. It happens only with heredity and only with a timed cue.
- A price on reading caps it: between 0.1 and 1 per-nat units, reading stops.
- Too little novelty (1e-5) gives almost nothing.
- What remains unshown is a top edge where too much novelty erases it, in this open-ended model.
