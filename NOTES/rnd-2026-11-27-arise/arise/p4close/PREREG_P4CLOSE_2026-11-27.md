# P4-CLOSE preregistration: does the novelty window close as world drift rises?

*Locked Friday 27 November 2026 (EST), before any test run. Model drift_model.py SHA-256 1211a62ee68861cc27282b03ee938933e2512ce894d23caca30f58d456f65b72 (unchanged from P4-DRIFT). Test close_test.py SHA-256 0bd044f93b5bd7cd4ecc1870c0f14bc179036da08097f42520ea660b8314c6cb. Fresh seeds 1701–1716. One run, no retries. No pilot: the range is known from P4-DRIFT. A code smoke run at T 150 with pilot seeds checked the script, and one rule (K2's tie handling, ">=" for the last step) was fixed before this lock.*

**Why (judgment rule).** P4-DRIFT showed drift squeezes the novelty window from below: the low edge rose 0.69 decades, the high edge stayed, and width fell from 3.2 to 2.3. If the squeeze continues, the window closes at some drift rate. Novelty would then be a binding condition, raising its weight (NOVELTY_ASSESSMENT judged it minor). The rival reading is known in kind (Kussell & Leibler 2005, doi 10.1126/science.1114383): under fast switching, a standing mix of both reader types (a hedge) keeps anticipation without needing more novelty, so the window stays open. Expected information is about 1 bit on the question that sets novelty's weight, for about 15 minutes of compute.

**Setup.** As P4-DRIFT: L* switches between 4 and 11; T 6000; zero-read start.
- r ∈ {1/100 (replicating P4-DRIFT), 1/30, 1/10}. At 1/10, the regime changes about 4 times per toxin interval, so it is close to random per event.
- 11 μ from 3e-6 to 3e-1. ON: 16 seeds (1701–1716). RANDOM (untimed cue) at r 1/10: 8 seeds × 11 μ. 616 runs.

**Rules (registered).**
- Edges: half of each r's max mean A, log-linear interpolation, as in P4-DRIFT.
- Width = high edge − low edge. Width = 0 ("closed") if max mean A < 0.005. If an edge is missing, width is undefined.

**Predictions (closure hypothesis).**
- **K1 (primary):** at r 1/10 the window is closed or narrower than 1.5 decades.
- **K2:** width(1/100) > width(1/30) ≥ width(1/10).
- **K3:** low edge at 1/10 above low edge at 1/100 (bootstrap 2000, lower bound > 0).
- **K4 (replication):** width at r 1/100 within 2.30 ± 0.5.
- **C (control):** at r 1/10, ON beats RANDOM at ON's max-mean μ (one-sided Mann–Whitney, p < 0.05). If C fails while the window is "closed", the closure is the absence of any anticipation; if C passes with an open window, a hedge holds it open.

**Reading, stated now.**
- K1 PASS: novelty becomes binding at fast drift. Its weight rises toward "keep" as part of SE7's drift clause.
- K1 FAIL with C PASS: a hedge holds the window open (the Kussell–Leibler rival). Novelty stays a range condition ("check").

**Status.** In-model toy, same limits as P4-DRIFT. No physics claims.
