# T85 preregistration: a Deutsch fixed point against the acyclic record route

Why this approach: the acyclic menu in route A has no cycle, and its same-channel gap is \(\kappa_D P_D\). A two-qubit Deutsch loop is the smallest cycle that can be set beside that gap. The fixed-point equation, the entropy signs, a finite gate family, one dephasing parameter, and one closed observer-plus-bath return are enough to see whether the loop changes the sign or the ratio. Anything finer is a later lock.

Can it fail: yes. A fixed point can come back with a CTC entropy change above the bar, the chronology-respecting entropy can come back negative, the 64-gate count can miss 20, depolarizing can move the ratio gap, phase damping can destroy the pure fixed points, and the closed return can miss zero.

Cheapest way to fail it: one accepted fixed point with \(\Delta S(\rho_{CR}) < -10^{-9}\), or a non-unique count other than 20 on the 64-gate grid.

*Tuesday 24 November 2026 (UTC). Written and committed before `ctc_fixed_point_checks.py` and before any scored output. Branch `forge-ctc-fixed-point`, cut from fork `main` at `d2aeb8100e22870dc5aee2529356de970c82a820`. `THEORY.md` and `CORE.md` are not edited. The sha256 of this file is in the commit message. A later change to a bar below is a deviation, appended in `DEVIATIONS.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. This is a toy model of Deutsch's fixed-point prescription. It is not a claim about physical time travel. A miss is a puzzle. Every statement about what \(J\) does on this loop is a model implication, in-model.

## Hypothesis

**HYPOTHESIS, Ace's unreviewed candidate, re-derived here before the bars were locked.** A two-qubit Deutsch loop is a toy model of Deutsch's fixed-point prescription, and on that model the closed loop does not push the chronology-respecting entropy below the acyclic Landauer sign or force the record-price ratio.

The three candidate sentences that were re-derived, and not adopted as bars, are in §5. Ace's numbers were not used. No number below is taken from an unscored note.

## Null

These are restatements. A pass on them is not a new result.

- \(\Delta S(\rho_{CTC})=0\) at a fixed point is the definition of that fixed point, because the von Neumann entropy is a function of the state. Deutsch 1991 already asks for a state the loop leaves unchanged.
- The sign \(\Delta S(\rho_{CR})\ge 0\) proved in §4 is unitarity, a product input, and subadditivity. It is not a thermal bound.
- Reeb and Wolf 2014, Theorem 3 as recorded at `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:145` on `forge-record-ratio-reframes`, is an equality for a unitary on a system and an initially thermal reservoir. This loop has no reservoir. That theorem is not re-derived and is not instantiated.
- Route A's same-channel gap \(\kappa_D P_D(\theta)\) (`theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:103` on that branch) is cited, not refit.
- A closed unitary return has \(\Delta\langle H_B\rangle=0\). Dividing by one constant temperature is arithmetic. Clausius on a reversible return is the classical statement. The revival note's \(Q_{\mathrm{keep}}=0\) is the same vanishing of a net heat on a closed box (fork PR #21).

An addition would be a term in \(J=\kappa I(W;M)+\kappa_D P_D+w L\) that those statements do not already assign, or a ratio \(\kappa_D/\kappa\) that route A does not already leave free. None is expected.

## 1. Prior art

Checked on the Crossref API on 24 November 2026, HTTP 200, before this commit. No page is claimed. A DOI that did not return is not cited. No number is taken from these works.

- Deutsch, D. Quantum mechanics near closed timelike lines. Physical Review D 44:3197 (1991). doi `10.1103/PhysRevD.44.3197`. Crossref: title, author David Deutsch, Physical Review D, volume 44, pages 3197-3217, issued 15 November 1991. The fixed-point equation in §3 is the toy model associated with that prescription. The maximum-entropy choice among several solutions is the selector used in §6. This note does not quote a page.
- Reeb, D. and Wolf, M. M. An improved Landauer principle with finite-size corrections. New Journal of Physics 16:103011 (2014). doi `10.1088/1367-2630/16/10/103011`. Crossref: title, authors David Reeb and Michael M. Wolf, New Journal of Physics, volume 16, article 103011, issued 8 October 2014. Used only as the acyclic comparison already recorded in route C of the file cited in the null. Not re-derived.
- Landauer, R. Irreversibility and Heat Generation in the Computing Process. IBM Journal of Research and Development 5:183 (1961). doi `10.1147/rd.53.0183`. Crossref: title, author Landauer, volume 5, pages 183-191, issued July 1961. Heat is tied to irreversible erasure. A unitary return erases nothing net.
- Brun, T. A., Harrington, J., and Wilde, M. M. Localized Closed Timelike Curves Can Perfectly Distinguish Quantum States. Physical Review Letters 102 (2009). doi `10.1103/PhysRevLett.102.210402`. Crossref: that title, those authors, Physical Review Letters, volume 102, issued 27 May 2009. The title's claim is prior art for discrimination. The unitary in §3 is constructed in this note. It is not claimed to be their circuit.

Route A, the acyclic comparison, is `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:74-116` on `forge-record-ratio-reframes` (upstream draft PR #257; that file is not on this branch). The gap identity is `:103`. The vanishing condition is `:106`. The status line is `:112`. The model implication that the ratio stays unidentified is `:116`. The cost is `:12`.

The closed-box comparison is fork draft PR #21, `theory/revival-phase-storage-2026-11-24/MEMO.md:19`, where \(Q_{\mathrm{keep}}=0\) with purity 1 is a relabel of `CORE.md:78`. This note does not rescore that well.

## 2. Cost

The record cost is the two-term form named on draft #252 and repeated at `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:12`:

\[
J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L,
\]

with \(\kappa=1\), \(q=\kappa_D/\kappa=\kappa_D\), and \(w=0\) on every scored cell below, so \(L\) does not move \(J\). Coefficients are nonnegative, as in A8 (`CORE.md:52`). \(I(W;M)\) is the Shannon mutual information, in nats, of a computational-basis measurement of the output chronology-respecting qubit. \(P_D\) is the mean entropy increase of that qubit, \(\mathbb{E}[S(\rho'_{CR})-S(\rho_{CR})]\), the same functional as the entropy form of the pinch at `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:55`. The ratio gap of one design is

\[
J(q=1)-J(q=0)=P_D.
\]

That is the algebra at `:103` with \(\kappa_D=\kappa\) and with this \(P_D\). It does not set \(q\).

## 3. The loop

Two qubits. Basis order \(\lvert CR, CTC\rangle = \lvert 00\rangle,\lvert 01\rangle,\lvert 10\rangle,\lvert 11\rangle\).

\[
\rho_{CTC}=\mathrm{Tr}_{CR}\bigl[U(\rho_{CR}\otimes\rho_{CTC})U^\dagger\bigr].
\]

Natural log. Entropy \(S(\rho)=-\mathrm{Tr}[\rho\log\rho]\), eigenvalues below \(10^{-12}\) dropped.

Gates, columns as images of the basis:

- \(I\), the \(4\times 4\) identity.
- SWAP: \(\lvert cr,c\rangle\mapsto\lvert c,cr\rangle\).
- CNOT\(_{CR}\): control \(CR\), target \(CTC\). \(\lvert 10\rangle\leftrightarrow\lvert 11\rangle\).
- CNOT\(_{C}\): control \(CTC\), target \(CR\). \(\lvert 01\rangle\leftrightarrow\lvert 11\rangle\).
- CZ: \(\lvert 11\rangle\mapsto -\lvert 11\rangle\).
- DCNOT: CNOT\(_{C}\) after CNOT\(_{CR}\).
- DISC, built so that \(U\lvert 00\rangle=\lvert 00\rangle\) and \(U(\lvert 01\rangle+\lvert 11\rangle)/\sqrt{2}=\lvert 11\rangle\), extended by \(U\lvert 10\rangle=\lvert 10\rangle\) and \(U(\lvert 01\rangle-\lvert 11\rangle)/\sqrt{2}=\lvert 01\rangle\). Columns:

\[
\begin{aligned}
U\lvert 00\rangle&=\lvert 00\rangle,\\
U\lvert 01\rangle&=(\lvert 01\rangle+\lvert 11\rangle)/\sqrt{2},\\
U\lvert 10\rangle&=\lvert 10\rangle,\\
U\lvert 11\rangle&=(-\lvert 01\rangle+\lvert 11\rangle)/\sqrt{2}.
\end{aligned}
\]

Consequences locked with the gate, before the run. \(U\lvert 0\rangle\lvert 0\rangle=\lvert 0\rangle\lvert 0\rangle\). \(U\lvert +\rangle\lvert 1\rangle=\lvert 1\rangle\lvert 1\rangle\). So \(\rho_{CTC}=\lvert 0\rangle\langle 0\rvert\) is a fixed point for \(\rho_{CR}=\lvert 0\rangle\langle 0\rvert\) with output \(\lvert 0\rangle\), and \(\rho_{CTC}=\lvert 1\rangle\langle 1\rvert\) is a fixed point for \(\rho_{CR}=\lvert +\rangle\langle +\rvert\) with output \(\lvert 1\rangle\).

For \(\rho_{CR}=I/2\), the induced map on the CTC Bloch vector \(r\mapsto Mr+d\) is:

- \(I\): \(M=I\), \(d=0\). Every state is fixed.
- SWAP: \(M=0\), \(d=0\). Unique fixed point \(I/2\).
- CNOT\(_{CR}\): control bit is 0 or 1 with equal weight, so the channel is \((\mathrm{id}+\mathrm{Ad}_X)/2\). Fixed set: the \(x\) segment. Not unique.
- CNOT\(_{C}\): target \(I/2\), control reduced by a controlled flip. Channel is complete \(Z\)-dephasing. Fixed set: the \(z\) segment. Not unique.
- CZ: \((\mathrm{id}+\mathrm{Ad}_Z)/2\). Same fixed set. Not unique.
- DISC on \(\lvert 0\rangle\) and on \(\lvert +\rangle\): \(M=\mathrm{diag}(1/\sqrt{2},\,1/\sqrt{2},\,1)\), \(d=0\). Eigenvalue 1 is simple. Fixed set: the \(z\) segment. Not unique. Maximum entropy is \(r=0\).

The Heisenberg grid is \(U(a,b,c)=\exp\bigl(-i(a\,XX+b\,YY+c\,ZZ)/2\bigr)\) with \(a,b,c\in\{0,\pi/4,\pi/2,\pi\}\), 64 gates, \(\rho_{CR}=I/2\). Non-unique means the smallest singular value of \(M-I\) is below \(10^{-8}\).

## 4. Two proofs, locked before the run

**Entropy signs.** Let \(\rho_C\) be any fixed point, and let primes denote the state after \(U\). The input is a product, so \(S(\rho_{CR})+S(\rho_C)=S(\rho_{CR}\otimes\rho_C)\). Unitary evolution keeps the joint entropy. Subadditivity gives \(S(\rho'_{CR})+S(\rho'_C)\ge S(\rho_{CR})+S(\rho_C)\). The fixed-point equation is \(\rho'_C=\rho_C\), so \(S(\rho'_C)=S(\rho_C)\) and

\[
\Delta S(\rho_{CR})=S(\rho'_{CR})-S(\rho_{CR})\ge 0.
\]

The difference equals the output mutual information \(I(CR';C')\). It is zero when the output is a product. \(\Delta S(\rho_C)=0\) holds because the state is the same state. This is the null for the CTC entropy, and it is the sign bar for the chronology-respecting entropy.

**Depolarizing contraction.** Write \(D_\gamma(\rho)=(1-\gamma)\rho+\gamma I/2\), \(\gamma\in[0,1]\), and replace the fixed-point equation by \(\rho=D_\gamma(\Phi(\rho))\), where \(\Phi\) is the partial-trace map of §3. On Bloch vectors, \(D_\gamma\) multiplies \(r\) by \(1-\gamma\). A qubit channel's Bloch matrix has eigenvalues of modulus at most 1, so \((1-\gamma)M\) has no eigenvalue 1 when \(\gamma>0\). The affine equation has one solution. Every \(\gamma>0\) removes non-uniqueness. It does not by itself set \(P_D\) to 0.

For DISC, \(d=0\) and the \(z\) eigenvalue of \(M\) is 1, so the noisy equation on that axis is \(\gamma r_z=0\). For \(\gamma>0\), \(r=0\) is the only solution, and the output state is \(\Phi(I/2)\), which does not depend on \(\gamma\).

Phase damping \(Z_\gamma(\rho)=(1-\gamma)\rho+\gamma Z\rho Z\) multiplies the transverse Bloch components by \(1-2\gamma\) and leaves \(z\) alone. The \(z\)-segment fixed points of DISC are diagonal, so they stay fixed at every \(\gamma\), including \(\gamma=1/2\).

## 5. What was not locked as a pass

Ace's three candidate sentences, re-derived and then not used as pass bars:

1. \(\Delta S(\rho_{CTC})=0\) at a unique fixed point. The entropy half is the null. Uniqueness is false on the gates in §3. The locked object is the count, not uniqueness.
2. A state-discriminating \(U\) gives \(\Delta S(\rho_{CR})<0\) with no bath export, outside the acyclic Landauer/Reeb-Wolf bound. Section 4 gives the opposite sign on every fixed point of one density operator. The negative number in P2-illicit is an average of two different fixed points, one per pure label. It is not a map in the fixed-point equation. There is no bath, so Reeb-Wolf is not instantiated, and the honest sign does not go below the Landauer sign.
3. Dephasing on the CTC wire removes any \(q\)-dependent gap above some \(\gamma_c\). For depolarizing, non-uniqueness is gone for every \(\gamma>0\), and the surviving ratio gap on DISC is the positive constant in P3. It is not removed. Phase damping does not even remove the pure fixed points.

A pass of P2-bound or P3-gap is a pass of the re-derived bar. It is an unsupported outcome for candidate sentences 2 and 3.

## 6. Locked bars

Tolerances are absolute. A miss of a bar is a puzzle. The candidate sentences are not rescued by moving a bar.

**P1a.** On every accepted fixed point of §7, \(|\Delta S(\rho_{CTC})|\le 10^{-9}\).

**P1b-named.** At \(\rho_{CR}=I/2\), with the \(10^{-8}\) singular-value rule: non-unique \(\{I,\mathrm{CNOT}_{CR},\mathrm{CNOT}_{C},\mathrm{CZ},\mathrm{DISC}\}\), unique \(\{\mathrm{SWAP},\mathrm{DCNOT}\}\).

**P1b-grid.** On the 64-gate Heisenberg grid at \(\rho_{CR}=I/2\), exactly 20 gates are non-unique. Every non-unique smallest singular value is \(<10^{-8}\). Every unique one is \(>0.2\).

**P2-bound.** On every accepted fixed point of §7, \(\Delta S(\rho_{CR})\ge -10^{-9}\).

**P2-illicit.** CNOT\(_{C}\), label-dependent pure fixed points: \(\rho_C=\lvert 0\rangle\langle 0\rvert\) on input \(\lvert 0\rangle\) and \(\rho_C=\lvert 1\rangle\langle 1\rvert\) on input \(\lvert 1\rangle\). The equal mixture of the two output chronology-respecting states has entropy 0. The equal mixture of the inputs has entropy \(\ln 2\). The difference equals \(-\ln 2\) within \(10^{-9}\). The line is marked not a process on one density operator. The maximum-entropy selector on each input separately, \(\rho_C=I/2\), has \(\Delta S(\rho_{CR})=\ln 2\) within \(10^{-9}\) (the entropy rises).

**P3-gap.** DISC, depolarizing, \(\gamma\in\{10^{-6},0.01,0.1,0.5,1\}\). The fixed point is unique and equals \(I/2\). For inputs \(\lvert 0\rangle\) and \(\lvert +\rangle\), the ratio gap \(J(1)-J(0)\) equals \(h\bigl((2+\sqrt{2})/4\bigr)\) within \(10^{-8}\), where \(h\) is the binary entropy in nats. The same gap is \(>0.1\). It is not removed. The mutual information of the computational-basis measurement equals \(\ln 2-h(3/4)\) within \(10^{-8}\).

**P3-phase.** DISC, phase damping \(\gamma=1/2\), pure fixed points \(\rho_C=\lvert 0\rangle\langle 0\rvert\) on \(\lvert 0\rangle\) and \(\rho_C=\lvert 1\rangle\langle 1\rvert\) on \(\lvert +\rangle\). Both remain fixed within trace distance \(10^{-9}\). The ratio gap of that pair is 0 within \(10^{-9}\).

**P3-contraction.** DISC on \(\lvert 0\rangle\): nullity at \(\gamma=0\) is at least 1, and nullity at \(\gamma=10^{-6}\) is 0, same singular-value rule.

**P4-cycle.** One joint loop. World qubit \(W\) fair and diagonal, memory \(M\) starts at \(\lvert 0\rangle\), bath \(B\) starts at \(\lvert 0\rangle\), product. Bath Hamiltonian \(Z/2\). Temperature label \(T=1\), constant. Steps: CNOT from \(W\) onto \(M\); SWAP of \(M\) and \(B\); SWAP of \(M\) and \(B\); CNOT from \(W\) onto \(M\). The sum of bath energy changes over the four steps, each divided by \(T\), has absolute value \(\le 10^{-12}\). Net learning \(I(W;M)_{\mathrm{final}}-I(W;M)_{\mathrm{initial}}\) has absolute value \(\le 10^{-12}\). The joint state returns: trace distance to the initial state \(\le 10^{-12}\).

**P4-half.** The same loop stopped after the first SWAP. The sum of \(\Delta E_B/T\) equals \(-1/2\) within \(10^{-12}\). This open path is the control. The zero in P4-cycle is the return, not a property of every prefix.

## 7. Accepted fixed points

The entropy bars see only these states.

- Every unique gate on the named list and on the 64-gate grid, at \(\rho_{CR}=I/2\): the one solution of \((M-I)r=-d\).
- Every non-unique gate on those two lists, at \(\rho_{CR}=I/2\): the minimum-norm solution, and, when the nullity is 1, the two points where that line meets the Bloch sphere, and, when the nullity is 3, the origin and the six Pauli poles.
- SWAP at \(\rho_{CR}\in\{\lvert 0\rangle\langle 0\rvert,\lvert 1\rangle\langle 1\rvert,\lvert +\rangle\langle +\rvert,I/2\}\).
- DISC at \(\rho_{CR}=\lvert 0\rangle\langle 0\rvert\) with \(\rho_C\in\{\lvert 0\rangle\langle 0\rvert,I/2,\lvert 1\rangle\langle 1\rvert\}\), and at \(\rho_{CR}=\lvert +\rangle\langle +\rvert\) with the same three CTC states. All six are on the \(z\) segment.
- CNOT\(_{C}\) at \(\rho_{CR}=\lvert 0\rangle\langle 0\rvert\) and at \(\rho_{CR}=\lvert 1\rangle\langle 1\rvert\), each with \(\rho_C\in\{\lvert 0\rangle\langle 0\rvert,I/2,\lvert 1\rangle\langle 1\rvert\}\).

A sample point whose image is more than \(10^{-8}\) in trace distance from itself is not accepted. If a listed point is rejected, that rejection is a puzzle under P1a, not a silent drop. The script prints the rejection count. The locked expectation is 0 rejections.

## 8. Advance reading

P1a is the null. P1b is the failure route for uniqueness: non-unique fixed points, and how often, with the maximum-entropy point as the selector when a point must be chosen. P2-bound is the sign theorem. P2-illicit is the number that candidate sentence 2 was pointing at, marked as not that map. P3 is the dephasing claim, re-derived as a flat positive gap under depolarizing and a surviving pure solution under phase damping. P4 is the closed return.

Model implication, conditional on these bars: the loop does not push \(\Delta S(\rho_{CR})\) below 0, does not instantiate Reeb-Wolf, and does not force \(q\). The ratio gap that survives is \(P_D\), the route A algebra, with the \(P_D\) of whichever fixed point the selector keeps. The closed return assigns net learning 0 and net \(\sum\Delta E_B/T=0\), so the integrated floor on this loop is 0. That is the revival note's vanishing keep-cost read on a return, not a new floor.

A match that holds by a definition or by §4 is marked that way in the memo. It is not evidence.
