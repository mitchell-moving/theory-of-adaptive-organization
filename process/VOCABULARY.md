# VOCABULARY: what we mean by memory, record, model, layer, level, nesting, scale, fractal and swarm

*Tuesday 24 November 2026 (America/New_York). Proposed maintained vocabulary, in the same spirit as the miss vocabulary in [`PROCESS.md`](PROCESS.md). It fixes words, not results: it adds no theorem, changes no status, and leaves `THEORY.md` untouched (`THEORY.md` governs wherever it differs; see section 4). Applies to new and maintained text. Historical files, locked preregistrations and dated notes keep their wording.*

> **The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

**Labels.** **DECIDED** is a naming decision, not a claim about the world (the CLAIM_MAP status of N30). **PROVED (in-model)**, **KNOWN**, **CONJECTURE**, **OPEN**, **INTERPRETATION**, **FAILS**, **SIM-FAIL** are used as in `CORE.md:169`, `theory/SWARM_RULE_2026-11-23.md:7` and the CLAIM_MAP. Each entry says which words are the decision and which are the cited results.

**Scope.** Nothing here says anything about experience or consciousness. That question is parked (`theory/IIT_PATH_2026-11-23.md`; `OPEN_WORK.md:107`, T56: "Open (exploration path, not a result)"). "A person is a model of their world" is an INTERPRETATION, not a measured result (entry 3).

## 1. Memory

**Definition (DECIDED).** The *memory* is the store a system acts from, written \(M_t\). The amount held is \(I_{\mathrm{mem}}\), in nats. The word is the theory's canonical noun for the store and for the cost coordinate.

**Test.** Estimate the mutual information between the store and the world. Zero means no memory in this sense.

**Status.** That the cost's memory coordinate is mutual information, for a system meeting A1–A7: **PROVED (in-model)** (Theorem R1; it does not choose the coordinate list, and the quantum case is not covered).

**Cites.** `THEORY.md:208` (Agent: a memory \(M_t\) updated from observations), `THEORY.md:220` and `:245` (symbols), `CORE.md:52` (R1, A6), `theory/QUANTUM_RECORD_PRICE_2026-11-24.md:27` (both named coordinates are classical).

**Say / don't say.** Say "memory" for the whole store and for \(I_{\mathrm{mem}}\). Do not use it for "answering from memory" in process text; say "without opening the file".

## 2. Record

**Definition (DECIDED).** A *record* is one stored state whose content is correlated with the world and can be read later. A memory is what a system holds and acts from; records are the items in it. A record is a correlation that can be read. It is not yet a model (entry 3).

**Test.** Can a reader, later, recover something about the world from the state better than chance? That is the "Correlation" row of the four notions of knowing (`theory/BOOKENDS.md:125`: \(I(M;X)>0\), "none needed; nearly universal").

**Cost (cited results, not new).**
- Acquiring or erasing a nat by a measuring tracker costs at least \(kT\) (**KNOWN**, Landauer 1961; `THEORY.md:36`), and the freeze-or-hold note prices a record's one-time write at that floor (`theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md:101`). A Landauer cost per irreversible reset as a steady floor is **OPEN** there (`:105`).
- In a frozen or disconnected world a static record can beat a no-memory guess at vanishing ongoing memory-bath heat after the one-time write (**PROVED (in-model)** in the named classes, T57, T59, T60; T59 is on main after independent review, `OPEN_WORK.md:110`; passive retention over a horizon short against the leak time, `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md:103`). In the words of `CORE.md:78`: "Storage is cheap. Tracking a changing, connected world is what costs."
- Keeping a record current against a changing, connected world costs heat of at least \(kT\) times the net learning rate (`CORE.md:70`): **KNOWN** for bipartite jump processes, **PROVED (in-model)** for additive-noise diffusions, open beyond those classes. When the memory also steers the world, the thermodynamic step still holds but the exogenous floor is not inherited (`CORE.md:80`).

**Example.** A crystal's isotope ratios are a frozen record of its formation. It is memory in the theory's sense with keeping cost 0, and it is not a model (`theory/SCALE_ENDS.md:106`).

