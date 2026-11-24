# T78 preregistration: persistence and the record ratio

*Tuesday 24 November 2026 (UTC). Written and committed before `persistence_checks.py` and before any persistence grid. Branch `forge-record-ratio-persistence`, cut from `forge-record-ratio-dual` at `e7204dd`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`, same commit. A later change to the criteria below is a deviation, logged in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\). Every statement about what the selector does is a model implication, in-model.

## 0. Question

\(J=\kappa I+\kappa_D P_D+w L\) is linear in the ratio \(q=\kappa_D/\kappa\). Minimizing \(J\) over \(q\) cannot select \(q\).

Prior rounds, adopted and not rescored here except where a gate says so:

- Wherever \(P_D>0\), the one-shot minimum over prices on the menus already scored sits at \(q=0\) (T76; the quantum-records lock is `dba140b`).
- Ratio \(1\) flattens the antipodal record cost (T74 Route 5). The minimum over prices ties the endpoints and does not select that ratio.
- Fork PR #9, head `e7204dd`, on the same closed form: at \(\phi=\pi/2\) the loss is flat, every binding upper cap has shadow price \(1\), and at the ledger the subdifferential is \([0,1]\). On the locked slice \(\phi=0\), \(w=1\), the tightening price is \(1-wr^2=0.64\), and the review's grid quotient there is \(0.642\). That quotient is not a tolerance in this lock.

**Forge's intuition, not an axiom and not a result.** \(q\) has to be set by a principle outside \(J\). The candidate is persistence. Repeated selection can act only on records that are still present at the next round. A nat already destroyed is invisible to that selection. A selector that prices only what persists should land on \(q=0\). On this reading, \(q=1\) is an artifact of a symmetry: it shows up where the loss or the record cost is flat in the control.

This lock builds that selector from the existing record and cost objects and scores it. The two adversarial channels below try to make a positive ratio win.

## 1. Prior exposure

- Antipodal closed form, \(\gamma=0\), \(r=0.6\): \(P_D=\tfrac12\big[h((1+r|\cos\theta|)/2)-h((1+r)/2)\big]\), \(I=\tfrac12\big[\ln 2-h((1+r|\cos\theta|)/2)\big]\), \(L=r^2/2-(r^4/4)\cos^2\phi\cos^2\theta\). So \(I+P_D=P_\chi(0)=0.096372378511\), \(P_D(0)=0\), \(P_D(\pi/2)=P_\chi(0)\). \(w_\star=3.209014724815\). \(w_\pi(1)=1/r^2\).
- Phase boundary, `PREREG_FIXED_POINTS.md` §3, for \(\delta=q-1<0\): equator when \(w<|\delta|/r^2\), pointer when \(w>|\delta|w_\star\). Adopted as the reason two ratios can install the same angle. Not a new forecast.
- `second_pinch` in `fixed_point_checks.py`: the second outcome, given the first, is the pure-state channel of the angle between the two axes. On the pairs already scored, the conditional mutual information is below \(10^{-9}\).
- A hand comparison, not a grid, at ANT, \(\gamma=0\), \(\phi=0\), \(w=2\), restoration \(\alpha=1/2\): the \(q=0\) design is the equator and the \(q=1/2\) design is the pointer, and the restoration cost is lower at the pointer. The size of that gap is not a tolerance. The prediction below stays weak dominance. This exposure says the restoration line can miss.

Not evaluated before this lock: the population weights, the ruin weights, the restoration grid, and the partial-dephasing cell.

## 2. Model

### 2.1 Objects

Reuse `record_ratio_reframes_checks` and `second_pinch`. Do not derive a new qubit. \(\kappa=1\). \(r=0.6\). Grid \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\). A design is minimal when its charged cost is within \(10^{-9}\) of the smallest charged cost on that grid. `SEED = 20261124` is set and not drawn from. The map is deterministic.

Ensembles and cells, all of them scored:

| id | ensemble | \(\gamma\) | \(\phi\) | \(w\) |
|---|---|---:|---:|---:|
| A0 | ANT | \(0\) | \(0\) | \(1,2,10\) |
| A4 | ANT | \(0\) | \(\pi/4\) | \(1,2,10\) |
| A2 | ANT | \(0\) | \(\pi/2\) | \(1,2,10\) |
| B0 | BIAS | \(0\) | \(0\) | \(1,2,10\) |
| G | ANT | \(1/2\) | \(0\) | \(1\) |

Ratio menu \(Q=\{0,\ 0.25,\ 0.5,\ 0.64,\ 1,\ 2\}\). The point \(0.64\) is \(1-r^2\), the equator-end price at \(w=1\). It is a menu point, not a fitted ratio.

### 2.2 What persists

A nat persists to the next round when it is still in the classical record or in the stake's loss. The disturbance \(P_D\) is the von Neumann entropy the pinch added. In the base selector those nats are gone, so they are not in the cost selection sees.

Persistent cost of a design, base selector:

\[
F(\theta)=I(\theta)+w L(\theta).
\]

**Fitness** of a policy is \(-F\) at the design that policy installs. **Long-run selected cost** is the persistent cost of the policies still present after the replicator below has run to its support. Lower is better.

### 2.3 What a policy installs

A policy is an element \(q\in Q\). It installs an angle by minimizing its own charged cost, which does price destruction:

\[
J_q(\theta)=I(\theta)+q\,P_D(\theta)+w L(\theta).
\]

Let \(T(q)\) be the set of grid angles within \(10^{-9}\) of the minimum of \(J_q\). The policy is willing to install any angle in \(T(q)\). Selection keeps the one with the lowest score under the cost that selection actually uses. If that score is flat across \(T(q)\) to within \(10^{-9}\), the reported angle is the smallest angle in \(T(q)\). The policy's score is that common value, not a noisy argmin inside the flat set.

Write \(C_0(q)\) for the base score, the minimum of \(F\) on \(T(q)\).

### 2.4 Population

Infinite population. Initial weight uniform on \(Q\). One generation multiplies the weight of \(q\) by \(\exp(\text{fitness}(q))\) and renormalizes. The long-run support is the set of maximizers of fitness. On the base selector that set is

\[
S_0=\{q\in Q: C_0(q)\le \min_{q'} C_0(q')+10^{-9}\}.
\]

Finite check, base cells only. \(T_{\mathrm{gen}}=100000\). Weights \(\propto \exp(-T_{\mathrm{gen}} C_0(q))\), computed after subtracting the minimum \(C_0\) so the exponential does not underflow. The finite support is \(\{q: x_q\ge 0.999\, x_{\max}\}\). On every base cell whose gap from \(S_0\) to the next ratio is at least \(10^{-3}\), the finite support equals \(S_0\). A cell with a smaller gap is counted as `SKIP-GAP` and is not a miss.

### 2.5 Restoration

A fraction \(\alpha\) of the disturbance is persistent again. Selection's cost becomes

\[
F_\alpha(\theta)=I(\theta)+\alpha P_D(\theta)+w L(\theta).
\]

The policy still installs \(T(q)\) from \(J_q\), not from \(F_\alpha\). It does not observe \(\alpha\). Its score \(C_\alpha(q)\) is the minimum of \(F_\alpha\) on \(T(q)\), with the same flat-set rule. \(\alpha=0\) is the base. Scored values: \(\alpha\in\{1/2,\ 1\}\), every cell in §2.1.

On ANT at \(\gamma=0\), \(F_\alpha=(1-\alpha)I+\alpha P_\chi(0)+w L\). That identity is a check on those cells, not a new ensemble. It says the restored nat is the same nat \(P_D\) already names.

### 2.6 Second pinch

The other recovery attempt uses the existing second pinch, not a new channel. ANT, \(\gamma=0\), \(\phi=0\), \(w\in\{1,2\}\). The first angle is the smallest angle in \(T(q)\). The second angle is the best of \(\{0,\pi/4,\pi/2\}\) under `second_pinch`'s conditional mutual information. Write \(I_{\mathrm{back}}(q)\) for that maximum.

The collapsed state is what the second pinch reads. If \(I_{\mathrm{back}}<10^{-6}\), nothing about \(W\) came back, and the persistent cost stays \(C_0\). Selection does not add a zero information term.

### 2.7 Ruin

Destruction raises the chance that the lineage is gone before the next round. This map is an adversary. It is not A2. A2 remains a cap on \(P(\mathrm{ruin})\) and still does not name a disturbance budget.

On a cell, let \(P_{\max}\) be the maximum of \(P_D\) on the \(721\)-grid. If \(P_{\max}<10^{-12}\), every ruin probability is \(0\). Otherwise, at the installed angle (the angle whose \(F\) is the policy's base score; smallest angle if that score is flat on \(T(q)\)):

\[
p(q)=\min\left(1,\ \rho\, P_D(\theta(q))/P_{\max}\right).
\]

Scored values: \(\rho\in\{1/2,\ 1\}\), every cell in §2.1. A policy with \(p=1\) has growth weight \(0\) and is absent. Otherwise

\[
g(q)=(1-p(q))\exp(-C_0(q)).
\]

Fitness is \(\log g\), and \(g=0\) has fitness \(-\infty\). The selected set \(S_\rho\) is the maximizers of \(g\), with the same \(10^{-9}\) relative tolerance on \(\log g\) when \(g>0\): a positive weight is tied when its \(\log g\) is within \(10^{-9}\) of the best. If every \(g\) is \(0\), the cell is `ALL-GONE` and the dominance line misses.

The long-run selected cost on a ruin cell is \(C_0\) of the policies in \(S_\rho\), together with their \(g\).

## 3. Predictions

Margins are fixed. A strict win is an undercut of at least \(10^{-4}\). A gap strictly between \(0\) and \(10^{-4}\) is printed `UNDER-MARGIN` and is not a miss. Flat means a range, over the \(721\)-grid, strictly below \(10^{-9}\).

**G0.** The module is the one already scored.

- Closed form against `functionals` on ANT, \(\gamma=0\), \(\phi\in\{0,\pi/2\}\), every grid angle: max absolute gap in \(I\), \(P_D\), and \(L\) below \(10^{-9}\).
- Loss range at \(\phi=\pi/2\) below \(10^{-12}\). Loss range at \(\phi=0\) above \(0.02\).
- Record-cost range of \(I+P_D\) on ANT, \(\gamma=0\), below \(10^{-9}\). On BIAS, \(\gamma=0\), \(\phi=0\), that range is above \(0.02\).
- At \(\phi=0\), \(w=1\), \(\theta=\pi/2-10^{-3}\), step \(10^{-4}\), the one-sided quotient \(-( \Delta I+w\Delta L)/\Delta P_D\) is within \(0.01\) of \(0.64\).
- At \(\phi=\pi/2\), \(w=1\), \(\theta=1\), step \(10^{-4}\), the central quotient is within \(10^{-6}\) of \(1\).

*Fails if* any bullet misses. Then this grid is not the T73–T77 menu, and the later lines are not read as a test of persistence. Report the bullet. Do not refit \(r\).

**P1.** On every base cell, \(C_0(q)\ge C_0(0)-10^{-9}\) is the elementary grid inequality: \(C_0(0)\) is the minimum of \(F\) on the grid, and every other policy scores \(F\) at some grid angle. The line misses only if some \(q>0\) undercuts \(C_0(0)\) by at least \(10^{-4}\).

*Fails if* any base cell has such an undercut. Report the cell, both angles, both costs, both \(P_D\), and the gap. A miss here means the code is not scoring \(F\) at an element of \(T(q)\), or the tie rule is not the one in §2.3. It is a puzzle for the implementation. It is not, by itself, a reading in which destroyed nats are visible.

**P2.** A positive ratio is selected to the exclusion of \(0\) only where the loss is flat or that ratio's own record cost \(I+q P_D\) is flat. Scored on every base cell, every restoration cell, and every ruin cell.

A cell excludes \(0\) when some \(q>0\) is in the selected set and \(0\) is not. It is a miss when, in addition, the loss range is at least \(10^{-9}\) and that \(q\) has record-cost range at least \(10^{-9}\).

A cell where some \(q>0\) ties \(0\) is not this miss, whether or not the cell is flat. The line counts those ties and how many of them are non-flat. A non-flat tie is a clue for the memo: the ratios share an angle. It is not a miss of P2.

*Fails if* any excluding cell is non-flat for one of its selected positive ratios, in the sense just stated. Report the cell, the channel, the selected set, the offending \(q\), the loss range, and that \(q\)'s record-cost range. A miss means a positive ratio was the long-run support, with \(0\) absent, on a control that is curved in both the loss and that ratio's record cost. On the reading in §0, that is a puzzle: persistence did not need a flat direction to drop \(0\). The clue is whichever channel produced the cell.

**A-restore.** The persistence reading, still Forge's intuition, says \(q=0\) weakly dominates at \(\alpha\in\{1/2,1\}\) as well: no \(q>0\) undercuts \(C_\alpha(0)\) by at least \(10^{-4}\).

*Fails if* any restoration cell has such an undercut. Report every such cell: \(\alpha\), \(w\), \(\phi\), ensemble, \(\gamma\), the selected set, the angles and \(P_D\) of \(q=0\) and of the best \(q>0\), and the gap \(C_\alpha(0)-C_\alpha(q)\). Tag the cell `RESTORE` when the two angles differ. Tag it `OTHER` when the angles agree and the costs still differ. The mechanism the memo is allowed to name, if the tag is `RESTORE`, is this one and no other: \(F_\alpha\) is \(J\) at ratio \(\alpha\), the winning policies are those whose \(T(q)\) meets a minimizer of \(F_\alpha\), and \(q=0\) minimizes \(F\) instead. If the tag is `OTHER`, the memo says the accounting identity did not separate the angles, and it does not invent a second mechanism.

**A-ruin.** The same reading says \(q=0\) is still in the long-run support at \(\rho\in\{1/2,1\}\): no \(q>0\) has \(\log g(q)>\log g(0)+10^{-4}\), and \(g(0)=0\) with some \(g(q)>0\) counts as an infinite gap.

*Fails if* any ruin cell has such a gap, or is `ALL-GONE`. Report every such cell: \(\rho\), the selected set, \(p\) and \(C_0\) and \(g\) for \(q=0\) and for the best \(q>0\), the angles, and both \(P_D\). Tag `RUIN-REMOVE` when \(p(0)>p(q)\). Tag `OTHER` otherwise. The mechanism the memo is allowed to name, if the tag is `RUIN-REMOVE`, is this one: the lineage that installs the more disturbed angle is removed more often, so selection never banks its one-shot persistent cost. If the tag is `OTHER`, the memo says the ruin probabilities did not rank the designs that way, and it names the printed \(p\) values instead of a removal story.

**A-repin.** On the four second-pinch cells, \(I_{\mathrm{back}}(q)<10^{-6}\) for every \(q\in Q\), and no \(q>0\) undercuts \(C_0(0)\) by at least \(10^{-4}\).

*Fails if* either part misses. An information miss means the second pinch still carries a record of \(W\), so the nat was not invisible. Tag that cell `REPIN` and report the angle pair and \(I_{\mathrm{back}}\). A cost miss with \(I_{\mathrm{back}}<10^{-6}\) is tagged `OTHER`.

**G-dyn.** The finite support equals \(S_0\) on every base cell that is not `SKIP-GAP`.

*Fails if* a qualified cell disagrees. Report the cell and both sets. A miss means the finite replicator is not the support defined in §2.4. It is not a second ratio.

## 4. What a miss points to

P1 miss: the score is not \(F\) on \(T(q)\). Next check is the tie set, not a new price.

P2 miss: some channel put a positive ratio in the support, and \(0\) out, on a curved control. The channel tag is the clue. It does not license a new term in \(J\).

A-restore miss with tag `RESTORE`: charging the restored fraction pays, because that fraction is persistent. The ratio that wins is a ratio whose installed angle minimizes \(F_\alpha\), not a universal \(1\), unless the printed set is only \(\{1\}\).

A-ruin miss with tag `RUIN-REMOVE`: charging destruction pays because a lineage that does not survive is not there to be selected. The price of remaining is not a disturbance budget taken from A2.

A-repin miss with tag `REPIN`: the collapsed state was still informative. The base sentence that a destroyed nat is invisible is false for that pair.

A pass of P1 together with a miss of A-restore or A-ruin is the split this lock is built to detect. The memo keeps both. It does not average them into one ratio.

## 5. What this run will not say

It will not edit `THEORY.md` or the T76 and T77 locks. It will not say that a value of the ratio has been obtained as a final answer. It will not say that a miss removes persistence from further work. It will not treat a win for \(q>0\) as a derivation of general relativity, quantum mechanics, holography, or gravity. It will not call the ruin map a consequence of A2. It will not add a cell, a ratio, a stake, or a margin after seeing the output. A hand-chosen \(\alpha\) or \(\rho\) inside the lists above is an adversary, not a measured recovery rate and not a measured ruin rate.

## 6. Output

The script prints one line per named check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test. `PREREG.md` is not read for numbers. `RUN_LOG.md` records every deviation and, if there is none, says so. The memo uses the labels PROVED (in-model), NUMERICAL, and PUZZLE.
