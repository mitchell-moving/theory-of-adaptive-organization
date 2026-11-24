# T82d: where the step map repeats

*24 November 2026 (UTC). Self-check, not an independent review. Locked in `PREREG_RESONANCE.md`, sha256 `3a37da80f100480efa7442a372fc94aa449541ea4b04b39a8b03ec0db5ad4a39`, commit `c496962`, before the scan. In-model only. This is the T81 map and the coupled lag map. It is not a Hamiltonian tongue and it does not estimate \(K_c\).*

## Scores

| Item | Score | Number | Where |
|---|---|---|---|
| P-port | PASS | \(T=415\) period 1, \(T=500\) period 2 at \(0.288951536270\) and \(0.291620058685\), \(T=831\) period 1; \(T=550\) locks at rate 6, return \(0.313065981732\) | `resonance_checks.out:2-5` |
| P-band, one plateau | FAIL | four blocks at stake 2 | `:7-12` |
| P-where | FAIL | no unique plateau to place | `:13` |
| P-align | FAIL | no unique center; \(\tau=415.345062231902\) | `:14` |
| P-stair | PASS | no horizon of period 3 or higher | `:15` |
| P-single | FAIL | stake 2 has 4 blocks; stakes 1 and 4 have 0 | `:16-19` |
| P-gain | FAIL | interior counts 184 and 148; 51 horizons change period | `:20-23` |
| P-null | FAIL | the four named runs are period 1; there is no unique \(C\) | `:24-28` |

FAILS 6 (`resonance_checks.out:43-44`).

## The band map

Every integer \(T\) from 300 through 1200, three stakes. Rotation number \(1/2\) occurs only at stake 2 (`:6`, `:11`):

| Stake | Horizons | Length | Rotation number |
|---|---|---|---|
| 1 | none | 0 | — |
| 2 | 500–505 | 6 | \(1/2\) |
| 2 | 555–558 | 4 | \(1/2\) |
| 2 | 613–615 | 3 | \(1/2\) |
| 2 | 674 | 1 | \(1/2\) |
| 4 | none | 0 | — |

(`resonance_checks.out:6-11`.) Everywhere else on this grid the one-dimensional map is period 1, rotation number 0 (`:15`). There is no period 3, no period doubling, and no staircase in \(T\).

The lock asked for one plateau containing 500. The set is four islands, so P-band, P-where, P-align, and P-single miss. The puzzle is the split, not an empty set: the review's \(T=500\) cycle sits in the first island, and two more islands of length at least 3 follow it.

Read against the gap clock \(\tau=415.345062231902\) (`:14`), the midpoint of each island:

- \(500\)–\(505\), center \(502.5\), against \(\tfrac{5}{4}\tau\): relative gap \(0.032130\).
- \(555\)–\(558\), center \(556.5\), against \(\tfrac{4}{3}\tau\): relative gap \(0.004887\).
- \(613\)–\(615\), center \(614\), against \(\tfrac{3}{2}\tau\): relative gap \(0.014474\).
- \(674\), a single horizon, against \(\tfrac{3}{2}\tau\): relative gap \(0.081831\), outside 5 percent.

The three plateaus each sit inside the locked 5 percent of one ratio from the locked list \(\{1/2,1,5/4,4/3,3/2,2\}\). P-align still fails, because the lock required one center and there is not one. The alignment shows up once the set is read as three plateaus.

## Interior rate, endpoint rate, gain

At gain \((1,1)\) the coupled map is a fixed point on 887 of the 901 horizons: 184 interior and 703 at an endpoint (`:20`). The other 14 are the islands above, and on each of them the coupled orbit is period 4, rotation number \(1/4\), with tail-mean rate \(7.5\), \(5.5\), \(3.5\), or \(1.5\) (`:29-42`). Those means are interior. They are not fixed points.

Raising the gain from \((0.5,0.5)\) to \((1.5,1.5)\) changes the least period on 51 horizons (`:21`). The interior count goes from 184 to 148, so the interior set shrinks. It does not widen. At \(T=500\) the seven equal gains have periods 16, 9, 12, 4, 3, 3, 5 (`:22`). The gain changes the period. That is the P-gain miss.

Stake 1 and stake 4 have no period-2 horizon. The period-2 set does not spread across the stake.

## The floor

At \(T=500\) and at \(T=550\), on angle grids of 181 and of 2881 points, the map with the width floor removed is period 1 (`:24-27`). The review's 2-cycle dies when the floor is removed. The lock also required the integer nearest the unique band center (`PREREG_RESONANCE.md:63`). There is no unique center, so that pair was not a period-1 run, and P-null fails. The puzzle is the missing center. The cycle at the two named horizons does not survive the interpolation.
