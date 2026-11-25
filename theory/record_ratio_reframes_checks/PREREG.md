# T76 preregistration: three reframes of the record-price ratio

*Tuesday 24 November 2026 (UTC). Written and committed before any T76 script and before any T76 grid. Branch `forge-record-ratio-reframes`, cut from `forge-record-ratio-consistency` at `f795666`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. The lock file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. The qubit, the dephasing channel, and the two record functionals are inputs from draft #252. A miss is a puzzle. The record price is a cost.

## 0. Question

Does a known sharp result in a distant field, read on

\[
J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L,
\]

force \(\kappa_D/\kappa\), or force the ratio to stay free? Three routes. Each has a claim that a grid can miss. Routes that only rename T75 are not scored.

- **Route K.** Kelly's doubling rate, and Sharma's quantum extension of it. Does the doubling-rate gain split into an \(I\) part and a \(P_D\) part with one fixed relative weight?
- **Route G.** Is the ratio a gauge of selected designs and of minimized costs on a named class, and where does that gauge stop?
- **Route C.** Which observation, inside the model, measures the ratio the way a load measures a spring constant, and which observation cannot?

Dropped, and not scored. Sequential composition by the chain rule and by telescoping entropy leaves every ratio a fixed point. The one-step map that sends every ratio to an effective \(0\) is T75 Route A (pointer measurement plus a classical garbling) rewritten as a flow. Rate-distortion's Lagrange multiplier is an operating-point slope; on the antipodal ledger that slope is the identity \(dI=-dP_D\), which is Route G's perfect-substitute line. Neither adds a check that those two routes do not already state.

## 1. Prior exposure (disclosed)

Already published, and not a T76 result:

- Complete-dephasing antipodal closed form, `PREREG.md:64-72` at `e584d8b`. \(P_D+P_\chi\) independent of \(\theta\). \(P_\chi(0)=0.096372378511\) at \(r=0.6\). Pure mutual information first has a unique \(\theta=0\) minimizer at \(w_\star=3.209014724815\) when \(\phi=0\).
- T74 at `1fb7b5b`: flatness of the antipodal record cost holds exactly at ratio \(1\). The minimum over prices ties the endpoints and does not select that ratio.
- T75 at `f795666`: Routes A and B point at the endpoint \(\kappa_D=0\) under strengthenings that are not axioms. The ledger identity does not force ratio \(1\).
- Partial dephasing on the same four-point ensemble: the stored \(P_D\) minimizer at \(\gamma=1/2\), \(\phi=\pi/4\), \(w=100\) is the cell \(0.449422\), continuous value \(0.448575\) (`MEMO.md` on `e584d8b`). At \(w=0\) that minimizer is \(\theta=0\). The review note that \(w=100\) is a small shift of the loss minimum is used only as a reason to expect a gap. It is not a tolerance.
- A hand evaluation of the biased endpoints in §3, not a grid and not a tolerance, puts \(H(M)-S(\bar\rho)\) near seven hundredths of a nat at \(\theta=\pi/2\). The locked bar is \(0.02\).

Not evaluated before this lock: the biased grid, the \((\alpha,\beta)\) net, the two-stake inversion, and the partial-dephasing comparison of ratio \(1\) with ratio \(100\) at \(w=1\). Draft #252's `PREREG_2.md` (unscored, two-state, \(\gamma=1/2\), label `SPLIT`) is not this file and is not scored.

## 2. What is adopted as known, and what is checked

**KNOWN, Kelly 1956.** Crossref on 24 November 2026, DOI `10.1002/j.1538-7305.1956.tb03809.x`. J. L. Kelly, Jr., "A New Interpretation of Information Rate," *Bell System Technical Journal* 35 (1956), 917–926. The publisher abstract states that, at odds consistent with the probabilities, the maximum exponential rate of growth of capital equals the rate of transmission of information over the channel, and that the result is generalized to arbitrary odds. The page proof was not re-read. Adopting the abstract's equality is **KNOWN**. It is not a derivation of \(\kappa_D/\kappa\).

