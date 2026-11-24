# T79 preregistration: two levels, two costs, and the record ratio

*Tuesday 24 November 2026 (UTC). Written and committed before `bicausal_checks.py` and before any scored grid. Branch `forge-record-ratio-bicausal`, cut from `forge-record-ratio-persistence` at `5660367007438f6cfa68c4f93cc38a140bebbe97`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`, same commit. A later change to the criteria below is a deviation, logged in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\). Every statement about what an equilibrium does is a model implication, in-model.

This question is a hypothesis from Chad, directed by the GTAO lead, and labeled as such. It is not an axiom and not a result.

## Why this approach

\(J=\kappa I+q\kappa P_D+w L\) is linear in \(q=\kappa_D/\kappa\), so a single minimizer of \(J\) cannot select \(q\). T78 put a return channel in by hand. Here each level minimizes its own cost, and the share that comes back is the parent's choice.

## Can it fail

Can it fail: yes. A pure Nash can be missing, or the angle it installs can be rationalized by a wide set of ratios.

Cheapest way to fail: the parent's return leaves the child on a corner of the angle grid, so the tie rule and the menu, not a unique price, name \(q\).

## 0. Question

There is no separate environment. The next level up is the only parent. Two levels each minimize their own cost under the record-cost objects already in the repo. The coupling runs both ways:

- the child's kept record and its destruction change the parent's information and the parent's cost;
- the parent's return share, how much of the child's destruction it sends back, changes the child's cost.

The return share is the parent's optimum. It is not an input.

**Q1.** Is there a joint equilibrium, both levels optimizing at once, neither leading, that pins the child's ratio with no outside data?

**Q2.** Is that ratio unique, and where does it sit in \([0,1]\) or beyond?

**Q3.** Does that ratio differ from the one-way equilibrium in which the parent leads?

This is not T69. T69 (`theory/layer-fixed-point-2026-11-23/PREREG.md:1` and `:5` on `forge-layer-fixed-point` at `dfb530d`) asked whether a nested-layer map has a renormalization fixed point that yields one dimensionless number. Its locked outcome did not yield that number. This lock asks whether the coupling pins the child's price ratio. It does not rerun that map.

### 0.1 What T78 assumed

T78 (`theory/record-ratio-persistence-2026-11-24/PREREG.md:84-93` and `:102-110`, memo `:13-17`) found three things, adopted here and not rescored:

- On the base selector, \(q=0\) weakly dominates while destruction stays gone.
- A positive ratio appears in the support only when a return channel is added: restoration, or removal of a lineage.
- The restoration score is the identity \(F_\alpha=J\) at ratio \(\alpha\). The flat-loss survivor \(q=2\) depends on the tie rule and on the menu. The removal score depends on dividing by \(P_{\max}\).

In T78 the return channel was assumed. The fraction \(\alpha\) and the removal factor \(\rho\) were adversary inputs. They were not the optimum of a parent that pays its own cost. This lock does not assume them.

## 1. Citations read before this lock

Read on this branch before any number below was used as a target. A later match to one of these targets is evidence only if the target number is not a parameter of the model in §2. A match that needs a coefficient set to the target does not count.

**Boundary.** `theory/BOUNDARY_SUFFICIENCY_2026-11-22.md:13` states that the decision loss follows the blanket. Proposition BS-loss (`:45-51`) says an exterior mean-square loss is a function of the blanket posterior alone. The interior without the blanket is not enough (`:13`, variances \(3/5\) and \(1/2\)). The strict sentence that the heat-minimizing channel sits on the blanket alone does not hold (`:17`).

*Reproduction target, if the equilibrium shares that cause.* Hiding the child's disturbance from the parent, and leaving the kept record and the loss, does not change the parent's return. Scored in §5. The numbers \(2/5\) and \(1/2\) from that note are not parameters here.

**Swarm.** `theory/SWARM_RULE_2026-11-23.md:40-46`. Parts of a whole each minimize their own cost. Alignment (`:46`): the part's choice equals the whole's optimum if and only if the part pays the stake share \(s_i=w_i/W\).

*Reproduction target, if the equilibrium shares that cause.* The parent's equilibrium return equals \(w_c/(w_c+w_p)\) on the three stake pairs in §5. That share is computed from the stakes. It is not written into either cost.

**Fractal.** `theory/FRACTAL_WORLD_2026-11-22.md:13-15`. On the locked graphs the minimum cost tracks the sites the decision names. It does not track the Hausdorff dimension or the spectral dimension. A decision that names only the outer boundary pays for those sites (`:76-78`).

*Reproduction target, if the equilibrium shares that cause.* Doubling the named record \((I,P_D,L)\), as two independent copies of the same design, leaves the equilibrium ratio unchanged and doubles both costs. An unpriced bulk factor leaves the ratio unchanged. Because that factor never enters the cost, a match on the bulk is the cost equation itself and is not extra evidence.

**Holographic, in-model and not a derivation.** `theory/HOLOGRAPHIC_2026-11-22.md:13-17`. For bulk per-site error the cost is not an encoding of a bulk on a boundary. Proposition H-iface (`:40-44`): the learning rate depends on the memory only through the conditional of the world given the memory. An added coordinate that leaves that conditional unchanged does not enter the floor.

*Reproduction target, if the equilibrium shares that cause.* The ratio is unchanged when a bulk coordinate is added that leaves \((I,P_D,L)\) unchanged. Landing on \(1/4\), or on a cut-versus-volume ratio, is not this target. If a printed ratio equals \(0.25\) within the tolerance below, the memo records the coincidence and does not call it holography.

## 2. Model

### 2.1 Objects

Reuse `functionals` in `theory/record_ratio_reframes_checks/record_ratio_reframes_checks.py`. Do not derive a new qubit. Headline ensemble ANT, \(\gamma=0\), \(\phi=0\), \(r=0.6\), the module's \(R\). \(\kappa_c=1\) unless a scale cell says otherwise.

Angle grid: \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\), \(j=0,\ldots,720\).

Return grid: \(\alpha_k=k/50\) for \(k=0,\ldots,50\). Comparisons of \(\alpha\) use the integer \(k\).

Report grid for the ratio: \(q_i=i/50\) for \(i=0,\ldots,100\), so \(q\in[0,2]\). Prices below \(0\) are outside this grid. A set that contains both \(q=1.98\) and \(q=2\) is marked `UNBOUNDED_HIGH` and is not a pin. The upper end is the menu, not a measured bound.

`SEED = 20261124` is set and not drawn from. The asymmetric starts in §2.7 are listed. The seed does not choose them.

Tie tolerance on a cost: \(10^{-9}\). Two grid values of \(\alpha\) or of \(q\) count as separated when they differ by more than one grid step, \(0.02\).

### 2.2 Timescale

\(\tau\) is the parent's return delay divided by the child's persistence time. The child's persistence time is the unit. Locked grid:

\[
\tau\in\{0,\ 0.25,\ 0.5,\ 1,\ 2,\ 4\}.
\]

A return that arrives after the child is gone counts as \(0\) for the child and not for the lineage. Arrival at \(\tau=1\), the end of the persistence window, counts as gone for the child.

Child accounting:

\[
\rho_c(\tau)=\max(1-\tau,\ 0).
\]

Lineage accounting:

\[
\rho_\ell(\tau)=1
\]

for every locked \(\tau\). Both accountings are scored. They are not averaged.

Effective return inside the child's cost: \(\beta=\alpha\,\rho\).

### 2.3 Pricing choices

These are choices. They are not measurements and not findings.

**Child.** The child keeps a classical record and pays \(\kappa_c\) per nat of \(I\). Destruction that stays destroyed is gone, so the child does not price it. Destruction the parent sends back in time is persistent again, and the child pays \(\kappa_c\) per nat of that returned piece. The child pays its own stake on the loss. With \(\beta=\alpha\rho\),

\[
C_c(\theta;\beta)=\kappa_c\,I(\theta)+\kappa_c\,\beta\,P_D(\theta)+w_c\,L(\theta).
\]

This is \(J\) at ratio \(\beta\). That identity is the T78 restoration identity. It is this pricing, not a result about the equilibrium. The reported ratio is the rationalizing set of the installed angle (§2.6), which is a singleton only when that angle is not shared by an interval of ratios.

**Parent.** The parent has no separate world. It holds the child's kept record at \(\kappa_p\) per nat. It pays a channel cost \(\kappa_p\,u(\alpha)\,P_D(\theta)\) to run a return of reliability \(\alpha\). It prices the residual information loss, the share \(1-\alpha\) of the destruction it does not send back, at \(\kappa_{D,p}\) per nat. It pays its own stake on the child's loss. The loss term does not depend on \(\alpha\) directly. The parent feels \(\alpha\) through the channel, through the residual loss of information, and, when it leads, through the angle the child then installs.

\[
u(\alpha)=1-\frac{h\!\left((1-\alpha)/2\right)}{\ln 2},
\]

where \(h\) is the binary entropy in nats, \(h(0)=h(1)=0\), and \(h(1/2)=\ln 2\). So \(u(0)=0\), \(u(1)=1\), and \(u\) is convex on \([0,1]\) because its derivative

\[
u'(\alpha)=\frac{1}{2\ln 2}\ln\frac{1-c}{c},\qquad c=(1-\alpha)/2,
\]

increases from \(0\) at \(\alpha=0\) to \(+\infty\) as \(\alpha\to 1\).

\[
J_p(\alpha;\theta)=\kappa_p\,I(\theta)+\kappa_p\,u(\alpha)\,P_D(\theta)+\kappa_{D,p}\,(1-\alpha)\,P_D(\theta)+w_p\,L(\theta).
\]

When \(P_D(\theta)>0\) and \(\kappa_{D,p}>0\), the unique minimizer of the continuous function of \(\alpha\) is the root of \(u'(\alpha)=\kappa_{D,p}/\kappa_p\),

\[
\alpha_\star=1-\frac{2}{1+4^{\kappa_{D,p}/\kappa_p}},
\]

and the second derivative \(\kappa_p P_D u''\) is positive there. When \(\kappa_{D,p}=0\) and \(P_D>0\), the derivative in \(\alpha\) is nonnegative and the unique minimizer is \(\alpha=0\). When \(P_D<10^{-12}\), every \(\alpha\) ties.

The factor in \(\alpha_\star\) is the binary-entropy derivative. It is not set to a stake share.

### 2.4 Strategies and equilibrium concepts

The child's strategy in the game is the angle \(\theta\). The parent's strategy is the return share \(\alpha\). The child's ratio \(q\) is not a strategy. It is read off in §2.6 from the angle the equilibrium installs. That is the sense in which the equilibrium might pin \(q\). Minimizing \(C_c\) over \(q\) directly is not the game: \(C_c\) is linear in \(\beta\), and \(\beta\) is the parent's action.

**Tie rules.** Both are scored on every cell. `T-small` picks the smallest \(\theta\), and the smallest \(\alpha\), in a \(10^{-9}\) tie set. `T-large` picks the largest. If the two rules produce headline ratios that differ by more than \(0.02\), the tie rule decides the headline and the pin fails.

**Nash.** A grid pair \((\theta,\alpha)\) is a pure Nash when \(\theta\) is the tie-rule best response to \(\beta=\alpha\rho\), and \(\alpha\) is the tie-rule best response to \(\theta\). The equilibrium set is the exhaustive set of such grid pairs. Best-response iteration (§2.7) is a reachability check. It does not define the set.

**Stackelberg, parent leads.** The parent commits to \(\alpha\). The child then plays its tie-rule best response to \(\beta=\alpha\rho\). The parent chooses the grid \(\alpha\) that minimizes \(J_p\) at that responding angle. A tie among \(\alpha\) uses the same tie rule. This is the one-way coupling: the parent moves first, the child does not move first.

### 2.5 Cells

Headline family, both accountings, both tie rules, every locked \(\tau\):

- \(w_c=w_p\in\{1,2,10\}\), \(\kappa_c=\kappa_p=\kappa_{D,p}=1\).

Scale family, for the dependence clause of P4, both accountings, both tie rules, \(\tau\in\{0,0.25,2\}\), \(w_c=w_p=1\):

- \((\kappa_c,\kappa_p,\kappa_{D,p})\in\{(1,1,1),\ (2,1,1),\ (1,2,2),\ (2,2,2)\}\).

The pair \((1,1,1)\) repeats the headline at those three delays. It is one cell, not a second weight.

Adversary, no cost for the parent's own information loss: \(\kappa_{D,p}=0\), \(\kappa_c=\kappa_p=1\), \(w_c=w_p=1\), both accountings, both tie rules, every locked \(\tau\). The reading under test: the return is \(0\), and \(0\) is in the rationalizing set.

Adversary, fully coupled parent: \(\kappa_{D,p}=\kappa_p=\kappa_c=1\), \(w_p=w_c=1\), both accountings, both tie rules, every locked \(\tau\). This is the headline at \(w=1\). It is reported under this name as well. Fully coupled means the parent prices a lost nat at the same coefficient it pays to hold a nat, and it carries the same stake as the child.

### 2.6 The reported ratio

Fix an installed angle \(\theta^\star\), a stake \(w_c\), and a scale \(\kappa_c>0\). For each \(q_i=i/50\), let \(T(q_i)\) be the set of grid angles whose charged cost

\[
I+q_i P_D+(w_c/\kappa_c)\,L
\]

is within \(10^{-9}\) of the minimum on the \(721\)-grid. The rationalizing set \(R\) is \(\{q_i:\theta^\star\in T(q_i)\}\).

- `pinned` when the Nash \(\alpha\) is unique, \(R\) is nonempty, \(R\) is not `UNBOUNDED_HIGH`, and \(\max R-\min R\le 0.02\).
- Otherwise not pinned. A ray is not a unique ratio.
- \(q_{\mathrm{hat}}=(\min R+\max R)/2\) when \(R\) is nonempty. It is a label of the set. It is the equilibrium ratio only when the cell is pinned.
- \(\beta=\alpha\rho\) is printed beside \(R\). Equality of \(q_{\mathrm{hat}}\) and \(\beta\) is the pricing identity of §2.3 when the angle is an interior critical point of \(C_c\). It is not, by itself, evidence that the game selected a price.

### 2.7 Finding the equilibria

Exhaustive pass: for each of the \(51\) values of \(\alpha\), score \(C_c\) on the \(721\) angles and apply the tie rule. For each of the \(721\) angles, score \(J_p\) on the \(51\) returns and apply the tie rule. A pair is Nash when each coordinate is the tie-rule reply to the other. No random search.

Best-response iteration, from three asymmetric starts, at most \(200\) rounds, stop when \((\theta,\alpha)\) repeats a previous pair:

| start | \(\theta\) | \(\alpha\) |
|---|---:|---:|
| S1 | \(0\) | \(0\) |
| S2 | \(\pi/2\) | \(1\) |
| S3 | \(\pi/4\) | \(0.2\), the grid point \(10/50\) |

S1 is a pointer with no return. S2 is an equator with a full return. S3 is an interior angle with a small return. None of the three is a time-symmetric pair of rates. A cycle is printed. A cycle is not a Nash point. `G-iter` fails only if iteration stops on a pair that the exhaustive pass does not list as Nash. A cycle, or a start that reaches only a subset of the Nash set, is printed and is not that failure.

### 2.8 Gate on the parent's root

Not an equilibrium forecast. At a fixed angle with \(P_D>10^{-4}\), \(\kappa_p=\kappa_{D,p}=1\), the tie-rule best return on the grid is within \(0.02\) of \(0.6\), and \(0.6=1-2/(1+4)\) is on the grid. At \(\kappa_{D,p}=0\) and the same angle, the unique best return is \(0\). A miss of this gate means the grid is not minimizing \(J_p\). The later lines are then not read.

## 3. Predictions

**P1.** On every headline cell, child accounting and lineage accounting, both tie rules, a pure Nash exists, the Nash \(\alpha\) is unique, and the rationalizing set is pinned.

*Fails if* any headline cell has an empty Nash set, more than one Nash \(\alpha\), a rationalizing set wider than \(0.02\), an `UNBOUNDED_HIGH` mark, or \(q_{\mathrm{hat}}\) values under the two tie rules that differ by more than \(0.02\). Report the cell, the accounting, \(\tau\), \(w\), the tie rule, the Nash set, \(R\), and \(\beta\). A miss means the joint equilibrium did not pin one ratio. The clue is whether the angle is a corner, whether the parent was indifferent because \(P_D\) vanished, or whether the two tie rules split.

**P2.** Every pinned headline ratio satisfies \(0<q_{\mathrm{hat}}<1\), and at each fixed \(\tau\) and accounting the pinned values at \(w\in\{1,2,10\}\) differ by at most \(0.02\).

*Fails if* a pinned ratio is at most \(0\) or at least \(1\), or if two pinned headline ratios at the same \(\tau\), same accounting, and different \(w\) differ by more than \(0.02\). A cell that P1 did not pin is also a miss of P2: there is then no unique ratio whose place in \((0,1)\) can be read, and the stake test has nothing to be independent of. Report the ratios and the stakes. A miss means either the pinned price sits on the boundary of the unit interval or outside it, or the stake remains in the price.

**P3.** On every headline cell, the Stackelberg \(\alpha\) differs from the Nash \(\alpha\) set: either the Nash set is empty, or the leader's \(\alpha\) is not the unique Nash \(\alpha\).

*Fails if* a headline cell has exactly one Nash \(\alpha\) and the Stackelberg \(\alpha\) equals it. Report both shares and both rationalizing sets. A miss means the parent leading does not change the return the joint equilibrium already selects.

**P4.** The pinned ratio is a function of \(\tau\) alone. At each fixed \(\tau\) and accounting, every pinned \(q_{\mathrm{hat}}\) in the headline family and in the scale family, under both tie rules, lies in an interval of length \(0.02\). In particular the value does not move by more than \(0.02\) when \(w\), \(\kappa_c\), \(\kappa_p\), \(\kappa_{D,p}\) (inside the scale list), or the tie rule changes.

Limits, scored on the pinned cells of that accounting:

- \(\tau\in\{2,4\}\) (the return is slower than the child persists): \(q_{\mathrm{hat}}\le 0.02\).
- \(\tau=0\) (the return is fast): \(|q_{\mathrm{hat}}-\alpha^\star|\le 0.02\), where \(\alpha^\star\) is the unique Nash return. The fast ratio sits on the returned share.

*Fails if* two pinned cells at the same \(\tau\) and the same accounting differ by more than \(0.02\), or a pinned slow cell has \(q_{\mathrm{hat}}>0.02\), or a pinned fast cell has \(|q_{\mathrm{hat}}-\alpha^\star|>0.02\). An unpinned cell is a miss of the clause "a function of \(\tau\) alone", because a set is not that function. Report the two cells, or the limit cell, with \(w\), the kappas, the tie rule, \(q_{\mathrm{hat}}\), \(\alpha^\star\), and \(\beta\).

A miss of the slow limit on the child accounting means a late return still prices a positive ratio for the child who is already gone. A miss on the lineage accounting means the lineage's books do not follow the child's clock. Those are different clues. They are not averaged.

**G-parent.** The root check in §2.8.

*Fails if* the grid return at the probe angle \(\theta=\pi/2\), ANT, \(\gamma=0\), \(\phi=0\), is not \(0.6\) when \(\kappa_p=\kappa_{D,p}=1\), or is not \(0\) when \(\kappa_{D,p}=0\). Do not refit \(u\).

**G-iter.** Iteration's terminal Nash pairs are inside the exhaustive set, on every headline cell and every start that terminates on a pair rather than a cycle.

*Fails if* a terminal pair is absent from the exhaustive set. A cycle is not this miss.

## 4. What a miss points to

P1 miss: the coupling did not select one price. If the Nash set is empty, simultaneous best replies do not meet on this grid. If the set of ratios is wide, the installed angle is cheap for an interval of prices, which is the linearity this series started from. The clue is the angle and \(P_D\), not a new term in \(J\).

P2 miss: a pin, if there is one, does not sit in the open unit interval, or it still carries the stake.

P3 miss: leading and moving together select the same return. The one-way parent is not a different price.

P4 miss: at fixed delay the price still moves with a stake, a kappa, or a tie rule, or the fast and slow limits do not sit on the returned share and on \(0\). The clue is which parameter moves it.

A pass of the parent's root together with a miss of P1 is the split this lock can detect: the parent has a preferred return, and that return still does not pin the child's ratio.

## 5. Common-cause checks

Scored after the equilibria, on the same costs. Not part of P1–P4. Tolerance \(0.02\) on a return or a ratio, and \(10^{-9}\) relative on a doubled cost. `REPRODUCED` only if the match uses no coefficient that was set to the target. Otherwise `CONTRADICTED`. If the Nash set the check needs is empty or not unique, the check is `NOT-MET`.

**B-blanket.** Probe angle: the tie-rule minimizer of \(I+w L\) on BIAS, \(\gamma=0\), \(\phi=0\), \(w=1\), \(\kappa_p=\kappa_{D,p}=1\). Full parent return versus the return when \(P_D\) is replaced by \(0\) in \(J_p\) only. Target: the two returns differ by at most \(0.02\).

**S-share.** Child accounting, \(\tau=0\), \(\kappa=1\), both tie rules, stake pairs \((w_c,w_p)\in\{(1,1),\ (1,2),\ (2,1)\}\). Target: the unique Nash return equals \(w_c/(w_c+w_p)\) within \(0.02\) on all three pairs. A match on the equal pair alone is not this target.

**F-copy.** Headline cell \(\tau=0\), \(w=1\), \(\kappa=1\), child accounting, `T-small`. Replace \((I,P_D,L)\) by twice those values inside both costs, same angle grid. Target: the Nash \(\alpha\) set and the rationalizing set are unchanged, and both equilibrium costs double, relative gap below \(10^{-9}\).

**F-bulk.** Same cell. Multiply an unused bulk slot by \(100\). The slot does not enter \(I\), \(P_D\), \(L\), or either cost. Target: the printed ratio is unchanged. A match here is not extra evidence.

**H-iface.** The same bulk slot. Target: the ratio is unchanged. Also print \(|q_{\mathrm{hat}}-0.25|\). A value inside \(0.02\) of \(0.25\) is a coincidence to record, not a derivation of holography, and it is not `REPRODUCED` for a cut-versus-volume claim. The invariance is the only holographic-note target.

## 6. What this run will not say

It will not edit `THEORY.md` or the T78 lock. It will not say that a value of the ratio has been obtained as a final answer. It will not say that a miss removes the coupling from further work. It will not treat a pin as a derivation of general relativity, quantum mechanics, holography, or gravity. It will not call \(\alpha_\star\) a stake share. It will not add a cell, a delay, a stake, or a tolerance after seeing the output.

## 7. Output

The script prints one line per named check, `PASS` or `FAIL`, then `FAILS` and a count. It then prints one line per scored cell. Stdout is stored and byte-compared by the test. `PREREG.md` is not read for numbers. `RUN_LOG.md` records every deviation and, if there is none, says so. The memo uses the labels PROVED (in-model), NUMERICAL, and PUZZLE. The memo has an errata section. This file is not rewritten to absorb an erratum.
