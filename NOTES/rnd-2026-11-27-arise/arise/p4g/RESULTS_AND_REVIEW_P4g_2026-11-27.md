# P4g results and hostile review: a price that can fail, and the high-novelty side

*Friday 27 November 2026 (EST). Prereg PREREG_P4g_2026-11-27.md, SHA-256 612c81c19a5aa8ef5a3f85a79c8afb6aed9f45581f1dde5c42aeb5f6b359a56a, locked 00:19:44 EST before the run. Calibration: CALIB_SPEC (b9b2434c…), calib.out. Outputs: p4g_test.out, runs.json. One run, fresh seeds 1001–1010. In-model toy.*

## Results
**Price cap (μ 1e-3; 10-seed means)**

| c_nat | 0.01 | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 | 1 | 2 |
|---|---|---|---|---|---|---|---|---|
| evolved read effort | 0.471 | 0.452 | 0.396 | 0.424 | 0.248 | 0.059 | 0.007 | 0.003 |
| f_inf (lags 2–6) | 0.98 | 0.98 | 0.97 | 0.97 | 0.83 | 0.30 | 0.03 | 0.02 |
| A (anticipation excess) | 0.024 | 0.027 | 0.031 | **0.041** | 0.027 | 0.005 | 0.000 | 0.000 |

- **c*_evolved = 0.511** (bootstrap 95% over seeds: 0.437–0.563).
- c*_designed = 0.617 (designed contest, pilot seeds).
- **P-cap: PASS** (inside the window [0.31, 1.23]).

**High-novelty side (c 0.01; median A)**

| μ | median A | f_inf | read effort |
|---|---|---|---|
| 1e-2 | 0.0196 | 0.90 | 0.51 |
| 3e-2 | 0.0179 | 0.71 | 0.41 |
| 1e-1 | 0.0052 | 0.35 | 0.26 |

**P-high: PASS** (p = 9.1e-5).

## Hostile review
1. **The P-cap window was wide, and P4f had already bracketed the answer** (disclosed). The sharper fact sits in the bootstrap: c*_evolved (0.44–0.56) lies **below** c*_designed (0.62) and the interval excludes it. A 50/50 designed contest overstates the price that evolution tolerates. A plausible reason (hypothesis): a new reader has to pay while rare, and some new readers read at useless lags and still pay.
2. **The price is a linear per-nat proxy,** so "a price that can fail" here means the toy's price can fail; it does not mean a measured price.
3. **The band is assembled across two preregs.** The low side (μ 1e-5 ≈ 0) is from P4f; the high side (μ 0.1 low) is from P4g, on different seeds. So the interior band in the open-ended model is shown only in that combined sense. P4f's F4 stays failed as registered.
4. **Post hoc, now seen twice:** a moderate price *raises* anticipation. A peaks at c 0.3 (0.041 vs 0.024 at 0.01), as in P4f's C0.1 arm. It is not preregistered, so it carries no weight, but it is a candidate prediction: a price trims readers that read at useless lags.
5. **Same toy limits as P4e and P4f:** a hand-made variant space, lumped cores, one world.

## Plain words
- In the toy, the price at which evolution stops reading (about 0.51) lands within 20% of the price at which a designed reader stops paying (0.62). That match was predicted before the run.
- Evolution is a bit more price-sensitive than the designed contest.
- Anticipation is lost both when novelty is too rare and when it is too frequent.
- A moderate price may sharpen anticipation rather than only reduce it. That is untested.
