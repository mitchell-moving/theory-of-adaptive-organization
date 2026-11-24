# PREREG T82: quasi-periodic worlds and torus memory

*24 November 2026 (UTC). Locked before `MEMO.md`, before any derivation, and before any script. Branch `forge-torus-memory`, cut from public upstream `main` `d2aeb8100e22870dc5aee2529356de970c82a820`. `THEORY.md` and `CORE.md` are not edited. A miss below is a puzzle to diagnose. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

**Chad's hypothesis.** A world driven by \(k\) independent phases at incommensurate frequencies has minimal sufficient state the torus \(T^k\), and the minimum of the tracking cost is a \(k\)-dimensional phase-only memory on that torus.

The hypothesis is the sentence under test. It is not a premise.

## Why this approach

The method is the same in every class: write the cost, find its minimum, and read off the design (`CORE.md:47`). The cost written here is the two-term record cost left open by T74, with the ratio \(q=\kappa_D/\kappa\) kept as a free nonnegative price (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md:9-15`; `theory/pointer-basis-stakes-2026-11-24/MEMO.md:64-68`):

\[
J=\kappa\,I+q\kappa\,P_D+w\,L,\qquad \kappa>0,\ q\ge 0,\ w>0,
\]

ruin slack. \(I\) is the classical memory coordinate, Shannon mutual information of the record (`CORE.md:52`). \(L\) is the mean squared decision loss of the cell below. \(P_D\) is defined in §2. It is not a quantum pinch, and this file does not fix the quantum ratio.

Two results already on the page could be the whole answer. On a per-mode loss the tracked count is one coordinate per mode that the stake pays for (`CORE.md:92`). On a sum loss the heat-optimal memory is one rank-one coordinate (`CORE.md:93`; Proposition G-sum, `theory/INFO_PHYSICS_GENERAL.md:191`, `:246`). The internal model principle says a regulator of a quasiperiodic disturbance carries a copy of that generator (`theory/THEOREMS.md:208-210`). `theory/TORUS.md` already records the torus as the state space of two phases and leaves a locking-cost hypothesis open (N45). This file does not rescore N45 and does not edit `theory/TORUS.md`.

The X post at `https://x.com/mathemetica/status/2125282454110109990` is context for the question (an autoencoder on two traveling waves learns a latent torus). It is known representation-learning behavior. It is not an input, not a measurement, and not evidence. No score may cite it.

## Can it fail: the forecast cell can come out one-dimensional, the sum cell can come out \(k\)-dimensional, \(P_D\) can refuse to equal \(I\), and a stake can move the Adler or Kuramoto threshold

Can it fail: a single angle with a \(C^1\) autonomous vector field can reproduce \(\cos t+\cos(\sqrt{2}\,t)\) on a time interval of length 1, which would kill the claim that the forecast memory has dimension 2. The sum cell fails the other way if a memory of both phases is strictly cheaper, at the same reconstruction loss, than a memory of the scalar sum. The identity \(P_D=I\) fails if the locked definition does not give it. Q2 fails if the coupling that changes the minimizing design is not the blind corner applied to the known order-parameter curve. Q3 fails if, with no payment rule added, the Adler bound or \(K_c=2/(\pi g(0))\) moves when the stake ratio changes from 1 to 4.

Cheapest way: exact comparisons at \(k=2\), one rational frequency pair and one irrational pair, one four-bin sum, one unequal-amplitude menu, the Adler equilibrium, one Lorentzian price point, and the stake pair \((1,4)\). No Monte Carlo, no fit, no embedding network.

## 0. Relabel criterion and beyond-Kuramoto criterion

Both are fixed before the derivation. A later memo may not tighten them.

**Relabel criterion.** The outcome is a RELABEL if every minimizing design's informative dimension equals one of these three, already on the page:

- **(R-sum)** dimension 1 on the current-sum cell, the shape of the sum-loss memory (`CORE.md:93`; `theory/INFO_PHYSICS_GENERAL.md:21`, `:191`, `:246`).
- **(R-mode)** the number of phases whose own loss saving beats their memory price, the shape of the per-mode count (`CORE.md:92`).
- **(R-hull)** the dimension of the orbit closure, which is the rank over \(\mathbb{Q}\) of the frequencies, the shape of the internal model principle (`theory/THEOREMS.md:208-210`).

A result is not a relabel only if, at a stake where every phase enters the loss with positive weight, the unique minimizer's informative dimension differs from all three by at least 1, or a radial coordinate with mutual information \(>0\) is required. RELABEL is a valid outcome. It is not a kill.

**Beyond-Kuramoto criterion.** Let \(K_{\mathrm{ref}}=|\Delta\omega|\) on the two-oscillator Adler cell, and \(K_c=2/(\pi g(0))\) on the mean-field cell. The cost is beyond Kuramoto only if the coupling \(K^\star\) at which the minimizing design changes satisfies all three of the following:

1. \(|K^\star-K_{\mathrm{ref}}|/\max(K_{\mathrm{ref}},10^{-12})>0.05\).
2. \(K^\star\) is not a function of \(K_{\mathrm{ref}}\) alone (it depends on \(\kappa\), \(q\), or \(w\)).
3. \(K^\star\) is not the unique coupling obtained by substituting the known amplitude \(r(K)\) into the blind corner already at `CORE.md:91` (do not track when the stake on the reducible loss does not beat the memory price), with that corner left unchanged.

A switch that sits on \(K_{\mathrm{ref}}\) for every price is not beyond. A switch that is exactly that substitution is not beyond, even if \(K^\star\neq K_c\). Tolerance on a later numerical check of a formula in this file is a relative gap of \(10^{-9}\).

## 1. World, two cells

Class QP. The memory does not move the world. \(\theta\in T^k=(\mathbb{R}/2\pi\mathbb{Z})^k\), \(\dot\theta=\omega\), invariant measure Haar. Incommensurate means \(m\in\mathbb{Z}^k\) and \(m\cdot\omega=0\) imply \(m=0\). Each oscillator radius is the constant 1 unless a cell names an amplitude. The observable in the symmetric cells is \(y=\sum_{j=1}^k\cos\theta_j\).

**Cell C, current sum.** \(L=\mathbb{E}[(a-y)^2]\). The action may use a simultaneous memory of a designer-chosen observation. Memory dimension is the dimension of the smallest manifold that carries the memory state, not the number of sensors.

**Cell F, forecast.** The action at time \(t\) is a function of the memory state alone. On \((t,t+\tau]\) the memory gets no new observation and may run only an autonomous flow of its own state. Zero loss for every \(\tau\) in an open interval requires that state to determine the future of \(y\).

Frequencies locked for the checks: irrational pair \((1,\sqrt{2})\); rational pair \((1,3/2)\).

## 2. What \(I\), \(P_D\), and \(L\) are

\(I(W;M)\) is Shannon mutual information when the record is discrete, and the differential mutual information when that integral is finite (`CORE.md:52`). The representation is not applied to an infinite mutual information.

\(P_D\) is the expected Kullback–Leibler divergence of the posterior of \(\theta\) given \(M\) from the Haar probability on the torus. It is the classical dephasing score: distance from the posterior to the fully mixed phase. It is not the quantum pinch of T73, and it is not used to name a quantum price.

\(L\) is the mean squared error named in the cell. On a discrete phase-bit menu the losses are the exact values in §4, from independence of the Haar coordinates and \(\mathbb{E}[\cos^2\theta_j]=1/2\).

## 3. Prior art, logged before the derivation

Crossref, queried 24 November 2026. A DOI is cited only when that query returned the title and the author.

- Kuramoto, "Self-entrainment of a population of coupled non-linear oscillators," pages 420–422, DOI `10.1007/BFb0013365`. Container: Lecture Notes in Physics / International Symposium on Mathematical Problems in Theoretical Physics. The chapter record's issued field is empty. The symposium volume, DOI `10.1007/BFb0013294`, is issued 1975. This is the 1975 citation.
- Kuramoto, *Chemical Oscillations, Waves, and Turbulence*, Springer Series in Synergetics, DOI `10.1007/978-3-642-69689-3`, issued 1984.
- Strogatz, "From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators," *Physica D* 143, pages 1–20, DOI `10.1016/S0167-2789(00)00094-4`, issued 2000.
- Acebrón, Bonilla, Pérez Vicente, Ritort, and Spigler, "The Kuramoto model: A simple paradigm for synchronization phenomena," *Reviews of Modern Physics* 77, pages 137–185, DOI `10.1103/RevModPhys.77.137`, issued 2005. The spelling Acebrón is the Crossref spelling.
- Arnold, "Small denominators. I. Mapping of the circumference onto itself," *Collected Works*, pages 152–223, DOI `10.1007/978-3-642-01742-1_10`, issued 2009. This is the reprint Crossref returns. No 1961 DOI was verified, and none is cited. Arnold tongues are this circle-map theory.
- Francis and Wonham, "The internal model principle of control theory," *Automatica* 12, pages 457–465, DOI `10.1016/0005-1098(76)90006-6`, issued 1976. Already the citation at `theory/THEOREMS.md:208`.

The critical coupling in the question is the one those Kuramoto reviews state for the infinite-\(N\) model, \(K_c=2/(\pi g(0))\). For the Lorentzian \(g(\omega)=(\gamma/\pi)/(\omega^2+\gamma^2)\), \(g(0)=1/(\pi\gamma)\), so \(K_c=2\gamma\). For \(K>K_c\) the amplitude used below is the standard Lorentzian reduction \(r=\sqrt{1-K_c/K}\), and \(r=0\) for \(K\le K_c\). Adler's equation \(\dot\varphi=\Delta\omega-K\sin\varphi\) locks if and only if \(|\Delta\omega|\le K\). Both are inputs from that literature, not results of this cost.

Repo text already in hand, not re-derived here: `theory/TORUS.md:7-9` and `:45-51` (torus as the state of two phases; N45 open); `theory/THEOREMS.md:236-238` (Adler and \(K_c=2\gamma\), already checked there). This preregistration does not reuse those checks as a score.

## 4. Locked predictions

Expectations only. The memo recomputes them. If one misses, the memo records a puzzle and does not edit this file.

**P1, cell C, sum.** Four equal bins on each circle, centers \(\pi/4,3\pi/4,5\pi/4,7\pi/4\). Each center has cosine \(\pm\sqrt{2}/2\). The sum of the two bin-center cosines takes at most the three values \(\sqrt{2},0,-\sqrt{2}\). The phase-bin memory has entropy \(\ln 16\). A memory that stores only that sum has entropy at most \(\ln 3<\ln 16\). Both memories output the same reconstruction, so they have the same \(L\). At every \(\kappa(1+q)>0\) the scalar memory has strictly smaller \(J\). The cost minimum on this cell is not a 2-dimensional phase memory. Shape (R-sum).
Fails if the distinct sums number more than 3, if \(\ln 3\ge\ln 16\), or if the two memories do not share one reconstruction loss.

**P2, cell F, hull.** \(\cos t+\cos(\sqrt{2}\,t)\) is not periodic: a common period would make \(\sqrt{2}\) rational. The rank of \((1,\sqrt{2})\) over \(\mathbb{Q}\) is 2. The rank of \((1,3/2)\) over \(\mathbb{Q}\) is 1, and \(\cos t+\cos(3t/2)\) has period \(4\pi\). Zero-loss forecast dimension equals that rank. Shape (R-hull). Phase-only: a coordinate frozen at a constant has mutual information 0, so a radius is not required. It ties if it is stored for free. It is not uniquely demanded.
Fails if \(\sqrt{2}=p/q\) for integers \(q>0\), or if the rational pair has no period \(4\pi\), or if a constant coordinate has mutual information \(>0\).

**P3, one price.** Under the definition in §2, \(P_D=I(\theta;M)\) whenever the prior is Haar and the mutual information is finite, so \(J=\kappa(1+q)I+wL\). The factor \(q\) rescales \(\kappa\). It is not a second coordinate.
Fails if that equality is false under §2.

**P4, symmetric bit menu.** Two independent fair phase bits, \(k=2\), \(y=\cos\theta_1+\cos\theta_2\). Rows: blind \((I,L)=(0,1)\); one phase \((\ln 2,\ 1/2)\); both \((2\ln 2,\ 0)\); and \(P_D=I\) on each row. The one-phase row is never the unique minimizer. All three tie if and only if \(w=2\kappa(1+q)\ln 2\). Below that, blind is unique. Above it, both is unique.
Fails if, at \(\kappa=1\), \(q=0\), \(w=10\), the unique minimizer is not both, or at \(w=1\) the unique minimizer is not blind, or the one-phase row is unique at any \(\kappa>0\), \(q\ge 0\), \(w>0\).

**P5, unequal amplitudes, the per-mode shape.** \(y=\cos\theta_1+0.1\cos\theta_2\), same bit menu, \(P_D=I\). Loss savings \(1/2\) and \(0.005\). Track a phase when \(w\) times its saving exceeds \(\kappa(1+q)\ln 2\). Thresholds \(w_1=2\kappa(1+q)\ln 2\) and \(w_2=200\kappa(1+q)\ln 2\). At \(\kappa=1\), \(q=0\): blind for \(w=1\), large phase only for \(w=10\), both for \(w=1000\). Informative dimension at \(w=10\) is 1, not 2. Shape (R-mode). This is the witness that "always \(T^k\)" is false inside the forecast menu once a small phase is not worth its price.
Fails if the unique minimizer at those three stakes is anything else.

**P6, rational versus irrational, and locking.** Rational versus irrational matters exactly as P2: the zero-loss dimension is the rank over \(\mathbb{Q}\). Mode locking lowers that dimension when it merges phases. Adler: the merge starts at \(|\Delta\omega|\), not at a shifted value. On the discrete copy, the information of one fair bit per free phase drops by \(\ln 2\) when two phases become one, and the cost drops by \(\kappa(1+q)\ln 2\) if \(L\) stays 0.
Fails if the Adler equilibrium condition is not \(|\Delta\omega|\le K\), within absolute error \(10^{-12}\) on the identity \(\sin\varphi=\Delta\omega/K\).

**P7, Kuramoto comparison.** Lorentzian, \(\gamma=1/2\), so \(K_c=1\), \(r^2=1-K_c/K\) for \(K>K_c\). The mean field has reducible loss \(r^2/2\). One phase bit costs \(\kappa(1+q)\ln 2\) and drives that loss to 0. Tracking pays when \(w r^2/2>\kappa(1+q)\ln 2\), that is

\[
K^\star=\frac{K_c}{1-2\kappa(1+q)\ln 2/w}
\]

when \(w>2\kappa(1+q)\ln 2\), and never when \(w\) is smaller. At the locked point \(\kappa=1\), \(q=1\), \(w=10\), the script evaluates this expression. By §0 this \(K^\star\) is the blind-corner substitution, so the beyond-Kuramoto criterion returns NOT BEYOND, including if \(K^\star\neq K_c\).
Fails if the minimizer over \(K\) of the two-design menu (blind versus one phase bit) differs from that expression by a relative gap above \(10^{-9}\), or if the criterion as written in §0 returns BEYOND on this point.

**P8, alignment, what must match.** If the phase memory and the swarm alignment term share a cause, all three of the following hold, and they are the whole match. Citations are on this tree:

- M1. The part's choice equals the whole's optimum if and only if \(s_i=w_i/W\) (`theory/SWARM_RULE_2026-11-23.md:47`; `THEORY.md:486`).
- M2. At that share the part's cost equals \((w_i/W)\) times the whole's cost (`theory/SWARM_RULE_2026-11-23.md:73`; `THEORY.md:491`).
- M3. Equal shares fail M1 when the stakes differ. Locked stakes \(w=(1,4)\).

Prediction: Adler's bound and \(K_c=2/(\pi g(0))\) contain no stake. Changing the stake ratio from 1 to 4 does not move either threshold. M1–M3 therefore fail on the bare phase vector field. They hold after the CT29 payment rule is copied onto a shared coupling budget, and that copy is a RELABEL of CT29, not a consequence of the phase flow. Q3 as a shared cause is a FAIL. The copied payment rule is not scored as support.
Fails if, with no payment rule added, \(|\Delta\omega|\le K\) or \(K_c=2/(\pi g(0))\) changes when the stake ratio changes from 1 to 4.

**Headline, predicted before the run.** RELABEL. Cell C is (R-sum), not a \(k\)-dimensional memory. Cell F's zero-loss dimension is (R-hull). The unequal menu is (R-mode) and is not \(T^k\) at \(w=10\). Q2's coupling is NOT BEYOND. Q3's shared cause FAILS; the payment-rule copy is a relabel of the alignment clause. Chad's hypothesis, read as one sentence that the cost minimum is always a \(k\)-dimensional phase-only memory, is false on cell C and on P5. The part that survives is the hull dimension of a zero-loss forecast, and that part is (R-hull).

## 5. What this file does not do

It does not score P1–P8. It does not edit `THEORY.md`, `CORE.md`, or `OPEN_WORK.md`. Deviations, if any, are appended to `DEVIATIONS.md` in this directory. This file is not edited after the locking commit.
