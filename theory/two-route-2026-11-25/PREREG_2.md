# Preregistration v2: two routes on the coupled world (supersedes the unscored v1 bars)

*Wednesday 25 November 2026 (America/New_York). Branch `forge-two-route-prereg`, after merging `main` `fa91b59`. This file supersedes the unscored bars of `PREREG.md` (A-T1, A-T3, B-T1, B-T2). `PREREG.md` stays locked as written (sha256 `9e42fe0a…9e54`, commit `b159d0f`), and its logged results stand: A-C1, A-C2, and A-T2, which was a miss of +0.145 run without a gate check, with the RI correction in `DEVIATIONS.md`. Gate per draft PR #263 (`process/PREREG_GATE.md` at `8c4b3c0`). It answers the independent gate read of #287: 5 blocking items, 14 non-blocking (§7). Locked in its own commit with `PREREG_2.sha256`. **No bar below runs until a fresh independent reader passes this Gate.** `THEORY.md`, `CORE.md` and the locked blobs are not edited. No real-world data.*

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

(Byte for byte from `CORE.md:7`.) Labels: **HYPOTHESIS** is a bet locked here. **OBSERVED** is on `main` or already logged in this folder. **PAPER** is a value computed by hand or by a closed-form one-line minimization, written here before any run.

## Gate

| ID | Label | G1 miss (honest odds) | G2 not an identity (paper attempt) | G3 rival: same quantity, its value, gap, resolution | G4 reach | G5 next step |
|---|---|---|---|---|---|---|
| A-C3 | **CONSISTENCY_CHECK** (not run) | — | Fails: \(p^*=\sqrt{\theta a kT/w}\), elasticity \(-1/2\) (`theory/FEEDBACK_FLOOR_2026-11-23.md:27`) | — | — | Logged only |
| A-C4 | **CONSISTENCY_CHECK** (not run) | — | Fails: §1.2. In W2, S3 and S4 are needed for a steady state at all (F3, F4). S2 is necessary and sufficient for a Boltzmann design distribution (CA1). The state-level pair is a joint equilibrium iff \(agD_M=\gamma cD\), and then both heats are 0 | — | — | Logged only |
| A-C5 | **CONSISTENCY_CHECK** (not run) | — | Fails: §1.3. With the friction lever free, CL11-cold has no minimizer (slowing the world is free). With the contact fixed at \(\eta=1\), PAPER elasticity is \(-0.507\) on the locked \(w\) grid, which RI's \(-1/2\) cannot be told apart from | — | — | Logged; CL11 needs a different family (§1.3) |
| **A-T1′** | **TEST** | \(G<0.10\), or no settling (odds 0.55) | Two-party design game on W2 with both bath heats: a Nash point of a non-potential, non-reversible game with no closed form. PAPER: one world best reply with \(\Sigma\) held is \(g\approx1.145\) (\(gc\approx0.68\)), §1.4 | **Joint-minimum reading** (the hypothesis read for the pair; CA1/CT31 with cost shares equal to stakes): \(G=0\). Gap to our band edge 0.10. Resolution 0.01. RI per party is the Nash point itself (§1.4), so it predicts the Nash number and does not separate | (b) `CORE.md:127` (coupling that settles); `CORE.md:80` (two baths) | Hit: BICAUSAL gets a sized Nash gap with both baths, and the reading per party is the scoped one. Miss (\(G<0.10\)): the per-party and joint readings agree in W2 to within 0.10, and the row says so. No settling: a W2 counterexample to settling for CX2 |
| B-C1 | **CONSISTENCY_CHECK** (not run) | — | Fails: CA1 regret \(d_i/(2\beta_i)\); joint efficiency iff cost shares equal stakes | — | — | Logged only |
| B-C2 | **CONSISTENCY_CHECK** (not run) | — | Fails: Theorem GB (`theory/GROWTH_BRIDGE.md:255`) | — | — | Logged only |
| B-C3 | **CONSISTENCY_CHECK** (run only as a code gate, §4) | — | Fails: equal strengths give a reversible chain, so the stochastic-potential minimizer is the global minimum (Freidlin–Wentzell) | — | — | Code gate: \(f\neq0\) at \(c=(1,1)\) fires a `measurement/code` location |
| B-C4 (was B-T1) | **CONSISTENCY_CHECK** (not run) | — | Fails G1: PAPER §1.5 gives \(R(k)\approx x^{*2}/k\) and \(X/R\approx40\), so the miss odds are about 0. Relabeled per the gate read | — | — | Logged only; the reading of §3 stays an unscored deliverable |
| **B-T2′** | **TEST** | \(f\notin[0.10,0.35]\) (odds 0.45) | Random-landscape enumeration of stochastic potentials; no closed form. PAPER heuristic, §1.6: \(f\approx0.1\)–\(0.2\) | Joint-minimum reading: \(f=0\), gap 0.10. Random-basin null: \(f=0.5\), gap 0.15. Resolution \(2\,\mathrm{SE}\le0.032\) at 1,000 qualifying draws. RI is silent: both basins are Nash points, which per-party RI does not rank | (b) `CORE.md:127`; `measurement/CLAIM_MAP_v2.md:890` (F6) | Hit: a size for how often mismatched strengths pick the worse Nash point. Miss: report \(f\) and its direction; the band was wrong |

