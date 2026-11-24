# Gate T82f: CONSISTENCY_CHECK. Do not run. Park the torus thread.

*24 November 2026 (UTC). Paper gate only. No code, no orbit, no population, no new number from a machine. `THEORY.md` and `CORE.md` are not edited. Locked preregistrations are not edited. This file does not score T82 through T82e. Formal gate status: NOT A TEST. Label: CONSISTENCY_CHECK. The rule applied is upstream draft PR #263, `process/PREREG_GATE.md` §2.*

Ace's question: in the torus world, under selection on realized outcomes (the EVO1 pattern, `tests/EVO1/PREREG_EVO.md:12-14`), does the stake decide when the evolved memory pays to track phase in addition to the conserved actions?

Four readings are checked below. Each one has a stake threshold, or a dimension triple, that the locked cost already fixes. None passes G2. None passes G5. The recommendation is to park the torus thread.

## Why this approach

T82e's lock, after the width and the scaling miss, shelves the resonance thread on this toy and names one next look: whether the continuous record is a smooth coordinate of the conserved actions (`PREREG_T82E.md:17`). The independent review of that lock (fork PR #16, comment 7146714705) already classifies one scored row, P-eps0, as NOT A TEST: the count is an identity of the free rotation on the grid, and the information is zero. The same review records that information plus destruction, in the locked antenna formula, is independent of \(\theta_2\).

The rewording replaces that coordinate question with a selection question. The selection pattern is a population evolving under mutation and selection on realized outcomes, scored against the design that minimizes \(J\). The simulator is written without the expected-cost formula (`tests/EVO1/PREREG_EVO.md:12-14`, `:27-28`). The gate asks, before any such population exists, whether the stake threshold is already the minimum of the cost T82 locked:

\[
J=\kappa I+q\kappa P_D+w L,\qquad \kappa>0,\ q\ge 0,\ w>0
\]

(`theory/torus-memory-2026-11-24/PREREG.md:14`). P3 of that lock passed: on a Haar prior, \(P_D=I\) whenever the mutual information is finite, so

\[
J=\kappa(1+q)\,I+w L
\]

(`PREREG.md:92`; `MEMO.md:36-40`). The factor \(q\) rescales \(\kappa\). The method those files cite is to write the cost, minimize, and read off the design. The sentence is `CORE.md:48`. `PREREG.md:11` points at `CORE.md:47`, the blank line above that sentence.

## Can it fail / Cheapest way

Inside this cost, on this menu, the comparison returns the threshold below. A miss would be a threshold other than the two numbers in G1, or an informative-dimension triple other than \((0,1,2)\) at the three stakes already named in P5. Both are arithmetic consequences of \(J=\kappa(1+q)I+wL\) and of \(\mathbb{E}[\cos^2\theta_j]=1/2\). The honest odds of that miss are about 0. That is a G1 stop by itself.

Cheapest way: the comparison in G2, three designs, no orbit. It returns the threshold on the page. A population is a more expensive way to ask the same comparison.

## Gate

### G1. Miss

On the locked unequal menu, \(y=\cos\theta_1+0.1\cos\theta_2\), two fair phase bits, \(\kappa=1\), \(q=0\) (`PREREG.md:98`), the outcome that would count as a miss is an informative dimension other than

| Stake \(w\) | Dimension | Minimizer |
|---|---|---|
| \(1\) | \(0\) | blind |
| \(10\) | \(1\) | the unit-amplitude phase only |
| \(1000\) | \(2\) | both phases |

or a switch stake other than

\[
w_1^\star=2\ln 2=1.386294361120,\qquad w_2^\star=200\ln 2=138.629436111989.
\]

Odds of that miss, given the locked cost and P3, are about 0. G1 stops the run.

The same stop holds for the selection wording. The evolved dimension triple those three stakes would be scored against is this table. A selector that minimizes the realized cost on this menu is being asked to reproduce the table. The chance that the minimum of the realized cost is a different table is about 0, because on this menu the realized cost is \(J\).

### G2. Not an identity

The stake threshold can be computed by hand from the locked cost. This item is a CONSISTENCY_CHECK.

**Actions drop out.** At zero coupling the actions are constant (`MEMO_REVERSIBLE.md:25`). The flow is \(\theta(t)=\theta(0)+\Omega(I)\,t\). Haar measure is invariant, so the conditional distribution of \(\theta(t)\) given the actions is Haar, and

\[
\mathbb{E}[\cos^2\theta_j\mid I]=\mathbb{E}[\cos^2\theta_j]=\tfrac12.
\]

