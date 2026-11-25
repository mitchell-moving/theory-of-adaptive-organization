# THEOREMS: math for one application of A Theory of Adaptive Organization (drift-matched memory)

Draft, Friday 2026-11-13 (ET). **Everything here is either a known result restated, an elementary corollary, or a hypothesis. Nothing here is claimed as a new theorem.**

Every algebraic step marked *checked* is reproduced by `theorems-checks/check_all.py`
(output in `theorems-checks/check_all.out`; sympy 1.14, numpy 2.5, scipy 1.18). The section labels printed in `check_all.out` are the script's own and do not always match the T-numbers below (for example, the output's "T1d" is T1c here). An independent re-derivation is in `../reviews/independent-sim/indep_checks.py`. The fixes from the independent review (`../reviews/independent-sim/REVIEW.md`) are applied in this public copy; see "Changes from the reviewed draft" at the end.

**Labels.** **[PROOF]** an elementary proof is given and checked. **[KNOWN]** the result is an existing theorem, restated in the theory's terms. **[UNCONFIRMED]** not found in a quick search, but elementary enough that it may well be known; no novelty is claimed. **[NUMERIC]** shown by computation only, no proof. **[FAILS]** the hoped-for result does not hold or could not be proved. **[ANALOGY]** a resemblance, not math.

**Bottom line first.**
- Nothing here is claimed as a new theorem. Most results are short corollaries of known ones: EOQ (Harris 1913), Kalman/Muth (1960), Cho & Garcia-Molina (2003), Roundy (1985), Still et al. (2012), Kuramoto (1975).
- Pieces we have not seen stated in exactly this form (each is elementary and may well be known; a proper literature search has not been done):
  - a sufficient condition for when facts sharing a driver should be modeled as driver plus residuals (T3a);
  - the √N decay of a shared trace, as an applied prediction (T4);
  - a precise statement of the conditions under which the optimal design is self-similar ("fractal"), and of when it is not (T7).
- The escalation condition (T2b) is simple cost accounting, not a result.
- "Nested always beats flat" and "the architecture is fractal" are **not** theorems. Each holds only under conditions stated below, and both conditions are properties of the world, not of the theory.
- Throughout, "cost" means attention, time, compute or money, not physical energy.

---

## T1. Drift-matched checking and memory decay **[KNOWN + PROOF]**

**Setting.** A held copy m of a quantity x(t) that drifts as a random walk, dx = σ dW (independent, finite-variance increments). A check costs c and resets the error to zero (perfect, instantaneous). Acting on a stale copy costs w·(error)² per unit time.

**T1a (check interval).** With periodic checks every T, the long-run cost rate is J(T) = c/T + wσ²T/2. It is minimized at
  **T\* = √(2c/(wσ²))**, with **J\* = σ√(2cw)**.
*Proof:* E[(x(t)−x(0))²] = σ²t, so the average holding loss over a cycle is (w/T)∫₀ᵀσ²t dt = wσ²T/2. Set dJ/dT = 0; J is convex. *Checked* symbolically, and by Monte Carlo on random walks (within 1-3%; the residual is time discretization).
This is the EOQ formula (Harris 1913) with σ² in place of demand × holding cost.
- Under a hard tolerance (|error| ≤ ε with confidence set by a normal quantile z), T\* ≈ (ε/(zσ))².
- Under jump drift (the value is replaced at Poisson rate λ) with bounded loss, the optimal check rate is ≈ √(μWλ/2c) for small λ. The setting is Cho & Garcia-Molina (2003); this explicit small-λ formula is our own expansion, not a formula quoted from their paper.
- "∝ √(cost/drift variance)" holds when drift is measured as a variance rate. Measured as σ, T\* ∝ 1/σ. A preregistration must state its drift unit and its loss.

**T1b (memory decay).** If x is seen through noise of variance r each step (q = σ² per step), the steady-state optimal exponential-decay weight is the Kalman gain K, which solves K²/(1−K) = q/r, so **K ≈ √(q/r)** for small q/r. *Checked* (series K = √z − z/2 + z^{3/2}/8, z = q/r). This is Muth 1960 / Kalman 1960 [KNOWN].

