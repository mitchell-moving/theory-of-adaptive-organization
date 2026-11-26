# The stochastic internal-model theorem, and where (if anywhere) the second law does work above the cell

*Draft by the executor subagent, Sat 14 Nov 2026 (~11 PM ET). Self-checked only. There has been **no independent, blind review** of this file.*

> **Status banner (19 Nov 2026, ET; added with THEORY v2.0).** Frozen derivation, public in this repository since 18 Nov 2026. Off-repo paths below: `checks/` is `theory/theorem-v2-checks/`; `attack/math/REVIEW.md` is `reviews/math-attack/REVIEW.md`. I5 is core result CT6 of THEORY v2.0 (CLAIM_MAP section O).
*Labels: **PROOF** (proved here, checked numerically), **KNOWN** (in the literature; the source was fetched), **CONJECTURE**, **FAILS** (refuted or excluded). **UNCONFIRMED novelty** means I found no prior art, which is not evidence that none exists.*
*Checks: `checks/i1_internal_model.py`, `i2_maintenance_sdpi.py`, `i3_throughput_scaling.py`, `i4_nonstationary_datarate.py`, each with a `.out` file. All four print `ALL OK`. `run_all.sh` re-runs them with c1–c8.*

This revision answers the review in `attack/math/REVIEW.md` (G2, O1). It builds on and cites:
- Stratonovich's value of information;
- the data-rate theorems (Nair & Evans 2004; Tatikonda & Mitter 2004);
- Polani et al. 2006;
- the thermodynamic tracking floor (Mitter & Newton 2005; Horowitz & Sandberg 2014).

It also extends the work to random-walk and unstable worlds (§4).

---

## 0. Bottom line, in plain words

1. **Yes, there is a stochastic internal-model theorem, and it is quantitative (I1–I3, PROOF).**
   - Take any agent whose memory is a function of the past, scored on log-loss over the next L steps. Its excess loss *equals* I(S; future | M): the predictive information about the world's causal state S that its memory M misses.
   - Solvency caps that miss at (margin − bit cost)/stakes.
   - When the causal states are separated by γ (total variation over L-blocks), the agent's memory must decode the causal state with error at most √(2·miss)/γ.
   - The agent's own update rule must then shadow the ε-machine's transitions, with error at most twice that.
   - At zero miss this becomes Shalizi & Crutchfield's prescient-rival theorem (KNOWN). The quantitative, solvency-indexed version is **UNCONFIRMED novelty**, but the proof is elementary (Pinsker plus a triangle inequality), so it is probably folklore somewhere.
   - What the data-rate theorems do **not** give is the *structural* conclusion. They give rates; this gives "the agent's state is a near-copy of the world's causal state, and its dynamics are a near-homomorphism of the world's."
2. **The bound holds but is loose.** In exact numerics on the Even process and on random 4-state machines:
   - the √ bound is often vacuous (> 1) at realistic misses;
   - the true decoding error tracks the miss *linearly*, at about 0.5–2.4 × the miss in bits.
   - A linear bound under stronger separation is a CONJECTURE.
3. **What is forced is only decision-relevant (FAILS for general losses).**
   - Under Hamming loss on the Even process, a memoryless agent that always says "1" is exactly optimal and knows nothing about S.
   - Only log-loss (or another strictly proper score) forces the full causal state.
   - Finite memory can never be exact for nonunifilar worlds, which have infinitely many causal states.
   - Rolling windows are never exact for finite-state worlds of infinite Markov order (the Even process). There, a 2-state automaton is exact while any k-window misses about 2^(−k/2). "History length" is the wrong measure of a model.
4. **Upkeep is a flow (I5, PROOF; the Gaussian case is KNOWN).**
   - Holding I bits about a drifting world needs an observation inflow of at least (1 − η)·I bits per step, where η is the world's contraction coefficient. For a bit that flips with probability q, this is about 4q·I.
   - The Kalman filter meets the Gaussian version *with equality*, consistent with Mitter–Newton and Horowitz–Sandberg.
   - Corollary (PROOF): there is a **precision ceiling**. With inflow r bits/step in an AR(a) world, I ≤ r + ½log₂(1/(1 − a²)).
   - For a random walk or an unstable world (|a| ≥ 1), the needed rate is ≥ log₂|a| + ½log₂(1 + q/(a²P)). That is the Nair–Evans data-rate floor (KNOWN), checked by Monte Carlo with real quantizers.
