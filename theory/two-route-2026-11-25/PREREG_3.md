# Preregistration v3: two routes on the coupled world (supersedes A-T1′ only)

*Wednesday 25 November 2026 (America/New_York). Branch `forge-two-route-prereg`. Append-only update to `PREREG_2.md` (lock `64c8b53`, sha256 `57d1caab…e01ce293`, untouched) and `PREREG.md` (lock `b159d0f`, sha256 `9e42fe0a…9e54`, untouched). This file supersedes **A-T1′ only** (relabeled **A-T1″**) to answer the 1 blocking item and the non-blocking/wording items of the v2 independent gate read (`gate_read_287_v2.md`). All other items from `PREREG_2.md` (A-C3, A-C4, A-C5, B-C1, B-C2, B-C3, B-C4, B-T2′, §1.1–§1.3, §1.5–§1.6, §2, §3, §5, §7, and the dropped A-T2′ entry) carry over by reference. Gate per draft PR #263 (`process/PREREG_GATE.md` at `8c4b3c0`). Locked in its own commit with `PREREG_3.sha256`. **Nothing in A-T1″ or B-T2′ runs until a fresh independent reader passes this Gate.** `THEORY.md`, `CORE.md` and the locked blobs are not edited. No real-world data.*

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

(Byte for byte from `CORE.md:7`.) Labels: **HYPOTHESIS** is a bet locked here. **OBSERVED** is on `main` or already logged in this folder. **PAPER** is a value or identity computed by hand or by a closed-form one-line minimization before any run.

## Gate

| ID | Label | G1 miss (honest odds) | G2 not an identity (paper attempt) | G3 rival: same quantity, its value, gap, resolution | G4 reach | G5 next step |
|---|---|---|---|---|---|---|
| A-C3 | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: \(p^*=\sqrt{\theta a kT/w}\), elasticity \(-1/2\) (`theory/FEEDBACK_FLOOR_2026-11-23.md:27`) | — | — | Logged only |
| A-C4 | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: `PREREG_2.md` §1.2 (F3, F4, CA1; detailed balance iff \(agD_M=\gamma cD\)) | — | — | Logged only |
| A-C5 | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: `PREREG_2.md` §1.3 (CL11-cold: no minimizer with \(\eta\) free; at \(\eta=1\), PAPER slope \(-0.507\) vs RI \(-1/2\)) | — | — | Logged; CL11 needs a non-thermal family |
| **A-T1″** (supersedes A-T1′) | **TEST** | \(G<0.10\), or no settling (odds 0.50) | Two-party design game on W2 with both bath heats and world state-excursion cost \(w_x\mathbb E[x^2]\) (\(w_x=1\)): a Nash point of a non-potential, non-reversible game with no closed form. PAPER (§1.4): at the logged \(g=0\) memory optimum, the 1-step world best reply is interior at \(g\approx0.9686\) (\(gc\approx0.5737\)); along \(g=c\), \(\min_\gamma J_{\mathrm{tot}}\) is interior near \(gc\approx0.7\) (\(14.20\), rising to \(27.11\) at \(gc=0.95\) and \(94.53\) at \(gc=0.99\)) | **Joint-minimum reading (weak)** (the hypothesis read for the pair; CA1/CT31 with cost shares equal to stakes): \(G=0\), labeled **weak** because each party's cost omits its externality on the other by construction, so \(G=0\) holds only by coincidence. No prior rival predicts a value in \((0,0.10)\); a miss in \((0.02,0.10)\) rejects both \(G\ge0.10\) and \(G=0\) together. Gap to our band edge: 0.10. Resolution: 0.01 (resolved threshold \(2\times0.01=0.02\)). RI per party is the Nash best-response map itself, so it predicts the **Nash point** and is silent on \(G\) | (b) `CORE.md:127` (coupling that settles); `CORE.md:80` (two baths); `CORE.md:27` (confinement / ruin constraint) | Hit (\(G\ge0.10\)): BICAUSAL gets a sized Nash gap with both baths under confinement, and the reading per party is the scoped one. Miss (\(G<0.10\)): the per-party and joint readings agree in W2 to within 0.10, and the row records it. No settling: a W2 counterexample to settling for CX2 |
| B-C1 | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: CA1 regret \(d_i/(2\beta_i)\); joint efficiency iff cost shares equal stakes | — | — | Logged only |
| B-C2 | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: Theorem GB (`theory/GROWTH_BRIDGE.md:255`) | — | — | Logged only |
| B-C3 | **CONSISTENCY_CHECK** (carried from v2; code gate only, §4) | — | Fails G2: equal strengths give a reversible chain, so the stochastic-potential minimizer is the global minimum (Freidlin–Wentzell) | — | — | Code gate: \(f\neq0\) at \(c=(1,1)\) fires a `measurement/code` location |
| B-C4 (was B-T1) | **CONSISTENCY_CHECK** (carried from v2, not run) | — | Fails G2: PAPER `PREREG_2.md` §1.5 gives \(R(k)\approx x^{*2}/k\) and \(X/R\approx 40\) from the locked map (and fails G1 with miss odds \(\approx 0\)). Relabeled per #263 and the v1 gate read | — | — | Logged only; the reading of §3 stays an unscored deliverable |
| **B-T2′** | **TEST** (carried from v2) | \(f\notin[0.10,0.35]\) (odds 0.45). Lower edge 0.10 is kept only for the 0.10 gap rule against \(f=0\), not on theoretical grounds | Random-landscape enumeration of stochastic potentials; no closed form. PAPER heuristic, `PREREG_2.md` §1.6: \(f\approx0.1\)–\(0.2\) | Joint-minimum reading: \(f=0\) (**weak** — qualitatively contrary to F6, kept only as the zero-mismatch baseline), gap 0.10. Random-basin null (primary non-weak rival): \(f=0.5\), gap 0.15. Stated resolution: \(2\,\mathrm{SE}\le0.032\) at 1,000 qualifying draws (\(\mathrm{SE}\le0.016\)). RI is silent: both basins are Nash points, which per-party RI does not rank | (b) `CORE.md:127`; `measurement/CLAIM_MAP_v2.md:890` (F6) | Hit: a size for how often mismatched strengths pick the worse Nash point. Miss: report \(f\) and its direction; the band was wrong |