A memory that stores the actions and not the phases has the blind loss. The actions do not appear in the threshold for adding a phase bit.

**Phase bit.** Bit \(j\) of amplitude \(a_j\) costs information \(\ln 2\) and saves \(\Delta L_j=a_j^2/2\), because a known phase cancels its own term and an unknown phase contributes \(a_j^2/2\). With \(P_D=I\),

\[
w\,\Delta L_j>\kappa(1+q)\ln 2
\quad\Longleftrightarrow\quad
w>w_j^\star=\frac{2\kappa(1+q)\ln 2}{a_j^2}.
\]

Unit amplitude: \(w^\star=2\kappa(1+q)\ln 2\). Amplitude \(0.1\): \(w^\star=200\kappa(1+q)\ln 2\). At \(\kappa=1\), \(q=0\) these are the two numbers in G1. They are P5 (`PREREG.md:98`), which already passed as the per-mode window (`CORE.md:92`).

**The three costs at \(\kappa=1\), \(q=0\).** Blind loss is \(1/2+0.005=0.505\). One nats price is \(\ln 2=0.693147180560\).

| Design | \(w=1\) | \(w=10\) | \(w=1000\) |
|---|---|---|---|
| Blind | \(0.505000000000\) | \(5.050000000000\) | \(505.000000000000\) |
| Unit phase only | \(0.698147180560\) | \(0.743147180560\) | \(5.693147180560\) |
| Small phase only | \(1.193147180560\) | \(5.693147180560\) | \(500.693147180560\) |
| Both | \(1.386294361120\) | \(1.386294361120\) | \(1.386294361120\) |

Unique minima: blind, unit phase, both. Dimensions \(0,1,2\).

On the symmetric menu, at every \(\kappa>0\), \(q\ge 0\), \(w>0\), another row matches or beats the one-phase row. Blind and both tie at \(w=2\kappa(1+q)\ln 2\); below it blind is unique; above it both is unique (`PREREG.md:95`). Stake decides that one threshold, and the threshold is already written.

**Reading A, the minimum of \(J\).** The scored value is \(w_j^\star\). It is the display above. G2 stops the run.

**Reading B, selection on realized outcomes.** This is Ace's wording and the EVO1 pattern: fitness from the realized cost, the evolved design compared with \(\arg\min J\) (`tests/EVO1/PREREG_EVO.md:12-14`, `:27-28`). The value the population is scored against is the table in G1. That table was computed before any population. Agreement of a reliable minimizer with \(\arg\min J\) is the bookkeeping comparison EVO1 already states (`tests/EVO1/PREREG_EVO.md:38-40`). G2 stops the run. The label stays CONSISTENCY_CHECK. The cost already fixes the value a selection run would be scored against.

**Reading C, the coordinate look T82e named.** In the locked antenna formula (`PREREG_T82E.md:39`),

\[
I+P_D=\tfrac12\bigl(\ln 2-h_b(\tfrac{1+R}{2})\bigr),
\]

which is constant in \(\theta_2\). The angle dependence in \(J=I+P_D+w L\) is \(w L\), and \(L\) depends on \(\theta_2\) through \(\cos^2\theta_2\). On a circulating orbit that equidistributes, the time average of \(\cos^2\) is \(1/2\), so the averaged record is the same number for every action that leaves the orbit circulating. On the librating island the average depends on the pendulum action through that same \(\cos^2\), and the island width is the reduction already locked, \(W(\varepsilon)=2\sqrt{2}\sqrt{\varepsilon}\) (`PREREG_T82E.md:69`). Stake multiplies \(L\). For every \(w>0\) the averaged record varies with the action exactly where \(\langle L\rangle\) does. The qualitative coordinate is fixed by the reduction. G2 stops the run.

**Reading D, a noisy phase, or the rate form.** A phase that must be tracked as a moving signal, with ongoing heat, is the blind corner already at `CORE.md:91`: at or below the stake \(kT a/v\) the design is blind, and above it the minimizing cost is \(2\sqrt{kT\,a\,v\,w}-kT\,a\). That threshold is hand arithmetic from the rate cost `CORE.md:66`. Separately, a deterministic phase whose frequency is known is a static initial condition plus an autonomous flow. A static record has vanishing ongoing heat after the write (`CORE.md:78`), so the rate cost keeps the phase at every \(w>0\). Both answers are closed forms. T82 already chose the stock cost (`PREREG.md:14`), and under that choice the threshold is \(w_j^\star\). G2 stops the run for the rate reading as well.

