# P4-BAND-T preregistration (the one registered follow-up): is the band's low edge a supply limit?

*Locked Friday 27 November 2026 (EST), after P4-BAND and before this run. Model band_model.py SHA-256 9120bb47e5d1b2a7048e2231df5982b653c62630fd052a877135dfc36bae274d (unchanged); test supply_test.py SHA-256 f01b2e1fb2e40a69f1e0be0fb4842fcc7c6e874458375a1903974c324624d89f. Fresh seeds 1501–1510. One run, no retries. No pilot.*

**Why (judgment rule).** P4-BAND passed, but its review (point 3) gives a cheap alternative reading of the low side: below μ ≈ 1e-4 a reader core simply has not arrived yet in a run of length T over N_c = 200 compartments (expected new cores μ·N_c·T). If so, the low edge is a finite-time, finite-population effect, and only the high edge is a property of novelty itself. The stake is what the band means for the theory's judgment rule. Cost: about 120 runs, under 10 minutes. Expected information: about 1 bit on a question the band result cannot answer alone.

**Setup.** Same as P4-BAND ON arm, except T = 12000 (2×; the measurement window stays the last 50%). Same 12-point μ grid, 10 seeds. Compared with P4-BAND's ON arm (T 6000, 20 seeds, runs.json SHA-256 635718c31a225656e0bd12cc22a633f704b3e82ecf1174e8bb555604178cbcf1).

**Edges (registered).** For each run length: half = 0.5 × max over the grid of mean A_ON. Low edge = first upward crossing of half; high edge = last downward crossing; log-linear interpolation in log10 μ. Seed bootstrap (2000, rng seed 0) for each shift.

**Predictions.**
- **S1 (supply-limited low edge):** low-edge shift (T12000 − T6000) ≤ −0.15 in log10 μ, with bootstrap 95% upper bound < 0. Pure supply scaling predicts −0.30 (a factor of 2).
- **S2 (high edge not set by supply):** |high-edge shift| < 0.15.
- A missing edge in either run fails both.

**Reading, stated now.** S1 PASS + S2 PASS: the low side is mostly a supply limit and the high side is intrinsic to the toy. S1 FAIL: the low edge does not move with run length, so the low side is more than waiting time. S2 FAIL: the high edge depends on run length too, so neither edge is a fixed property.

**Status.** In-model toy, same limits as P4-BAND. No physics claims.