## 1. Paper justification of the A-T1″ fix (superseding `PREREG_2.md` §1.4)

### 1.1 Why the v2 joint minimum hit `gc = 0.95`, and comparison of the three candidate fixes

In W2 (`PREREG_2.md` §1.1, \(a=D=D_M=1\)), solving the \(2\times2\) Lyapunov equation \(A\Sigma+\Sigma A^\top=2\,\mathrm{diag}(1,1)\) with \(A=\begin{pmatrix}1&-g\\-\gamma c&\gamma\end{pmatrix}\) on \(\gamma>0,\,gc<1\) in closed form gives:

\[
\Sigma_{xm}=\frac{g+\gamma^2 c}{\gamma(1+\gamma)(1-gc)},\qquad
\Sigma_{xx}=1+\frac{g(g+\gamma^2 c)}{\gamma(1+\gamma)(1-gc)},\qquad
\Sigma_{mm}=\frac{1}{\gamma}+\frac{c(g+\gamma^2 c)}{\gamma(1+\gamma)(1-gc)},
\]

\[
\dot Q_X=\frac{g(g-\gamma c)}{1+\gamma},\qquad
\dot Q_M=\frac{\gamma c(\gamma c-g)}{1+\gamma},\qquad
\mathbb E[(x-gm)^2]=1+\frac{g(g-\gamma c)}{1+\gamma},
\]

\[
\mathbb E[(x-m)^2]=1+\frac{1}{\gamma}+\frac{(g+c-2)(g+\gamma^2 c)}{\gamma(1+\gamma)(1-gc)}.
\]

(Cross-checked at `DEVIATIONS.md:10-11` for \(\gamma=6.884105, c=0.592273, g=0.5\): \(\dot Q_M=1.849987\) and \(\mathbb E[(x-gm)^2]=0.773134\) agree to 6 decimal places.)

