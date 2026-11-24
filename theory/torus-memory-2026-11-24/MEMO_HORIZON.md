# T82c: horizon scan of the step map and the walk

*24 November 2026 (UTC). Self-check, not an independent review. Locked in `PREREG_HORIZON.md`, sha256 `abb56169340490e2a420d47f5c0cb556e90e86caf720a2a86d5423a4c5ee85d9`, commit `af44b86`, before the scan. In-model only.*

## Scores

| Item | Score | Number | Where |
|---|---|---|---|
| P0, lock hash | PASS | `abb56169340490e2a420d47f5c0cb556e90e86caf720a2a86d5423a4c5ee85d9` | `horizon_checks.out:1` |
| P-port, \(T=500\) | PASS | levels \(0.288951536270\), \(0.291620058685\); step \(0.002668522416\); widths 7 and 8 | `:2` |
| P-res, one period-2 block | FAIL | 4 blocks, 14 cycle horizons, 401 point, 0 set | `:3-6` |
| H-label, separation | PASS | start distance \(0.785398\), end ratio \(1\) | `:8` |
| H-flow, gap along the flow | FAIL | \(\sqrt{2}\) minimum \(0.047912\) against half of \(0.229580\) | `:14-24` |
| H-walk, gap along the walk | FAIL | both families are \(0\) at \(T=83069\) | `:35`, `:46-47` |
| H-gamma, half-time | FAIL | no sample reaches half of \(0.076988\) | `:48-61` |

FAILS 4 (`horizon_checks.out:62-63`). Zero clamps (`:7`).

## The period-2 set

The port matches the review: at \(T=500\) every start is a 2-cycle between widths 7 and 8 (`REVIEW_MEASURED_INDEPENDENT.md:159`, `:213`). The cycle horizons are \(500\) through \(505\), \(555\) through \(558\), \(613\) through \(615\), and \(674\) (`horizon_checks.out:5`). Four islands, the longest of length 6. The lock asked for one block containing 500 and no longer than 207 (`PREREG_HORIZON.md`). The miss is the split. The puzzle is that the skipped window holds several short period-2 islands, not one tongue.

## The walk gap

At \(\gamma=0\) the rational gap stays above half its maximum: the smallest rational sample is \(0.193568\) at \(t=40\), and half of \(0.332754\) is \(0.166377\) (`:9-13`). The \(\sqrt{2}\) gap falls to \(0.047912\) at \(t=80\), below half of its maximum \(0.229580\). The golden gap falls to \(0.055431\), below half of \(0.206368\). At every listed time the rational gap is at least the \(\sqrt{2}\) gap. The miss is the decay on the two irrational families inside a flow that does not damp the action.

On the walk itself the gap decays in both families. At \(T=415\) it is \(0.291867\) (rational) and \(0.085218\) (\(\sqrt{2}\)). At \(T=83069\) both are \(0\) (`:27`, `:35`, `:39`, `:46`). The rational gap is at least the \(\sqrt{2}\) gap at every listed horizon, including the tie at zero. The lock asked each family to keep at least half of its \(T=415\) gap out to \(T=83069\). The walk forgets the starting angle on that list.

Phase contraction does not produce a half-time on the locked samples. \(G_0=0.076988268821\), so the bar is \(0.038494\). At \(\gamma=0.02\) the last sample is \(0.078925\). At \(\gamma=0.05\) it is \(0.064447\) (`:52`, `:59`). Neither series has a \(t_{1/2}\). The puzzle is that contracting \(\theta_2\) on this horizon moves the gap, and does not halve it by \(t=100\).
