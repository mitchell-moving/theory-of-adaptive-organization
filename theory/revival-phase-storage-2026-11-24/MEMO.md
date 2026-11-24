# T83 memo: quantum revivals and reversible phase storage

*Tuesday 24 November 2026. Self-check, not an independent review. The lock is `PREREG.md` (sha256 `0397c70ea558bdbd58e6a4657213c12aee7582d6deea3a555c862f5e4cdc0144`, commit `f97d11f`), before `revival_phase_checks.py`. That file was not edited after the commit. `THEORY.md` and `CORE.md` are unchanged.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The advance criterion is `PREREG.md:25`: a consistency check reproduces a cited result, a relabel is `CORE.md` §3 or the T73 pinch read on this well, and an addition would be a quantity \(J\) assigns that those results do not. No item below is an addition.

## Why this approach

**HYPOTHESIS, Chad's intuition, framed by Ace.** Reversible phase storage is a memory with no record and zero heat to keep. Cost is paid only at read-out or decoherence. The well is an input. The question is whether the cost says anything the revival, the fractal coefficients, the recurrence theorem, and Landauer 1961 do not already say.

## Can it fail

Can it fail: yes. Six cells did. Cheapest way: \(\tau=1/3\) missed \(1/3\), or the incommensurate return at \(t=2\pi\) reached \(0.5\). Neither of those happened. The miss is the \(q=7\) window.

## (a) Heat and the pinch

`CORE.md:70` states \(\dot Q_M\ge kT\,\dot I_M\) under a memory/world split and local detailed balance, or an Einstein relation. This well has no bath, so those hypotheses are not met. The floor does not assign a positive rate, and it does not by itself prove zero. The zero in `revival_phase_checks.out:39`–`:41` is \(Q_{\mathrm{keep}}=0\) with purity \(1\). That is a **relabel** of `CORE.md:78`: storage after a write, vanishing ongoing heat. It is consistent with Landauer 1961 (doi `10.1147/rd.53.0183`): heat is tied to irreversible erasure, and keeping the phases erases nothing. Landauer 1961 is not a measurement-cost paper. The measurement side is the pinch.

T73 writes \(J=\kappa I(W;M)+\kappa_D P_D+w L\) (`theory/pointer-basis-stakes-2026-11-24/MEMO.md:66`) and says an unmeasured state was not taken up (`:68`). With no pinch, both record terms are uncharged (`out:42`). A binary pinch of a pure state has entropy \(h(R)\): \(0\) at \(\tau=0\) within \(10^{-12}\) (`out:42`), and \(0.636514168295\) at \(\tau=1/3\) where \(R=1/3\) (`out:43`). Full energy dephasing of the flat window costs \(H=\ln 120=4.787491742782\) in one shot, with no \(\tau\) dependence (`out:45`). **Relabel** of the pinch. The cost does not add a keep-price the frozen sentence and Landauer do not already give.

## (b) Return share

T81's \(q(T)\) is the first-entrance fraction on a lazy path (`forge-record-ratio-measured` at `f625bb7`). It has no revival time. It is not used.

**MINIMAL-RETURN** (`PREREG.md:61`): \(R(\tau)=|\sum |c_n|^2\exp(-2\pi i n^2\tau)|^2\).

Locked shape, \(N=120\). Where \(q\) divides \(120\), \(R=1/N_c\) when a copy sits on the origin and \(R=0\) when \(q\equiv 2\pmod 4\): \(q=3\) gives \(1/3\) and \(N_c=3\) (`out:6`), \(q=4\) gives \(1/2\) and \(N_c=2\) (`out:8`), \(q=2\) gives \(0\) and \(N_c=1\) (`out:5`), \(q=8\) gives \(1/4\) and \(N_c=4\) (`out:22`). The modal wave matches the shifted copies to \(10^{-14}\) (`out:27`–`:29`). Between the peaks, nine irrational probes sit below \(0.012\) (`out:30`–`:38`). **Consistency check** of the Gauss sum proved in the preregistration. Not an addition.

**Puzzle.** The six \(q=7\) cells fail the \(10^{-9}\) bar (`out:16`–`:21`). \(N_c=7\) matches. \(R\) misses \(1/7\) by about \(0.003\) to \(0.004\). `PREREG.md:69` says \(120\) is a multiple of every \(q\le 8\). It is not: \(7\) does not divide \(120\). The file was not edited. An unscored sum at \(N=840\) gives \(R=0.142857142857\) (`out:52`). The shape stands when the residues are balanced. The locked window does not balance \(q=7\).

Berry's fractal of \(P(x)\) is not a dimension of \(R\). No Hausdorff number for \(R\) is claimed.

## (c) Dimension, and the two spectra

**Speculative.** Odd-mode \(|c_n|^2=8/(n^2\pi^2)\), slope \(-2\) (`out:50`). That is the input to Berry's \(D=(5-\beta)/2\), hence his \(D_{\mathrm{space}}=3/2\) (doi `10.1088/0305-4470/29/20/016`). A truncation slope was not scored. \(Q_{\mathrm{keep}}\) is \(0\) at \(\tau=0\) and at \(\tau=\sqrt 2/2\) (`out:51`). **Relabel** of `CORE.md:78` and of T54 at `CORE.md:161`. The dimension does not enter \(J\).

**Commensurate.** \(E_n=n^2\), \(R(2\pi)=1\) (`out:46`). Exact return at \(T_{\mathrm{rev}}\).

**Incommensurate.** \(E_n=n^2+\sqrt{p_n}\), \(R(2\pi)=0.116259270951\), and a later time reaches \(0.997501976263\) without hitting \(1\) (`out:47`). Both keep-costs stay \(0\). **Consistency check** of Bocchieri and Loinger 1957 and of Hogg and Huberman 1982. Not an addition.

**Perturbed basis.** On the matrix written in `PREREG.md:141`, \(\lambda=0\) returns exactly and \(\lambda=8\) returns \(0.472533712464\) at \(t=2\pi\), with a later maximum \(0.994552216198\) (`out:49`). See the deviation: that off-diagonal is not \(\langle x^2\rangle\). The integral of \(x^2\), unscored, gives \(0.929538906895\) and a later maximum \(0.989130295842\) (`out:53`), on the same side of every locked bar. Either matrix shows exact versus approximate recurrence of a finite basis. The keep-cost does not differ.

## Deviations

`DEVIATIONS.md`. The preregistration and the stored output are not edited to clear the six fails.

## What was not found

No term in \(J\) that the cited results do not already assign. The hypothesis, read on this well, is a relabel of frozen storage plus the pinch, and the return share is the known revival.