**KNOWN, Sharma.** Naresh Sharma, "A gambling interpretation of some quantum information-theoretic quantities," arXiv `1306.3791v2` (17 July 2013). The text was read. No journal DOI was returned for that title; none is printed. Section VI.5, fair odds \(o_i=1/p_i\), posterior bets: the doubling rate equals the mutual information of the input and the measurement outcome (his (53)), and the Holevo quantity (his (55)) is an upper bound, not the rate. Section VI.3, (47)–(48): under uniform fair odds and eigenbasis measurements, the gap between his two helper protocols equals quantum discord. That gap is not \(P_D\). Adopting these equalities is **KNOWN**.

The in-model checks do not re-derive those theorems. They ask whether \(I\) and \(P_D\), as defined on these ensembles, realize those equalities at one fixed weight.

## 3. Model (fixed)

One qubit. Pure dephasing multiplies the Bloch \(x\) and \(y\) components by \(\gamma\) and leaves \(z\). Radius \(r=0.6\). Projective record \(n(\theta)=(\sin\theta,\,0,\,\cos\theta)\), \(\theta\in[0,\pi/2]\). Outcome \(M\in\{+1,-1\}\), \(P(M=+1\mid W)=(1+n\cdot v_W)/2\) on the post-dephasing Bloch vector \(v_W\).

Von Neumann entropy of a qubit is the binary entropy, in nats, of \((1+b)/2\), with \(b\) the Bloch length, and \(h(0)=h(1)=0\). For this rank-1 pinch, \(S(\Phi_\theta(\rho))=h(P(M=+1\mid\rho))\) and

\[
P_D=\mathbb{E}[S(\Phi_\theta(\rho))-S(\rho)],\qquad I(W;M)=H(M)-\mathbb{E}[S(\Phi_\theta(\rho))].
\]

The Holevo quantity of the ensemble does not depend on \(\theta\):

\[
\chi=S(\bar\rho)-\mathbb{E}[S(\rho)].
\]

Stake observable \(A(\phi)=\sin\phi\,\sigma_x+\cos\phi\,\sigma_z\). Target \(y_W=r\,n_A\cdot u_W\) on the pre-dephasing unit vector \(u_W\). Action \(\hat a(M)=\mathbb{E}[y\mid M]\). Loss \(L=\mathbb{E}[(y-\hat a(M))^2]\). Cost \(J=\kappa I+\kappa_D P_D+w L\). Ruin is slack. Coefficients nonnegative.

**Ensembles.**

- **ANT.** Four labels, equal weight \(1/4\), pre-dephasing Bloch vectors \(\pm r\hat z\), \(\pm r\hat x\). The T75 ensemble.
- **BIAS.** Two labels, weights \(0.8\) and \(0.2\), pre-dephasing Bloch vectors \(+r\hat z\) and \(-r\hat z\). Not an antipodal pair of weights. \(\gamma=0\) only. \(\phi=0\) only. This is not class PB2.

**Grid.** \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\), \(j=0,\ldots,720\). A point is minimal when its cost is within \(10^{-9}\) of the smallest cost. "Unique" means one grid point. If several tie, the reported \(\theta\) is the smallest, and the tie is flagged. No random numbers. `SEED = 20261124` is set and not drawn from.

**Derivatives** used in Route C are central differences of the smooth functions at the minimizing grid \(\theta\), step \(10^{-5}\) radians. A difference that would read past the endpoints uses the one-sided step of the same size. The determinant of a \(2\times 2\) system is singular when its absolute value is below \(10^{-8}\).

## 4. Route K — predictions

**K1 (ANT, \(\gamma=0\)).** On the grid, \(\max|I+P_D-\chi|<10^{-9}\). The least-squares fit of \(\alpha I+\beta P_D\) to \(I\), minimizing the sum of squares with no intercept, returns \(|\alpha-1|<10^{-8}\), \(|\beta|<10^{-8}\), and max residual \(<10^{-9}\). The same fit to the constant \(\chi\) returns \(|\alpha-1|<10^{-8}\), \(|\beta-1|<10^{-8}\), and max residual \(<10^{-9}\).

*Fails if* any of those six inequalities fails. A failure here, after gate G0 has passed, withdraws the claim that the antipodal knife-edge writes the Holevo bound as \(I+P_D\) and the doubling rate as \(I\).

