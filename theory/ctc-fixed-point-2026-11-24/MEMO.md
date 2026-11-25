# T85 memo: a Deutsch fixed point against the acyclic record route

*Tuesday 24 November 2026. Self-check, not an independent review. The lock is `PREREG.md` (sha256 `756d9f0c257d4dcf73d53440cde43a50dd8092633cdc3383cf7b21ad3b0e2f8e`, commit `f18721fc852f83a6154aa50186cbbdb876fe0ad9`), before `ctc_fixed_point_checks.py`. That file was not edited after the commit. `THEORY.md` and `CORE.md` are unchanged.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. This is a toy model of Deutsch's fixed-point prescription. It is not a claim about physical time travel. Each bar is logged as a hit or a miss with a signed size, a location and an update (`process/MISS_LOG_TEMPLATE.md`).

## Why this approach

**HYPOTHESIS, Ace's unreviewed candidate, re-derived before the bars were locked.** A two-qubit Deutsch loop is a toy model of Deutsch's fixed-point prescription, and on that model the closed loop does not push the chronology-respecting entropy below the acyclic Landauer sign or force the record-price ratio.

Route A has no cycle. Its same-channel gap is \(\kappa_D P_D(\theta)\) (`theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:103` on `forge-record-ratio-reframes`; the vanishing condition is `:106`, the status is `:112`). The two-qubit loop is the smallest cycle that can sit beside that gap. The score is `theory/ctc_fixed_point_checks/ctc_fixed_point_checks.out`. `FAILS 0` (`out:18`).

## Can it fail

Can it fail: yes. It did not. The cheapest miss, one accepted fixed point with \(\Delta S(\rho_{CR}) < -10^{-9}\), or a non-unique count other than 20, did not occur (`out:6`, `out:8`).

## Closed observer and bath

The composite is the world register \(W\), the memory \(M\), and the bath \(B\). Each step below is unitary, so the joint von Neumann entropy is constant. The four steps are CNOT from \(W\) onto \(M\), SWAP of \(M\) and \(B\), the same SWAP again, and CNOT from \(W\) onto \(M\) again (`PREREG.md:150`). CNOT twice is the identity on that pair, and SWAP twice is the identity, so the joint state returns exactly. The trace distance to the initial state is 0 (`out:15`).

