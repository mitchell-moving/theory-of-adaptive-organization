# T82c preregistration: horizon, dephasing, and the period-2 window

*24 November 2026 (UTC). A new lock. `PREREG.md`, `PREREG_COUPLED.md`, and `PREREG_REVERSIBLE.md` are not edited. Written and committed, with `PREREG_HORIZON.sha256` and the same hash in `RUN_LOG_HORIZON.md`, before `horizon_checks.py` and before any scored horizon.*

## Why this approach

The independent review of T81, commit `7f1d108` on `forge-measured-review`, file `theory/reviews/REVIEW_MEASURED_INDEPENDENT.md`, reads the measured return as a dissipative instrument. On the six locked cells the fixed-point map is a step, and it stops on the entrance fraction of width 9 or width 1 (`:148-159`, `:213`). At \(T=500\), between the locked horizons 415 and 831, all five starts 2-cycle, \(0.288952\) against \(0.291620\) (`:159`, `:213`). The E-pair gap peaks near \(x=2\) and is gone by \(x=200\) (`:131-145`, `:217-219`). A diffusive world forgets. The coupled loop used only the six locked horizons (`PREREG_COUPLED.md:39`) and could not see \(T=500\).

T82b already scored the closed flow. Distinct starts stay apart, and damping the action from \(I=0\) leaves the return gap unchanged (`reversible_torus_checks.out:5`, `:10-20`). This lock asks the question that score leaves open. Does the history gap in the return share survive a longer horizon when the torus label is conserved, and does an added phase contraction erase it at a rate set by \(\gamma\)? Separately, is the \(T=500\) cycle a localized period-2 window on a dense horizon scan?

## Can it fail

Can it fail: yes. The closed walk's entrance fraction tends to 1, so the return share can forget the start even while the torus keeps it. A phase contraction can move the angles without halving the return gap on the locked time grid. The period-2 run can be wide, broken, or of a longer period.

Cheapest way to fail it: one \(\sqrt{2}\) orbit at zero coupling and zero damping, return horizons \(T=415\) and \(T=83069\). If the angle range of \(q\) at the long horizon is under half the range at \(T=415\), H-walk fails.

## What can genuinely fail

H-label fails if the free rotation brings two angles together. H-flow fails if extra Poincaré samples wash the angle out of \(q\), or if the rational range falls below the \(\sqrt{2}\) range. H-walk fails if the long horizon flattens the entrance fractions. H-gamma fails if the gap never halves, or if the half-time misses \(\ln 2/\gamma\) by more than the locked window. P-port fails if the recomputed cycle misses the review's digits. P-res fails if a non-stopped run is not period 2, if the two widths are not neighbors, or if the cycle horizons are not one block around \(T=500\) with fixed points on both sides and length at most half the scan.

## 1. The period-2 scan

This part uses T81's map at commit `f625bb7`, not a new cost. \(N=32\), \(c=1\), \(\phi=0\), \(w=2\). The walk, the block, the width menu, and the iteration are the ones in `measured_checks.py:146-196` and `:332-396` at that commit, and in `PREREG.md:145-157` of `theory/record-ratio-measured-2026-11-24` at that commit. Starts \(q\in\{0,1/4,1/2,3/4,1\}\). At most 40 updates. Stop when the absolute step is at most \(10^{-4}\).

- `POINT` if every start stops, the terminals differ by at most \(0.02\), and the width of \(\Phi\) at the mean terminal is at most \(0.02\).
- `SET` if every start stops and `POINT` fails.
- `CYCLE` if any start has not stopped.

On a `CYCLE` start, the tail is the last six updates. It is period 2 when the even positions agree to \(10^{-9}\), the odd positions agree to \(10^{-9}\), and the two levels differ by more than \(10^{-4}\). The width of a level is the width menu at that \(q\).

**P-port.** At \(T=500\) the class is `CYCLE`. All five starts are period 2. The two levels, sorted, lie within \(5\times 10^{-7}\) of \(0.288952\) and \(0.291620\). The absolute step lies within \(10^{-8}\) of \(2.668522\times 10^{-3}\). The two widths are 7 and 8. Fails if any clause misses. A pass says this script is the review's map. It is not a new measurement.

