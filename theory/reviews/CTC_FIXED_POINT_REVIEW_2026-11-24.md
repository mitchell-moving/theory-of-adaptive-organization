# Independent review: Deutsch fixed point, 24 November 2026

Reviewed fork draft PR #25, branch `forge-ctc-fixed-point`, head `3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45`. The preregistration commit is `f18721fc852f83a6154aa50186cbbdb876fe0ad9`. The sha256 of `theory/ctc-fixed-point-2026-11-24/PREREG.md` is `756d9f0c257d4dcf73d53440cde43a50dd8092633cdc3383cf7b21ad3b0e2f8e`. This review does not edit that file, `THEORY.md`, or `CORE.md`.

This is a toy model of Deutsch's fixed-point prescription. It is not a claim about physical time travel. Nothing here derives general relativity, quantum mechanics, holography, or gravity. Every statement about what the cost does on this loop is a model implication.

> The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

Wording and the ledger follow `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` on upstream `main` at `652d936f3f6c9a97a0cfec60fb99a209db0f015b` (upstream PR #261, merged 2026-11-24T21:24:40Z). A prediction error is a miss, with signed size, location (`model`, `measurement/code`, or `process`), and update. A hit that follows from unitarity, subadditivity, or the fixed-point definition carries about zero information and is labeled **NOT A TEST / consistency check** (`PROCESS.md` item 5). Historical text, including the locked preregistration, is not rewritten.

**HYPOTHESIS under review.** A two-qubit Deutsch loop is a toy model of Deutsch's fixed-point prescription, and on that model the closed loop does not push the chronology-respecting entropy below the acyclic Landauer sign or force the record-price ratio.

## Commands

Head `3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45`. `THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b` and `CORE.md` blob `dbf0d2322ce9fe751a5359e85859ca6f9448ec66` match the fork base `d2aeb8100e22870dc5aee2529356de970c82a820`. NumPy 1.26.4. The independent exponential below does not use the author's Hermitian diagonalization.

```
sha256sum theory/ctc-fixed-point-2026-11-24/PREREG.md
git rev-parse f18721fc852f83a6154aa50186cbbdb876fe0ad9^ 3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45^
git diff f18721fc852f83a6154aa50186cbbdb876fe0ad9 HEAD -- theory/ctc-fixed-point-2026-11-24/PREREG.md
python3 theory/ctc_fixed_point_checks/ctc_fixed_point_checks.py   # twice
python3 tools/check_consistency.py
python3 -m pytest -q
```

`sha256sum` matches the locked digest. The preregistration's parent is `d2aeb8100e22870dc5aee2529356de970c82a820`. The score's parent is the preregistration. `git diff` on `PREREG.md` between those two commits is empty. The script, the stored stdout, `DEVIATIONS.md`, `MEMO.md`, and `RUN_LOG.md` first appear in the score commit. Two reruns of the script matched the stored stdout byte for byte, and matched each other.

`python3 tools/check_consistency.py`: RESULT PASS. Maintained-doc wording count 0. Frozen-record INFO count 29, the same count the run log names.

`python3 -m pytest -q`, with no `--ignore`: 292 passed, 1 skipped, in 476.20s. Pytest 9.2.0, SciPy 1.18.1, SymPy 1.14.0, numba 0.68.1 were installed for that run. The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). The run log's `--ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` was the command used when numba was absent. With numba present that ignore is unnecessary: `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py` imports, and the collected total stays 292 passed, 1 skipped. The tracked `test_result.json` was not left modified.

## Lock

| Commit | Committer time | What landed |
|---|---|---|
| `f18721fc852f83a6154aa50186cbbdb876fe0ad9` | 2026-11-24T21:14:59Z | `PREREG.md` only. Commit message carries the sha256. |
| `3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45` | 2026-11-24T21:26:15Z | script, stdout, memo, run log, deviations, sha file, the pytest, the two index lines |

