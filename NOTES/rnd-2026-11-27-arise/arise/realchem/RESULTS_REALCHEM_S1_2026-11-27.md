# REALCHEM-S1 results and hostile review

*Prereg b6ef5292…747e5, locked 2026-11-27 00:39:02 EST. One run (pen_s1.out). Status: in-silico with published Montagne 2011 constants; a reduced model.*

## Scores (medians over seeds 1–3)

| V (fL) | leak 0: κ / switch / loss | leak 1e-3 | leak 1e-2 |
|---|---|---|---|
| 0.1 | 0.999 / 0 / 0.001 | 0.992 / 0 / 0.004 | 0.947 / 0 / 0.026 |
| 0.3 | 1.000 / 0 / 0 | 0.981 / 0 / 0.009 | 0.840 / 0 / 0.077 |
| 1 | 1.000 / 0 / 0 | 0.945 / 0 / 0.028 | 0.486 / 0 / 0.346 |
| 3 | 1.000 / 0 / 0 | 0.962 / 0 / 0.018 | **0.666 / 0.0048 / 0.196 (BAND)** |
| 10 | 1.000 / 0 / 0 | 1.000 / 0 / 0 | 1.000 / 0 / 0 |

- **R1 PASS (disclosed beforehand):** with published constants there is no bistability at T_i = 0, and bistability holds at every T_i ≥ 1 nM.
- **R2 FAIL:** at leak 1e-2, κ = 0.486 at 1 fL and 0.666 at 3 fL, both below 0.9.
- **R3 PASS, but narrow:** one cell out of 15 is in the band (3 fL, leak 1e-2). Its switching rate of 0.0048 per passage is about 2.4× the cutoff.
- **R4 PASS, but uninformative:** at leak 1e-3 switching is 0 at every V, so "non-increasing" holds trivially.

## Observed (not predicted)
1. **Intrinsic noise alone never switched a state, even at 0.1 fL.** In this model the published inhibitor binding is about 400× tighter than trigger binding, and that makes the memory very robust. In this model, novelty comes from **leak**, not from small numbers of molecules.
2. **Heredity is lost mainly to "mixed" states, not to clean switches.** Loss is non-monotone in V: it peaks at 1 fL and is 0 at 10 fL.
   - In small droplets, leak per droplet is under one molecule per passage, so leak rarely fires.
   - In large droplets, the established trigger sops up the leak.
   - In between, leak seeds stuck mixed states.
3. In this model, the toy's heredity–novelty axis (molecule count M) does **not** map onto droplet volume alone. It maps onto *leak × volume against inhibitor strength*.

## Hostile review
1. **Leak is unpublished,** and it decides the result. The band exists only at the top of my leak range. Had the range been capped at 1e-3, R3 would have missed. The range was chosen by me, not by measurement.
2. **The band is narrow:** 1 of 15 cells, 3 seeds. Its switching rate of 0.0048 per passage means about 19 switches in 4000 pairs, so it is not robust evidence of a band.
3. **The model is reduced:**
   - no enzyme saturation or competition, which Rondelez 2012 (doi 10.1103/PhysRevLett.108.018102) shows to be a major coupling in PEN;
   - quasi-steady occupancy;
   - one k_a for all pairs.
   - Saturation would couple the two cores through shared enzymes and could change switching.
4. **Passaging is binomial halving with refill,** a stand-in. Real PEN droplets do not divide; Genot 2016 uses static droplets, not lineages.
5. **The "mixed" state is defined by my thresholds** (50 nM, 10×). A different cutoff would move loss and κ.
6. **Tau-leaping at counts below 1** (0.1 fL) is approximate.
7. **Engineering disclosure:** the first bistability test was flawed and was fixed before the lock (see the prereg).
8. **No reader, cue, price or selection** is in this run. S1 tests only the heredity substrate (M1-like), not the P4 threshold rule.

**Labels.**
- R1, R3 and R4 are proved-in-model.
- That novelty is set by leak rather than intrinsic noise is a model observation and a hypothesis for real PEN. It is testable by measuring the untemplated (leak) synthesis rate and droplet volumes.
