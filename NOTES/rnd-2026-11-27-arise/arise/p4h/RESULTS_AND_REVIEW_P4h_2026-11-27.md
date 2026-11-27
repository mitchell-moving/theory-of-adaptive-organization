# P4h results and hostile review: a moderate price and anticipation

*Friday 27 November 2026 (EST). Prereg PREREG_P4h_2026-11-27.md, SHA-256 345f53aec1cd0ac75886a7333399aaf5b61b63a8f5c148ca6457faf18d62a60d, locked 00:23:03 EST. Output: p4h_test.out, runs.json. One run, fresh seeds 1101–1120. In-model toy.*

| c_nat | A mean (median) | read effort | useless-lag share | f_inf | growth |
|---|---|---|---|---|---|
| 0.01 | 0.0227 (0.0202) | 0.500 | 0.0099 | 0.980 | 0.0678 |
| 0.3 | **0.0459 (0.0439)** | 0.441 | 0.0184 | 0.967 | 0.0608 |

- **H1: PASS** (p 9.0e-6): a moderate price about doubles the anticipation excess A.
- **H2: FAIL** (p 0.997): the proposed mechanism is wrong. Useless-lag readers are *not* fewer under the price; they are slightly more.

## Hostile review
1. **A is a timing excess, not fitness.** Growth is *lower* at c 0.3 (0.061 vs 0.068), as it must be with a pure cost. So "the price sharpens anticipation" holds for the signal (detox concentrated at the toxin onset), not for net performance.
2. **The mechanism is unknown.** H2 failed, so the trimming story is out. Untested candidates (hypotheses): the price shifts the evolved lag mix toward lags that put detox right at onset, or it lowers baseline detox more than onset detox. The lag histogram was not saved per run, so this cannot be checked from the outputs.
3. **Two price levels, one μ, one toy.** "Known in kind" from rational inattention (information costs focus attention); this is a small in-model instance, not a new principle.

## Plain words
In the toy, charging for reading makes the population's preparation more sharply timed to the threat (about 2× the excess at onset), at some cost to growth. Why is not yet known: the trimming explanation failed.
