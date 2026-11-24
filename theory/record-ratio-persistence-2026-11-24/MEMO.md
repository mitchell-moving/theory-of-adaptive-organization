# Record ratio: what persists can be selected

*24 November 2026 (UTC). Lock `theory/record-ratio-persistence-2026-11-24/PREREG.md`, sha256 `d48a03e1efa2925db460ad3da11aa9f2026f8f6d9d85c4810de09b1d1696cfea`, commit `f8ffe82`, author date 2026-11-24 17:54:23 UTC, before `persistence_checks.py`. Self-check, not an independent review. `THEORY.md` is unchanged (blob `6caadae569116a94a74563398be94cebf6e99e9b`). Open-work row T78. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

*Forge's intuition, not an axiom: a selector that prices only the part of the record still present next round should land on \(q=0\), and a positive ratio should show up only where the loss or the record cost is flat. The grid agrees on the base selector. It does not agree once a destroyed nat is put back, or once destruction removes the lineage.*

## Answer

**Model implication, in-model.** On the base selector the long-run cost is \(F=I+wL\). Ratio \(0\) installs a minimizer of \(F\), so it weakly dominates every \(q>0\). The dominance is equality when that \(q\) installs the same angle. A second measurement of the collapsed state does not change this: the conditional information is roundoff.

Two adversaries do change it. Both were locked before the grid, and both miss the reading that \(q=0\) still wins.

**Restoration.** A fraction \(\alpha\) of \(P_D\) is persistent again, so selection's cost is \(F_\alpha=I+\alpha P_D+wL\), which is \(J\) at ratio \(\alpha\). The policy still installs the angle that minimizes \(J\) at its own \(q\). On 10 of 26 cells a \(q>0\) undercuts \(q=0\) by at least \(10^{-4}\). Every such cell is tagged `RESTORE`: the angles differ. The winning object is an angle, and the support is every ratio in the menu that installs it. It is not a single ratio, and it is not always \(1\).

**Ruin.** Removal probability \(\rho P_D/P_{\max}\) is an adversary, not A2. On 20 of 26 cells it drops \(q=0\). Every such cell is tagged `RUIN-REMOVE`. At complete dephasing the equator is the most disturbed angle. At \(\rho=1\) its growth weight is \(0\). At \(\phi=\pi/2\), where the loss is flat, ratio \(1\) is indifferent over the angle, the tie rule installs the equator, and the unique survivor is \(q=2\).

P2 misses on the 24 of those cells whose loss and whose offending record cost are both curved. The six flat-loss ruin cells are not P2 misses. The clause that allowed them is the flat loss, and the ratio they keep is \(2\), not \(1\).

## What was scored

`persistence_checks.out`, `FAILS 3`. The menu is the T76 qubit: ANT and BIAS, \(r=0.6\), \(\kappa=1\), ratios \(\{0,0.25,0.5,0.64,1,2\}\). `G0` matches the closed form to \(1.110\times 10^{-16}\). The loss range at \(\phi=0\) is \(0.032400\). At \(\phi=\pi/2\) it is \(0\). The equator-end quotient at \(w=1\) is \(0.640000050577\). The flat-loss quotient at \(\theta=1\) is \(0.999999999997\). The finite replicator at \(100000\) generations matches the exact support on every base cell (`G-dyn`, `skip_gap=0`).

**P1 matches. PROVED (in-model), and NUMERICAL.** \(C_0(0)\) is the minimum of \(F\) on the shared grid, and every other policy is scored at a grid angle. No \(q>0\) can undercut it. The worst gap on the 13 base cells is \(0\).

**Second pinch matches. NUMERICAL.** On ANT, \(\gamma=0\), \(\phi=0\), \(w\in\{1,2\}\), the largest conditional information of a second angle in \(\{0,\pi/4,\pi/2\}\) is \(5.551\times 10^{-17}\). The base ranking does not move. Remeasuring the collapsed state is not a recovery. The adopted reason is the one in `second_pinch`: given the first outcome, the second outcome is fixed by the angle between the axes.

**Non-flat ties, a clue, not a miss.** Of 34 cells where some \(q>0\) ties \(0\), 25 are non-flat. Those ratios install the same angle as \(0\), so persistence does not separate them. A positive ratio in the support is not yet a positive ratio selected against \(0\).

## Where a positive ratio wins

### Restoration

\(F_\alpha=(1-\alpha)I+\alpha P_\chi(0)+wL\) on ANT at \(\gamma=0\). When \(q=0\) installs the equator and the winner installs the pointer,

\[
F_\alpha(\pi/2)-F_\alpha(0)=(\alpha-1)P_\chi(0)+w(r^4/4)\cos^2\phi.
\]

