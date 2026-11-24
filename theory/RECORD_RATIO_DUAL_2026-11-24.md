# Record-price ratio: shadow price of a disturbance budget

*24 November 2026 (UTC). Two locks, each committed before its grid. The shadow-price lock is `theory/record_ratio_dual_checks/PREREG.md`, sha256 `4e306d83…25ec`. The floor lock is `PREREG_FLOOR.md`, sha256 `29879441…c73a`. Self-check, not an independent review. `THEORY.md` is unchanged (blob `6caadae569116a94a74563398be94cebf6e99e9b`). Open-work row T77. Status words are those at `CORE.md:169`. Nothing here derives general relativity, quantum mechanics, or holography.*

*T76 showed that \(J\) is linear in \(q=\kappa_D/\kappa\), so minimizing \(J\) over the ratio cannot select an interior value, and on the antipodal menu it selects the boundary \(0\) whenever \(P_D>0\). This note asks whether that coefficient is instead the Lagrange multiplier of a disturbance budget \(P_D\le D\) in \(\min(\kappa I+w L)\).*

## Answer

**Model implication.** On the menus scored here, ratio \(1\) is not the shadow price of any disturbance cap the repository already names. Ratio \(0\) is the shadow price of a slack cap. A cap that binds on the antipodal menu, at a positive stake, prices a ratio strictly below \(1\). The largest such price, at stake \(w\), is \(1-w/w_\star\).

The hope that some natural \(D\) would give \(\lambda^\star=1\) is a **Puzzle**. The break is that the named sources are not budgets that bind at that price. A \(D\) chosen so the multiplier equals \(1\) would be a hand pick, and this note does not make one.

A gravitational floor is a further candidate, scored in its own lock below. It does not supply \(\varepsilon(m)\), and the coefficient it does produce is negative. It is not a reason \(\kappa_D\) cannot be \(0\).

## What was scored

Nine lines, `shadow_price_checks.out`, `FAILS 0`. The predictions were the structural consequences. They matched.

**Ledger stock, antipodal.** \(D=P_\chi(0)=0.096372378511\). That number is \(I+P_D\), and it is the maximum of \(P_D\). The cap \(P_D\le D\) removes no design (`H-led`, gap \(0\)). At \(w\in\{1,w_\ast,10\}\) the shadow price is \(0\).

**How large a binding multiplier can get.** For \(\delta=\lambda-1<0\) the stationary angle fixes \(\lambda=1-w\cdot 2r^3\cos\theta/\Lambda(\theta)\). On \((0,\pi/2)\) at \(w=1\) the grid maximum is \(0.688377609733\), against the pointer-end ceiling \(1-1/w_\star=0.688377871168\) (`H-bound`). The equator end of the same formula is \(1-wr^2=0.64\) at \(w=1\), and \(1-3\ln 2=-1.079441541680\) at \(w=w_\ast\). A negative value means the cap does not bind. At no positive stake does the formula reach \(1\). Reaching \(1\) would require \(w=0\).

**Derivative check.** At \(\theta=1\), \(w=1\), the formula is \(0.652985548762\) and the difference quotient of \(I+w L\) along \(P_D\) agrees to \(2.242\times 10^{-10}\) (`H-deriv`). The phase boundary is the shadow price. **ELEMENTARY** for the closed form, **NUMERICAL** for the quotient.

**Off the antipodal pair.** The ledger at \(\theta\in\{0,0.4,\pi/2\}\) is \(0.050672\), \(0.057695\), \(0.096372\), range \(0.045701\). There is no single ledger cap. The ratios that level \(\theta=0\) against \(0.4\) and against \(\pi/2\) are \(0.548714\) and \(0.525792\). They are the review's \(0.549\) and \(0.526\), and they are not one price (`H-off`). **Adopted** as the ensemble from review 1 at `21ab5f0`, recomputed here.

**Rank-2 block.** \(P_D=0\), \(I=0\), and the two sides of the identity differ by \(\tfrac12\ln 2=0.346573590280\) (`H-rank`). One instrument has no design multiplier. **Adopted** from the review's state, recomputed here.

**Reeb–Wolf and the ruin cap.** Theorem 3 bounds heat by an entropy change. It does not name a \(P_D\) cap. The ruin cap is \(P(\mathrm{ruin})\le\varepsilon_r\), and this menu does not convert \(\varepsilon_r\) into a disturbance. Both lines are `NO-D` (`H-reeb`, `H-ruin`). **KNOWN** for the theorem, as in T75 Route C. The ruin sentence is A2.

**The stake \(w_\ast\).** \(w_\ast=5.776226504666\) sits \(2.998449\) above \(1/r^2\) and \(2.567212\) above \(w_\star\). At that stake the single-shot minimizer of \(I+w L\) is the pointer, where \(P_D=0\), so the ledger cap is slack (`H-w`). \(w_\ast\) is where a repeated equatorial record stops being cheaper than a resolved one. It is not where a disturbance budget starts to bind.