The preregistration precedes the score by about eleven minutes and was not edited. `DEVIATIONS.md` is a single add in the score commit. No later commit appends or rewrites it. It says no deviation was appended and no bar was moved. That is append-only in the only sense the history can show: there is no second edit. Breach check: none.

The score commit is after upstream PR #261. `MEMO.md:7` still uses the outcome label that `PROCESS.md` §2 retires. The three occurrences in `PREREG.md` (`:13`, `:132`, `:164`) are inside the locked file and stay. Location of the memo line: `process`. Stake: low. Update: none yet. This review does not edit the memo.

## Independent recomputation

The author's module was not imported. The Heisenberg unitary was built in the Bell basis. The eigenvalues of \(a\,XX+b\,YY+c\,ZZ\) are \(a-b+c\), \(-a+b+c\), \(a+b-c\), and \(-a-b-c\) on \(|\Phi^+\rangle,|\Phi^-\rangle,|\Psi^+\rangle,|\Psi^-\rangle\), and \(U=\exp[-i(a\,XX+b\,YY+c\,ZZ)/2]\) multiplies each Bell vector by \(\exp(-i\lambda/2)\). That matrix matches a Hermitian diagonalization of the same generator to \(8.4\times 10^{-17}\) after one global phase. Partial traces are index sums. Singular values are square roots of the eigenvalues of \((M-I)^\top(M-I)\), not a call to the author's SVD helper.

**Gate family for the 20/64 count.** \(U(a,b,c)=\exp[-i(a\,XX+b\,YY+c\,ZZ)/2]\) with each of \(a,b,c\) in \(\{0,\pi/4,\pi/2,\pi\}\). That is 64 gates, every combination, once. The chronology-respecting input is \(\rho_{CR}=I/2\). The Bloch map \(r\mapsto Mr+d\) is fit from the images of \(r=0\) and the three poles. Non-unique means the smallest singular value of \(M-I\) is below \(10^{-8}\). The bar also requires every non-unique value below \(10^{-8}\) and every unique value above \(0.2\).

On every one of the 64 gates, \(d=0\) to machine noise. The joint state \(I/4\) is invariant, so \(r=0\) is always a fixed point. Non-unique means the fixed set is larger than \(\{I/2\}\).

**Outcome.** 20 gates are non-unique. The largest non-unique singular value is \(5.551\times 10^{-16}\). The smallest unique singular value is \(0.292893218813\), equal to \(1-1/\sqrt{2}\) within \(1.1\times 10^{-16}\). The printed `0.292893` is that quantity at six decimals.

Read off that list, the 20 are exactly the grid points with at least two coordinates equal to 0, or at least two equal to \(\pi\). In units of \(\pi\):

\((0,0,0)\), \((0,0,1/4)\), \((0,0,1/2)\), \((0,0,1)\), \((0,1/4,0)\), \((0,1/2,0)\), \((0,1,0)\), \((1/4,0,0)\), \((1/2,0,0)\), \((1,0,0)\), and \((0,1,1)\), \((1/4,1,1)\), \((1/2,1,1)\), \((1,0,1)\), \((1,1/4,1)\), \((1,1/2,1)\), \((1,1,0)\), \((1,1,1/4)\), \((1,1,1/2)\), \((1,1,1)\).

**Entropy sample, the 149.** This is not a draw. It is the accepted list in `PREREG.md` §7, rebuilt here: every grid gate and every named gate at \(\rho_{CR}=I/2\), with the minimum-norm solution, the two sphere ends when the nullity is 1, and the origin plus the six Pauli poles when the nullity is 3; SWAP at \(|0\rangle,|1\rangle,|+\rangle,I/2\); the six DISC points on the \(z\) segment; the six CNOT\(_C\) points on the \(z\) segment. A point is kept when the trace distance from the CTC image to the trial state is at most \(10^{-8}\). Entropy drops eigenvalues at or below \(10^{-12}\), as in the scored script, and does not renormalize.

