# T77 preregistration: the ratio as a shadow price

*Tuesday 24 November 2026 (UTC). Written and committed before any script in this directory and before any shadow-price grid. Branch `forge-record-ratio-dual`, based on `forge-record-ratio-reframes` at `c534798`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\).

## 0. Question

\(J=\kappa I+\kappa_D P_D+w L\) is linear in the ratio \(q=\kappa_D/\kappa\). Minimizing \(J\) over \(q\ge 0\) cannot select an interior ratio. **Model implication, not an axiom:** a linear coefficient on a resource is the shadow price of a constraint. The candidate constraint is a disturbance budget \(P_D\le D\) in the problem \(\min(\kappa I+w L)\). Complementary slackness would then read: ratio \(0\) is a slack budget, and a positive ratio, possibly \(1\), is a binding budget whose value is set by \(D\).

## 1. Where D is allowed to come from

A cap chosen so that the multiplier comes out near \(1\) is not a result. It moves the open question. The only caps this lock scores are objects already in the repository:

1. **Ledger stock.** \(D_{\mathrm{led}}=H(M)-\mathbb{E}[S(\rho)]\). On the rank-1 antipodal menu this equals \(I+P_D\), and that sum is independent of \(\theta\). The number already printed is \(P_\chi(0)=0.096372378511\).
2. **Reeb–Wolf / Landauer.** Reeb and Wolf 2014, doi `10.1088/1367-2630/16/10/103011`, Theorem 3: \(\beta\Delta Q=\Delta S+I(S':R')+D(\rho'_R\|\rho_R)\), so \(\beta\Delta Q\ge\Delta S\). Landauer is the floor already cited at `theory/REPRESENTATION.md:120`. T75 Route C says this bound does not set \(\kappa_D/\kappa\).
3. **Ruin cap.** A2, `theory/REPRESENTATION.md:45`: \(P(\mathrm{ruin})\le\varepsilon_r\) is a feasibility cut, not a term. In the record menu the ruin cap is slack (`theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md`).
4. **The repeated-record stake** \(w_\ast=3\ln 2/r^2\). This is a stake, not a disturbance. It is scored only as test (c): is it the stake at which a named budget starts to bind?

No other number is a \(D\). In particular the script does not invert \(\lambda(D)=1\) and call the answer a budget.

## 2. Prior exposure

- Antipodal closed form, \(\gamma=0\), \(r=0.6\): \(P_D=\tfrac12\big[h((1+r|\cos\theta|)/2)-h((1+r)/2)\big]\), \(I=\tfrac12\big[\ln 2-h((1+r|\cos\theta|)/2)\big]\), \(L=r^2/2-r^4\cos^2\theta/4\) at \(\phi=0\). So \(I+P_D=P_\chi(0)\) and \(P_D\) rises from \(0\) at \(\theta=0\) to \(P_\chi(0)\) at \(\theta=\pi/2\).
- Phase boundary, \(\kappa=1\), \(\delta=\lambda-1<0\): the stationary angle satisfies \(w=|\delta|\,\Lambda(\theta)/(2r^3\cos\theta)\) with \(\Lambda=\ln\frac{1+r\cos\theta}{1-r\cos\theta}\). Hence the multiplier that holds a binding angle is \(\lambda=1-w\cdot 2r^3\cos\theta/\Lambda(\theta)\), and only while that value is nonnegative. Otherwise the cap is slack and the shadow price is \(0\).
- Hand evaluation of that formula, not a grid: \(w_\star=3.209014724815\), \(1/r^2=2.777777777778\), \(w_\ast=5.776226504666\). The binding multiplier is largest near the pointer, where it equals \(1-w/w_\star\). At \(w=1\) that ceiling is \(0.688377871168\). At the equator the same formula tends to \(1-wr^2\), which is \(0.64\) at \(w=1\) and \(1-3\ln 2=-1.079441541680\) at \(w=w_\ast\).
- Review 1 at `21ab5f0`, not recomputed here before the lock. Off the antipodal pair, equal mixture of the post-dephasing states \(+z\) and \(+x\) at \(r=0.6\): the ledger is \(0.050672\), \(0.057695\), \(0.096372\) at \(\theta\in\{0,0.4,\pi/2\}\). Pairwise levelers \(0.549\) and \(0.526\). Rank-2 block: \(P_D=0\), \(I=0\), sides differ by \(\tfrac12\ln 2\).

## 3. Model

\(\kappa=1\). ANT, \(\gamma=0\), \(\phi=0\), \(r=0.6\), grid \(721\) points, tie \(10^{-9}\). `SEED = 20261124` is set and not drawn from.

Off-pair: weights \(\tfrac12,\tfrac12\) on pre-dephasing Bloch \((0,0,r)\) and \((r,0,0)\), then \(\gamma=0\). That is the review's mixture.

Rank-2: one state \(\mathrm{diag}(1/2,1/4,1/4)\), Lüders instrument with projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\). No angle.

The shadow price \(\lambda^\star(D)\) is \(0\) when every minimizer of \(I+w L\) satisfies \(P_D\le D\). When the cap removes that minimizer, \(\lambda^\star\) is the nonnegative formula above at the boundary angle \(P_D(\theta)=D\). A negative formula means the cap does not bind.

## 4. Predictions

**H-led.** \(D=P_\chi(0)\). On the grid, \(\max P_D-D<10^{-9}\). At \(w\in\{1,w_\ast,10\}\), \(\lambda^\star=0\).

*Fails if* any grid point exceeds \(D\) by \(\ge 10^{-9}\), or any of the three shadow prices satisfies \(|\lambda^\star|\ge 10^{-6}\). Then the ledger stock removes a design or prices it. Report the cell. Do not replace \(D\).

**H-bound.** At \(w=1\), the formula on \(\theta\in(0,\pi/2)\) is at most \(0.688377871168\), and every grid value is \(\le 0.688377871168+10^{-6}\) and \(\le 0.70\). At \(w=w_\ast\) the equator limit \(1-3\ln 2\) is \(<0\), so a cap near the ledger does not bind and \(\lambda^\star(D_{\mathrm{led}})=0\).

*Fails if* any grid formula at \(w=1\) exceeds \(0.70\), or the reported maximum misses \(0.688377871168\) by \(\ge 10^{-4}\), or \(1-3\ln 2\ge 0\). Then a binding disturbance cap on this menu can price ratio \(1\). Report the angle. Do not invert the formula for a new \(D\).

**H-deriv.** At \(\theta=1\), \(w=1\), the formula equals \(0.652985548762\). The numerical ratio \(-(dI+w\,dL)/dP_D\), step \(10^{-4}\), agrees within \(10^{-4}\).

*Fails if* the absolute gap is \(\ge 10^{-4}\). Then the phase-boundary multiplier is not the derivative of \(I+w L\) along \(P_D\). Report both numbers.

**H-off.** On the off-pair menu the ledger at \(\theta\in\{0,0.4,\pi/2\}\) matches \(0.050672\), \(0.057695\), \(0.096372\) within \(5\times 10^{-4}\), and the range is \(>0.02\). The levelers of \(\theta=0\) against \(0.4\) and of \(\theta=0\) against \(\pi/2\) match \(0.549\) and \(0.526\) within \(5\times 10^{-3}\), and they differ by \(>0.01\). No single \(D\) is selected.

*Fails if* a ledger misses by \(\ge 5\times 10^{-4}\), the range is \(\le 0.02\), a leveler misses by \(\ge 5\times 10^{-3}\), or the two levelers differ by \(\le 0.01\). A range at or below the bar would mean the off-pair ledger is a single cap. Levelers that agree would be one price. Report the values. Do not pick one of the three ledgers and call it \(D\).

**H-rank.** \(P_D=0\) and \(I=0\) within \(10^{-12}\). The two sides of the ledger identity differ from \(\tfrac12\ln 2\) by \(<10^{-9}\). There is one instrument, so there is no design multiplier. The line records \(\lambda^\star\) as undefined, not as \(1\).

*Fails if* \(|P_D|\ge 10^{-9}\) or the identity gap misses \(\tfrac12\ln 2\) by \(\ge 10^{-6}\). Then this block has a disturbance a budget could price. Report the values.

**H-reeb.** Theorem 3 bounds heat by an entropy change. It does not name a number \(D\) with \(P_D\le D\) on this menu. The line is `NO-D`.

*Fails if* the script prints a numerical budget for this candidate. A printed budget would be a hand pick. The absence is the result this line is allowed to record.

**H-ruin.** The ruin cap is \(P(\mathrm{ruin})\le\varepsilon_r\). This menu has no formula from \(\varepsilon_r\) to a disturbance cap, and the record notes treat ruin as slack. The line is `NO-D`.

*Fails if* the script prints a numerical budget for this candidate.

**H-w.** \(|w_\ast-1/r^2|>1\) and \(|w_\ast-w_\star|>1\). At \(w=w_\ast\), \(q=0\), the unique minimizer on ANT is \(\theta=0\), so \(P_D=0\le D_{\mathrm{led}}\) and the ledger cap is slack.

*Fails if* either gap is \(\le 1\), or the minimizer is not uniquely the pointer. Then \(w_\ast\) sits on the single-shot onset where a disturbance cap would start to bind. Report the angle and the gaps. Do not move \(w_\ast\).

**H-none.** Across H-led, H-bound, H-rank, H-reeb, H-ruin, and H-off, no scored shadow price equals \(1\). H-off and the two `NO-D` lines contribute no price. The line is `NO-NATURAL-D`.

*Fails if* any scored \(\lambda^\star\) satisfies \(|\lambda^\star-1|<0.05\). Then a named source does set ratio \(1\). Report which source. Do not add a fifth source after the run.

What counts as the finding, stated before the run: \(\lambda^\star(D)\ne 1\) at every natural \(D\) this list actually contains, and Reeb–Wolf, the ruin cap, and the off-pair ledger do not provide a single \(D\) at all. That outcome is a puzzle for the hope that ratio \(1\) is the shadow price of one of these caps. It is not a reason to choose \(D\) by hand. A hand-chosen \(D\) would also count as that same finding.

## 5. What this run will not say

It will not edit `THEORY.md` or the T76 locks. It will not say the ratio has been solved. It will not say a miss removes the shadow-price reading from the memo. It will not treat a \(D\) fitted to \(\lambda=1\) as one of the four sources. The formula in §2 is the derivation test (a) asks for. A grid point where the formula is not \(1\) is the complementary-slackness claim failing to produce ratio \(1\), not a new budget.

## 6. Output

One line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test.
