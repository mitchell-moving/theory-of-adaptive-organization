# P4 results and hostile review: autocatalytic cores in compartments (R4)

*Thursday 26 November 2026 (EST). Prereg PREREG_P4_2026-11-26.md (SHA-256 4ad61616ada66ec6c04cf4b6bf82e2c0294320d1d7de745a2d620bbd99f4adf0, locked 23:44:32 EST before the run). Raw output: p4_test.out; arm means: arm_means.out. One run, fresh seeds 401–405, no retries. Every result below is in-model, for a planted toy chemistry.*

## Path to the test (all logged in WORKLOG)
- **Gate v1** (GATE_SPEC_P4, gate.out): the reader beat a non-reader 5/5 in all 8 cells. A control added before any prereg (gate_control.out) showed that it also won 5/5 with an **untimed** cue. Its edge was hedging (making some B material at all), not anticipation, so **v1 was not run**.
- **Gate v2** (GATE_SPEC_P4_v2, gate2.out) pits the reader against a **hedger** with the same mean B flux, untimed and unpriced.
  - Result: 5 of 8 cells pass at 4/5. The chosen cell was δ 0.1, phase 60, c 0.2.
  - Validity check: with a random cue the reader won only 1/5, so the gate is valid. The first nat pays in this world, but weakly; even in the passing cells the reader lost 1 seed in 5.

## Scored results (strict, ≥ 4/5 seeds)
| Prediction | Seeds | Score |
|---|---|---|
| (i) heredity arises: H_on ≥ 0.10 and H_on − H_off ≥ 0.10 | 0/5 | FAIL (open miss) |
| (ii-a) reader cores take over, reader_freq_on ≥ 0.75 | 0/5 | FAIL |
| (ii-a2) anticipation signature, AI_on − AI_sieve ≥ 0.02 | 5/5 | PASS (largely gate-implied, see review) |
| (ii-b) only with heredity, reader_on − reader_off ≥ 0.25 | 0/5 | FAIL; reversed sign |
| (ii-c) random cue gives reader_freq ≤ 0.30 | 1/5 | FAIL |
| (iii) price c = 1.0 gives reader_freq ≤ 0.30 | 0/5 | FAIL |
| (s) growth_on ≥ 1.10 × growth_sieve | 0/5 | FAIL (+7%) |

Arm means:

| Arm | reader_freq | AI | H | H_parent | growth |
|---|---|---|---|---|---|
| ON | 0.454 | 0.053 | 0.029 | 0.991 | 0.760 |
| OFF | 0.489 | 0.015 | 0.014 | 0.918 | 0.355 |
| SIEVE | 0.321 | 0.000 | 0.148 | 0.989 | 0.712 |
| RANDOM | 0.381 | −0.001 | 0.037 | 0.991 | 0.746 |
| PRICE | 0.397 | 0.023 | 0.026 | 0.991 | 0.750 |

**Observed, not preregistered (direction only; it carries no evidential weight):** reader frequency orders ON > PRICE ≈ RANDOM > SIEVE, and AI falls by half at the high price. Both directions match (ii-c) and (iii), but well short of the thresholds. OFF's 0.49 is a coin flip from random compositions, not selection.

## Hostile review
1. **The one pass is mostly planted.** The reading reaction is written into the chemistry. Any compartment holding some A2 will raise its B fraction while the cue is on. So AI > 0 follows from the design plus the presence of A2. It is not evidence that anticipation arose by selection.
2. **(i) was not a fair Vasas-2012 replication: a design miss.** The cores here do not compete or exclude each other inside a compartment. Compartments therefore end up as near-identical mixtures (H_parent 0.99 against random pairs that are also about 0.96). There was no viable-core *switching*, the mechanism Vasas 2012 relies on.
   - Telling sign: H was highest in SIEVE (0.15), where no cue exists. The reading flux homogenizes compartments.
3. **The gate did not match the test.** The gate started from pure designed lineages; the test started from random mixtures. A reader can win a lineage contest yet fail to separate out of a mixture. The gate should have used the test's start.
4. **The heredity-off null is not clean.** Random reassignment also wrecks the cores (growth falls from 0.76 to 0.36), so ON vs OFF mixes "heredity" with "core destruction".
5. **The metrics are coarse.** reader_freq is A2 mass > A1 mass, so a 50/50 mixture sits near 0.5 whatever selection does. H uses a 5-core cosine, which saturates.
6. **One fixed chemistry** (network seed 7), with a price per read flux rather than per nat. The world was chosen from those where a designed reader could win.

## What it means for "how judgment arises" (plain words)
- **Observed in-model:** a timed reading reaction, once present, gives a small anticipation signal that vanishes when the cue carries no timing (AI about 0 under a random cue). It also gives a small growth edge over no signal (+7%). Gate v2 shows that the first nat of timing pays over untimed hedging, but only weakly.
- **Not observed:** compartment selection did **not** turn that small edge into a takeover by readers, and heredity did not arise in a form that could carry it. In this class the population stays a well-mixed soup. Judgment cannot accumulate there because no unit keeps its own variant distinct.
- **Hypothesis for the next step (not tested):** heredity below chemistry (M1) needs **mutually exclusive cores**, so that a compartment is one of several alternative stable states (Vasas 2012's viable-core switching), before any reading trait can be inherited and selected. P4 points to core exclusion, not cue design, as the missing ingredient. M1 stays an open miss.