**Gate summary (self-check; the binding check is the fresh independent reader).** Two TESTs, one per route, each scored against a rival that predicts the same number, with a gap of at least 0.10 on every scored number. Seven identities are labeled CONSISTENCY_CHECK and are not run, except B-C3 as a code gate. Every TEST has a PAPER attempt and honest odds. Reach is level (b) for both TESTs, cited to `CORE.md` lines.

**Dropped, with reason: a fresh A-T2′ memory-heat bar.** The W2 optimum curve over \(g\in\{0,\dots,0.9\}\) at \(w=10\) has been seen (`checks/route_a_w2.out`), and the corrected RI value (0.877) and the optimum ratio (1.045) are both known. A new memory-heat bar in the same family would be scored after seeing its trend. Its information would be about 0, so none is locked.

## 1. Paper attempts and identities

### 1.1 Model W2 (unchanged from `PREREG.md` §2.1)

\(dx=-a(x-gm)\,dt+\sqrt{2D}\,dW_x\), \(dm=-\gamma(m-cx)\,dt+\sqrt{2D_M}\,dW_m\). Heat into bath \(i\) is \(\dot Q_i=\mathbb E[f_i^2]+D_i\mathbb E[\partial_if_i]\), with \(kT_X=D\) and \(kT_M=D_M\). Reference: \(a=D=D_M=1\), capacity not binding.

### 1.2 A-C4 (identities, not run)

- Steady state needs the drift matrix \(\begin{pmatrix}a&-ag\\-\gamma c&\gamma\end{pmatrix}\) to be stable: \(\det=a\gamma(1-gc)>0\) (F3 analogue), and no delay past the Hayes bound (F4).
- A linear drift \(-Az\) with diagonal noise \(\mathcal D\) is in detailed balance iff \(\mathcal D^{-1}A\) is symmetric, that is \(ag/D=\gamma c/D_M\). On that set the pair is one joint equilibrium and \(\dot Q_X=\dot Q_M=0\). This confirms the gate read's check at \((\gamma,c,g)=(2,0.25,0.5)\) and \((1,0.5,0.5)\). v1's claim of "a nonzero cross term at \(gc\neq0\)" was false there.
- The design-level Boltzmann form holds iff the \(\beta\)-scaled design game is an exact potential (CA1, `theory/COADAPTATION.md:11-17`).

What is left of v1's A-T1 (S1, time-scale separation, and S5, convex capacity) is a derivation deliverable of the BICAUSAL work order (`OPEN_WORK.md:247`), not a scored bar. It has no rival that predicts a number.

### 1.3 A-C5: the CL11-cold family (paper, not run)

`PREREG.md` §2.5's family, \(dx=-\frac{x}{1+\eta}dt+\frac{\sqrt{2(T_0+\eta T_c)}}{1+\eta}dW\). The heat current into the cold bath is \(\dot Q_c=\eta(T_0-T_c)/(1+\eta)^2\) (unit stiffness, frictions 1 and \(\eta\)). The refrigerator is paid at \(W=\dot Q_c(T_0/T_c-1)\). Tracking costs \(J=kT_0L+W+wp\) with \(L=a(\theta/p-1)\), \(a=1/(1+\eta)\), \(\theta=(T_0+\eta T_c)/(1+\eta)\), which gives \(p^*=\sqrt{\theta aT_0/w}\).

