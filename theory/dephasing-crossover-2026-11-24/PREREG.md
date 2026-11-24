# PREREG: phase holding under dephasing, and the pointer-split cost

*Tuesday 24 November 2026 (UTC). Written and committed before any results script and before any stored output. Branch `forge-dephasing-crossover`, cut from fork `main` `d2aeb8100e22870dc5aee2529356de970c82a820`. `THEORY.md` and `CORE.md` are not edited. This file is locked by the commit that adds it. A later change to a prediction, a bar, or a grid is a deviation and is appended in `DEVIATIONS.md`. Open-work id **T84**. Self-check, not an independent review.*

Can it fail: the respecting projectors can move the coherent block, the crossing destruction can fall as the off-diagonal grows, the stock-cost crossover can sit on the other side of \(h(\varepsilon)/\varepsilon\), and the one-time-write reading can fail to be the \(\gamma\tau\)-only null.

Cheapest way to fail it: one qutrit block, one qubit, three record designs, closed forms checked against the matrices. No bath Hilbert space and no Monte Carlo.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. The qubit, the qutrit, and the dephasing channel are inputs. A miss is a puzzle. The record price is a cost.

## 0. Question

Phase storage is free of ongoing destruction only when no coherence crosses the pointer split. With a dephasing rate \(\gamma\), a phase held for a time \(\tau\) meets that split. The cost is the one named in T73 and left with a free ratio in T74,

\[
J=\kappa I+q\kappa P_D+w L,
\]

with \(q=\kappa_D/\kappa\ge 0\) (`theory/pointer-basis-stakes-2026-11-24/MEMO.md:64-68`; `theory/QUANTUM_RECORD_PRICE_2026-11-24.md:9-15`). Ruin stays outside the sum (`CORE.md:27`, `CORE.md:66`). Two questions:

- **(a)** Does this cost name a price for keeping a phase memory at dephasing rate \(\gamma\) over horizon \(\tau\)?
- **(b)** Does it name a crossover, in \((\gamma,\tau,w)\), at which a classical record in the pointer basis is cheaper than holding the phase?

The crossover counts only if it is not the plain-decoherence null in §4. A third question is locked from draft #257 / T76, below, and is scored as a clue whichever way it falls.

## 1. Why this approach

The stock \(\kappa I\) and the stake \(w L\) are the memory and error terms of the five-term display (`CORE.md:35`). In the proved class the stock rental is not the coordinate: the bath heat replaces it, and a frozen record has vanishing ongoing heat after a one-time write (`CORE.md:39`, `CORE.md:78`). Those are two readings of the same bit. Scoring both separates a stake boundary from the null, which is "any noise, and the pointer record is strictly cheaper for every positive stake."

\(P_D\) is the entropy produced by the record map, \(S(\Phi(\rho))-S(\rho)\), the disturbance used on the quantum menu of T76 (`theory/record_ratio_reframes_checks/PREREG_QUANTUM.md:35` on `forge-record-ratio-reframes` at `40c4060`). T73's projective price is the Umegaki form, equal to that entropy gap for a pinching map (`theory/pointer-basis-stakes-2026-11-24/PREREG.md:28-31`). A8 only requires the coefficient to be nonnegative (`CORE.md:52`). This note does not derive \(q\).

Draft #257 scored Q-coh twice. The lock named projectors \(P_0=|0\rangle\langle 0|\) and \(P_1=|1\rangle\langle 1|+|2\rangle\langle 2|\) on

\[
\rho=\begin{pmatrix}1/2&0&0\\0&1/4&1/8\\0&1/8&1/4\end{pmatrix}
\]

(`PREREG_QUANTUM.md:31-35`; `quantum_record_checks.py:281-283`). Those projectors leave the block fixed, so \(P_D=0\) and the costs at \(q=0\) and \(q=1\) agree. The re-score is `Q-coh FAIL PD=0.000000 cost_gap=0.000000` (`quantum_record_checks.out:14-16`, `:24`; `DEVIATIONS.md:19-23`). The first script printed `Q-coh PASS PD=0.065406 cost_gap=0.065406` (`quantum_record_checks.out:8`). That figure is the entropy gap from this state to \(\mathrm{diag}(1/2,1/4,1/4)\), eigenvalues \((1/2,3/8,1/8)\) against \((1/2,1/4,1/4)\) (`DEVIATIONS.md:23`). The memo records the miss (`theory/RECORD_RATIO_REFRAMES_2026-11-24.md:85`). The prediction that missed was \(P_D>0.01\) (`PREREG_QUANTUM.md:67`). A miss there is a puzzle at that instrument (`PREREG_QUANTUM.md:73`).