**No named source prices ratio \(1\).** `H-none` is `NO-NATURAL-D`.

## Where the reading breaks

The step that would produce ratio \(1\) is a binding cap whose multiplier equals \(\kappa\). On the antipodal menu the multiplier of \(P_D\le D\), when it is positive, equals \(1-w/w_\star\) at the pointer end and is smaller at every larger angle. That expression equals \(1\) only at \(w=0\), where the record cost is flat and the multiplier is not a selector. The ledger stock is the wrong end of the same interval: it is the largest \(P_D\), so the inequality does not bind. The off-pair ledger is not one number. The rank-2 block has nothing to price. Reeb–Wolf and the ruin cap are constraints on other quantities.

What that says about \(0\) and \(1\). Complementary slackness does account for ratio \(0\): a cap that the minimizer of \(I+w L\) already meets has shadow price \(0\). It does not account for ratio \(1\) on these sources. Ratio \(1\) remains the fixed point of the destruction charge in review 1, which is not this budget.

A later inversion that picks \(D\) so the formula equals \(1\) is the hand pick this lock ruled out. It is not a next test.

**Model implication.** Conditional on \(\min(I+w L)\) subject to \(P_D\le D\) with \(D\) equal to the antipodal ledger, or with no \(D\) supplied by Reeb–Wolf or by the ruin cap: the shadow price is \(0\) or is undefined, not \(1\). Conditional on a cap that does bind on ANT at stake \(w>0\): the price is at most \(1-w/w_\star<1\). Conditional on \(w=w_\ast\): the single-shot design is the pointer and the ledger cap is slack. **ELEMENTARY** for the closed-form ceiling. **NUMERICAL** for the grid maximum, the derivative, and the off-pair levelers.

## Gravitational floor

**Model implication, not a derivation of gravity.** A record with mass might broadcast part of its state on a channel that cannot be screened. The candidate reading is a floor \(P_D\ge\varepsilon(m)>0\) on every such record, and a reason \(\kappa_D\) cannot be \(0\).

The citation was checked on Crossref on 24 November 2026 before the lock. Groszek, Woffinden, Harvey, White, and Davis, "Unblockable communication with gravity," *Science Advances* 12, issue 47 (2026), doi `10.1126/sciadv.aee0802`. The record is a journal article issued 20 November 2026. The paper reports a binary message encoded by moving a mass and read by a gravimeter through a brick wall, about \(0.7\) m, at about \(1\) bit per minute. That is an experimental communication result. **KNOWN** as that citation. It is not a measurement of \(P_D\).

The floor was allowed to come only from the four sources already named for \(D\): the ledger, Reeb–Wolf / Landauer, the ruin cap, and \(w_\ast\). The bit rate is not one of them. T64's barrier-to-mass step is an assumed input in another note. Using it here would add a free parameter. It was not used.

**Observed against the lock** (`floor_checks.out`, `FAILS 0`).

- **H-eps matches.** The line is `NO-EPS`. No decimal floor is printed.
- **H-sign matches.** At the probe \(\varepsilon=P_\chi(0)/2\), which is not \(\varepsilon(m)\), and at stake \(w=10\), the central-difference coefficient is \(q_{\mathrm{probe}}=-2.363872\) at \(\theta=0.767426\). It is negative, and it is not \(1\).
- **H-move matches.** The upper-budget price at the ledger and \(w=10\) is \(0\). The probe coefficient is not that price.

**Where the hope breaks.** A binding lower constraint \(P_D\ge\varepsilon\) carries a multiplier \(\mu\ge 0\) on \(\varepsilon-P_D\). That enters \(J\) as \(q=-\mu\le 0\). The probe is the numerical reading of that sign: about \(-2.36\), not \(+1\). An unscreenable channel, even if granted, prices a floor with the opposite sign from \(\kappa_D>0\). It does not move \(\lambda^\star\) of the upper budget. And nothing in the four sources fixes the size \(\varepsilon(m)\) without a new parameter. The \(1\) bit per minute stays a bit rate.

What that says about \(0\) and \(1\). Ratio \(0\) is still the shadow price of a slack upper cap. The floor does not push the coefficient up through \(0\). It pulls the other way, and only after a size is chosen. Choosing that size by hand is the move the shadow-price lock already ruled out.

The next test would be a formula already written in \(J\) or in one of the four sources that takes a mass and returns a nat of \(P_D\). No such formula is in those objects. Adding a coupling in order to have a number is not that test.

**Model implication.** Conditional on the four named sources: there is no \(\varepsilon(m)\). Conditional on a binding floor: the coefficient of \(P_D\) is nonpositive, and at the locked probe it is \(-2.363872\). Conditional on the ledger cap at \(w=10\): \(\lambda^\star=0\), unchanged. **ELEMENTARY** for the sign of a lower-constraint multiplier. **NUMERICAL** for the probe. The hope that the floor forces \(\kappa_D>0\) is a **Puzzle**. Not a derivation of gravity.