- **The slowing loophole (gate read blocking 1).** As \(\eta\to\infty\), \(a\to0\) and \(\dot Q_c\to0\) for every \(T_c\le T_0\). So \(W\to0\), \(J^*\to0\) and \(p^*\to0\), and there is no minimizer. Bounding \(T_c<T_0\) strictly does **not** remove this: the heat current vanishes as \(1/\eta\) whatever \(T_c\) is. Friction slows the world, and a slow world is cheap to track. It is the passive-plant loophole of `CORE.md:80` in another form.
- **With the contact fixed at \(\eta=1\)** (design \(T_c\in(0,T_0]\) and \(L\)), \(J(T_c)=\sqrt{w(1+T_c)}-\tfrac12+(1-T_c)^2/(4T_c)\) at \(T_0=1\). This is strictly convex near its minimum, and the minimum is interior because \(W\to\infty\) as \(T_c\to0\). PAPER: optimal \(T_c\) goes from 0.1285 at \(w=10^3\) to 0.0225 at \(10^6\) (about \(w^{-1/4}\)). The least-squares slope of \(\ln p^*\) on \(\ln w\) over \(w\in\{10^3,10^{3.5},\dots,10^6\}\) is **\(-0.507\)**. The hot contact keeps a noise floor \(\theta\ge T_0/2\), so the scaling stays RI's \(-1/2\). The gap to RI (0.007) is inside the 0.01 resolution. v1's hypothesis (\(\le-0.6\)) would have missed on paper.
- **Consequence for CL11.** In a thermal world, cutting noise intensity is either free through slowing (no optimum) or leaves RI's scaling (bounded contact). A CL11 TEST needs a world whose noise is not thermal, an active driver, and that belongs in a later prereg. The CL11 row (`THEORY.md:37`, `measurement/CLAIM_MAP_v2.md:891`) stays open. This paragraph is a PAPER result for review, not a scored bar.

### 1.4 A-T1′ paper attempt

Parties: the memory picks \((\gamma,c)\) to minimize \(J_m=\dot Q_M+w\,\mathbb E[(x-m)^2]\). The world picks \(g\) to minimize \(J_w=\dot Q_X+w_w\,\mathbb E[(x-gm)^2]\), its own bath heat plus its own stake on being away from its copy target. Total \(J_{\mathrm{tot}}=J_m+J_w\). Stakes \(w=w_w=10\). Since \(\dot Q_X=a^2\mathbb E[(x-gm)^2]-aD\), \(J_w=(a^2+w_w)\mathbb E[(x-gm)^2]-aD\).

PAPER, one step: at the logged \(g=0\) memory optimum (\(\gamma=6.884\), \(c=0.592\); \(\Sigma_{xx}=1\), \(\Sigma_{xm}=0.5172\), \(\Sigma_{mm}=0.4516\)), the world's best reply with \(\Sigma\) held fixed is the regression slope \(g=\Sigma_{xm}/\Sigma_{mm}=1.145\), with \(gc=0.68<1\). \(\Sigma\) moves with \(g\), so this is only a first step.

The A-T2 table (`checks/route_a_w2.out`) shows the memory-side cost falling with \(g\) up to 0.9 at the re-optimized memory, so both the Nash point and the joint minimum may sit at high \(gc\), near the confinement boundary. That would make \(G\) small. Hence odds of a miss 0.55.

RI per party: each party optimizes against the other held fixed, which is the Nash best-response map. So RI predicts the Nash point and does not separate. The rival that predicts a different \(G\) is the joint reading.

**Scored:** \(G=J_{\mathrm{tot}}(\text{Nash})/\min J_{\mathrm{tot}}-1\). **HYPOTHESIS:** \(G\ge0.10\). **Rival:** \(G=0\). **Miss** if \(G<0.10\) (signed size \(G-0.10\)), or if no Nash point is found (§4), which is logged as an open miss with size "undefined", location model.