**Outcome.** 149 kept, 0 rejected. Maximum \(|\Delta S(\rho_{CTC})|=5.551115123126\times 10^{-16}\). Minimum \(\Delta S(\rho_{CR})=0\) exactly. Thirty of the 149 sit at 0. The largest chronology-respecting change on the list is \(\ln 2\).

**DISC at the completely mixed fixed point.** Both \(\rho_{CR}=|0\rangle\langle 0|\) and \(\rho_{CR}=|+\rangle\langle +|\), with \(\rho_{CTC}=I/2\), have output spectrum \((2\pm\sqrt{2})/4\). The computational-basis probabilities of outcome 0 are \(3/4\) and \(1/4\). Therefore

\[
P_D=h\bigl((2+\sqrt{2})/4\bigr),\qquad I(W;M)=\ln 2-h(3/4),
\]

with \(h\) the binary entropy in nats. Double precision gives \(0.416495530699687\) and \(0.130812035941137\). Printed to twelve digits those are \(0.416495530700\) and \(0.130812035941\). The Bloch matrix is \(\mathrm{diag}(1/\sqrt{2},\,1/\sqrt{2},\,1)\) with offset 0, maximum absolute error \(1.1\times 10^{-16}\).

Depolarizing \(D_\gamma(\rho)=(1-\gamma)\rho+\gamma I/2\) forces the \(z\) coordinate through the factor \(\gamma\). The output state is \(\Phi(I/2)\) and does not depend on \(\gamma\). At the five locked strengths the gap and the mutual information match the two closed forms. At \(\gamma=10^{-6}\) the numerical Bloch solution has \(r_z=1.110\times 10^{-10}\), inside the \(10^{-9}\) band the script uses for "equals \(I/2\)".

**Phase damping.** \(Z_{1/2}\) zeros the transverse Bloch components and leaves \(z\) alone. The pure pairs \((|0\rangle,|0\rangle)\) and \((|+\rangle,|1\rangle)\) stay fixed at trace distances \(0\) and \(1.110\times 10^{-16}\). Both chronology-respecting outputs are pure, so the ratio gap is \(1.110\times 10^{-16}\).

**Contraction.** At \(\gamma=0\) one singular value of \(M-I\) is \(1.1\times 10^{-16}\) and the other two are \(1-1/\sqrt{2}\). At \(\gamma=10^{-6}\) the small singular value of \(I-(1-\gamma)M\) is \(10^{-6}\), above \(10^{-8}\), so the numerical nullity is 0. At \(\gamma=10^{-9}\) that singular value is \(10^{-9}\) and the same cutoff reports a kernel.

**Label-dependent mixture.** CNOT with control on the CTC qubit sends both \((|0\rangle,|0\rangle)\) and \((|1\rangle,|1\rangle)\) to a chronology-respecting output \(|0\rangle\). The equal mixture of the outputs has entropy 0. The equal mixture of the inputs has entropy \(\ln 2\). The difference is \(-\ln 2=-0.693147180560\). The completely mixed selector on each pure input separately raises that qubit's entropy by \(\ln 2\).

**Closed return, two classical branches, no \(8\times 8\) matrix.** Bath energy is \(+1/2\) on \(|0\rangle\) and \(-1/2\) on \(|1\rangle\), from \(H_B=Z/2\). The fair branch \(W=0\) contributes 0. The branch \(W=1\) contributes \(-1\) through the first SWAP and \(+1\) through the second. The fair average through the first SWAP is \(-1/2\). The four-step sum is 0 on both branches. Each branch returns to \((W,0,0)\), so the trace distance is 0 and the net mutual information is 0.

## Attacks tried

The precedent is the acting-loop review (`reviews/acting_loop_2026-11-22/HOSTILE_REVIEW.md:226`), where a zero counter was agreement with expressions already written in the preregistration, and the night-1 physics review (`reviews/night1/REVIEW_PHYSSTAT.md`), where scored passes reproduced identities of the cost. Each locked bar is asked the same question: could the outcome have missed the bar, or is the hit a restatement?