**T1c (robustness: rough estimates are nearly as good) [PROOF; known in EOQ texts].**
- J(xT\*)/J\* = (x + 1/x)/2 = cosh(ln x).
- Because T\* ∝ √(c/(wσ²)), misjudging drift, stakes or check cost by a factor m costs (m^{1/2} + m^{−1/2})/2. That is **+6% at m = 2 and +74% at m = 10**.
- The same cosh form governs a misjudged filter gain. Exact EWMA: +6.2% at m = 2, +75.8% at m = 10. *Checked.*

**Why it matters.** It means stakes, chances and drift rates can be rough judged estimates: being within 2x costs about 6%. Being off by 10x is not harmless.

## T2. When a cheap watcher pays **[PROOF; algebra is EOQ]**

**T2a (the condition to verify).** One item, stakes w, drift σ. Checking with the main model costs c_main per check. A cheap watcher costs c_w per check plus upkeep h_w per unit time. By T1a, the optimal costs are σ√(2wc_main) and σ√(2wc_w) + h_w. So
  **the watcher pays iff √(2w)·σ·(√c_main − √c_w) > h_w.** *Checked* symbolically. **Verified.**
Assumptions: quadratic loss, random-walk drift, perfect resets, periodic checks, and a watcher check that is as good as a main check.

**T2b (escalation: an accounting identity, not a result).** Real watchers detect, then escalate. Suppose a fraction ε of watcher checks must also wake the main model. Each check then costs c_w + εc_main on average, and the condition becomes
  **√(2w)·σ·(√c_main − √(c_w + ε·c_main)) > h_w**, which requires **ε < 1 − c_w/c_main.**
*Checked* by simulation of random escalations (agrees to 0.1%).
- **Assumptions, and why this is weak:** escalations are random (real ones are triggered by surprise), and a watcher check is as informative as a main check, so escalating adds no information. Under those assumptions "a 10x-cheaper watcher that escalates more than 90% of the time never pays" is close to a tautology: each check then costs at least c_main. Treat T2b as bookkeeping, not as evidence for any design.

**T2c (noisy watchers) [NUMERIC].** If watcher checks are noisier (variance r_w versus r), the comparison depends on the regime.
- When noise dominates (checks are frequent relative to drift), information per unit cost is 1/(c·r), so cheap wins iff c_w·r_w < c·r.
- When drift dominates (stale data is the main error), many cheap checks win by more. In the toy sim (E3), cheap watchers still won with noise 45x the main model's (c_w·r_w ≈ 4.5·c·r). E3's watchers are cheaper, noisier sensors with no escalation logic, so E3 is not evidence for T2b.

**Prior art.** EOQ. Dual-prediction in sensor networks. Model-based networked control (Montestruque & Antsaklis 2003-04). Cheap-first cascades (FrugalGPT, RouteLLM) without stakes or checks.

## T3. Nested versus flat **[PROOF for a, KNOWN for b, NUMERIC for c; no general theorem]**

"Nested beats flat" is not one theorem. A nested design can buy three different things, and each has its own condition:
- **pooling:** one model of a shared driver serves many facts;
- **per-level clocks:** each level is checked at its own interval;
- **per-level tiers:** each level gets the cheapest adequate checker (T2).

Against these, it pays upkeep for each level, plus an error from treating levels as decoupled.

**T3a (a sufficient condition for modeling a shared driver) [PROOF; elementary; not seen stated in this form, may well be known; cousins are MDL, square-root pooling and joint replenishment].**
- **Setting.** N facts share one driver: x_i = g + u_i. The driver g drifts at variance rate q_g; each residual u_i drifts at q_u. Write ρ = q_g/q_u. Checks cost c, the model's upkeep is h, and the stakes are w per fact.
- **Costs.** Flat tracks each x_i separately, at rate q_g + q_u, for a total cost of N√(2cw(q_g+q_u)). Nested tracks g once (its error hits all N facts, so its stakes are Nw) and each u_i separately. That gives the cost of one feasible nested policy, and so an upper bound on the best nested cost: √(2c_g·w·N·q_g) + N√(2cwq_u) + h. **Assumption (fixed after review):** the driver can be read from its own source at cost c_g (for example, the schedule itself). If g can be seen only through the facts, residual errors contaminate each driver check, and the expression is an approximation, not a bound.
- **Result.** With c_g = c, nested is cheaper whenever
  **√N·√(2cwq_u)·[√N(√(1+ρ) − 1) − √ρ] > h.**
  With h = 0 this is **N > N\* = (√(1+ρ) + 1)²/ρ** (≈ 4/ρ when shared drift is small). *Checked* symbolically: N\* = 5.83 at ρ = 1, 9.9 at ρ = 0.5, 42 at ρ = 0.1.