**Say / don't say.** Say "record" for the stored, readable item. For a time series write "data series" or "observation record" (legacy uses: `THEORY.md:166`, `:470`). For documentation write "the repository history" or "the published record". Say "quantum record price" only as the open row T74, which names no unique price (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md:9`).

## 3. Model

**Definition (DECIDED, already decided as N30).** A *model* is a held structure, in a system with something at stake, that contains the dynamics of an outside variable bearing on the system's own persistence and regulates against it by error feedback. It is built from records and is more than a record. The minimal case is integral feedback, the model of a constant or step world. A structure that tracks a variable with nothing at stake is a *regulator without stakes*, outside the theory's sense of knowing (`theory/BOOKENDS.md:127`, CLAIM_MAP N30).

**Test (the repo's own).** BK-SEM: scramble the state–drive correlation at fixed fluxes and viability must drop (the survival-relevant step). BK-IMP, all three parts: return to the prior value after a sustained step, robustness to parameter change, and a structural check that the integrated quantity is the error (BK-SEM at `theory/BOOKENDS.md:126`, BK-IMP at `:127`). Flames, dunes and hurricanes are expected not to meet (a) (`theory/BOOKENDS.md:204`).

**Why predictive correlation alone is not enough.** A driven system that retains predictive information has a correlation, and that is nearly universal (`theory/BOOKENDS.md:125`). A star is held but carries no model (`theory/SCALE_ENDS.md:83`).

**The cost reading, with its limits.**
- Memory beyond the predictive part pays heat for nothing predictive: at least \(kT(I_{\mathrm{mem}}-I_{\mathrm{pred}})\) (**KNOWN**: Landauer 1961, Still et al. 2012; `THEORY.md:36`).
- For a forecaster scored by log-loss, the miss of a memory equals the predictive information it fails to carry, and a memory with near-zero shortfall must nearly copy the world's causal state, with dynamics near a homomorphism of the world's, when the causal states are separated (\(\gamma_L>0\)) (CL10, `THEORY.md:408`, `theory/INTERNAL_MODEL.md:110-123`): The square-root bound is often vacuous at realistic misses (`theory/INTERNAL_MODEL.md:28-31`). **PROVED (in-model)**, self-checked, parts probably folklore (Shalizi and Crutchfield at zero shortfall).
- What is forced is only what decisions use. Under Hamming loss on the Even process a memoryless agent that always says "1" is exactly optimal. Only log-loss, or another strictly proper score, forces the full causal state. History length is the wrong measure of a model (`theory/INTERNAL_MODEL.md:32`: **FAILS** for general losses).
- So the working paraphrase "a model is the cheapest record that still gets the decisions right" is a *reading* of these results at the minimum of the cost. It holds inside the proved classes, and only for a system that meets the stakes and error-feedback conditions in the definition above; a copy of the causal state with nothing at stake is a regulator without stakes. That real systems sit at that minimum is Part 2 of the theory and is untested. Do not shorten it to "the cheapest record that predicts".

**A person.** "A person is a model of their world" is an INTERPRETATION. Cells and every level above are the *candidate* held models, and earlier cases are OPEN (`theory/SCALE_ENDS.md:78`). Nothing here speaks to experience.

**Say / don't say.** In new text bare "model" means this entry. For the theory's mathematical setting write "in-model" or "model class" (the label PROVED (in-model)). For code that imitates a world write "simulator". In the miss ledger, `location: model` means the in-model math or a Part-2 prediction (`PROCESS.md` §1 item 6). That is a third use, and the column name stays as is. `theory/INTERNAL_MODEL.md` and CL10 use 'model' for the memory's decoded state ('P(model ≠ world's causal state)'). In new text write 'decoded state' or 'internal-model bound'; that result is about a memory, not about entry 3's model.

## 4. Layer, store, level and tracker

**Definitions (DECIDED, taken from `THEORY.md`).**
- A *tracker* is a memory that is updated to follow a changing world (`THEORY.md:208` for the memory; CT7, `:295`, for its use as a tracker).
- A *layer* is "a tracking store, not an org-chart level" (`THEORY.md:67`). It is the general word. \(K\) counts layers by degree, so a rhythm counts two (CT21, `THEORY.md:180` and `:245`).
- A *store* is a layer on the time axis, and a *level* is a layer on the member axis, one shared tracker for the members that face a common driver: "stores lie across time scales and levels across members" (`THEORY.md:123`).

**Test.** Name the axis. A time-axis layer is told apart by a separate time scale in the world's spectrum. A level is told apart by a shared driver and members that pay to share one tracker (CT14).

**Status.** Layer count by degree: **PROVED (in-model)** in the linear-Gaussian, squared-error class (CT21; CLAIM_MAP: not yet independently reviewed). Levels of a nested tree fill from the broadest scope down iff \(\chi<\chi^*=(1-a)/(1-b)\): **PROVED (in-model)** (CL15, `THEORY.md:123`). The word "layer" still covers four things in the audit: a first-order store, a McMillan degree, an org-chart level and a lumpy reset (`theory/MATH_COMPLETENESS_AUDIT.md:114`). The degree count is not the count of separate stores one would build (`core/KEYSTONE_NOTE.md:37`). Whether layers must be separate agents or can be stores inside one agent is OPEN (`THEORY.md:180`).

**Say / don't say.** Never use "level" for an org-chart rank without the words "org-chart". "Drift level" (\(q\), `THEORY.md:207`) is a defined quantity, not an organizational level. A *group* of agents is not a layer unless it shares one tracker.

## 5. Nesting (three different things)

1. **Cost nesting (CT34), PROVED (in-model).** For parent design \(x\) and team design \(y\): \(\min_{x,y}J=\min_x[F(x)+J^*_T(\theta(x))]\), exactly, where \(\theta\) is what the parent passes down (`THEORY.md:497`). The team's optimized cost is a constant upkeep \(h\) if \(\theta\) does not depend on \(x\) (generically only if). Otherwise it is a value function of \(\theta(x)\), still exact. The *stated error* applies only if the team is frozen at its stand-alone optimum under weak coupling: at most \((\varepsilon L)^2/(2\mu)\), second order in \(\varepsilon\). A shared driver is not weak coupling. **CONJECTURE, not shown:** that real teams coarse-grain to one member with upkeep \(J^*_T\) (`THEORY.md:125`). The dyadic renormalization analogue is BROKEN as preregistered and that "does not settle CT34" (T69, `OPEN_WORK.md:120`).
2. **Nested versus flat layers.** "Nested beats flat" is not one theorem: **[PROOF for (a), KNOWN for (b), NUMERIC for (c); no general theorem]** (`theory/THEOREMS.md:60-62`, `:111`). Decoupled nesting loses to flat when time scales collapse (T3c).
3. **A nested tree of members.** The CL15 result in entry 4.

**Say / don't say.** Write "cost nesting" for 1, "nested versus flat" for 2, "nested tree" for 3. Never say "everything nests" or "problems nest" without naming CT34 and its conditions.

## 6. Scale

*Scale* is used in four ways: size or organizational scale ("at every scale"), time scale, scale-free (self-similar), and a numerical scale ("one positive scale" in R1; the shock scale \(\sigma\)). In new text say **time scale**, **size** (or, with a defined term, level), **self-similar** and **units** or **numerical scale** for those four.

**What "the same at every scale" does mean (DECIDED wording; results as cited).** The same cost and the same method are used at every scale. In each system's own units the equation is one problem: only dimensionless ratios matter (`THEORY.md:36`). Cost shares equal price elasticities and are currency-free when the feasible set does not depend on the prices, and a binding ruin cap is a counterexample (CT24, **PROVED (in-model)**). Covariance under rescaling holds in the stated class (S1–S3) and fails when two cost components scale differently with size (S4); that real systems sit in the generic class is a **CONJECTURE** (`THEORY.md:418-420`).

**What it does not mean.** It does not say the *design* is the same at every scale. That depends on the world (entry 7).

## 7. Fractal and self-similar

**Definition (DECIDED).** *Self-similar* describes an input, a world whose change repeats its statistics across a band of time scales. The theory does not say physical time is fractal: that framing is withdrawn (`THEORY.md:189`, N46 **WITHDRAWN** as framing, `measurement/CLAIM_MAP_v2.md:484`).

**Test.** Measure whether the world the system tracks changes self-similarly over a band. If it does, the layers come out roughly log-spaced (`THEORY.md:189`).

**Status.**
- Self-similar world and power-law costs give a self-similar optimal architecture: **PROVED (in-model)** as a conditional, close to a tautology (T7b, `theory/THEOREMS.md:175-204`). "The architecture is fractal" is not a theorem (`theory/THEOREMS.md:17`). The CLAIM_MAP status of CL16 is MATH-CORRECTED.
- A scaling of the heat floor with fractal dimension **FAILS** in the checked class: on the locked Sierpiński gasket and carpet the heat floor follows the sites the decision names and the degree sum, not the Hausdorff or spectral dimension. This is a self-check, not an independent review, in one class (`theory/FRACTAL_WORLD_2026-11-22.md:5`, `OPEN_WORK.md:105`, T54).
- Geometric spacing of layers that holds across spans: LAYERS1 P2 is **SIM-FAIL** (6 of 12), and geometric levels are proved only in T7b's shared-clock model (`theory/LAYERS.md:21`, `measurement/CLAIM_MAP_v2.md:317`).

**Say / don't say.** Say "self-similar world" for the input. Never say "the theory says time is fractal", "the universe is fractal" or "everything is the same at every level".

## 8. Swarm

**Definition (DECIDED).** A *swarm* is any whole whose parts can come together, stay, leave and regroup: cells in a tissue, agents in an organization, people in a firm, ants on a trail (`theory/SWARM_RULE_2026-11-23.md:11`). *The swarm rule* is the seven-clause life cycle of that membership (`theory/SWARM_RULE_2026-11-23.md:40-50`): join, stay (\(\pi_i<1\)), leave or tamper, align (\(s_i=w_i/W\)), reintegrate, re-form, remove or reprice. It is "a use of the cost of judgment", not a separate principle and not a statement of self-similarity.

**Test.** Check the stay condition \(\lambda s c<w\Phi\) with measured inputs. \(\lambda, s, c, w\) and \(\Phi\) are MEASUREMENTS (`theory/SWARM_RULE_2026-11-23.md:17-36`).

**Status.** Onset, stay, leave, align and the re-form band are **PROVED (in-model)** in their named classes. Reintegrate is an identity on stay plus a property of the memoryless class (`theory/SWARM_RULE_2026-11-23.md:52`). Merging and remove-or-reprice are **CONJECTURE** (T53). Every reading onto cells, agents, people or bacteria is **INTERPRETATION**. That real parts minimize this cost is the hypothesis, untested there (`theory/SWARM_RULE_2026-11-23.md:52`). *The swarm limit* (\(k\to0\), groups re-form continuously) is an ANALOGY, not a theorem (`theory/FLUID_LAYERS_2026-11-21.md:11`, `theory/GENERALITY_2026-11-22.md:285`).

**Say / don't say.** Do not say "the swarm principle". Say "the swarm rule" for the membership life cycle. Do not use "swarm" for the claim that levels repeat the same pattern (entries 6 and 7).

## 9. State (a collision to avoid)

*State* is the world's state \(X_t\) in `THEORY.md:207` and `:220`. The memory is \(M_t\). `theory/INTERNAL_MODEL.md` also says "the agent's state". In new text, say **world state** for \(X_t\), **memory** for \(M_t\), and keep **causal state** as the computational-mechanics term (**KNOWN**; `theory/INTERNAL_MODEL.md:110`). In that file, "miss" means the forecast shortfall \(\delta\), an unsigned predictive information in nats (`THEORY.md:408`). In new text write **predictive shortfall** for it, and keep **miss** for the signed gap between a locked prediction and its outcome (`PROCESS.md` §1 item 1).

## 10. Wording rules that still apply

Say **theory**, never "theory of everything". Use "law" only inside the hypothesis sentence or in a prior-art or physics name. Never say "solved". Say **cost**, not "bill". Call a prediction error a **miss**. The gate statuses (`PROXY-FAIL`, `SIM-FAIL`, `NOT A TEST`, `INCONCLUSIVE`, `FIELD-FAIL`) stay as gate classifications (`PROCESS.md` §2).
