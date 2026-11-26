# GENERAL_THEOREM: an attempt at the central theorem of A Theory of Adaptive Organization, and a red team of it

> **Status banner (19 Nov 2026, ET; added with THEORY v2.0).** Frozen derivation, public in this repository since 18 Nov 2026. The "private working file" line below is from its drafting and no longer holds. Off-repo paths below: `checks/` is `theory/theorem-v2-checks/`; `public-repo/` is this repository (`public-repo/theorems/THEOREMS.md` is `theory/THEOREMS.md`); `X_TEXT.txt` was an off-repo draft of the 12 Nov post (the posted text is archived in [`history/2026-11-12_X_POST.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-12_X_POST.md)). **Convention warning:** in §4 of this file z = σ√τ/B (the temperature); the canonical statement (`THEORY.md`; written against THEORY v2.0) and `theory/MATH_ATTACK.md` write z = B/(σ√τ) and call 1/z the temperature. Results here are listed in `measurement/CLAIM_MAP_v2.md` section O (v2.49).

Draft, Saturday 2026-11-14 (ET). Private working file. Nothing here was posted or sent, and nothing in `public-repo/` or the Looper README was edited.

**Sources read for this pass, from the files themselves:**
- `X_TEXT.txt`: the live post, v9.
- `public-repo/theorems/THEOREMS.md`: T1–T9.
- `REAUDIT_2026-11-13.md` §0.
- `tests/C3/RESULTS.md` and `DATA_NOTES.md`.

**Framing used (Chad's).** This is a general theory of any adaptive organization: cells, immune systems, ants, people, firms, cities. It is not a theory of everything. The physics is meant literally; only the currency of cost and the implementation change with scale.

**Labels.**
- **PROOF**: proved here, and checked by code.
- **KNOWN**: an existing result, with the citation fetched this pass.
- **CONJECTURE**: not proved.
- **FAILS**: the hoped-for statement is false or could not be proved, usually shown by a counterexample.
- **UNCONFIRMED novelty**: elementary; not found in a quick search; may well be known. Novelty is not claimed.

**Checks.** Every numerical claim is reproduced by `checks/c1…c8_*.py`, with outputs in the matching `.out` files. Re-run them all with `checks/run_all.sh` (Python venv `theorem-v2/.venv`: sympy 1.14, numpy 2.5.4, scipy 1.18.1).

---

## 0. Bottom line, in plain words

1. **One objective does give most of the rules, but the objective is decision theory, not the second law.**
   - **The objective.** Stay solvent: keep a reserve above zero, paying for losses, checks and memory out of income.
   - **What it yields.** Rules 2, 5 and 7, rule 4 trivially, the ex-ante form of rule 3, the weak form of rule 6, and the "late is worthless" part of rule 1. Each holds under stated conditions.
   - **What the physics contributes.** Every derivation goes through unchanged for any optimizer with those costs. The second law enters in only two places:
     - it is why persistence costs a continual throughput (there is a maintenance term at all);
     - it sets a physical floor on memory cost (Landauer; Still et al. 2012), which binds for cells and is negligible for firms.
   - **Verdict.** The shared structure across scales is information and decision theory running on a budget that thermodynamics forces to exist. "The same physics all the way up" is not proved by any of this. "The same optimization problem all the way up" is, conditionally.
2. **The new statement most worth claiming is Theorem P**, a quantitative, stochastic "must carry a model" theorem.
   - **Statement.** An agent facing an exogenous, drifting world can persist only if its memory carries at least R(y − c̄) bits of information about the future it must act on. R is the rate–distortion function of that future under the agent's loss; y − c̄ is the income left after other costs.
   - **Consequences.** A model is necessary if and only if acting blind is not viable. Lead time is capped by how fast predictive information decays. With a per-bit cost κ, carrying any model pays only if κ is below the marginal value of the first bit, and the optimal model size then grows only logarithmically with stakes.
   - **Status.** It is elementary: a rate–distortion converse plus random-walk ruin. Its ingredients are known, and its cousins are Kelly / Donaldson-Matasci et al. (growth ≤ information), Kolchinsky & Wolpert (viability-based semantic information) and Touchette & Lloyd. The packaging is UNCONFIRMED novelty.
   - **Comparison with older results.** It is weaker than the internal model principle on structure: it says how many bits, not that the bits must replicate the generator. It is stronger than Conant & Ashby on content: it is quantitative and stochastic, it covers prediction and cost, and it holds as a necessity for persistence rather than optimality.
3. **The general "rise, then fall to zero" of watching effort (Theorem G) holds for any stationary Markov world and any loss** (PROOF).
   - A periodically checked copy beats letting the fact fade if and only if drift speed × check cost < Φ. Φ is the integrated value of one fresh reading over its life.
   - Effort keeps rising with drift only when Φ = ∞, i.e. when staleness cost is unbounded.
   - It generalizes T5 and Cho & Garcia-Molina. It is likely known in substance in the age-of-information literature, so novelty is UNCONFIRMED.
4. **Temperature, done rigorously (Theorem R).** For diffusive errors with full resets, per-window ruin is exactly erfc(B/(σ√(2τ))). This is Black & Cox's first-passage default probability with zero drift, not Merton's terminal one.
   - **The index is forced by dimensional analysis.** z = σ√τ/B is the only dimensionless group available. That is why it is universal for diffusive errors, and also why it carries little content by itself.
   - **It breaks in four places:**
     - biased errors (a second group, μB/σ²);
     - heavy-tailed jumps (single-big-jump ruin, nearly independent of τ);
     - long memory (σ τ^H / B);
     - partial fixes.
   - **In calendar-time hazard, τ's exponent is not ½ of σ's.** The model's own ratio runs from about 0.42 in the cold regime to about 0.02 in the hot regime.
5. **C3 failed on proxy, and the theory now says why, quantitatively.** In the reset model, hazard × τ equals per-window ruin, so the observed dormancy hazard and τ alone pin z, with no units needed.
   - At C3's numbers (h ≈ 0.07/yr, median τ = 44 days), the model would predict a hazard ratio of about 11 per doubling of τ. C3 measured about 1.0 (upper CI ≈ 1.09).
   - So at most about 1–5% of OSS dormancy hazard can come from diffusive error accumulation reset at issue-close time.
   - **Reading.** Dormancy is not diffusive first passage at this τ. Either failures are jump-like (maintainers leave) or τ does not measure the fix interval. This kills the mechanism as posted for this proxy and scale. It does not kill the index where errors really are diffusive.
6. **Scale covariance (Theorem S).**
   - **Where it holds exactly.** The optimal structure is invariant to the currency exactly when the objective is homogeneous in one currency, and it is covariant under time rescaling.
   - **The exponents.** They depend on only two numbers: the loss exponent p and the drift scaling H. The interval scales as σ^(−p/(1+pH)). Smooth losses near an optimum (p = 2) and aggregated independent shocks (H = ½) make the "Gaussian–quadratic class" generic. This is a mean-field-style argument, and it FAILS for heavy tails, thresholds and long memory.
   - **Where it fails.** It provably fails whenever two cost components scale differently, which produces crossovers. That is the generic real case: a fixed per-check cost plus a size-proportional cost.
   - **The one currency-free statement.** In multiplicative (growth) persistence, a cue is worth at most its mutual information in nats of growth (Kelly 1956; Donaldson-Matasci et al. 2010), the dual of kT ln 2 of work per bit (Vinkler et al. 2016).
7. **Strongest objection.** It comes in three parts:
   - The rules are consequences of Bayesian decision theory with check and memory costs. They hold for any optimizer, self-maintaining or not.
   - "Behavior is optimal for some cost" is vacuous unless costs are measured independently (C7c).
   - Nothing guarantees real systems sit at the optimum (Alchian 1950: selection gives "as if" at best).

   So the theory's content lives entirely in predictions with independently measured costs, and its first such prediction, C3, failed on proxy in a way the theory itself now shows is decisive for that mechanism.

---

## 1. The general model (setting S)

**Discrete or continuous time t. The pieces:**
- **World.** X_t is a stationary, ergodic, time-homogeneous Markov process on a Polish space 𝒳. It is general Markov, not only a random walk. A drift speed λ rescales time: X^λ_t = X_{λt}.
- **Agent.**
  - It holds memory M_t, updated causally from observations Y_t, with p(y_t | x_t) and possibly costly checks.
  - It commits an action A_t = π(M_t) with lead time k ≥ 0: A_t meets the world at X_{t+k}.
  - k > 0 is "acting late is costly", meaning the action must be committed before the world it meets is revealed.
- **Loss.** ℓ(a, x) ≥ 0, arbitrary and measurable. Write the blind risk r_∞ = min_a E_π ℓ(a, X) under the stationary law.
- **Costs.** All are in one currency (heat, time or money):
  - c per check;
  - κ per bit of memory per step, standing for upkeep, update and erasure;
  - in a physical system meeting Still et al.'s conditions, additionally at least kT(I_mem − I_pred) of dissipation per step;
  - storage h per retained item.
- **Persistence.** A reserve R_t starts at B > 0 and has increments ΔR_t = y − ℓ(A_t, X_{t+k}) − (costs at t) + noise. Ruin occurs at the first t with R_t ≤ 0.
  - Objectives considered: P(no ruin); the Lundberg exponent θ (P_ruin ≈ e^{−θB}); for multiplicative systems, the growth rate.
  - **Why this encodes "far from equilibrium".** Without income the reserve only decays, so y > 0 is the second-law throughput requirement. This is the one place the second law enters literally.

**Assumptions used below (named so they can be attacked):**
- (A1) X is exogenous: no feedback from A to X. Relaxed in §5.
- (A2) Stationarity and ergodicity of (X, M) under the policy.
- (A3) Renewal checks: a check returns a reading of fixed quality and resets the copy. Retained history is relaxed in remarks.
- (A4) Costs additive in one currency.
- (A5) Bounded increments for the ruin results, or finite exponential moments for Lundberg.

---

## 2. Theorem P: persistence requires predictive information

**P0 (the bound) [PROOF; the ingredients are KNOWN].**
- **Hypotheses.** Assume (A1), (A2) and (A5). Let D(R) be the distortion-rate function of the stationary marginal of X under ℓ: D(R) = min over p(a | x) with I(A; X) ≤ R of E ℓ(A, X). Let I_pred = lim (1/T) Σ_t I(M_t; X_{t+k}).
- **Claim.** For every agent, the long-run mean loss is at least D(I_pred).
- **Corollary (persistence).** If y − c̄ < D(I_pred), ruin is certain. Here c̄ is the long-run mean of the other costs.
- **Proof.**
  - A_t is a function of M_t, so I(A_t; X_{t+k}) ≤ I(M_t; X_{t+k}) by data processing.
  - By the definition of D, E ℓ(A_t, X_{t+k}) ≥ D(I(A_t; X_{t+k})) ≥ D(I(M_t; X_{t+k})), since D is nonincreasing.
  - D is convex, so averaging over t and applying Jensen gives mean loss ≥ D(I_pred).
  - The reserve increments are then stationary and ergodic with mean ≤ y − c̄ − D(I_pred) < 0, so R_t → −∞ almost surely by the ergodic theorem.
  - At mean exactly 0, nondegenerate increments are recurrent, so ruin is also certain.
- **Sources.** The converse is Shannon's rate–distortion definition; the ruin step is the strong law / random-walk recurrence.
- **Checked (`c6`):**
  - The binary symmetric Markov world with Hamming loss and delayed readings sits exactly on D(R) = h⁻¹(1 − R).
  - Noisy memories also sit on or above the bound.
  - Ruin fractions are 1.000 just below the threshold and 0.002–0.029 just above it.
  - Linear-Gaussian agents in an AR(1) world achieve D(R) = Var·2^{−2R} exactly; a 1-bit sign memory is strictly above it (4.36 vs 4.02).

**P1 (when a model is necessary) [PROOF].** A model is necessary if and only if blind action is not viable.
- **Blind is not viable.** If r_∞ = D(0) > y − c̄, every persistent agent has I_pred > 0.
- **Blind is viable.** If D(0) ≤ y − c̄, persistence with I_pred = 0 is possible.
- **Erratum (19 Nov 2026, ET; math-attack REVIEW G3, applied with THEORY v2.0).** The inequality must be strict: at D(0) = y − c̄, P0's recurrence clause makes ruin certain. And c̄ depends on the policy (a blind agent pays no memory or read cost), so the threshold is per policy: blind action is viable iff some blind policy π₀ has D(0) < y − c̄(π₀); a model is necessary iff every blind policy has D(0) ≥ y − c̄(π₀). The recurrence step at equality also needs nondegenerate increments (positive asymptotic variance, as for i.i.d. or mixing increments); a bounded coboundary is the exception. This note governs the two bullets above.
- **Counterexample to the universal bet "every self-maintaining system pays to keep a model":** bet-hedging in an i.i.d. world (`c7d`).
  - A lineage with allocation f = p grows at ln 1.5 per generation with zero predictive information.
  - It carries a constant, the distribution, which needs no tracking.

**P2 (maximum lead time) [PROOF].**
- **Claim.** I(M_t; X_{t+k}) ≤ I(X_t; X_{t+k}), and the right-hand side is nonincreasing in k (data processing along the Markov chain). So persistence requires k ≤ k_max, where k_max is the largest k with I(X_t; X_{t+k}) ≥ R(y − c̄).
- **Example.** In the binary world with q = 0.05 and y = 0.30, k_max = 7 steps (`c6a`).
- **Meaning.** This is the quantitative core of rule 1's "early enough": there is a horizon beyond which no model, however good, makes acting ahead viable.

**P3 (when carrying a model pays, and how big) [PROOF of the threshold; the closed form is Gaussian].**
- **Setup.**
  - Let F(I) be the world's information-bottleneck curve: the maximum of I(M; X_{t+k}) over memories with I(M; past) ≤ I. It is concave and increasing.
  - Then D(F(I)) is a convex lower bound on achievable loss at memory I.
  - It is a lower bound because the IB-optimal memory need not also be the rate–distortion-optimal test channel. It is tight in the Gaussian and binary-symmetric cases.
- **Claim.** min_I [D(F(I)) + κI] has I\* > 0 if and only if κ < −(D∘F)′(0⁺): the first bit must be worth its cost.
- **Gaussian AR(1), coefficient a, quadratic loss:**
  - loss(I) = Var[(1 − a²) + a²·2^{−2I}];
  - carry a model if and only if κ < 2 ln 2 · a² · Var;
  - then **I\* = ½ log₂(2 ln 2 · a² · Var / κ)**: a model's size grows only logarithmically with stakes × predictable variance ÷ cost per bit (reverse water-filling form).
  - Checked by brute force over memory noise: 2.0014 vs 2.0018 bits (`c6d`).
- **The physics layer (physical systems meeting Still et al.'s conditions only).** Dissipation is at least kT(I_mem − I_pred). Persistence then demands the cheapest memory that clears the prediction floor: min I_mem subject to I_pred ≥ R(y − c̄). That is an information-bottleneck point whose operating level is set by the persistence budget.
  - Still (2020, PRL 124, 050601) already derives the information bottleneck from minimizing a dissipation bound. "Information bottleneck from physics" is therefore KNOWN and must not be claimed.
  - What P adds is the operating point: the persistence requirement fixes the level of I_pred.

**How P differs from the prior "must carry a model" theorems (all fetched this pass):**
- **Conant & Ashby (1970).**
  - *What they prove:* the simplest optimal regulator, with "good" meaning minimum outcome entropy H(Z) under a fixed p(S), can be taken to be a mapping from S to R.
  - *Their own concessions:* not all optimal regulators are models; inputs, noise and dynamics are omitted.
  - *Later critiques:* Wentworth (2021) notes the identity map counts as a model, and his repair adds expected utility, information arriving over time and storage cost. Virgo, Biehl, Baltieri & Capucci (2025, arXiv:2508.06326) replace "is a model" with "can be interpreted as having beliefs".
  - *How P differs:* P is quantitative (bits) and stochastic. It is about prediction at lead time k with costs, and it is a necessity for persistence, not a property of optimal regulators. It also says exactly when no model is needed.
- **Internal model principle (Francis & Wonham 1976, Automatica 12:457–465; Wonham 2018's set-theoretic version).**
  - *What it proves:* structurally stable, exact, asymptotic regulation of deterministic exosignals requires error feedback plus a reduplicated model of the signal generator.
  - *How P differs:* P concerns approximate regulation of stochastic signals and says nothing about structure, only quantity. The IMP is stronger on structure and needs exact regulation; P is weaker on structure but needs only persistence.
  - *What would be new:* a stochastic IMP (persistence ⇒ memory contains a sufficient statistic of the generator's predictive state up to R(y − c̄) bits). That is a CONJECTURE not attempted here; it is the natural next theorem.
- **Kelly (1956) / Donaldson-Matasci, Bergstrom & Lachmann (2010) / Rivoire & Leibler (2011).** For growth-rate fitness, a cue's fitness value is at most I(E; C), with equality under proportional betting (re-checked numerically in `c5d`). P is the additive-reserve counterpart: a lower bound on information needed, rather than an upper bound on its value.
- **Kolchinsky & Wolpert (2018, Interface Focus 8:20180041).** They define semantic information as the syntactic information causally necessary to maintain existence, via interventions that scramble correlations. P is a converse bound in the same spirit with a decision-theoretic viability criterion, not an interventional definition.
- **Touchette & Lloyd (2000, PRL 84:1156).** Feedback can reduce entropy by at most the information gathered. This is the control analogue, relevant once (A1) is dropped.
- **Sims (2003), Ortega & Braun (2013), Tishby & Polani (2011).** Expected utility minus an information cost: the same Lagrangian as P3, without the ruin constraint.

---

## 3. Theorem G: staleness, hold-or-fade, and the rise-then-fall of watching effort, for any Markov world and any loss

Setting: S with renewal checks (A3). A copy taken at age 0 is used by the Bayes action. Define r(u) = E[min_a E[ℓ(a, X_u) | reading at 0]] (staleness risk), with r(∞) = r_∞.

**G1 (monotone staleness, in age and in hops) [PROOF; KNOWN in substance].**
- **Claim.** For a stationary Markov world, r(u) is nondecreasing in u for every loss.
- **Proof.**
  - By stationarity, predicting X_{u+s} from X_0 has the same risk as predicting X_{u+2s} from X_s.
  - X_0 → X_s → X_{u+s} is Markov, so X_0 is a garbling of X_s with respect to X_{u+s}.
  - Blackwell (1953): a garbling never lowers Bayes risk.
- **Copies.** A chain of copies with independent hop noise is a garbling chain, so risk is nondecreasing in hops.
- **Prior art.** Sun & Cyr (arXiv:1812.07241, Lemma 1) prove the mutual-information version for stationary Markov sources.
- **Checked:** 0 violations in 300 random 5-state chains × random losses; copy-chain MSE 0, 0.23, 0.38, 0.47, 0.55 over 0–4 hops (`c1a`).
- **FAILS for non-Markov observed variables.** For an MA(2) signal, a 2-step-old reading has MSE 1.5 and a 1-step-old one has 2.0 (exact, and Monte Carlo 1.497 vs 1.998). Seasonality does the same (last Monday beats yesterday).
  - So rule 5's "a copy's error grows with time since the source was checked" holds in the full Markov state, not in arbitrary observed coordinates.

**G2 (hold or fade) [PROOF; UNCONFIRMED novelty; generalizes T5 and Cho & Garcia-Molina].**
- **Setup.**
  - Periodic checks every T at drift speed λ. With s = λT, the cost rate is J = λc/s + A(s), where A(s) = (1/s)∫₀ˢ r.
  - Fading (blind action) costs r_∞.
  - Note the identity s·(r_∞ − A(s)) = ∫₀ˢ (r_∞ − r(u)) du, which is nondecreasing in s.
- **Claim.** Holding beats fading if and only if
  **λ·c < Φ := ∫₀^∞ (r_∞ − r(u)) du**,
  where Φ is the integrated value of one fresh reading over its whole life, in drift-time units.
- **Equivalently.** The critical drift speed is λ_c = Φ/c: keep a fact while (chance needed × cost of missing it), integrated over its life, beats the cost of keeping it current. This is rule 2 exactly, with "rises with how fast it drifts" entering as λ.
- **State-dependent intervals** can only help, so Φ/c ≤ λ_c ≤ sup_x Φ\*(x)/c, with Φ\*(x) the same integral conditioned on the reading x.
- **Retained history** (filtering instead of renewal) can only lower holding cost, so λ < Φ/c stays sufficient for holding.
- **Checked:**
  - two-state chain with 0–1 loss: Φ = 1/4 predicts λ_c = 5.0, and the numerical optimum holds up to λ = 4.9999 and fades at 5.1;
  - Ornstein–Uhlenbeck process with quadratic loss: θ_c = 10, found exactly;
  - Monte Carlo cost 0.2916 vs analytic 0.2907 (`c1b`, `c1d`).

**G3 (rise, then fall) [PROOF].**
- **The rise.** f\*(λ) → 0 as λ → 0, as √(λ r′(0)/2c) when r′(0) is finite (checked: 0.03156 vs 0.03162). f\*(λ) > 0 on (0, λ_c) and f\* = 0 for λ ≥ λ_c.
- **Smooth fall vs cliff.** With blind fallback and r approaching r_∞ only asymptotically, f\* falls toward 0 as λ → λ_c, but only logarithmically when r approaches r_∞ exponentially (1.68, 1.18, 0.91, 0.74 at λ = 4.9, 4.99, 4.999, 4.9999). In practice that is a near-cliff.
- **Cliff.** With a bounded fallback F < r_∞ (read the source at use), there is a true cliff.
  - Holding stops at λ_c = Φ_F/c, with Φ_F = ∫₀^{s_F}(F − r) and s_F the age at which r reaches F.
  - Effort jumps from λ_c/s_F to 0. Predicted 1.1674; found between 1.1557 and 1.1791, with a jump from 2.54 (predicted 2.55) (`c1e`).
- **When effort never falls.** If Φ = ∞ (unbounded staleness cost with no fallback, e.g. a random walk under quadratic loss), holding always pays and effort rises without limit. This is T1/T5b's "only where staleness cost keeps growing".

**G4 (effort rises with stakes) [PROOF; Topkis 1978].** J(f; w) = cf + w·A(λ/f), and A(λ/f) is nonincreasing in f, so J has decreasing differences in (f, w). The minimizer is therefore nondecreasing in w. Checked: f\* rises monotonically over w = 0.5 → 8 (`c1c`).

**Scope.**
- G needs renewal checks and one item. Several items sharing a budget couple only through a shadow price (the Lagrange multiplier on the budget), which preserves G2–G4 item by item.
- Retained history and correlated items (T3) are outside the renewal proof.

---

## 4. Theorem R: temperature as a first-passage result

**Setting.** The error e_t = σW_t (plus optional bias μt) accumulates from 0 and is reset to 0 at fixes every τ. Ruin occurs when |e| ≥ B (two-sided) or e ≥ B (one-sided). Write z = σ√τ/B.

**R0 (dimensional forcing) [PROOF; Buckingham π].** With only σ [x·t^{−½}], τ [t] and B [x], z is the only dimensionless group. So per-window ruin is a function of z alone for any Brownian error model: resets, continuous correction, one- or two-sided.
- This is why the index is universal for diffusive errors, and also why it says little by itself.
- **Checked:**
  - (σ, τ, B) = (1,1,1), (2,¼,1) and (½,4,1) give 0.3187, 0.3181 and 0.3165 against exact 0.3173;
  - the continuous-correction (Ornstein–Uhlenbeck) mean first-passage times collapse exactly at equal z (`c2a`, `c2f`).

**R1 (exact results) [KNOWN; checked].**
- **One-sided (reflection principle).** P = erfc(1/(z√2)) = 2Φ̄(1/z). Monte Carlo agrees to 0.001–0.003.
- **Two-sided (Fourier series).** P = 1 − (4/π)Σ_k (−1)^k/(2k+1)·exp(−(2k+1)²π²z²/8). Checked at z = 0.3–2; it equals the image series to 6 digits.
- **With bias μ (Bachelier–Lévy).** P = Φ̄((B − μτ)/(σ√τ)) + e^{2μB/σ²}Φ̄((B + μτ)/(σ√τ)). A second group, the Péclet number μB/σ², appears.
  - At the same z, Pe = 0 gives 0.134 and Pe = 1.5 gives 0.433. **z alone FAILS once errors are biased.**
- **Continuous correction at rate 1/τ (Ornstein–Uhlenbeck).** Mean first-passage time ≈ τ√π·z·e^{1/z²} for small z. This is asymptotic: within 15% at z = 0.5 and 7% at z = 0.33 (`c2f`).

**R2 (Merton vs Black–Cox) [KNOWN; checked, `c8a`].**
- **Merton (1974).** Distance to default DD = [ln(V/D) + (μ − s²/2)T]/(s√T), with PD = Φ(−DD) (default only at maturity).
- **Black & Cox (1976).** Adds a first-passage barrier.
- **The correspondence.** With zero log-drift, Black–Cox gives 2Φ(−DD) (checked: 0.2345 exact vs Monte Carlo 0.2326). That is exactly our one-sided formula, with buffer = ln(V/D) and **z = 1/DD**, horizon = the fix interval.
- **Correction to the post's wording.** The posted "form of Merton's distance to default" is right about the index but wrong by a factor of 2 on probability. The first-passage version is Black–Cox's.

**R3 (where slow fixing hurts most) [PROOF within the model].**
- **One fix window.** ∂P/∂z peaks at z = 1/√2 and ∂P/∂ln τ peaks at **z = 1**; both vanish at both extremes (`c2e`). This supports the post's "most of the extra failures land where shocks are large relative to buffers, as long as slow fixers still usually survive a fix window".
- **Calendar time.** Hazard h = (σ²/B²)·G(z) with G(z) = −ln S(z)/z².
  - **Two-sided (hot regime):** G → π²/8, so in the hot regime the fix interval stops mattering: hazard is set by the diffusion time B²/σ² (within 10% for z ≳ 1.5).
  - **One-sided:** G → 0 as z → ∞ (non-monotone).
  - **Elasticity:** d ln h/d ln τ is 12.0, 5.0, 1.49, 0.24, 0.05 and 0.01 at z = 0.2, 0.3, 0.5, 1, 2 and 4. So in the cold regime slow fixing multiplies rare failures many-fold, as the post says.

**R4 (the τ/σ exponent ratio is not ½ in calendar time) [PROOF; corrects C3's prereg band].**
- **Claim.** r_τ = (∂ln h/∂ln τ)/(∂ln h/∂ln(σ/B)) = g/(2(2 + g)), with g = d ln G/d ln z.
- **Values.** 0.42 at z = 0.3, 0.30 at z = 0.5, 0.10 at z = 1, 0.02 at z = 2 (`c8b`). Exactly ½ holds only for per-window risk.
- **Consequence for C3.** C3's band r_τ ∈ [0.25, 1] was correct only in the cold regime.

**R5 (where the index fails) [PROOF/NUMERIC; the ruin asymptotics are KNOWN].**
- **Heavy-tailed jumps.** Under compound Poisson jumps with Pareto sizes (α = 1.5), ruin is dominated by single big jumps (Embrechts & Veraverbeke 1982).
  - Calendar hazard was 0.024, 0.024, 0.026, 0.029 and 0.035 for τ = ¼ to 4, against a single-jump rate of 0.022.
  - The τ elasticity is about 0.14, against 1.5–12 for diffusive errors at z ≤ 0.5 (`c2g`).
- **Correlated (long-memory) shocks.** Under fractional Brownian motion with H = 0.75, the group becomes σ τ^H/B.
  - At the same σ τ^H: 0.0766 vs 0.0768. At the same σ√τ: 0.0766 vs 0.1704 (`c2h`).
- **Fixes that don't reset.** Shrinking the error by (1 − k) at each fix makes the effective variable roughly τ/(k(2 − k)). The approximation holds within about 2× at k = 0.2 (`c2i`).
- **Error correction that is itself the failure.** If the fix process stops (maintainers leave), τ jumps to ∞: a jump hazard on τ, not a diffusion against B.

**R6 (why τ did not show up in C3) [PROOF of a units-free consistency test + NUMERIC mechanisms].**
- **The test.**
  - In the reset model, h·τ = −ln S(z): per-window ruin. So the observed hazard and τ alone determine z; no units for σ or B are needed.
  - With C3 coding A (137/896 dormant over 2.33 yr, h = 0.071/yr) at median τ = 44 d, z ≈ 0.35. The model then predicts d ln h/d ln τ ≈ 3.5, i.e. a **hazard ratio of about 11 per doubling of τ**.
  - C3 measured about 1.00–1.02, with upper CI exp(0.693 × 0.12) ≈ 1.09.
  - If only a share φ of hazard were diffusive, φ ≤ 0.8% at τ = 44 d (0.2% at 7 d, 2.2% at 180 d, 5.2% at 546 d). This is conservative: a smaller diffusive share implies a colder z and a larger elasticity (`c2j`).
- **No regime fits.** The hot regime would fit the null τ effect (R3/R4), but it needs h·τ ≈ 1, i.e. h ≈ 8/yr at τ = 44 d. That is impossible at C3's event rate. **No regime of the diffusive-reset model fits both the hazard level and the null τ effect.**
- **Mechanisms that dilute a real τ effect** (`c4`, simulated C3-style logit, true β_lnτ = +2.66 when failure is purely diffusive):

| Simulated case (`c4`) | β_lnτ |
|---|---|
| Pure diffusive failure (the true model) | +2.66 |
| Add τ-independent jump hazard (diffusive share 0.75) | +0.85 |
| Plus τ measured with noise (sd 1 in ln τ) | +0.40 |
| Plus unmeasured shock frailty and survivor selection | +0.18 |

  - Even with every dilution stacked, β stays above C3's upper CI (0.10–0.12) unless the diffusive share is small.
- **Verdict on C3 (FAILS for this mechanism at this scale and proxy).**
  - **Erratum (19 Nov 2026, ET; math-attack REVIEW G1, applied with THEORY v2.0).** Every C3 conclusion in this file (§0 item 5, this R6, §8, §9 items 2, 9 and the closing line) holds only if the fix interval is **deterministic (or narrowly distributed) and exogenous** given (σ, B). With random fix intervals the same pinning predicts a hazard ratio per doubling of 3.0 (exponential), 2.1 (lognormal, sd 1), 1.5 (Pareto κ = 1.5), 1.26 (Pareto κ = 1.2) or 1.20 (lognormal, sd 2), and the diffusive share of hazard compatible with C3 rises from ≈1% to ≈4%, 8%, 18%, 34% or 43% (`reviews/math-attack/review_checks/review_checks.out` R2b). If τ is chosen in response to z, the coefficient can lie anywhere down to −1. So C3 excludes a deterministic, exogenous reset clock at that proxy; with heavy-tailed or endogenous fix intervals it does not. Read "rules out", "at most about 1–5%" and "dead" below and above with this condition. In the repo's vocabulary C3 is a **proxy result** (CLAIM_MAP H15, PROXY-FAIL), not a kill of the theory.
  - OSS dormancy is not diffusive error accumulation reset at issue-close time.
  - The surviving readings are: (i) dormancy is jump-like (people leave); (ii) issue-close time is not the error-correction interval; (iii) both.
  - A fair second test needs a setting where errors are plausibly diffusive and the fix interval is measured directly.
  - **Hypothesis:** inventory or cash-flow buffers with known review periods, or the planned exogenous-shock arm (adaptation lag to upstream breaking releases).

---

## 5. Theorem L: persistence as the single objective (Lundberg), and how it relates to expected cost

**Setting.** Reserve income y dt + s₀dW₀. A check costs c every τ. Holding loss is w·e_t² dt with e = σW reset at checks. The cycle increment is D = yτ − c − wσ²∫₀^τ W² + s₀√τ N.

**L1 [PROOF; Cramér–Lundberg KNOWN (Asmussen & Albrecher 2010)].**
- **Claim.** P_ruin ≤ e^{−θB}, with θ the root of E e^{−θD} = 1. Exactly:
  −θ(yτ − c) + θ²s₀²τ/2 − ½ ln cos(τ√(2θwσ²)) = 0.
- **Ingredients.** The last term uses E e^{b∫W²} = cos(τ√(2b))^{−½}; checked by Monte Carlo, 1.1822 vs 1.1829. The diffusion approximation is θ ≈ 2m/s², with mean margin m = y − c/τ − wσ²τ/2 and s² = s₀² + w²σ⁴τ³/3; the Var ∫₀^τ W² = τ⁴/3 term is checked as 0.331 vs ⅓.
- **Checked against Monte Carlo ruin.** The bound holds, and the decay rate in B matches θ (ratio between B = 0.5 and 1: 13.9 vs e^{θ/2} = 13.9) (`c3c`).

**L2 (survival-optimal ≠ cost-optimal) [PROOF in the diffusion approximation; checked exactly].**
- **Survival-optimal checking is faster.** Maximizing θ(τ) gives τ\* = 0.258, against the EOQ cost-optimal 0.316, because loss variance grows like τ³.
- **When the two agree.** EOQ is the limit where policy barely changes the variance (s₀² dominant): there, maximizing survival is minimizing expected cost.
- **This is the unification.** The expected-cost results T1–T5 are the large-buffer, policy-insensitive-variance limit of the persistence objective. Persistence adds a risk-sensitivity correction, the same direction as risk-sensitive control (Jacobson 1973; Whittle 1990): more caution.

**L3 (the buffer doesn't set the interval; it sets what survival is worth) [PROOF].**
- **The interval.** argmax_τ θ(τ) does not involve B, so under Lundberg asymptotics the optimal check interval is independent of the buffer.
- **What the buffer does set.** The marginal value of raising θ is V·B·e^{−θB}, maximized at **θB = 1**: effort to improve survival is worth most when the buffer is about one ruin length s²/(2m).
- **Status of rule 7's last clause.** "Watch most where shocks are large relative to buffers but not yet overwhelming them" follows as a statement about the value of extra effort. It FAILS as a statement about the cost-optimal interval, which ignores B.

---

## 6. Theorem S: scale covariance and its limits

**S1 (currency invariance) [PROOF, trivial].** If the objective is positively homogeneous of degree 1 in one currency, J(k·costs) = k·J, so the argmin is invariant (`c5b`). The same holds for:
- constant-relative-risk objectives (log, power);
- the Kelly growth rate, since W → kW adds ln k to log-wealth;
- ruin probabilities when B, σ and all costs are in the same currency (only ratios enter).

**S2 (time covariance) [PROOF, trivial].** Rescaling time by k rescales optimal frequencies by k (checked: ratio = 1/3 at k = 3).

**S3 (universality classes) [PROOF of the exponents; CONJECTURE that real systems sit in the generic class].**
- **The exponents.** With loss w|e|^p and self-similar drift e ~ σt^H Z:
  - **T\* = [c(pH + 1)/(pH · m_p · w σ^p)]^{1/(1+pH)}**;
  - exponent on σ: −p/(1 + pH); exponent on c/w: 1/(1 + pH).
  - Values: (p, H) = (2, ½) → −1; (1, ½) → −⅔; (2, ¾) → −⅘.
  - Monte Carlo for p = 1 puts the minimum at T/T\* = 1.00 (`c5a`).
- **So the exponents depend only on two numbers (p, H), not on the currency.** This is the defensible sense of "same structure at every scale".
- **Why the Gaussian–quadratic class (p = 2, H = ½) is generic.** Any smooth loss is quadratic near its optimum (Taylor). Sums of many weakly dependent shocks are diffusive (central limit theorem). This is a mean-field-style universality argument.
- **Where it FAILS.**
  - heavy tails (α-stable: H = 1/α);
  - long memory (H ≠ ½);
  - thresholds and deadlines (p → 0, the Cho–Garcia-Molina regime);
  - drift with a characteristic time (mean reversion, seasonality).

**S4 (impossibility) [PROOF].** Covariance cannot hold when two cost components scale differently with size or currency.
- **Example.** Check cost = fixed + size-proportional. The local exponent of T\*(n) then slides from −1 to −½ over n = 1…10⁶: a crossover, not a power law (`c5c`).
- **In general.** Only the exchange rates between cost components (dimensionless ratios) matter. Changing one rate changes the optimum by k^{1/(1+pH)}.
- **Landauer's floor** is one such fixed-unit component. It is kT ln 2 ≈ 3×10⁻²¹ J per bit at room temperature, many orders of magnitude below what a bit costs a firm in money or attention, which is why it constrains cells and not firms.
- **Consequence.** "Only the currency differs" is true exactly when one currency dominates every cost line. Otherwise the theory predicts crossovers between regimes.

**S5 (the only currency-free exchange rate) [KNOWN].**
- **The statement.** In multiplicative persistence, a cue is worth at most I(E; C) nats of growth per generation, with equality under proportional allocation (Kelly 1956; Donaldson-Matasci et al. 2010; re-checked: gain = I to 6 digits, `c5d`).
- **The physical dual.** Measurement-based work extraction gives at most kT ln 2 per bit (Vinkler, Permuter & Merhav 2016, doi 10.1088/1742-5468/2016/04/043403).
- **Reading.** This is the one place where "same tradeoff, different currency" is literally exact: a bit buys ln 2 of log-growth or kT ln 2 of work.
- **Limit.** It needs multiplicative dynamics (cells, populations, compounding capital). Additive-reserve organizations get problem-specific exchange rates, namely the slope of D(R).

---

## 7. Which rules follow, under what assumptions

| Rule | Follows? | From | Assumptions | What does not follow |
|---|---|---|---|---|
| 1. Return early; interrupt iff stake × P + teaching > cost | Partly | P2 (lead-time cap); value of information after commitment = 0 (trivial) | (A1), Markov | The myopic interrupt rule FAILS in general. Each XOR signal alone has zero value of information, but together they are perfect (`c7e`). The rule is exact only when "teaching" is the full continuation value, which makes it the Bellman equation. |
| 2. Keep a fact while need × miss-cost beats upkeep, which rises with drift | **Yes** | G2: λc < Φ | Renewal checks, stationary Markov, any loss | "Recoverably" is not derived (it is option value; trivial if re-acquisition is possible). |
| 3. Move a belief further the more reliable the signal | Partly | Gaussian: weight = precision ratio (KNOWN). Ex ante: more informative ⇒ mean-preserving spread of posteriors (Blackwell) | Gaussian, or ex-ante reading | Realization-wise FAILS. With Cauchy noise, E[X\|s] rises then falls (1.06 at s = 2, 0.07 at s = 30): very surprising reports are discounted (O'Hagan 1979). |
| 4. Keep prior versions while need × loss beats keeping cost | Trivially | G2 at λ = 0: keep iff h < μ·loss | — | "Keep every prior version" and "a wrong overwrite usually costs more" are empirical claims, not derived. Erasure isn't free either (Landauer), which favors keeping, weakly. |
| 5. Act from the current model; copy error grows with hops and age | **Yes** (Markov) | G1 (data processing, Blackwell) | Markov in the stored variable | FAILS for non-Markov observed variables: MA(2) and seasonality. |
| 6. Record outcomes; use carries the signal (Hebb, trails) | Weakly | Recording has value of information ≥ 0 when free, > 0 iff it changes future decisions (Blackwell); without outcomes the posterior over relevance = prior | — | The mechanism (Hebbian or stigmergic, no one in charge) does NOT follow from any objective here. Only its √N trail-fade consequence (T4) is derived once a shared trace exists. "Same mechanism at every level" stays a CONJECTURE. |
| 7a. More watching as stakes rise | **Yes** | G4 (Topkis) | Linear-in-loss objective | — |
| 7b. With drift: rise, then fall to none; keeps rising only if staleness cost is unbounded | **Yes** | G3 (Φ < ∞ vs Φ = ∞; cliff under a bounded fallback) | Stationary Markov, renewal | — |
| 7c. Watch most where shocks are large relative to buffers but not overwhelming | Yes, as the value of effort | R3 (peak at z = 1 for one window); L3 (θB = 1) | Diffusive errors | FAILS for heavy-tailed jumps. The cost-optimal interval ignores B under Lundberg. |
| "Every self-maintaining system pays to keep a model" | **Only conditionally** | P1: iff blind is not viable and κ < marginal value of the first bit | (A1) | FAILS universally: bet-hedging (`c7d`); viable blind policies; regulating the world instead of modeling it (dropping (A1), Touchette–Lloyd); cheap buffers. |

**One objective?** Yes, the solvency objective of §1.
- **What it yields.** P comes directly. G, and rule 7, come in its expected-cost limit (L2), and L/R give its finite-buffer corrections. Rule 3 needs Gaussian structure or the ex-ante reading.
- **What it does not yield.** Neither the mechanism in rule 6 nor the universality of "carry a model".

---

## 8. Relation to the big results (statements checked against fetched sources this pass)

**Thermodynamics of prediction**
- **Still, Sivak, Bell & Crooks (2012), PRL 109:120604** (already checked in THEOREMS T6).
  - *What it says:* β⟨W_diss⟩ per step equals I_mem − I_pred, under its conditions: driven, no feedback, Markov, a heat bath.
  - *Relation:* P3 uses it only as the physical memory-cost term, and only where those conditions hold.
- **Still (2020), "Thermodynamic cost and benefit of memory", PRL 124:050601.** For partially observable information engines:
  - the dissipation floor is proportional to irrelevant information;
  - maximizing the bound on net work (with a temperature difference) yields the information bottleneck, max I[Y, Z] − λI[X, Z] with λ = T/T′.
  - *Relation:* "IB from physics" is **KNOWN**. Our contribution can only be setting the operating point by persistence (P3).
- **Tishby, Pereira & Bialek (1999), the information bottleneck.** KNOWN; it is the compression side of P3.
- **Bialek, Nemenman & Tishby (2001), Neural Computation 13:2409.** Predictive information I(past; future) can be finite or grow logarithmically or as a power law. In P2 it is the ceiling on what any memory can carry; the theory adds nothing to it.

**Rate–distortion and costly information**
- **Rate–distortion with drift; rational inattention (Sims 2003, J. Monetary Econ. 50:665–690).**
  - *What it says:* actions pass through a finite-capacity channel. Gaussian sequential versions give Kalman-like filters with drift-set gains (T1b).
  - *Relation:* P's converse is the stationary single-letter bound.
- **Ortega & Braun (2013, Proc. R. Soc. A 469:20120683); Tishby & Polani (2011, Perception-Action Cycle, 601–636).** Expected utility minus an information cost: the P3 Lagrangian without ruin.

**"Must carry a model" theorems**
- **Good regulator theorem (Conant & Ashby 1970).** See §2: weak and widely criticized. P differs in every listed respect.
- **Internal model principle (Francis & Wonham 1976).** See §2: the closest rigorous prior "must carry a model" theorem. It is stronger on structure; P is stochastic and quantitative. The open target is a stochastic IMP.

**Free energy and dissipation**
- **Free-energy principle (Friston 2010, Nat. Rev. Neurosci. 11:127–138).**
  - *What it says:* self-organizing systems minimize variational free energy, a bound on surprise.
  - *Critiques:* Biehl, Pollock & Kanai (2021, Entropy 23:293) show the original free-energy lemma is false in general and that the Markov-blanket definitions are not equivalent. Aguilera et al. (2022, Phys. Life Rev.) show its conditions hold only in narrow regimes of linear systems.
  - *Relation:* nothing here assumes or implies free-energy minimization. P is a necessary condition derived from an explicit solvency constraint, which avoids the FEP's main technical problems. The price is that P says less: a bound, not a dynamics.
- **England (2013, J. Chem. Phys. 139:121923; 2015, Nat. Nanotech. 10:919–923).**
  - *What it says:* the 2013 paper bounds heat production for self-replication. The 2015 perspective proposes "dissipative adaptation": driven matter preferentially reaching states that absorb and dissipate work.
  - *Relation:* it is about which structures appear, not about prediction or memory cost. It shares the far-from-equilibrium premise and nothing else. Treat any claim that it supports this theory as ANALOGY.

**Value of information**
- **Kelly (1956, BSTJ 35:917–926); Donaldson-Matasci, Bergstrom & Lachmann (2010, Oikos 119:219–230); Rivoire & Leibler (2011, J. Stat. Phys. 142:1124–1166).** Growth gain ≤ mutual information. This is S5, and the multiplicative counterpart of P.
- **Kolchinsky & Wolpert (2018).** Viability-based semantic information. This is the closest conceptual prior art to "information needed to persist". P is a converse bound in the same spirit with a decision-theoretic viability criterion, not an interventional definition.

**Ruin and default**
- **Age-of-information sampling (Sun & Cyr, arXiv:1812.07241).** Optimal sampling for monotone age penalties is a threshold policy; MI-freshness is nonincreasing in age for stationary Markov sources. This is prior art for G1 and close to G2.
- **Ruin and credit:**
  - Merton (1974, J. Finance 29:449), Black & Cox (1976, J. Finance 31:351): R2.
  - Embrechts & Veraverbeke (1982, Insurance Math. Econ. 1:55–72): the heavy-tail failure of R.
  - Asmussen & Albrecher (2010): L1.

**What is new versus known:**
- **New as a theorem (UNCONFIRMED novelty, elementary):**
  - P0–P3 as packaged: minimum viable predictive information R(y − c̄), the lead-time cap, and the "first bit must pay" threshold with the logarithmic model-size law;
  - G2's λ_c = Φ/c for general Markov worlds and arbitrary loss;
  - R4's calendar-time exponent ratio;
  - S3's exponent −p/(1 + pH) as a classification.
- **New as analysis (not a theorem):** R6's units-free test showing C3 excludes the diffusive-reset mechanism to within a few percent of hazard.
- **Known:** everything else, including the information bottleneck from thermodynamics, the temperature formulas, the Black–Cox correspondence, Kelly's information value and the Blackwell monotonicity.

---

## 9. Red team: the strongest objections, with verdicts

1. **"This is decision theory in a lab coat."** The derivations never use the second law; they hold for a thermostat designer, a portfolio manager and a cell alike.
   - **Verdict: correct; it survives only in a reduced form.** The literal physics enters as (a) the existence of a maintenance cost (why y > 0 is needed) and (b) a memory-cost floor (Landauer; Still) that binds only for molecular and cellular systems.
   - The claim that can be defended is "one optimization problem at every scale, whose budget the second law guarantees exists". "The same physics doing the work at every scale" is not established by any theorem here, and Chad's framing should not claim it is.
2. **"Optimal for some cost" is vacuous.** Every policy is the unique optimum of some loss (`c7c`).
   - **Verdict: correct.** Predictions have content only with costs, stakes and drifts measured independently of the behavior they predict. That is how C3 was built, and it failed on proxy.
3. **There is no mechanism that puts real systems at the optimum.** Alchian (1950): selection rewards relative, realized success; "as if" optimization is at best an approximation.
   - **Verdict: open.** The theory needs either a selection argument (survivors are near the persistence frontier P0, which is testable) or a learning argument (outcome-driven updating, rule 6).
4. **The temperature index is forced by dimensional analysis, so it has no content.**
   - **Verdict: half right.** The functional form is forced for diffusive errors. The content lies in (i) diffusive scaling (√τ, H = ½) rather than jumps or long memory, and (ii) the calendar-time elasticities (R3, R4).
   - The C3 data refute (i) for OSS dormancy (R6). The posted prediction survives only where errors are demonstrably diffusive and the fix interval is directly measured.
5. **Feedback breaks everything.** Agents act on their worlds, violating Still's no-feedback condition and (A1).
   - **Verdict: partly.** P's bound still holds with the policy-induced marginal D_π, but the agent can then buy persistence by stabilizing the world (lowering H(X)) instead of modeling it (Touchette & Lloyd; Sagawa & Ueda 2010 for the thermodynamics).
   - "Model the world or make it predictable" is the honest version. Niche construction and regulation are the second strategy.
6. **Non-Markov observed variables.** Seasonality breaks rule 5's age monotonicity (G1 fails, `c1a`).
   - **Verdict: correct.** The rule holds in the predictive (Markov) state, which a good model has to discover. That is a real requirement, not a technicality.
7. **Heavy tails and regime shifts.** Big jumps set ruin; the quadratic and diffusive class does not apply.
   - **Verdict: correct where tails are heavy.** S3 gives the exponents for α-stable drift, but ruin is set by the single big jump and buffers sized to σ√τ are irrelevant. Firm and city data are often heavy-tailed, which may itself explain C3.
8. **"Every self-maintaining system keeps a model" is false.** Bet-hedging, cheap buffers, viable blind policies and regulation are all counterexamples.
   - **Verdict: correct.** P1 replaces it with an exact condition. That condition is testable: blind viability, and the first-bit threshold κ < 2 ln 2·a²·Var in the Gaussian case.
9. **Kill rule.** C3 failed at scale 1 on the τ term.
   - **Verdict.** The posted kill rule needs two scales. But by R6 the diffusive-reset mechanism, as operationalized with issue-close time, is effectively excluded for OSS. A second-scale test is only informative if it uses a directly measured fix interval in a diffusive-error setting.

**Can any part not survive?** Five things do not:
- the universal "every self-maintaining system must carry a model";
- the calendar-time ratio r_τ = ½;
- the realization-wise form of rule 3;
- unconditional age monotonicity (rule 5);
- the derivation of rule 6's mechanism.

The τ term as operationalized in C3 is dead for that scale and proxy.

What survives: P, G and R/L as conditional theorems; S as a conditional universality with explicit failure conditions; and the "same optimization problem at every scale" framing.

---

## 10. Next steps (proposed; not started)

1. **Stochastic internal model principle (CONJECTURE).** Persistence at margin ε implies the memory contains an ε-sufficient statistic of the world's predictive (causal) state, with a quantitative bound, extending Francis & Wonham beyond deterministic exosignals. This is the theorem that would make the theory more than a toolkit.
2. **A second-scale test aimed at the surviving mechanism.** Use a setting with diffusive errors and a directly observed fix interval: inventory with known review periods, or cash buffers with known reconciliation cycles. Preregister R3/R4's elasticity curve, including the hot-regime flattening, plus the R6 units-free check.
3. **Test P1's threshold** in a lab or biology dataset where a blind strategy is viable or not (bet-hedging vs sensing in microbes), as a cross-scale check.
4. **Alignment items for the post and README, for Chad's decision only. Nothing was edited:**
   - (a) "Merton's distance to default" should read "first-passage (Black–Cox) form of Merton's distance to default".
   - (b) The τ prediction should state the calendar-time ratio and the hot-regime flattening.
   - (c) C3's result should be reported with R6's bound.

---

## Files
- `checks/c1_staleness_holdfade.py`: G1–G4.
- `checks/c2_ruin_temperature.py`: R0–R6.
- `checks/c3_lundberg_persistence.py`: L1–L3.
- `checks/c4_why_tau_vanishes.py`: R6 mechanisms.
- `checks/c5_scaling_universality.py`: S1–S5.
- `checks/c6_persistence_bound.py`: P0–P3.
- `checks/c7_rules_counterexamples.py`: rules 1 and 3, vacuity, bet-hedging.
- `checks/c8_merton_and_index_ratio.py`: R2 and R4.
- `checks/run_all.sh`: re-runs everything.