The clue taken from that pair, and locked here as a hypothesis, is: destruction \(P_D\), and with it the destruction piece of \(J\), is zero when the pointer split respects the coherent subspace, and positive and increasing in the coherence the split cuts when the split crosses that subspace. Under dephasing at rate \(\gamma\), the \(\gamma\)-dependence of the pointer-record destruction is exactly the decay of the coherence that crosses the pointer split. The full price \(J\) of a respecting record is a separate claim and is not assumed to vanish.

T73 already shows that, at complete dephasing, the relative-entropy minimizer on its ensemble is the dephasing axis for every stake (`MEMO.md:19`). That slice has no horizon \(\tau\). This note asks the horizon question. It does not rescore T73 and it does not rescore Q-coh.

## 2. Model (class DP)

\(\kappa=1\) in the scored units. Stake \(w\ge 0\) is in those units. \(q\) is an input, not a result. Ruin is slack, as in T73 (`PREREG.md:36`): the cap is not in the sum. One Hamming decision at time \(\tau\). Binary entropy \(h\) is in nats, \(h(0)=h(1)=0\).

**Channel, an input.** Pure dephasing in the computational basis multiplies every off-diagonal by \(e^{-\gamma t}\) and leaves populations fixed. \(\gamma\) is a rate. T73 used the symbol \(\gamma\) for a surviving Bloch factor. Here the surviving factor is \(r=e^{-\gamma\tau}\).

**Phase bit.** \(B\in\{0,1\}\) uniform, encoded as the \(\sigma_x\) eigenstates. After time \(\tau\) the Bloch vectors are \((\pm r,0,0)\).

**Design H, respecting read.** At time \(\tau\), measure \(\sigma_x\). The projectors are the spectral projectors of the remaining state.

**Design P, pointer encoding.** At \(t=0\), rotate the bit onto a \(\sigma_z\) eigenstate and hold it. Read \(\sigma_z\) at time \(\tau\). Populations are invariant.

**Design Z, T73 pointer pinch.** Leave the phase encoding in place and, at time \(\tau\), measure \(\sigma_z\).

**Qutrit block.** The state and the two splits from #257. Coherence parameter \(c\in[0,1/4]\),

\[
\rho(c)=\begin{pmatrix}1/2&0&0\\0&1/4&c\\0&c&1/4\end{pmatrix}.
\]

The locked state is \(c=1/8\). Respecting split: \(P_0=|0\rangle\langle 0|\), \(P_1=|1\rangle\langle 1|+|2\rangle\langle 2|\), Lüders map \(\Phi_R(\rho)=P_0\rho P_0+P_1\rho P_1\). Crossing family: multiply the block off-diagonal by \(\alpha\in[0,1]\) (phase damping inside the block). \(\alpha=1\) removes nothing. \(\alpha=0\) is the fully dephased diagonal. One state, so \(I=0\). No stake coordinate is defined on this block (`PREREG_QUANTUM.md:35`), so \(L=0\) and \(J=q\kappa P_D\) here. That reduction is part of the model.

**Grids.** \(\gamma\tau\in\{0,0.01,0.1,0.5,1,2,5,20\}\), \(w\in\{0,0.5,1,2,5,20\}\), \(q\in\{0,0.5,1,2\}\), \(c\in\{0,0.05,0.125,0.2,0.25\}\), \(\alpha\in\{1,0.75,0.5,0.25,0\}\) at \(c=1/8\), and \(\theta\in\{0,\pi/6,\pi/4,\pi/3,\pi/2\}\) at \(r\in\{1,0.5,0.1\}\). Deterministic. `SEED = 20261124` is set and not drawn from.

### Closed forms (part of the model)

Write \(\varepsilon=(1-r)/2\) and \(\chi(r)=\ln 2-h((1+r)/2)\). For the phase bit,

\begin{align*}
I_H&=\chi(r),& P_{D,H}&=0,& L_H&=\varepsilon,\\
I_P&=\ln 2,& P_{D,P}&=0,& L_P&=0,\\
I_Z&=0,& P_{D,Z}&=\chi(r),& L_Z&=1/2.
\end{align*}

So \(J_H=\kappa\chi(r)+w\varepsilon\), \(J_P=\kappa\ln 2\), and \(J_Z=q\kappa\chi(r)+w/2\).

A projective measurement at angle \(\theta\) from the dephasing axis, on a state of Bloch length \(r\) along \(x\), has

\[
P_D(\theta)=h\big((1+r|\sin\theta|)/2\big)-h((1+r)/2).
\]