**K2 (BIAS, \(\gamma=0\)).** \(\max|I+P_D-\chi|>0.02\). The Gram determinant \(\|I\|^2\|P_D\|^2-(I\cdot P_D)^2\), vectors over the grid, exceeds \(10^{-6}\). The least-squares fit of \(\alpha I+\beta P_D\) to \(I\) returns \(|\alpha-1|<10^{-8}\) and \(|\beta|<10^{-8}\). Let \(f(\alpha,\beta)=\max_\theta|\alpha I+\beta P_D-\chi|\). Then \(f>0.005\) at the least-squares fit of \(\chi\), and at every pair on the net \(\alpha,\beta\in\{-2,-1.95,\ldots,4\}\).

*Fails if* the max ledger gap is \(\le 0.02\), or the Gram determinant is \(\le 10^{-6}\), or any evaluated \(f\le 0.005\), or the fit to \(I\) misses \((1,0)\) at the stated tolerance. A net miss means a fixed weight reproduces the Holevo bound on this ensemble to \(0.005\) nat. The doubling-rate split is then not uniquely \((1,0)\) against that bound. Next, if the net is the only miss and the least-squares \(f\) stays above \(0.005\): refine the net in a new preregistration, not in this file. If the least-squares \(f\) itself is \(\le 0.005\): the bound is an affine image of \((I,P_D)\) here, and the route stops with that pair reported, not with ratio \(1\) declared.

## 5. Route G — predictions

**G1 (corner gauge).** ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\), ratios \(\kappa_D/\kappa\in\{1,2,10\}\), stakes \(w\in\{0.1,1,10\}\). Each of the nine cells has unique minimizer \(\theta=0\). At each stake the three minimized costs differ by \(<10^{-9}\).

*Fails if* any cell has a minimizer at \(\theta\ge\) one grid step, or a tie, or the three costs at one stake differ by \(\ge 10^{-9}\).

**G2 (indifference).** Same ensemble and \(\phi\), \(w=0\), \(\kappa=1\). At ratio \(1\) the cost range on the grid is \(<10^{-9}\). At ratio \(2\) the unique minimizer is \(\theta=0\) and \(J(\pi/2)-J(0)>0.01\).

*Fails if* the ratio-\(1\) range is \(\ge 10^{-9}\), or ratio \(2\) is not uniquely \(\theta=0\), or the endpoint gap is \(\le 0.01\).

**G3 (below \(1\)).** ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\), \(\kappa_D=0\). At \(w=1\), \(\theta^\star>0.2\). At \(w=10\), the unique minimizer is \(\theta=0\).

*Fails if* \(w=1\) has \(\theta^\star\le 0.2\), or \(w=10\) is not uniquely \(\theta=0\). This cell is on the published side of \(w_\star\). It checks the gauge boundary against that closed form. It is not a new forecast.

**G4 (where ratios above \(1\) separate).** ANT, \(\gamma=1/2\), \(\phi=\pi/4\), \(\kappa=1\), \(w=1\). Let \(\theta_1\) be the minimizer at \(\kappa_D=1\) and \(\theta_{100}\) the minimizer at \(\kappa_D=100\). \(|\theta_1-\theta_{100}|\ge 0.2\).

*Fails if* the absolute gap is \(<0.2\). A tie spanning \(\ge 0.2\) is a failure of uniqueness and is reported as such, not as a gap. If this fails, ratios \(\ge 1\) may still share a design at this stake, and the gauge has not been shown to stop here. Next: the same comparison at \(w\in\{0.1,10\}\) in a new preregistration. Do not move the bar.

**G5 (shift).** ANT, \(\gamma=0\), \(\phi=0\). Price vectors \((1,0.5)\) and \((1.5,1.0)\) have the same difference \(\kappa_D-\kappa=-0.5\) and different ratios. For every \(w\in\{0,0.5,1,2,4,10\}\), their minimizers differ by at most one grid step, and their minimized costs differ by \(P_\chi(0)\) within \(10^{-9}\) (the added coefficient times the constant ledger).

*Fails if* any stake separates the minimizers by two or more grid steps, or the cost gap misses \(P_\chi(0)\) by \(\ge 10^{-9}\).

## 6. Route C — predictions