- **Reading.** This is a **sufficient condition, not a cutoff**: above N\*, modeling the driver is guaranteed cheaper (under the assumptions); below N\*, the condition says nothing, and modeling may still pay. It does **not** say "below N\*, keep raw facts".
- **Sim check (consistent, but not diagnostic).** In the toy sim, with zero upkeep, nested already won from n = 2 items per group at ρ = 1 (E2b); with upkeep charged, from about 6-8. This agrees with the bound being conservative, but it is not a real test of T3a: with h = 0 and the true joint model, a Kalman filter cannot lose to an independence approximation (up to greedy scheduling), and the sim optimizes a budgeted-MSE objective, not the periodic cost in the bound. A real test needs a misspecified world (overlapping or switching drivers).
- **Cousins.**
  - MDL (Rissanen): compress when model length plus residuals is shorter than the raw data. T3a is the dynamic-upkeep analogue.
  - Square-root pooling laws in inventory (Eppen 1979).
  - Joint replenishment with a major setup cost.

**T3b (per-level clocks) [KNOWN: Cauchy–Schwarz on EOQ costs; Roundy 1985].**
- With K independent components at rates q_k, one shared check interval costs √(2cw·K·Σq_k), and per-component intervals cost √(2cw)·Σ√q_k.
- So per-level clocks save 1 − Σ√q_k/√(KΣq_k).
- For two levels with separation R = √(q_fast/q_slow), the saving is 0 at R = 1, 5% at R = 2, 14% at R = 4, 23% at R = 10, and at most **1 − 1/√2 ≈ 29%** as R → ∞. *Checked.*
- So nested clocks beat a single clock by at most 29% for two levels, and they pay only if the saving exceeds the extra upkeep.

**T3c (time-scale separation makes decoupled levels nearly optimal) [NUMERIC; principle KNOWN].**
- **Setting.** x = s + f: a slow random walk s plus a fast mean-reverting part f (time constant τ), seen through noise.
- **Designs compared:**
  - the optimal joint filter (benchmark);
  - FLAT, the best single-timescale smoother;
  - NESTED, a slow smoother that treats f as noise, plus a fast filter on the residual.

| τ_fast / slow memory (≈28 steps) | flat / optimal | nested-decoupled / optimal |
|---|---|---|
| 0.07 (τ=2) | 1.15 | 1.00 |
| 0.36 (τ=10) | 1.07 | 1.02 |
| 1.8 (τ=50) | 1.02 | 1.06 |
| 9 (τ=250) | 1.00 | 1.11 |
| 36 (τ=1000) | 1.01 | 1.14 |

- **Result.** Decoupled nesting is near-optimal and beats flat when the fast level is much faster than the slow level's memory (ratio ≪ 1). It **loses** to flat when the ordering of time scales collapses or inverts.
- **Known principles behind it:**
  - singular perturbation (Tikhonov);
  - two-time-scale stochastic approximation (Borkar 1997);
  - the Simon–Ando aggregation theorem for nearly decomposable systems (1961);
  - Simon 1962.
- **Combined condition (stated, not proved as one theorem).** Nested beats flat when pooling gain + clock gain + tier gain > Σ upkeep + decoupling error, where the decoupling error grows with τ_fast/τ_slow.

**What fails.** There is no theorem that nested is always better. With no shared drift, nested loses by its upkeep: 2-10% in the sim (E1, phi = 0). With collapsed time scales, decoupled nesting loses to flat (T3c).

## T4. The √N fade of a shared trace **[PROOF in a stated regime; math KNOWN; application UNCONFIRMED]**

**Setting.**
- N agents each deposit an independent noisy reading (noise variance r) of the same drifting quantity (random walk, variance q per step) into one shared trace.
- The trace decays exponentially: an evaporating trail, or a shared store whose entries fade.
- The mean of N independent readings is a sufficient statistic, with noise r/N.