**P-res.** Integer horizons \(T=416,417,\ldots,830\).
- Every `CYCLE` start on every such horizon is period 2, and each of the two levels has one width, and those widths differ by 1.
- The `CYCLE` horizons form one contiguous block containing 500. At least one horizon below the block and one above it, inside the scan, is `POINT` or `SET`. The scan has 415 horizons. The block length is at most 207.
Fails if any clause misses. A long block, a gap, a period other than 2, or a width jump larger than 1 is a miss. The review's sentence that this cycle is what the locked rule calls `CYCLE` is the port. The localization is the prediction.

## 2. The conservative world

The flow is the one locked in `PREREG_REVERSIBLE.md:21-63`: Stormer–Verlet, \(h=0.05\), \(\beta=0.25\), \(\omega_{10}=1\), families \(3/2\), \(\sqrt{2}\), and \((\sqrt{5}-1)/2\), destruction rate \(\rho=\exp(I_1)\), site from \(\theta_2\), \(q\) the mass-weighted mean of the T81 single-site returns. \(\varepsilon=0\) and \(I=0\) throughout this file. Angles \(\theta_1=0\), \(\theta_2=2\pi k/8\) for \(k=0,\ldots,7\).

Dephasing is off when \(\gamma=0\). The step is then the T82b step. When \(\gamma>0\), after that step, \(I\leftarrow I e^{-\gamma h}\) and \(\theta_2\leftarrow \mathrm{wrap}(\theta_2)\,e^{-\gamma h}\), with the principal value in \((-\pi,\pi]\). \(\theta_1\) is not contracted. T82b already scored the action factor alone, at this start, and the two rates printed the same gap. The new factor is the contraction of \(\theta_2\).

The history gap \(G\) is the range of \(q\) across the eight angles. A missing sample makes that \(q\) undefined and the prediction fails.

**H-label.** Family \(\sqrt{2}\), \(\gamma=0\), \(n=2000\) steps. The minimum pairwise state distance at the end is at least half the minimum pairwise distance of the eight starts. Distance is the T82b distance. Fails if the ratio is under \(1/2\).

**H-flow.** \(\gamma=0\). The walk horizon is \(\max(1,\mathrm{round}(80/\Omega_2))\), fixed. Integration times \(t=20,40,60,80,100\). For each family, the smallest \(G\) on that list is at least half the largest. At every listed time the rational \(G\) is at least the \(\sqrt{2}\) gap. Fails if any clause misses.

**H-walk.** \(\gamma=0\), \(n=2000\), families \(3/2\) and \(\sqrt{2}\). Walk horizons \(104,208,415,500,831,1661,3323,6646,13291,26582,83069\), the review's E-pair list plus \(T=500\) (`REVIEW_MEASURED_INDEPENDENT.md:131-144`). For each family, \(G(83069)\ge G(415)/2\). At every listed horizon the rational gap is at least the \(\sqrt{2}\) gap. Fails if any clause misses. This is the line the long entrance can kill.

**H-gamma.** Family \(\sqrt{2}\), walk horizon \(\max(1,\mathrm{round}(80/\sqrt{2}))\). \(G_0\) is the \(\gamma=0\) gap at \(t=100\). For \(\gamma\in\{0.02,0.05\}\), stop at \(t=20,40,60,80,100\) and let \(t_{1/2}\) be the first with \(G\le G_0/2\). \(|\gamma t_{1/2}/\ln 2-1|\le 0.5\). Fails if \(G_0\) is undefined, if the gap never halves, or if the half-time misses the window. No T84 formula is used.

## 3. What a split would mean

In-model only. If H-label holds and H-walk fails, the torus still carries the start and the return share does not. That is the review's finite-time transient (`:217-219`), read on this flow. If H-gamma holds, the phase contraction, not the action factor, is what sets the rate. If P-res fails, the \(T=500\) cycle is not a short period-2 window on this scan. None of these edits a locked score.

## 4. What this file does not do

It does not score. It does not edit a locked preregistration, `THEORY.md`, or `CORE.md`. Deviations after this commit go to `DEVIATIONS.md`, appended. This file is not edited after the locking commit.
