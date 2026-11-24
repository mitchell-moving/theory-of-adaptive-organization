# T83 preregistration: quantum revivals and reversible phase storage

*Tuesday 24 November 2026 (UTC). Written and committed before `revival_phase_checks.py` and before any scored output. Branch `forge-revival-phase-storage`, cut from upstream `main` at `d2aeb8100e22870dc5aee2529356de970c82a820`. `THEORY.md` and `CORE.md` are not edited. Locked by sha256 in `PREREG.sha256`, same commit. A later change to the criteria below is a deviation, appended in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle or a pivot. It is not a kill and not a verdict. Every statement about what the cost does on this well is a model implication, in-model.

## Hypothesis

**HYPOTHESIS, Chad's intuition, framed by Ace.** Reversible phase storage is a memory with no record and zero heat to keep. Cost is paid only at read-out or decoherence.

The carrier used below is the infinite square well, because its spectrum is the textbook quadratic case. It is an input from quantum mechanics. It is not derived from the cost.

## Why this approach

The questions are whether `CORE.md` §3 already gives zero ongoing heat for a bath-free unitary trajectory, whether the T73 pointer prices already sit on the pinch, and whether a return share across \(t/T_{\mathrm{rev}}\) does anything but reproduce the known revival shape. The cheapest way to see an addition would be a term in \(J\) that those results do not already assign. If no such term appears, the honest score is a consistency check or a relabel.

## Can it fail

Can it fail: yes. The locked Gauss-sum heights can miss, the copy count can miss, an irrational probe can sit on a peak, the incommensurate spectrum can still return near 1 at \(T_{\mathrm{rev}}\), the perturbed well can still revive inside the exact bar, and a keep-cost can come out nonzero.

Cheapest way: the single cell \(\tau=1/3\) on the flat window, where the locked return is \(1/3\), or the three-level spectrum \(E_n=n^2+\sqrt{p_n}\) with return at \(t=2\pi\) at least \(0.5\).

## Advance criterion

An item is a **consistency check** if the measured number reproduces a cited result inside the tolerance below. It is a **relabel** if the number is `CORE.md` §3 or the T73 pinch prices read on this system. It is an **addition** only if \(J\) assigns a quantity that the cited revival, fractal, recurrence, and Landauer results do not already assign. Locked expectation, before the run: (a), (b), and (c) are consistency checks or relabels. An addition would be a puzzle under that expectation, not a victory lap.

A match that holds by a definition or by the algebra already written here is marked that way. It is not evidence.

## 1. Prior art

Checked on the Crossref API on 24 November 2026, HTTP 200, before this commit. No number is taken from these works except the dimensions and the revival statements named below. No page of a book is claimed. A DOI that did not return is not cited.

- Berry, M. V. Quantum fractals in boxes. Journal of Physics A 29:6617 (1996). doi `10.1088/0305-4470/29/20/016`. For a discontinuous initial wave in a one-dimensional box, the graph of \(P\) in time has dimension \(7/4\) for almost every position, and the graph of \(P\) in space has dimension \(3/2\) for almost every time. At rational times \(P\) is piecewise constant (a finite superposition of shifted copies; his propagator writes \(q\) copies). At irrational times the density is fractal. His \(\tau\) is the half-integer convention of that paper, not the integer \(\tau\) of §3 below.
- Berry, M. V. and Klein, S. Integer, fractional and fractal Talbot effects. Journal of Modern Optics 43:2139 (1996). doi `10.1080/09500349608232876`. The optical Talbot carpet: finite copies at rational fractions, fractal between them.
- Wen, J., Zhang, Y., and Xiao, M. The Talbot effect: recent advances in classical optics, nonlinear optics, and quantum optics. Advances in Optics and Photonics 5:83 (2013). doi `10.1364/AOP.5.000083`. Review of that carpet, including the quantum case.
- Averbukh, I. Sh. and Perelman, N. F. Fractional revivals: universality in the long-term evolution of quantum wave packets beyond the correspondence principle dynamics. Physics Letters A 139:449 (1989). doi `10.1016/0375-9601(89)90943-2`. Fractional revivals as a finite superposition of packets.
- Aronstein, D. L. and Stroud, C. R. Fractional wave-function revivals in the infinite square well. Physical Review A 55:4526 (1997). doi `10.1103/PhysRevA.55.4526`. The infinite well, at every time, as translated copies of the initial wave, parity-paired.
- Robinett, R. W. Quantum wave packet revivals. Physics Reports 392:1 (2004). doi `10.1016/j.physrep.2003.11.002`. Review. No table entry is copied.
- Landauer, R. Irreversibility and Heat Generation in the Computing Process. IBM Journal of Research and Development 5:183 (1961). doi `10.1147/rd.53.0183`. Heat is tied to logical irreversibility. Keeping a reversible state is not an erasure.
- Bocchieri, P. and Loinger, A. Quantum Recurrence Theorem. Physical Review 107:337 (1957). doi `10.1103/PhysRev.107.337`. A finite quantum system returns arbitrarily close to its initial state. The return need not be periodic.
- Hogg, T. and Huberman, B. A. Recurrence Phenomena in Quantum Dynamics. Physical Review Letters 48:711 (1982). doi `10.1103/PhysRevLett.48.711`. The same recurrence, and its destruction once the spectrum is effectively irregular.

