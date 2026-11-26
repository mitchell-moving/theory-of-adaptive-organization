# Preregistration: two routes on the coupled world (Route A two-way, Route B selection)

*Wednesday 25 November 2026 (America/New_York). Locked before any derivation, check script or run on this branch (`forge-two-route-prereg`, cut from `main` `4f17326`). Lock-before-data per `process/PROCESS.md:17` and `:26`: this file and its `PREREG.sha256` go in their own commit, and nothing scored below is computed before that commit. `THEORY.md`, `CORE.md` and the locked blobs are not edited. No real-world data is used; every bar is in-model. Deviations go in `DEVIATIONS.md` in this folder as appended lines only. A self-written prereg; the `Gate` section still needs a separate reader (draft PR #263).*

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

The sentence is copied byte for byte from `CORE.md:7` and is not changed here. Everything below is labeled **HYPOTHESIS** (a bet locked here, not a result) or **OBSERVED** (on `main` at `4f17326`, with a file and line). Nothing here is a field result.

## 0. Scope and sources

The queue is `OPEN_WORK.md` §9. This prereg covers three rows, each with its work order as written there:

- **BICAUSAL** (rank 1, `OPEN_WORK.md:247`). OBSERVED: no theorem joins T61's two-bath heat account (`theory/FEEDBACK_FLOOR_2026-11-23.md:15-35`), the design-level response (CA1, `theory/COADAPTATION.md:11-22`; F3, `:251`; F4, `:252`) and a finite-capacity boundary. The ledger row is `measurement/CLAIM_MAP_v2.md:894` (open).
- **CL11** (rank 2, `OPEN_WORK.md:248`). OBSERVED: drift-intensity reduction is not modelled (`measurement/CLAIM_MAP_v2.md:891`, open). F3's copy gain is a different lever (`theory/COADAPTATION.md:251`).
- **CX2-SETTLE** (rank 3, `OPEN_WORK.md:249`). OBSERVED: CA5 (`theory/COADAPTATION.md:9`), F3, F4 and F6 (`:254-262`) are proved in-model classes; no necessary-and-sufficient settling scope exists (`measurement/CLAIM_MAP_v2.md:882`, CX2 open). `CORE.md:127` states the fourth condition, a coupling that settles.
- **Growth bridge.** OBSERVED: Lemma LY gives long-run growth \(\lambda=\mathbb E[\log W]\) and GF3 makes the additive display a special case (`theory/GROWTH_BRIDGE.md:22`); Theorem GB recovers the argmax ranking only, and the term list, the cap and H3 are inputs (`theory/GROWTH_BRIDGE.md:255-261`).

**Named rival where quantities overlap: rational inattention.** Sims, C. A. 2003. Implications of rational inattention. *Journal of Monetary Economics* **50**(3):665–690. doi `10.1016/S0304-3932(03)00029-1` (resolved on the Crossref API on 25 November 2026, `crossref.out` in this folder). The repository already credits the cost-plus-information form to it (`THEORY.md:195`, `:283`). Rational inattention (RI below) prices information and treats the world as exogenous: the agent's optimum depends on its stake, its information price and the world's statistics, and not on how the world responds to the agent. Every bar below that scores a quantity RI also predicts names RI's value for that quantity.

**What this prereg does not promise.** No area cap on frozen stock (`OPEN_WORK.md:247`). T61's fixed-noise statements are left as they are (`OPEN_WORK.md:247-248`). No general convergence theorem (`OPEN_WORK.md:249`). The CL11 lever is not called F3's copy gain (`OPEN_WORK.md:248`). Nothing here derives holography, quantum theory or gravity, and none of it derives the master equation (`theory/GROWTH_BRIDGE.md:259`).

## 1. Gate (draft PR #263, `process/PREREG_GATE.md` at head `8c4b3c0`)

Each scored item is either a **TEST** (passes G1–G5 on paper below) or a **CONSISTENCY_CHECK** (fails G2: its value follows from formulas already on `main`; one ledger line, not reviewed as a test, information about 0). Labels are given up front.

| ID | Label | G1 miss (odds of a miss) | G2 not an identity | G3 named rival and its value | G4 reach | G5 next step |
|---|---|---|---|---|---|---|
| A-C1 | **CONSISTENCY_CHECK** | — | Fails: at \(g=0\) the joined account is T61's (`theory/FEEDBACK_FLOOR_2026-11-23.md:27-33`) | — | — | Logged only |
| A-C2 | **CONSISTENCY_CHECK** | — | Fails: the stability determinant \(\propto 1-gc\) and the Hayes delay bound are F3 and F4 inputs (`theory/COADAPTATION.md:251-252`) | — | — | Logged only |
| A-C3 | **CONSISTENCY_CHECK** | — | Fails: at \(\eta=0\) the CL11 family is the fixed-noise OU case, \(p^*=\sqrt{\theta a kT/w}\) (from \(L=a(\theta/p-1)\), `theory/FEEDBACK_FLOOR_2026-11-23.md:27`) | — | — | Logged only |
| A-T1 | **TEST** | §2.3: a case inside S1–S5 that is not one object, or a case outside them that is (odds 0.45) | The iff is not proved; S2 may not be necessary | Two-one-way null (each party priced as if the other were exogenous, RI style): cross term in entropy production \(=0\) | (b) `CORE.md:127`, `measurement/CLAIM_MAP_v2.md:894` | Hit: write BICAUSAL as a scoped theorem, then A-T2. Miss: the counterexample becomes the row's scope line; drop S2 or replace it |
| A-T2 | **TEST** | \(\rho>0.9\) (odds 0.5) | Optimum over a two-parameter design of a non-reversible linear system; no locked formula gives it | RI: \(\rho=1\) | (b) `CORE.md:80`, `:127` | Hit: memory heat is shared with the world bath, carry into CL11. Miss: RI's exogenous reading is enough at this order; record and stop the free-ride line |
| A-T3 | **TEST** | \(\epsilon_p>-0.6\) (odds 0.5) | Optimum over \((\eta,T_c,L)\) with a Carnot-priced cold bath; not computed anywhere | RI and T61 fixed noise: \(\epsilon_p=-1/2\) | (b) `measurement/CLAIM_MAP_v2.md:891` (CL11) | Hit: CL11 gets a worked lever with a steeper stake response. Miss: the lever does not change the scaling; CL11 stays open with a named negative |
| B-C1 | **CONSISTENCY_CHECK** | — | Fails: CA1 regret \(d_i/(2\beta_i)\) and joint efficiency iff cost shares equal stakes (`theory/COADAPTATION.md:20`, `CORE.md:127`) | — | — | Logged only |
| B-C2 | **CONSISTENCY_CHECK** | — | Fails: Theorem GB argmax agreement and the \(\mu-\sigma^2/2\) limit (`theory/GROWTH_BRIDGE.md:255`) | — | — | Logged only |
| B-C3 | **CONSISTENCY_CHECK** | — | Fails: at equal strengths the Metropolis chain on a common cost is reversible with a Gibbs distribution (CA1, `theory/COADAPTATION.md:11-17`), so the selected state is the global minimum | — | — | Logged only |
| B-T1 | **TEST** (low information) | §3.3 (odds 0.10) | Delay system with saturation, no closed form at finite \(k\); a paper estimate is given in §3.3 | RI per party and the near-minimizer reading: \(X(20)\to 0\) with \(R\) | (b) `CORE.md:127` (the reading when coupling does not settle) | Hit: the reading in §3.4 is written into the CX2-SETTLE row. Miss: the reading is replaced |
| B-T2 | **TEST** | \(f\notin[0.05,0.35]\) (odds 0.4) | Random-landscape enumeration with stochastic potentials; no closed form | Joint-efficiency reading and the equal-strength case: \(f=0\). Random-basin null: \(f=0.5\). RI is silent (per-party RI gives both basins, which are both Nash) | (b) `CORE.md:127`, `measurement/CLAIM_MAP_v2.md:890` (F6) | Hit: a size for how often strength mismatch picks the worse Nash point. Miss: report the observed \(f\) and its direction; the band was wrong |

**Paper check of the gate (self-check, 25 November 2026; a separate reader is still required by #263).**

- **G1.** Every TEST names a miss band and odds. None has odds near 0; B-T1 is the lowest (0.10) and is labeled low information.
- **G2.** Six items fail G2 and are labeled CONSISTENCY_CHECK above. The five TESTs depend on an unproved iff (A-T1), constrained optima of non-reversible or two-bath systems (A-T2, A-T3), a nonlinear delay system (B-T1), or an enumeration (B-T2). For B-T1 the paper estimate is written down (§3.3), as G2 asks.
- **G3.** Each TEST names a rival with a different value. RI is the rival for A-T2 and A-T3, and enters B-T1 through the per-party reading. The gap to the rival is at least 0.1 on each scored number, and the numerical resolution is at most 0.01 (§4).
- **G4.** Every TEST reaches level (b), a cited `CORE.md` or `measurement/CLAIM_MAP_v2.md` line. None reaches (c); a real system is DATA-ONE (`OPEN_WORK.md:251`), outside this prereg.
- **G5.** Each TEST has a different next step after a hit and after a miss (table).
- **Per route.** Route A has two TESTs scored against RI (A-T2, A-T3). Route B has B-T2 against the joint-efficiency reading and B-T1 against RI's per-party reading.

## 2. Route A, two-way: BICAUSAL then CL11

### 2.1 Model W2 (the responding world as another party)

State \((x,m)\): world \(x\), memory \(m\). Each coordinate has its own bath, unit mobility, Einstein temperatures \(kT_X=D\) and \(kT_M=D_M\) (T61 conventions, `theory/FEEDBACK_FLOOR_2026-11-23.md:27`).

\[
dx=-a\,(x-g\,m)\,dt+\sqrt{2D}\,dW_x,\qquad dm=-\gamma\,(m-c\,x)\,dt+\sqrt{2D_M}\,dW_m .
\]

The world descends its own cost \(\tfrac a2(x-gm)^2\): it is a party that copies the memory with gain \(g\). The memory descends \(\tfrac\gamma2(m-cx)^2\). This is F3's copy-gain structure written at the state level, with T61's two baths. At \(g=0\) it is T61's passive plant at fixed noise (A-C1). Heat into bath \(i\) at steady state is \(\dot Q_i=\mathbb E[f_i^2]+D_i\,\mathbb E[\partial_i f_i]\) (Sekimoto, Stratonovich, unit mobility). The cost is

\[
J=\dot Q_M+\dot Q_X+w\,\mathbb E[(x-m)^2].
\]

**Finite boundary capacity.** The learning rate across the boundary is capped, \(|I_{\mathrm{alt}}|\le C\) (nats per unit time). A-T2 is scored at \(C=\infty\) (cap not binding); the binding case is reported, not scored.

**Update rule (design level).** The designs \((\gamma,c)\) of the memory and \((a,g)\) of the world change by the CA1 substitution chain (`theory/COADAPTATION.md:11-22`) on clocks slower than the state relaxation by a factor \(\varepsilon\).

### 2.2 Conditions for one object (to be stated and proved or refuted)

S1 time-scale separation, \(\varepsilon\to0\) (CT32 (iii) speed ratio, `OPEN_WORK.md:147`). S2 the \(\beta\)-scaled design game is an exact potential (CA1). S3 confinement, \(gc<1\) (F3 analogue). S4 no delay, or delay with \(k\tau\) below the Hayes bound (F4). S5 finite capacity \(C\) enters as a convex constraint on designs.

**One object** means: the design distribution is \(\propto e^{-\Psi}\) for one potential \(\Psi\) on designs, whose value at each design is built from the stationary two-bath heats and task loss of §2.1, up to \(O(\varepsilon)\).

Pre-named counterexample candidates (at least one is to be worked out): (CE-a) the F4 delayed world response with \(k\tau\) above the Hayes bound, where the fast account has no steady state at a fixed design; (CE-b) \(gc\ge1\); (CE-c) a world whose noise intensity, not its drift target, responds (the CL11 lever), which leaves T61's fixed-noise class.

### 2.3 A-T1 (TEST): the iff

**HYPOTHESIS.** Inside W2, S1–S5 are necessary and sufficient for one object. **Miss** if the derivation finds a case meeting S1–S5 that is not one object (signed size: the \(O(1)\) gap in the design distribution's log-ratio), or a case failing exactly one of S1–S5 that is one object (the condition is not necessary; size: which condition, and the measure of the case). **Rival.** Two one-way accounts: each party priced as if the other were exogenous, RI style. Its cross term in total entropy production at \(gc\neq0\) is 0; the joined account predicts a nonzero cross term. Odds of a miss: 0.45 (S2 is the most likely to be unnecessary).

### 2.4 A-T2 (TEST, against RI): does the responding world lower the memory's heat?

Reference point: \(a=1\), \(D=1\), \(D_M=1\), \(w=10\), \(C=\infty\). For each \(g\), minimize \(J\) over \(\gamma>0\) and real \(c\) with \(gc<1\). Let \(\dot Q_M^*(g)\) be the memory heat at that minimizer.

\[
\rho=\dot Q_M^*(0.5)/\dot Q_M^*(0).
\]

**HYPOTHESIS:** \(\rho\le0.9\). **RI's value:** \(\rho=1\) (the RI design ignores the world's response). **Miss** if \(\rho>0.9\); signed size \(\rho-0.9\); location `model` unless a reproducible bug is found (`process/PROCESS.md:30`). Odds of a miss: 0.5. Also reported, not scored: \(J^*(g)\), \(\dot Q_X^*(g)\) and \(I_{\mathrm{alt}}\) on \(g\in\{0,0.25,0.5,0.75,0.9\}\).

### 2.5 A-T3 (TEST, against RI): CL11 drift-intensity lever

Family CL11-cold. A world coordinate in a unit harmonic trap, coupled to its own bath (friction 1, temperature \(T_0=1\)) and, by design, to a cold bath (friction \(\eta\ge0\), temperature \(T_c\in(0,T_0]\)):

\[
dx=-\frac{x}{1+\eta}\,dt+\frac{\sqrt{2(T_0+\eta T_c)}}{1+\eta}\,dW .
\]

Keeping the cold bath at \(T_c\) is paid by a refrigerator at the Carnot floor, \(W_{\mathrm{ref}}\ge \dot Q_{c}\,(T_0/T_c-1)\), where \(\dot Q_c\) is the steady heat flow from \(x\) into the cold bath. The memory tracks \(x\) by compensated Kalman–Bucy at learning rate \(L\) and pays \(kT_0L\) (T61's class at fixed observation noise). The cost is \(J=kT_0L+W_{\mathrm{ref}}+w\,p\), with \(p\) the tracking error variance. Design \((\eta,T_c,L)\). At \(\eta=0\) this is T61's fixed-noise case (A-C3), and the design lever is the noise intensity and relaxation rate, not a copy gain.

Scored: \(\epsilon_p=d\ln p^*/d\ln w\), the least-squares slope of \(\ln p^*\) on \(\ln w\) over \(w\in\{10^3,10^{3.5},\dots,10^6\}\).

**HYPOTHESIS:** \(\epsilon_p\le-0.6\). **RI's value (and T61 fixed noise):** \(-1/2\). **Miss** if \(\epsilon_p>-0.6\); signed size \(\epsilon_p+0.6\). Odds of a miss: 0.5. The derivation names the cases where the lever does not pay, as the work order asks (`OPEN_WORK.md:248`), including the conservative-trap loophole (`CORE.md:80`) if it reappears.

## 3. Route B, selection: CX2-SETTLE plus the growth bridge

### 3.1 Scope statement to be written (not scored)

Compare CA5 (strongly monotone, non-potential, stable at all speeds), F4 (delay), F3 (loss of confinement at copy gain one) and F6 (multi-basin resistance), in one table: what each guarantees, whether it bounds Nash regret, and whether it bounds the gap to the joint optimum. Joint efficiency needs cost shares equal to stakes (`CORE.md:127`). No general convergence theorem is stated (`OPEN_WORK.md:249`).

### 3.2 Growth bridge (not scored beyond B-C2)

Selection on long-run growth \(\lambda=\mathbb E[\log W]\) (`theory/GROWTH_BRIDGE.md:22`) gives argmax rankings only (`:255-257`); the cost enters Route B through the assumed map \(W=e^{-\beta J}\), which is an input, as are the term list, the cap and H3 (`:259-263`). Every Route B result is stated in that conditional form.

### 3.3 B-T1 (TEST, low information): Nash regret and joint excess when coupling does not settle

Model (F4 with saturation): \(\dot x=-k\,(x-\theta)\), \(\theta(t)=g\tanh x(t-\tau)\), \(g=-2\), \(\tau=1\), history \(x=0.1\) on \([-1,0]\); RK4, step \(10^{-3}\), horizon 400, averages over \([200,400]\). The system's cost \(J_s=\tfrac12(x-\theta)^2\); the world's cost \(J_w=\tfrac12(\theta-g\tanh x)^2\) at current \(x\). The unique Nash point and joint optimum is \((0,0)\) with both costs 0. Hayes bound at \(g=-2\): \(k\tau<1.209\) (`theory/COADAPTATION.md:252`).

\(R(k)\) is the time average of \(J_s\) (the system's Nash regret, since its best reply costs 0). \(X(k)\) is the time average of \(J_s+J_w\) (the gap to the joint optimum).

**Paper estimate (G2).** For large \(k\) the orbit approaches a period-\(2\tau\) square wave between \(\pm x^*\), \(x^*=2\tanh x^*\approx1.915\); then \(R(k)\approx x^{*2}/k\) and \(X(k)\to\) about \(\tfrac12(2g\tanh x^*)^2\approx7.3\). This is a heuristic, not a proof.

**HYPOTHESIS:** \(R(20)<R(5)\) and \(X(20)/R(20)\ge5\). **Rival (RI per party and the near-minimizer reading of strong selection):** \(X\) falls to 0 with \(R\) as selection strengthens. **Miss** if \(R(20)\ge R(5)\) (size \(R(20)-R(5)\)) or \(X(20)/R(20)<5\) (size: ratio \(-5\)). Odds of a miss: 0.10. Grid also reported: \(k\in\{0.5,1,1.5,2,3,5,10,20\}\).

### 3.4 Reading of the hypothesis when coupling does not settle (to be written, then checked against B-T1)

HYPOTHESIS for the reading: where coupling does not settle, "strongly selected" does not imply near a minimum (F4, `theory/COADAPTATION.md:252`), stronger selection can lower each party's regret while the gap to the joint optimum stays order one, and the hypothesis sentence makes no claim about the joint cost there. The hypothesis is then read per party, against each party's best reply, and only inside a demonstrated settling bound (`CORE.md:127`).

### 3.5 B-T2 (TEST, against the joint-efficiency reading): which Nash point does mismatched selection pick?

Landscape: a common team cost \(J\) on a \(3\times3\) product grid, party 1 picks the row and party 2 the column; entries i.i.d. Uniform(0,1); 20,000 draws from `numpy.random.default_rng(20261125)`, filled row-major. Unilateral moves: a party may move to either other value of its own coordinate. Resistance (F6, `theory/COADAPTATION.md:254`): \(r(x\to y)=c_i\,(J(y)-J(x))_+\) for a move by party \(i\), with \(c=(1,3)\). Stochastic potential of each state: minimum total resistance of a spanning in-tree rooted at that state (Chu–Liu/Edmonds, own implementation, cross-checked by brute force on the first 200 qualifying draws). A draw qualifies if it has exactly two unilateral local minima and a unique stochastic-potential minimizer; draws with ties are counted and reported.

Scored: \(f\), the fraction of qualifying draws whose selected state is not the global minimum of \(J\). Both local minima are pure Nash points with Nash regret 0, so \(f\) measures joint inefficiency at zero Nash regret.

**HYPOTHESIS:** \(f\in[0.05,0.35]\). **Rivals:** the joint-efficiency reading (and the equal-strength case, B-C3 at \(c=(1,1)\)): \(f=0\); random-basin null: \(f=0.5\). **Miss** if \(f<0.05\) (size \(f-0.05\)) or \(f>0.35\) (size \(f-0.35\)). Odds of a miss: 0.4. If fewer than 1,000 draws qualify, B-T2 is `INCONCLUSIVE`, not a miss. Binomial standard error at 1,000 qualifying draws is at most 0.016.

## 4. Numerics and resolution

Optimizations (A-T2, A-T3) use a stated grid plus local refinement, tolerance \(10^{-6}\) on the design and \(10^{-4}\) relative on \(J\); a result whose scored number moves by more than 0.01 under halving the tolerance is reported as not resolved. Stationary covariances of linear systems come from the Lyapunov equation, checked against a direct simulation at one design per model. All scripts and outputs go in `checks/` in this folder.

## 5. Budget and stop rule

- **Route A.** At most two executor sessions for A-T1 and A-T2 and one for A-T3, and one independent review round before upstream. Stop when A-T1 and A-T2 are logged; A-T3 then starts. If the budget runs out, each unscored bar is logged as a `process` miss with size "not reached". Stop at once on any breach risk (`process/PROCESS.md:26`).
- **Route B.** One executor session for B-T1, B-T2 and the scope table, and one independent review round. Stop when the three are logged. B-T2 computation is capped at 30 CPU-minutes; if not finished, `INCONCLUSIVE`.
- **Both.** No scored number is recomputed with a changed model after it is logged. A changed model is a new prereg.

## 6. Shared criterion: which route moved the core claim further

Locked before either route runs. For each route, score

\[
S=2\times(\text{CLAIM\_MAP\_v2 rows in its scope whose status changes}) + 1\times(\text{TEST bars resolved outside the rival's resolution, hit or miss}),
\]

with scope rows BICAUSAL, CL11 for Route A and CX2, FOUR, F6 for Route B. A status change counts both ways (open to proved-in-model in a named class, or a counterexample that narrows a row). CONSISTENCY_CHECK items score 0. A miss counts as much as a hit, because it is information. The higher \(S\) moved the core claim further; a tie is reported as a tie, and neither route is preferred by this criterion.

## 7. Ledger

Every outcome, hit or miss, gets one eight-field row of `process/MISS_LOG_TEMPLATE.md` (`prediction_id`, `locked_prediction`, `outcome`, `miss`, `location`, `stake_x_info`, `update`, `breach_check`) in `RESULTS.md` in this folder. An open miss follows `CORE.md:169`: a miss with a diagnosis and a next test, and no update yet.