**Result.** The optimal decay weight solves K²/(1−K) = Nq/r, so **K\*_shared ≈ √(Nq/r) = √N · K\*_private** while Nq/r ≪ 1.
- *Checked:* local exponents d ln K/d ln N = 0.49, 0.48, 0.46, 0.41, 0.33 from N = 1 to 1024 at q/r = 10⁻³. Monte Carlo best gains agree within noise.

**Conditions** (each is required):
- **Small gain:** the predicted K stays below about 0.3. Above that, the exponent falls toward 0.
- **Independent deposits.** Trail-followers deposit where the trail already is, so their effective N is smaller.
- **A rival mechanism** (positive-feedback lock-in) also favors faster evaporation in larger colonies. Only an arm with independent depositors tests pooling.

**Status.** The math is Kalman averaging. A quick search found no stated √N rule linking evaporation to colony size. Ant colony optimization (ACO) adapts evaporation to the pace of change instead (Mavrovouniotis & Yang 2013). Novelty is unconfirmed and not claimed.

## T5. Rise-then-fall of watching effort **[PROOF; KNOWN in its core case (Cho & Garcia-Molina 2003)]**

**Theorem.**
- **Setting.** An item changes at Poisson rate λ. A copy is used at rate μ, and using a stale copy costs at most W (bounded loss). Refreshing at rate f costs c per refresh. Freshness is F(f, λ) = (f/λ)(1 − e^{−λ/f}).
- **Claim.** The optimal refresh rate f\*(λ) is 0 at λ = 0, strictly positive on 0 < λ < μW/c, and exactly 0 for λ ≥ μW/c. Hence f\* has an interior maximum: effort rises, then falls to zero.
- **Proof.** Cost = cf + μW(1 − F).
  - (i) F depends only on f/λ, and ∂²F/∂f² = −λe^{−λ/f}/f³ < 0, so F is concave in f and the cost is convex.
  - (ii) The marginal benefit of the first refresh is μW·∂F/∂f at f → 0⁺, which equals μW/λ. By convexity, f\* > 0 iff μW/λ > c, i.e. iff λ < μW/c.
  - (iii) As λ → 0⁺, f\* ≈ √(μWλ/2c) → 0 (our expansion; see T1).
  - (iv) f\* is continuous in λ (strictly convex cost, so the argmin is continuous), positive inside the interval and zero at both ends, so it attains an interior maximum. ∎
- *Checked* symbolically, and numerically: f\* = 0.07, 0.67, 1.88, 2.73, 2.98 (peak near λ = 5), 2.87, 2.31, 1.49, then 0 at λ = 10.1.
- Unimodality (a single peak) is shown numerically, not proved.

**T5b (generalization) [PROOF, elementary].**
- Under unbounded quadratic loss, holding costs σ√(2cw), which grows without bound. If any bounded-cost alternative exists (fade, or read the source at use for cost u per use, rate μ), holding stops at σ_c = μu/√(2cw).
- Effort rises as σ√(w/2c) up to σ_c, then jumps to zero: a cliff, not a smooth hump. *Checked.*
- So the fall comes from any bounded fallback. Effort keeps rising only where staleness cost grows without bound and no fallback exists.
- Cho & Garcia-Molina (2003) already show the freshness/age contrast for web crawlers (to maximize freshness, ignore pages that change too often; for age, refresh rises monotonically). Only a cross-domain field test would be new, and none has been run.

## T6. Useless memory and dissipation: Still, Sivak, Bell & Crooks 2012 **[KNOWN; stated only under its conditions]**

**Statement** (Phys. Rev. Lett. 109, 120604; text checked this pass, arXiv:1203.3271).
- **Conditions:**
  - A system with state s_t and energy E(s, x) is driven by a signal x_t, which follows any stochastic process.
  - **There is no feedback from the system to the signal.**
  - System dynamics are Markovian in discrete time, p(s_t | s_{t−1}, x_t).
  - The system stays in contact with a heat bath at temperature T and starts in equilibrium.
  - Work is done when x changes (with s fixed); heat flows when s relaxes (with x fixed).
