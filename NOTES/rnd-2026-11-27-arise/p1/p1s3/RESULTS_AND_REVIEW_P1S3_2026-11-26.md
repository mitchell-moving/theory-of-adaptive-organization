# P1-S3: results against the locked prereg, and a hostile self-review

*Thursday 26 November 2026, 23:21:52–23:30:13 EST (test runs); written by about 23:40 EST. Prereg `PREREG_P1S3_2026-11-26.md` (SHA-256 ec0d1418b27e3e79f086fcb458246a21fdfe3bac5c213172d13f88a867484c71, locked 23:21:49 EST). Scorer `score3.py` → `score3.out`. Local note; nothing committed, pushed, emailed or posted.*

**Labels:** numbers are **observed** (in-model). Readings are **hypothesis**. Nothing here derives quantum theory or any physics.

## 1. Gate (before the lock)
11 of 24 grid worlds passed (`gate.out`, pilot seeds 101–105). In all 24, the designed judge beat the reflex (frequency 1.0, 5/5). Against the sieve it failed only where design k = 1.0 (heavy reading) led to extinctions, or where ruin was too rare (x_r = 4 at low σ_f; ruin share 0.11). **So the first nat does pay in this class, in a broad region.** The rule chose the least judge-friendly passing world: σ_f = 1.0, c = 0.02, x_r = 3, k = 0.1. The full-length pilot (seed 106) showed the sieve arm going extinct (t = 595). Designed references there: judge dA_u = 0.348, reflex dA_u = 0.033.

**Design limit (as stated in the prereg §0):** this world was picked so that a judge pays. Any result here is about whether selection **finds** a judge where one pays, not whether judges pay in general.

## 2. Scores (seeds 301–305, T = 30000, about 650 generations in P_on)

| prediction | threshold | observed | score |
|---|---|---|---|
| **H-A** anticipation by action (P_on) | dA_u ≥ 0.19 | 0.080, 0.143, 0.112, 0.137, 0.140 | **FAIL 0/5** |
| **H-B** needs heredity | on − off ≥ 0.10 | 0.072, 0.134, 0.103, 0.127, 0.131 | **PASS 4/5** |
| **H-D** heredity-off loses | ruin ratio ≥ 1.3 | 5.36, 5.17, 5.26, 5.59, 5.07 | **PASS 5/5** |
| H-C reading beats no reading (flagged near-certain) | sieve extinct or ratio ≥ 1.43 | sieve extinct in 5/5 (t = 42–414) | PASS 5/5 |
| H-E record heredity follows drift persistence | h_max(P) − h_max(U) ≥ 0.10 | 0.384, 0.155, 0.049, 0.176, 0.088 | FAIL 3/5 |
| H-F price pushes reading down | Δ log k ≤ −0.5 | −1.17, −1.29, −1.04, −0.64, −1.30 | PASS 5/5 |

**PRIMARY (H-A and H-B and H-D): OPEN MISS.** H-A missed by 0.047 to 0.11 in every seed.

Other observed numbers:
- dA_u: heredity-off 0.0075–0.0098; fast-drift world 0.0000 in all seeds; high price 0.002–0.120.
- Ruin share of deaths in P_on: 0.755–0.779, so selection was strong (fix 2 worked). Evolved reading in P_on: log10 k ≈ −1.0 to −1.15.

## 3. What happened (observed, in this model)
- Starting from random linear controllers, survival selection with heredity built actions that carry information about the **future** force beyond the body, in 5 of 5 seeds: 0.080–0.143. That is 2.4–4.3× the designed reflex (0.033) and 8–19× the heredity-off null.
- It is 15–35% of the way from the reflex to the designed judge, under the halfway bar locked before the run. **It did not reach judge level in about 650 generations.**
- With heredity off it did not appear (≈ 0.009). In a world whose drift cannot be predicted 2 time units ahead, it did not appear (0.0000), as the W10 / Kalman condition says.
- Raising the price ten times cut reading by 0.6–1.3 decades. Reading did not go to zero, because in this world populations that don't read die (the sieve went extinct in all five seeds).
- Record heredity rose more in the persistent world in 5 of 5 seeds, but by more than the 0.10 bar in only 3 (FAIL as locked; the direction held in all five, noted post hoc).

## 4. Hostile self-review
1. **dA_u does not cleanly separate a force model from a memory of past body states.** Any controller with lagged memory of x carries some information about a slow force, because x is a filtered copy of it. The reflex reference (0.033) is one reflex design, not the best possible reflex. Part of the 0.08–0.14 could be "long memory of the body", not "a model of the world". The halfway bar was set to guard against this. That the miss sits below it is the honest reading. **Fix for any future run:** a competition test that plays evolved genomes against the best reflex in a fixed-design contest.
2. **Was 650 generations enough?** No time series of dA_u was saved, so I can't tell whether it was still rising. The miss could be a time limit, not a ceiling. No retry was run, as locked.
3. **The world was tuned (by design).** It limits a pass, and it also limits this miss: one world, one price, one force size.
4. **H-C and H-D carry little information.** The gate and pilot made H-C near-certain (no reading means extinction here). H-D compares accumulated selection with random designs every generation, which is W13 territory (selection with heredity is a search). H-B is the informative heredity result: anticipation by action appears only with heredity.
5. **The zero-action limit is not reachable in this world without extinction.** H-F tests the direction only.
6. **H-E's metric (mean of the largest h_j per agent) is crude.** Neutral h_j drift toward a mean largest value of 0.75 (seen in P_off: 0.749–0.751). The fast-drift world's values (0.50–0.85) vary a lot between seeds.
7. **Nothing quantum-specific was tested** (same as P1-S, review item 8): this is the decohered, Gaussian level.
8. **Walls.** W12: the prices and the ruin edge are imposed; accepted. W13: the linear memory and its wiring are given, and heredity is imposed in P_on (the off-null addresses it). W10: confirmed as a condition (the fast-drift world shows zero), not escaped.
9. **Prior art.** Selection for prediction when information pays is known in kind (Kussell & Leibler 2005, doi 10.1126/science.1114383; observed in microbes by Tagkopoulos et al. 2008, doi 10.1126/science.1154456, and Mitchell et al. 2009, doi 10.1038/nature08112). Rejecting a persistent force needs an internal model of it (Francis & Wonham 1976, doi 10.1016/0005-1098(76)90006-6). What is new here is a small in-model fact: at the decohered-oscillator level, with quantum backaction priced, survival-only selection builds partial anticipation in action, with heredity required. It does not reach the designed judge in the time allowed.

## 5. Plain words (hypothesis)
- Once the world is set up so that foresight pays, survival selection does start to build it from scratch. With heredity, populations came to act on where the force was heading, not just where the body was. Without heredity, or when the force could not be predicted, nothing like that appeared. That is the pattern Chad describes ("molecules come to anticipate their environment and are selected for it"), seen here in a toy model at the boundary just above decoherence.
- But it got only part of the way, about 15–35% of a designed judge, in 650 generations, and the test was strict, so it scores as an open miss. Part of what was built may be long memory rather than a true model of the world.
- Across P1-S, S2 and S3, foresight appears only where it pays, and only with heredity. Where it doesn't pay, selection doesn't build it. That is what the theory's own switch-on condition says. It is evidence that judgment can **emerge** by selection once the conditions hold. It does not show that it **must**, and it says nothing about nesting.