5. **Throughput scaling: a definite, testable cross-scale law.**
   - Model the world as modes with variance spectrum λ_i ∝ i^(−β), set stakes ∝ throughput Q (an *assumption*), and charge bits at a fixed price.
   - Stationary (mean-reverting) world: optimal model bits ∝ Q^(1/β) (PROOF; reverse water-filling, a KNOWN tool).
   - Random-walk (drifting) world: the information *rate* ∝ Q^(min(1/2, 1/β)) (PROOF). For β ≤ 2 the rate is dominated by the many slowly drifting modes and follows the square-root/EOQ law.
   - New FAILS: an infinite random-walk world with β ≤ 2 and unbounded per-mode loss is **not viable** at any finite rate.
   - Unstable modes add a stakes-independent "survival tax" F = Σ log₂|a_i| (Nair–Evans). This gives a **minimum viable size** Q_min = κF/μ.
   - The information share of throughput has an interior optimum **iff β < 1**. For β ≥ 1 it falls with size monotonically.
   - β is *measurable independently* from the environment's spectrum:
     - a 1/f^α field in d dimensions gives β = α/d (PROOF);
     - natural images give β = 1.81/2 = 0.905 (Ruderman & Bialek 1994, KNOWN);
     - 1/f temporal noise gives β = 1.
6. **Existing data is consistent with the law but does not discriminate it (honest).**
   - Brain mass ∝ M^0.75 ∝ BMR (Martin 1981): implied β = 1.
   - Brain energy ∝ brain volume^0.86 (Karbowski 2007): implied β ≈ 1.16.
   - City administrative staff ∝ N^~1.2 (Hutcheson & Prather 1979, abstract-level only) against GDP ∝ N^1.13–1.26 (Bettencourt et al. 2007): admin ∝ GDP^0.94–1.05, so β ≈ 1.
   - Firms (Blau 1970: the administrative ratio falls with size) need β > 1 or the drift regime.
   - **But the null model "every organ or department takes a fixed share of the budget" also predicts exponent 1.** No dataset I found separates the two. The discriminating test is to measure β from the *environment* and check that the model exponent moves with it (§7).
7. **"Decision theory in a lab coat": the objection mostly survives above the cell, and I say so plainly.**
   - kT ln2 per bit does not bind anywhere above the cell. Synapses spend about 10⁴ ATP per bit, roughly 10⁵ × Landauer (Laughlin et al. 1998, KNOWN).
   - The exponents in item 5 come from information theory plus network physics (WBE/Bettencourt transport dissipation fixes Q(M) or Q(N)). They do not come from the second law of thermodynamics itself.
   - What *does* hold at every scale is one inequality, KNOWN in pieces: **growth ≤ disequilibrium + information − house take**. It covers:
     - Szilard engines (W ≤ kT[D(p‖p_eq) + I]: Esposito & Van den Broeck 2011; Sagawa & Ueda 2009);
     - Kelly bettors and investors (G = D(p‖r̃) − ln(1 + v) + I; the isomorphism is in Vinkler et al. 2016);
     - evolution (information accumulation is bounded by the substitutional load, the Haldane cost: Kimura 1961).
   - In markets, no-arbitrage plays the role of the second law. Its consequence is a theorem (PROOF, checked): **in an efficient environment (D → 0) blind persistence is impossible**, so persistence *requires* I > ln(1 + v).
   - That is a real "second-law-shaped" constraint above the cell. It concerns competition, not heat.

**Net: what survives the new prior art?**
1. The quantitative structural internal-model theorem (I3). Modest.
2. The spectrum→exponent scaling law with its regime split, its non-viability result and its minimum-size result (§4–5). This is the only genuinely *cross-scale, testable* claim. Its ingredients are KNOWN, but I did not find the assembly as an organizational scaling law (UNCONFIRMED).
3. Everything else is KNOWN, packaging, or FAILS. I say so where it applies.

