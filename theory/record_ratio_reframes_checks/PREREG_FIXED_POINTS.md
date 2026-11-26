# T76 preregistration: 0 and 1 as candidate fixed points

*Tuesday 24 November 2026 (UTC). Written and committed before any fixed-point script and before any fixed-point grid. Branch `forge-record-ratio-reframes`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. The earlier lock `PREREG.md` (sha256 `8e495b7b…fce8`) is not edited. Locked by sha256 in `PREREG_FIXED_POINTS.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This lock file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. The qubit, the dephasing channel, and the two record functionals are inputs from draft #252. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\).

## 0. Question

Consistency readings (no-arbitrage with pointer-plus-garbling; match to R1 off the pointer) point at \(\kappa_D=0\). The structural picture (one shared coefficient; antipodal record cost flat in \(\theta\); the ledger \(I+P_D=H(M)-\mathbb{E}[S(\rho)]\)) points at ratio \(1\). Treat the two as candidate fixed points of a composition, not as rival answers that one of them has to win.

Three claims, each with a line a grid can miss.

1. **Flow.** Under sequential composition, under parallel composition of independent worlds, and under coarse-graining a record of records, does an effective ratio move? Are \(0\) and \(1\) the only fixed points? Which is stable, and what sets the basin boundary?
2. **Switch.** Is there a parameter — the stake \(w\), or the fraction \(\lambda\) of trials on which the post-measurement state is part of the kept behavior — at which the selected angle changes from the ratio-\(0\) design to the ratio-\(1\) design?
3. **Duality.** Is there an exact involution that pairs the ratio-\(0\) regime with the ratio-\(1\) regime?

The chain-rule remark in `PREREG.md:21-23` is kept as the sequential and independent-world cases below. It is not the whole of composition. Those two cases are now scored. They are not re-opened as a reason to skip the menu and the repeated record.

## 1. Prior exposure (disclosed, not a result of this lock)

- Published antipodal closed form at complete dephasing, \(r=0.6\): \(P_D+P_\chi\) independent of \(\theta\), \(P_\chi(0)=0.096372378511\), and pure mutual information first has a unique \(\theta=0\) minimizer at \(w_\star=3.209014724815\) when \(\phi=0\). The formula for \(w_0\) below is that \(w_\star\) when \(|\kappa_D-\kappa|=1\). Matching it is a check, not a new forecast.
- T75 Route A: pointer measurement plus a binary symmetric channel of crossover \((1-\cos\theta)/2\) reproduces the direct channel, and the cost gap is \(\kappa_D P_D\). Adopted here as already proved on that ensemble. The new claim is the fixed-point reading of that gap, and the boundary at which the two paths stop being the same behavior.
- T75 ledger identity, for this rank-1 pinch. Adopted. It is not a price.
- The post-hoc window in `posthoc_windows.out`, plant \((1,0.5)\), moved between about \(w=1.40\) and \(w=1.60\). The phase boundary below puts that plant's window at \(|\delta|/r^2\) to \(|\delta|\,w_\star\) with \(|\delta|=0.5\). Agreement with that window is a check against exposure already in hand, not an independent location of the band.
- A hand evaluation, not a grid, of the two-copy joint at the antipodal endpoints: \(P(M_1=M_2=+1)\) is \(0.295\) at \(\theta=0\) and \(0.25\) at \(\theta=\pi/2\), and the joint-entropy gap is near two hundredths of a nat. The locked bar on that range is \(0.005\). The hand gap is not a tolerance.

Not evaluated before this lock: the repeated-record grids, the conditional mutual information of a second pinch, the affine residual of the two-copy cost on the biased ensemble, and the sign of the endpoint slopes at the interior stakes named below.

## 2. Model (same objects as `PREREG.md` §3)

One qubit. Radius \(r=0.6\). Dephasing multiplies Bloch \(x\) and \(y\) by \(\gamma\). Projective direction \(n(\theta)=(\sin\theta,0,\cos\theta)\), \(\theta\in[0,\pi/2]\). Binary entropy \(h\) in nats. For this rank-1 pinch,

\[
P_D=\mathbb{E}[S(\Phi_\theta(\rho))-S(\rho)],\qquad I(W;M)=H(M)-\mathbb{E}[S(\Phi_\theta(\rho))].
\]

Ensembles ANT and BIAS as in `PREREG.md` §3. Stake \(A(\phi)\), loss \(L=\mathbb{E}[(y-\mathbb{E}[y\mid M])^2]\), with \(y\) read from the pre-dephasing Bloch vector. Cost \(J=\kappa I+\kappa_D P_D+w L\). Coefficients nonnegative. Write \(\delta=\kappa_D-\kappa\) and \(q=\kappa_D/\kappa\) when \(\kappa>0\).

Grid: \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\). Minimal when within \(10^{-9}\) of the smallest cost. Unique means one grid point. Ties report the smallest \(\theta\) and are flagged. `SEED = 20261124` is set and not drawn from.

**Repeated record of one world.** \(n\) copies are prepared in the same \(\rho_W\) and measured i.i.d. at one \(\theta\). The count \(K\) of \(+1\) outcomes is the sufficient statistic. \(I_n=I(W;K)\). The loss \(L_n\) uses \(\mathbb{E}[y\mid K]\). The disturbance adds, \(P_{D,n}=n P_D\), because the joint state is a product and the von Neumann entropy of a product adds. Cost \(J_n=\kappa I_n+\kappa_D\, n P_D+w L_n\).

**Independent worlds.** Two independent draws of \(W\), each measured once. Costs, mutual informations, disturbances, and losses add. This is the product the chain rule does not mix.

**Reuse fraction.** On a fraction \(\lambda\in[0,1]\) of trials the post-measurement state is part of the kept behavior and the disturbance is charged; on the rest only the classical outcome is kept. The charged disturbance coefficient is \(\lambda\kappa_D\). No other term changes. \(\lambda\) is a multiplier of \(\kappa_D\), not a third resource.

## 3. Phase boundary (the switch)

Scope of the closed form in this section: ANT, \(\gamma=0\), \(\phi=0\). Both \(P_D\) and \(L\) have a factor \(\sin\theta\) in their \(\theta\)-derivatives, so \(\theta=0\) and \(\theta=\pi/2\) are critical points of \(J\). For \(\delta<0\), with \(\Lambda(\theta)=\ln\frac{1+r\cos\theta}{1-r\cos\theta}\),

\begin{align*}
w_\pi(|\delta|)&=|\delta|/r^2,\\
w_0(|\delta|)&=|\delta|\,\ln\frac{1+r}{1-r}\big/(2r^3),\\
w_{\mathrm{crit}}(\theta)&=|\delta|\,\Lambda(\theta)/(2r^3\cos\theta).
\end{align*}

\(w_0(1)\) equals the published \(w_\star\). \(w_{\mathrm{crit}}\) decreases from \(w_0\) at \(\theta=0\) to \(w_\pi\) at \(\theta=\pi/2\), if the monotonicity check below passes.

- If \(\delta>0\) and \(w\ge 0\), or if \(\delta=0\) and \(w>0\): the unique minimizer is \(\theta=0\).
- If \(\delta=0\) and \(w=0\): \(J\) is constant on the grid (range \(<10^{-9}\)).
- If \(\delta<0\) and \(0\le w<w_\pi\): the unique minimizer is the grid point \(\theta=\pi/2\). Call this the ratio-\(0\) design at small stake (minimize \(I\), which on this menu is the equator).
- If \(\delta<0\) and \(w>w_0\): the unique minimizer is \(\theta=0\). Call this the ratio-\(1\) design (the stake's pointer; ratio \(1\) selects it for every \(w>0\)).
- If \(\delta<0\) and \(w_\pi<w<w_0\): the minimizer is interior, and it lies within one grid step of the unique root of \(w=w_{\mathrm{crit}}(\theta)\).

*Fails if* a listed cell is in the wrong phase, a predicted unique minimizer ties, an interior root is missing or not unique on \((0,\pi/2)\), or the grid minimizer misses that root by two or more grid steps. A miss means the endpoint-stability algebra is not the minimizer on this grid. Report the cell. Do not move a boundary. Next, if the only misses are interior cells: a finer grid in a new preregistration. If an endpoint cell misses: the derivative factor is not the stability condition, and the phase reading stops.

**Monotonicity.** On fifty equally spaced \(\theta\) in \([0.02,\pi/2-0.02]\), \(w_{\mathrm{crit}}(\theta)/|\delta|\) is strictly decreasing. *Fails if* any consecutive pair increases.

**Listed cells, \(\kappa=1\).** Phases are predictions.

| \(q\) | \(w\) | phase |
|---:|---:|---|
| \(0\) | \(1\) | equator |
| \(0\) | \(3\) | interior |
| \(0\) | \(10\) | pointer |
| \(0.5\) | \(1\) | equator |
| \(0.5\) | \(1.5\) | interior |
| \(0.5\) | \(2\) | pointer |
| \(0.67\) | \(1\) | interior |
| \(1\) | \(0\) | flat |
| \(1\) | \(1\) | pointer |
| \(2\) | \(1\) | pointer |

The cells at \(q=0\), \(w\in\{1,10\}\), and at \(q=1\), \(w=0\), sit on published or already-scored sides. They are checks. The interior cells and \(q\in\{0.5,0.67,2\}\) are the forecast.

**Slopes, step \(10^{-4}\).** Just to the right of \(0\), and just to the left of \(\pi/2\): the difference quotient of \(J\) has the sign of the phase (negative leaving an endpoint that is a local maximum, positive leaving an endpoint that is a local minimum), and absolute value \(>10^{-6}\), on the cells \(q=0,w=1\) (equator), \(q=0,w=10\) (pointer), and \(q=0.5,w=1.5\) (interior: both endpoints local maxima, so the quotient just right of \(0\) is negative and the quotient just left of \(\pi/2\) is positive). *Fails if* a sign is wrong or a quotient is at most \(10^{-6}\) in absolute value.

**Where the same formula is not claimed.** ANT, \(\gamma=1/2\), \(\phi=0\), \(\kappa=1\), \(q=0\), \(w=3\). The \(\gamma=0\) root at that stake and the \(\gamma=1/2\) minimizer differ by \(\ge 0.1\) rad. *Fails if* they differ by \(<0.1\). Then the complete-dephasing boundary still locates the partial-dephasing angle, and the formula is less special to \(\gamma=0\) than this sentence says. Report the two angles. Do not refit.

**Reuse, nominal ratio \(1\), \(\kappa=1\), \(w=1\).** Charged coefficient \(\lambda\kappa_D=\lambda\). The phase rule above is applied to \(\delta=\lambda-1\).

| \(\lambda\) | phase |
|---:|---|
| \(0\) | equator |
| \(0.5\) | equator |
| \(0.66\) | interior |
| \(0.8\) | pointer |
| \(1\) | pointer |

*Fails if* a row is in the wrong phase. This does not add a resource. It says the switch from the equator to the pointer, at a price list that is nominally ratio \(1\), is the same boundary with \(\kappa_D\) replaced by \(\lambda\kappa_D\).

## 4. Flow

**F-seq. Same system, second pinch.** ANT and BIAS, \(\gamma=0\). Angle pairs \((\theta_1,\theta_2)\) from \(\{0,\pi/4,\pi/2\}\). The conditional mutual information \(I(W;M_2\mid M_1)<10^{-9}\) on every pair. When \(\theta_2=\theta_1\), the second disturbance is \(<10^{-9}\). On the pair \((0,\pi/2)\), the second disturbance is \(>0.05\). At \(\theta_1=0\), \(\kappa=\kappa_D=1\), the minimum over the \(721\)-grid of \(\theta_2\) of the added cost \(\kappa I(W;M_2\mid M_1)+\kappa_D P_{D,2}\) is \(<10^{-9}\).

*Fails if* any conditional mutual information is \(\ge 10^{-9}\), the same-basis disturbance is \(\ge 10^{-9}\), the right-angle disturbance is \(\le 0.05\), or the best second pinch has added cost \(\ge 10^{-9}\). A failure means a second pinch on the same system can change the price. The "every ratio is a fixed point" reading of sequential composition then stops. Next: report the pair and the added cost. Do not add a third measurement in this file.

**F-prod. Independent worlds.** ANT, \(\gamma=0\), \(\phi=0\), two independent draws, same \(\theta\). At five grid points \(\theta\in\{0,0.3,\pi/4,1,\pi/2\}\) and at \((q,w)\in\{(0,1),(1,1),(2,1)\}\) with \(\kappa=1\), the product cost equals \(2J\) within \(10^{-9}\), and the product minimizer equals the single-copy minimizer within one grid step.

*Fails if* a cost misses by \(\ge 10^{-9}\) or a minimizer separates by two or more grid steps. Then independent copies do not preserve the ratio. Report the cell.

**F-menu. Coarse-graining by pointer plus garbling.** ANT, \(\gamma=0\). For every grid \(\theta\), a pointer measurement followed by a binary symmetric channel of crossover \((1-\cos\theta)/2\) matches the direct channel's \(P(M=+1\mid W)\) within \(10^{-12}\) on every label. The direct record cost minus the garbling-path record cost equals \(\kappa_D P_D(\theta)\) within \(10^{-12}\), at \((\kappa,\kappa_D)=(1,1)\). \(P_D(\pi/2)>0.05\). The menu cost of the classical channel is the garbling-path cost, which does not depend on \(\kappa_D\). The one-step map on ratios is \(q\mapsto 0\) for every \(q\ge 0\). Ratio \(0\) is a fixed point. Ratio \(1\) is not: the gap at \(\theta=\pi/2\) equals \(P_D(\pi/2)\) within \(10^{-12}\), which is not zero.

*Fails if* any channel probability misses by \(\ge 10^{-12}\), the gap misses \(\kappa_D P_D\) by \(\ge 10^{-12}\), or \(P_D(\pi/2)\le 0.05\). Then Route A's identity is not reproducing on this grid, and the fixed-point reading is withdrawn with it. The basin statement that is being checked, not a second grid: the map is available only when the kept behavior is the classical channel. The direct pinch leaves the qubit diagonal in \(n(\theta)\); the pointer pinch leaves it diagonal in \(z\). When that residual state is part of the behavior, the two paths are different behaviors, the map is not a comparison, and this route does not send \(q\) to \(0\).

**F-rep. Repeated record of one world.** ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\).

- At \(q=0\), \(w=1\): the unique minimizer is \(\theta=\pi/2\) for \(n\in\{1,2,8\}\).
- At \(q=1\), \(w=1\): the unique minimizer is \(\theta=0\) for \(n\in\{1,2,8\}\), and also for \(n=20\).
- At \(q=0\), \(w=4\): the unique minimizer at \(n=1\) is \(\theta=0\); at \(n=8\), \(J_8(\pi/2)<J_8(0)\) and the minimizer is \(\ge 0.3\).
- At \(q=0.5\), \(w=1.5\): the \(n=8\) minimizer is at least \(0.05\) rad below the \(n=1\) minimizer.
- At \(q=1\), \(n=2\): the range of \(I_2+2 P_D\) over the grid is \(>0.005\).
- At \(n=16\), \(\theta=0\): \(|I_{16}-(3/2)\ln 2|<0.02\). The saturated value is the elementary count: infinite pointer data identifies \(\pm z\) and leaves \(\pm x\) exchangeable, so \(I_\infty=H(W)-\tfrac12\ln 2=\tfrac32\ln 2\) with \(H(W)=\ln 4\).
- Certificate, \(q=1\), \(w=1\), \(n=20\): \(J_{20}(\pi/2)>J_{20}(0)\).

*Fails if* a listed minimizer is in the wrong place, a predicted unique cell ties, the two-copy range is \(\le 0.005\), the saturated mutual information misses by \(\ge 0.02\), or the certificate inequality reverses. A two-copy range at or below the bar means ratio \(1\) still flattens the repeated record at this tolerance; report the range and do not claim flatness is lost. An \(n=8\) minimizer below \(0.3\) at \(q=0,w=4\) means the repeated record has not left the pointer; next is \(n=16\) in a new preregistration, this prediction unchanged. An \(n=8\) angle at \(q=0.5,w=1.5\) that does not drop by \(0.05\) means repetition does not push this interior point toward the pointer; report both angles.

**F-span. The repeated cost need not stay in the single-shot family.** BIAS, \(\gamma=0\), \(\phi=0\), \(\kappa=\kappa_D=1\), \(n=2\). Over the grid, fit \(I_2+2 P_D\) by least squares, with an intercept, to \(I_1\) and \(P_D\). The max absolute residual is \(>0.01\).

*Fails if* the residual is \(\le 0.01\). Then the two-copy cost is an affine image of the single-shot pair on this ensemble, at this tolerance. Report \(\alpha\), \(\beta\), and the intercept. If \(\alpha\neq 0\), report \(\beta/\alpha\). Do not declare that the ratio flowed to \(0\) or to \(1\). Do not declare that it left the family.

## 5. Duality

**D-value.** Record cost \(R=\kappa I+\kappa_D P_D\), the loss omitted. The involution \(\delta\mapsto-\delta\) is \((\kappa,\kappa_D)\mapsto(\kappa,2\kappa-\kappa_D)\), which sends \(q=0\) to \(q=2\) and fixes \(q=1\). On ANT, \(\gamma\in\{0,1/2\}\), \(\kappa=1\), \(\delta=1\): the range over \(\theta\) of \(R(\delta)+R(-\delta)\) is \(<10^{-9}\). On BIAS, \(\gamma=0\), the same range is \(>0.02\).

*Fails if* an antipodal range is \(\ge 10^{-9}\) or the biased range is \(\le 0.02\). Then the ledger reflection is not the involution on this menu, or it survives off the antipodal ensemble. Report the ranges.

**D-argmin.** ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\). At \(w=1\), the unique minimizer at \(q=0\) and the unique minimizer at \(q=1\) differ by \(\ge 1\) rad. At \(w=1\), the unique minimizer at \(q=2\) equals the minimizer at \(q=1\) within one grid step, and differs from the minimizer at \(q=0\) by \(\ge 1\) rad. No stake-preserving map can send the \(q=0\) minimizer to the \(q=1\) minimizer at this \(w\), because one angle is the equator and the other is the pointer.

*Fails if* the \(q=0\) and \(q=1\) angles differ by \(<1\), or \(q=2\) separates from \(q=1\) by two or more grid steps. A \(q=0\)/\(q=1\) gap below \(1\) at this stake means the two regimes already share a design here, and the obstruction to a stake-preserving duality is not this cell.

The involution that the ledger does provide pairs \(0\) with \(2\). It does not pair \(0\) with \(1\). Ratio \(1\) is the fixed ratio of that involution. That is the duality claim. There is no second, unnamed map being scored.

## 6. What this run will not say

It will not edit `THEORY.md` or `PREREG.md`. It will not say that the ratio has been solved. It will not say that a miss removes a fixed point from further work. It will not treat the ledger identity, or T75 Route A, as a sentence that was missing from A1–A8. A fixed point that appears only by adopting that identity or that gap is marked as adopted from T75. The phase boundary is **ELEMENTARY** from the closed form if the grid matches it, and a puzzle if the grid does not.

## 7. Output

The script prints one line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test. `PREREG.md` checks are not re-run from this script.