**PROVED (in-model)** for that pair of endpoints. The grid matches it.

| cell | \(\alpha\) | selected set | gap |
|---|---:|---|---:|
| ANT, \(\phi=0\), \(w=2\) | \(1/2\) | \(\{0.5,0.64,1,2\}\) | \(1.661381\times 10^{-2}\) |
| ANT, \(\phi=0\), \(w=1\) | \(1\) | \(\{1,2\}\) | \(3.240000\times 10^{-2}\) |
| ANT, \(\phi=0\), \(w=2\) | \(1\) | \(\{0.5,0.64,1,2\}\) | \(6.480000\times 10^{-2}\) |
| ANT, \(\phi=\pi/4\), \(w=1\) | \(1\) | \(\{1,2\}\) | \(1.620000\times 10^{-2}\) |
| ANT, \(\phi=\pi/4\), \(w=2\) | \(1\) | \(\{1,2\}\) | \(3.240000\times 10^{-2}\) |

At \(\alpha=1/2\), \(w=2\), \(\phi=0\), the costs are \(0.408186\) at the equator and \(0.391572\) at the pointer. \(P_D\) is \(0.096372\) and \(0\). The smallest winning ratio is \(1/2\), the restoration fraction, not \(1\). At \(\alpha=1\) and \(w=1\) the designs separate only for ratios that reach the pointer, and the smallest such menu point is \(1\). At \(w=2\) ratio \(1/2\) already reaches it, so \(1\) is in the set and is not the unique element.

**NUMERICAL, same tag.** BIAS, \(\phi=0\): gaps \(3.089358\times 10^{-2}\) and \(9.188182\times 10^{-2}\) at \(\alpha=1/2\), \(w=1\) and \(w=2\); \(1.272660\times 10^{-1}\) and \(1.882542\times 10^{-1}\) at \(\alpha=1\). Partial dephasing, ANT, \(\gamma=1/2\), \(\phi=0\), \(w=1\), \(\alpha=1\): gap \(3.240000\times 10^{-2}\), selected set \(\{0.64,1,2\}\), pointer disturbance still \(2.285027\times 10^{-2}\). The angle has moved. The state has not been returned to \(P_D=0\).

The 16 cells that do not miss are the ones where the two designs do not separate: \(\phi=\pi/2\) at every scored stake (the loss is flat, so \(F_1\) is flat and nobody undercuts), \(w=10\) where \(q=0\) is already at the pointer, and the low-stake half-restoration cells whose rescaled stake is still on the equator.

**Mechanism.** The restored nat is back in the stock selection can see. \(F_\alpha\) is \(J\) at ratio \(\alpha\). A policy whose own ratio installs a minimizer of that cost beats a policy that minimizes \(I+wL\) and, at these stakes, destroys the nat restoration then charges. Charging destruction pays because the destruction did not stay destroyed.

### Ruin

**Mechanism.** The lineage that installs the more disturbed angle is removed more often, so selection never banks its lower one-shot persistent cost. The map is the adversary in the lock. It is not a disturbance budget taken from A2.

At ANT, \(\gamma=0\), \(\phi=0\), \(w=1\), \(\rho=1\): the equator has \(P_D=P_\chi(0)\), removal probability \(1\), growth weight \(0\), persistent cost \(0.180000\). The pointer has removal probability \(0\), persistent cost \(0.243972\), growth weight \(0.783509\). The one-shot cost is higher. The lineage is the one still present. The selected set is \(\{1,2\}\).

At the same cell with \(\rho=1/2\), the printed weights are \(0.417635\) and \(0.783509\). The pointer still leads. Tag `RUIN-REMOVE` on all 20 misses. No cell is `OTHER`.

At \(\phi=\pi/2\) the loss does not depend on the angle, so the persistent-cost gap between pointer and equator is \(P_\chi(0)\) at every stake. The printed costs differ by \(0.096372\) at \(w=1\), \(w=2\), and \(w=10\). Ratio \(1\) has a flat charged cost, so §2.3 keeps the minimizer of \(F\), which is the equator, and ruin treats it as \(q=0\). Ratio \(2\) has a negative coefficient on \(I\) and installs the pointer. The support is \(\{2\}\) at each of those six cells. At \(\rho=1/2\) the equator's survival factor is \(1/2\) and \(\exp(P_\chi(0))=1.101169\), so a factor \(1/2\) does not offset a ledger of that size. **PROVED (in-model)** for that comparison. The three stakes match it.