The experimenter knows the ensemble, \(r\), \(\phi\), and the stake \(w\). The experimenter records the minimizing \(\theta\). The numerical value of \(J\) is not an input to the inversion below, except in the sentence that says so.

**C1 (ANT does not measure the ratio).** Plant \((\kappa,\kappa_D)=(1,0.5)\), \(\gamma=0\), \(\phi=0\), stakes \(\{0.5,1,2,4,8\}\). At least one stake has \(\theta^\star\in[0.05,\pi/2-0.05]\). Every such stake recovers \(\delta=\kappa_D-\kappa\) by \(\delta_{\mathrm{hat}}=-w L'/P_D'\) within absolute error \(5\times 10^{-3}\). Every pair of such stakes has \(|\det|<10^{-8}\) in the system with rows \((I',P_D')\). The solver returns no unique \((\kappa,\kappa_D)\).

*Fails if* no stake is interior, or any interior stake misses \(\delta=-0.5\) by \(\ge 5\times 10^{-3}\), or any interior pair has \(|\det|\ge 10^{-8}\). No interior stake means this stake list never opened the tradeoff. Next: add \(w\in\{0.2,0.3\}\) in a new preregistration.

**C2 (BIAS measures both coefficients).** Same plant, \(\gamma=0\), \(\phi=0\), stakes \(\{0.05,0.1,0.2,0.5,1,2,5\}\). At least two stakes are interior, and the interior pair with the largest \(|\theta|\) gap differs by \(\ge 0.05\) rad. Cramer's rule on that pair, rows \((I'(\theta_i),P_D'(\theta_i))\), right-hand side \((-w_i L'(\theta_i))\), recovers \(|\hat\kappa-1|<0.02\) and \(|\hat\kappa_D-0.5|<0.02\).

*Fails if* fewer than two interior stakes, or the best gap is \(<0.05\), or the determinant is singular under the \(10^{-8}\) rule, or either recovered coefficient misses by \(\ge 0.02\). A singular or empty interior is a puzzle: this load list did not pin the ratio. Next: a denser stake list in a new preregistration, predictions in this file unchanged. A recovery outside \(0.02\) with a nonsingular pair means the first-order reading does not invert on this grid. Report the residuals. Do not adjust the plant.

**C3 (the gauge stops on BIAS at zero stake).** \(w=0\), \(\kappa=1\). Ratio \(0\) (\(\kappa_D=0\)): \(\theta^\star>\pi/2-0.02\). Ratio \(1\) (\(\kappa_D=1\)): \(\theta^\star<0.02\).

*Fails if* either angle misses its end by the stated margin, or either cell ties. The argument that is being checked, not a grid result: at \(\gamma=0\) both states are \(z\)-diagonal, so \(P(M=+1)=1/2+0.3 r\cos\theta\), \(H(M)\) is minimized only at \(\theta=0\), and \(I(W;M)=0\) only at \(\theta=\pi/2\). Ratio \(1\) prices \(H(M)\) up to a constant. Ratio \(0\) prices \(I\).

## 7. Gates (code correctness)

A failing gate is a code bug. Fix the code, log the fix in `DEVIATIONS.md`, do not edit this file, do not change a prediction.

- **G0.** ANT, \(\gamma=0\), \(r=0.6\). The Bloch evaluator matches the closed form of \(P_D\), \(I\), and \(L\) at \(\theta\in\{0,0.3,\pi/4,\pi/2\}\) and \(\phi\in\{0,\pi/4,\pi/2\}\), absolute error \(<10^{-10}\).
- **G0b.** ANT, \(\gamma\in\{0,1/2\}\), every grid \(\theta\): \(|P(M=+1)-1/2|<10^{-12}\).

## 8. What this run will not say

It will not edit `THEORY.md`. It will not say that the ratio has been solved, and it will not say that a miss removes a route from further work. It will not score `PREREG_2.md`. It will not treat Kelly's equality, or Sharma's bound, as a sentence of A1–A8. A weight that appears only by adopting one of those theorems is marked **KNOWN**.

## 9. Output

The script prints one line per check, `PASS` or `FAIL`, then `FAILS` and a count, then `ALL T76 CHECKS PASS` only when the count is \(0\). Stdout is stored and byte-compared by the test.