Under `PREREG_2.md` §1.4, \(J_m=\dot Q_M+w\mathbb E[(x-m)^2]\) and \(J_w=\dot Q_X+w_w\mathbb E[(x-gm)^2]\) (\(w=w_w=10\)). Neither \(\dot Q_X\), \(\dot Q_M\), nor \(\mathbb E[(x-gm)^2]\) contains \((1-gc)^{-1}\), and along the diagonal \(g=c\to 1^-\) the factor \((g+c-2)/(1-gc)=-2/(1+g)\to -1\) cancels the \((1-gc)\) pole in \(\mathbb E[(x-m)^2]\). Physically, at \(g=c=1\) both \((x-m)^2\) and \((x-gm)^2\) are invariant under simultaneous shifts \((x,m)\mapsto(x+\Delta,m+\Delta)\), so the slow mode wanders to \(\Sigma_{xx},\Sigma_{mm}\to\infty\) while \(J_{\mathrm{tot}}\) falls monotonically to the non-ergodic F3 boundary infimum \(\lim_{g=c\to 1^-}J_{\mathrm{tot}}=\min_{\gamma>0}\frac{(1-\gamma)^2+2w+2w_w}{1+\gamma}=2\sqrt{44}-4\approx 9.2665\). Thus any hard margin \(gc\le M<1\) sets \(\min J_{\mathrm{tot}}\).

Evaluating the three candidate fixes on paper before any run:

1. **(i) A model-derived limit on \(gc\): rejected.** W2 (`PREREG_2.md` §1.1) has no finite parameter-free bound on \(gc\) below \(1\); stability requires only \(\det A=\gamma(1-gc)>0\) (F3). Any hard cap on \(gc\), \(\Sigma_{xx}\), or \(I(X;M)\) still chooses an arbitrary cutoff number on which the joint optimum sits.
2. **(iii) A bar on the limit \(M\to 1^-\): rejected.** Although \(\min_{gc\le M}J_{\mathrm{tot}}\) converges to \(2\sqrt{44}-4\approx 9.2665\) as \(M\to 1^-\), it does so only at the non-ergodic F3 boundary where \(\Sigma_{xx}\to\infty\) and \(I(X;M)=-\frac{1}{2}\ln(1-\rho_{xm}^2)\sim\frac{1}{2}\ln\frac{1}{1-gc}\to\infty\). Moreover, under `PREREG_2.md` §1.4, \(J_w(g)=w_w+\frac{1+w_w}{1+\gamma}g(g-\gamma c)\) has unconstrained minimizer \(g=\gamma c/2\), which hits the ceiling \(M/c\) whenever \(\gamma c^2>2M\) (already true at the \(g=0\) memory optimum, where \(\gamma c^2=2.415>2\)). Consequently the world's best reply itself hits \(gc=M\), and Nash convergence as \(M\to 1^-\) cannot be established on paper without running the Nash search across \(M\) (which would score the bar).
3. **(ii) A model-motivated cost term that diverges as \(gc\to 1^-\): chosen.** Add the world's quadratic state-excursion / ruin-confinement cost \(w_x\,\mathbb E[x^2]\) to \(J_w\) with unit reference stake \(w_x=1\) (matching \(a=D=D_M=1\)):

\[
J_w=\dot Q_X+w_w\,\mathbb E[(x-gm)^2]+w_x\,\mathbb E[x^2],\qquad w_w=10,\; w_x=1,
\]

