# T79 memo: two levels, each minimizing its own cost

*Tuesday 24 November 2026. Self-check. P1–P4 are the main result. P5 is a secondary reading of the same equilibria. The locks are `PREREG.md` (sha256 `b78addd0edf765e9fa76c1f0d82cfdc88a30d9105b8bb0ddd5a4e6410a37e39e`, commit `6849d6a`) and `PREREG_3.md` (sha256 `6f89428bca13a08d9714f08cca260c83e4719ae4a7f735055f815ad5c66430c9`, commit `9c004d7`), both before `bicausal_checks.py`. Neither file was edited after its commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every number below is in-model.

## Why this approach

The parent and the child each minimize the cost already in the repo. The child's angle changes the parent's record. The parent's return changes the share the child is charged. The ratio is read off the angle that equilibrium installs. It is not a strategy, and it is not minimized directly, because that cost is linear in the ratio.

## Can it fail

Can it fail: yes. A pure Nash can be missing, or the angle it installs can be rationalized by a wide set of ratios. For the reversibility reading, the persistence reset is not the reverse of the keep rate, so the steady divergence need not hit 0.

Cheapest way to fail: one headline cell with an empty Nash set or a rationalizing set wider than 0.02, or two equilibria with the same entropy production and different ratios.

## Pricing, stated again

The child's charged cost is \(I+\beta P_D+(w_c/\kappa_c)L\) with \(\beta=\alpha\rho\). That is \(J\) at ratio \(\beta\), the restoration identity from T78, used here as a price. The parent's channel cost is the binary entropy \(u(\alpha)=1-h((1-\alpha)/2)/\ln 2\), and the residual information loss is linear in \(1-\alpha\). At equal parent kappas the root is \(0.6\). The loss term does not depend on \(\alpha\) inside the parent's cost. \(\rho=\max(1-\tau,0)\) for the child and \(\rho=1\) for the lineage. The two books are not averaged.

## PROVED (in-model)

`G-parent` passes. At \(\theta=\pi/2\), ANT, \(\gamma=0\), \(\phi=0\), \(P_D=9.637238\times 10^{-2}\). Equal parent kappas: the grid return is \(0.600000\). No information-loss cost: the return is \(0.000000\).

`G-rev` passes. Six equal off-diagonal rates give steady entropy production \(0\).

`G-iter` passes. Every fixed point the iteration stops on is in the exhaustive Nash set. The empty cells are 2-cycles, printed, and are not that miss. The cycle at child accounting, \(\tau=0\), \(w=2\), `T-small`, is \((\theta=0,\alpha=0)\) with \((\theta=\pi/2,\alpha=0.60)\).

`F-copy` is reproduced. Doubling \((I,P_D,L)\) leaves the Nash return at \(0.600000\) and the rationalizing set unchanged. Both equilibrium costs scale by \(2.000000000000\).

## NUMERICAL

Headline grid: 72 cells. `FAILS 5` (`bicausal_checks.out`).

**P1, puzzle.** 71 of 72 cells are not pinned. The one pin is child accounting, \(\tau=0.5\), \(w=2\), `T-small`: \(\theta=1.075559\), \(\alpha=0.600000\), \(\beta=0.300000\), \(I=2.061163\times 10^{-2}\), \(P_D=7.576075\times 10^{-2}\), \(R=\{0.30\}\), \(q_{\mathrm{hat}}=0.300000\). That equality \(q_{\mathrm{hat}}=\beta\) is the pricing identity at an interior angle. It is not evidence the game selected a price. `T-large` on the same cell adds a second Nash, the pointer at \(\alpha=1.000000\), \(R=[0.38,2.00]\), \(q_{\mathrm{hat}}=1.190000\).

The typical `T-small` cell with \(w=1\) is the equator, \(\alpha=0.600000\), \(R=[0.00,0.64]\), midpoint \(0.320000\). At \(w=10\) the Nash is the pointer at \(\alpha=0\) when `T-small` picks it, and \(R=[0.00,2.00]\), marked unbounded. At \(w=2\) and a fast return, `T-small` has no pure Nash.

**P2, puzzle.** The one pinned ratio, \(0.300000\), sits in \((0,1)\). The other 71 cells are not pinned, so there is no second ratio against which the stake could be compared.

