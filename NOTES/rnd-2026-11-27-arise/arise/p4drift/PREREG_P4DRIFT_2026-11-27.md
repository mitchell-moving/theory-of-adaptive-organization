# P4-DRIFT preregistration: does the novelty band move with world drift?

*Locked Friday 27 November 2026 (EST), before any test run. Model drift_model.py SHA-256 1211a62ee68861cc27282b03ee938933e2512ce894d23caca30f58d456f65b72 (the P4-BAND model plus a drifting cue-to-toxin lag; diff shown in the WORKLOG line). Test drift_test.py SHA-256 f821ea43d811535f58be0be536c73b5f78e30427f123942986759e1b6acb8eb5. Fresh seeds 1601–1624 (never used before). One run, no retries. Next step chosen by the judgment rule after NOVELTY_ASSESSMENT §5 test 1 (parent agent, 01:13 EST).*

**Why.** NOVELTY_ASSESSMENT judged novelty minor ("check"), but flagged one way it could matter more: if the band tracks the world's drift rate, novelty is tied to SE7's "drift inside the hold band" and is not just a range condition. Prior art predicts the direction in kind. Mutation-rate theory (Leigh 1970, doi 10.1086/282663) and sensing-vs-switching theory (Kussell & Leibler 2005, doi 10.1126/science.1114383) favour more variation when the environment changes faster. Both DOIs were verified on Crossref tonight (../p4band/crossref_band.out).

**World drift.** The cue-to-toxin lag switches between two regimes, L* = 4 and L* = 11, as a Poisson process of rate r per unit time (checked at each toxin onset). The starting regime is random per seed. The informative reader lags for the two regimes do not overlap (about 0–4 vs about 7–11), so a switch makes the current reader useless until a new one is found or a mix is kept.

**Pilot (disclosed; range only, not evidence).** pilot.py, pilot seeds 1391–1394, μ 1e-3 only (pilot.out SHA-256 89240493f99589d443faa7906dafd982813080547be5d57e37fae18ebb1a8589).
- Each regime alone was learnable: mean A 0.024 (L* 4) and 0.022 (L* 11). Static two-regime mean A was 0.026.
- Mean A by drift: 0.026 (1/3000), 0.015 (1/1000), 0.009 (1/300), 0.013 (1/100).
- Choice rule, written in pilot.py before the pilot ran: r_fast = the largest r with A ratio in [0.3, 0.8], which gave 1/100 (ratio 0.48); r_slow = r_fast/10 = 1/1000.
- Disclosed: the pilot's manipulation curve is not monotone (1/300 lowest). A code smoke run at T 150 with pilot seeds checked that the script runs.

**Setup.** Same model as P4-BAND otherwise: zero-read start, no reader written in, T 6000, c_nat 0.01.
- r ∈ {0 (static, random regime), 1/1000, 1/100}.
- μ ∈ {3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1}.
- ON: 24 seeds per cell (792 runs). This is more than P4-BAND-T's 10, which was underpowered.
- Controls at r = 1/100: OFF (heredity off) and RANDOM (untimed cue), 8 seeds × 11 μ (176 runs).

**Estimators (registered).**
- *Centroid* (primary, continuous, not grid-locked): mean log10 μ weighted by mean A_ON clipped at 0.
- *Edges:* half of each drift level's max mean A, first upward and last downward crossings, log-linear interpolation (as in P4-BAND-T). Disclosed: a relative rule moves with peak height (P4-BAND-T review 2).
- *Tie-rule peak* (median A, 0.95 top set) as in P4-BAND.
- Seed bootstrap within cells, 2000 resamples, rng seed 0.

**Predictions (directional, failable).**
- **D1 (primary):** the centroid at r 1/100 minus the centroid at r 0 is ≥ +0.25 decades, with bootstrap 95% lower bound > 0.
- **D1m:** centroids are ordered r 0 < 1/1000 < 1/100 (point estimates).
- **D2:** the low edge rises with drift (fast − static > 0, bootstrap lower bound > 0).
- **D3 (Eigen-type edge fixed):** |high edge, fast − static| < 0.25 decades.
- **D4:** at r 1/100 the band is still two-sided: the top set excludes both grid ends, the peak beats both ends (one-sided Mann–Whitney, Holm), and both end medians are ≤ 0.5 × the peak median.
- **C1, C2:** at the r 1/100 peak grid point, ON > OFF and ON > RANDOM (one-sided Mann–Whitney, Holm).
- Holm family: D4a, D4b, C1, C2 (α 0.05).

**Reading, stated now.**
- D1 PASS: the band moves with drift, so novelty is tied to the world's drift rate in this toy. That would raise novelty from "check" toward "keep" as part of SE7's drift clause.
- D1 FAIL: the band does not move. Novelty stays a fixed range condition ("check"), or fades to a note.
- D3 FAIL: the upper edge is not a fixed Eigen-type bound.

**Status.** In-model toy, hand-made two-regime world, linear price proxy, fitness = growth only. No physics claims.