with \(J_m=\dot Q_M+w\,\mathbb E[(x-m)^2]\) (\(w=10\)) and \(J_{\mathrm{tot}}=J_m+J_w\) unchanged otherwise. Justification from the model (not added just to rescue the test):
- **Confinement / ruin anchor:** In W2 at \(g=0\), the world's uncoupled equilibrium is \(x=0\) with \(\mathbb E[x^2]=D/a=1\), and `CORE.md:5, 27, 66` subjects the physical cost to a ruin/confinement constraint on excursions. `PREREG_2.md` priced only \((x-gm)^2\), creating the translation zero mode at \(g=c=1\). Including \(w_x\mathbb E[x^2]\) removes that unphysical zero mode.
- **Divergence everywhere on \(gc\to 1^-\):** Because \(g(g+\gamma^2 c)>0\) whenever \(gc>0\), \(\Sigma_{xx}\sim(1-gc)^{-1}\to+\infty\) as \(gc\to 1^-\) for every pair \((g,c)\) with \(gc\to 1^-\). Thus \(J_w\to+\infty\) and \(J_{\mathrm{tot}}\to+\infty\) everywhere on \(gc\to 1^-\), and \(J_{\mathrm{tot}}\to+\infty\) as \(\gamma\to 0^+\), forcing a strictly interior minimum on \(\{\gamma>0,\,gc<1\}\) with no artificial \(gc\le 0.95\) margin.
- **Fixes the v2 row-16 stake degeneracy:** \(\partial J_w/\partial g|_{g=0}=-\frac{(1+w_w-w_x)\gamma c}{1+\gamma}<0\) for \(w_x=1<11\) (when \(c>0\)), so feedback \(g>0\) remains advantageous, and \(w_w=10\) now enters the world's best-reply equation alongside \(w_x=1\) rather than cancelling out.

### 1.2 A-T1″ paper attempt and restatement under G1–G5 (no Nash search run, no \(G\) computed)

- **PAPER 1-step world best reply** (at the logged \(g=0\) memory optimum \(\gamma=6.884105, c=0.592273\)): minimizing \(J_w(g)\) over \(g\in[0,1/c)\) gives the strictly interior point \(g\approx0.9686\) (\(gc\approx0.5737\), \(J_w\approx8.0144\)), instead of the boundary-hitting \(g=2.038\) (\(gc=1.207>1\)) without \(w_x\).
- **PAPER 1D well-posedness probe** (optimizing \(\gamma\) along \(g=c\), the same probe used in `gate_read_287_v2.md` row 15): \(\min_\gamma J_{\mathrm{tot}}\) equals \(15.94\) at \(gc=0.25\) (\(\Sigma_{xx}=1.30\)), \(14.42\) at \(gc=0.50\) (\(\Sigma_{xx}=1.89\)), reaches an interior minimum near \(gc\approx0.70\) (\(14.20\), \(\Sigma_{xx}=3.06\)), and rises monotonically to \(15.01\) (\(gc=0.80\)), \(18.74\) (\(gc=0.90\)), \(27.11\) (\(gc=0.95\)), and \(94.53\) (\(gc=0.99\)).
- **Paper justification of miss odds (0.50):** In the interior valley around \(gc\approx0.5\)–\(0.7\), \(J_{\mathrm{tot}}\) is smooth with \(\min J_{\mathrm{tot}}\sim 14\), so moderate displacements between the Nash point and the joint minimizer can leave \(G<0.10\); conversely, each player omits a large stake borne by the other (\(J_w\) omits \(w\mathbb E[(x-m)^2]+\dot Q_M\), and \(J_m\) omits \(w_x\mathbb E[x^2]+w_w\mathbb E[(x-gm)^2]+\dot Q_X\)), which can push \(G\ge 0.10\). Honest miss odds: **0.50**.
- **Scored:** \(G=J_{\mathrm{tot}}(\text{Nash})/\min J_{\mathrm{tot}}-1\). **HYPOTHESIS:** \(G\ge0.10\). **Rival:** \(G=0\) (**weak**; no prior rival predicts a number in \((0,0.10)\)). **Gap:** \(0.10\). **Resolution:** \(0.01\) (resolved iff \(|G-0|>0.02\) and §4 tolerance passes, or `"no settling"`). **Miss** if \(G<0.10\) (signed size \(G-0.10\)) or `"no settling"` (open miss, size `"undefined"`, location `model`).

## 2. Updates to `PREREG_2.md` §4 and §6 (other sections carried over by reference)

### 2.1 Grid, boxes, and boundary rule for A-T1″ (replaces `PREREG_2.md` §4 lines 81–86; line 87 for B-T2′ unchanged)