Every reading fixes its stake threshold by the locked formulas, by P3, by CT4, or by CT33. CT4 states the general comparison: the first bit pays when its price lies below the loss it saves (`THEORY.md:279`; the same sentence at `CORE.md:96`). CT33 states that, on a menu independent of the stake and with ruin slack, error is nonincreasing in the stake and judgment spend is nondecreasing (`THEORY.md:495`; `CORE.md:54`). The torus menu is an instance of those two statements.

### G3. Named rival

The rival is a no-heat predictive-information memory in the sense of Bialek, Nemenman, and Tishby, with the tradeoff setting fixed before the stake is chosen.

Crossref, queried 24 November 2026, `GET https://api.crossref.org/works/10.1162/089976601753195969`. The DOI resolves. Record: William Bialek, Ilya Nemenman, and Naftali Tishby, "Predictability, Complexity, and Learning," *Neural Computation* 13(11), pages 2409–2463, issued 2001-11-01, publisher MIT Press. The abstract defines predictive information \(I_{\mathrm{pred}}(T)\) as the mutual information between the past and the future of a time series, and states that when the series lets one learn a model with a finite number of parameters, \(I_{\mathrm{pred}}(T)\) grows logarithmically with a coefficient that counts the dimensionality of that model. The coefficient is a property of the series. The stake \(w\) is not in it.

The rival's objective, fixed in advance, is

\[
C_\lambda=I(M;\mathrm{past})-\lambda\,I(M;\mathrm{future}),
\]

with one \(\lambda\) chosen before \(w\), and with no \(\kappa\), no \(q\), and no \(w\). On the fair-bit menu the flow is deterministic, so a stored phase bit has \(I(M;\mathrm{past})=I(M;\mathrm{future})=\ln 2\). Then \(C_\lambda=(1-\lambda)\ln 2\) if the bit is stored and \(C_\lambda=0\) if it is not. The bit is stored when \(\lambda>1\). Both bits have the same predictive information. Amplitude sits in \(L\), and \(L\) is absent from \(C_\lambda\), so the rival stores both bits or neither.

Predicted dimension, at every stake including \(w=1\), \(10\), and \(1000\):

\[
d_\lambda=\begin{cases}0& \lambda\le 1,\\ 2& \lambda>1.\end{cases}
\]

The no-heat endpoint is the second line: information is unpriced, both phases are kept, \(d=2\). The locked cost at those three stakes has dimensions \(0,1,2\). The absolute gap at the locked witness \(w=10\) is \(1\), for every fixed \(\lambda\). At that stake the locked minimum is the unit phase only, cost \(0.743147180560\). The rival's two candidates there are the blind design, cost \(5.050000000000\), and both phases. Both phases, with the information price restored, cost \(1.386294361120\); with the information price removed they cost \(0\). Either rival candidate is a different design from the unique minimizer of the locked cost.

The rival predicts a dimension in \(\{0,2\}\) that stays constant as \(w\) changes. The locked cost predicts the triple \((0,1,2)\).

### G4. Reach

Level (a), the toy menu already locked as P4 and P5 (`PREREG.md:95`, `:98`). The numbers land on lines already written: the per-mode count `CORE.md:92`, the blind corner `CORE.md:91`, higher stakes buy more judgment `CORE.md:54`, the first bit must pay `THEORY.md:279`, and judgment spend is nondecreasing in the stake `THEORY.md:495`. The question names no real system and no external series.

A hit restates those lines. The toy stays at level (a). G4 stops the run.

### G5. Next step

**Reading A, and readings C and D.** A hit records the hand threshold and stops. A miss on this page is an arithmetic discrepancy in the same display. The next step in both cases is to keep the closed form. Do not run.

**Reading B, the selection wording.** A hit says the evolved designs sit on the table in G1. That is the bookkeeping outcome EVO1 already describes, and EVO1 states that this outcome says nothing about nature (`tests/EVO1/PREREG_EVO.md:38-40`). The next step is to park the torus thread. A miss says the population did not sit on that table. The threshold \(w_j^\star\) stays the hand value. The miss is a selector miss of a known minimum, which EVO1 already treats as a diagnosis of the selector (`tests/EVO1/PREREG_EVO.md:19-22`). The next step for the torus thread is again to park it. The two outcomes prescribe the same next step for this question.

Do not run.

No version passes G2 and G5. Park the torus thread. One ledger line is enough: `gate: stopped`, fields G1, G2, and G5, label CONSISTENCY_CHECK.
