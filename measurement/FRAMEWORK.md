# MEASUREMENT FRAMEWORK: how A Theory of Adaptive Organization's quantities are measured, and what counts as a fair refutation

Sunday 15 November 2026, written about 08:10–08:20 AM ET (America/New_York) by a Grok Bot executor for Chad Mitchell, via Ace. Nothing was posted or sent by that work. This document sits on top of `reviews/night1/formal/AXIOMS.md` (the model class 𝓜 and its notation, used unchanged) and `reviews/night1/CLAIM_MAP_FINAL.md`. Its companion is `CLAIM_MAP_v2.md`.

**Why this exists.** Chad (t1908): the theory never said how its quantities are measured, so every field "kill" and "hit" so far tested a proxy whose validity nobody had checked. That is correct, and it is the single largest methodological gap in the project. This file builds the missing layer:
1. An operational definition, procedure, validity checks and failure modes for every core quantity, at every scale (§3).
2. A re-audit of every past field test: what it actually measured, where validity fails, and the honest relabel (§4).
3. The systems where all quantities can be measured validly, ranked by feasibility with public data (§5).
4. A fair refutation specification for each main prediction (§6), and the three decisive tests to run next (§7).

**Wording rule (Chad's, kept throughout).** GTAO is a general causal theory of adaptive organization, with the same three costs (memory/upkeep, prediction error, and reads) at every level. Only its hypothesis sentence (THEORY §3, "The law of adaptive organization (hypothesis)") carries the word; nothing else is called a law, and it is never called a theory of everything. *Scope (updated 18 Nov 2026, Chad t1927):* the costs apply from atoms to the cosmos; design predictions apply where selection makes a model pay (THEORY §2.3, `theory/SCALE_ENDS.md`; §1.2 item 4 below). *Process vocabulary (24 Nov 2026, `process/PROCESS.md`, `process/MISS_LOG_TEMPLATE.md`):* prediction errors are logged as misses (prediction ID, outcome, signed size, location, update scaled to stake × information) rather than `'puzzle'` or `'kill'`; irreversible rule violations (editing locked preregs, post-hoc patching) are breaches; say cost (not `'bill'`), and never claim open problems are `'solved'`.

**Citation markers.** Markers carried over from the night-1 reviews keep their meanings: [FULL], [ABS], [OCR], [SEC], [BIB], [DOI], [UNVERIFIED]. New in this file:
- **[DATA-VERIFIED 15 Nov]**: I confirmed this session that the named public dataset exists at the named location (landing page or search summary). I did **not** download or inspect it unless stated.
- **[ON BOX]**: already downloaded by a project test; a path is given.
- **[DERIVED HERE]**: an elementary derivation made in this file and checked numerically in `checks/`. It has not been independently reviewed.
- **[PROPOSAL]**: a measurement design. No data have been pulled for it.

No citation or dataset in this file was invented. If a source is named without a marker, it is from the project's own earlier files, with the marker given there.

---

## 1. The logic of the problem, and where I agree and disagree with Chad

### 1.1 Every field test was a test of a conjunction
A field prediction is never "GTAO says X". It is **T ∧ M ∧ A ⇒ X**, where:
- **T** is the theory: the in-model theorems in `reviews/night1/formal/THEOREMS.md`. These are mostly correct, after the math review's corrections.
- **M** is the measurement mapping. It says which observable stands for which model quantity: target, pool, level, drift, effort, stakes, price.
- **A** is the set of auxiliary assumptions: the sensing class (often class R with a = b = ½), Brownian drift (H = ½), zero upkeep, κ = 0 (see §3.9), strong selection, and the right comparator.

A failed X refutes the conjunction. It moves blame to T only if M and A were independently validated. **In no field test so far were M or A validated before the test.** So Chad is right: no field result licenses "GTAO is killed". By the same logic, no field pass licenses "GTAO is supported". The measles pass loses its standing for exactly the same reason the Enron kill does (§4).

### 1.2 Where I push back
Chad asked me to push back where I disagree. I disagree on four points.
1. **Not every "kill" was a field kill.** Some night-1 kills are proofs. "V ≥ 2 at onset for every upkeep and price" is false as mathematics (math review, Issue 1). The general mixed-technology sign claim (B10) is refuted by a counterexample. The ADM 2008 citation is a miscitation. These stay dead. In v2 they are labeled **MATH-CORRECTED** or **WITHDRAWN**, and each has a correct replacement. Locked simulation failures (SENSING2 EVO_A; ANTS1 P3-MODE, P5(c), P6; LAYERS1 P2) are also not proxy problems. They are failures of predictions about the authors' own simulators, and they keep the label **SIM-FAIL**.
2. **A proxy fail still carries information.** It kills the specific mapping-plus-auxiliaries that was tested, and that narrows where the theory can live. Example: Enron plus PIAAC rule out "raw external reading rate rises as √span". That rules out κ ≈ 0 under class R in those settings, *if* those channels carried the sampling (§3.9, §4.4). The fair statement is "failed on proxy X", not "no information".
3. **The relabel is only honest if it cuts both ways and is locked before data.** The physics referee's Issue 5 was that GTAO shields itself through "the mapping might be wrong" plus "selection might be weak". This file is the cure only if:
   - the validity gates in §2 are fixed **now**, before any new data;
   - a test that passes the gates counts **fully**, as a pass or a refutation, with no later appeal to "the measure missed it".

   Otherwise relabeling every failure as a proxy failure is exactly the unfalsifiability the free-energy principle has been criticised for (Aguilera et al. 2022 [DOI]; Bruineberg et al. 2022 [DOI]).
4. **"From atoms to cities."** The cost accounting, including physical floors on what a read or a stored bit costs, applies from atoms up. The *design predictions* (onset, vigilance, freeze/hold/lookup) need Axiom 7, a process that selects cheaper designs. An atom or a crystal has physics but no selection over tracking designs. So I would state the scope as: **physical floors at every scale; design predictions wherever there is selection, from cells (and arguably self-replicating chemistry) upward.** This is a scope disagreement worth Chad's call, not a correction. *Resolved 18 Nov 2026 (Chad, t1927):* the costs apply from atoms to the cosmos. `theory/SCALE_ENDS.md` (independently refereed, PASS-WITH-FIXES; THEORY v1.4.18 §2.3; CLAIM_MAP N25–N29) shows the two readings agree: the costs are physically priced at every scale, and what vanishes where nothing selects is the value of a model (N25, PROVED in-model, partly definitional under Axiom 7).

### 1.3 Where I think Chad is more right than the night-1 map
- **"Killed" was the wrong word for P1, Enron, LANG1, the τ tests and inventory buffering.** In every case at least one gate in §2 fails. The v2 map relabels them all as **PROXY-FAIL**.
- **Physics (Chad: it applies at every level but constrains less at firm scale).** That is a measurable claim, not a decorative one, once it is written as a ratio (§3.11). The *binding ratio* β_phys is the actual cost of a read or held bit divided by its thermodynamic floor. It is near 1 where physics constrains design, which plausibly means some cellular sensing, and ≫ 1 where it does not (firms). Measuring β_phys per scale is what turns "physics applies at every level" into content. The night-1 referee's point survives only in this narrower form: **no theorem in 𝓜 currently uses a physical floor.** So the physics is not decorative in the theory's scope. It is idle in its current proofs, and it constrains designs only where β_phys is near 1.
- **Variational free energy = thermodynamic free energy only as a special case.** Agreed. The two coincide numerically when the system's physical energy function equals −kT ln of its generative model (energy ↔ surprisal at temperature T). That is a special identification, not a general identity [DERIVED HERE as a definitional observation; no source verified this session]. The v2 map labels the general identity **WITHDRAWN** and the special case **OPEN** (it needs a system where both sides are measured).
- **The title stays.** Chad's call. The v2 map records it as decided, with Dessein & Santos 2006 cited prominently.

### 1.4 What the theory's empirical content actually is
The physics referee's Issue 3 is right and important for measurement. GTAO's exponents are not universal numbers. They are functions of the sensing class (a, b). So GTAO's empirical content is a set of **relations between independently measured quantities**:
- onset exponent ↔ the level's effort elasticities;
- vigilance ↔ the shared share ρ;
- raw rank gradient of sampling ↔ the sharing-decay exponent κ;
- freeze/hold/lookup edges ↔ drift, use rate and lookup cost.

A valid test therefore needs **at least two quantities measured independently in the same system**. Comparing one proxy against a constant computed under assumed auxiliaries (−1, 2, √, 0.5) is a test of the auxiliaries. Every past field test had this structure. That is the deepest reason they cannot count as kills of T.

---

## 2. General measurement rules (fixed now, before any new data)

### 2.1 The measurement triple: nothing is measurable until three things are named
Every GTAO quantity is defined **relative to** three things:
1. **Target** x_i. This is the decision-relevant quantity member i must track, named *before* data. "Information in general" or "the environment" is not a target.
2. **Pool**. This is the set of members whose targets load on a shared source s (x_i = Σ B_im s_m + u_i). "Shared" and "private" are relative to the pool (Chad, t1901): the CEO's pool is the firm, and a team lead's pool is the team.
3. **Channel set**. This is every channel through which the tracker can buy information about the target: reads, queries, meetings, calls, messages, sensors, receptors, antennation.

A test that leaves any of the three implicit fails gate MV1 below.

### 2.2 Validity gates (MV1–MV10)
**Treated as binding from 18 November 2026, on Chad's instruction to proceed without his sign-off (t1927; CLAIM_MAP M2 and v2.40 note):** every prereg locked from then on must state its tier against these gates before data. MV9's external timestamp still needs Chad's go per lock.

A field test is **decisive (Tier 1)** only if it passes every gate. It is **Tier 2** if it passes MV1–MV4 and MV8 but not all the rest. It is **Tier 3** otherwise. The tiers extend those in `prereg/vigil-ona/FAIR_MEASURE.md` from vigilance to every prediction.

| Gate | Requirement | What it rules out |
|---|---|---|
| **MV1 Triple named** | Target, pool and channel set fixed in writing before data | "Any external contact", "information work in general" |
| **MV2 Construct match** | The observable is the model quantity, not a correlate. **Effort means the tracker's chosen sampling of the named target** (not receipt, not role assignment). **Drift means the variance rate of the target's own increments** (not event frequency or "need"). **A level means a tracker whose estimate is demonstrably consumed by ≥ 2 members** (not a title) | Received mail (Enron); headline-word recurrence standing in for an item's need (P1); town presence standing in for antigenic drift (measles); titles standing in for levels |
| **MV3 Independent measurement of inputs** | Every input a prediction needs (ρ, q, (a, b), h, κ, N) is measured *in the same system*, by a procedure that does not use the outcome | Constants imported from theory under assumed class R, H = ½, h = 0, κ = 0 |
| **MV4 Comparator correct** | The comparator matches the theorem. **V needs a flat comparator** (an unlevelled unit, or the same unit before the level), not the level's own members (math Issue 10). Onset needs groups both below and above N\* | Leads compared with their own nested members |
| **MV5 Convergent validity** | At least two independent methods agree on each key input, within a stated tolerance (e.g. \|Δ ln\| < 0.3) | Single-proxy inputs |
| **MV6 Discriminant validity** | Pre-declared rival drivers of the same observable are controlled or contrasted: status, generic activity volume, function, the generic OU-with-barrier baseline, and heterogeneity | Generic "seniors do more of everything" (PIAAC P2), status-driven advice flows |
| **MV7 Known-groups check** | The instrument reproduces a value known in advance in at least one calibration case (§3, per quantity) | Instruments that cannot see the effect even where it is known to exist |
| **MV8 Power / resolution** | (i) Statistical: the SE of the key estimate is ≤ \|Δ\|/2.8, where Δ is the gap between GTAO's value and the nearest named rival (80% power, two-sided α = 0.05). (ii) **Selection** (Prop 10): the prize at the observed operating point exceeds the measured design resolution ε̂ (§3.10). Settings outside the selection gate are not analysed | Underpowered nulls; the small-ρ regime that POOLSIM showed is invisible under ≥ 1% decision noise |
| **MV9 Process** | Externally timestamped lock (needs Chad's go), code hashed, estimator dry-run on synthetic truth with floors and ceilings, raw data kept, analyst blind to outcome where possible | Everything in night-1 §4 lock integrity |
| **MV10 Feasibility / power gate (at lock)** | Before lock, every causal-form or optimality-form prereg, and every known-groups, moot or equivalence bound, states π (default 0.8) and shows on its own planned data (planned n, span and input changes; σ = sd of the same contrast over comparable no-change periods, measured before lock, with its df), by `tools/power_gate.py` or a simulation of the locked decision code: P(PASS \| locked prediction true) ≥ π; P(FAIL \| the null its FAIL rule targets) ≥ π; each rule fires at its own best-case data; any PASS band is wider than its CI half-width. Minimal form: \|b\|·S ≥ (z₁₋α/₂ + z_π)·σ / min(1, κ), S = √(Σ Δlog x_k²) over independent contrasts, κ = share of the predicted move the FAIL rule must exclude (for a causal-form test, THEORY §1 N6's κ_F: 0 < κ ≤ ½, the predicted move b·S scaled by the design's measured adjustment share and input reliability, their errors propagated into the decision; `tools/power_gate.py` defaults to κ = ½ and fails a gate outside that range; v1.4.7, `reviews/night2/CAUSAL_KILL_MAGNITUDE_REVIEW.md`; a causal-form PASS needs D − zσ above the same κ·b·S, so with the scaled prediction known P(PASS \| true) = Φ((1 − κ)·SNR − z) and the minimal gate is unchanged for κ ≤ ½; with the adjustment share's or reliability's error propagated the PASS leg can bind, so the simulation route checks P(PASS \| true) ≥ π too, THEORY v1.4.17, `reviews/night2/CAUSAL_KAPPA_LENIENCY.md`, `reviews/night2/CAUSAL_KAPPA_LENIENCY_REVIEW.md`); an absolute FAIL margin ε needs σ ≤ ε/(z₁₋α/₂ + z_π) whatever S; optimality form: gap to the nearest rival Δ ≥ 2.80σ. **Discrimination line (v1.4.16, THEORY §1 N6; proposed in `reviews/night2/PREREG_LOSS_LOCK.md`):** a prereg that reports its test as telling the locked optimum from a named rival optimum computes the rival's predicted move for the same loss (§3.3) and a named rival family and shows P(FAIL \| rival true) ≥ π on the planned data (`tools/power_gate.py contrast --rival-effect`); if the rival's move is at or above the kill line (κ_F × predicted move) no sample size reaches it (pick 35 and its review: a sign-payoff-best one-pole linear rival moves about 90% of the Bayes move, two-pole kernels 90–105%) and the result is labelled non-discriminating between the two. Output pasted in the prereg; a prereg that fails is redesigned or locked as exploratory, not decisive (`reviews/night2/CAUSAL_POWER_GATE.md`; merges KG-FEASIBILITY-GATE) | Locks that can only end INCONCLUSIVE: STAKES-SHIFT-CAISO (PASS region empty; FAIL unreachable at any stakes change), WIKIDATA-BAND KG(a) (bound unattainable at n = 40 even with zero changes) |

**Admissibility rule (the anti-rescue clause).** If a test passes MV1–MV8, its result counts fully. A later claim that "the instrument missed how X really works" is inadmissible unless it names a gate the test actually failed. Two independent Tier-2 failures in different systems count as one Tier-1 failure (as in FAIR_MEASURE §5).

### 2.3 Status vocabulary this implies (used in CLAIM_MAP_v2)
- **PROVED (in-model)**: a theorem in 𝓜 that survived the math review. Nothing about nature.
- **MATH-CORRECTED**: the original statement was false as mathematics, and a corrected statement replaces it (the correction is usually PROVED).
- **PROXY-FAIL / PROXY-PASS**: a locked prediction failed or passed on a proxy that fails at least one of MV1–MV8. The row names the failed gates. A PROXY-FAIL is a valid fail *of that mapping*.

- **NOT A TEST** (added 20 Nov 2026, GRID-DX review of PR #113; compound status after the confirm round): a field claim is first gated on qualification under the pre-written definition (THEORY §3 / FRAMEWORK §9), then reported as passed or failed on proxy. The headline is **NOT A TEST (qualification not established; proxy: passed)** or **(…; proxy: failed)** or **(…; proxy: INVALID)** when no pre-test qualification check was recorded, and **NOT A TEST (not qualified; proxy: …)** when the class is shown not to qualify. Applied symmetrically to PROXY-PASS and PROXY-FAIL. The original proxy result and the validity-gate reasons stay visible in the status column and the cell; nothing is deleted. This is not a rescue of a miss.
- **OPEN**: not tested on a valid instrument.
- **PRIOR ART**: published by others.
- Three extra labels, because forcing rows into the six above would misstate them:
  - **SIM-FAIL**: a locked in-model simulation prediction failed. That is not a proxy problem.
  - **NOT EVIDENCE**: circular or by-construction.
  - **WITHDRAWN**: a miscitation, or a framing claim withdrawn as false.
- Reserved for the future: **FIELD-FAIL** and **FIELD-PASS**, for Tier-1 results. **No row currently has either.**

---

## 3. The quantities: operational definitions by scale, procedures, validity checks and failure modes

Notation follows `AXIOMS.md` §0. Scales:
- **Cell**: bacteria, single eukaryotic cells.
- **Immune**: an individual's adaptive immune system, and population immunity plus public-health surveillance as a higher level.
- **Ant**: a colony.
- **Person**: an individual's memory and attention.
- **Team/firm**.
- **City**.
- **AI**: multi-agent or memory-augmented AI systems, including this bot.

Each table cell is an **operational proposal** [PROPOSAL] unless it cites a dataset or a published measurement. Mappings that are hypotheses are marked "(mapping hypothesis)". They need their own validity check before use.

### 3.0 Prerequisites: target, pool and level (Q0)
**Definition.** Target x_i is the quantity whose error costs member i (Axiom 2). The pool is the set of members sharing a source. A **level** is a tracker of a source whose estimate is consumed by ≥ 2 members (Axiom 6).

| Scale | Target x_i | Pool | Level (consumption evidence required) |
|---|---|---|---|
| Cell | Ligand concentration or gradient at the cell (chemotaxis); nutrient level (gene regulation) | Receptors of one cell (shared ligand), or cells sharing a medium | A shared signaling module whose output many receptors' or cells' decisions use (mapping hypothesis: the CheR/CheB adaptation module shared by receptor types; a quorum signal for cells). Evidence: knockout changes all consumers' responses |
| Immune | Antigenic phenotype of a pathogen lineage that host defenses must match | Hosts exposed to the same lineage; or the epitopes of one pathogen | Within a host: a memory pool for a conserved epitope, used against many strains (mapping hypothesis). Across hosts: surveillance plus vaccine-strain selection (e.g. WHO GISRS), whose estimate many hosts "consume" by vaccination |
| Ant | Location or quality of food patches; nest-site quality | Foragers sharing a patch field | Trail or pheromone network, or scouts, whose information recruits many foragers. Evidence: foragers' choices follow the trail (Beckers et al. 1989 [FULL]) |
| Person | A fact or skill state needed for one's decisions (a password, a colleague's role, a price) | Several of one's own tasks sharing a fact (intra-person pool) | A personal external store (notes, calendar) consulted by several tasks; or a memory "schema" shared across tasks (mapping hypothesis) |
| Team/firm | A named driver: supplier price, upstream API version, a regulation, a customer segment's demand | Units whose decisions load on the driver (measured loading, §3.2) | A role, team or system that tracks the driver and whose estimate others use. Evidence: reads of its output (dashboard views, report distribution, "who do you go to for X" nominations), **not title** |
| City | Demand for a service in a neighborhood; weather; traffic | Neighborhoods or agencies sharing a driver | A citywide office or system (311 analytics, a weather service, a traffic center) whose estimate several agencies consume |
| AI | The state an agent's action depends on (a file's content, an API's schema, a user's preferences) | Agents or sessions whose tasks read the same state | A shared memory, index or cache consumed by ≥ 2 agents. Evidence: retrieval logs |

**Validity checks.**
- **Construct**: show consumption (logs, knockouts, nominations), not just existence.
- **Convergent**: two consumption measures agree (e.g. dashboard reads and nominations).
- **Discriminant**: the "level" is not just the most-connected node for unrelated reasons (status, hub position). Contrast its use for the named driver against its use for unrelated content.
- **Known-groups**: a documented central tracker (a commodities desk for a commodity price; a dependency-management team for an upstream library) must classify as a level.

**Failure modes.** Title ≠ level. A level's estimate may be consumed through intermediaries (assistants, staff), so the "level" is an office, not a person. Pools defined by office or org chart instead of measured loading.

### 3.1 Drift rate q, Hurst exponent H, drift spectrum (Q1)
**Definition.** q is the variance per unit time of the target's increments; more generally E(Δ_τ x)² = q τ^{2H}. The spectrum is S(f) ∝ f^{−α}. Poisson replacement at rate λ is an alternative class.

**Procedure (all scales).**
1. Obtain a time series of the **target itself**, not of events about it, at a resolution finer than the tracker's read interval.
2. Compute the structure function (variogram) D(τ) = mean (x(t+τ) − x(t))² over τ spanning ≥ 1.5 decades. Fit ln D = ln q + 2H ln τ. Report q at a stated reference τ.
3. Remove measurement noise using the τ → 0 intercept (a nugget).
4. Detect jumps (Poisson class) via the kurtosis of increments.
5. Remove calendar cycles before any spectral fit (DRIFT1 lesson).

| Scale | Target time series | Source |
|---|---|---|
| Cell | Ligand concentration experienced along tracked trajectories; or designed microfluidic stimulus statistics (then q is set by the experimenter) | Designed stimuli give exact q (Mattingly et al. 2021 [fetched BIO1]; Frankel et al. 2014 [fetched BIO1]) |
| Immune | Antigenic position per year from HI cartography (antigenic units per year) | Bedford et al. 2014 HI data for H3N2, H1N1, B/Vic, B/Yam on Dryad doi 10.5061/dryad.rc515 [DATA-VERIFIED 15 Nov]; Smith et al. 2004 cartography [SEC, via Bedford 2014] |
| Ant | Patch location or quality over time (experimental manipulation) | Not in the public tracking sets checked (§5): needs an experiment |
| Person | The changing fact itself (e.g. an officeholder, a price, a colleague's role) | Wikidata statement histories for fact types [PROPOSAL; API DATA-VERIFIED 15 Nov, see §5] |
| Team/firm | The named driver's series: supplier price, upstream library releases and breaking changes, regulation text versions | Public for software (upstream release histories); commodity price series |
| City | Demand per category and neighborhood | NYC 311 Socrata [ON BOX, used in DRIFT1] |
| AI | The environment generator (designed), or the measured rate of change of the files/APIs/users the agent serves | Designed (LEARNSIM) or repository histories |

**Validity checks.**
- **Construct**: the series is the target, not its use. **"Need" (recurrence of mentions) is not drift.** It measures use rate μ (§3.8). Several past tests conflated them (P1, MATCH1, measles).
- **Convergent**: q from the variogram vs q from an independent method (sequence-based vs HI-based antigenic drift; release-note breaking changes vs API diffs).
- **Discriminant**: q should not be explained by observation intensity (more observed items look more variable). Check q against sampling density.
- **Known-groups**: measles (antigenically monotypic, q ≈ 0) vs H3N2 (fastest of the four flu lineages per Bedford 2014 [DATA-VERIFIED abstract]); a fixed constant (q = 0) vs a random-walk price.
- **Power**: to estimate H to ±0.1, use ≥ 1.5 decades of τ with ≥ 30 independent increments at the longest lag.

**Failure modes.** Mistaking event frequency for variance. Calendar leakage. Short spans that cannot tell H = ½ from long memory. Selection of "interesting" targets. Observation noise inflating short-lag q.

### 3.2 Shared vs private drift, ρ, and the sharing-decay exponent κ (Q2)
**Definition.** x_i = Σ_m B_im s_m + u_i. q_g is the drift of source s (times its loading); q_u is the private drift; ρ = q_g/q_u, **relative to the pool**. Across nested scopes, q_s ∝ n_s^{−κ}, where n_s is the pool size at scope s (T7).

**Procedure.**
1. Collect increment series Δx_i for all members of the pool over common windows.
2. Fit a factor model on increments (one factor per named source). Estimate B_im and Var(Δs), and take residual variance as q_u. **ρ̂ = B̄² q̂_s / q̂_u.**
3. For nested scopes, fit a hierarchical random-effects model on increments: member ⊂ team ⊂ department ⊂ firm. The variance component at scope s gives q_s. Regress ln q_s on ln n_s to get **κ̂**.
4. Report ρ̂ per pool with a bootstrap CI over members and time blocks.

| Scale | Increment data for the decomposition |
|---|---|
| Cell | Single-cell responses to a common designed stimulus plus cell-specific fluctuations. Keegstra et al. 2017 single-cell FRET separates cell-to-cell and temporal variability (source .mat files exist, eLife doi 10.7554/eLife.27455 [DATA-VERIFIED 15 Nov: source data files listed]) |
| Immune | Shared vs strain-specific antigenic change across co-circulating strains (shared = conserved-epitope drift, private = strain-specific drift; mapping hypothesis) |
| Ant | Common (colony-wide patch field) vs forager-specific information. Requires an experiment |
| Person | Shared vs task-specific change in facts used across a person's tasks |
| Team/firm | Unit KPIs or decision inputs (demand by unit, prices faced by unit). A common factor gives q_g, residuals give q_u. A hierarchical decomposition gives κ |
| City | Neighborhood demand series. Common citywide vs local components (311 [ON BOX]) |
| AI | Designed in the environment, or measured from co-change of files across agents' tasks |

**Validity checks.**
- **Construct**: the factor must be the *named* source. Validate its loadings against an external measure of the source (e.g. commodity price index vs. units' input costs).
- **Convergent**: ρ from factor analysis vs ρ from structural knowledge (exposure shares).
- **Discriminant**: ρ must not just reflect a common measurement artifact (a reporting calendar). Use placebo pools (random members).
- **Known-groups**: a designed world with known ρ (LEARNSIM); placebo pools where ρ ≈ 0.
- **Power**: ρ near the small-ρ regime (ρ ≲ 0.1) needs long series. The CI for ln ρ should be ≤ ±0.3.

**Failure modes.** Pool misdefinition (offices instead of reporting units). Factor rotation ambiguity with several sources. Nonstationary loadings. **Assuming κ = 0 when computing predicted rank gradients**, which was the hidden auxiliary in every past vigilance prediction (§3.9, §4.4).

### 3.3 Stakes W and loss shape ℓ (Q3)
**Definition.** w_i is the cost per unit time per unit of loss of tracking error. W_m = Σ_i w_i B_im² is pooled. The loss shape is ℓ(e).

**Procedure.** Estimate the outcome cost as a function of tracking error, from natural or designed variation in error (an error-cost curve). Fit ℓ(e) ∝ |e|^p. W is the summed per-member slope.

| Scale | Error-cost evidence |
|---|---|
| Cell | Growth rate or chemotactic drift speed vs. mismatch between internal state and environment (designed environments) |
| Immune | Infection probability or severity vs antigenic distance between memory and challenge strain (e.g. HI-titer-to-protection curves; mapping hypothesis) |
| Ant | Food intake lost vs error in patch information (experiments) |
| Person | Task error or time lost vs memory error |
| Team/firm | Cost of decisions made on stale driver values (mispricing loss, rework after an upstream breaking change) |
| City | Service failure cost vs forecast error |
| AI | Task reward lost vs stale state (directly measurable) |

**Validity checks.** Construct: the error is error *in the target*, and the cost is *caused* by it (use designed or natural-experiment variation). Convergent: two outcome measures. Known-groups: designed AI tasks with a known ℓ. **Bundled vs separable** (Axiom 2, T4): record whether shared and private errors feed **one decision** (bundled) or different decisions (separable). T4's loss-irrelevance claim depends on it.

**Failure modes.** Loss measured only at the extremes. Survivorship (units with high stakes and poor tracking are gone). Confounding stakes with drift.

### 3.4 Sensing price p and sensing class (a, b), measured separately for members and for the level (Q4)
**Definition.** φ(W, q; p) = k p^{1−a} W^a q^b. **Effort elasticities equal (a, b)** (Lemma 1, claim map A5; in A_θ, "effort" means r^{−θ}). Class R (reset reads): a = b = ½. R2 (entropy-priced filtering): a = b = ½. A_θ (averaging): b = a/2 in the averaging row. **The level's class (a_L, b_L) sets e_g (T1.8, T4). The members' b_m sets e_u.** These must be measured on different units: this was the night-1 SENSING mistake (physstat §7.2).

**Procedure (the class gate).**
1. On **lone or flat** units (no level), record effort E per unit time on the named target (reads, queries, receptor occupancy time, antennation rate), together with measured stakes W and drift q.
2. Fit ln E = const + a ln W + b ln q (+ ln p controls). Use cluster-robust SEs.
3. **Separately**, on units that act as levels, fit the same model using the level's own effort on its own source. This gives (a_L, b_L).
4. Where the technology is designed (AI, software CI), read the price structure directly as well. A per-read price is R1-like. A per-token or per-nat price is R2-like. A precision price is A_θ.

| Scale | Effort observable (sampling choice) | Price |
|---|---|---|
| Cell | Receptor sampling time, CheY-P integration time, or methylation-based adaptation time vs stimulus statistics (Keegstra 2017 single-cell FRET [DATA-VERIFIED]; Mattingly 2021 information-rate limit [fetched BIO1]) | ATP or protein cost per unit precision (a mapping hypothesis; J11). Berg–Purcell averaging makes cells A_θ-like (physstat §2.1) |
| Immune | Frequency of re-sampling an antigen (germinal-center re-entry, booster cadence); at the population level, surveillance sampling (sequences per month) | Cost per surveillance sample, or per booster |
| Ant | Scout departures or antennation rate per patch | Time and energy per scouting trip |
| Person | Checks of a fact (lookups, glances, queries) | Time per check |
| Team/firm | All-channel sampling events of the named driver: reads, queries, API or log accesses, meetings or calls tagged to the driver, scheduled jobs that poll it | Staff time per read; compute per poll |
| City | Inspection or sensor polling rates per driver | Cost per inspection |
| AI | Tool calls or retrievals on the target per unit time | Tokens or compute per call (real cost, not a formula) |

**Validity checks.**
- **Construct**: effort is chosen sampling, **not** receipt or assignment. Every channel is counted.
- **Convergent**: class from elasticities vs class from the technology's price structure.
- **Discriminant**: elasticities are not driven by generic activity. Include total activity as a control, and check a placebo target.
- **Known-groups**: designed AI arms with a known class; schedule-driven reading (EOQ-like inventory reorder) should come out a ≈ b ≈ ½.
- **Power**: to separate class R (a = b = ½) from A₁ (θ = 1: a = ⅔, b = ⅓, from b = a/2 and e_g = −(1+θ)) needs SE(b̂) ≤ 0.06 (gap ⅙ divided by 2.8). To separate a = b from a ≠ b needs SE(â − b̂) ≤ 0.1.

**Failure modes.** **Quantized schedules** (defaults like "daily" or "weekly" crons; top-coded survey scales) compress elasticities toward 0. Channel omission. Measuring the members' class and using it for the level. Effort measured as precision when the theory's "effort" is r^{−θ}. A Hurst exponent H ≠ ½ shifts the R1 exponents (claim map E4).

### 3.5 Upkeep h (Q5)
**Definition.** The existence cost per tracker per unit time, independent of reading.

| Scale | Operationalization |
|---|---|
| Cell | Expression and maintenance cost of a receptor or pathway (protein burden), from fitness cost of expressing it in a constant environment |
| Immune | Maintenance cost of a memory pool (homeostatic turnover); not directly measurable today in most systems |
| Ant | Trail maintenance deposits when nothing changes |
| Person | Rehearsal time for an unchanged fact |
| Team/firm | Salary and overhead of a tracking role, net of time spent reading |
| City | Fixed budget of a monitoring office |
| AI | Storage plus index maintenance per store; context tokens spent holding a summary |

**Validity checks.** Construct: cost incurred with zero reads. Known-groups: in AI, h is set by design. Convergent: accounting cost vs revealed cost (removal saves it).

**Failure modes.** Bundled with read costs in accounts. Not separable in biology without knockouts. **h′ depends on q_u** (math Issue 5). Report the normalized h′ only with q_u fixed.

### 3.6 Vigilance V (Q6)
**Definition.** V = the level's information effort on source g ÷ a **flat** member's effort on g, both **per unit of g's own drift** and over the **same channel set**. Corrected predictions (E6–E8):
- V(N\*) = ½(1 + (1+ρ)^{−1/2})(1 + √(1 + 4h′(√(1+ρ) − 1)/(rρ))).
- Floor: V(N\*) ≥ 1 + (1+ρ)^{−1/2}, for every upkeep and price ratio.
- V grows as N^a above onset.
- At h = 0, V(N\*) does not depend on the price ratio.

**Procedure.** As claim map §3.2 and FAIR_MEASURE §2, but with all of the following added:
- (i) the class gate (§3.4) on flat units first;
- (ii) ρ̂ from §3.2 for the level's pool;
- (iii) q̂_g for normalization;
- (iv) all-channel effort;
- (v) a flat comparator;
- (vi) κ̂ (§3.9) whenever the comparison spans ranks.

| Scale | Level effort vs flat comparator |
|---|---|
| Cell | Shared module's sampling vs a cell or receptor type lacking it (knockout or natural variant) (mapping hypothesis) |
| Immune | Population surveillance sampling of a lineage vs individual-level re-sampling (mapping hypothesis; weak) |
| Ant | Scouts' sampling of patch field vs foragers in colonies without recruitment trails (species contrast; mapping hypothesis) |
| Person | A person's external note-checking for a fact shared by several tasks vs single-task checking |
| Team/firm | Central tracker's all-channel sampling of g vs units without one (before/after a reorg that created the level) |
| City | Central office polling vs neighborhood offices in cities without a central office |
| AI | Shared-memory agent's retrieval rate on g vs flat agents each tracking g (designed) |

**Validity checks.** Known-groups: in a designed AI system, V must come out at the formula's value (calibrates the instrument). Discriminant: status, generic activity, and function (FAIR_MEASURE §2.6). Power: detect ln V = 0.5 at 80% power (FAIR_MEASURE §2.8).

**Failure modes.** Every one that hit PIAAC and Enron (§4): self-report, top-coding, received not sought, one channel, no named driver, the nested-member comparator, assistants, **κ unmeasured**.

### 3.7 Onset group size N\* and onset exponents e_g, e_u (Q7)
**Definition.** N\* is the smallest N with a level (G(N) > 0). e_g = ∂ln N\*/∂ln q_g. Predicted e_g = −(1−b_L)/(1−a_L) (T1.3, T1.8) at small ρ, h = 0. T3: shared drift lowers N\* and private drift raises it (common technology).

**Procedure.**
1. Across many pools with measured N, ρ̂ and q̂_g, q̂_u, code the presence of a level (§3.0 consumption evidence).
2. Fit a presence model P(level | N, ρ) with a threshold N\*(ρ) = A ρ^{e}. Estimate e with a CI.
3. **Experimental version (preferred):** manipulate ρ over ≥ 1.5 decades and observe adoption.
4. Measure (a_L, b_L) on the level separately (§3.4), and predict e from it **before** fitting.

| Scale | Pools and level presence |
|---|---|
| Cell | Strains or species with vs without a shared module, vs environmental ρ (comparative; weak) |
| Immune | Pathogens with vs without population-level strain surveillance and vaccine updating, vs shared/private antigenic drift (n small) |
| Ant | Species or colonies with vs without recruitment trails vs colony size and patch persistence. A threshold colony size exists (Beekman, Sumpter & Ratnieks 2001 [DOI]); counter-evidence: Dornhaus et al. 2006 [FULL] |
| Person | Tasks sharing a fact: when does a person create an external note? |
| Team/firm | Groups of units sharing a driver: when does a central tracking role or system exist? |
| City | When does a citywide monitoring office exist, by city size and ρ? |
| AI | Agent groups: when is a shared memory adopted? (LEARNSIM, `tests/LEARNSIM/`, done 15 Nov 2026; CLAIM_MAP G23–G29) |

**Validity checks.** Selection gate (§3.10) is mandatory: POOLSIM showed the onset is invisible when decision noise is ≥ 1% of cost. Known-groups: designed AI arms. Discriminant: rule out the rival "levels appear at a fixed size regardless of ρ" (span-of-control norms).

**Failure modes.** Institutional mimicry (levels copied, not selected). Coarse N bins. Levels created for authority rather than tracking (physstat on F5). Reverse causation (levels change ρ by reducing private drift, §5 of THEORY).

### 3.8 Freeze / hold / lookup modes and their inputs μ, u, c, H_l (Q8)
**Definition.** For an item:
- **freeze**: read once per lifetime H_l;
- **hold**: track at a refresh rate;
- **lookup**: read the source at each use, with use rate μ and cost u per lookup.

T8: the hold band exists iff μuH_l > 2c + hH_l. The freeze edge is q_f = 2c/(WH_l²) and the lookup edge is q_c = (μu − h)²/(2cW). A shared store widens the band by N².

**Procedure.** Classify each item's mode from logs:
- **freeze**: no refresh during life;
- **hold**: periodic refresh of a local copy;
- **lookup**: a fetch at each use.

Measure q per item (§3.1), μ from use logs, u from lookup latency or cost, c from refresh cost, and H_l from item lifetime. Predict each item's mode from the closed forms, then compare.

| Scale | Item and modes |
|---|---|
| Cell | Constitutive expression (freeze) vs regulated expression (hold) vs induction on demand (lookup) per gene, vs environmental drift of its target (mapping hypothesis) |
| Immune | Long-lived plasma cells, sterilizing memory (freeze); memory recall and boosting (hold); naive primary response (lookup). Drift from HI cartography. Prior art: Mayer et al. 2016 [ABS] |
| Ant | Fixed routes (freeze) vs maintained trails (hold) vs individual search (lookup) |
| Person | Memorized fact vs regularly refreshed fact vs looked up each time (Sparrow et al. 2011 [ABS] on offloading) |
| Team/firm | Hardcoded value vs maintained local copy vs live query. In software: a pinned dependency (freeze), a vendored copy updated on schedule (hold), a floating or latest dependency (lookup) |
| City | Static signage vs periodically updated schedules vs live feeds |
| AI | Weights or system prompt (freeze) vs summarized memory (hold) vs retrieval at use (lookup) |

**Validity checks.** Known-groups: values that never change (birth dates, constants) must classify as freeze. Values with very high drift and use should classify as lookup or shared store. Convergent: mode from logs vs mode from documented policy. Discriminant: policy mandates (e.g. a community rule against central storage) must be coded and contrasted, not ignored.

**Failure modes.** Mode set by norms or technical constraint, not cost. Use rate confused with drift (the measles test, §4.3). Lifetime censoring.

### 3.9 Level speed and the sharing-decay exponent κ (Q9)
**Definition.** A level's speed is its tracker's update bandwidth: the read rate n_s, or its inverse, the read interval. Across nested scopes, the shared driver at scope s drifts at q_s ∝ n_s^{−κ}.

**Derived consequence [DERIVED HERE; checked in `checks/kappa_rank_gradient.py`]:**
- In P(a, b), the level's effort scales as W^a q^b, with W ∝ N_s.
- So the **raw** sampling rate of the level at scope s scales as **N_s^{a − κb}**. For class R (a = b = ½) that is N_s^{(1−κ)/2}.
- The raw rate rises with rank only if κ < a/b (κ < 1 for class R).
- For class R this coincides with T7's top-down condition κ < κ\* = (1−a)/(1−b) = 1.
- Numerical check: fitted elasticities 0.500, 0.250, 0.000 and −0.250 at κ = 0, 0.5, 1 and 1.5 match (1−κ)/2 exactly.

**What this means for past tests.** The Enron P3 band (elasticity 0.3–0.7 on subtree size) and the PIAAC P3 band (√span, 0.5) both **implicitly assumed κ ≈ 0**: a driver at the top drifting as fast per member as one at the bottom. With κ unmeasured, those bands were predictions of "class R and κ ≈ 0", not of GTAO.

**Heuristic, not derived.** If a scope's shared component behaves like an average of many weakly correlated sub-components, its variance falls roughly as 1/n_s (κ near 1). A genuine common shock (a macro factor, a regulation) gives κ near 0. Which holds is an empirical property of each environment.

**This must not be used to rescue Enron after the fact.** It becomes a test only when κ is measured independently and the rank gradient is predicted *before* the sampling data are opened (§6.9).

| Scale | Level speed observable | κ estimate |
|---|---|---|
| Cell | Adaptation or integration time of shared vs specific modules | Variance of stimulus components at nested scopes (designed) |
| Immune | Surveillance update cadence (e.g. twice-yearly WHO influenza recommendations [UNVERIFIED cadence; check before use]) vs individual response time | Drift of shared vs lineage-specific antigenic components |
| Ant | Trail turnover vs individual memory decay | Patch-field variance at nested spatial scales |
| Person | Refresh interval of shared vs task-specific facts | Variance decomposition of facts across task scopes |
| Team/firm | Read interval of each level's tracker (dashboard refresh, meeting cadence on the driver) | Hierarchical variance decomposition of unit-level drivers (team ⊂ dept ⊂ firm) |
| City | Update cadence of neighborhood vs citywide monitoring | 311 variance at block ⊂ board ⊂ borough ⊂ city [ON BOX in part] |
| AI | Refresh interval of per-agent vs shared memory | Designed |

**Validity checks.** Known-groups: a designed hierarchy with known κ. Convergent: κ from variance components vs κ from exposure structure. Power: SE(κ̂) ≤ 0.2 to separate κ < 1 from κ > 1 decisively.

**Failure modes.** Few scopes (≤ 3) make κ̂ poorly determined. Scopes defined by org chart rather than measured pools.

### 3.10 Selection resolution ε (Q10; the gate for every design prediction)
**Definition (Axiom 7).** The realized design satisfies J(A) ≤ min J + ε. Prop 10: no level is detectable for ρ ≲ ε/b.

**Procedure.**
1. Among comparable units, compute the dispersion of realized designs around the predicted optimum (e.g. the residual SD of ln effort after the class fit).
2. Convert it to a cost loss using the fitted φ: a mis-set read rate by factor k costs (k + 1/k)/2 − 1 of tracking cost in class R [DERIVED HERE from φ ∝ cn + Wq/(2n)].
3. ε̂ is that cost loss at the median dispersion.
4. **Gate**: analyse only settings where the predicted prize (e.g. bρ times tracking cost for onset) exceeds ε̂.

| Scale | Expected selection strength (prior; to be measured, not assumed) |
|---|---|
| Cell | Strong in large microbial populations (drift barrier: Lynch et al. 2016 [DOI]) |
| Immune | Within-host selection strong; population-level public health is a designed and political process (weak) |
| Ant | Colony-level selection moderate; experiments help |
| Person | Learning-based, moderate, noisy |
| Team/firm | Weak to moderate; competition varies by industry |
| City | Weak (political) |
| AI | Set by the optimizer: strong if trained or evolved on the cost |

**Failure modes.** Using ε to excuse misses after the fact. **The gate must be computed before outcomes.**

### 3.11 Physics: the thermodynamic binding ratio β_phys (Q11; Chad's "constrains less at firm scale" made measurable)
**Definition.** β_phys = (actual cost of one read or of holding one bit) ÷ (its thermodynamic floor, kT ln 2 per bit erased, or the relevant nonequilibrium bound). β_phys near 1 means physics constrains the design choice. β_phys ≫ 1 means physics is a non-binding floor, and the design is set by other prices.

| Scale | Status |
|---|---|
| Cell | Measurable in principle. Chemotaxis adaptation is dissipative with an energy–speed–accuracy relation (Lan et al. 2012 [fetched BIO1]). Information-rate limits are approached (Mattingly et al. 2021 [fetched BIO1]). β_phys for the E. coli aspartate-receptor network was computed in SENSE-CELL (18 Nov 2026) as fuel free energy (≈29 kT per SAM methyl transfer, Lan et al. 2012) ÷ the Lan best-performance-line minimum dissipation for the achieved adaptation error. This floor is the best-circuit minimum for a minimal feedback network with Tar energetics, not a second-law floor. **Status: INCONCLUSIVE** (CLAIM_MAP N24; Tier 3). β_phys ≤ 10 is equivalent to a dissipation-limited adaptation error of about 2-8% (premises: Lan's ε0 0.18-0.7, α 0.70-0.75). The closest like-for-like readings give β_phys about 5-9 at Lan's Tar anchor (~99%, circular) and about 7-21 (median 11) at Lan's own wild-type whole-cell accuracy (~95%): at the edge of the band [1, 10], neither inside nor outside. The one reading that gave 18 [12.5, 26.2] (Keegstra 2017, whole mixed array, 500 µM MeAsp) is not a valid measurement of the energy-limited error, because at that stimulus methylation-site saturation, not energy, caps precision (Neumann et al. 2014), so its locked-rule FAIL is not counted as evidence against. A matched measurement needs Tar-only cells at a small step with the error resolved to ±1% and the fuel energy measured (queue SENSE-CELL-MATCHED). `reviews/night2/SENSE_CELL_REVIEW.md` |
| Neurons | Synapses pay roughly 10⁵–10⁶ times kT ln 2 per bit (Laughlin et al. 1998 [fetched], as summarised in THEORY §2.3), so β_phys ≫ 1 |
| Ant, person, firm, city | β_phys is astronomically above 1 (attention and money prices dwarf kT). Physics is a floor, not a constraint |
| AI | Computable: joules per token vs the Landauer bound. β_phys ≫ 1 on current hardware [classic magnitude; not computed here] |

**What this changes.** The physics claim becomes testable in one place: at the cell scale, if β_phys ≈ 1–10 for a sensing system, the thermodynamically priced class should be the one selected. That would **fix (a, b) and so the exponent** (J11). The cell value is now computed but INCONCLUSIVE (above), so J11 is still owed: the matched measurement is the single most valuable physics derivation still open.

**The "same three costs at every level" statement.** Axiom 5 builds the same decomposition (reads, error, upkeep) into every level. So the *form* of the budget is universal by construction. The *exchange rates* (prices) are not. The universal content is that the same **relations** hold at every level with that level's own measured prices and class. That is testable (§6.1) and not yet tested.

### 3.12 Self-application: the AI scale, applied to this bot (Chad, t1908)
The same quantities apply to the system writing this file. [PROPOSAL; descriptive, not evidence.]
- **Targets**: project facts (what was locked, what was killed).
- **Pool**: the parallel subagents (night-1 reviewers, LEARNSIM, VIGIL_ONA, this executor), which share those facts.
- **Level**: the shared stores. These are the private repo, the claim maps, and the bot's memory. Their estimates are consumed by every agent.
- **Drift**: the rate at which project facts change. It was very high overnight: the claim map went stale in four rows within an hour, per physstat §7.
- **Reads**: file reads and memory recalls, which cost tokens.
- **Upkeep**: maintaining the claim maps.
- **Freeze/hold/lookup**: locked preregistrations are frozen. Claim maps are held, which means they must be refreshed when tests finish. Raw outputs are looked up.

The theory's prediction for this system: because the drift of project facts is high and many agents consume them, a **shared, frequently refreshed store** beats per-agent summaries once there are more than a handful of agents. A stale shared store (the night-1 FORMAL/CLAIM_MAP) is the predicted failure when the refresh rate falls below the drift. That is what physstat §7 found. This is an anecdote, not a test. A real test would log reads, staleness and errors across agent runs. It is cheap to instrument, and it is the cleanest AI-scale test of the freeze/hold/lookup band.

---

## 4. Re-audit of every past field test (what was actually measured, the validity gaps, and the honest relabel)

Each row lists the gates from §2.2 that the test **failed**. "Mapping" means what the observable was taken to stand for.

### 4.1 P1: within-item news recall slope (theory-v3; Meeter, Murre & Janssen 2005 data) [ON BOX: uncommitted raw archive; see `tests/MATCH1/DATA.md` and `tests/MATCH1/memory/meeter.py`]
- **Measured.** The within-item, within-session slope of open-recall odds on ln(age of the news event). Locked a_c = 0.310; independent re-fit 0.321 [0.289, 0.352].
- **Mapping.** The recall slope stood for the *held memory* of an item. Headline-**word** recurrence in ABC headlines (0.71) stood for that item's **need** for that person.
- **Auxiliaries.**
  - The SCALEFREE derivation that the item-level exponent ratio d ≥ 1. This is a derived claim that was itself never independently reviewed.
  - Retrieval failure exponentially tailed.
  - Stakes and upkeep homogeneous after fixed effects.
- **Failed gates.**
  - **MV2**: need for an item was proxied by word recurrence in a different corpus, not by that respondent's exposure or use. Open recall measures retrieval, not holding.
  - **MV3**: d was taken from theory, not measured.
  - **MV5**: no second need measure.
  - **MV7**: no known-groups calibration showing the instrument recovers a matched slope where matching is known.
  - The never-encoded floor was a pre-stated threat.
- **What passed.** The statistics are sound (physstat re-fit). The lock is clean apart from the in-text time. The kill was pre-declared to count under these threats.
- **Honest relabel: PROXY-FAIL.** This is **the strongest of the proxy fails.** The memory measure is valid for recall. The weak link is the need proxy plus an unreviewed derivation.
- **What it still tells us.** Item-level recall in a quiz population does not follow headline-word need with d ≥ 1. The named rival (0.24) is also excluded.

### 4.2 MATCH1 A1: memory exponent = need exponent (news, population level)
- **Measured.** The marginal recall slope (0.24) vs headline-word need (0.71).
- **Failed gates.** MV2 (as 4.1, plus marginal heterogeneity attenuation, which SCALEFREE S2(iv) itself predicts); MV3; MV6 (heterogeneity rival not separated).
- **Relabel: PROXY-FAIL** (the strong form). The weak form, a power law following a power law, is **PRIOR ART** (Anderson 1990; Anderson & Schooler 1991 [DOI]).

### 4.3 MATCH1 B1: measles freeze-or-hold (the "hit")
- **Measured.**
  - **Need**: the odds that measles is *reported in an English or Welsh town* again, vs biweeks since its last report, 1944–65 (exponent 2.15).
  - **Memory**: measles antibody titer decay in 42 people (Antia et al. 2018), with time since infection approximated as age − 5 (exponent 0.11).
  - Ratio 0.05 < 0.5, scored as "frozen".
- **Mapping.** Town-level epidemic recurrence stood for an individual's re-exposure need. Titer decay stood for (lack of) refresh effort.
- **Failed gates.**
  - **MV2**: Theorem G's freeze condition is about **drift** × check cost vs the value of holding. The relevant drift is **antigenic drift of measles**, which was not measured. Measles is generally described as antigenically monotypic, but I have not verified a source this session. Town recurrence measures epidemic dynamics, i.e. use rate μ, not drift q. Titer decay measures waning, not refresh effort.
  - **MV3**: time since infection was approximated.
  - **MV5**: no second memory measure.
  - **MV6**: the mechanistic rival (long-lived plasma cells) was not separated.
  - **MV7**: no known-groups calibration (e.g. a fast-drifting pathogen classified as held).
  - **MV9**: the data were already read (an ordinal postdiction per CORE_AUDIT); not reviewed.
- **Honest relabel: PROXY-PASS.** It supports nothing GTAO-specific. Under valid measurement, "a non-drifting antigen gets frozen memory" is the Mayer et al. 2016 phase-diagram result [ABS], i.e. **PRIOR ART**.
- **Chad's hypothesis, checked.** Chad suggested the hits may also be measurement artifacts. For measles this is right in a specific way: the test measured use rate (μ) and called it need/drift. Its "pass" does not bear on the freeze edge q_f = 2c/(WH_l²).

### 4.4 VIGIL (PIAAC, 9 countries): supervisors vs non-supervisors on external reading
- **Measured.** Self-reported frequency (5 top-coded categories) of reading news, journals, and "keeping up with products" at work, for supervisors vs non-supervisors in the same occupation × country. Results: P1 1.14 (1.05–1.23); P2 specificity null when correctly specified (1.06); P3 span slope 0.036; P4 1.15.
- **Mapping.** Those items stood for sampling the unit's shared external driver. Supervisor stood for the level. Span stood for pooled N.
- **Failed gates.**
  - **MV1**: no named driver; channels limited to reading; no meetings.
  - **MV2**: self-report; "whose driver" unknown.
  - **MV3**: ρ, q_g and κ not measured.
  - **MV4**: comparator = the supervisor's own kind of subordinates (nested members), not flat (Issue 10).
  - **MV7**: no known-groups check.
  - **MV8**: top-coding compresses ratios. Huge n makes direction "significant" while size is unidentifiable.
- **The κ point (§3.9).** P3's 0.5 band assumed κ ≈ 0. With κ unmeasured, P3 was a test of "class R and κ ≈ 0".
- **Relabel.**
  - P1 direction: **PROXY-PASS**, which is also PRIOR ART (Mintzberg's monitor role [FULL in VIGIL]).
  - P2 specificity: **OPEN (proxy null)**. The locked "pass" came from a misspecified estimator. The correctly specified contrast is 1.06 (0.98–1.16). No locked kill fired.
  - P3 growth: **OPEN (proxy null)**. 0.036 (CI −0.005 to 0.076) is inside the locked band 0 < slope ≤ 0.5, but its CI does not exclude 0, so P3 did not pass. No kill fired. The 0.5 theory value assumed κ = 0.
  - P4 size: **NOT EVIDENCE** (declared non-decisive by its own prereg).

### 4.5 VIGIL-2 (Enron email, 98 custodians): external share of received mail by rank
- **Measured.** The share and monthly volume of **received** mail from non-Enron domains, by a 5-level rank coded from a title list. Results: share RR 0.93 (0.82–1.06); volume 1.00 (0.84–1.20); implied elasticity 0.001.
- **Mapping.** Received external mail stood for the level's sampling of shared external drivers. Title rank stood for level. An assumed k = 6 per rank step stood for pooled N.
- **Failed gates.**
  - **MV1**: no named driver; one channel. Executives sample mostly verbally: Mintzberg [FULL in VIGIL]; Porter & Nohria, as cited in VIGIL-2 [not verified by me].
  - **MV2**: **received, not sought**; assistants filter mail; external ≠ the pool's shared driver (counterparties are private drivers).
  - **MV3**: no span, no ρ, **no κ**.
  - **MV4**: rank gradient, not a flat comparator.
  - **MV6**: function confound only partly handled.
  - **MV7**: none.
  - **MV9**: code edited 6 s after the lock; the pre-edit file was lost.
- **What passed.** MV8 statistical power (MDE ≈ RR 1.21 per level).
- **The κ point.** As derived in §3.9, under class R a flat raw rate across ranks is what GTAO predicts when κ ≈ 1. So a powered null on raw rates is uninformative about V unless κ is measured. **I flag this as a post-hoc observation that must not be used to claim Enron "fits".** It shows that the locked band encoded an unmeasured auxiliary.
- **Relabel: PROXY-FAIL** (a valid fail of the instrument's own prediction: "the external share of received mail rises with title rank").

### 4.6 LANG1: √N fade on Polynesian vocabulary (ABVD) [raw data off-repo, on the author's box; not in this repository]
- **Measured.** The elasticity of word-gain rate (91% of "gains" are *uncoded forms*) on current speaker population, over 10 sister pairs: 0.13 [0.05, 0.26].
- **Mapping.** Speakers stood for independent depositors. Basic vocabulary stood for a drifting shared target. Gain rate stood for the fade or turnover rate.
- **Failed gates.**
  - **MV2**: the theorem (N1/T4) needs **independent** noisy readings of a **drifting** target with small Kalman gain. Basic-vocabulary meanings are close to stable, and speakers are not independent depositors (both stated in the prereg). The outcome was dominated by a documentation artifact (uncoded forms).
  - **MV3**: no drift or independence measure.
  - **MV7**: no known-groups check (the stable-target Lieberman side was reproduced, but not inside the same table).
  - **MV8**: 10 pairs.
- **Relabel: PROXY-FAIL**, arguably out of the theorem's domain.

### 4.7 DECISIVE (banks, glucose, populations), F1 (firms) and C3 (open source): the τ "temperature" index
- **Measured.**
  - Banks: hazard on capital-ratio AR(1) τ.
  - Glucose: fixed-spread slope on autocorrelation time.
  - Populations: GPDD return rate.
  - F1: bankruptcy on cost-adjustment τ, which mostly measures fixed-cost share.
  - C3: dormancy on issue-close time.
- **Status of the claim itself.** `AXIOMS.md` §3 puts failure rates given a design **out of scope** for the structural theory ("first-passage physics, not GTAO"). The generic OU-with-barrier baseline makes the same signs (THEORY §8).
- **Failed gates.**
  - F1: MV2 (τ = operating leverage, per the independent review).
  - C3: MV2 (issue-close time is a habit measure) and MV7.
  - Glucose: the τ measure is closest to construct-valid. The literal kill fired on size, and the theory-specific structure (−1, √τ, collapse) failed.
  - Banks: sign only.
- **Relabel: PROXY-FAIL** for F1, C3, banks and populations. **Glucose: PROXY-FAIL (best-measured of the set).** All five rows are also tagged **out of scope** for the current structural core. These tests do not bear on onset, vigilance or freeze/hold/lookup at all.

### 4.8 BIO1 P3a and COLLAPSE1: immune memory lifetime vs pathogen drift; inventory buffering
- BIO1 P3a (lifetime does not track drift) was shown by COLLAPSE1 to be largely a measurement artifact: under power-law waning, a measured half-life grows with the age at measurement. That is MV2/MV7 failed in the original measure. **Relabel: OPEN** (the original contradiction is a PROXY-FAIL of a proxy now known to be invalid).
- COLLAPSE1 C2 (inventory buffering vs demand volatility, slope 0.00): industry-aggregate inventory stood for a buffer design, and volatility was not separated into shared and private parts. Fails MV1, MV3 and MV6. **Relabel: PROXY-FAIL.**
- COLLAPSE1 A1 (immune cue model): **PROXY-FAIL** (literature-derived proxies, MV5).

### 4.9 MATCH1 C1, D1–D3, E1 and DRIFT1 (descriptive tests of the world side)
- Need exponents in code and Wikipedia (D1, E1 passed). These measure **use recurrence (μ structure), not drift**. Valid as descriptions of need. **NOT EVIDENCE** for GTAO, because heterogeneous memoryless items produce the same band (SCALEFREE S1).
- D3 redness sign opposite: **PROXY-FAIL** (exploratory; the spectrum-to-exponent mapping was never derived, so the prediction had no valid construct).
- C1 layer count: OPEN (inconclusive).
- DRIFT1: descriptive, valid for its own question. It measured **event-rate distributions**, not target drift q (MV2 for T7's condition), so it is weak support for "scale-free drift".

### 4.10 Simulations (not field tests; the measurement critique does not apply)
POOLSIM, SENSING, SENSING2, ANTS1 and LAYERS1 measure the authors' own simulators. Their quantities are measured exactly by construction. So:
- passes stay **NOT EVIDENCE** (circular);
- locked failures stay **SIM-FAIL**.

ANTS1's fails (P3-MODE, P5(c), P6) are failures about a simulated ant-like readout, not about ants. They are not proxy fails, and they are not evidence about real ants either way. I disagree with relabeling them as proxy problems. They show that GTAO's √N pooling needs a linear readout, which is a substantive in-model limit.

### 4.11 Summary of the re-audit

| Test | Old label | Gates failed | New label |
|---|---|---|---|
| P1 news recall | KILLED | MV2, MV3, MV5, MV7 | **PROXY-FAIL** (strongest) |
| MATCH1 A1 | KILLED | MV2, MV3, MV6 | **PROXY-FAIL**; weak form PRIOR ART |
| MATCH1 B1 measles | PASSED | MV2, MV3, MV5, MV6, MV7, MV9 | **PROXY-PASS**; substance PRIOR ART (Mayer 2016) |
| VIGIL P1 | PASSED | MV1–MV4, MV7, MV8 | **PROXY-PASS** + PRIOR ART |
| VIGIL P2, P3 | OPEN | as above + κ | **OPEN (proxy null)** |
| VIGIL-2 Enron | KILLED | MV1–MV4, MV6, MV7, MV9 (MV8 passed) | **PROXY-FAIL** |
| LANG1 | KILLED | MV2, MV3, MV7, MV8 | **PROXY-FAIL** (out of domain) |
| τ tests (DECISIVE, F1, C3) | KILLED / mixed | MV2 (most), scope | **PROXY-FAIL**, out of scope for the structural core |
| BIO1 P3a | contradiction | MV2, MV7 | **OPEN** |
| COLLAPSE1 C2, A1 | KILLED | MV1, MV3, MV5, MV6 | **PROXY-FAIL** |
| ANTS1, SENSING2, LAYERS1 locked fails | KILLED (in-model) | n/a (simulation) | **SIM-FAIL** |

**Net position.** There is no FIELD-FAIL and no FIELD-PASS anywhere. In the real world, GTAO's distinctive content is **untested, not refuted.** The in-model mathematics is mostly correct, after the corrections.

---

## 5. Where every quantity can be measured validly: systems ranked by feasibility with public data

Scored 0–3 on: (A) all inputs measurable (MV3); (B) a sampling choice is observable (MV2); (C) a named driver and pool (MV1); (D) a level and a flat comparator (MV4); (E) selection strength measurable (MV8-ii); (F) public data available now. Feasibility rank = the sum, with F weighted ×2 for "today".

| Rank | System | Data (verification) | A | B | C | D | E | F | Total | What it can test validly | Main validity risk |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Designed AI multi-agent systems** with real token or compute prices and agents *not given* the cost function | Generated; LEARNSIM done 15 Nov 2026 (`tests/LEARNSIM/`; CLAIM_MAP G23–G29) | 3 | 3 | 3 | 3 | 3 | 3 | 21 | O1 (level vs member class), O2, T3 signs, V formula, O5 band | External validity is AI-only. It is "nature" only for AI systems |
| 2 | **Public software ecosystems** (GitHub): named upstream drivers, scheduled CI jobs that poll upstream (designed read rates with real compute cost), dependency manifests, org-level shared infrastructure | GitHub API via authenticated `gh` on the box (works; used for this repo). **No pilot pull yet** | 3 | 3 | 3 | 2 | 1 | 3 | 18 | Class gate (a, b) from read rate vs upstream drift and stakes; drift matching; V on named drivers; κ; freeze/hold/lookup (pinned / vendored / floating) | Cron quantization (daily/weekly defaults); copying of templates (weak selection); zero-inflation |
| 3 | **Wikipedia + Wikidata** as an information organization: facts held locally (hardcoded) vs looked up from a shared store (Wikidata or templates) vs frozen | MediaWiki API `prop=wbentityusage`, `list=wblistentityusage` and revision histories [DATA-VERIFIED 15 Nov via mediawiki.org and the Wikibase usage-tracking docs] | 2 | 3 | 3 | 3 | 1 | 3 | 18 | O5 band and its N widening; T3 signs for shared-store adoption; known-groups (birth dates frozen) | Community policy (some wikis restrict Wikidata in infoboxes) dominates cost; volunteer selection |
| 4 | **Influenza and other antigenically variable pathogens + vaccine-update system** (immune and public-health levels) | Bedford et al. 2014 HI data, Dryad doi 10.5061/dryad.rc515 [DATA-VERIFIED 15 Nov]; Antia 2018 and Meeter data [ON BOX]; iReceptor / AIRR Data Commons repertoires [DATA-VERIFIED 15 Nov, search summary] | 2 | 2 | 3 | 1 | 2 | 2 | 14 | Valid drift q (antigenic units per year); freeze vs hold across pathogens; known-groups (measles vs H3N2) | Few pathogens (n ≈ 4–8); costs u, c, h hard to price; prior art (Mayer 2016) |
| 5 | **Bacterial chemotaxis** (cell scale) | Keegstra et al. 2017 single-cell FRET source data (.mat) [DATA-VERIFIED 15 Nov]; Lan 2012, Mattingly 2021 [fetched BIO1] | 2 | 3 | 2 | 0 | 3 | 2 | 14 | Cell-scale sensing class (a, b) and adaptation time vs stimulus statistics; β_phys (physics binding) | No natural "level" or onset; needs designed stimulus statistics for b |
| 6 | **Ant colonies with tracking** | Mersch, Crespi & Keller 2013, Dryad doi 10.5061/dryad.8d8h7 (6 *Camponotus fellah* colonies, 41 days) [DATA-VERIFIED 15 Nov]; Stroeymeyt et al. 2018, Zenodo doi 10.5281/zenodo.1480665 (24.7 GB) [DATA-VERIFIED 15 Nov]; anTraX benchmarks, Zenodo 3740547 [DATA-VERIFIED 15 Nov, search summary] | 1 | 2 | 1 | 1 | 2 | 2 | 11 | Interaction and information-flow structure; candidate levels (nurse vs forager groups); not onset or drift (no environmental manipulation) | No measured drift of a foraging target in these sets; a real test needs a new experiment |
| 7 | **Multilayer ONA surveys** (Krackhardt; Lazega; Cross & Parker) | [ON BOX: uncommitted raw archive; sha256 recorded in `prereg/vigil-ona/SHA256SUMS_raw.txt`] | 1 | 2 | 1 | 1 | 0 | 3 | 11 | Vigilance direction beyond status, with reporting lines (Krackhardt only) | Small (Tier 3); no named driver; no flat comparator |
| 8 | **Multichannel communication data without hierarchy** (Copenhagen Networks Study: calls, SMS, Bluetooth; ~700 students) | figshare 7267433; Sapiezynski et al. 2019 *Sci Data* [DATA-VERIFIED 15 Nov] | 1 | 2 | 0 | 0 | 0 | 3 | 9 | Channel-completeness methodology (how much one channel misses) | No organization or levels |
| 9 | **Cities** (311, open data) | NYC 311 [ON BOX, DRIFT1] | 2 | 1 | 2 | 1 | 0 | 3 | 12 | Drift and κ by nested geography | Levels are political; onset unidentifiable |
| 10 | **Firms with full telemetry** (calendar, meetings, logs) | **Not public.** Bandiera et al. 2020 CEO diaries: journal archive blocked by Cloudflare for the box (VIGIL-2 notes); a browser attempt needs Chad's go. Partner firm needed | 3 | 3 | 3 | 3 | 1 | 0 | 13 | Tier-1 vigilance (FAIR_MEASURE §6) | Access |

**Reading the ranking.** The two best *real-world* (non-designed) systems with public data are (2) software ecosystems and (3) Wikipedia/Wikidata. Both are human information organizations with full telemetry, named drivers, real sampling choices and measurable shared stores. They lack strong selection. Run the selection gate (§3.10) and report only gated results. Cells (5) are the best route to Chad's physics point. The firm-scale Tier-1 vigilance test needs partner data (10).

---

## 6. Fair refutation specifications, one per main prediction (fixed now, before data)

Every spec inherits MV1–MV10 and the admissibility rule (§2.2). A refutation means a Tier-1 failure (a qualifying miss to diagnose, locate, and update from for the class; `process/PROCESS.md`). Tier 2 → DISFAVORED. Tier 3 → logged only.

### 6.1 O1: the level's sensing class sets the onset exponent, e_g = −(1−b_L)/(1−a_L)
- **System.** A designed AI multi-agent system (preferred), or any system scoring ≥ 2 on A–E in §5.
- **Measure first, on separate units.** (a_m, b_m) on flat members; (a_L, b_L) on the level's tracker in isolation (§3.4).
- **Design.** ρ manipulated or observed over ≥ 1.5 decades in the selection-gated range. Arms:
  - (i) level class = member class;
  - (ii) level class ≠ member class: e.g. level A₁ (a = ⅔, b = ⅓; predicted −2) over class-R members (−1 if members set it).
- **Prediction (locked before onset data).** ê_g within ±0.25 of −(1−b̂_L)/(1−â_L) in both arms. In arm (ii), ê_g is closer to the level's value than to the members'.
- **Rivals.** Members' class sets e_g. The exponent is technology-independent (−1 always).
- **Fails if.** In arm (ii) the CI excludes the level's value and includes the members' value; or in both arms the CI excludes −(1−b̂_L)/(1−â_L) by more than 0.25.
- **Power.** SE(ê_g) ≤ 0.35 to separate −1 from −2; SE ≤ 0.18 to separate −1 from −½.

### 6.2 O2: the technology, not the loss shape, sets the exponent under bundled decisions (T4)
- **System.** AI agents (designed loss), or a physical system with a measurably non-quadratic loss.
- **Design.** A bundled loss with p = ½ (absolute) vs p = 2 (quadratic), level re-optimized under each loss (the SENSING2 QUART_R flaw fixed), and the flat-arm bug fixed.
- **Prediction.** ê_g is the same across losses (Δ < 0.15), equal to the technology's quadratic-loss value.
- **Rival.** The lone-member loss exponent (−2 for absolute loss in R1).
- **Fails if.** Δê_g across losses has a CI excluding 0 and including the rival's predicted difference.

### 6.3 O3: vigilance floor, growth and price invariance
As claim map §3.2 and FAIR_MEASURE, plus:
- the class gate on flat units;
- ρ̂ with CI;
- normalization by √q̂_g;
- **κ̂ measured whenever ranks are compared** (§3.9).

- **Prediction.** V_obs ≥ 1 + (1+ρ̂)^{−1/2}.
- **Fails if.** The pooled upper 95% bound of V_obs/(1 + (1+ρ̂)^{−1/2}) is < 0.8. Or V_obs ≤ 1 with a CI excluding 1, in a class with â ≥ b̂.
- **Growth.** The slope of ln V on ln N lies in [â − 0.2, â + 0.2]. Fails if the CI excludes â − 0.2 and includes 0.
- **Price invariance (h ≈ 0 only).** |elasticity of V on p_g/p| < 0.2. Fails if it exceeds 0.2 with a CI excluding 0.

### 6.4 T3: opposite signs of shared and private drift on onset or centralization
- **Design.** A factorial: shared volatility (low/high) × private volatility (low/high), common technology, with ρ in a range where the prize exceeds ε̂.
- **Prediction.** Centralization (level presence, or the share of tracking done by the level) rises with q_g and falls with q_u.
- **Rival.** Contingency theory: a single sign for total volatility.
- **Fails if.** The same sign on both factors with both CIs excluding 0, or the q_u effect positive with a CI excluding 0.
- **Systems.** AI agents (today); lab teams; Wikidata/software observationally (Tier 2).

### 6.5 O4: ordering threshold κ\* = (1−a)/(1−b) (h ≈ 0)
- **Measure.** κ̂ (§3.9) and the level's (â, b̂).
- **Predict.** Top-down filling if κ̂ < κ\*, bottom-up if κ̂ > κ\*. Use systems that grew levels over time (software orgs' infrastructure history; designed AI).
- **Fails if.** Fill order opposite to the prediction in ≥ 2 of 3 systems where |κ̂ − κ\*| > 2 SE.

### 6.6 O5: freeze/hold/lookup band (T8) and its N widening
- **Measure per item.** q (§3.1), μ, u, c, h, H_l and N (users of a shared store).
- **Predict.**
  - Freeze if q < q_f; lookup if q > q_c; hold between.
  - The hold band exists iff μuH_l > 2c + hH_l.
  - For shared stores, band width ∝ N² (or N^{(1−a)/b} in class P(a, b)).
- **Rival.** Mode set by norms or item type, independent of q and N.
- **Fails if.** Classification accuracy of the closed form is no better than an item-type-only model (ΔAUC < 0.02, CI including 0) in a gated sample. Or the band-width elasticity on N has a CI excluding the predicted value and including 0.
- **Systems.** Wikidata vs hardcoded facts; software pinning; AI memory.

### 6.7 Drift matching (refresh rate vs drift; the "√" core)
- **Prediction.** On flat units, the elasticity of effort on drift equals b̂ measured from the technology's price structure (MV5 convergent). For class R, b = 1/(1+2H) with H measured on the same targets (½ only at H = ½; v1.2 correction, THEORY §2.5).
- **Fails if.** The elasticity CI excludes the technology-derived b by > 0.15 in a gated sample.
- **Note.** The √ law is PRIOR ART (EOQ; Lee, Flack & Krakauer 2024). This test calibrates the class gate. It does not test novelty.

### 6.8 N1: √N fade of pooled shared memory (T4 of the older layer)
- **Preconditions (MV2).**
  - Depositors **measured** to be independent (correlation of deposits given the state < 0.2).
  - A target with measured drift q > 0.
  - A **linear** readout, or the readout class measured. ANTS1 shows nonlinear readouts break the N^{−½} error pooling.
- **Prediction.** Optimal fade rate ∝ N^{½} in the small-gain regime (Nq/r ≪ 1, measured).
- **Fails if.** Elasticity CI excludes 0.5 and includes 0, under the preconditions.
- **Systems.** Designed AI shared memories; collaborative documents with measured independent contributors.

### 6.9 New cross-prediction from §3.9: raw sampling rank gradient = a − κb [DERIVED HERE]
- **Measure (before opening any sampling data).** κ̂ from a hierarchical variance decomposition of the drivers at each scope; (â, b̂) from the class gate.
- **Prediction.** The elasticity of the raw read rate on scope size is â − κ̂b̂, within ±0.15.
- **Fails if.** The CI excludes â − κ̂b̂ and includes the κ = 0 value â (or vice versa).
- **Why it matters.** It turns the Enron/PIAAC-type rank comparison into a valid test. It also tests the T7 ordering logic through a second observable.

### 6.10 Spectrum → exponent (N4/N6) and layers
**Precondition:** first derive the mapping from a measured spectrum to the predicted memory exponent. MATCH1 D3's sign came out opposite, so this is owed before any lock. Until then, nothing in N6 can be fairly refuted or passed. **OPEN.**
*Update (18 Nov 2026 audit):* the precondition is now met. THEORY v1.4 §2.2 derives the spectrum → exponent map by regime (classical; CLAIM_MAP K12/K13 MATH-CORRECTED), and MATCH1 D3's opposite sign was a mis-derived prediction (CLAIM_MAP H19 MATH-CORRECTED). What stays open is measured-input optimality on one system (CLAIM_MAP N13 OPEN; THEORY §1 N6), first tested by SAME-SYSTEM-AQN.

---

## 7. The three decisive, validly measurable tests to run next (today)

*Update (18 Nov 2026 audit):* this list is from 15 Nov. Exploratory versions of #2 and #3 have since run and failed gates: GITHUB-UPSTREAM (CLAIM_MAP N14 PROXY-FAIL → NOT A TEST (qualification not established; proxy: failed), Tier 3; N15 OPEN) and WIKIDATA-BAND (N19 OPEN, known-groups check failed; N20 PROXY-PASS → NOT A TEST (qualification not established; proxy: passed), historically weak). Reruns count only if they pass MV1–MV8. No Tier-1 test has run anywhere. The current first test is SAME-SYSTEM-AQN (`reviews/night2/SYNTHESIS_2026-11-15.md` §7; `process/QUEUE.md`).

1. **The mixed-technology onset test in agents not given the cost function** (§6.1, plus §6.4 as a second factorial arm). This is the only test where every quantity passes MV1–MV8 today. It discriminates O1 (level's class sets e_g) from the members-set and technology-independent rivals, which SENSING2 never ran cleanly.
   - Build on `tests/LEARNSIM/`. Make sure it has a level ≠ member arm (e.g. A₁ level over R members), (a_L, b_L) measured on the level alone before onset is fitted, real per-call costs, and a gated ρ range.
   - Feasibility: high; LEARNSIM (done 15 Nov 2026, `tests/LEARNSIM/`) is the starting point.
2. **The GitHub named-driver read-rate test: class gate → drift matching → κ → V** (§3.4, §6.7, §6.9, §6.3). This is the first real-world measurement of (a, b) anywhere.
   - **Units**: repositories that depend on a named upstream (e.g. a major scientific-Python library).
   - **Effort**: scheduled CI runs that test against the upstream's development branch. Cron frequency is a designed read rate with real compute cost.
   - **Drift**: the upstream's breaking-change rate (release notes, API diffs).
   - **Stakes**: dependents or downloads.
   - **Level**: shared downstream-testing infrastructure that polls the upstream for many packages.
   - Fit (a, b) on flat repos, then predict V and the rank gradient. Run a pilot pull first to check zero-inflation and cron quantization.
   - Feasibility: medium-high (public, authenticated `gh` works); no pilot yet.
3. **The Wikidata freeze/hold/lookup band and shared-store onset** (§6.6, with T3 signs observationally).
   - **Items**: fact types (properties).
   - **Drift**: value-change rate from Wikidata histories.
   - **N**: pages using the entity (`wblistentityusage`).
   - **Mode**: lookup = a statement-usage aspect on the page; hold = a hardcoded value edited during the page's life; freeze = a hardcoded value never edited.
   - **Known-groups**: birth dates must come out frozen.
   - **Replication**: across ≥ 2 language editions with different Wikidata norms (the discriminant check against policy).
   - Feasibility: high (public API).

Fourth (the physics route Chad cares about): measure β_phys and the class (a, b) for *E. coli* chemotaxis from Keegstra 2017 source data plus the Lan 2012 energy–speed–accuracy relation. If the cell sits near its thermodynamic floor and its class is the one that floor selects, that is the first place GTAO's physics does work. It is lower feasibility today (data parsing, plus a derivation still owed).

The vigilance ONA test run in `prereg/vigil-ona/` (finished; CLAIM_MAP N1–N3) is Tier 3 by its own preregistration. It cannot change vigilance's status. It is useful as a dry run of the status and channel controls.

---

## 8. Limits of this document
- Written by one executor in well under an hour of drafting, on top of the night-1 files. It is **not independently reviewed.** Several mappings in §3 are marked as hypotheses and need their own validity checks.
- The §3.9 derivation is elementary, and the numerical check is in `checks/`. It has not been checked by the math referee.
- The heuristic "κ ≈ 1 for aggregated sub-components" is a heuristic, not a theorem.
- Dataset verifications are existence checks (landing pages or search summaries). Nothing in §5 was downloaded except where marked [ON BOX].
- This file relabels; it does not re-run any test. Every number quoted is from the cited project files.
- Updated 18 Nov 2026 (consistency audit): gates binding (§2.2, CLAIM_MAP M2), scope per Chad t1927 (§1.2 item 4), §6.10 and §7 status notes. Re-audit result unchanged: no FIELD-PASS and no FIELD-FAIL; the theory is untested in the field, not refuted.
- External timestamping of future locks (MV9) still needs Chad's explicit go.

## 9. Preregistered refutation conditions for the hypothesis (added 20 Nov 2026, v2.4; written by one executor after the independent review of v2.3 found the hypothesis "well protected in practice"; not independently reviewed)

THEORY §3 defines *strongly selected* and the refutation conditions; this section is the protocol. **Nothing here is a lock yet:** a lock happens when a named test is registered with a timestamp (MV9 still needs Chad's go).

1. **Qualifying (decide before any measurement; all five, with the evidence recorded).** (a) A cost-to-fitness map σ (fractional change in growth, survival or reproduction rate per fractional change in J) with its source. (b) A population proxy N_e (independent lineages competing in the same world per redesign time); cities, nation-states, global economies and the biosphere are excluded until a class-specific proxy is preregistered. (c) The selection-resolvable band ε = 10/(σ·N_e) (the drift barrier is s·N_e ≈ 1, Lynch et al. 2016; the factor of 10 above it is a conservative choice made here); the prediction band is at least ε wide, so a worse measurement cannot make qualification easier. (d) Power: the band plus measurement error excludes the design of at least one named rival (item 6). (e) A redesign time T_red, the time to close 1 − 1/e of the gap to the new argmin J after a step change in the prices or in the world's statistics (measured, or preregistered from the class's turnover), with at least 10 T_red of the same world (N54 is the longer record a redesign learns from). A class that fails any item is excluded and is not evidence either way. Drift-limited misses are excluded this way before the test, never invoked after it.
2. **Closed term list (per substrate).** List J's cost terms for the substrate (memory, upkeep, error stake, acquisition, link, telling, lookup, ruin) and price each independently of the design predicted (no price fitted to the design). A cost found after the test that is not on the list counts as a miss unless it was added publicly, with a date, before the test on that class.
3. **Inputs, measured once.** The world's drift spectrum and sensing noise, the prices, and the stakes (or the stake-free form: elasticity 1/α in drift, N51) from data independent of the design; re-measure once if a validity gate fails, before the comparison. After the comparison nothing is re-measured.
4. **Prediction with a band.** argmin J (layers counted by degree, memories, read rates) with an error band propagated from the input errors (CT23 gives second-order regret for picture errors; near cliffs the band is wider). The band is defined in J and converted to design units: {𝒟 : J(𝒟) ≤ (1 + ε + δ_meas)·J*}, with J flat at its minimum so a fractional gap ε allows about √(2εJ*/H_ii) in each continuous design variable (≈ √ε); the class preregisters the band in design units from its own J (THEORY §3).
5. **Verdict.** Misses outside the band in qualifying systems refute the hypothesis for that substrate class once they exceed the binomial allowance fixed by the preregistered coverage and minimum number of systems (item 7); for a small class that is one miss. A design that fails to move with a measured change in its inputs, by the preregistered share, counts as a miss, unless the post-change gap is inside the redesign band at the lower bound of the class's preregistered redesign cost (CT41, `theory/DYNAMICS.md` §2). A band exists only where adjustment is lumpy, and only if the class preregisters, before data, the redesign cost on the closed term list (point estimate and error budget, measured independently of the design), the curvature w, the input-process type (step or drift) and T or σ_d. A gap between the bands at the cost's lower and upper bounds is INDETERMINATE. If the band at the upper bound covers the predicted move, the move test is NOT A TEST. Without these preregistered quantities the band is zero and the rule is unchanged. (Amended 20 Nov 2026, CLAIM_MAP v2.67, revised the same day after independent review of PR #117 so that only the cost's lower bound excuses a non-move.) Each class also preregisters its objective (per-unit J or lineage growth, CT42) and whether its stakes are additive or compounding (CT43). Misses in two classes at different scales refute it as a cross-scale hypothesis. A pass supports it only if the minimum also beats a named rival (a fixed budget share; a universal exponent of ½) under the same error budget.
6. **Named rivals and error budget.** Rivals: (R1) design equals a fixed share of budget; (R2) every read interval ∝ the world's time scale with exponent ½; (R3) design equals the world's time scales with no price dependence. Error budget: the propagated input error from item 4 plus the interpolation error of the estimator (`measurement/estimators/RESULTS.md`).
7. **Coverage and number of systems (preregistered per class).** The band's coverage c (the probability the band contains the design the cost implies, given measurement error; for example 99%), the minimum number n_min of qualifying systems (all tested and reported; a class below n_min is excluded and not evidence either way) and a significance level α, all fixed before any measurement. The class is refuted when the number of misses m satisfies P(Bin(n, 1 − c) ≥ m) < α. For a small class this can be one miss (c = 99.9%, n ≤ 10, α = 1%: one miss has chance probability about 1%). The "two classes" rule for refutation across scales is unchanged.
8. **Counting layers in a real system (placeholder; to be finalized per class before any test).** Count the distinct measured memory time constants (filter poles) of the system's estimated input–output response, by degree (a rhythm counts two), with a preregistered model-selection criterion; count only what that rule returns; never recount after a miss. Not yet written for any class.