The integer-well copy count in §3 is proved there from the Gauss sum. It is not a quotation of a page in the list above. Berry's count of \(q\) copies belongs to his half-integer propagator.

## 2. What the cost already says

`CORE.md:70`. The floor \(\dot Q_M\ge kT\,\dot I_M\) is stated under a memory/world split and local detailed balance, or under the Einstein relation for additive-noise diffusions. A closed well has no bath and no such split. The floor therefore does not assign a positive rate, and its hypotheses do not by themselves prove a zero. The nearest sentence is `CORE.md:78`: a static record in a frozen world can sit at vanishing ongoing memory-bath heat after a one-time write. Storage is cheap. Tracking a changing, connected world is what costs. Reading phase storage as that sentence is a relabel, and it is consistent with Landauer 1961 because keeping the phases erases nothing.

`theory/pointer-basis-stakes-2026-11-24/MEMO.md:66`. The T73 cost with both record terms named is \(J=\kappa I(W;M)+\kappa_D P_D+w L\), coefficients nonnegative (`MEMO.md:68`, A8 at `CORE.md:52`). The same line says a record kept as an unmeasured state was not taken up. \(I(W;M)\) and \(P_D\) are prices of a pinch. They are zero when no pinch is applied, because they are not defined on the coherent state. That placement is a relabel of where those terms sit. It is not a derivation that the keep-cost is zero.

`CORE.md:161` (T54). On the graphs scored there, the cost tracks the sites the decision names, not the Hausdorff or spectral dimension. A dimension entering \(J\) on this well would be an addition. None is expected.

## 3. The well, and the locked shape

Units \(\hbar=1\), \(2m=1\), width \(1\). Then \(E_n=n^2\) for \(n=1,2,\ldots\) and \(T_{\mathrm{rev}}=2\pi\). The reduced time is \(\tau=t/T_{\mathrm{rev}}\), and the phase of level \(n\) is \(\exp(-2\pi i n^2\tau)\).

**T81's definition is present and is not this object.** On fork branch `forge-record-ratio-measured` at `f625bb74c2702a6a9b1f7d5b8afff922f90cf8b3`, `theory/record-ratio-measured-2026-11-24/PREREG.md` defines \(q(T)\) as the fraction of displaced excitations that have made a first entrance into the agent region of a lazy path. That chain has no revival time and no copy count. It is not measured here.

**Minimal definition, labeled MINIMAL-RETURN.** The return share of the initial packet is the Born probability of the initial state,

\[
R(\tau)=\Bigl|\sum_n |c_n|^2\exp(-2\pi i n^2\tau)\Bigr|^2.
\]

It is not T81's \(q\). In this note the phrase "flow-ratio return share" means this \(R\), and the label stays on it.

**Flat window.** \(N=120\), \(c_n=1/\sqrt{N}\) for \(n=1,\ldots,N\), and \(0\) otherwise. \(120\) is a multiple of every \(q\le 8\), so each residue class appears equally often.

**Locked shape, proved below, before the run.** For \(\tau=p/q\) in lowest terms, \(1\le q\le 8\),