- **Definitions.** I_mem(t) = I[s_t; x_t] and I_pred(t) = I[s_t; x_{t+1}].
- **Result.** With dissipation defined as work minus the change in nonequilibrium free energy F_neq = ⟨E⟩ − kT·H(S|X):
  **β⟨W_diss[x_t → x_{t+1}]⟩ = I_mem(t) − I_pred(t)** for each work step, and **Σ_t [I_mem − I_pred] ≤ β⟨W_diss⟩ ≤ β⟨W_ex⟩** over a protocol.
- **Refined Landauer bound:** −β⟨Q⟩ ≥ I_erased + Σ(I_mem − I_pred).

**Checked.** Exact enumeration on a two-state system driven by a two-state Markov signal reproduces the per-step equality to 6 decimals and the summed inequality (`check_all.out`, T6).
- Note that the per-step equality is close to an identity once F_neq is defined this way: H(S_t) cancels and H(S_t|X_{t+1}) − H(S_t|X_t) = I_mem − I_pred.
- The physics lies in F_neq being a real free energy, which requires the bath and an energy function.

**What it does and does not license.**
- **It does:** for physical systems under these conditions (molecular machines, cells), memory that does not predict the signal costs at least that much dissipated work, in units of kT.
- **It does not:**
  - (a) It does not make thermodynamics the binding cost for firms, people or software. Those systems are physical, so the thermodynamic floor (Landauer's kT ln 2 per erased bit, and this bound wherever its conditions hold) applies to every bit they erase. But at kT ≈ 4×10⁻²¹ J per nat it sits many orders of magnitude below their real costs in money and attention, so at firm scale it **applies but constrains nothing**. The theory's bet is that the same memory/prediction/cost tradeoff still shapes design there, paid in other currencies. That bet is a hypothesis; this result does not show it.
  - (b) It does not cover systems that act back on their signal. An assistant that nudges its user violates the no-feedback condition. The relevant physics there is information thermodynamics with feedback (Sagawa & Ueda 2010, 2012). T61 (`theory/FEEDBACK_FLOOR_2026-11-23.md`) treats a memory that steers its world in named classes: the heat bound holds on the net learning rate, and no design-independent floor on memory heat alone exists. Decision-level tampering with a signal or its enforcement, as a priced action in the part's set, is treated in `theory/SWARM_RULE_2026-11-23.md` §4. Applying T61 to a part that moves the whole's signal is open.
  - (c) It does not say adaptive systems minimize dissipation or free energy.
- I_mem − I_pred is still a well-defined measure of predictive inefficiency at any scale, and it is the information-bottleneck quantity (Tishby, Pereira & Bialek 1999). It can be used as an information measure; reading it as a physical cost outside the stated conditions is not licensed. **Nothing in this repository applies Still et al. to software assistants, people or firms.**

## T7. Is "fractal" a theorem? **[PROOF of three conditional propositions; FAILS as an unconditional claim]**

The question is whether the optimal policy at one level has the same form at the next. It does, under three conditions. Each is checkable, and each can fail.

**T7a (scale-free cost penalty) [PROOF; known].** By T1c, the cost of running an item at interval T instead of T\* depends only on the ratio T/T\*: penalty cosh(ln(T/T\*)) − 1. The cost structure has no preferred time scale.

**T7b (scale-free populations get geometric hierarchies) [PROOF; Roundy-type, known in substance].**
- **Setting.** Items have natural intervals spread log-uniformly over a log-span L. They are served by K shared clocks ("levels"), each costing h.
- **Penalty per level.** A level covering log-width Δ, set at its log-center, has mean penalty φ(Δ) = (2/Δ)·sinh(Δ/2) − 1. *Checked* symbolically.
- **Why the levels are equal (proof step corrected after review).** The total mean penalty is Σ_k (Δ_k/L)·φ(Δ_k) with Σ_k Δ_k = L, so the function that must be convex is ψ(Δ) = Δ·φ(Δ) = 2 sinh(Δ/2) − Δ, not φ itself. ψ''(Δ) = ½ sinh(Δ/2) > 0 for Δ > 0, so ψ is strictly convex, and for fixed K Jensen's inequality makes **equal log-widths** optimal. (The earlier draft justified this with the convexity of φ, which is true but is the wrong function; the conclusion is unchanged. `../review/indep_checks.out` checks ψ.) The levels are therefore **geometrically spaced**, with ratio e^{L/K}: each level's interval is a fixed multiple of the one below.
- **Cross-check.** At ratio 2, the mean penalty is 1/(√2·ln 2) − 1 = **2.01%** and the edge penalty is **6.07%**. These are the same numbers, from the same integral, as Roundy's (1985) power-of-two results (1.02 and about 1.06). The statements differ: Roundy's 1.02 is a **worst-case bound** after optimizing the base period (1.06 with a fixed base); 2.01% here is a population mean under a log-uniform spread. Same math, different statement.
- **Number of levels (superseded; see T7(iii) below and CLAIM_MAP K12, MATH-CORRECTED).** With base cost C, K\* ≈ (C·L²/(12h))^{1/3} (exact search agrees: K\* = 9 for a 1000x span, 13 for 10⁵x, with level ratios of about 2.2-2.4).

**T7c (coarse-graining closure) [PROOF, elementary].**
- **Closure of the drift model.** Sums of independent random walks are random walks with summed variance rates (Gaussian laws are closed under addition). So a unit made of n sub-units faces the same problem as T1, with aggregated parameters. For α-stable increments (α < 2) the variance is infinite. The same closure holds for the scale parameter (it grows as n^{1/α}), but the quadratic-loss cost in T1 then has to be replaced.
- **Scaling law.** If a unit's check cost scales as n^γ, its stakes as n^δ and its aggregate drift variance as n^{2H}, then
  **T\*(n) ∝ n^{(γ − δ)/2 − H}**,
  a power law in unit size. Here H = ½ for independent parts and H = 1 for fully shared drift. *Checked.*

**What this makes testable (the fractal claim, stated so it can fail).**
- **(i)** At every level, the check interval falls with drift with the same exponent: −½ in drift variance under quadratic loss.
- **(ii)** Across levels, log(check interval) against log(unit size) is a straight line with one slope.
- **(iii)** When the drift rates of what a system tracks are spread log-uniformly, its review cadences cluster at geometrically spaced intervals. ~~The number of levels grows as L^{2/3}.~~ **Withdrawn (18 Nov 2026, BOOKENDS BK-P8):** the L^{2/3} level count (L = log-span) predates THEORY v1.4. The current store count is ∝ ln(span)·ln(stakes/upkeep) away from α = 2, with its rate conjectural (THEORY §1 N4; CLAIM_MAP K12, MATH-CORRECTED).

**What fails.** The theory does not make the architecture fractal by itself. Self-similarity holds if (sufficient conditions; necessity is not proved: erratum 19 Nov 2026, ET, LOCK_AUDIT S4 and THEORY v2.0, replacing "only if"):
- the world's drift is scale-free (no characteristic time: mean reversion, seasonality or regime lengths break it);
- costs are power laws in size (fixed setup costs break it);
- the loss form is the same at every level.

T7b is close to tautological: scale-free input gives scale-free output. It is a statement of conditions, not a finding. The honest statement is that **the optimal architecture inherits whatever scale structure the world has**: it is self-similar when the world, the costs and the loss are scale-free (conditional; whether it can be self-similar otherwise is not proved either way). Human calendars (day, week, month, quarter, year) are roughly geometric but astronomical in origin, so they are not evidence.

## T8. Supporting known theorems the theory rests on **[KNOWN]**

- **Internal model principle** (Francis & Wonham 1976). A controller that asymptotically rejects a class of disturbances must contain a model of the disturbance generator.
  - This is the rigorous form of "a regulator must carry a model", and it is much sharper than Conant & Ashby's good regulator theorem (1970), whose proof covers only optimal, simplest regulators.
  - Disturbances at several time scales therefore require models of each. That supports levels tracking slower causes (Kiebel et al. 2008), but it does not prove a hierarchy is the cheapest way to hold them.
- **Successive refinement** (Equitz & Cover 1991; Lastras & Berger 2001). A coarse-then-fine (nested) description of a Gaussian source under squared error loses no rate compared with a single fine description. For any i.i.d. source under squared error, the loss is at most ½ bit per sample per stage.
  - **Analogy only.** These results concern coarse-to-fine descriptions of one i.i.d. source. They say nothing about driver-plus-residual memory of drifting, correlated facts with upkeep, so they are not evidence for nested memory; they are only a reminder that coarse-then-fine descriptions need not cost much.
- **Landauer** (1961; Bérut et al. 2012 experiment): erasing a bit dissipates at least kT ln 2 on average.

## T9. Tori and coupled loops **[KNOWN math; the link to this hypothesis is an untested ANALOGY]**

**What is rigorously true about tori (standard results):**
1. **Phase spaces.** N oscillators' phases live on the N-torus Tᴺ. Two unlocked loops with incommensurate frequencies wind densely around T² (quasi-periodic flow).
2. **Integrable Hamiltonian systems** (Liouville–Arnold). Compact level sets of n conserved quantities are n-tori with quasi-periodic motion. **KAM:** under small perturbations, tori with sufficiently irrational (Diophantine) frequency ratios survive.
3. **Steady ideal fluid flows** (Arnold's structure theorem, 1965-66). In a bounded domain, an analytic steady Euler flow whose velocity is not everywhere parallel to its vorticity is fibered into invariant tori (or cylinders) outside a lower-dimensional set.
4. **Recirculation without rest points** (Poincaré–Hopf). A closed orientable surface carries a flow with no rest points only if its Euler characteristic is 0, i.e. only a torus. This is one rigorous reason recirculating surfaces without rest points are tori (as with nested flux surfaces in a tokamak).

In these results tori come from topology and integrability. They do not express a general energy-minimum principle (for example, steady vortex rings are energy **maxima** at fixed impulse; Benjamin 1976).

**One genuine constrained minimum: the spheromak.**
- *Variational fact.* In a closed, perfectly conducting system, the state of lowest magnetic energy at fixed total magnetic helicity is a force-free field ∇×B = λB with constant λ (Woltjer 1958, PNAS 44(6):489-491).
- *Relaxation.* Taylor (1974, Phys. Rev. Lett. 33:1139) argued that a turbulent, slightly resistive plasma reconnects until total helicity is the only surviving invariant, and so relaxes to that state. Review: Taylor, "Relaxation revisited", Phys. Plasmas 7:1623 (2000).
- *In a sphere.* In a spherical (simply connected) flux conserver the minimum is the spheromak: the lowest Chandrasekhar–Kendall eigenstate, with λa ≈ 4.493 for radius a (Rosenbluth & Bussac 1979, "MHD stability of Spheromak", Nucl. Fusion 19(4):489). Its field lines lie on **nested toroidal flux surfaces**, and its currents are internal. The torus is not supplied by the container's shape (Taylor 2000 lists "flux generation and flux amplification in Spheromaks" among the relaxed state's features).
- *Conditions and limits:*
  - It needs turbulence or reconnection ("if a plasma is not turbulent it need not relax", Taylor 2000), conserved helicity and a conducting boundary.
  - Nonzero helicity already means linked flux, so some of the topology is in the constraint.
  - Real spheromaks depart from the force-free state (pressure, incomplete relaxation).
  - It concerns a magnetic field, not fluid flow. It does not make toroidal flow a general minimum-energy principle.
- *Use here.* None of this is evidence for the hypothesis in this repository. No claim is made here that adaptive systems minimize energy.

**The only piece relevant here: coupled loops as phase-locking (hypothesis; not tested on real data).**
- Model a person's action rhythm and an assistant's return rhythm as two phases. Their phase difference obeys Adler's equation, dφ/dt = Δω − K·sin φ, which **locks iff |Δω| ≤ K**. *Checked:* slip rate √(Δω² − K²) to 3 decimals.
- For many oscillators with Lorentzian spread γ, the Kuramoto threshold is K_c = 2γ. *Checked:* r = 0.404, 0.610, 0.773 against theory 0.408, 0.612, 0.775.
- **Testable statement, not a finding:** returns phase-lock to the person's rhythm iff outcome-feedback strength exceeds the frequency mismatch. **Not tested on real data.** Locking was seen in one unpublished toy simulation of agents sharing a store (checked by a second, non-blind review).
  - It appeared once each loop could trigger the other, and that trigger-and-reset coupling forces it by construction, so it is not evidence for the statement above.
  - The toy's accuracy gains came from how much agents weighted shared error signals, not from the locking.
  - It showed no golden-ratio or torus effect, and the predicted locking staircase did not appear.
  - Any phase measure on real data must first be checked against coupling-definition and Sakaguchi-type phase-lag artifacts.

## Summary table

| # | Result | Status | Rests on |
|---|---|---|---|
| T1 | T\* = √(2c/(wσ²)); K\* ≈ √(q/r); cosh robustness | KNOWN + checked | EOQ (Harris 1913), Muth/Kalman 1960 |
| T2a | Watcher pays iff √(2w)σ(√c_main − √c_w) > h_w | PROOF (verified) | EOQ algebra |
| T2b | Escalation: needs ε < 1 − c_w/c_main | Accounting identity (not a result) | EOQ algebra |
| T3a | Sufficient condition N > (√(1+ρ)+1)²/ρ (not a cutoff) | PROOF; elementary, may be known | EOQ, MDL, joint replenishment |
| T3b | Per-level clocks save ≤ 29% (two levels) | KNOWN | Cauchy–Schwarz, Roundy 1985 |
| T3c | Decoupled nesting near-optimal iff time scales separate | NUMERIC; principle KNOWN | Tikhonov, Borkar 1997, Simon–Ando 1961 |
| T4 | Shared trace decays √N faster (small gain) | PROOF in regime; application UNCONFIRMED | Kalman averaging |
| T5 | Rise-then-fall under bounded loss; cliff under bounded fallback | PROOF; core KNOWN | Cho & Garcia-Molina 2003 |
| T6 | Nonpredictive memory ≤ dissipation (physical, no feedback) | KNOWN, toy-checked | Still et al. 2012 |
| T7 | Fractal iff world scale-free + power-law costs; geometric levels | PROOF (conditional); unconditional claim FAILS | EOQ homogeneity, Roundy, stable laws |
| T8 | Internal models; successive refinement (analogy only) | KNOWN | Francis–Wonham 1976; Equitz–Cover 1991; Lastras–Berger 2001 |
| T9 | Tori from topology/integrability; spheromak as a constrained energy minimum; coupled loops as phase-locking (not tested on real data) | KNOWN math/physics; link is ANALOGY | Liouville–Arnold, KAM, Arnold 1966, Poincaré–Hopf, Woltjer 1958, Taylor 1974/2000, Rosenbluth & Bussac 1979, Adler 1946, Kuramoto 1975 |

## Changes from the reviewed draft (independent review, `../reviews/independent-sim/REVIEW.md`)
- T7b: the convexity step now uses ψ(Δ) = Δφ(Δ) = 2 sinh(Δ/2) − Δ, the function actually being summed (issue 10).
- T7b: Roundy's 1.02 described as a worst-case bound; ours is a population mean ("same math"), and T7b called near-tautological (issues 11, prior-art table).
- T2b: relabeled as an accounting identity, with its assumptions (issue 6).
- T3a: stated as a sufficient condition, not a cutoff; the sim check called consistent but non-diagnostic (issues 1, 4).
- T1/T5: the small-λ formula marked as our expansion, not Cho & Garcia-Molina's (prior-art table).
- T1a: confidence factor z restored (issue 12).
- T8: successive refinement downgraded to an analogy (issue 7).
- T9: shortened to the standard math plus the untested phase-locking hypothesis; rhetorical wording removed (issue 13).
- Internal project references removed for privacy; no mathematical content was removed except as listed.

## Later corrections (2026-11-13, after a second review)
- **T6(a).** "Says nothing about firms" is replaced. The thermodynamic floor applies to every physical system but constrains nothing at firm scale; the bet is that the same tradeoff shapes design there in other currencies.
- **T9, spheromak.** Taylor relaxation in a spherical flux conserver gives a minimum-energy state with nested toroidal flux surfaces (Woltjer 1958; Taylor 1974, 2000; Rosenbluth & Bussac 1979). This was checked against the primary abstracts and texts. Toroidal flow is still not a general minimum-energy principle.
- **T9, phase-locking.** "Has not been tested" is replaced with what one unpublished agent toy showed. Its locking was forced by its coupling definition, and its accuracy effect was informational. The hypothesis remains untested on real data.
