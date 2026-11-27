# P4-DRIFT results and hostile review: does the novelty band move with world drift?

*Friday 27 November 2026 (EST). Prereg PREREG_P4DRIFT_2026-11-27.md, SHA-256 1c35c91168b45701ac884656c4de84d779b9a2d420256e7e4359039ab7dc0f49, locked and logged 01:15:55 EST before the run. Run 01:15:55–01:45:38 EST. Outputs: drift_test.out (SHA-256 1f227fc92e6c178a0e5120028955c1a36a46e7df09873b9b9cda4ce561283bf9), runs.json (ecebd29a…), descriptive.out (post hoc). One run, fresh seeds 1601–1624, 968 runs. In-model toy. No physics claims.*

## Results (ON, 24 seeds per cell; mean A, with median in brackets)
| μ | r 0 (static) | r 1/1000 | r 1/100 | seeds with A > 0.005, r 0 / 1/1000 / 1/100 (post hoc) |
|---|---|---|---|---|
| 3e-6 | 0.0000 | 0.0000 | 0.0000 | 0 / 0 / 0 |
| 1e-5 | 0.0007 | 0.0003 | 0.0008 | 2 / 0 / 1 |
| 3e-5 | 0.0113 (0.0000) | 0.0026 | 0.0020 | 10 / 4 / 4 |
| 1e-4 | 0.0174 (0.0158) | 0.0034 (0.0002) | 0.0038 (0.0028) | 20 / 3 / 7 |
| 3e-4 | 0.0185 | 0.0104 | 0.0067 | 20 / 19 / 16 |
| 1e-3 | 0.0209 | 0.0142 | **0.0100** (0.0093) | 23 / 23 / 24 |
| 3e-3 | **0.0233** | 0.0150 | 0.0084 | 24 / 24 / 22 |
| 1e-2 | 0.0216 | **0.0155** | 0.0074 | 24 / 24 / 22 |
| 3e-2 | 0.0167 | 0.0115 | 0.0050 | 24 / 24 / 14 |
| 1e-1 | 0.0048 | 0.0046 | 0.0037 | 3 / 3 / 0 |
| 3e-1 | 0.0029 | 0.0030 | 0.0027 | 0 / 0 / 0 |

Estimators (log10 μ):

| r | centroid | low edge | high edge | width | tie-rule top set |
|---|---|---|---|---|---|
| 0 | −2.79 | −4.49 | −1.30 | 3.19 | {3e-3, 1e-2} |
| 1/1000 | −2.47 | −3.71 | −1.24 | 2.47 | {1e-3, 3e-3, 1e-2} |
| 1/100 | −2.59 | −3.80 | −1.50 | 2.30 | {1e-3} |

Controls at r 1/100: median A OFF ≤ 0.0032 and RANDOM ≤ 0.0000 at every μ.

## Scored (as registered)
| Clause | Numbers | Score |
|---|---|---|
| **D1 (primary)** centroid shift ≥ +0.25, CI lower bound > 0 | +0.206 (bootstrap 95% +0.053 to +0.354) | **FAIL (open miss)**: right sign, CI excludes 0, below the registered size |
| D1m centroids ordered 0 < 1/1000 < 1/100 | −2.79, −2.47, −2.59 | **FAIL** |
| D2 low edge rises with drift | +0.69 (bootstrap +0.13 to +1.10) | **PASS** |
| D3 high edge fixed (|shift| < 0.25) | −0.20 (bootstrap −0.37 to +0.07) | **PASS** |
| D4 two-sided band at fast drift | top set {1e-3}; peak > 3e-6 p 9.7e-10, > 3e-1 p 1.5e-9 (Holm); end medians 0.0000, 0.0027 ≤ 0.5 × 0.0093 | **PASS** |
| C1, C2 controls at fast-drift peak | ON > OFF p 9.5e-8; ON > RANDOM p 9.5e-8 (Holm) | **PASS** |
| **Overall** | | **FAIL** (D1, D1m), with D2, D3, D4, C1, C2 passing |

## Hostile review
1. **The band does not slide up; it is squeezed from below.** The registered picture was a peak moving to higher novelty under drift. What was seen: the low edge rises (+0.69 decades), the high edge stays or falls slightly (−0.20), and the peak *falls* (tie-rule top set from {3e-3, 1e-2} to {1e-3}). The centroid rises modestly (+0.21) only because the low side is cut. Width shrinks from 3.2 to 2.3 decades. **Observed, in-model.**
2. **Drift raises the floor of novelty needed (D2, PIM in this toy).** At μ 1e-4, anticipation succeeded in 20/24 static seeds but in 3/24 and 7/24 under drift (post hoc). After a regime switch, the current reader is useless, and a new reader for the other lag must arrive and spread before the next switch. This is the mutation-rate / changing-environment result known in kind (Leigh 1970; Kussell & Leibler 2005), here as a rising lower edge rather than a moving optimum.
3. **The upper edge looks like a fixed retention limit** (D3 PASS, with the P4-BAND-T S2 pass). That is consistent in shape with an Eigen-type bound (doi 10.1007/BF00623322), not a demonstration of one.
4. **Drift costs anticipation everywhere:** peak mean A falls from 0.023 to 0.016 to 0.010. Growth falls too (for example 0.0672 → 0.0624 → 0.0596 at 1e-3).
5. **D1m failed because the slow-drift centroid was highest.** At r 1/1000 the low side is already cut while the top is intact; at r 1/100 the top also shrinks toward lower μ. A plausible reading (hypothesis, untested): at fast drift, populations keep both lag types as a standing mix (shares 0–4 and 7–11 both about 0.3 at 1e-3), a hedge that high novelty dilutes. The pilot's non-monotone manipulation curve points the same way.
6. **The relative edge rule moves with peak height** (disclosed in the prereg). Lower peaks under drift lower the half-max line, which would push the low edge *down*, against D2. So D2's pass is conservative with respect to that artifact.
7. **Same toy limits:** hand-made two-regime world (L* 4 or 11), lumped cores, linear price proxy, growth-only fitness, 24 seeds.

## Plain words
- When the world changes, the toy needs more novelty to keep up: the bottom of the useful range rises by about two-thirds of a decade.
- The top of the range does not move, so the useful window gets narrower, from about 3.2 to 2.3 decades.
- The best novelty level did not move up, as I had predicted; it moved slightly down. The registered primary prediction failed.
- If drift keeps rising, the window might close. Whether it does is the open question this result raises.