**P3, puzzle on 46 of 72 cells.** The parent leading and the joint equilibrium select the same return there. Child, \(\tau=0.5\), \(w=1\), `T-small`: both returns are \(0.600000\). They differ on other cells. Child, \(\tau=0\), \(w=1\), `T-small`: Nash \(0.600000\), Stackelberg \(0.700000\). Where the Nash set is empty the fail condition is not met. Child, \(\tau=0\), \(w=2\), `T-small`: the cycle above, Stackelberg \(0.380000\).

**P4, puzzle.** No cell in the slow or fast limits is pinned, so the ratio is not a function of \(\tau\) alone. The printed `bad=119` counts 72 headline rows and 48 scale rows, minus the one pin. Twelve of those scale rows repeat \((\kappa_c,\kappa_p,\kappa_{D,p})=(1,1,1)\), which the lock counts once. The unique count is 107 unpinned cells out of 108. At \(\tau=0\), child, \(w=1\), `T-small`, the Nash return is \(0.600000\) and the midpoint of \(R\) is \(0.320000\), which is \(0.28\) from the returned share. At \(\tau=2\) and \(\tau=4\), \(\beta=0\) for the child, and \(R\) is still \([0.00,0.64]\) at \(w=1\) (midpoint \(0.320000\)) and \([0.00,0.28]\) at \(w=2\) (midpoint \(0.140000\)). A late return does not put the ratio at \(0\). The scale family moves the midpoint of the same kind of set: at \(\tau=0\), child, `T-small`, \(w=1\), the midpoint is \(0.320000\) at \(\kappa_c=1\) and \(0.410000\) at \(\kappa_c=2\).

The lineage book keeps \(\rho=1\) at every \(\tau\), so a late return is still a live charge there. It does not pin a ratio either. At lineage, \(w=2\), `T-small`, every locked \(\tau\) is the same empty Nash and the same 2-cycle.

**Adversary, no information-loss cost.** 24 cells: 16 have the unique return \(0\), and \(0\) is in the rationalizing set; 8, all `T-large`, have the Nash set \(\{0,1\}\); none are empty. The small tie rule gives the reading. The large tie rule adds a full return where \(P_D=0\) and the parent is indifferent. The set that contains \(0\) is \([0.00,0.64]\) on those equator angles, not a pin.

**Adversary, fully coupled.** This is the headline at \(w=1\): unique Nash return \(0.600000\) under `T-small`, \(R=[0.00,0.64]\).

## PUZZLE, P5

Hypothesis from Chad and Ace: the ratio measures how reversible the boundary is. Scored on the headline Nash pairs, not on a wider model. Steady entropy production is the path-space KL per unit time of the locked three-state chain. The floor \(\varepsilon_0=10^{-6}\) only keeps every reverse edge finite. Reverse rates are not copies of forward rates. Starts S1 \((0.80,0.15,0.05)\), S2 \((0.05,0.20,0.75)\), S3 \((0.50,0.40,0.10)\) are asymmetric. Seed `20261124` is set and not drawn from.

Child steady \(\sigma\) runs from \(1.706013\times 10^{-8}\) to \(1.551351\times 10^{-2}\). The smallest is below \(0.05\), and its \(q_{\mathrm{hat}}\) is \(0.320000\), not \(1\). The largest has \(q_{\mathrm{hat}}=0.300000\), not at most \(0.02\).

Same \(\sigma\), different \(q\): child, \(\tau=0\), \(w=1\), `T-small`, \(\sigma=1.706013\times 10^{-8}\), \(q_{\mathrm{hat}}=0.320000\); child, \(\tau=0.25\), \(w=1\), `T-large`, \(\alpha=1\), \(\sigma=9.595494\times 10^{-7}\), \(q_{\mathrm{hat}}=1.350000\). The gap in \(\sigma\) is below \(10^{-3}\). The gap in \(q\) is \(1.03\). The delay is still visible at fixed \(\sigma\).

Not monotone: child, \(\tau=4\), \(w=2\), `T-small`, \(\sigma=1.008748\times 10^{-6}\), \(q_{\mathrm{hat}}=0.140000\); then child, \(\tau=0.5\), \(w=2\), `T-large`, \(\sigma=1.551351\times 10^{-2}\), \(q_{\mathrm{hat}}=0.300000\). The ratio rises while the divergence rises.

Lineage \(\sigma\) all sits in \([1.706013\times 10^{-8},\ 1.008748\times 10^{-6}]\), one band of width \(10^{-3}\), while \(q_{\mathrm{hat}}\) runs from \(0.320000\) to \(1.350000\). There is no slope to read. The same-band clause is the miss.