On the qutrit, the respecting map fixes \(\rho(c)\), so \(P_D=0\). The crossing map at damping \(\alpha\) has eigenvalues \(1/2\), \(1/4+\alpha c\), \(1/4-\alpha c\), and

\[
P_D(\alpha)=S(\Phi_\alpha(\rho))-S(\rho(c)).
\]

At \(\alpha=0\) and \(c=1/8\) this is the gap between eigenvalues \((1/2,1/4,1/4)\) and \((1/2,3/8,1/8)\).

## 3. Predictions

Each line fails on the input named with it. The script does not drop a cell.

**P1, encoding crossover.** For \(\varepsilon>0\), design P is strictly cheaper than design H if and only if

\[
\frac{w}{\kappa}>\frac{h(\varepsilon)}{\varepsilon},\qquad \varepsilon=\frac{1-e^{-\gamma\tau}}{2}.
\]

At \(\gamma\tau=0\) the two costs are equal. *Fails if* any grid cell has the opposite strict sign, or a tie where the inequality is strict by more than \(10^{-9}\) in the stake gap.

**Shape of P1.** \(t(\varepsilon)=h(\varepsilon)/\varepsilon\) is strictly decreasing on \(\{10^{-4},10^{-3},10^{-2},0.05,0.1,0.2,0.4,1/2\}\). The limit \(\gamma\tau\to 0^+\) is above every finite stake: \(t(10^{-4})>8\). The limit \(\gamma\tau\to\infty\) is \(t(1/2)=2\ln 2\), absolute error \(\le 10^{-12}\). Therefore a stake \(w/\kappa\le 2\ln 2\) never makes P strictly cheaper at a finite \(\tau\), and a stake above \(2\ln 2\) has exactly one crossover time

\[
\tau_\times(\gamma,w)=\gamma^{-1}\ln\frac{1}{1-2\varepsilon_\times},
\]

where \(\varepsilon_\times\in(0,1/2)\) is the unique root of \(h(\varepsilon)/\varepsilon=w/\kappa\). *Fails if* the sample is not strictly decreasing, the endpoint misses \(2\ln 2\), or \(t(10^{-4})\le 8\).

**P2, pointer pinch.** For \(q<1\) and \(r>0\), design Z is strictly cheaper than design H if and only if

\[
\frac{w}{\kappa}<\frac{2(1-q)\,\chi(r)}{r},\qquad r=e^{-\gamma\tau}.
\]

For \(q\ge 1\), Z is not strictly cheaper at any grid cell with \(w\ge 0\). *Fails if* a cell has the opposite strict sign.

**Shape of P2.** For fixed \(q\in[0,1)\), the threshold falls as \(\gamma\tau\) rises: \(\chi(r)/r\) is strictly increasing on \(\{0.05,0.2,0.5,0.9,1\}\), from a value below \(0.03\) at \(r=0.05\) to \(\ln 2\) at \(r=1\). *Fails if* that sample is not strictly increasing, or \(\chi(1)\) misses \(\ln 2\) by \(\ge 10^{-12}\).

**P3, \(q\) on the eigenbasis records.** \(J_H\) and \(J_P\) do not change with \(q\). *Fails if* any two values of \(q\) move either cost by \(\ge 10^{-12}\).

**P4, price of holding the phase.** The price asked in (a), for design H, is

\[
J_H(\gamma,\tau,w)=\kappa\,\chi(e^{-\gamma\tau})+w\,(1-e^{-\gamma\tau})/2.
\]

The excess over the noiseless box (\(\gamma\tau=0\), cost \(\kappa\ln 2\)) is \(\Delta=w\varepsilon-\kappa h(\varepsilon)\). Then \(\Delta=0\) at \(\gamma\tau=0\), and for \(\varepsilon>0\) the sign of \(\Delta\) is the sign of \(w/\kappa-h(\varepsilon)/\varepsilon\). *Fails if* a grid cell disagrees by \(\ge 10^{-9}\).

**P5, the null reading.** Charge \(\kappa\ln 2\) once to both encodings and then only the stake, which is the frozen-record reading (`CORE.md:78`): \(J_H^{\mathrm{write}}=\kappa\ln 2+w\varepsilon\) and \(J_P^{\mathrm{write}}=\kappa\ln 2\). For every \(w>0\) and \(\gamma\tau>0\), P is strictly cheaper, and the costs tie if \(w=0\) or \(\gamma\tau=0\). The strict winner does not depend on how large the positive stake is. *Fails if* any such cell disagrees. This line is the plain-decoherence null. It is scored so the stock formula can be told apart from it. A pass of P5 does not make P1 a pass.

