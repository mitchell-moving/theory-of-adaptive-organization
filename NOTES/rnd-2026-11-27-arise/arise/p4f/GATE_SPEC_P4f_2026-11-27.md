# P4f gate specification (hashed before the gate ran)

*Friday 27 November 2026 (EST). This is P4f, tightening P4e. Model p4f_model.py SHA-256 9120bb47e5d1b2a7048e2231df5982b653c62630fd052a877135dfc36bae274d: it is p4e_model.py plus a non-saturating anticipation measure A (mean population detox at toxin onsets minus mean detox, last 50%). gate.py SHA-256 25356241829d424c0dd60d60ac4a39ba2b4c9c2392246e5a2877dcfbc1b4fdb7.*

**Disclosed smoke run** (seed 999, T 600, μ 1e-3): A 0.0028, read effort 0.048.

**Gate.** All 16 lags (0–15), each against a zero-read core. Pilot seeds 101–105 (the same seeds as P4e's gate, so lags 0, 2, 4, 6, 8 and 12 repeat P4e's gate). A lag passes if its frequency is ≥ 0.75 in ≥ 4/5. L_inf = the passing lags. Validity: at the best lag, the random cue passes ≤ 2/5. If nothing passes, stop.

**Correction to P4e review point 5 (reasoning, hypothesis; to be checked in the test).** Detox D is shared by every core in a compartment, so reading is a public good inside a compartment. Within-compartment selection should therefore work **against** readers, not for them. P4e's high heredity-off MI at μ 1e-2 is more likely the saturating MI measure. The test's heredity-off arm, scored with A, checks this.