Path KL over one persistence time is a different number. On the child cloud, S1 spans \(0.359032\) to \(1.565091\), S2 spans \(7.068414\) to \(8.675755\), and S3 spans \(1.071406\) to \(4.336982\). The three starts agree. Each one is smallest at \(\tau=0\), \(w=1\), `T-large`, \(\alpha=1\), \(q_{\mathrm{hat}}=1.350000\). The smallest steady \(\sigma\) is a different cell: \(\tau=0\), \(w=1\), `T-small`, \(\alpha=0.6\), \(q_{\mathrm{hat}}=0.320000\). Clause 6 fails because those two cells differ.

The clue is the reset. Its rate is \(1\), and the keep rate is \(I\), which is \(0\) at the equator, so the stationary mass sits in the unrecorded state. At the minimum cell, \(\pi_U=0.999998\). Steady \(\sigma\) is below \(10^{-3}\) on 35 of 37 child Nash pairs. The range is that leak plus the one interior pin. The ratio stays the width of the angle's rationalizing set. Forcing the reverse rates to match the forward rates would be the mirror's circularity (`MIRROR_REVIEW.md:31`, `:60`, at `e3e0e701`) and was not done.

## What the grid is sampling

Wherever \(P_D>0\), the parent's continuous best reply is the constant root \(0.6\). An interior Nash is the child answering a return that formula fixed. The child's angle changes the grid return at the pointer, where \(P_D=0\) and the tie rule picks \(0\) or \(1\). It changes the leader's return when a commitment moves the child off the equator. On child accounting, \(\tau=0\), \(w=1\), `T-small`, the Nash cost of the parent at \(\alpha=0.600000\) is \(0.245347\) and the leader's cost at \(\alpha=0.700000\), on the pointer, is \(0.243972\). The leader's cost is lower by \(0.001375\).

On every equator Nash the rationalizing set is the \(0.02\)-grid sample of \([0,\ 1-(w_c/\kappa_c)r^2]\) with \(r=0.6\). The edges are \(0.64\) at \(w/\kappa_c=1\), \(0.28\) at \(w/\kappa_c=2\), and \(0.82\) at \(w/\kappa_c=1/2\). The midpoints \(0.320000\), \(0.140000\), and \(0.410000\) are half those edges. The movement with \(\kappa_c\) is that normalized stake. The cycle, the Stackelberg gap, and the entropy-production miss are the parts that go past this identity.

## Common-cause targets

**B-blanket, contradicted.** On BIAS the probe has \(P_D=0.192745\). The full parent returns \(0.600000\). Replacing \(P_D\) by \(0\) in the parent's cost returns \(0.000000\) under `T-small` and \(1.000000\) under `T-large`.

**S-share, not met.** `T-small` at stakes \((2,1)\) has an empty Nash set. `T-large` at \((1,1)\) and at \((1,2)\) has two Nash returns. The unique returns that do exist miss the stake shares: \(0.600000\) against \(0.500000\), \(0.600000\) against \(0.333333\), and \(1.000000\) against \(0.666667\). The parent's root does not move with the stakes.

**F-copy, reproduced.** As in the proved line. The match is the homogeneity of a linear cost, which is the reason already in the fractal note. It is not a new dimensionless ratio.

**F-bulk, reproduced.** An unused factor \(100\) leaves \(q_{\mathrm{hat}}\) at \(0.320000\). A match here is not extra evidence.

**H-iface, reproduced for the invariance only.** The same unused factor. \(|q_{\mathrm{hat}}-0.25|=0.070000\), outside \(0.02\). There is no coincidence with a quarter, and this is not holography.

## Errata

The locks were not edited.

`PREREG_3.md:71-77` names two boundary terms. The displayed equation is \(H(p_n)-H(p_0)\). The sentence above it puts the start \(p_0\) on both ends. The run scores the equation. Substituting the fixed-reference boundary leaves the path-KL minimum on the same cell, \(\tau=0\), \(w=1\), `T-large`, \(q_{\mathrm{hat}}=1.350000\), which is still not the steady minimum. The steady clauses do not use this boundary. P5 misses either way.

The P1 fail text also names a split of \(q_{\mathrm{hat}}\) across the two tie rules. The script marks a cell by its own summary. It does not compare the two rules in a separate line. The only pin's other rule is already unpinned, so `FAILS 5` does not depend on that comparison.

A review's line check: swarm alignment is `theory/SWARM_RULE_2026-11-23.md:47`, and line 46 is the tamper sentence. The fractal citation `:76-78` is the section heading. The T78 base-selector sentence is that memo's line 11, just above the cited lines. Those pointers stay in the committed lock.