\[
\begin{aligned}
q\text{ odd:}&\quad N_c=q,\quad R=1/q=1/N_c,\\
q\equiv 0\pmod{4}:&\quad N_c=q/2,\quad R=2/q=1/N_c,\\
q\equiv 2\pmod{4:}&\quad N_c=q/2,\quad R=0.
\end{aligned}
\]

\(N_c\) is the number of nonzero weights in the period-\(q\) expansion of the quadratic phase. When the weight at shift \(0\) is nonzero, one copy sits on the initial packet and the return equals \(1/N_c\). When \(q\equiv 2\pmod 4\), every surviving copy is shifted off the origin and the return is \(0\), even though \(N_c=q/2\) copies are present. Peaks of \(R\), where they exist, are weighted by the copy count. The zero at \(q\equiv 2\pmod 4\) is part of the shape, not a miss.

**In between.** Eight probes \(\tau_k=\{k(\sqrt 5-1)/2\}\) for \(k=1,\ldots,8\), and \(\tau=\sqrt 2/2\). Locked: each has \(R<0.05\). That is the finite-window stand-in for structure between the peaks. A Hausdorff dimension of \(R(\tau)\) is not claimed. Berry's fractal is the graph of the probability density of a discontinuous wave, scored only as the coefficient exponent in §6, not as a dimension of \(R\).

### Proof of the three lines

Let \(\gcd(p,q)=1\) and

\[
a_s=\frac1q\sum_{j=0}^{q-1}\exp\bigl(-2\pi i(pj^2+sj)/q\bigr),\qquad s=0,\ldots,q-1.
\]

