# T82d run log

Locked file: `theory/torus-memory-2026-11-24/PREREG_RESONANCE.md`

sha256: `3a37da80f100480efa7442a372fc94aa449541ea4b04b39a8b03ec0db5ad4a39`

The scored script has not been run. Scores, when they exist, are appended below this line and this paragraph is not rewritten.

2026-11-24, after the scan. `resonance_checks.out` has FAILS 6: P-band, P-where, P-align, P-single, P-gain, P-null. P-port and P-stair pass. Stake 2 has period-2 islands 500-505, 555-558, 613-615, and 674. On those horizons the coupled map at gain (1, 1) is period 4 with tail-mean rates 7.5, 5.5, 3.5, and 1.5.

## Ledger, appended 2026-11-24 16:50 ET

Independent review, fork PR #16 comment 7145388655, write-up on fork PR #27. Lock `c496962`. Breach check: none. Odds were not locked on every row. Location is `model` on every row: no MV1–MV8 gate was declared, and the recomputation matches the lock, so the width floor is not `measurement/code`. Signed size is outcome minus the locked value. The sentences above this heading are unchanged.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82d-P-port | Stake 2: T=415 period 1 at 0.246706007043; T=500 period 2 at 0.288952 and 0.291620 within 5e-7; T=831 period 1 at 0.422916079022; T=550 rate 6 and return 0.313065981732. Odds not locked. | Periods 1, 2, 1. Levels 0.288951536270 and 0.291620058685. Means 0.246706007043 and 0.422916079022. T=550 return 0.313065981732. | HIT. Level residuals -4.64e-7 and +5.87e-8, inside the band. | model | low | none yet | none |
| T82d-P-band | One period-2 plateau, length at least 3, containing 500, and no other period-2 horizon. Odds not locked. | Four blocks: 500-505, 555-558, 613-615, 674. | +3 blocks. | model | high | None to the lock or the scoreboard. The four islands are the boundaries between five width blocks, pairs (8, 7), (6, 5), (4, 3), (2, 1). They move with the floor offset and vanish without the floor. | none |
| T82d-P-where | That one plateau lies strictly between 415 and 831. Odds not locked. | No single plateau. All four blocks lie in (415, 831). | Placement residual 0. The row misses because the unique plateau is absent (+3 blocks). | model | medium | None to the lock or the scoreboard. Same block-boundary reading as T82d-P-band. | none |
| T82d-P-align | The one center C satisfies abs(C/(r*tau)-1)>0.05 for every r in {1/2, 1, 5/4, 4/3, 3/2, 2}. tau=1/sin^2(pi/64). Odds not locked. | No unique C. tau=415.345062231902. | The locked residual is the missing center (+3 blocks). | model | high | None to the lock or the scoreboard. The 5/4, 4/3, 3/2 reading does not support an update: look-elsewhere P=0.449 for any q<=4; ordered match P=0.044; 6/5 is closer once q<=5; horizon 674 is within 5 percent of 5/3. tau is not the walk decay constant: 1/(1-lambda)=1712.66, not 415.35. | none |
| T82d-P-stair | Every horizon at stake 2 has period 1 or 2. Odds not locked. | Period above 2: 0 horizons. | HIT. Count residual 0. | model | low | none yet | none |
| T82d-P-single | Each of stakes 1, 2, 4 has at most one period-2 block. Odds not locked. | Stakes 1 and 4 have 0. Stake 2 has 4. | Stake 2: +3 blocks. Stakes 1 and 4: HIT, count 0. | model | medium | None to the lock or the scoreboard. Same block-boundary reading as T82d-P-band. | none |
| T82d-P-gain-interior | N(1.5,1.5)-N(0.5,0.5) <= 2. Odds not locked. | 184 and 148. | HIT. Signed difference -36, which is 38 under the cap of +2. The interior set shrinks. | model | medium | none yet | none |
| T82d-P-gain-differ | Horizons whose period changes between gains (0.5, 0.5) and (1.5, 1.5): at most 2. Odds not locked. | 51. | +49 horizons. | model | high | None to the lock or the scoreboard. The periods are closed orbits of a contraction, separation exponent equal to the log of the absolute value of (1-g), which is negative, not a tongue. | none |
| T82d-P-gain-fine | The seven equal gains at T=500 share one period. Odds not locked. | Periods 16, 9, 12, 4, 3, 3, 5. | +6 gains differ from the first. | model | high | None to the lock or the scoreboard. Same contraction reading as T82d-P-gain-differ. | none |
| T82d-P-null | Six runs are period 1: T=500, T=550, and the integer nearest the unique center, each on 181 and 2881 angles, with the floor removed. Odds not locked. | The four named runs are period 1. There is no unique center, so two runs are not executed. | -2 runs not executed. The four executed runs have period residual 0. | model | high | None to the lock or the scoreboard. The floor comparison is the locked null. The islands move with the floor offset and vanish without the floor. | none |