Partial dephasing does not need a safe pointer. At \(\gamma=1/2\), \(\rho=1/2\), the winning angle is \(0\) with \(P_D=2.285027\times 10^{-2}\) and removal probability \(0.118552\), against \(0.5\) at the equator. Weights \(0.690623\) and \(0.408200\). The smallest menu ratio in the support is \(0.64\).

The six cells that hold are \(w=10\) at \(\phi=0\) and at \(\phi=\pi/4\), ANT and the BIAS row. There \(q=0\) already installs the undisturbed pointer, so removal has nothing to charge.

## What the misses point to

P1 does not miss. The base sentence holds: a nat that is gone is not in \(F\), and minimizing \(F\) is ratio \(0\).

P2 misses where a channel excludes \(0\) on a curved control. The clue is the channel, not a new term in \(J\). Flatness of the antipodal record cost at ratio \(1\) is not what excluded \(0\). Several ratios that do not flatten \(I+qP_D\) install the same winning angle, and the support keeps all of them. Ratio \(1\) is one element of that set when the winning angle is the pointer. It is absent from the set when the loss is flat and removal is on, because the tie rule then gives ratio \(1\) the equator.

The second pinch is the adversary that does not pay. Restoration pays by putting the nat back. Ruin pays by deleting the lineage that spent it. Those are different mechanisms, and neither is a symmetry of a flat loss.

A pass of P1 with a miss of both adversaries is the split the lock asked to keep. The two misses are not averaged into one ratio.

**Model implication, in-model.** Conditional on selection seeing only \(I\) and \(L\): the long-run support contains \(0\), and a \(q>0\) is there only by installing the same angle. Conditional on a fraction \(\alpha\) of \(P_D\) persisting: the support is the set of menu ratios that install a minimizer of \(J\) at ratio \(\alpha\). Conditional on removal proportional to \(P_D\): the support is the set of menu ratios that install a less disturbed angle, and on the flat-loss axis that set is \(\{2\}\).

## Errata after the independent review

*Appended after the independent review of head `5660367` (fork PR #11, comment 7140772595; branch `forge-persistence-review` at `d6e9653`). Zero blockers. `PREREG.md`, `persistence_checks.py`, and `persistence_checks.out` are unchanged. The sections above are the record of the locked map. This section restates their scope. The three notes below are the review's HIGH notes.*

### Restoration

**Identity.** \(F_\alpha=I+\alpha P_D+wL\) is \(J\) at ratio \(\alpha\), by the definition in PREREG §2.5. The sentence above, that the persistent cost is \(J\) at ratio \(\alpha\), restates that definition. It is not a finding. The grid did not produce it.

**NUMERICAL. The only evidence is the angle separation.** On 10 of 26 cells the installed angles differ (tag `RESTORE`). Ratio 0 is at the equator and a positive menu ratio is at the pointer. The stored gaps on those cells run from \(1.620000\times 10^{-2}\) to \(1.882542\times 10^{-1}\). Those gaps are what the identity and that separation already imply.

### Flat-loss support

**Clue. It depends on the tie rule and on the menu.** On the locked menu \(\{0,\ 0.25,\ 0.5,\ 0.64,\ 1,\ 2\}\), ratio 2 is the only point above 1. Every ratio above 1 installs the pointer, and those ratios tie. The locked tie rule minimizes \(F\) on a flat charged cost, assigns ratio 1 the equator, and the removal map then drops ratio 1, so the stored support is \(\{2\}\). The independent review applied the smallest-angle rule and the minimum-\(P_D\) rule to that same flat charged cost. Both put ratio 1 in the support, at the same weight as ratio 2. \(\{2\}\) is that menu under that resolution of a flat charged cost. It is not a unique survivor.

### Removal map

**Modeling choice.** The locked probability is \(\min(1,\ \rho P_D/P_{\max})\). At maximum disturbance this equals \(\rho\), and at \(\rho=1\) the growth weight is 0. The stored weights \(0\) and \(0.783509\) are that cap. The independent review scored the monotone map \(\min(1,\ \rho P_D)\), which is not divided by \(P_{\max}\). Ratio 0 is back in the support on 7 cells, all at \(\rho=1/2\), and on the flat-loss axis that map removes the locked support \(\{2\}\). The 20 exclusions, and \(\{2\}\) on the flat-loss axis, depend on that normalization. The closing conditional above, removal proportional to \(P_D\) with flat-loss support \(\{2\}\), is broader than the map that was scored.

## What survives

**Model implication, in-model.**

\(q=0\) weakly dominates when destruction stays gone. That is P1.

A positive \(q\) needs a return channel, and its size is set by how that channel is modeled, not by \(J\).

So \(q\) is set outside \(J\) by whatever produces the return. That is the open question T79 takes up.
