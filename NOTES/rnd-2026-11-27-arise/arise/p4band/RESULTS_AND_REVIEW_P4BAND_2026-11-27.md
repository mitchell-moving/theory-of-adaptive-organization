# P4-BAND results and hostile review: a two-sided novelty band in one locked transect

*Friday 27 November 2026 (EST). Prereg PREREG_P4BAND_2026-11-27.md, SHA-256 e83183eb467911eab26ce3c85bb0eccb464b4fe6ca510a4284c5524bcded8592, locked and logged 00:42:37 EST before the run. Run 00:42:37–00:55:22 EST. Outputs: band_test.out (SHA-256 8e18e671674a5eb7f8e995aeff291571349235095f3a71a7c3deb78831c6a016), runs.json (635718c3…), descriptive.out (post hoc). One run, fresh seeds 1401–1420. In-model toy. No physics claims.*

## Results (ON 20 seeds, OFF and RANDOM 10 seeds per μ) — observed in-model
| μ | median A ON | mean A ON | median A OFF | median A RANDOM | f_inf ON | reader share ON | dominated ON | read effort ON | ON seeds with A > 0.005 (post hoc) | growth ON (post hoc) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1e-6 | 0.0000 | −0.0000 | 0.0000 | 0.0000 | 0.000 | 0.002 | 0.992 | 0.000 | 0/20 | 0.0547 |
| 3e-6 | −0.0000 | 0.0008 | 0.0000 | −0.0000 | 0.059 | 0.060 | 0.992 | 0.025 | 1/20 | 0.0555 |
| 1e-5 | 0.0000 | 0.0044 | 0.0000 | −0.0000 | 0.234 | 0.235 | 0.993 | 0.093 | 6/20 | 0.0572 |
| 3e-5 | 0.0002 | 0.0074 | 0.0000 | −0.0000 | 0.445 | 0.451 | 0.992 | 0.190 | 8/20 | 0.0594 |
| 1e-4 | 0.0154 | 0.0146 | 0.0000 | −0.0000 | 0.863 | 0.867 | 0.991 | 0.298 | 16/20 | 0.0619 |
| 3e-4 | 0.0174 | 0.0162 | 0.0000 | −0.0000 | 0.962 | 0.969 | 0.991 | 0.421 | 16/20 | 0.0653 |
| 1e-3 | 0.0189 | 0.0208 | 0.0001 | 0.0001 | 0.979 | 0.988 | 0.990 | 0.466 | 20/20 | 0.0671 |
| 3e-3 | 0.0216 | 0.0232 | 0.0002 | 0.0002 | 0.962 | 0.985 | 0.987 | 0.501 | 20/20 | 0.0682 |
| **1e-2** | **0.0250** | 0.0236 | 0.0007 | −0.0000 | 0.897 | 0.970 | 0.978 | 0.501 | 20/20 | 0.0679 |
| 3e-2 | 0.0174 | 0.0171 | 0.0020 | 0.0001 | 0.705 | 0.930 | 0.956 | 0.415 | 20/20 | 0.0656 |
| 1e-1 | 0.0053 | 0.0054 | 0.0040 | −0.0001 | 0.354 | 0.855 | 0.909 | 0.260 | 17/20 | 0.0645 |
| 3e-1 | 0.0034 | 0.0034 | 0.0036 | −0.0002 | 0.270 | 0.750 | 0.802 | 0.216 | 0/20 | 0.0679 |