The bath Hamiltonian \(H_B=Z/2\) does not depend on time. The energy change on a step is \(\Delta E_B=\mathrm{Tr}[H_B(\rho'-\rho)]\). Around a return,

\[
\sum \Delta E_B=\mathrm{Tr}[H_B(\rho(T)-\rho(0))]=0.
\]

One temperature label \(T=1\) is the label of this one bath. Then \(\sum \Delta E_B/T=0\). The scored sum is `0.000e+00` (`out:15`). The same sum stopped after the first SWAP, before the return, is \(-1/2\) (`out:16`). The zero is the return. It is not a property of a prefix.

A second temperature label, lower on the leg that absorbs energy and higher on the leg that returns it, would not give zero. The lock does not allow that label. The box has one bath Hamiltonian and no second reservoir.

Net learning is a function of the reduced state of \(W\) and \(M\). The final reduced state equals the initial one, so

\[
I(W;M)_{\mathrm{final}}-I(W;M)_{\mathrm{initial}}=0.
\]

The scored difference is `0.000e+00` (`out:15`). The intermediate copy is not a net. Uncomputing it puts the stock back.

`CORE.md:70` states \(\dot Q_M\ge kT\,\dot I_M\) under a memory/world split and local detailed balance, or under an Einstein relation. This unitary box meets neither hypothesis, so that floor does not assign a positive rate, and it does not by itself prove a zero. The zero this loop does prove is the pair above. The integrated comparison is \(0\ge 0\). Model implication: the heat floor on this closed loop contributes no positive net. That is the same vanishing as \(Q_{\mathrm{keep}}=0\) with purity 1 in the revival note (`theory/revival-phase-storage-2026-11-24/MEMO.md:19` on fork PR #21), read on a return rather than on a well with no bath. It is not a new floor. Landauer 1961 (doi `10.1147/rd.53.0183`) ties heat to irreversible erasure. A return erases nothing net.

## The fixed point, beside route A

\(\Delta S(\rho_{CTC})=0\) on every accepted fixed point. The maximum absolute value on 149 points is \(5.551\times 10^{-16}\), with 0 rejections (`out:7`). **Null.** It is the definition of a fixed point (`PREREG.md:25`, `:112`). Deutsch 1991 (doi `10.1103/PhysRevD.44.3197`) already asks for a state the loop leaves unchanged. No page is quoted.

Uniqueness is not part of that null. At \(\rho_{CR}=I/2\) the named gates split as locked (`out:4`): non-unique \(I\), CNOT\(_{CR}\), CNOT\(_{C}\), CZ, DISC; unique SWAP and DCNOT. On the 64-gate Heisenberg grid, 20 gates are non-unique (`out:6`). The smallest singular value on a unique gate is \(0.292893\). The largest on a non-unique gate is \(5.551\times 10^{-16}\). The maximum-entropy point is the selector when a point has to be chosen (`PREREG.md:168`). **This is the failure route for the word "unique" in candidate sentence 1.** The count is the locked object, and it passed.

**Sign.** For a product input and a unitary, subadditivity plus \(\rho'_C=\rho_C\) gives \(\Delta S(\rho_{CR})\ge 0\) (`PREREG.md:106-112`). The minimum on the accepted set is \(0\) (`out:8`). Candidate sentence 2, a negative chronology-respecting entropy with no bath export, is unsupported (`out:9`).

The number \(- \ln 2 = -0.693147180560\) is real and is not that map (`out:10`). It is the entropy of an equal mixture of two output states minus the entropy of the equal mixture of the two inputs, with a different pure fixed point on each label of CNOT\(_{C}\). The maximum-entropy selector on each input separately raises the entropy by \(\ln 2\). The line is marked `not-a-process`. There is no bath, so Reeb and Wolf 2014 (doi `10.1088/1367-2630/16/10/103011`), Theorem 3 as recorded at `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:145` on that branch, is not instantiated. The honest sign does not go below the Landauer sign.

**Ratio gap.** With \(\kappa=1\) and \(w=0\), \(J(1)-J(0)=P_D\) (`PREREG.md` cost section; the same algebra as route A `:103`). On DISC, depolarizing of strength \(\gamma>0\) leaves the unique fixed point \(I/2\) (`PREREG.md:114-116`). At \(\gamma\in\{10^{-6},0.01,0.1,0.5,1\}\) the gap is \(h((2+\sqrt{2})/4)=0.416495530700\) and the computational-basis mutual information is \(\ln 2-h(3/4)=0.130812035941\) (`out:11`). The gap stays above \(0.1\). Candidate sentence 3, that dephasing removes any \(q\)-dependent gap, is unsupported (`out:12`). Phase damping at \(\gamma=1/2\) keeps the pure fixed points, and that pair's ratio gap is \(1.110\times 10^{-16}\) (`out:13`). Nullity of the noiseless DISC map on \(\lvert 0\rangle\) is 1, and at \(\gamma=10^{-6}\) it is 0 (`out:14`).

Model implication, conditional on these bars (`PREREG.md:170`): the loop does not push \(\Delta S(\rho_{CR})\) below 0, does not instantiate Reeb-Wolf, and does not force \(q\). The ratio gap that survives is \(P_D\), with the \(P_D\) of the fixed point the selector keeps. Route A `:106` still has no reverse leg. A cycle on the CTC wire with \(\Delta S(\rho_{CTC})=0\) is not that reverse leg.

## Correction appended after the independent review

The sentences above that call the scored gap the route A gap stay visible. They are withdrawn. `PREREG.md` is not edited. The lock remains `f18721fc852f83a6154aa50186cbbdb876fe0ad9`, sha256 `756d9f0c257d4dcf73d53440cde43a50dd8092633cdc3383cf7b21ad3b0e2f8e`.

**Miss.** Location `model`. The prose claim was that the loop's ratio gap is route A's same-channel gap and is not undercut. Route A's minimized record cost of one classical channel has slope 0 in \(\kappa_D\) (`theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:116` on `forge-record-ratio-reframes`). The scored DISC design, one fixed point, has slope \(P_D=h((2+\sqrt{2})/4)=0.416495530700\). Signed size: \(+0.416495530700\) nats per unit \(\kappa_D\), outcome minus that slope 0. The eight-field row is `route-A-id` in `DEVIATIONS.md`. This blocks reading the score as a test of route A. The ten locked bars are not moved.

The loop's gap and route A's gap differ as follows.

1. Route A at `:103` is the cost of a direct measurement minus the cost of pointer-plus-garbling, two designs of one classical channel, equal to \(\kappa_D P_D(\theta)\). The scored gap is \(J(q=1)-J(q=0)=P_D\) on one DISC design (`PREREG.md:59-60`, `out:11`). There is no garbling path. `:114` is the menu on which that two-design gap is not a comparison.
2. Route A \(P_D\) is the entropy of a projective pinch on the antipodal ensemble (`:55` on that file). The CTC \(P_D\) is the entropy increase of the chronology-respecting qubit under the two-qubit unitary. For DISC at \(I/2\), the output of \(\lvert 0\rangle\) has diagonal entries \(3/4\) and \(1/4\) and an off-diagonal \(1/4\). That state is not the dephasing of \(\lvert 0\rangle\).
3. On route A's menu the minimized cost does not depend on \(\kappa_D\) (`:116`). On the scored design the cost rises with \(\kappa_D\) at slope \(0.416495530700\). That is the signed miss.
4. Minimizing \(q\) on this one design, with \(P_D>0\), selects the endpoint \(q=0\). `:112` already separates that endpoint from a ratio that stays unidentified.
5. If the pure fixed points and the mixed fixed point are both kept as designs, their costs meet when \(q=h(3/4)/h((2+\sqrt{2})/4)=1.350158892880\). Below that value the mixed point is cheaper, and its cost still depends on \(q\). The maximum-entropy selector keeps the mixed point and drops the pure pair. Neither reading recomputes `:103`.

What still stands, and is not that identification: the loop supplies no reverse leg that refunds a pinch, and \(\Delta S(\rho_{CTC})=0\) is not such a leg. The integrated floor 0 in P4 is the identity of CNOT twice and SWAP twice on the world, the memory, and a pure bath. The CTC qubit is not in that circuit. It is reversible uncomputation. It does not price the Deutsch fixed point.

**Grid.** The count 20/64 is exact on \(U(a,b,c)=\exp[-i(a\,XX+b\,YY+c\,ZZ)/2]\) with each angle in \(\{0,\pi/4,\pi/2,\pi\}\), \(\rho_{CR}=I/2\), non-unique when the smallest singular value of \(M-I\) is below \(10^{-8}\) (`out:6`). The unique-gate floor on that grid is \(1-1/\sqrt{2}=0.292893218813\). The count moves with the angle set. The same cutoff on \(\{0,\pi/6,\pi/3,\pi/2\}\) gives 10 of 64, on \(\{0,\pi/3,2\pi/3,\pi\}\) gives 20, on \(\{0,\pi/4,\pi/2,3\pi/4\}\) gives 10, and on \(\{\pi/4,\pi/2,3\pi/4,\pi\}\) gives 10. The locked bar is the locked grid. It was not moved.

## What is new, and what is not

Not new: \(\Delta S(\rho_{CTC})=0\); the sign from unitarity and subadditivity; route A's gap formula; Reeb-Wolf on a thermal reservoir, which this loop does not meet; Clausius on a return; the revival note's vanishing keep-cost.

Reported here, on this toy: 20 of 64 gates need a selector; the discriminating unitary's honest entropy does not fall; the label-dependent \(-\ln 2\) is excluded from the fixed-point map; depolarizing removes the extra fixed points and leaves the ratio gap at \(0.416495530700\); phase damping does not remove the pure solution; the closed return contributes no positive net floor.

## Deviations

`DEVIATIONS.md`. No bar was missed. The preregistration was not edited.

Appended after the review: the route A identification is a miss, logged in that file. The ten locked bars stay hits.

**Labels, 25 November 2026 (bar by bar, `process/PROCESS.md:28`).** CONSISTENCY_CHECK, an identity that could not miss: P1a, P2-bound, P3-phase, P3-contraction, P4-cycle. Bars that could have missed: P1b-named, P1b-grid, P2-illicit, P3-gap, P4-half. The route A identification is a separate miss located in the model (`DEVIATIONS.md`). No number or bar changed.
