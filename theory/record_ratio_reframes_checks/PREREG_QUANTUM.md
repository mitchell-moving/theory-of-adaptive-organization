# T76 preregistration: ratio 0 on quantum records

*Tuesday 24 November 2026 (UTC). Written and committed before `quantum_record_checks.py` and before any quantum-record grid. Branch `forge-record-ratio-reframes`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Earlier locks are not edited. Locked by sha256 in `PREREG_QUANTUM.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\).

## 0. Question

Routes A and B, and the H1 bound \(J^\star(q)\ge J^\star(0)\) for \(q\ge 0\), select ratio \(0\) on a projective measurement plus a classical garbling. Do those selections use the classical character of the record? The same questions are asked of three quantum records: a non-commuting unsharp POVM, a coherent post-measurement state that is measured again, and the mixed rank-2 block from review 1.

## 1. Prior exposure

- H1 on the projective antipodal menu: at fixed \(\theta\), \(J\) is linear in \(q\) with slope \(\kappa P_D\ge 0\), so the joint minimum on \(q\ge 0\) sits at \(0\). That algebra is the definition of \(J\). It is a check on each new menu, not a new forecast.
- Route A: pointer measurement plus a binary symmetric channel reproduces the projective \(\theta\)-channel on the dephased antipodal ensemble, and the cost gap is \(\kappa_D P_D\). Adopted from T75. The new claim is whether that reproduction survives when the target instrument does not commute with the pointer and the kept object is the quantum state.
- Route B: \(P_D=0\) at the projective pointer, so every ratio matches a price of \(I\) there; \(P_D>0\) off the pointer forces \(\kappa_D=0\) if the match is required at every angle. Adopted from T75. The new claim is whether an unsharp instrument still has an angle with \(P_D=0\).
- Review 1 at `21ab5f0`: the mixed rank-2 block has \(P_D=0\), \(I=0\), and the ledger sides differ by \(\tfrac12\ln 2\).
- Hand evaluation, not this lock's grid. Unsharp effects \(E_\pm=(I\pm\eta n\cdot\sigma)/2\) at \(\eta=1/2\). The Lüders channel keeps the Bloch component along \(n\) and multiplies the perpendicular part by \(\gamma=\sqrt{1-\eta^2}=\sqrt{3}/2\). On ANT, \(r=0.6\), a 19-point sample of the entropy disturbance has minimum about \(0.0254\). The locked bar is \(0.02\). The commutator \([E_+(z),E_+(x)]\) has Frobenius norm \(\eta^2/\sqrt{2}=0.176776695297\).

## 2. Model

ANT, four labels, Bloch length \(r=0.6\), no prior dephasing. \(\kappa=1\), \(w=1\), \(\phi=0\). Grid \(721\) points on \([0,\pi/2]\). Tie \(10^{-9}\). `SEED = 20261124` is set and not drawn from.

Unsharp instrument, sharpness \(\eta=1/2\). Outcome probability \((1\pm\eta\, r\cdot n)/2\). Disturbance \(P_D=\mathbb{E}[S(\Phi(\rho))-S(\rho)]\), where \(\Phi\) is the unconditional Lüders channel above. \(I\) is the Shannon mutual information of the binary outcome. \(L\) is the mean squared error of \(y\), the same stake coordinate as in `PREREG.md`.

Second measurement: Lüders state conditional on the first outcome, then the same unsharp instrument on an axis. The conditional mutual information is \(I(W;M_2\mid M_1)\).

Rank-2, review block: state \(\mathrm{diag}(1/2,1/4,1/4)\), projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\). One state, so \(I=0\).

Rank-2, coherent block: the same instrument on
\[
\rho=\begin{pmatrix}1/2&0&0\\0&1/4&1/8\\0&1/8&1/4\end{pmatrix}.
\]
One state, so \(I=0\). \(P_D=S(\Phi(\rho))-S(\rho)\).

## 3. Predictions

**Q-comm.** The Frobenius norm of \([E_+(z),E_+(x)]\) equals \(0.176776695297\) within \(10^{-9}\), and is \(>0.1\).

*Fails if* the absolute gap is \(\ge 10^{-9}\) or the norm is \(\le 0.1\). Then these two effects commute at the printed precision, and the menu is not a non-commuting POVM. Report the norm.

**Q-slope.** On the \(721\)-grid, every entropy disturbance is \(>0.02\). For \(q\in\{0.5,1,2\}\), \(J^\star(q)\ge J^\star(0)-10^{-9}\).

*Fails if* any disturbance is \(\le 0.02\), or any ratio undershoots \(J^\star(0)\) by \(\ge 10^{-9}\). Then this quantum menu has a nonpositive disturbance or a ratio above \(0\) that lowers the cost. Report the cell. Do not drop the bar to the hand sample.

**Q-pointer.** \(P_D(0)>0.02\) and \(P_D(\pi/2)>0.02\).

*Fails if* either is \(\le 0.02\). Then the unsharp instrument still has a pointer where every ratio matches a price of \(I\) alone, which is Route B's pointer clause. Report the two values.

**Q-garble.** Projective \(z\) followed by a binary symmetric channel of any crossover leaves both \(x\)-labels at outcome probability \(1/2\). The unsharp \(x\)-instrument has \(P(M=+1\mid +x)=(1+\eta r)/2=0.65\). The gap is \(0.15\). The check uses crossovers \(\{0,0.25,0.5\}\) and requires every gap \(>0.1\).

*Fails if* any crossover matches \(+x\) within \(0.1\). Then a classical garbling of the pointer reproduces the non-commuting instrument's outcome law, and Route A's comparison is available. Report the crossover and the gap.

**Q-state.** On the \(+x\) label, the unconditional state after the unsharp \(x\)-instrument and the unconditional state after a projective \(z\)-instrument have trace distance \(>0.2\).

*Fails if* the distance is \(\le 0.2\). Then the quantum records of the two paths agree closely enough that Route A is comparing one behavior. Report the distance.

**Q-reuse.** First axis \(z\), second axis \(x\), both unsharp. \(I(W;M_2\mid M_1)>0.05\). The sum of the two disturbances is \(>0.02\). At \(q\in\{0,1,2\}\), with the cost \(I(W;M_1,M_2)+q\,P_{D,\mathrm{total}}+w L_2\) and \(L_2\) the loss of the second outcome alone, the minimum is at \(q=0\) and the other two costs exceed it by \(>0.01\).

*Fails if* the conditional information is \(\le 0.05\), the added disturbance is \(\le 0.02\), or \(q=1\) or \(q=2\) comes within \(0.01\) of \(q=0\). A small conditional information means the post-measurement state did not carry a reusable record. A ratio above \(0\) that matches \(q=0\) means the second quantum record has stopped selecting ratio \(0\). Report the three numbers.

**Q-rank.** On the review block, \(|P_D|<10^{-12}\), \(|I|<10^{-12}\), and the ledger gap equals \(\tfrac12\ln 2\) within \(10^{-9}\). The costs at \(q=0\) and \(q=1\) differ by \(<10^{-12}\).

*Fails if* \(|P_D|\ge 10^{-9}\), the gap misses by \(\ge 10^{-6}\), or the two costs differ by \(\ge 10^{-9}\). Then the mixed block has a slope, and ratio \(0\) is selected rather than tied. Report the values.

**Q-coh.** On the coherent block, \(P_D>0.01\) and the cost at \(q=1\) exceeds the cost at \(q=0\) by \(>0.01\).

*Fails if* \(P_D\le 0.01\) or the cost gap is \(\le 0.01\). Then coherence inside the rank-2 block is not a disturbance this instrument prices, and ratio \(0\) is not selected by a positive slope. Report both numbers.

## 4. What this run will not say

It will not edit `THEORY.md`, the earlier locks, or the stored `.out` files of those locks. It will not say the ratio has been solved. A line that misses is a puzzle at the instrument named in that line. The H1 algebra is not a derivation that every quantum record has \(P_D\ge 0\); Q-slope and Q-coh are the checks of that sign.

## 5. Output

One line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test.