- **Boxes (stated on all coordinates):** \(\ln\gamma\in[-3,5]\), \(c\in[-2,3]\), \(g\in[0,3]\), with numerical stability guard \(gc\le0.999\) solely to keep the Lyapunov solver away from the singular line \(gc=1\) (where \(J_{\mathrm{tot}}>900\) along \(g=c\), vs \(\sim 14\) in the interior).
- **A-T1″ memory best reply:** Nelder–Mead from every start on the \(17\times 17\) grid \(\ln\gamma\in\{-3,-2.5,\dots,5\}\times c\in\{-1,-0.75,\dots,3\}\) inside the box above and \(gc\le0.999\).
- **A-T1″ world best reply:** 201-point pre-grid plus bounded Brent on \(g\in[0,\min(3,\,0.999/c)]\) for \(c>0\) (\([0,3]\) for \(c\le0\)).
- **A-T1″ joint minimum:** Nelder–Mead over \((\ln\gamma,c,g)\) from the \(17\times 17\) grid \(\times\, g\in\{0,0.25,\dots,2\}\) (9 values) inside the box and \(gc\le0.999\).
- **Boundary rule:** Both the joint minimum and the Nash point must be strictly interior to the stated box and satisfy \(gc<0.999\). If any optimum hits a box edge or \(gc=0.999\), A-T1″ is flagged as **not resolved / boundary-hit** (logged as an open miss, not scored on the boundary).
- **Nash search and tolerances:** Alternate best replies from \((\gamma,c,g)=(6.884,0.592,0)\), max 200 undamped rounds (stop when every coordinate changes by \(<10^{-6}\)), then up to 200 rounds with damping \(0.5\); if still not stopped, outcome is `"no settling"`. Tolerances \(10^{-6}\) on design coordinates and \(10^{-8}\) relative on \(J\); resolution check reruns at half of each tolerance (change in \(G>0.01\) means not resolved).

### 2.2 Shared criterion (`PREREG_2.md` §6 clarified)

\[
S=2\times(\text{scope rows whose status changes after independent review})+1\times(\text{TESTs resolved}).
\]

- **Carried over:** Scope rows are BICAUSAL and CL11 for Route A, and CX2 and F6 for Route B (max 5 per route). `CONSISTENCY_CHECK`s score 0. Higher \(S\) moved the core claim further; a tie is reported as a tie.
- **No pre-banked PAPER points:** The PAPER results already written in `PREREG_2.md` §1.3 (A-C5 / CL11-cold) and §1.5 (B-C4) do **not** count as scope-row status changes toward \(S\). Only status changes established by the new runs and deliverables under this prereg after independent review count.
- **Definition of "resolved" (unambiguous):** A TEST is **resolved** when its outcome is a HIT or a MISS (neither INCONCLUSIVE nor not-resolved by §2.1 / `PREREG_2.md` §4), **and**:
  - for **A-T1″**, \(|G-0|>0.02\) (\(2\times\) the stated \(0.01\) resolution), or the outcome is `"no settling"` (which differs from every rival);
  - for **B-T2′**, \(|f-0.5|>4\,\mathrm{SE}\) (\(2\times\) the stated \(2\,\mathrm{SE}\) resolution, i.e., \(>0.064\) at \(n=1{,}000\) qualifying draws), **measured from the non-weak rival \(f=0.5\)** (the random-basin null, not from the weak \(f=0\) baseline).
- **Note on B-T2′ lower edge:** As stated in the Gate table, B-T2′'s lower edge \(0.10\) is carried over from `PREREG_2.md` and kept **only** to satisfy the \(0.10\) gap rule against \(f=0\), not on theoretical grounds; it sits at the low end of `PREREG_2.md` §1.6's paper heuristic (\(f\approx 0.1\)–\(0.2\)).

### 2.3 Carried-over sections

`PREREG_2.md` §1.1 (Model W2), §1.2 (A-C4), §1.3 (A-C5), §1.5 (B-C4), §1.6 (B-T2′ paper heuristic), §2 (Route A deliverables beyond the TEST), §3 (Route B deliverables beyond the TEST), §4 line 87 (B-T2′ procedure, code gate, CPU cap), §5 (Budget, order and stop rule: step 0 fresh gate read of this file, then (1) A-T1″, (2) B-T2′, (3) §2 and §3 deliverables), and §7 (gate-read log for v1) stand by reference.