## Scored (as registered)
| Clause | Numbers | Score |
|---|---|---|
| B1 curvature (quadratic in log10 μ) | b2 = −0.00257, bootstrap 95% −0.00287 to −0.00227; vertex log10 μ −2.88 (μ 1.3e-3), bootstrap −2.96 to −2.80 | **PASS** |
| B2 interior peak (tie rule 0.95) | top set {1e-2} only; neither end | **PASS** |
| B3 both-side drops | peak 1e-2 > 1e-6: p 1.2e-8; > 3e-1: p 3.4e-8 (both Holm-rejected); end medians 0.0000 and 0.0034 ≤ 0.5 × 0.0250 | **PASS** |
| B4 peak-location CI | bootstrap 95% log10 μ −3.0 to −2.0 (μ 1e-3 to 1e-2); 2000/2000 defined | **PASS** |
| C1, C2 controls at peak | ON > OFF p 6.0e-6; ON > RANDOM p 6.0e-6 (Holm-rejected) | **PASS** |
| C3 no band without heredity or timed cue | max median A: OFF 0.0040, RANDOM 0.0002, both < 0.00625 | **PASS** |
| **Overall** | | **PASS (proved-in-model for this toy: a two-sided band in anticipation, in one locked run)** |

## Hostile review
1. **It is a broad plateau, not a sharp sweet spot.** Median A is within about 40% of its peak from 1e-4 to 3e-2, a span of 2.5 decades. The low drop is steep (1e-4 → 3e-5: 0.015 → 0.0002), and so is the high drop (3e-2 → 1e-1: 0.017 → 0.005). "Sweet spot" overstates it; "a wide band with two edges" is what was seen.
2. **The quadratic and the grid peak disagree by about a decade** (vertex 1.3e-3; grid peak 1e-2). A quadratic is a crude shape for a flat-topped hump with a zero floor (stated in the prereg). B1 shows negative curvature, not the peak location. The peak CI (1e-3 to 1e-2) is limited by the half-decade grid.
3. **The low edge is very likely a supply limit, not a property of the band (hypothesis, testable).** Expected new cores per run are μ·N_c·T = 1.2 at 1e-6, 12 at 1e-5, 120 at 1e-4. Below about 1e-4, seeds split into "a reader arrived and spread" vs "none did" (0/20, 1/20, 6/20, 8/20, then 16/20 with A > 0.005). That is the standard mutation-supply (N·μ) waiting-time effect from population genetics. It predicts the low edge moves down in proportion to 1/(N_c·T). If so, the low side reflects finite time and population size, not a cost of too little novelty at steady state.
4. **The high edge is in anticipation, not in growth (post hoc, important).** Growth at μ 0.3 (0.0679) equals growth at the peak (0.0679), while A falls to 0.003. At high novelty a constant stream of new cores with random lags gives broad, untimed detox. Reader share stays at 0.75 while the informative-lag share falls to 0.27. In this toy, too much novelty does not cost growth; it replaces a timed reader with a re-supplied, spread-out hedge (Kussell–Leibler territory). So "too much novelty erases judgment" holds for the timing signal A, not for fitness.
5. **Heredity stops mattering at the high edge.** OFF approaches ON at μ ≥ 0.1 (median A 0.0040 vs 0.0053; 0.0036 vs 0.0034 at 0.3). Fresh nucleation in every compartment substitutes for inheritance. This is the Eigen-type side in shape only (doi 10.1007/BF00623322): identity turnover outruns selection on timing.
6. **Prior signal was disclosed** (P4f/P4g suggested a top near 1e-2), so B2/B4 were partly expected. What is new: both sides in one run, fresh seeds, controls at every μ, and the tie rule.
7. **Same toy limits as P4e–P4h:** hand-made variant space (17 lags × θ), lumped cores, one world, linear per-nat price proxy, fitness = growth only (W12/W13).

## Plain words
- In one locked run, the toy's chemistry learns to prepare for a toxin before it arrives only within a band of novelty rates, from about 1e-4 to 3e-2 new cores per compartment per unit time. Below that, readers mostly never show up in time. Above it, the timing washes out.
- The band is wide, not a narrow spot.
- Its low edge is probably about how long the run is and how many compartments there are (a supply limit). That is the next cheap test.
- Its high edge removes the timing, not the growth. At high novelty the population survives about as well by constantly re-making a spread of untimed protectors.