**Q1, respecting split.** On \(\rho(c)\) for every locked \(c\), the #257 projectors give \(\Phi_R(\rho)=\rho\), so \(P_D=0\) within \(10^{-12}\), and \(J=0\) within \(10^{-12}\) for every locked \(q\). *Fails if* any cell has \(|P_D|\ge 10^{-9}\) or \(|J|\ge 10^{-9}\).

**Q2, crossing split.** At \(c=1/8\), \(P_D(\alpha)\) is strictly increasing as \(\alpha\) runs down the locked list, \(P_D(1)=0\) within \(10^{-12}\), and

\[
\big|P_D(0)-0.065406\big|\le 5\times 10^{-7}.
\]

The same \(P_D(c)\) at \(\alpha=0\) is strictly increasing in the locked \(c\), and \(P_D(0)=0\). At \(q=1\), \(J=P_D\). *Fails if* the six-digit gap misses, or either sample is not strictly increasing.

**Q3, the price does not vanish with \(P_D\).** On design H, \(P_{D,H}=0\) at every locked \((\gamma\tau,w)\), and every cell with \(\gamma\tau=0\) has \(J_H=\kappa\ln 2\). *Fails if* any cell has \(P_{D,H}\ge 10^{-9}\), or any \(\gamma\tau=0\) cell misses \(\kappa\ln 2\) by \(\ge 10^{-9}\). A pass means \(P_D=0\) while the price is a positive information rent. The parenthetical "the GTAO price is zero whenever the split respects the subspace" is then false for this phase bit. That outcome is a clue, not a dropped question.

**Q4, holding and the crossing coherence.** For the pure phase bit, \(S(\rho(0))=0\) and, at every locked \(\gamma\tau\),

\[
S(\rho(\tau))+P_{D,Z}(\tau)=\ln 2
\]

within \(10^{-12}\). The drop \(P_{D,Z}(0)-P_{D,Z}(\tau)\) equals \(S(\rho(\tau))\). Both pieces depend on \((\gamma,\tau)\) only through \(e^{-\gamma\tau}\). The respecting destruction stays \(0\), so it is not this partition. *Fails if* any cell misses by \(\ge 10^{-9}\).

**Q5, the cut on the qubit.** \(P_D(\theta)\) matches the closed form within \(10^{-12}\), is \(0\) at \(\theta=\pi/2\), and is strictly decreasing in \(|\sin\theta|\) on the locked angles, at each locked \(r\). *Fails if* the form misses or the sample is not strictly decreasing.

### Headline rule

| Predicates | Label |
|---|---|
| P1, Q1, Q2, Q3, and Q4 hold, and P5 holds as the null it names | `CLUE_SPLIT` |
| P1 fails because, under the stock formula, P is strictly cheaper for every \(w>0\) whenever \(\gamma\tau>0\) | `NULL_DECOHERENCE` |
| anything else | `PUZZLE` |

The predicted label is **`CLUE_SPLIT`**. `NULL_DECOHERENCE` is the plain-decoherence restatement and does not count as the result asked in (b). `PUZZLE` is a miss to diagnose. The script prints the table's label only.

### What counts as the null

A comparison is a plain-decoherence restatement when the strict winner changes only because \(e^{-\gamma\tau}\) crossed a constant that does not depend on \(w\) and \(q\), or when every positive stake agrees as soon as \(\gamma\tau>0\). P5 is that restatement. P1 is not: the critical stake \(h(\varepsilon)/\varepsilon\) moves with \(\gamma\tau\). Zurek's sieve and Landauer's erasure bound, as cited in §5, do not state P1 or P2.

## 4. Code-scored checks

Script `theory/dephasing_crossover_checks/dephasing_crossover_checks.py`, standard library only. One line per check, then `HEADLINE`, then `FAILS`, and `ALL T84 CHECKS PASS` only when the count is 0.

| Check | Scores | Pass |
|---|---|---|
| C0 | matrix \(I\), \(P_D\), \(L\) against the three closed forms, every locked \((\gamma\tau)\) | max absolute error \(\le 10^{-9}\) |
| C1 | P1, including the shape sample | P1 true |
| C2 | P2, including \(\chi(r)/r\) | P2 true |
| C3 | P3 | P3 true |
| C4 | P4 | P4 true |
| C5 | P5 | P5 true |
| C6 | Q1 | Q1 true |
| C7 | Q2 | Q2 true |
| C8 | Q3 | Q3 true |
| C9 | Q4 | Q4 true |
| C10 | Q5 | Q5 true |
| C11 | headline | the table's label, and a miss does not print `CLUE_SPLIT` in its place |