### (a) Circularity

| Bar | Could the outcome have missed? | What the hit is |
|---|---|---|
| P1a | Only for an inexact accepted point. Trace distance \(10^{-8}\) allows an entropy change up to \(h(10^{-8})=1.942\times 10^{-7}\) by the qubit Fannes bound, and that would miss \(10^{-9}\). The sampled points are algebraic fixed points, so the change is roundoff. | **NOT A TEST.** \(\Delta S(\rho_{CTC})=0\) is the fixed-point definition. Entropy is a function of the state. |
| P1b-named | Yes. A wrong matrix element changes the split. | A channel calculation on seven named gates. Not an identity of unitarity. |
| P1b-grid | Yes. A different count misses the bar. See (b). | A tally on one grid. Not an identity. |
| P2-bound | Only if a point is not a product input, not unitary, or not a fixed point, or if the entropy routine is wrong. | **NOT A TEST.** Unitarity, a product input, subadditivity, and \(\rho'_C=\rho_C\). The difference equals the output quantum mutual information, which is nonnegative. |
| P2-illicit | Yes, if either output were not \(\lvert 0\rangle\). | Exact arithmetic on two pure branches. The "not a process" mark is a scope choice. See (c). |
| P3-gap, the value | Yes, if the output spectrum were not \((2\pm\sqrt{2})/4\). | A partial-trace calculation. The twelve digits are that binary entropy. |
| P3-gap, flat in \(\gamma\) | No, once \(r=0\) is the only solution and \(d=0\). Five copies of one state add nothing. | **NOT A TEST** of the contraction paragraph in `PREREG.md` §4. |
| P3-phase | Only if the locked columns were not implemented. The pure states are diagonal, and phase damping does not move diagonal states. | **NOT A TEST** of those columns plus the definition of phase damping. |
| P3-contraction | Not at the locked \(\gamma=10^{-6}\), where the singular value equals \(\gamma\) and sits \(100\times\) above \(10^{-8}\). A locked \(\gamma=10^{-9}\) would miss the nullity clause with the same mathematics. | **NOT A TEST** of "\((1-\gamma)M\) has no eigenvalue 1 for \(\gamma>0\)", inside a cutoff. |
| P4-cycle | Only if CNOT or SWAP were not their own inverses in the code. | **NOT A TEST.** The composition is the identity, so the energy sum, the mutual information, and the trace distance are 0. |
| P4-half | Yes. The sign is the choice that \(\lvert 0\rangle\) is the excited eigenstate of \(Z/2\). The opposite ground state changes the sign. | A one-line energy average. Not implied by the return. |

The script counter bundles the five consistency checks with the five information-bearing hits. A zero counter is not an information count. The memo already marks P1a as the definition and the sign as the subadditivity argument, and it says a definitional match is not evidence. The counter line in the stdout and in `OPEN_WORK.md:125` still leads with the bundle.

### (b) The 20/64 count, gate set, and tolerance

On the exact locked grid the count is stable from a cutoff of \(10^{-15}\) through \(0.29\). The next cluster of unique singular values begins at \(1-1/\sqrt{2}\). A cutoff of \(0.3\) raises the count to 35. The locked pair of tests, non-unique below \(10^{-8}\) and unique above \(0.2\), sits inside the gap. Tolerance is not what produces 20 on this grid.

The angle set is what produces 20. At the same cutoff \(10^{-8}\):

| Angles | Non-unique out of 64 |
|---|---|
| \(\{0,\pi/4,\pi/2,\pi\}\) (locked) | 20 |
| \(\{0,\pi/6,\pi/3,\pi/2\}\) | 10 |
| \(\{0,\pi/3,2\pi/3,\pi\}\) | 20 |
| \(\{0,\pi/2,\pi,3\pi/2\}\) | 20 |
| \(\{0,\pi/4,\pi/2,3\pi/4\}\) | 10 |
| \(\{\pi/4,\pi/2,3\pi/4,\pi\}\) | 10 |
| 64 Haar unitaries, seed 20261124, via QR | 0 (smallest singular value \(0.178766186913\)) |

Shifting every locked angle by \(10^{-4}\) drops the count from 20 to 0 at cutoff \(10^{-8}\): the split singular values sit at \(1.000\times 10^{-8}\), just above the cutoff. The same shift at cutoff \(10^{-6}\) keeps 20. A shift of \(10^{-3}\) does the same at the two cutoffs, with the split values near \(10^{-6}\).

**Model implication.** Twenty of these 64 symmetric gates need a selector. A generic two-qubit gate, and a small rigid shift of this grid, does not reproduce 20. The fraction is not a property of Deutsch's prescription at large.

### (c) The label-dependent \(-\ln 2\)

The number is printed (`ctc_fixed_point_checks.out:10`) and marked not a process on one density operator. It is not hidden.

It is also not \(\Delta S\) of one fixed-point equation. Each branch has \(\Delta S(\rho_{CR})=0\). The \(- \ln 2\) is \(S(\mathbb{E}\rho'_{CR})-S(\mathbb{E}\rho_{CR})\) across two branches whose CTC state is a function of a classical label. The fixed-point equation takes one product operator \(\rho_{CR}\otimes\rho_{CTC}\). A label-dependent CTC state is a correlated preparation, and the product hypothesis of the sign argument does not hold.

Candidate sentence 2 asked for a negative chronology-respecting entropy with no bath. That number is what the sentence points at, and it sits outside the locked map. Inside the locked map the maximum-entropy selector raises the entropy by \(\ln 2\). The author's question on this point is the right question, and the bars do not move.

**Model implication.** Conditional on one product density operator: the chronology-respecting entropy does not go negative, and that sign is the subadditivity argument. Conditional on a CTC state that is allowed to depend on a classical label: the mixture of the two pure CNOT branches changes the chronology-respecting entropy by \(-\ln 2\), with no bath in the circuit. Those are different objects. The hypothesis sentence, read as a sentence about the product model, is the first conditional.

### (d) Route A is not the same gap

Route A is `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md` on `forge-record-ratio-reframes` at `bcb62358abb9aa74f3cbcc2800643c1500100f97`. The lines cited by the note say the following.

- `:12` is \(J=\kappa I(W;M)+\kappa_D P_D+w L\), with \(P_D=\mathbb{E}[D(\rho\|\Phi_\theta(\rho))]\) on the antipodal ensemble of draft #252.
- `:55` is \(P_D=\mathbb{E}[S(\Phi_\theta(\rho))-S(\rho)]\) for one projective measurement.
- `:103` is the difference of two designs that realize one classical channel: direct measurement minus pointer-plus-garbling, equal to \(\kappa_D P_D(\theta)\).
- `:106` says that gap vanishes for every \(\theta\) if and only if \(\kappa_D=0\), and that ratio 1 does not remove the designer's one-way saving.
- `:112` says the same-channel gap equals \(\kappa_D P_D(\theta)\), no cycle forces the ratio, and the endpoint \(\kappa_D=0\) is the refusal of the second coefficient.
- `:114` says the gap is withdrawn when the menu is only one measurement, because the second path is not there.
- `:116` says that, conditional on free classical post-processing and on the kept record being the final outcome, the minimized record cost of a channel does not depend on \(\kappa_D\), and the ratio stays unidentified.

The scored CTC gap is \(J(q=1)-J(q=0)=P_D\) on one design, the DISC loop at the completely mixed fixed point, with \(\kappa=1\) and \(w=0\). That algebra has the same shape as `:103` when \(\kappa_D=\kappa\). The objects differ.

1. Route A \(P_D\) is the entropy of a projective pinch on the antipodal ensemble. The CTC \(P_D\) is the entropy increase of the chronology-respecting qubit under a two-qubit unitary. For DISC the output of \(\lvert 0\rangle\) is \(\begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}\), which is not the dephasing of \(\lvert 0\rangle\).
2. Route A's gap compares two designs. The CTC gap compares two coefficients on one design. There is no garbling path. By `:114`, that is the menu on which the route A gap is not a comparison the designer can make.
3. Route A's minimized cost has slope 0 in \(\kappa_D\). The scored DISC design has slope \(P_D=h((2+\sqrt{2})/4)=0.416495530700\). The signed difference of those slopes is \(+0.416495530700\) nats per unit \(\kappa_D\).
4. If the ratio is minimized on that one design, \(P_D>0\) forces the endpoint \(q=0\). `:112` already separates that endpoint from the sentence that the ratio stays unidentified.
5. If both the pure fixed points and the completely mixed fixed point are admissible designs, their costs cross. The pure pair has mutual information \(\ln 2\) and \(P_D=0\). The mixed point has mutual information \(\ln 2-h(3/4)\) and \(P_D=h((2+\sqrt{2})/4)\). The pure pair is the cheaper record when

\[
q=\frac{\kappa_D}{\kappa}>\frac{h(3/4)}{h((2+\sqrt{2})/4)}=1.350158892880.
\]

Below that value the mixed point is cheaper, and its cost still depends on \(q\). Deutsch's maximum-entropy selector refuses the pure pair, which returns the problem to item 4.

**Model implication.** The loop does not supply the reverse leg route A says is missing, and \(\Delta S(\rho_{CTC})=0\) is not that leg. That negative statement is right, and it is not a recomputation of `:103`. The sentence that the route A gap is not undercut compares two different slopes.

### (e) Classical and modeling assumptions

These are assumptions of the toy, not results of the run.

- The mutual information in \(J\) is the Shannon mutual information of a computational-basis measurement. On the mixed DISC pair the quantum mutual information of the output equals \(P_D=0.416495530700\), because \(\Delta S(\rho_{CTC})=0\). The computational-basis number is \(0.130812035941\). The cost prices the smaller one. The difference is \(0.285683494759\).
- \(w=0\), so the stake term does not move \(J\). The ratio gap then equals \(P_D\) by algebra, for any \(I\) and any \(L\).
- The fixed-point equation is a product input. That is Deutsch's prescription, and it is the step that places the label-dependent mixture outside the sign bar.
- The bath in P4 is a pure qubit prepared in the excited eigenstate of \(Z/2\), not a Gibbs state at temperature 1. The symbol \(T=1\) is a label. \(\sum\Delta E_B/T\) is not a Clausius sum and not a Landauer heat. On the open prefix the fair energy change is \(-1/2\) while the \(W=1\) branch takes the bath from a pure excited state toward a correlated state. A thermal reservoir at positive temperature would be biased toward the ground state.
- P4's registers are the world bit, the memory, and that bath. The CTC qubit is not in the circuit. The four gates are CNOT, SWAP, SWAP, CNOT. **Model implication.** The integrated floor 0 is Bennett uncomputation on that triple. It is the same vanishing the revival note already records, which the memo says. It is not a property of the Deutsch fixed point.
- The world bit in P4 is diagonal. One bath and one temperature label are locked. The memo already says a second temperature label need not sum to 0.
- Eigenvalues at or below \(10^{-12}\) are dropped before the logarithm.

### What is new, and what is known

Known, and marked as such by the note where it says so: \(\Delta S(\rho_{CTC})=0\) at a fixed point; the nonnegative chronology-respecting sign from unitarity, a product input, and subadditivity; existence of some fixed point for a continuous map of the Bloch ball; non-uniqueness for some channels, and a maximum-entropy choice among solutions, in Deutsch's prescription; the route A coefficient algebra, as an algebra; Reeb and Wolf's equality for a unitary on a system and an initially thermal reservoir, which this loop does not meet; Landauer's tie between heat and irreversible erasure; a reversible return with net energy change 0; the revival note's vanishing keep-cost.

Computed here, on this toy, and not taken from the four papers: the partition 20/64 on this Heisenberg grid and the singular-value gap from \(5.551\times 10^{-16}\) to \(1-1/\sqrt{2}\); the DISC spectrum \((2\pm\sqrt{2})/4\) and the two nats \(0.416495530700\) and \(0.130812035941\); the contrast that depolarizing selects the mixed point while phase damping keeps the pure points; the open-prefix sum \(-1/2\) for this excited pure bath.

Not a new constraint on the record-price ratio. The comparison that would have been new, a second design set beside route A's garbling path, is not in the score.

## Ledger

Lock reference: `forge-ctc-fixed-point` `f18721fc852f83a6154aa50186cbbdb876fe0ad9`, scored at `3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45`. Logged at 2026-11-24 16:50 ET. Breach check for the lock: none.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT + info) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| P1a | \(\lvert\Delta S(\rho_{CTC})\rvert\le 10^{-9}\) on the accepted list; 0 rejections | max \(5.551\times 10^{-16}\); \(n=149\); rejections 0 | HIT, residual \(+5.551\times 10^{-16}\) inside the band. About 0 information. **NOT A TEST** / consistency check of the fixed-point definition. A point accepted only at trace distance \(10^{-8}\) could have reached \(1.942\times 10^{-7}\) and missed | model | low | none yet | none |
| P1b-named | non-unique \(\{I,\mathrm{CNOT}_{CR},\mathrm{CNOT}_C,\mathrm{CZ},\mathrm{DISC}\}\); unique \(\{\mathrm{SWAP},\mathrm{DCNOT}\}\) at \(I/2\) | that split | HIT. Could have missed. Not an identity | model | low | none yet | none |
| P1b-grid | exactly 20/64; non-unique singular value \(<10^{-8}\); unique \(>0.2\) | 20/64; non-unique max \(5.551\times 10^{-16}\); unique min \(0.292893218813\) | HIT. Gap margin \(0.292893218813\). Could have missed. Not an identity | model | medium | none yet | none |
| P2-bound | \(\Delta S(\rho_{CR})\ge -10^{-9}\) on the accepted list | minimum 0 | HIT. The minimum is \(+10^{-9}\) above the floor and sits on 0. About 0 information. **NOT A TEST** / consistency check of unitarity, a product input, subadditivity, and the fixed point | model | low | none yet | none |
| P2-illicit | mixture difference \(-\ln 2\) within \(10^{-9}\); selector change \(+\ln 2\) within \(10^{-9}\); not one process | \(-0.693147180560\) and \(+0.693147180560\) | HIT, residual 0 at twelve digits. Could have missed. The exclusion is the scope in attack (c) | model | medium | none yet | none |
| P3-gap | unique \(I/2\); gap \(h((2+\sqrt{2})/4)\) within \(10^{-8}\) and \(>0.1\); \(I=\ln 2-h(3/4)\) within \(10^{-8}\); five \(\gamma\) | both closed forms at all five \(\gamma\); \(r_z=1.110\times 10^{-10}\) at \(\gamma=10^{-6}\) | HIT. Margin above 0.1 is \(+0.316495530700\). The value could have missed. Flatness in \(\gamma\) is **NOT A TEST** | model | medium | none yet | none |
| P3-phase | both pure points fixed within trace distance \(10^{-9}\); gap 0 within \(10^{-9}\) | distances 0 and \(1.110\times 10^{-16}\); gap \(1.110\times 10^{-16}\) | HIT. About 0 information. **NOT A TEST** / consistency check of the locked columns and of phase damping on a diagonal state | model | low | none yet | none |
| P3-contraction | nullity at least 1 at \(\gamma=0\); nullity 0 at \(\gamma=10^{-6}\) | 1, then 0; the small singular value equals \(\gamma=10^{-6}\) | HIT. About 0 information. **NOT A TEST** of the contraction. The same rule at \(\gamma=10^{-9}\) reports a kernel | model | low | none yet | none |
| P4-cycle | absolute energy sum, net learning, and trace distance each \(\le 10^{-12}\) | 0, 0, 0 | HIT. About 0 information. **NOT A TEST** / consistency check that CNOT twice and SWAP twice are the identity | model | low | none yet | none |
| P4-half | open-prefix sum \(-1/2\) within \(10^{-12}\) | \(-1/2\) | HIT, residual 0. Could have missed: the sign is \(H_B=Z/2\) with \(\lvert 0\rangle\) excited | model | low | none yet | none |
| route-A-id | prose claim that the scored gap is the route A same-channel gap and is not undercut. Not a locked numeric bar | one-design slope \(0.416495530700\); route A minimized slope 0 | miss \(+0.416495530700\) nats per unit \(\kappa_D\). See attack (d) | model | high | none yet | none |

## DOIs

Crossref `GET /works/<doi>` on 24 November 2026, HTTP 200 for each.

| DOI | Crossref | Note |
|---|---|---|
| `10.1103/PhysRevD.44.3197` | David Deutsch, "Quantum mechanics near closed timelike lines", Physical Review D 44, pages 3197-3217, issued 15 November 1991 | matches |
| `10.1088/1367-2630/16/10/103011` | David Reeb and Michael M Wolf, "An improved Landauer principle with finite-size corrections", New Journal of Physics 16, 103011, issued 8 October 2014 | matches. The note prints a period in the middle initial. No page of the article is used, and the theorem is not instantiated |
| `10.1147/rd.53.0183` | R. Landauer, "Irreversibility and Heat Generation in the Computing Process", IBM Journal of Research and Development 5, pages 183-191, issued July 1961 | matches |
| `10.1103/PhysRevLett.102.210402` | Todd A. Brun, Jim Harrington, and Mark M. Wilde, "Localized Closed Timelike Curves Can Perfectly Distinguish Quantum States", Physical Review Letters 102, article 210402, issued 27 May 2009. The page field is empty | matches. The note claims no page. The unitary in the note is not claimed to be their circuit |

No number in the score is taken from these four records.

## Findings

1. **The route A identification does not hold.** `theory/ctc-fixed-point-2026-11-24/MEMO.md:13` and `:51-55`, `PREREG.md:59-60`, `OPEN_WORK.md:125`. The scored gap is the coefficient difference on one DISC design. Route A's gap is a dominance between two designs of one classical channel, and on that menu the minimized cost does not depend on \(\kappa_D\). The signed slope gap is \(+0.416495530700\). This blocks reading T85 as a test of route A. It does not move the ten locked bars.

2. **Five of the ten bars are consistency checks.** P1a, P2-bound, P3-phase, P3-contraction, and P4-cycle. The flatness in \(\gamma\) inside P3-gap is a sixth. They are labeled **NOT A TEST** above. The information-bearing hits are the named split, the 20/64 tally, the \(-\ln 2\) arithmetic, the DISC spectrum, and the open-prefix sum \(-1/2\). The update is this ledger. The locked file is not rewritten.

3. **The \(-\ln 2\) mixture is reported, and it is outside the product equation.** Keeping it out of P2-bound is the right scope for the locked map. It leaves candidate sentence 2 unanswered for a label-dependent preparation. That is the open question already written on the draft. No bar moves.

4. **The count 20 is exact on the locked grid and is not stable under a change of grid.** See attack (b). The bar that was locked is the bar that was scored.

5. **P4 does not contain the CTC qubit.** The zero floor is the identity of a reversible circuit on a pure excited bath. **Model implication.** It does not price the Deutsch loop.

## Wording of the new T85 files

The hypothesis sentence is byte-identical in `PREREG.md:17`, `MEMO.md:11`, and `OPEN_WORK.md:125`. The notes call the construction a toy model of Deutsch's fixed-point prescription and say it is not a claim about physical time travel. They do not derive general relativity, quantum mechanics, holography, or gravity. The record term is called a cost. The memo line recorded under Lock uses the outcome label retired after the preregistration was locked.

Blockers remaining: 1
