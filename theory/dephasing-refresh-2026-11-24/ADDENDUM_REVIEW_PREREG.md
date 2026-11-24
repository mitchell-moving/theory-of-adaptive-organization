# ADDENDUM PREREG: review fold-in for the refresh cost

*Tuesday 24 November 2026 (UTC). Own file. `PREREG.md` and `ADDENDUM_PREREG.md` are not edited. Commit this file before any script that scores the predictions below. Branch `forge-dephasing-refresh`. `THEORY.md` and `CORE.md` are not edited. A later change to a prediction or a bar is a deviation, appended in `DEVIATIONS.md`. Open-work id **T84b**. Self-check. Results are labeled observed in-model until an independent review clears them.*

Can it fail: the squared-Hamming refresh can keep exponent \(1/2\) and a critical \(\Pi\) near 4, the two stake thresholds at \(\gamma T=1\) can disagree, or an alternative in the review's table can leave the locked sign in place.

Cheapest way to fail it: the locked linear time average, the squared-Hamming time average, and the five nearby one-shot costs, each at one cell. No bath Hilbert space and no Monte Carlo.

## Why this approach

The independent review of fork PR #22 (comment `7144884461`; write-up `theory/reviews/DEPHASING_CROSSOVER_REVIEW_2026-11-24.md` on `forge-dephasing-review` at `4513933`, PR #24) says T84's signs are the identity \(J_P-J_H=h(\varepsilon)-w\varepsilon\). A script that subtracts the closed form from itself cannot miss. This file names the refresh cost, labels that class of identity as a consistency check, and locks an alternative cost under which the refresh claims \(\Pi_c\to 4\) and exponent \(1/2\) fail. The null says which part restates the binary rate-distortion comparison and which part restates an elementary refresh balance.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The record price is a cost.

## 1. Cost form, and what is only a consistency check

**Locked refresh cost.** Class RF, accountings A and B of `PREREG.md`: time average of the Hamming loss \(\varepsilon(t)=(1-e^{-\gamma t})/2\), heat \(A\) per refresh. Inside this cost, \(s_*(u)=2/[1-(1+u)e^{-u}]\), \(\Pi_c\to 4\), and the short-period elasticity \(\to 1/2\) are identities. They are consistency checks. A pass does not count as a test that could have missed.

**Locked one-shot cost, for the null only.** T84's \(J_H=\kappa\chi(e^{-\gamma\tau})+w\varepsilon\) and \(J_P=\kappa\ln 2\) (`theory/dephasing-crossover-2026-11-24/PREREG.md:131-134`). The sign \(J_P-J_H=h(\varepsilon)-w\varepsilon\) is an identity of that cost. Consistency check. T84 did not lock a stake exponent \(w^{1/2}\): `theory/dephasing-crossover-2026-11-24/PREREG.md` contains neither `w^{1/2}` nor `T_hold`.

## 2. Null: what restates a known comparison

**Rate distortion.** With \(R(D)=\ln 2-h(D)\) for a binary source under Hamming loss, \(D\in[0,1/2]\), the pointer is cheaper exactly when \(\kappa R(0)\) beats \(\kappa R(\varepsilon)+w\varepsilon\), and \(R(\varepsilon)=\chi(e^{-\gamma\tau})\) once \(\varepsilon=(1-e^{-\gamma\tau})/2\). That is the endpoint comparison. Pure dephasing only supplies \(\varepsilon\). It is not a fault-tolerance threshold and not a refresh schedule. Shannon's fidelity-criterion paper, Crossref HTTP 200 on 24 November 2026, doi `10.1109/9780470544242.ch21` (collected volume, issued 2009; no abstract, so no sentence is quoted). A pass of \(w/\kappa>h(\varepsilon)/\varepsilon\) is this restatement. It is not the refresh result.

**Elementary refresh balance.** End-of-interval loss \(\approx\gamma T/2\) with a reset \(A\) gives \(T^*=\sqrt{2A/(w\gamma)}\) and \(J^*=\sqrt{2A\,w\,\gamma}\). The locked time average \(\approx\gamma T/4\) gives \(T^*=2\sqrt{A/(w\gamma)}\) and \(J^*=\sqrt{A\,w\,\gamma}\). Both are proportional to \(w^{1/2}\). That exponent restates the balance of a reset cost against a loss linear in the interval. The prefactor is the part that depends on which loss is averaged. T84's scored script does not score either balance.

