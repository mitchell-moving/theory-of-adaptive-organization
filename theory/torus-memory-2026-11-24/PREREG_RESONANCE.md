# T82d preregistration: resonance scan of the step map

*24 November 2026 (UTC). A new lock. `PREREG.md`, `PREREG_COUPLED.md`, `PREREG_REVERSIBLE.md`, and `PREREG_HORIZON.md` are not edited. Written and committed, with `PREREG_RESONANCE.sha256` and the same hash in `RUN_LOG_RESONANCE.md`, before `resonance_checks.py` and before any scored horizon of this scan.*

## Why this approach

Two off-grid points are already on the record. At \(T=500\) the T81 map 2-cycles, \(0.288952\) against \(0.291620\) (`forge-measured-review` `7f1d108`, `theory/reviews/REVIEW_MEASURED_INDEPENDENT.md:159`, `:213`). The locked horizons 415 and 831 skip it (`PREREG_COUPLED.md:39`). At \(T=550\) the coupled lag map locks at destruction rate 6 and return \(0.313065981732\) (fork PR #16, comment 7144237250). The question is whether those points sit in bands of rational period, lined up with the gap clock and widened by the gain, or whether each is one crossing of the step-function menu.

## Can it fail

Can it fail: yes. A monotone entrance curve can cross the decision window once, with no staircase and no widening. A finer menu can kill the cycle, or the cycle can survive the removal of the floor.

Cheapest way to fail it: horizons \(T=499\), \(500\), and \(501\) on the floored width menu at stake 2. If \(T=500\) is not period 2, or the three periods are not the same, the period-2 set is not a band.

## What can genuinely fail

P-port fails if the recomputed digits miss the review. P-band fails if period 2 is absent, split, or shorter than three horizons. P-where fails if that band touches a locked POINT horizon. P-align fails if the band's center sits within 5 percent of a simple multiple of the gap clock. P-stair fails if any horizon has period 3 or higher. P-single fails if any stake has two period-2 blocks. P-gain fails if raising the gain adds more than two interior fixed points or changes the period on more than two horizons. P-null fails if the map with the floor removed is still period 2.

## 1. The world

This is the T81 map at commit `f625bb7` and the coupled lag map of `PREREG_COUPLED.md:53-62`. \(N=32\), \(c=1\), \(\phi=0\). The walk, the block, and the floored width are `measured_checks.py:146-196` and `:332-396` at that commit. Starts of the one-dimensional map are \(q\in\{0,1/4,1/2,3/4,1\}\). At most 40 updates. Stop when the absolute step is at most \(10^{-4}\).

The coupled step uses the previous state only:

\[
\rho\leftarrow\rho+\alpha(R^\star(q)-\rho),\qquad q\leftarrow q+\beta(Q_{\mathrm{mid}}(\rho)-q).
\]

\(R^\star\) is the mean of the tied floored widths. \(Q_{\mathrm{mid}}\) interpolates the midpoint-block returns on \([1,9]\) and holds the endpoint outside it, as `PREREG_COUPLED.md:43-51`. Four hundred steps. The tail is steps 200 through 399. Initial conditions \((1,0)\), \((5,0.5)\), \((9,1)\).

The walk has integer time. The dense axis is every integer \(T\) from 300 through 1200. Stakes \(w\in\{1,2,4\}\). Gains \((\alpha,\beta)\in\{(0.5,0.5),(1,1),(1.5,1.5)\}\). The cheap fine grid is \(T=500\) only, with \(\alpha=\beta\in\{0.25,0.5,0.75,1,1.25,1.5,1.75\}\).

## 2. Classifier

On the one-dimensional map, the least period is 1 when every start stops. Otherwise it is the smallest \(p\in\{2,\ldots,16\}\) such that every non-stopped start has at least \(2p\) updates and the last \(2p\) of them satisfy \(|q_{k+p}-q_k|\le 10^{-9}\). Otherwise the horizon is `OTHER` and the period is undefined.

On the coupled map, the least period is the smallest \(p\in\{1,\ldots,32\}\) such that every tail index \(i\) with \(i+p\) still in the tail has distance at most \(10^{-3}\) in \((\rho,q)\). \(p=1\) is a fixed point. Otherwise `OTHER`. The three initial conditions must share that period. If they do not, the horizon is `SPLIT`.

The rotation number is \(0\) at period 1 and \(1/p\) at period \(p\ge 2\). A plateau is at least three consecutive integers \(T\) with the same rotation number. An interior rate has tail-mean \(\rho\) strictly between \(1+10^{-3}\) and \(9-10^{-3}\). An endpoint rate is within \(10^{-3}\) of 1 or of 9.

## 3. Predictions

**P-port.** At stake 2, \(T=415\) is period 1 and the mean terminal is within \(10^{-6}\) of \(0.246706007043\). \(T=500\) is period 2 and the two levels, sorted, are within \(5\times 10^{-7}\) of \(0.288952\) and \(0.291620\). \(T=831\) is period 1 and the mean terminal is within \(10^{-6}\) of \(0.422916079022\). At \(T=550\), gain \((1,1)\), each of the three initial conditions is period 1 with \(\rho\) within \(10^{-6}\) of 6 and \(q\) within \(10^{-9}\) of \(0.313065981732\). Fails if any clause misses. A pass says the script is the recorded map.

**P-band.** At stake 2 the horizons with rotation number \(1/2\) form one plateau, that plateau contains 500, and no horizon outside it has rotation number \(1/2\). Fails if the set is empty, split, or not a plateau.

**P-where.** Every horizon of that plateau lies strictly between 415 and 831. Fails if the plateau includes 415 or 831 or extends outside that open interval. If P-band has no unique plateau, P-where fails.

**P-align.** Let \(\tau=1/\sin^2(\pi/(2\cdot 32))\), the gap clock in the T81 review (`REVIEW_MEASURED_INDEPENDENT.md:41-43`). Let \(C\) be the midpoint of the plateau's end horizons. For each \(r\in\{1/2,1,5/4,4/3,3/2,2\}\), \(|C/(r\tau)-1|>0.05\). The prediction is that the band is not on those ratios. Fails if any ratio is within 5 percent, or if there is no unique plateau.

**P-stair.** At stake 2 every horizon in the scan has period 1 or 2. Fails if any horizon has period 3 or higher, or is `OTHER`. A devil's staircase would be three or more distinct positive rationals. This line says that staircase is absent.

**P-single.** At each stake in \(\{1,2,4\}\) the horizons with rotation number \(1/2\) form at most one contiguous block, of any length. Fails if any stake has two or more such blocks.

**P-gain.** Let \(N(\alpha,\beta)\) be the number of scan horizons whose coupled orbit, at stake 2 and the midpoint block, is period 1 with an interior rate. \(N(1.5,1.5)-N(0.5,0.5)\le 2\). Separately, the number of horizons whose least period differs between \((0.5,0.5)\) and \((1.5,1.5)\) is at most 2. The bands do not widen with the gain, and the gain does not create new periods. Fails if either count exceeds 2. On the fine grid at \(T=500\), all seven equal gains have the same least period. Fails if they do not.

**P-null.** The null is that the period-2 orbit is the floor in the width. The comparison map keeps the same angle grid, 181 points, and the same minimizer \(\theta^\star\), and sets

\[
W=1+8\,P_D(\theta^\star)/P_D(\pi/2)
\]

without the floor. The next return is the linear interpolation of the integer-width midpoint returns at \(\lfloor W\rfloor\) and \(\lceil W\rceil\), with width 1 and width 9 as the ends. The same five starts and the same stop rule apply. At \(T=500\), at \(T=550\), and at the integer nearest \(C\), this map is period 1. The same three horizons on an angle grid of 2881 points are period 1. Fails if any of the six runs is not period 1. The floored map at \(T=500\) stays the port above. A pass of P-null says the cycle died when the floor was removed.

## 4. What a miss would mean

In-model only. A split band or a period above 2 would be the staircase this lock says is absent. A center within 5 percent of \(r\tau\) would say the gap clock, not only the entrance curve, sits under the band. A gain that adds interior horizons would be the tongue widening. A period-2 orbit that survives the interpolation would say the cycle is not the floor. None of these edits a locked score. This scan does not estimate \(K_c\).

## 5. What this file does not do

It does not score. It does not edit a locked preregistration, `THEORY.md`, or `CORE.md`. Deviations after this commit go to `DEVIATIONS.md`, appended. This file is not edited after the locking commit.