### 1.5 B-C4 (was B-T1), paper only

As in `PREREG.md` §3.3: the period-\(2\tau\) square wave between \(\pm x^*\), \(x^*=2\tanh x^*=1.915\), is stable (the composite map slope is \(4\,\mathrm{sech}^4x^*\approx0.03\)). That gives \(R(k)\approx x^{*2}/k\), so \(R(5)\approx0.73\) and \(R(20)\approx0.18\), and \(X(20)\approx2x^{*2}+R\approx7.5\). Not run. The reading of the hypothesis when coupling does not settle stays an unscored deliverable (`PREREG.md` §3.4).

### 1.6 B-T2′ paper heuristic

At \(c=(1,1)\), \(f=0\) (B-C3). With \(c=(1,3)\), a mismatch can only flip the selection when the two basins' cheapest escapes use different parties: the climb out of the lower basin is cheap for party 2's coordinate, while the climb out of the higher basin is cheap for party 1's. In a \(3\times3\) grid each party owns half the unilateral moves, so roughly a quarter to a half of two-basin draws have mixed escape parties. Within those, weighting by 3 flips the order when the two escape heights are within a factor of 3, which is common for uniform entries. Rough \(f\approx0.1\)–\(0.2\). This is a heuristic, not a bound, so the odds of a miss are 0.45.

**Scored:** \(f\), as in `PREREG.md` §3.5 (same landscape, seed `20261125`, 20,000 draws, same qualification rule). **HYPOTHESIS:** \(f\in[0.10,0.35]\). **Miss** if \(f<0.10\) (size \(f-0.10\)) or \(f>0.35\) (size \(f-0.35\)). Fewer than 1,000 qualifying draws gives INCONCLUSIVE.

## 2. Route A deliverables beyond the TEST (unscored)

The BICAUSAL work order, as written (`OPEN_WORK.md:247`): the bipartite pair, fixed noise, finite capacity, the update rule, symmetric entropy production on both baths, CA1/F3/F4 kept separate, the conditions for one object (§1.2 plus S1 and S5), and a counterexample (CE-a, CE-b or CE-c of `PREREG.md` §2.2). No area cap on frozen stock. T61's fixed-noise statements unchanged.

## 3. Route B deliverables beyond the TEST (unscored)

The CA5/F3/F4/F6 scope table, Nash regret against joint efficiency, and the reading when coupling does not settle (`PREREG.md` §3.1, §3.2, §3.4). No general convergence theorem.

## 4. Grid, tolerances and boundary rule (stated)

- **A-T1′ memory best reply.** Nelder–Mead from every start on the grid \(\ln\gamma\in\{-3,-2.5,\dots,5\}\) (17 values) × \(c\in\{-1,-0.75,\dots,3\}\) (17 values), with \(\gamma\in[e^{-3},e^{5}]\).
- **A-T1′ world best reply.** Bounded Brent on \(g\in[0,\min(2,\,0.95/c)]\) for \(c>0\) (\([0,2]\) for \(c\le0\)), after a 201-point pre-grid.
- **A-T1′ joint minimum.** Nelder–Mead over \((\ln\gamma,c,g)\) from the 17×17 grid × \(g\in\{0,0.25,\dots,2\}\) (9 values), under the same box and the confinement margin \(gc\le0.95\).
- **Boundary rule.** If either optimum lies on \(gc=0.95\) or on a box edge, the scored \(G\) is taken there and flagged as a boundary optimum. This rule is locked here.
- **Nash search.** Alternate best replies from \((\gamma,c,g)=(6.884,0.592,0)\), at most 200 rounds, stopping when the change in every design coordinate is below \(10^{-6}\). If it does not stop, run 200 more rounds with damping 0.5. If it still does not stop, the outcome is "no settling".
- **Tolerances.** \(10^{-6}\) on designs and \(10^{-8}\) relative on \(J\). Resolution check: rerun at half of each tolerance; a change in \(G\) over 0.01 means not resolved.
- **B-T2′.** Chu–Liu/Edmonds, own implementation, cross-checked by brute force on the first 200 qualifying draws. Code gate: at \(c=(1,1)\) the code must return \(f=0\) on the same draws, or the `measurement/code` location fires and B-T2′ is not scored. CPU cap 30 minutes.