---

## 1. Setup

- **World.** X = (X_t) is stationary and ergodic over a finite alphabet. The causal state S_t = ε(X_{≤t}) is the class of pasts with the same conditional future law (Shalizi & Crutchfield 2001, J. Stat. Phys. 104:817, KNOWN). S_t takes values in a finite set **S**. The ε-machine is unifilar: S_{t+1} = T(S_t, X_{t+1}).
- **Agent.** The agent's memory is M_t = f(M_{t−1}, X_t), plus optional private noise independent of the future given the past. So M_t is a (randomised) function of the past, and Fut − Past − M is a Markov chain.
- **Per-period income** is y − c(M_t) − w·ℓ_t:
  - ℓ_t is the log-loss of the agent's forecast of the next L symbols;
  - w is the stakes;
  - the bit cost is c̄ = c₀ + κ·I_mem, where I_mem is the information the memory holds.
- **Margin.** Persistence, in the sense of Theorem P in GENERAL_THEOREM.md, requires non-negative long-run mean income. Define the *solvency margin with a perfect model* as m := y − c₀ − w·H(X_{1:L} | S).
- **Notation.** F_s := P(X_{1:L} = · | S = s), and γ_L := min_{s≠s′} TV(F_s, F_{s′}).
  - γ_L > 0 for some finite L whenever **S** is finite, because distinct causal states differ on some finite word and there are finitely many pairs.

## 2. Theorems

**I1 (miss = excess loss) [PROOF].**
- Statement: for any forecaster q(·|M), E[−log q(X_{1:L}|M)] − H(X_{1:L}|S) ≥ δ := I(S; X_{1:L} | M), with equality iff q = P(·|M).
- Also, δ = I(Past; Fut_L) − I(M; Fut_L). In words, the miss is exactly the predictive information the memory fails to carry.
- Proof:
  1. E[−log q] ≥ H(Fut|M) (Gibbs).
  2. Expand H(Fut|M) = H(Fut|S, M) + I(S; Fut|M).
  3. H(Fut|S, M) = H(Fut|S), because S screens the past from the future and M is a function of the past.
  4. The second identity follows because S is sufficient: I(S; Fut) = I(Past; Fut).
- Check: i1 computes δ and the realised excess loss independently, for 2 + 2 + 10 machines and many k. They agree to 1e-9.

**Solvency corollary [PROOF].** Persistence ⇒ wδ + κI_mem ≤ m ⇒ **δ ≤ (m − κ·I_mem)/w**.
- Equivalently, **viability ⇔ min_R [κR + w(E_L − IB_L(R))] ≤ m**, where IB_L(R) := max{I(M; Fut_L) : I(M; Past) ≤ R} is the predictive information-bottleneck curve and E_L = I(Past; Fut_L).
- In words: the agent persists iff the predictive-IB curve dips below the solvency line.
- Related KNOWN results:
  - optimal causal filtering recovers the causal states as the trade-off parameter goes to 0 (Still, Crutchfield & Ellison 2010, Chaos 20:037111);
  - predictive rate-distortion via causal states (Marzen & Crutchfield 2016, J. Stat. Phys. 163:1312);
  - minimum relevant information for a persistence utility (Polani, Nehaniv, Martinetz & Kim 2006, ALife X; fetched by the reviewer, not by me);
  - the general value-of-information function (Stratonovich 1965).
- **Novelty of this corollary: packaging.** The new content is only the solvency line.

**I2 (exact stochastic internal-model principle) [PROOF; KNOWN at δ = 0].**
- Statement: if δ = 0 and γ_L > 0, then S = g(M) a.s. for a measurable g, and g(f(m, x)) = T(g(m), x) a.s. In words, the agent's dynamics map homomorphically onto the ε-machine.
- The first half is Shalizi & Crutchfield's Theorem 2: any prescient rival refines the causal states. The homomorphism follows from unifilarity.
- Check: the golden-mean process with a k = 1 agent has δ = 0, decoding error 0 and homomorphism violations 0 (i1).