C0–C11 failing is a puzzle in the memo. The script is not edited to change a criterion. A bug that does not change a criterion is a deviation.

`tools/test_dephasing_crossover.py` compares the stored stdout byte for byte.

## 5. Prior-art log (before the scored run)

### 5.1 Repository

On this branch, at `d2aeb81`, before any results file:

```
git grep -n -i -E 'dephasing rate|phase memory' -- '*.md' '*.py'
```

No match for a holding-time price. The pointer-basis note is T73. The ratio note on this main is T74. Q-coh is not on this main. It is on `origin/forge-record-ratio-reframes` at `40c4060`, the head of upstream draft #257.

### 5.2 Crossref (API, 24 November 2026)

User-Agent `theory-repo-prereg/1.0`. Direct lookups, HTTP 200, titles as returned:

| DOI | Title | Author, issued, container |
|---|---|---|
| `10.1147/rd.53.0183` | Irreversibility and Heat Generation in the Computing Process | Landauer. July 1961. *IBM Journal of Research and Development* 5(3), 183–191 |
| `10.1143/ptp/89.2.281` | Preferred States, Predictability, Classicality and the Environment-Induced Decoherence | Zurek. 1 February 1993. *Progress of Theoretical Physics* 89(2), 281–312 |
| `10.1103/PhysRevLett.70.1187` | Coherent states via decoherence | Zurek, Habib, Paz. 1 March 1993. *Physical Review Letters* 70(9), 1187–1190 |
| `10.1103/RevModPhys.75.715` | Decoherence, einselection, and the quantum origins of the classical | Zurek. 22 May 2003. *Reviews of Modern Physics* 75(3), 715–775 |
| `10.1038/nphys1202` | Quantum Darwinism | Zurek. March 2009. *Nature Physics* 5(3), 181–188 |
| `10.1103/PhysRevA.72.062101` | Predictability sieve, pointer states, and the classicality of quantum trajectories | Dalvit, Dziarmaga, Zurek. 1 December 2005. *Physical Review A* 72 |
| `10.1103/PhysRevX.4.031015` | Thermodynamics with Continuous Information Flow | Horowitz, Esposito. 28 July 2014. *Physical Review X* 4(3) |
| `10.3390/e24010106` | Does Decoherence Select the Pointer Basis of a Quantum Meter? | Kofman, Kurizki. 10 January 2022. *Entropy* 24(1), 106 |
| `10.1103/PhysRevLett.90.010403` | Decoherence-Induced Continuous Pointer States | Blanchard, Olkiewicz. 10 January 2003. *Physical Review Letters* 90(1) |
| `10.1088/1751-8113/43/1/015303` | Pointer basis induced by collisional decoherence | Busse, Hornberger. 8 December 2009. *Journal of Physics A* 43(1), 015303 |

The sieve, as read in this repo, picks states by entropy production and does not put a stake in the sum (`theory/pointer-basis-stakes-2026-11-24/MEMO.md:9`). Landauer, as stated in this repo, is at least \(kT\ln 2\) per erased bit (`theory/SCALE_ENDS.md:23`). Horowitz and Esposito is the heat floor at `CORE.md:70`. None of those Crossref titles states an inequality in \((\gamma,\tau,w)\). No abstract field was returned for these ten records, so no abstract is quoted. A title is not a novelty proof.

Bibliographic queries the same day, `rows=5` unless noted, `total-results` as returned:

- `dephasing Landauer pointer basis cost`: 704730. First items included `10.2139/ssrn.7246118` and `10.5772/34846` (Venugopalan, "Measurement in Quantum Mechanics: Decoherence and the Pointer Basis", 22 February 2012). Not used as an input.
- `query.title=thermodynamic cost coherence`: 629664. First items included `10.1088/1367-2630/aca49b` (Hammam, Leitch, Hassouni, De Chiara, "Exploiting coherence for quantum thermodynamic advantage", 1 November 2022, *New Journal of Physics* 24(11), 113053) and `10.1103/PhysRevE.84.061110` (Granger, Kantz, "Thermodynamic cost of measurements", 6 December 2011, *Physical Review E* 84(6)). Both titles were confirmed on a direct lookup. The texts were not opened. They are not evidence that a stake threshold is absent.
- `Landauer cost pointer basis decoherence`, `rows=8`: 707392. First relevant items were the Kofman, Busse, and Blanchard records in the table.

## 6. What this note will not say

It will not edit `THEORY.md` or `CORE.md`. It will not say that quantum mechanics, general relativity, holography, or gravity has been derived. The sentence quoted from `CORE.md:7` is the hypothesis. A miss is a puzzle or a clue. The record price is a cost.