## 3. Product, floor, and the printed elasticity

\(t(\gamma,T)=h(\varepsilon)/(\kappa\varepsilon)\) with \(\kappa=1\) depends on \(\gamma\) and \(T\) only through \(x=\gamma T\). Locked: \(t(2,1/2)=t(1/2,2)\), the common value equals \(t(1)\), and \(t(0.01)>t(1)>2\ln 2\). The floor \(2\ln 2\) does not move with \(\gamma\) or with \(T\) separately. In bits that floor is 2.

At the printed cell \(\gamma\tau=1\), \(w=2\), \(\kappa=1\), the stake elasticity of the affine cost is \(e=w\varepsilon/J_H\). Locked: \(|e-0.901222|\le 10^{-5}\) and \(|e-1/2|\ge 0.3\). The first clause checks the arithmetic of \(w\partial J_H/\partial w=w\varepsilon\). The second says this cell is not a square-root elasticity. T84 locked no \(w^{1/2}\).

## 4. Alternative under which the refresh claims fail

**Squared Hamming, on the refresh rate.** Replace the loss by \(\varepsilon(t)^2\) and keep the time average and the heat \(A\). Short time: the average is \((\gamma\tau)^2/12\), the stationarity condition is \(s=6/u^3\) with \(s=w/(\gamma A)\), the loss share is \(1/3\), and the critical value of \(\Pi=w\gamma T^2/A\) at \(\tau=T\) is \(6/(\gamma T)\).

Locked bars: the short-time share equals \(1/3\) within \(10^{-12}\). At \(\gamma T=0.01\), that critical \(\Pi\) equals 600 within \(10^{-6}\), and it exceeds 100, so it is not the linear-Hamming limit 4. The statement "exponent \(1/2\)" fails here (the share is \(1/3\)). The statement "\(\Pi_c\to 4\)" fails here.

If this alternative still has share \(1/2\) and critical \(\Pi<10\), the bars do not separate the costs and the headline is `CONSISTENCY_CHECK`.

**One-shot alternatives, the review's table, at \(\gamma\tau=1\), \(\kappa=1\).** Each is predicted to flip the locked sign. Tolerances \(10^{-4}\) on the printed magnitudes.

- Carrier entropy: \(J_H=h(\varepsilon)+w\varepsilon\), \(J_P=0\). At \(w=1\), \(J_H>0.9\), so the pointer is cheaper. At \(\gamma\tau=0\), \(J_H=0\), which misses \(\ln 2\) by more than \(0.5\).
- Linear leak: \(J_H=(1-e^{-\gamma\tau})+w\varepsilon\), \(J_P=\ln 2\). The threshold is below \(0.2\), so stake \(1\) prefers the pointer.
- Squared Hamming: \(L=\varepsilon^2\), rent unchanged. At \(w=2\), \(J_H<\ln 2\), so the phase hold is cheaper. The fair-coin floor is \(4\ln 2\), and \(|4\ln 2-2\ln 2|>1\).
- Stake-dependent rent: coefficient \((1+w)\) on \(I\). At \(w=2\), \(J_P-J_H>1\), so the phase hold is cheaper.
- Linear coherence, \(q=0\): rent \(1-r\) instead of \(\chi\), and \(J_Z=w/2\). At \(w=0.5\) the threshold is above \(3\), so the pinch is cheaper. The locked P2 threshold at this cell is below \(0.4\).

## 5. Headline

`OBSERVED_ALT_FLIPS` if the squared-Hamming refresh fails both \(1/2\) and \(\Pi\to 4\), the product identity holds, the printed elasticity is near \(0.901222\) and at least \(0.3\) from \(1/2\), and all five one-shot alternatives flip. `CONSISTENCY_CHECK` if the squared-Hamming refresh does not flip those two claims. Any other miss is `PUZZLE`. The script computes the label from the booleans and does not print `OBSERVED_ALT_FLIPS` after a miss. The label is observed in-model either way. The parent identities in §1 stay consistency checks even when this headline passes.
