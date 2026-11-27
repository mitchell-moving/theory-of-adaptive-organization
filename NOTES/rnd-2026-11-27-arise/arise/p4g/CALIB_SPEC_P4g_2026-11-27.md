# P4g calibration spec (hashed before calibration ran)

*Friday 27 November 2026 (EST). Model p4g_model.py SHA-256 9120bb47e5d1b2a7048e2231df5982b653c62630fd052a877135dfc36bae274d (a copy of p4f_model.py); calib.py SHA-256 1ab7c1ac70d4767657356f4e63eb029817c33deb875e6d273615908ed7697507.*

**Purpose: a price that can fail (M5), in-model.**
- First, measure the price at which a *designed* reader (lag 4, θ 0.3) stops paying against a zero-read core: c*_designed. This uses a designed contest only, no evolution, on pilot seeds 101–105.
- Then preregister that the *evolved* read effort, starting from no reader, collapses at a price within a factor of 2 of c*_designed.
- This turns P4f's coarse bracket (between 0.1 and 1) into a quantitative prediction that can miss.

**Definition.** pass_frac(c) = the share of seeds where the reader reaches ≥ 0.75. c*_designed is the log-interpolated price where pass_frac first falls through 0.5. If there is no crossing on the grid {0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1, 2}: report it and do not preregister the cap test.