### Scaled notes, stake medium and high

Odds were not locked, so a hit here is a reproduction inside the band, not a surprise against a stated prior.

**T82d-P-band, T82d-P-where, T82d-P-single.** The lock asked for one plateau. The outcome is four. The integer menu has five distinct blocks: widths 2 and 3 share sites, as do 4 and 5, 6 and 7, and 8 and 9, and width 1 is one site. A 2-cycle needs two different returns, and the four islands are the boundaries (8, 7), (6, 5), (4, 3), and (2, 1). Shifting the floor offset moves all four. Removing the floor removes the plateaus. Update: none to the lock or the scoreboard.

**T82d-P-align.** The locked residual is the missing center. The later reading, that the three plateau centers sit on 5/4, 4/3, and 3/2 times tau, does not support an update. Three centers drawn in [416, 830] fall within 5 percent of some p/q with q<=4 with probability 0.449. The ordered-gap event has probability 0.044. With q<=5 the first center is closer to 6/5. Horizon 674 is within 5 percent of 5/3. The largest eigenvalue of the 32-site lazy step gives 1/(1-lambda)=1712.66, not 415.35, so tau is not the decay constant of this walk.

**T82d-P-gain-differ, T82d-P-gain-fine.** The period list changes with the gain (+49 horizons, +6 gains). Inside a cell the step has eigenvalues 1-alpha and 1-beta. For a gain in (0, 2) the separation exponent, the log of the absolute value of (1-g), is negative. The orbits close. The period is not held fixed while a band widens. The interior-count row hits in the direction of a smaller set.

**T82d-P-null.** The four executed runs are period 1. The row misses by the two runs that have no unique center. That is the locked null, not a disagreement between the code and the lock.

## Strong-resonance row, appended 2026-11-24 17:05 ET

The rows above are unchanged. This row is the strong reading that those rows left as an alignment note. Odds were not locked in `PREREG_RESONANCE.md` (lock `c496962`).

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82d-strong-resonance | One period-2 plateau, and its center off every simple multiple of the gap clock by more than 5 percent (`PREREG_RESONANCE.md`, P-band and P-align). Odds not locked. | Four islands, 500-505, 555-558, 613-615, 674. They are the boundaries between width blocks, pairs (8, 7), (6, 5), (4, 3), (2, 1). They move with the floor offset and vanish without the floor. Centers 502.5, 556.5, and 614 sit -0.032130, +0.004887, and -0.014474 from 5/4, 4/3, and 3/2 times tau. A simple-fraction match on [416, 830] has look-elsewhere probability 0.449 for any p/q with q<=4. | +3 islands (4 against 1). Alignment gaps -0.032130, +0.004887, -0.014474, inside a baseline of probability 0.449. | model (discretization) | high | The next look moves to the lossless continuous-record world (T82e) and makes no claim of resonance from T82d. No edit to the lock or the scoreboard. | none |