\(N_c=\#\{s:a_s\neq 0\}\) and the flat-window return is \(R=|a_0|^2\), because a complete set of residues is exactly the average of the phase.

Write \(S(s)=\sum_j\exp(-2\pi i(pj^2+sj)/q)\). Then

\[
|S(s)|^2=\sum_{d=0}^{q-1}\sum_{k=0}^{q-1}\exp\bigl(-2\pi i\bigl(pd(2k+d)+sd\bigr)/q\bigr).
\]

The inner sum over \(k\) equals \(q\) when \(2pd\equiv 0\pmod q\), and equals \(0\) otherwise. Since \(\gcd(p,q)=1\), this is \(q\mid 2d\).

- If \(q\) is odd, \(2\) is invertible, so \(d\equiv 0\) only. \(|S(s)|^2=q\) for every \(s\). Thus \(|a_s|=1/\sqrt q\), \(N_c=q\), and \(R=1/q\).
- If \(q\equiv 0\pmod 4\), then \(q\mid 2d\) iff \(d\in\{0,q/2\}\). The \(d=q/2\) phase is \(\exp(-2\pi i\,pq/4)\exp(-\pi i s)=(-1)^s\), using that \(q/4\) is an integer. So \(|S|^2=q\bigl(1+(-1)^s\bigr)\): even \(s\) have \(|a_s|=\sqrt{2/q}\), odd \(s\) vanish. \(N_c=q/2\) and \(R=2/q\).
- If \(q\equiv 2\pmod 4\), the same two values of \(d\) appear, and \(q/4\) is a half-integer, so the \(d=q/2\) phase is \(-(-1)^s\) (and \(p\) is odd). Thus \(|S|^2=q\bigl(1-(-1)^s\bigr)\): odd \(s\) have \(|a_s|=\sqrt{2/q}\), even \(s\) vanish. \(N_c=q/2\) and \(R=|a_0|^2=0\).

The \(\tau=0\) and \(\tau=1\) rows are the case \(q=1\): \(N_c=1\), \(R=1\).

**Copies in space.** The odd extension of a wave on \([0,1]\) to period \(2\) is \(U(y)=\psi(y)\) on \((0,1)\) and \(U(y)=-\psi(2-y)\) on \((1,2)\). At \(\tau=p/q\),

\[
\psi(x,\tau)=\sum_{s=0}^{q-1}a_s\,U_0(x-2s/q),
\]

with \(U_0\) the odd extension of the initial wave. This is the discrete Fourier inversion of the quadratic phase, so it is an identity on any finite sine packet. The script checks it. A mismatch is an algebra or a shift error, and it is a puzzle.

## 4. Heat, read-out, decoherence

Scored times for the keep-cost: \(\tau=0\), \(\tau=1/3\), \(\tau=\sqrt 2/2\).

- **A-keep.** Unitary evolution. Purity stays \(1\). Populations \(|c_n|^2\) do not change. There is no bath operator, so the memory-bath heat used here is \(Q_{\mathrm{keep}}=0\) at each scored time. Reading: RELABEL of `CORE.md:78`, consistent with Landauer 1961. Not an addition, because `CORE.md:70` does not apply its hypotheses to this well, and the zero is the absence of a bath.
- **A-read.** No pinch: \(P_D=0\) and there is no outcome \(M\), so \(I(W;M)\) is not charged. A two-outcome projective pinch onto the initial state, on a pure state, has outcome entropy \(h(R)=-R\ln R-(1-R)\ln(1-R)\) with \(h(0)=h(1)=0\). Locked: that entropy equals \(h(R)\) within \(10^{-12}\), and equals \(0\) at \(\tau=0\). Reading: RELABEL of T73's pinch prices (`MEMO.md:66`, `MEMO.md:68`). The prices sit at the pinch because that is where they are defined.
- **A-dephase.** Complete dephasing in the energy basis of a pure state produces Shannon entropy \(H=-\sum |c_n|^2\ln|c_n|^2\) in one shot, then no further ongoing term in this model. On the flat window \(H=\ln 120\), the same at \(\tau=0\) and at \(\tau=\sqrt 2/2\), within \(10^{-12}\). That one-shot entropy is the Landauer erasure content of the resulting classical record. It is not a heat paid to keep the phases.

Falsifier of "no addition": a keep-cost, built only from `CORE.md:70` or from \(J\) at `MEMO.md:66`, that is nonzero at a scored \(\tau\) while no pinch and no bath have been applied.

## 5. Commensurate and incommensurate

**Spectrum arm.** Three levels, equal superposition.

- Commensurate: \(E_n=n^2\). At \(t=2\pi\), \(R>1-10^{-9}\). Exact Poincaré return at the revival time. Consistency check of the quadratic spectrum.
- Incommensurate: \(E_n=n^2+\sqrt{p_n}\) with \(p_1=2\), \(p_2=3\), \(p_3=5\). At \(t=2\pi\), \(R<0.5\). The quadratic part realigns and the irrational parts do not.
- Approximate return: \(t_k=0.37\,k\) for \(k=1,\ldots,800\). The maximum satisfies \(0.9\le R<1-10^{-8}\), and it exceeds the value at \(t=2\pi\). A finite sum of incommensurate phases returns close and not exactly (Bocchieri and Loinger 1957; Hogg and Huberman 1982). A miss of the \(0.9\) bar is a horizon puzzle, not a claim that recurrence fails.

**Perturbed well.** Basis \(n=1,\ldots,6\). \(H_{nm}=n^2\delta_{nm}+\lambda\langle n|x^2|m\rangle\) on \([0,1]\),

\[
\langle n|x^2|n\rangle=\frac13-\frac{1}{2\pi^2 n^2},
\]

and for \(n\neq m\), with \(I(r)=2\bigl((-1)^r-1\bigr)/(r^2\pi^2)\) for \(r\neq 0\),

\[
\langle n|x^2|m\rangle=I(|n-m|)-I(n+m).
\]

Packet: equal superposition of \(n=1,2,3\). Jacobi diagonalization, at most \(40\) sweeps, stop when every off-diagonal entry is below \(10^{-12}\).

- \(\lambda=0\): \(R(2\pi)>1-10^{-8}\).
- \(\lambda=8\): \(R(2\pi)<0.98\). Not the exact revival.
- Same \(\lambda=8\), grid \(t=0.05\,j\) for \(j=1,\ldots,1600\): the maximum exceeds \(R(2\pi)\) by at least \(0.02\), exceeds \(0.95\), and stays below \(1-10^{-6}\). Approximate recurrence of a finite basis. A miss is a puzzle about the horizon or the shift, not a kill.

Both arms are known spectral facts. They are consistency checks unless \(J\) assigns a different keep-cost to the two spectra. Locked: both keep-costs are \(0\).

## 6. Fractal dimension and the cost

Exploratory, labeled speculative. Berry's \(D_{\mathrm{space}}=3/2\) is the dimension of the infinite sum, read off the coefficient decay by his formula \(D=(5-\beta)/2\) when \(|a_m|^2\sim|m|^{-\beta}\). The discontinuous state on \((0,1)\) has exact sine coefficients \(c_n=2\sqrt 2/(n\pi)\) for odd \(n\) and \(c_n=0\) for even \(n\), so \(|c_n|^2=8/(n^2\pi^2)\) and \(\beta=2\) on the odd modes, which is his input for \(D=3/2\). The script checks that closed form on odd \(n=1,3,\ldots,81\): the slope of \(\ln|c_n|^2\) against \(\ln n\), and the value against \(8/(n^2\pi^2)\), within \(10^{-12}\).

A box-counting slope on a truncation is not scored. Berry states that a finite largest \(n\) softens the finest detail, and this note does not enlarge the basis until a slope could be that dimension. Printing a truncation slope and calling it \(3/2\) would not be his theorem.

**C-link.** \(Q_{\mathrm{keep}}(0)=Q_{\mathrm{keep}}(\sqrt 2/2)=0\). The cited spatial dimension differs between a rational revival and an irrational time, and the keep-cost does not. Reading: RELABEL of `CORE.md:78` and of T54 at `CORE.md:161`. Not an addition. Falsifier: a term of \(J\), taken from `CORE.md:70` or `MEMO.md:66`, nonzero on the unitary trajectory and different at those two times.

## 7. Tolerances and falsifiers

| Check | Bar | Falsifier | Reading if it holds |
|---|---|---|---|
| B-shape | Every lowest-terms \(p/q\) with \(q\le 8\), and \(\tau=0,1\), match §3 within \(10^{-9}\) on \(R\) and exactly on \(N_c\) | any miss | consistency check of the Gauss sum |
| B-copy | At \(\tau=1/3,1/4,1/6\), max absolute gap between the modal wave and the shifted copies, on \(48\) mid-bin points, at most \(10^{-8}\) | gap above \(10^{-8}\) | consistency check of the copy identity |
| B-between | Each of the nine irrational probes has \(R<0.05\) | any probe at least \(0.05\) | the finite-window stand-in; a puzzle if a probe hits a peak |
| A-keep | \(Q_{\mathrm{keep}}=0\) and purity \(>1-10^{-12}\) at the three times | a nonzero keep-cost | relabel |
| A-read | pinch entropy within \(10^{-12}\) of \(h(R)\); zero with no pinch | a gap above \(10^{-12}\) | relabel of the pinch |
| A-dephase | the two times agree with \(\ln 120\) within \(10^{-12}\) | a gap, or a drift in \(\tau\) | consistency with one-shot erasure |
| P-comm | \(R(2\pi)>1-10^{-9}\) | below the bar | consistency check |
| P-incomm | \(R(2\pi)<0.5\), and the \(800\)-step max in \([0.9,1-10^{-8})\) and above \(R(2\pi)\) | outside | consistency check; a short horizon is a puzzle |
| P-well | \(\lambda=0\) above \(1-10^{-8}\); \(\lambda=8\) below \(0.98\); later max above that value by \(0.02\), above \(0.95\), below \(1-10^{-6}\) | outside | consistency check |
| C-beta | odd-mode \(|c_n|^2\) matches \(8/(n^2\pi^2)\) within \(10^{-12}\) | a gap | consistency check of Berry's input, not a graph dimension |
| C-link | both keep-costs \(0\) | a nonzero difference | relabel, speculative |

Instrument: the diagonal of \(x^2\) matches the closed form within \(10^{-12}\) on \(n=1,\ldots,6\). A miss there is an instrument puzzle and voids P-well, logged, not repaired by editing this file.

## 8. What this run will not do

It will not edit `THEORY.md`, `CORE.md`, or this file. It will not say that quantum mechanics, general relativity, holography, or gravity has been derived. It will not treat a pass as an addition when the advance criterion says relabel or consistency check. It will not replace MINIMAL-RETURN with T81's chain. It will not fit the bars to the output. It will not score a truncation slope as Berry's \(3/2\).
