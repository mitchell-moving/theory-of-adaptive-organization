# T76 preregistration: repeated records, where the design goes

*Tuesday 24 November 2026 (UTC). Written and committed before any script in this file's scope and before any grid at \(n=256\). Branch `forge-record-ratio-reframes`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Earlier locks `PREREG.md`, `PREREG_FIXED_POINTS.md`, and `PREREG_MHD.md` are not edited. Locked by sha256 in `PREREG_REPEAT_ASYMPTOTE.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This lock file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\).

## 0. Question

Under repeated i.i.d. records of one world, the single-shot ratio-\(0\) design is the equator and the ratio-\(1\) design is the pointer. Do those two designs survive as \(n\) grows, or does repetition move the design while leaving the ratio at the boundary \(0\)?

## 1. Prior exposure

- `fixed_point_checks.out:9`. At \(q=0\), \(w=4\), the minimizer is the pointer at \(n=1\) and \(0.966476\) at \(n=8\), with \(J_8(\pi/2)=0.720000<J_8(0)=0.746122\). At \(q=0\), \(w=1\), the minimizer is the equator through \(n=8\). \(I_{16}(\theta=0)=0.713026\) against \(\tfrac32\ln 2=1.039721\). This file does not rescore that line and does not predict \(0.559888\).
- The single-shot phase boundary and \(P_D=\tfrac12\big[h((1+r|\cos\theta|)/2)-h((1+r)/2)\big]\) on ANT, \(\gamma=0\). \(P_D=0\) only at \(\theta=0\) on \([0,\pi/2]\). \(P_D(\pi/2)=P_\chi(0)=0.096372378511\).
- Hand evaluation of that formula, not a grid: \(P_D(\pi/4)=0.049914607565\).
- MHD lock: at fixed design, \(J\) is linear in the ratio. Adopted as the reason a product \(q(1-q)\) is not expected here. Not rescored except for the one second-difference line below, which is the repeated-record case.

## 2. Model

Same objects as `PREREG_FIXED_POINTS.md` §2. ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\), \(r=0.6\). \(n\) i.i.d. pinches, sufficient statistic \(K\), \(J_n=\kappa I(W;K)+\kappa_D\, n P_D+w L_n\). Grid \(721\) points. Tie \(10^{-9}\). `SEED = 20261124` is set and not drawn from.

## 3. Elementary limits, checked only through the predictions below

On this ensemble the four outcome probabilities are \((1\pm r\cos\theta)/2\) and \((1\pm r\sin\theta)/2\).

- At \(\theta=0\), the two \(x\)-labels share probability \(1/2\). Infinite data identifies \(\pm z\) and leaves \(\pm x\) exchangeable. \(I_\infty=\tfrac32\ln 2\). The stake coordinate \(y\) is \(+r\), \(-r\), \(0\), \(0\), and it is a function of the identified class, so \(L_\infty=0\).
- At \(\theta=\pi/2\), \(I_\infty=\tfrac32\ln 2\) and \(L_\infty=r^2/2\), because the unresolved class is \(\pm z\) and \(y=\pm r\) there.
- At \(\theta=\pi/4\), the rates collide in sign pairs. \(I_\infty=\ln 2\) and \(L_\infty=r^2/4\).
- At every other \(\theta\in(0,\pi/2)\), the four rates are distinct, so \(I_\infty=2\ln 2\) and \(L_\infty=0\).

At \(q=0\), the limiting cost is \(I_\infty+w L_\infty\). The equator is above the pointer by \(w r^2/2\). A generic angle is above the pointer by \(\tfrac12\ln 2\). The collision angle is below the pointer when

\[
w < \frac{2\ln 2}{r^2}=3.850817669777.
\]

At \(w=4\) the pointer is below the collision angle by \(0.013426409720\). At \(w=1\) the collision angle is below the pointer by \(0.256573590280\). These four decimals are the closed form, evaluated before the grid.

For \(q>0\), \(n P_D(\theta)\) diverges at every \(\theta>0\) while \(I_n\le 2\ln 2\) and \(L_n\le r^2\). The repeated-record minimizer is driven to the pointer.

The deficit \(I_\infty(\theta=0)-I_n(\theta=0)\) equals the entropy of the three-rate label \(\{+z,-z,x\text{-pair}\}\) given \(K\). Hoeffding with half-gap \(0.15\) puts that error below \(2\times 10^{-5}\) at \(n=256\), and the Fano bound on the deficit is then below \(10^{-3}\), under the \(0.0134\) gap at \(w=4\). The bound covers only that classification error at \(\theta=0\). It does not cover other angles. The grid is the check.

## 4. Predictions

**R-class.** At \(n=16\), \(\theta=0\): \(I_{16}=\tfrac32\ln 2-H(C\mid K)\) within \(10^{-9}\), and \(H(C\mid K)>0.2\). \(C\) is the three-rate label.

*Fails if* the identity misses by \(\ge 10^{-9}\) or the conditional entropy is \(\le 0.2\). Then the locked gap at \(n=16\) is not this overlap. Report both numbers. Do not edit `fixed_point_checks.out`.

**R-low.** \(q=0\), \(w=1\), \(n=256\). The unique minimizer lies within \(0.15\) rad of \(\pi/4\). \(J(\pi/4)<J(0)-0.05\) and \(J(\pi/4)<J(\pi/2)-0.05\).

*Fails if* the minimizer is outside that window, the cell ties, or either cost gap is \(\le 0.05\). Then the large-\(n\) ratio-\(0\) design at this stake is not the collision angle. Report the angle and the two gaps.

**R-high.** \(q=0\), \(n=256\). At \(w=4\) and at \(w=10\), the unique minimizer is the grid point \(\theta=0\), and \(J(0)<J(\pi/4)\).

*Fails if* either cell is not uniquely the pointer, or \(J(0)\ge J(\pi/4)\). Then \(n=256\) has not reached the stake \(2\ln 2/r^2\). Report the angle. Do not move that stake.

**R-pos.** \(n=256\), \(w=1\). At \(q=1\) and at \(q=0.5\), the unique minimizer is \(\theta=0\).

*Fails if* either cell is not uniquely the pointer. Then a positive ratio has not been driven to the pointer by this \(n\). Report the angle.

**R-ratio.** \(n=256\), \(w=1\), \(q\in\{0,0.5,1,2\}\). \(J^\star(q)\ge J^\star(0)-10^{-9}\). At \(\theta=\pi/4\), the second difference of \(J\) in \(q\) with step \(1/2\), at \(q=1\), has absolute value \(<10^{-9}\).

*Fails if* any ratio undershoots \(J^\star(0)\) by \(\ge 10^{-9}\), or the second difference is \(\ge 10^{-9}\). Then repetition has made an interior ratio cheaper, or \(J_n\) is not linear in the ratio. Report the cell. Do not fit a product in \(q\).

## 5. What this run will not say

It will not edit `THEORY.md`, the earlier locks, or `fixed_point_checks.out`. It will not say the ratio has been solved. It will not say a miss removes either candidate design. It will not treat \(2\ln 2/r^2\) as a coefficient of \(J\). The Hoeffding sentence is the reason \(n=256\) was chosen. It is not a scored pass.

## 6. Output

The script prints one line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test.