## 5. Budget, order and stop rule

**Order:** (0) a fresh independent gate read of this file passes; (1) A-T1′; (2) B-T2′; (3) the unscored deliverables of §2 and §3. Each route gets one executor session and one independent review round. A TEST not scored inside its session is logged as a `process` miss with size "not reached". No bar runs before step 0. No scored number is recomputed under a changed model after it is logged; a changed model is a new prereg.

## 6. Shared criterion (balanced)

Score each route with

\[
S=2\times(\text{scope rows whose status changes after independent review})+1\times(\text{TESTs resolved}).
\]

Scope rows are BICAUSAL and CL11 for Route A, and CX2 and F6 for Route B. Each route has one TEST, so each has a maximum of 5. A status change counts in either direction: proved in a named class, or narrowed by a counterexample or a PAPER result. A TEST is **resolved** when its outcome is a HIT or a MISS (not INCONCLUSIVE, and not not-resolved by §4), **and** \(|\text{outcome}-\text{rival value}|>2\times\) the stated resolution (A-T1′: 0.02; B-T2′: \(2\,\mathrm{SE}\) of \(f\)). "No settling" in A-T1′ counts as resolved, because it differs from every rival. CONSISTENCY_CHECKs score 0. The higher \(S\) moved the core claim further. A tie is reported as a tie.

## 7. The gate read of #287 item by item

**Blocking.**

1. **A-T3 ill-posed.** Bounding \(T_c<T_0\) does not remove the loophole (§1.3). With the contact fixed, the answer is a PAPER value equal to RI's. So A-T3 is replaced by the identity A-C5, and the CL11 TEST is deferred to a family with a non-thermal world.
2. **B-T1 cannot miss.** Relabeled B-C4, CONSISTENCY_CHECK, not run. Its RI rival is dropped.
3. **A-T1 rival.** The iff splits into identities (A-C4) and unscored deliverables. The new TEST A-T1′ scores one number, \(G\), and its rival (\(G=0\)) predicts that same number, with a gap of 0.10. The false cross-term claim is corrected in §1.2.
4. **A-T2 rival value.** Corrected to 0.877 in `DEVIATIONS.md`. The logged miss stands, and no fresh A-T2′ is locked (reason in the Gate section).
5. **A-T2 before the gate read.** Logged as `FORGE-GATE-1` in `process/FAILURES.md`. §5 step 0 now comes before any run.

**Non-blocking.**

1. Gate not at the top: it is now at the top.
2. A-C1 computed although identities are not run: acknowledged. v2 runs no identity except B-C3, as a code gate.
3. No A-T2 paper attempt: the RI value is now computed in `DEVIATIONS.md`, and each v2 TEST has a PAPER attempt (§1.4, §1.6).
4. A-T3 reach cited only the CLAIM_MAP row: A-C5 cites `THEORY.md:37`.
5. B-T2's \(f=0\) rival already refuted by F6: F6 says the selection can differ from the lowest cost, but gives no size. \(f=0\) is kept as the simplest null of the joint reading, labeled weak, next to the random-basin null.
6. Self-check claimed a gap of at least 0.1 on every bar, false for B-T2: the band is now \([0.10,0.35]\), so the gap is at least 0.10.
7. §5 did not fix the order: the order is now fixed (§5), and the v1 deviation is logged.
8. §6 asymmetric and "resolved" undefined: both are now balanced (5 and 5) and defined.
9. `sha256sum -c` only passed from the repo root: `PREREG_2.sha256` names the bare file name, so it passes from this folder. The v1 file is locked and is not edited.
10. crossref.out in the lock commit: no action needed. v2 cites no new source.
11. Git shows commit order only: v2 adds the independent gate read between the lock and any run, which is a check on order by a second reader.
12. "09:05 ET" stamps: corrected by an appended line in `DEVIATIONS.md` and a note in `RESULTS.md`.
13. No grid in §4: the grid is now stated (§4).
14. The thermodynamics term the gate read flagged in RESULTS.md: kept, because it is a physics name, allowed by `process/PROCESS.md:39`. A note in `RESULTS.md` says so.
