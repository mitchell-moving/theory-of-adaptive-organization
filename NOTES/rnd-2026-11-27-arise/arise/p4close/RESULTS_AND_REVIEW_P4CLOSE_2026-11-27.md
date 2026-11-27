# P4-CLOSE results and hostile review: does the novelty window close as world drift rises?

*Friday 27 November 2026 (EST). Prereg PREREG_P4CLOSE_2026-11-27.md, SHA-256 bbb9516d02bc84f20f5ae6932ef8ee390d43104d1d1e88c0ba1c8168ea094887, locked and logged 01:50:44 EST before the run. Run 01:50:44–02:10:16 EST. Outputs: close_test.out (SHA-256 08ae30b1717379b0f053464f27543725cd4eaa5547d378cf2342a04669ad9d71), runs.json (6fa5c814…), descriptive.out (post hoc). One run, fresh seeds 1701–1716, 616 runs. In-model toy. No physics claims.*

**Run integrity.** My session was interrupted while waiting. The background run was not cut off: it started 01:50:44 and finished 02:10:16 with full output, so the locked script was not rerun and no amendment was needed.

## Results (ON, 16 seeds; mean A)
| μ | r 1/100 | r 1/30 | r 1/10 | seeds A > 0.005 (post hoc) 1/100 / 1/30 / 1/10 |
|---|---|---|---|---|
| 3e-6 | 0.0013 | 0.0011 | 0.0011 | 1 / 1 / 1 |
| 1e-5 | −0.0001 | 0.0011 | −0.0001 | 0 / 2 / 0 |
| 3e-5 | 0.0014 | 0.0025 | 0.0032 | 2 / 3 / 5 |
| 1e-4 | 0.0030 | 0.0049 | 0.0052 | 4 / 10 / 6 |
| 3e-4 | 0.0067 | 0.0081 | 0.0074 | 12 / 13 / 10 |
| 1e-3 | 0.0056 | 0.0077 | **0.0093** | 9 / 12 / 14 |
| 3e-3 | 0.0084 | **0.0095** | 0.0090 | 15 / 15 / 16 |
| 1e-2 | 0.0080 | 0.0053 | 0.0056 | 16 / 11 / 11 |
| 3e-2 | 0.0055 | 0.0038 | 0.0036 | 11 / 0 / 0 |
| 1e-1 | 0.0037 | 0.0031 | 0.0028 | 0 / 0 / 0 |
| 3e-1 | 0.0027 | 0.0024 | 0.0022 | 0 / 0 / 0 |

Edges (log10 μ) and widths: r 1/100 low −3.84, high −1.15, width 2.69; r 1/30 low −4.04, high −1.83, width 2.21; r 1/10 low −4.15, high −1.78, width 2.37. Max mean A: 0.0084, 0.0095, 0.0093. RANDOM at r 1/10: median A ≤ 0.0003 at every μ.

## Scored (as registered)
| Clause | Numbers | Score |
|---|---|---|
| **K1 (primary)** window closed or < 1.5 decades at r 1/10 | width 2.37; max mean A 0.0093, far above the 0.005 closure line | **FAIL (open miss)** |
| K2 width(1/100) > width(1/30) ≥ width(1/10) | 2.69, 2.21, 2.37 | **FAIL** |
| K3 low edge at 1/10 above 1/100 | −0.31 (bootstrap 95% −0.83 to +0.35) | **FAIL** |
| K4 replication of P4-DRIFT width at 1/100 (2.30 ± 0.5) | 2.69 | **PASS** (just inside) |
| C ON > RANDOM at r 1/10, μ 1e-3 | p 1.4e-6 | **PASS** |

## Hostile review
1. **No closure, so the closure hypothesis fails.** Anticipation survives at r 1/10, where the regime changes about four times per toxin interval. Peak mean A there is 0.0093, roughly 40% of the static value (0.023 in P4-DRIFT), and it is not distinguishable from the r 1/100 level (0.0084). **Observed, in-model.**
2. **The squeeze from P4-DRIFT saturates.** Most of the low-edge rise happened between static and r 1/1000 (P4-DRIFT: +0.69 to 1/100). From 1/100 to 1/10 the edge does not rise further (K3). More drift cost nothing extra in window terms.
3. **The window top moved down at faster drift** (high edge −1.15 → −1.78, with 11/16 seeds at 1e-2 and 0/16 at 3e-2 beyond 1/100). That is a difference from D3's fixed top, so "the top is a fixed retention limit" is only roughly supported: at r ≥ 1/30 the top sits about 0.6 decades lower than at r 1/100. Single run, 16 seeds; not scored.
4. **Neither registered story is the mechanism (hypothesis, untested).** At r 1/10 the dominant reader lags are 0–4 (share 0.91 at μ 1e-3) and the other regime's lags nearly vanish (0.06). The population appears to specialise on one regime and be right on about half the toxin onsets, not hold a standing mix of both (the Kussell–Leibler-type hedge in the prereg's rival reading). Whether the regime-4 reader is favoured by something in the toy (for example a shorter cue-to-toxin delay costing less) was not tested.
5. **C passes with an open window.** By the prereg's own reading, an open window with C passing points to a retained partial reader, but as item 4 says, not the hedge reading I named. I record the prereg reading as not matched.
6. **Edge widths are noisy** (2.69 here vs 2.30 in P4-DRIFT at the same r; K4 passes only narrowly). Width differences below about 0.4 decades are not interpretable at 16 to 24 seeds.
7. Same toy limits as P4-DRIFT.

## Plain words
- Making the world change faster did not close the useful novelty range. The toy keeps a reader for one regime and is right about half the time.
- Most of the harm from drift shows up by a modest rate and then stops getting worse.
- So novelty does not become a binding condition at high drift in this toy.