**I3 (quantitative internal model) [PROOF; UNCONFIRMED novelty].**
- Statement, with g(m) := argmin_s TV(F_s, q_m) and q_m := Σ_s P(s|m)F_s:
  - P(g(M) ≠ S) ≤ √(2δ)/γ_L (δ in nats);
  - P(g(M_{t+1}) ≠ T(g(M_t), X_{t+1})) ≤ 2√(2δ)/γ_L.
- With solvency: **P(model ≠ world's causal state) ≤ √(2(m − κI_mem)/w) / γ_L.**
- Proof:
  1. δ = E_M Σ_s P(s|M)·KL(F_s ‖ q_M).
  2. If s ≠ g(m), the triangle inequality and the choice of g give TV(F_s, q_m) ≥ γ/2.
  3. Markov's inequality, Pinsker's inequality and Jensen's inequality give P(g ≠ S) ≤ (2/γ)·E√(KL/2) ≤ √(2δ)/γ.
  4. For the homomorphism: S_{t+1} = T(S_t, X_{t+1}), so a violation requires a decoding error at t or at t + 1. A union bound gives the factor 2.
- How it differs from the closest prior results:
  - Approximate information states (Subramanian et al. 2022, JMLR 23(12)) prove the *converse*: an approximately sufficient state ⇒ near-optimal control.
  - The data-rate theorems give *rates*.
  - Boyd, Mandal & Crutchfield 2017 (J. Stat. Phys. 167:1555) show that a thermodynamic ratchet's memory must reflect the source's memory to harvest optimally. That is the closest structural prior art, but it is qualitative and thermodynamic.
- **Tightness (from the numerics).** The bound holds in every case (i1: Even, golden mean, 10 random 4-state machines, k = 0…10). It is loose:
  - Even process, k = 10: δ = 0.0215 b, true error 0.0104, bound 0.23;
  - random machine "rand3", k = 8: δ = 0.0092 b, error 0.021, bound 0.54.
- **CONJECTURE:** under a Hellinger-type separation, P(g ≠ S) = O(δ/γ²).

**I4 (memory floor; Fano) [PROOF, standard].** I(M; S) ≥ H(S) − h(P_e) − P_e·log(|**S**| − 1).
- Combined with I3, a solvent agent needs I_mem ≥ C_μ − O(√δ log(1/δ)).
- If κ·C_μ > m, the agent cannot afford the full model and must coarse-grain. How much it loses is then given by the IB curve of I1.
- Check: Fano holds in every case in i1.

**I5 (upkeep is a flow) [PROOF, elementary; Gaussian case KNOWN].**
- Assume an exogenous world: M_{t−1} − S_{t−1} − S_t is a Markov chain.
- Then I(M_t; S_t) ≤ I(M_{t−1}; S_t) + I(Y_t; S_t | M_{t−1}) ≤ η·I(M_{t−1}; S_{t−1}) + I_obs.
- So in steady state **I_obs ≥ (1 − η)·I(M; S)**.
- For a binary world flipping with probability q, η_KL = (1 − 2q)² (Polyanskiy & Wu, arXiv:1508.06025, KNOWN), so I_obs ≥ 4q(1 − q)·I.
- Check: i2 tests 400 random stochastic finite-state agents (2–5 states), BSC observations and random q. The minimum slack is +6.1e-3 bits, with no violations.
- **Gaussian caveat (found while checking).** The unconstrained Gaussian kernel has input-free η_KL = 1, so "η = a²" is **wrong** as a general SDPI constant. The correct statement is the jointly-Gaussian contraction ρ² → a²ρ², so decay = I − I′ with I′ = −½log₂(1 − a²(1 − 2^(−2I))).
- The Kalman filter meets this **with equality**: inflow equals decay to 1e-12 in four cases (i2). This is consistent with Mitter & Newton 2005 (J. Stat. Phys. 118:145) and Horowitz & Sandberg 2014 (NJP 16:125007), both KNOWN: information flow equals the decay, and heat ≥ kT × flow.
- **Precision ceiling [PROOF].** Since I′ ≤ ½log₂(1/(1 − a²)), an inflow of r bits/step supports at most I ≤ r + ½log₂(1/(1 − a²)). Every bit of precision beyond the world's own predictability costs one bit per step, indefinitely.
- **Physical floor (KNOWN).** Measurement plus erasure costs W ≥ kT·I (Sagawa & Ueda 2009, PRL 102:250602; erratum PRL 106:189901). So upkeep power ≥ kT ln2 × (bits/step).

## 3. Counterexamples and exact conditions (FAILS list)

| # | Condition broken | What happens | Status |
|---|---|---|---|
| F1 | Loss not strictly proper (e.g. Hamming) | Even process: P(1\|A) = ½, P(1\|B) = 1, so "always 1" is Bayes-optimal in both states. A memoryless agent has zero excess risk and I(M;S) = 0. Only the **decision-relevant partition** of causal states (states sharing a Bayes act) is forced, with error ≤ excess/Δ_min, where Δ_min is the smallest regret gap (Markov's inequality). | FAILS for the general claim; PROOF for the coarse version |
| F2 | γ_L = 0 at the horizon used | States that are indistinguishable over L steps are not forced apart. Longer horizons restore the result. | FAILS (exact condition) |
| F3 | Nonunifilar world (infinitely many causal states) | Simple nonunifilar source: δ_k = 0.146, 0.0136, 0.0029, …, 4e-6 bits at k = 0, 1, 2, …, 8. It is positive for every finite k, so no finite agent is exact. Only the approximate I3 applies, with the γ of a finite coarse-graining. | FAILS for exactness |
| F4 | Window agents on infinite-order, finite-state worlds | Even process: δ_k halves about every 2 symbols and never reaches 0, while the 2-state ε-machine is exact. | FAILS for "longer memory ⇒ sufficient" |
| F5 | Agent's actions affect the world | The causal states of the closed loop depend on the policy. CONJECTURE: the theorem carries over to input-output (transducer) causal states. I did not fetch that literature, so I cite nothing. | CONJECTURE |
| F6 | i.i.d. world | \|**S**\| = 1, so the model is trivial. Consistent with P1 (a model is necessary iff blind action is not viable). | consistent |
| F7 | Non-stationary world | Causal states are undefined. Use I5/§4 (rate theorems) instead. | handled in §4 |
| F8 | Bet-hedging population | The *individuals* are blind; the "model" is the population's phenotype distribution. Sensing beats switching when the environment changes fast and sensing is cheap (Kussell & Leibler 2005, Science 309:2075, KNOWN). The theorem applies to the population as the agent. | consistent, with the agent redefined |

## 4. Non-stationary and unstable worlds (the data-rate route, as the reviewer asked)

**KNOWN (Nair & Evans 2004, SIAM J. Control Optim. 43:413; Tatikonda & Mitter 2004, IEEE TAC 49:1056).**
- Mean-square stabilising or tracking x′ = Ax + w needs a rate above Σ_{|λ_i|≥1} log₂|λ_i|.
- In the scalar Gaussian case, holding a one-step error variance P needs **R ≥ log₂|a| + ½log₂(1 + q/(a²P))**. Equivalently, P ≥ q/(4^R − a²).
- Checks (i4):
  - Real R-bit quantizers always sit above the bound. For a = 1, R = 2 the error is 0.50 against a bound of 0.067; practical quantizers are far from tight.
  - Noise-free zoom quantizers converge iff R > log₂a:
    - a = 3, R = 1: diverges;
    - a = 3, R = 2: converges;
    - a = 1.5, R = 1: converges.

**Random-walk world with many modes [PROOF; UNCONFIRMED novelty as an organizational result].**
- Setup: modes drift with per-step variances q_i ∝ i^(−β). Per-step cost is w·ΣP_i + κ·Σ½log₂(1 + q_i/P_i).
- Per-mode optimum: P_i² + q_iP_i − q_iθ = 0, with θ = κ/(2 ln2 · w).
- Two regimes:
  - fast modes (q ≫ θ): P ≈ θ, and the rate is logarithmic;
  - slow modes (q ≪ θ): P ≈ √(qθ), and the rate ≈ √(q/θ)/(2 ln2). This is **the square-root/EOQ law** (the T1/O1 regime, KNOWN per the review).
- Summing over modes:
  - β > 2: total rate ∝ (w/κ)^(1/β);
  - β ≤ 2: the slow tail Σ√q_i diverges, so the rate ∝ (w/κ)^(1/2)·N^(1−β/2), dominated by the many slow modes and growing with the number of modes N.
- Check: i4 finds late exponents 0.494, 0.489, 0.462, 0.390 and 0.334 for β = 0.8, 1, 1.5, 2.5 and 3. Theory gives 0.5, 0.5, 0.5, 0.4 and 0.333.
- **New FAILS / condition:** with unbounded per-mode loss and infinitely many random-walk modes, **β ≤ 2 is non-viable at any finite rate**. A persistent agent in such a world must have *bounded* loss per ignored mode, i.e. a fallback; this links to Theorem G's bounded-fallback cliff. Or the world must have β > 2.

**Survival tax and minimum viable size [PROOF given the model].**
- Unstable modes add a rate floor F = Σ log₂|a_i| that does not depend on the stakes (Nair–Evans).
- With income margin μ per unit throughput, viability needs μQ ≥ κF + …, so **Q_min = κF/μ**.
- The information share of throughput, share(Q) = κ(F + c(Q/κ)^(1/β))/Q, has an **interior minimum iff β < 1**, at Q* = κ[Fβ/(c(1 − β))]^β (i4: numeric 7.28 against theory 7.17).
- For β ≥ 1 the share falls monotonically: economies of scale in "cognition".
- CONJECTURE (empirical): environments with steeper spectra or more instability set larger minimum viable sizes.

## 5. Stationary scaling law and the spectral bridge

- **Reverse water-filling [PROOF; the tool is KNOWN].**
  - With λ_i = i^(−β), the water level is θ = κ/(2 ln2 · w) and n* = θ^(−1/β).
  - Bits ≈ (β/(2 ln2))·n* ∝ (w/κ)^(1/β), and spend ∝ κ^(1−1/β)w^(1/β).
  - Check (i3, N = 10⁶): fitted exponents 2.004, 1.115, 1.002, 0.667 and 0.500 for β = 0.5, 0.9, 1, 1.5 and 2 (theory 1/β). The ratio bits/n* matches β/(2 ln2) to 3 digits.
  - A finite flat world (n modes) grows only *logarithmically*, by 16.61 bits per decade at n = 20. So power laws need a power-law world.
- **Spectral bridge [PROOF].** A field with power spectrum k^(−α) in d dimensions has rank-ordered mode variances ∝ i^(−α/d), so β = α/d.
  - Check (i3): fitted 0.904, 0.999, 0.999 and 1.998 against theory 0.905, 1, 1 and 2.
  - Natural images have α = 1.81 ± 0.01 in d = 2 (Ruderman & Bialek 1994, PRL 73:814, KNOWN), so β_vision = 0.905 and the predicted exponent is 1.10.
  - 1/f temporal noise gives β = 1 and exponent 1.
- **Chain to body size (CONJECTURE: stakes ∝ throughput, assumption A-w).**
  - WBE's dissipation-minimising networks give Q ∝ M^(3/4) (West, Brown & Enquist 1997, Science 276:122, KNOWN).
  - So model ∝ M^(3/(4β)): M^0.75 at β = 1 and M^0.83 at β = 0.905.
  - Bettencourt 2013 (Science 340:1438, KNOWN) derives the city output exponent 1 + δ, with δ = 1/6, from interaction versus transport costs.

## 6. Data that bear on it (fetched sources only)

| System | Throughput Q | "Model" proxy | Observed | Implied β (stationary reading) | Source (fetched) |
|---|---|---|---|---|---|
| Mammal brains | BMR ∝ M^0.75 | brain mass ∝ M^0.75 | model ∝ Q^1.0 | 1.00 | Martin 1981, Nature 293:57 |
| Mammal brains | BMR | brain energy ∝ V_brain^0.86, so ∝ M^0.645; neurons ∝ brain energy (per-neuron glucose ~constant) | model ∝ Q^0.86 | 1.16 | Karbowski 2007, BMC Biol 5:18; Herculano-Houzel 2011, PLoS One |
| US cities | GDP ∝ N^1.13–1.26 | city administrative staff ∝ N^~1.2 | admin ∝ GDP^0.95–1.06 | 0.94–1.05 | Bettencourt et al. 2007, PNAS 104:7301 (Table 1); Hutcheson & Prather 1979, Urban Aff. Q. 15(2), doi 10.1177/107808747901500203 (**abstract-level only; the DOI fetch timed out**) |
| Firms | sales ∝ assets^0.90; employees ∝ assets^0.74 (US) | administrative ratio falls with size (Blau) | admin sublinear in sales | > 1, or the drift regime (exponent 1/2) | Zhang, Kempes, Hamilton, Tao & West, arXiv:2109.10379; Blau 1970, ASR 35:201, doi 10.2307/2093199 |
| Bacteria | metabolism ∝ M^1.7 (prokaryotes), attributed to more genes | transcription regulators ∝ genes² | not mapped cleanly | n/a | DeLong et al. 2010, PNAS 107:12941; van Nimwegen 2003, Trends Genet. |
| Retina | n/a | operates near the predictive-IB bound (up to 98%) | evidence that the I1 viability curve is *used* by biology | n/a | Palmer, Marre, Berry & Bialek 2015, PNAS 112:6908 |
| E. coli | n/a | gradient-climbing speed limited by information rate (~65% of max) | a real cell sits on an information bound | n/a | Mattingly, Kamino, Machta & Emonet 2021, Nat. Phys. |

**Honest reading.**
- Every exponent is within about 15% of the β ≈ 1 stationary prediction.
- So is the null "a fixed share of the budget goes to the model". **These data cannot distinguish the theory from the null.**
- The firm row conflicts with stationary β ≤ 1 unless firms are in the drift (EOQ) regime. That is itself a prediction: administration ∝ (throughput)^½ in fast-drifting industries.
- I found **no** dataset of firm IT/admin spend against revenue with a fitted exponent from a fetched source. Nothing is claimed for that row.

## 7. The testable cross-scale prediction (CONJECTURE, falsifiable)

**Model exponent = 1/β (mean-reverting environment) or min(½, 1/β) (drifting environment), where β is measured from the environment's own variance spectrum. The share of throughput spent on the model has an interior minimum iff β < 1.**

How it could fail:
1. Measure β, for example from PCA of demand shocks across a firm's product lines, of a city's service-demand variability, or of a species' sensory environment.
2. Check that the model exponent tracks 1/β *across* environments.
3. A constant exponent near 1 regardless of β falsifies the theory and favours the budget-share null.
4. Retina and vision give one anchor: β = 0.905 predicts 1.10.

## 8. The "decision theory in a lab coat" objection: verdict

| Claim | Does the second law do the work? | Status |
|---|---|---|
| kT ln2 per bit sets the size of organizational models | **No.** Real costs are ≥ 10⁵ × Landauer at synapses (10⁴ ATP/bit; 10⁶–10⁷ for graded or spiking signals; Laughlin et al. 1998, Nat. Neurosci. 1:36). Firms are far higher still. | FAILS as literal physics above the cell |
| Upkeep is a flow, not a stock | Partly. The *flow* form is information theory (SDPI, data-rate); the second law *prices* it at ≥ kT per nat. | PROOF + KNOWN |
| Throughput exponents Q(M), Q(N) | Yes, via transport dissipation (WBE; Bettencourt). | KNOWN |
| Growth ≤ disequilibrium + information − take | Same inequality for Szilard (Esposito & Van den Broeck 2011, EPL 95:40004; Sagawa & Ueda 2009), Kelly (Vinkler et al. 2016) and selection (Kimura 1961, Genet. Res. 2:127: ~0.29 bits/generation at load 0.2). No-arbitrage is the market's "second law". | KNOWN (isomorphism) |
| Efficient environment ⇒ blind persistence impossible, so persistence needs I > ln(1 + v) | Follows from the identity above. Check (i3): blind growth −0.154 and −0.086 in near-efficient markets; MC with side information matches D − ln(1 + v) + I to < 0.015. The value of information is linear, so the choice is bang-bang at κ = 1 nat/nat. | PROOF (assembly; UNCONFIRMED novelty) |

**Verdict.**
- Above the cell, the thermodynamic second law constrains the *currency* (a floor on κ) and the *throughput* (via networks), but not the *exponents*.
- The one law that is truly the same at every scale is the growth/disequilibrium/information inequality. It is a known isomorphism.
- The objection is answered only in that weak sense. I am not claiming more.

## 9. Prior art across fields (all fetched)

**Economics and organizations**
- Hayek 1945 (AER 35:519): prices as compressed information.
- Mount & Reiter 1974 (JET 8:161): minimal message-space dimension for Walrasian outcomes.
- Jordan 1982 (JET 28:1): the competitive mechanism is *uniquely* informationally efficient. This is the economic analogue of I2: a minimal sufficient statistic, forced and unique.
- Galbraith 1974 (Interfaces 4(3):28): information-processing capacity matched to task uncertainty.
- Garicano 2000 (JPE 108:874): knowledge hierarchies.
- Blau 1970.

**Biology**
- Palmer et al. 2015; Mattingly et al. 2021; Kussell & Leibler 2005.
- Mayer, Balasubramanian, Mora & Walczak 2015 (PNAS 112:5950): optimal immune repertoires over-represent rare antigens. That is *not* the water-filling pattern, so the allocation law differs; noted as a tension.
- Laughlin et al. 1998; Kimura 1961.

**Physics and information theory**
- Shalizi & Crutchfield 2001; Still et al. 2010; Marzen & Crutchfield 2016; Boyd et al. 2017.
- Sagawa & Ueda 2009; Esposito & Van den Broeck 2011; Mitter & Newton 2005; Horowitz & Sandberg 2014.
- Littman, Sutton & Singh 2002 (PSRs); Subramanian et al. 2022 (AIS); Polyanskiy & Wu.

**Control:** Nair & Evans 2004; Tatikonda & Mitter 2004.

**Scaling:** WBE 1997; Bettencourt et al. 2007; Bettencourt 2013; Zhang et al. (arXiv:2109.10379); Martin 1981; Karbowski 2007; Herculano-Houzel 2011; DeLong et al. 2010; Ruderman & Bialek 1994.

Cited via the reviewer's fetch only, not re-fetched by me: Stratonovich 1965 and Polani et al. 2006. Page numbers for Palmer et al. (6908), Mayer et al. (5950), Kussell & Leibler (2075) and Blau (35:201) are from memory: titles and DOIs were fetched, the page numbers were not. Verify them before any public use.

## 10. Red team

1. **I3 is elementary**, Pinsker plus a union bound, so it is likely known in some form. Its √ is loose by an order of magnitude in practice.
2. **The scaling law rests on assumption A-w (stakes ∝ throughput)** and on a single price per bit. Mixed currencies break it, as Theorem S showed.
3. **β is not yet measured for any organization.** Without that, §6 is curve-matching against a null that predicts the same thing.
4. **The city row rests on an abstract-level reading of a 1979 study.** The full text was not fetched.
5. **Brain mass and brain energy give different exponents (1.0 vs 0.86).** Which one is the "model size" is a choice, and that choice moves the implied β by 16%.
6. **The random-walk regime gives exponent ½ for most β.** If real organizations live there, the clean 1/β law is the exception. Which regime applies is decided by mean-reversion time against model refresh time, an extra parameter.
7. **The data-rate floors assume linear dynamics.** For nonlinear worlds the analogue is topological or metric entropy. It is plausible but not checked here.
8. **Self-checks only.** An independent, blind grader should rerun `checks/i1–i4` and audit §2–4.

## Files
- `checks/i1_internal_model.py/.out`: I1–I4, F1, F3, F4 (exact enumeration).
- `checks/i2_maintenance_sdpi.py/.out`: I5, the Kalman equality, the Gaussian η correction.
- `checks/i3_throughput_scaling.py/.out`: water-filling exponents, spectral bridge, data chain, Kelly with overround.
- `checks/i4_nonstationary_datarate.py/.out`: data-rate floor against real quantizers, random-walk regime split, survival tax and share minimum.
