# P4-BAND preregistration: a two-sided novelty band in one locked transect

*Locked Friday 27 November 2026 (EST), before any test run. Model band_model.py SHA-256 9120bb47e5d1b2a7048e2231df5982b653c62630fd052a877135dfc36bae274d (byte-identical to p4f_model.py and p4g_model.py); test band_test.py SHA-256 1ebc41c6d174e69708156cbd0dc2289aa6b7c3b25c0549f76340e9a4fb62e0b5. Fresh seeds 1401–1420 (never used before). One run, no retries. Asked for by Chad (t198u, via the parent agent).*

**Why.** P4d, P4e (d) and P4f F4 each failed or were uninformative on an interior novelty optimum. The two sides were seen only in separate runs: the low side in P4e/P4f (μ 1e-5, few readers arise), the high side in P4g (A at μ 1e-1 below μ 1e-2, p 9.1e-5). This test asks for both sides in a single locked transect.

**Pilot (disclosed; range and compute only, not evidence).** pilot.py, pilot seeds 1391–1392 (pilot.out): run time about 8–14 s per run; A was 0.000 at μ 1e-6, 0.017–0.028 at 1e-3, 0.003–0.004 at 3e-1 and at 1. A code smoke run at T 200 with pilot seeds 1391–1393 checked that the script runs (outside the notes, meaningless numbers). **Prior signal, disclosed:** P4f and P4g already suggest a hump with its top near μ 1e-2, so passing the location clauses is partly expected. The new content is whether both sides show up in one run with fresh seeds, controls and a CI on the peak.

**Setup.** Same world and model as P4f/P4g: zero-read start, no reader written in, T 6000, c_nat 0.01, fitness = growth only.
- μ grid (12 points, half-decade steps): 1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1. Five points below the P4f/P4g top, three above.
- ON: 20 seeds (1401–1420) at every μ. OFF (heredity off) and RANDOM (untimed cue): 10 seeds (1401–1410) at every μ. 480 runs.

**Primary metric.** A = mean population detox at toxin onsets minus mean detox, last 50% of the run (as in P4f/P4g; continuous, not capped).

**Tie rule (registered, against the P4e ceiling-tie artifact).** Top set = grid points whose median A_ON ≥ 0.95 × the maximum median. Peak location = mean log10 μ of the top set. Peak grid point = top-set member nearest that mean (lower μ if equidistant). No first-in-list argmax is used anywhere.

**Clauses (all must pass for an overall PASS).**
- **B1 (curvature):** OLS of per-seed A_ON on log10 μ and (log10 μ)². PASS iff the bootstrap 95% CI of the squared coefficient lies below 0 (2000 resamples of seeds within each μ, rng seed 0) and the point vertex lies strictly inside [−6, log10 0.3].
- **B2 (interior peak):** the top set contains neither end grid point (1e-6, 3e-1).
- **B3 (both-side drops):** at the peak grid point, A_ON > A_ON at 1e-6 and A_ON > A_ON at 3e-1 (one-sided Mann–Whitney, both Holm-rejected), and both end medians ≤ 0.5 × the peak median.
- **B4 (peak CI):** the bootstrap 95% percentile interval of the peak location (tie rule applied in every resample) lies strictly inside (−6, log10 0.3).
- **C1, C2 (controls at the peak grid point):** A_ON > A_OFF and A_ON > A_RANDOM (one-sided Mann–Whitney, 20 vs 10, Holm-rejected).
- **C3 (no band without heredity or a timed cue):** the maximum over μ of median A in OFF and in RANDOM are each < 0.25 × the peak median of ON.
- Holm family: the four Mann–Whitney tests (B3 ×2, C1, C2), family-wise α 0.05.

**Descriptive only (no weight):** f_inf (lags 2–6), reader share and dominated share of compartments, read effort, per μ. These are for mechanism (low side: readers fail to arise; high side: dominance and inheritance erode), not scored.

**Known limits, stated now.** A quadratic in log μ is a crude shape for a hump with a flat zero floor on the low side; B1 can fail on shape while B2–B4 pass, and that would be reported as such. The model is a hand-made toy (17 lag values × θ, lumped cores, one world); the price is a linear per-nat proxy. In-model only. No physics claims.
