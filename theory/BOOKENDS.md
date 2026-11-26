# BOOKENDS: how the pieces of GTAO fit together, from chemistry to heat death, and what follows at each level *if* the theory is right

**Revision 3.** Wednesday 18 November 2026, evening ET (America/New_York). Revision 2 was written earlier the same evening, revision 1 before it. Written by a Grok Bot executor for Chad Mitchell, via Ace, on branch `bookends` (Chad, t1943, t1944, t1945, t1946). Nothing was posted or sent.

**What revision 3 changes.** Round 2 of the same three reviews (all PASS-WITH-FIXES) is fixed item by item: math R2-1…R2-7, physics R2-1…R2-7, bio R2-1…R2-5 and the low items. The main changes:
- The finite-horizon bound now states its conditional-mean condition and a mixing-time caveat; the Markov case stays OPEN.
- CM-N26's PROVED (in-model) scope is limited to pre-Page-time holes.
- K2 needs a model of the entity's *own* ruin variable; otherwise the structure is a **regulator without stakes**.
- BK-IMP adds a robustness-to-parameters check and a structural check.
- BK-G2 is redesigned again: the droplet entrains chemically, and light only scrambles.
- Shared fate is partial (scaled by relatedness r).
- BK-P4 gets a third kill.

**The proposals (§6) are applied in this same PR** to THEORY.md, `theory/SCALE_ENDS.md`, `theory/THEOREMS.md`, CLAIM_MAP, litmap and the checker. §6 records what was applied where.

**What revision 2 changed.** Three independent reviews of revision 1 were held outside the repo at the time; their reports (and the later rounds) are now in `reviews/bookends/`:
- MATH_LOGIC: FAIL, fixable;
- PHYSICS: PASS-WITH-FIXES;
- BIO_PRIORART: PASS-WITH-FIXES.

Every blocker, major and high finding is addressed here. The disposition, finding by finding, is kept with the reviews. The main changes:
1. "Response" and "action" are now separate terms (§2.0).
2. The pre-heredity tier is now *survival-relevant (semantic) information*, not a "model". It has an explicit test that flames, dunes, hurricanes and galaxies are expected to fail.
3. "Model" now means the internal-model-principle sense: proportional feedback holds no model, and integral feedback is the minimal one.
4. Theorem P gets a finite-horizon form and an explicit mapping lemma.
5. The onset order is a HYPOTHESIS.
6. The physics corrections: the second law is the backbone but not the only principle; Landauer applies to erasure; galaxies, hurricanes and the carbonate–silicate cycle are reclassified; black-hole read delay follows Hayden & Preskill; light delay is a latency cost on Earth and a hard cap off-planet.
7. The planet's information sits in the biosphere; humans make Earth forecast ahead.
8. Credit is restored for "shared fate" and for missing prior art.
9. The proposals are renamed BK-P1…BK-P14.

**Status of this file.** This is a derivation and synthesis file. Its proposals (§6) were reviewed in two rounds and are **applied in the canonical files in the same PR** (Chad delegated theory decisions at t1927). Its own synthesis passed two rounds of independent review with fixes; the round-3 edits themselves have not been re-reviewed, and the file is not self-certified. If it disagrees with THEORY.md, THEORY.md governs.

**What kind of claim.** GTAO is a falsifiable causal theory. It is not a "law" and not a theory of everything. In the field it is **untested, not refuted** (FRAMEWORK §2.3; no row has FIELD-PASS or FIELD-FAIL).

**Labels.**
- **PROVED (in-model):** a CLAIM_MAP theorem inside the model. It says nothing about nature by itself.
- **DERIVED:** follows from the theory's own results plus stated mappings or published physics. Where the derivation is new here, it is marked **[BK, new]** and was reviewed in two rounds unless marked unreviewed.
- **PRIOR ART:** published by others and credited.
- **HYPOTHESIS:** a real-system claim with a stated kill.
- **OPEN:** not settled.
- **IMPOSTER:** sounds like it follows from GTAO but does not. Rejected.
- **ANALOGY:** a borrowed formula whose premises do not hold, used for direction only.
- **CLASSIFICATION (not a prediction):** a placement that no data could fail.
- Labels quoted from a source file are kept exactly as that file states them: PROOF, KNOWN, NUMERIC, ELEMENTARY, FAILS, CONJECTURE, PROOF + NUMERIC, MATH-CORRECTED, WITHDRAWN.

**Identifiers.** IDs are prefixed with their file: SE- for SCALE_ENDS (SE-E1…SE-E4, SE9), GT- for GENERAL_THEOREM (GT-P0…GT-P3), IM- for INTERNAL_MODEL (IM-I5), CM- for CLAIM_MAP rows (CM-N25, CM-H8), TH- for `theory/THEOREMS.md` (TH-T3a, TH-T7), and H- for the local hypothesis file. This file's own items are BK-….

**Sources read.**
- Repo: THEORY.md v1.4.19 (status block, §0, §2.1–§2.3, §3–§7, §10); `theory/SCALE_ENDS.md` (all); `theory/GENERAL_THEOREM.md` §0–§2 and §5; `reviews/night1/formal/AXIOMS.md`; `theory/THEOREMS.md` T3 and T7; `theory/MATH_ATTACK.md` §3.2–§3.6; `measurement/CLAIM_MAP_v2.md` (rows cited); `measurement/FRAMEWORK.md` §1, §2, §3.10, §3.11; `BRIEF.md` (now [`history/2026-11-18_BRIEF.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-18_BRIEF.md)); `litmap/LITMAP.md`, `PRIOR_ART.md`, `THREATS.md`.
- Local: the hypothesis files (H1, H2, H8, H9, H37, H80, and C13 in the reviewed core file). No personal content is reproduced.
- The 12 Nov X post supplies the spine.
- Primary sources opened by this author are listed under References. Each is marked "abstract", "page" or "metadata only".

---

## 0. Bottom line

1. **The spine.** Everything obeys the second law: total entropy rises, though local order can grow when it exports entropy. That law, together with gravity, the speed of light, quantum physics, conservation laws, and the universe's unusually low-entropy start, sets the stage. GTAO adds no new physics. Its content is about **judgment under the second law**. Some structures last only by running free energy through themselves while staying matched to a world that changes and can ruin them. For those, once acting late is costly, carrying a model and acting ahead can pay (12 Nov post; GT §1: "k > 0 is acting late is costly").
2. **Four separate things, not one word "model".** This file separates:
   - (a) **correlation**: any mutual information with the world, which nearly every driven system has (Still et al. 2012);
   - (b) **survival-relevant (semantic) information**: correlation whose scrambling shortens persistence (Kolchinsky & Wolpert 2018);
   - (c) **a model** in the internal-model-principle sense: error feedback that contains the dynamics of the outside signal, regulating something the structure's own survival depends on. Integral feedback is the minimal case, the model of a constant world (Francis & Wonham 1976; Barkai & Leibler 1997; Yi et al. 2000 for bacterial chemotaxis). Proportional feedback holds none. The same structure with nothing at stake is a *regulator without stakes*, not a knower;
   - (d) **a selected model**: (c) whose design is shaped by selection (Axiom 7), which is where GTAO's design predictions live.

   Revision 1 blurred (a), (b) and (c). That blur is why it made flames and hurricanes look like "models".
3. **Corrections to the chat.**
   - "Models start at cells" was **wrong**. Selected models switch on with heredity below Eigen's threshold, which is below the cell (CM-N28 OPEN). Survival-relevant information, and even integral-feedback structure, are not excluded before heredity.
   - "Feedback isn't a model" was **wrong as stated**. Integral feedback on an outside variable is the minimal model. Proportional feedback, and feedback on one's own state, are not models of the world in this file's definitions. Excluding self-feedback is a **definitional choice**: Rosen 1985 counts "a predictive model of itself and/or its environment" (litmap).
   - "A planet would need selection between versions to have a model" was **wrong as stated**. Selection is needed for a *selected* model (Axiom 7), not for (b) or (c).
4. **The onset of knowing is graded and only partly ordered (HYPOTHESIS).** Correlation, survival-relevant information, minimal models, heredity and acting ahead are separately measurable. They need not arrive in that order: an entrained oscillator may be able to act ahead (phase lead) without heredity, which is untested (BK-G2).
5. **Frozen memory has a job.** Knowers are built from frozen structures, inherit through near-frozen stores (genomes: low-upkeep, repaired, updated across generations), read frozen records, and spend upkeep only on what drifts (the freeze edge of the T8 band; CM-F13 PROVED (in-model)). Black holes are the limit of keeping and predict nothing (CM-N26 PROVED (in-model), conditional; scope narrowed to pre-Page-time holes, §2.0.4). Most of the entropy now present in the observable universe is in supermassive black holes (Egan & Lineweaver 2010).
6. **Layers and governance follow from the same spine (§3).** A level is a shared model of a common driver (TH-T3a: PROOF, sufficient condition only). Architecture is self-similar when the world is scale-free and costs and loss are too (TH-T7: PROOF (conditional) of that direction; the converse is not proved, and the "iff scale-free" layering claim is withdrawn, THEORY §1 N4, v1.4.27; unconditional claim FAILS). Parts under-watch when failure costs do not reach them (MATH_ATTACK §3.4, PROOF). That is cured by **shared fate or enforcement** (CM-J9 stays OPEN). Signal delay forces federation, and light delay is a latency cost on Earth and the hard floor off-planet (CM-N27 OPEN), unless shortcuts faster than light exist, which the theory does not predict (`WORMHOLES.md` §4b: a finite throat network keeps the bound at a faster speed; open throats remove it).
7. **Planets and consciousness.** Earth's information sits in its biosphere, not its rock. Since humans, part of it forecasts ahead (climate models, asteroid tracking). GTAO has no variable for experience, so "GTAO shows a planet is or is not conscious" is an **IMPOSTER** claim. The question itself is out of scope.
8. **Status changes.** No status label in CLAIM_MAP changes. Three rows change their wording or stated conditions: CM-N25 (a note), CM-N26 (its PROVED (in-model) scope narrows to pre-Page-time holes; post-Page holes are stated outside that scope, conditional on a conjecture) and CM-N28 ("*selected* models"). §2.0.4 shows why the labels survive.
9. **Repo inconsistencies flagged (three; all fixed in this PR, §6).**
   - SCALE_ENDS labels its no-model class "H80's thermostat tier", though H80's thermostat tier tracks an outside target.
   - SCALE_ENDS and THEORY say "models switch on only with heredity" while Theorem P carries no selection premise. Under the Axiom-7 reading of "action" this is consistent, but the wording hides the choice (MATH_LOGIC's verdict, accepted).
   - `theory/THEOREMS.md` T7(iii) keeps the withdrawn L^{2/3} level count, where L is the log-span.

   Two smaller ones: THEORY §6 cited MATH_ATTACK "§3.5" for under-watching, but the result is in §3.4 (fixed, BK-P10). GENERAL_THEOREM defines z = σ√τ/B, the inverse of THEORY's z = B/(σ√τ) (not a proposal here; left as a note).

---

## 1. The picture in plain words

Everything runs downhill. Fuel burns, heat spreads, and the total disorder of the universe goes up. That is the second law. It does not mean order can't grow: crystals form, stars clump and living things build themselves, but always by pushing more disorder out somewhere else. The second law is the backbone of this picture. Gravity, the speed of light, and the fact that the universe started out unusually orderly set the rest of the stage. GTAO adds no new physics. It asks one question: **what does it take to last while everything runs downhill?** There are three answers.

**Keep.** Some things settled long ago into states almost nothing can knock loose: atoms, crystals and, at the extreme, black holes. They pay nothing to last. They carry traces of where they came from, but none of those traces helps them last, because nothing they do depends on getting the world right.

**Hold** (called "Burn" before 19 Nov 2026). Some things last only by running energy through themselves: a star, a candle flame. They regulate themselves, and a star does so richly: self-regulating fusion (if the core runs hot, it expands, cools and burns slower), convection, magnetic dynamos, and a layered composition that is itself a frozen record of its history. But they regulate only themselves: they anticipate nothing outside, and nothing outside has to be known for them to keep going. Storms burn too. A hurricane is a heat engine between warm sea and cold sky, and it dies when the water under it cools or it hits land. Its state follows the world, so it carries a correlation with it. As far as anyone knows, nothing in it uses that correlation to last longer; whether anything does is an open question with a test (§2.2).

**Know.** Some things last only by running energy through themselves *and* staying matched to an outside world that changes and can kill them: a cell whose food moves, an animal, a company, a city. Knowing comes in steps:
- **Notice.** Many things merely follow the world. That is correlation, and it is everywhere.
- **Need it.** Some things would die sooner if that match were scrambled. Now the information matters for survival.
- **Hold a set point.** The simplest real model is a feedback loop that keeps adding up its error until the error is gone. A bacterium does this when it re-sets its sensitivity after a change in smell (integral feedback). That loop carries a tiny model of the world: "it will stay like this." A loop that only pushes back in proportion to the error, without adding up, does not.
- **Act ahead.** When the world arrives faster than you can react, you need a model of how it moves, such as a clock for a daily cycle. Then you act before it gets there. That is judgment. It is not a new principle, just a way of staying alive under the old one.
- **Pay for it.** Knowing is never free. Every knower has to balance **what to keep, what to check, and what to let go**. GTAO's bet is that the balance is set by how fast your world changes and how much a mistake costs you. That bet is testable and untested.

**How the three depend on each other.** Knowers are *built* from keepers: atoms, bonds, and DNA that is cheap to keep and repaired as it goes. They are *fed* by holders (self-regulating burners): a star's light, and heat and chemistry from a planet's interior. They *record* themselves in keepers: rocks, fossils, books. A good knower freezes whatever does not change and spends effort only on what does. Frozen memory is the cheap foundation knowing stands on.

**Knowing came on gradually (an idea, not a finding).** Chemistry first followed its surroundings, then depended on them, then perhaps held simple set points, then copied itself well enough for improvements to pile up, and then acted ahead. These steps may have come in a different order. The cell is the first place we know of where they were all packaged together.

**When many knowers face the same world, they share a model.** One trail, one price, one rulebook or one brain serves many parts. That is where layers come from. Shared knowledge goes stale unless each part bears the cost of the whole failing. That can happen in two ways: the parts share one fate, or someone enforces upkeep (a monitor, a rule, an owner). Shared fate is usually only partial. Worker ants, bees and wasps mostly can't breed, so the colony's success is largely, but not entirely, their success. That is why some bees and wasps, and some ants, police each other: even social insects mix both routes. And because no signal is instant, nothing large can know everything centrally. Big things federate. (If shortcuts faster than light existed, which the theory does not predict, a finite network of them would only raise the speed limit, and open ones would remove it; `WORMHOLES.md`.) On Earth, slow people and slow wires set that limit. The speed of light is the hard floor: on Earth it is a latency cost that shapes how organizations federate, and off-planet it is a hard cap.

**Where the bookends sit.** At the bottom, atoms have nothing to know. At the top, black holes keep the most for their size and predict nothing. Most of the disorder now in the observable universe is inside them. The universe is still far below its maximum disorder, and that gap is what makes every star and living thing possible. As it closes, knowing can last only as long as the last usable source of energy, which may be black holes slowly leaking long after the stars are gone. In an accelerating universe even that is finite.

**What it would mean if this is right.** The same few relations would hold from the first self-copying chemistry to cities: how often to look, how long to remember, when to share a model, when someone has to be in charge. Each would be set by how fast that level's world changes and what a mistake costs. You could look at an organization's world and say how it should be built. That is a bet, not a finding. §4 lists how to break it at each level. The top and bottom bookends (atoms, stars, galaxies, black holes, the cosmos) are **classifications, not predictions**: they place things in the picture, but no data could fail them.

---

## 2. The answers, with status

### 2.0 Definitions and formal pieces added in revisions 2 and 3 [BK, new; reviewed in two rounds unless labelled]

**2.0.1 Response vs action.**
- A **response** is any state-dependent physical effect of a structure on its own loss: A_t = π(M_t), with M_t its internal state. It needs no selection. A response is enough for Theorem P's information bound (GT-P0/GT-P1 use A1, A2, A5 and, implicitly, A4).
- An **action** is a response alternative over which a selection, learning or design process operates (Axiom 7; the reading THEORY §2.3 uses for "action"). Actions are needed for every *optimization* statement: GT-G2 (hold vs fade), Theorem 8, GT-P3 ("pays"), and all design predictions.
- Throughout, "pays", "optimal" and R\* need actions. "Required for persistence" needs only responses.

**2.0.2 Four notions of "knowing", kept apart.**

| Notion | Definition | Who has it | Test |
|---|---|---|---|
| Correlation | I(M; X) > 0, including predictive I_pred > 0 | almost every driven system (Still et al. 2012: a system "responding to a stochastic driving signal" retains information, "a fraction" of it predictive) | none needed; nearly universal |
| **Survival-relevant (semantic) information** | correlation whose scrambling, at fixed energy and matter fluxes, lowers viability (Kolchinsky & Wolpert 2018; viability = "ability to keep itself in a low entropy state", or a stated persistence time) | candidates: driven chemistry, storms, cells | **BK-SEM test:** scramble the state–drive correlation with a dose-matched sham; viability must drop. **Kill (non-model):** a drive-matched structure whose viability does *not* drop under scrambling at fixed fluxes holds correlation only |
| **Model (structural)** | error feedback containing a reduplicated model of the outside signal's dynamics (internal model principle, Francis & Wonham 1976), **regulating a variable that bears on the entity's own ruin**. Minimal case: integral feedback, the model of a constant/step world. It gives robust perfect adaptation (Barkai & Leibler 1997, abstract: adaptation that "does not require the 'fine-tuning' of parameters"; Yi et al. 2000 show that this is integral feedback, "integral control … necessary"). Proportional or leaky feedback holds no internal model; it leaves a steady error that shifts with the drive. High-gain proportional loops can *approximate* adaptation, because the IMP's necessity result concerns asymptotic, structurally stable regulation, which is why BK-IMP tests robustness. An oscillator matched to a periodic signal generator (an entrained clock) is **IMP-like**. **Regulator without stakes:** an IMP-like structure whose regulated variable does not bear on its own persistence. It is outside GTAO's knowing, whatever its structure | bacterial chemotaxis (integral); circadian clocks (IMP-like oscillator). Regulators without stakes: the carbonate–silicate cycle (candidate), ocean carbonate compensation | **BK-IMP test**, all three parts required: (a) after a sustained step in the drive, the regulated variable returns to its prior value; (b) that return is **robust to parameter perturbation**, which excludes tuned or high-gain proportional loops but does not by itself exclude an incoherent feedforward loop: searching all three-node topologies, "only two major core topologies emerge as robust solutions: a negative feedback loop with a buffering node and an incoherent feedforward loop with a proportioner node" (Ma et al. 2009, abstract); (c) a **structural check**, which is what separates feedback from feedforward: that the integrated quantity is the error (for example antithetic integral feedback, Briat, Gupta & Khammash 2016, metadata only). Flames, dunes and hurricanes are expected to fail (a) |
| **Selected model** | a structural model whose design is shaped by selection with resolution ε (Axiom 7) | cells and above, under strong selection | GTAO's design predictions (CM-N13, CM-J6, OPEN) |

"Feedback on own state only is not a model" is a definitional choice of this file, made so that the model concept stays about an exogenous world. Rosen 1985 (litmap; book not fetched) defines anticipatory systems to include "a predictive model of itself". Under Rosen's reading a star still does not qualify, because it acts on no prediction.

**2.0.3 Theorem P on real structures: finite horizon and the mapping lemma.**
- **Finite-horizon corollary (PROVED (in-model) in CLAIM_MAP N33 terms; elementary; supermartingale scope; Markov form OPEN) [BK, new; MATH_LOGIC round 2 checked].**
  - Let a blind structure (I_pred = 0) have reserve increments whose **conditional mean given the past is ≤ −δ < 0** (δ = r_∞ − (y − c̄), the smallest blind shortfall), with |ΔR + δ| ≤ b. This holds for an i.i.d. world, or whenever the centred reserve is a supermartingale.
  - Survival to T implies R_T > 0. By Azuma–Hoeffding, **P(blind survives to T) ≤ exp(−(δT − B)²/(2b²T)) for T > B/δ**.
  - *Under that condition*, survival well past B/δ is evidence, at stated confidence, that I_pred > 0. The bound was checked by Monte Carlo for i.i.d. ±b increments with B = 5, δ = 0.05, b = 1 and holds, loosely (`theory/bookends_checks/finite_horizon.py`, `.out`: at T = 1600 the simulated survival is 0.003 against a bound of 0.17).
  - **Mixing-time caveat.** In a Markov world the conditional mean of a blind agent's increment depends on the current world state even when I_pred = 0, and the condition fails. A persistent drifting world is exactly the case Q2 and BK-G2 are about. With mixing time τ_mix, blind survival can last of order τ_mix regardless of δ. The MATH_LOGIC round-2 counterexample (two-state world, flip probability 0.001, B = 5, δ = 0.1, b = 1) gives simulated survival 0.27 at T = 1600 against the i.i.d. bound's 0.0005. **Only survival ≫ max(B/δ, τ_mix) can count, and the mixing-adjusted exponent is OPEN.**
  - GT-P1's original statement is infinite-horizon and cannot classify any observed structure alone.
- **Mapping lemma (DERIVED under stated premises) [BK, new; MATH_LOGIC round 2: algebra correct].** For a non-replicating dissipative structure:
  - M_t is its internal state, declared before data;
  - A_t = π(M_t) is its response;
  - the reserve R_t is its stock of usable free energy, or a stated viability margin;
  - the influx depends on the world, y = y(X_{t+k}), evaluated at the same time index as the loss. Fold it into the loss as ℓ′(a, x) = ℓ(a, x) − (y(x) − ȳ), with ȳ = E[y(X)]. Because the shift depends on x only, D_ℓ′(R) = D_ℓ(R) exactly, so the distortion-rate function is unchanged; ℓ′ must be bounded (A5);
  - **premises, checked one by one:** A1 (exogenous world) fails if the structure alters its own feed. A2 (stationarity) holds only in the stationary regime. A4 (one currency) holds when every term is free energy. A5 holds for bounded fluxes.

  **What the lemma gives:** a *floor* on I_pred. **What it does not give:** that the structure holds a model. If M is declared to be the coupled state itself, the floor is met automatically. So Theorem P supplies the *amount* of information persistence requires. BK-SEM decides whether that information is causally used. BK-IMP decides whether a model structure carries it.

**2.0.4 CM-N25 and CM-N26 under the two-term reading (re-derivation).**
- **CM-N25 (atoms).** Its CLAIM_MAP statement ("no action whose payoff depends on the world ⇒ Φ = 0 …; blind-viable + E1 ⇒ R\* = 0") is an optimization statement. It is true *as written* under the Axiom-7 reading it states, so its PROVED (in-model) label is unaffected. Under the response reading the parallel conclusion follows from SE-E2 alone, which is non-definitional. Atomic persistence is blind-viable: a Boltzmann factor of about 10^−228.5 for hydrogen ionization at 300 K, so D(0) ≤ y − c̄ and GT-P1 allows I_pred = 0. Its ionization hazard is set by the bath temperature, not by the correlation between the atom's own state and the bath, so scrambling that correlation is expected to leave viability unchanged: semantic information **expected to be 0 (physical argument, not computed)**. It holds no integrator on any external variable, so it has no model. **Note added to the CM-N25 row (BK-P6). Label unchanged.**
- **CM-N26 (black holes): PROVED (in-model) scope limited to pre-Page-time holes.**
  - Condition (i), the Axiom-7 reading, can be replaced by SE-E2 plus SE-E4. Nothing outside threatens a hole's persistence, whose lifetime is set by its own leak, so persistence is blind-viable. Scrambling correlations between (M, J, Q) and the surroundings is expected not to change that lifetime: semantic information expected to be 0 (physical argument, not computed).
  - The "past every tracker's lookup edge" half is about *other* trackers using a hole as memory. They are selected, so the Axiom-7 reading applies to them anyway.
  - **Pre-Page-time holes (inside the PROVED scope):** information comes back no sooner than about the Page time ≈ 0.54 t_ev. That includes every astrophysical hole today. They are colder than the CMB, absorb more than they emit, and have not begun net evaporation, so for them the delay is effectively unbounded. The lateness condition holds with unitary evaporation assumed.
  - **Post-Page-time holes (outside the PROVED scope):** newly deposited information comes back after about the scrambling time, but only to someone holding essentially all the earlier radiation and paying a decoding cost (Hayden & Preskill 2007, via SCALE_ENDS). The lookup-edge conclusion then rests on that decoding cost, which is Harlow–Hayden's *conjecture*. So it is stated as **conditional on a conjecture** and kept out of the PROVED row.
  - **Applied to CM-N26 and THEORY §2.3 (BK-P7). Label PROVED (in-model) unchanged for its narrowed scope.**

### 2.1 Pre-cellular knowing: where between atoms and cells does it appear?

**Answer: there is no single switch. There are five separately measurable quantities. Their historical order is a HYPOTHESIS (H2-type) and only a partial order. CM-N28 concerns only selected models.**

| Quantity | First carriers (candidates) | What GTAO says | Status |
|---|---|---|---|
| Q0 Correlation | atoms (spin, speed, level populations correlate with temperature and fields; SE-E3(c)) | present, not needed for persistence (SE-E2) | DERIVED (§2.0.4) |
| Q1 Self-maintenance on a flow | dissipative chemistry; reflexively autocatalytic sets; the chemoton; autopoiesis | held structure; needs disequilibrium D > 0 | PRIOR ART (Prigogine 1978; Kauffman 1986; Hordijk, Hein & Steel 2010, metadata only; Gánti's chemoton and Maturana & Varela's autopoiesis, classics, not fetched) |
| Q2 Survival-relevant information | a self-maintaining system whose viability drops when its match to a drifting feed is scrambled | Theorem P (mapping lemma, §2.0.3) gives the floor on how much is required. BK-SEM decides whether it is used | **Synthesis, not new in substance:** Still et al. 2012; Kolchinsky & Wolpert 2018; Di Paolo 2005 ("adaptivity … allows organisms to regulate themselves with respect to their conditions of viability", abstract); England 2015 / Perunov, Marsland & England 2016 (dissipative adaptation; litmap). **New here is only the mapping onto Theorem P [BK, new]** |
| Q3 Minimal model (integral feedback) | any chemistry with robust perfect adaptation of a variable bearing on its own persistence | IMP-structural model. Possible without heredity in principle; no prebiotic case known. It needs throughput: "adaptive processes are necessarily dissipative" (Lan et al. 2012, abstract) | OPEN (BK-IMP) |
| Q4 Heredity with cumulative selection | template replicators below Eigen's threshold (εL ≲ ln σ). Compartmentalized networks with multiple viable cores show "limited heredity and selectability" before templates (Vasas et al. 2012, abstract); simple compositional genomes lack evolvability (Vasas et al. 2010) | selected models become possible (Axiom 7). *Strong* cumulative design points to templates; weak pre-template selection is possible. Pross's dynamic kinetic stability applies here, to replicators | PRIOR ART (Eigen 1971; Vasas 2010, 2012; Pross 2011; England 2013's heat bound on replication); CM-N28 OPEN |
| Q5 Acting ahead (realized lead k > 0) | entrained oscillators with phase lead (may not need heredity; untested, BK-G2); circadian clocks (Woelfle et al. 2004); microbial anticipation (Mitchell et al. 2009; Tagkopoulos et al. 2008; litmap) | acting ahead is *viable* only within the predictability horizon (GT-P2: k ≤ k_max, a ceiling set by the world and the budget). It *pays* only where lateness costs exceed upkeep (GT-P3, with actions) | PROOF (GT-P2, GT-P3); PRIOR ART for the data; H2 stays HYPOTHESIS |

**What changes relative to the record.**
- **CM-N28's wording changes; its status stays OPEN.** Its text said "a model switches on only with heredity …". Under this file's definitions that is true of *selected* models (Q4) and false for Q2–Q3 as a matter of definition. The same sentence in THEORY §2.3 (the "ends of the scale" bullet) gets the same change (BK-P5, applied). Under the response/action split the claim is no longer definitional: it has a kill, SCALE_ENDS SE4 kill (iii) (BK-P4).
- **SCALE_ENDS §3.3** put all pre-hereditary chemistry in "held, no model". Under §2.0 that stays right for "model". The structures can still carry survival-relevant information, which SCALE_ENDS now separates (BK-P2, applied).

**Testable consequence (HYPOTHESIS BK-G2, redesigned again in revision 3 per PHYSICS R2-1 and BIO R2-4).** *This is a test of the mapping in a designed system, not evidence about natural prebiotic chemistry.* **Not preregistered**, and it must not be until the premise check and power calculation below are done.
- **System:** compartmentalized light-sensitive Belousov–Zhabotinsky droplets (Ru(bpy)₃-catalysed). Each droplet consumes a reagent that arrives in pulses and is usable only within a phase window, so mistiming depletes it.
- **Physical premise to verify first:** the reagent pulsing must sit inside a measured entrainment (Arnold) tongue, or there is no natural entrainment to scramble. Resonance tongues under periodic forcing are documented for light-forced BZ (Petrov, Ouyang & Swinney 1997, metadata only; Lin, Hagberg, Meron & Swinney 2004, abstract). Whether *chemical* reagent pulsing entrains these droplets is to be measured. The droplet's phase-response curve to light must also be measured, to find its phase-insensitive window.
- **Viability (ruin) defined:** time until oscillation amplitude falls below a preregistered threshold after the feed switches to pulsed and depleting.
- **Arms (every arm gets the same light dose and pulse count):**
  - (T) **natural entrainment:** droplets entrain to the reagent pulses chemically, on their own. Light pulses are delivered only in the phase-insensitive window of the measured phase-response curve, so they do not move the phase (the dose-matched sham);
  - (S) **scrambling arm (the Kolchinsky–Wolpert intervention):** the same light dose, delivered at random phases so that it resets the droplet's phase relative to the feed;
  - (C) **rhythmless matched-mean control:** an aperiodic feed with the same mean reagent supply, where no phase information can help;
  - (L) **light-alone check:** the matched light dose under the C feed, to confirm that light by itself does not change amplitude decay.
- **Prediction:** viability T > S, and S ≈ C.
- **Kill:** T ≤ S within the preregistered minimum detectable effect.
- **Caveat:** the phase dependence of the feed is engineered, so a pass shows only that the mapping (§2.0.3) and the scrambling test (BK-SEM) work as instruments, here on a droplet's *own* entrained state. It is not evidence that nature built such systems. **Status:** HYPOTHESIS. Design OPEN until the tongue and phase-response premises are measured and the minimum detectable effect and power are computed (MV10).

### 2.2 Is feedback the simplest model? (revised)

**Decision [BK, new; reviewed in two rounds; resting on PRIOR ART].**
1. **Integral feedback on an exogenous variable is the minimal model** (Francis & Wonham 1976; Barkai & Leibler 1997; Yi et al. 2000), provided the regulated variable bears on the entity's own ruin. It holds the integrated error, a model of a constant/step world, and returns the regulated variable to its set point robustly. Without stakes it is a **regulator without stakes** (§2.0.2).
2. **Proportional (or leaky) feedback is not a model** in this sense. It carries correlation, and possibly survival-relevant information, but it leaves a steady error that shifts with the drive. High gain can approximate adaptation, but not robustly, which BK-IMP (b) separates.
3. **Feedback on own state only is not a model of any world.** This is a definitional choice (§2.0.2). A star's core balance is a proportional restoring effect: if the core heats, it expands, cools and burns slower.
4. **Revision 1's "lowest rung of a model = zero-order hold, exactly class R1" is withdrawn** (MATH_LOGIC finding 11; BIO finding 4). Axiom 3's R1 is discrete, costly, exact periodic reads. Continuous noisy feedback is at most analogous to R1 in the limit of frequent reads, and its cost class must be assigned separately.
5. **A repo inconsistency, now fixed.** SCALE_ENDS §2 labelled its no-model class "(H80's thermostat tier)", and §4.1 called the star's balance "H80's feedback tier". But H80's thermostat rung is a *predictor* of an outside target. BK-P1 (as amended per MATH_LOGIC R2-2) removes the label.
6. **Two orders, not one ladder.** H80 orders rungs by **cost**: constant predictor, timer, threshold/thermostat, small model, large model. The K axis (§2.7) orders by **structure and lead**: correlation, then survival-relevant information, then integral model, then dynamic model with lead. A timer is cheap (low in H80) but acts ahead (high on K). Revision 1 merged the two orders, which contradicted its own sequence (MATH_LOGIC finding 10; BIO finding 7).
7. **"Frozen" has three senses, now named:**
   - **frozen structure** (persistence mode, h = 0);
   - **frozen store** (a T8 memory tier: a stored fact with I > 0 that decays at H_l);
   - **constant predictor** (H80's bottom rung: a fixed prediction with I_pred = 0, the "blind" agent of GT-P1).

**Where hurricanes, flames, dunes and galaxies land** (expected results, not measured; CLASSIFICATION pending tests):
- **Correlation:** all have it (Still et al. 2012).
- **Survival-relevant information (BK-SEM):** OPEN for each. For drive-slaved structures whose relaxation is much faster than the drive changes, the expected result is no drop, because the scrambled state relaxes back within one relaxation time.
- **Model (BK-IMP):** expected **no** for all four. A flame's size shifts with oxygen supply, a dune migrates with the wind, and a hurricane's intensity tracks sea-surface temperature. A galaxy's gas reservoir in the gas-regulator ("bathtub") model is a **leaky** integrator: star formation "is instantaneously regulated by the mass of gas in a reservoir", and the sSFR "is set to the specific accretion rate" *if the SFR efficiency and wind mass loading are constant* (Lilly et al. 2013, abstract). The gas mass scales with inflow, so this is tracking with a shifting state, not perfect adaptation: **K1 per the Lilly 2013 regulator model**. An observational BK-IMP form for galaxies is not defined (OPEN).
- **Kill for this expectation:** any of them passes BK-IMP (a)–(c) for a regulated variable after a sustained step in its drive.

### 2.3 Why frozen memory exists in the grand scheme

GTAO gives roles inside its budget and the physical conditions behind them. It gives no purposes. **Three roles (DERIVED; revision 1's roles 1 and 4 merged per BIO finding 10):**
1. **Scaffold and freeze edge.** Knowers are built from frozen structures (nuclei, atoms, covalent frameworks, minerals) whose lifetime is set by a barrier, a conservation law or a horizon (SE-E4). Within a knower's own memory, anything drifting slower than q_f = 2c/(W H_l²) should sit in a frozen store (Theorem 8; CM-F13 PROVED (in-model)). H9's "paid systems are built out of frozen parts earlier flows left behind" is the plain form. Local hypothesis H8's note that frozen things formed in earlier non-equilibrium flows is consistent with this and was not checked here.
2. **Heredity in a near-frozen store.** A genome is **near-frozen, not frozen**. It is held at low upkeep (continuous repair within a lifetime), copied rather than tracked, and updated only across generations, with its length capped by copying fidelity (Eigen 1971). Crick's "frozen accident" (classic, not fetched) is the classic credit for heredity as freezing. In T8 terms it is the store for features drifting slower than a generation. The lower edge of the hold band is where "write it in the genome" gives way to "sense it" (CM-N28's S3; Kussell & Leibler 2005).
   - **HYPOTHESIS (O5/BH-1 on cellular tiers; CM-F13's field form is OPEN):** across DNA, chromatin marks, mRNA and protein modification, the denser and costlier-to-read the tier, the slower the drift of its content.
   - **Validity condition (BIO finding 9, accepted):** "drift of what each tier holds" must be measured *independently of the tier's own turnover*, for example as the rate at which the corresponding environmental variable changes, fixed in the prereg. Otherwise the test passes by construction.
3. **Records.** Frozen stores serve as memory for *later* knowers: zircons, fossils, ice cores, archives, append-only histories. Reading one is a T8 "freeze read" (SCALE_ENDS §3.1).

**Black holes as the frozen extreme (CM-N26 PROVED (in-model), conditional; conditions restated in §2.0.4).** A black hole has maximal memory for its size at the Bekenstein-minimum energy per nat, no upkeep, readable state (M, J, Q), and a leak lifetime of about 1.2×10⁶⁷ yr × (M/M☉)³ (photons and gravitons only). Three massless neutrino species would give about 1.5×10⁶⁶ yr (PHYSICS F17), but massive neutrinos are not emitted at T_H ≪ m_νc²/k. The clock starts only once the CMB is colder than T_H.

**The entropy picture, corrected (PHYSICS F7).** Egan & Lineweaver 2010 (abstract opened) find:
- S_obs = 3.1 (+3.0/−1.7)×10¹⁰⁴ k for the observable universe, with supermassive black holes "the largest contributor";
- the current cosmic event horizon's S_CEH = 2.6 ± 0.3×10¹²² k, "dwarfing the entropy of its interior, S_CEH,int = 1.2 (+1.1/−0.7)×10¹⁰³ k".

The like-for-like gap is therefore S_CEH,int ≈ 10¹⁰³ against S_CEH ≈ 10¹²². SCALE_ENDS's S_obs vs S_dS comparison mixes two volumes. "Most of the entropy now present in the observable universe is in SMBHs" is what Egan & Lineweaver estimate. Revision 1's "most of the running-down so far is stored in black holes" conflated entropy content with production history and is withdrawn. Their sentence that the uncapped increase "is the reason dissipative processes are ongoing and that life can exist" refers to the gap below the holographic bound (as PHYSICS F7 reports from their introduction; this author read only the abstract). **Caveat:** an entropy gap is not usable free energy by itself. Structures draw on local gradients (fusion, gravitational contraction, chemical disequilibrium), and the low-entropy start is what makes those gradients possible. **IMPOSTER:** "black holes exist *in order to* store entropy." GTAO has no teleology. The only published selection-based role for black holes is Smolin's cosmological natural selection (PRIOR ART, under observational pressure; SE12: GTAO adds no test).

### 2.4 Stars

**Classification: held, self-regulated, no model (CLASSIFICATION; SE9).** The reason is restated per PHYSICS F9: **no response of the star has a payoff that depends on getting an exogenous variable right.** External bodies can change its fate. More than 70% of massive stars will exchange mass with a companion (Sana et al. 2012, page summary), and binary interaction may affect the evolution of most massive stars. But the star cannot act on them, its core regulation is a proportional restoring effect with no integrator on any outside variable, and the scrambling test is expected to show no survival-relevant information. Convection, dynamos and pulsation are driven by internal gradients and do not change the class.
- **Withdrawn from revision 1:** "its ruin is fixed by its own mass and composition", which holds only for isolated stars.
- **Withdrawn:** "upkeep h = L". L is the star's **free-energy throughput**, not a maintenance cost. A star that stops fusing contracts and heats, and white dwarfs persist with no flux.
- **Stellar generations** pass on composition, a frozen record, with no selection over designs.
- **Kill (SE9):** a star whose persistence depends on tracking an external drift through a response it can vary. Stars remain an MV7 calibration case for "held but not modelling". **Galaxies are removed from that known group** (PHYSICS F3): they are K1 per the Lilly 2013 regulator model; an observational test is not defined (OPEN).

### 2.5 Planets and Gaia

**First name the persisting entity and its ruin variable (PHYSICS F2, accepted). Then classify.**

| Entity | Ruin variable | Classification | Basis |
|---|---|---|---|
| The rocky body | disruption (practically none) | frozen structures plus held, self-regulated convection; blind-viable (Venus persists) | CLASSIFICATION |
| **Abiotic climate regulation** (carbonate–silicate weathering) | none of its own: habitability matters only to life, so the cycle is not a persisting entity in Theorem P's sense | feedback in which a CO₂ reservoir integrates outgassing minus temperature-dependent weathering (Walker, Hays & Kasting 1981, title: "A negative feedback mechanism for the long-term stabilization of Earth's surface temperature"; metadata only). It is structurally **integrator-like** to the degree that weathering depends on temperature alone. It has no stakes, so it is a **regulator without stakes** (§2.0.2), not a knower. Scope (PHYSICS R2-5): (a) only BK-IMP applies, not BK-SEM, since nothing persists or is ruined; (b) Earth's actual weathering is strongly biologically mediated (land plants, soils) and also depends directly on pCO₂ and runoff, so perfect adaptation is not expected even in principle, and "abiotic" means the idealized or pre-vegetation cycle; (c) the structural test is cleaner on Walker-type box models than on Earth data (n = 1, slow forcing) | CLASSIFICATION (regulator without stakes); degree of integral action OPEN (BK-IMP on box models) |
| **The biosphere** | extinction of life | a population of knowers. Its regulation (Gaia) is carried by organisms under organism-level selection. In Daisyworld the coupling comes from competing daisy types (Watson & Lovelock 1983, litmap). Doolittle 2014 argues the same for real Gaian traits | selected models *within* it (class 3); planet-scale regulation is a by-product, **unselected at planet scale** |
| **Planet-scale persistence filtering** | — | Lenton et al. 2018 (abstract): "sequential selection", where destabilizing systems "are short-lived and result in extinctions and reorganizations until a stable attractor is found", plus "selection by survival alone". That phrase is Doolittle 2014's (page read): "differential survival of non-competing and non-reproducing individuals will also result in increasing frequencies of survival-promoting 'adaptations' among survivors". He predicts *accumulation* of persistence-promoting traits even at n = 1, mostly fixed by lower-level selection (his note 3). Bouchard 2008 and 2011 and Bourrat 2014 are part of this debate (named via Doolittle and BIO; not opened) | PRIOR ART. **HYPOTHESIS (revision 1 asserted it):** a persistence filter at n = 1 has a large design resolution ε, so GTAO's *optimality* predictions do not apply at planet scale. Doolittle's accumulation claim is compatible with that, since accumulation is not optimality, but the ε is unquantified (OPEN) |
| **Atmosphere, oceans, soils** | — | a **shared slow store and drift reducer**: life reshapes its world so it changes less (THEORY §5; Lee, Flack & Krakauer 2024, "Constructing stability: optimal learning in noisy ecological niches", whose preprint calls niche construction "outsourced memory"; Lenton et al. 2018) | PRIOR ART; also a commons (§3) |
| **The technosphere** | — | since humans, Earth forecasts ahead (climate models, asteroid tracking): **K3 components at planet scale**. Frank, Grinspoon & Walker 2022 (abstract) treat "intelligence as a planetary scale process" and technological intelligence as a transition that happens "to a planet" | PRIOR ART framing; CLASSIFICATION |

**Rival framing (credited).** Rubin, Parr, Da Costa & Friston 2020 (abstract) formalize Gaia with a Markov blanket. The biosphere's metabolic rates are the internal states, solar radiation the external states, greenhouse and albedo changes the active states, and ocean-driven temperature the sensory states. This is the free-energy principle's specific planetary claim and a **rival** to this file's more restrictive criteria (§2.0.2). The disagreement is testable only once both sides fix an intervention (BK-SEM, BK-IMP) in advance.

**Earlier chat claim corrected again.** Revision 1 said Daisyworld's regulation is "a model of the lowest, reactive kind … unselected". Under §2.0 it carries correlation and, at the daisy level, selected responses. Whether its feedback is integral (a model) depends on the model's equations, and it is **selected at the daisy level, unselected at planet scale**.

**Why would life outlast humans? (ANALOGY plus PRIOR ART; not PROVED.)** Revision 1 used THEORY §4's pooling rule z′ = z√(N/(1+(N−1)ρ)) and called it "DERIVED from PROVED (in-model) rules". Both labels were wrong. MATH_ATTACK labels §3.2 "PROOF + NUMERIC", and the rule needs a pooled, fungible buffer (its condition C2), which lineages do not share (MATH_LOGIC finding 7; PHYSICS F12). What stands:
- **The direction:** many weakly correlated lineages make a whole that fails only under shocks correlated across nearly all of them. This **extends by analogy** the insurance hypothesis (Yachi & Loreau 1999, abstract: "many species provide greater guarantees that some will maintain functioning even if others fail"). Their model concerns the temporal mean and variance of ecosystem productivity under environmental fluctuation, driven by asynchronous species responses, not lineage survival through extinction shocks. The parallel-survival argument itself is not derived in the repo (OPEN).
- **The evidence** is empirical: the biosphere has re-established after mass extinctions; for example, biotic recovery after the end-Permian extinction is the subject of Chen & Benton 2012 (metadata only, so no rates are quoted from it here). "Fast" means fast relative to geological forcing, not to human time. This sentence is not carried into canonical files until a source is read.
- **The long-run end** is a ρ ≈ 1 exogenous drift (solar brightening; Caldeira & Kasting 1992 per PHYSICS F12, metadata only), consistent in direction with the argument.

**"Is a planet conscious?"** GTAO's quantities (correlation, survival-relevant information, model structure, lead k, selection resolution ε) are **not measures of consciousness**, and GTAO has no variable for experience. So the question is **out of scope**, and any claim that *GTAO shows* a planet is, or is not, conscious is an **IMPOSTER**.

### 2.6 Implications at every level: see §4 (table).

### 2.7 One coherent picture in technical terms: three axes

**[BK, new synthesis; reviewed in two rounds.]**
- **Axis P (persistence):**
  - *frozen structure*: h = 0; lifetime set by a barrier, a conservation law or a horizon;
  - *held*: free-energy throughput; needs D > 0.
- **Axis K (knowing; §2.0.2):**
  - K0: correlation only;
  - K1: response without model (self-regulation, proportional or leaky feedback, drive-slaved), possibly with survival-relevant information (written K1s when BK-SEM is positive);
  - K2: minimal structural model *of a variable bearing on the entity's own ruin* (integral feedback; robust perfect adaptation; BK-IMP (a)–(c)). The same structure without stakes is a **regulator without stakes**, outside the K axis;
  - K3: dynamic model with realized lead k > 0 (IMP-like oscillator or clock, predictive model), again of the entity's own ruin variable.
- **Axis S (selection):** none; persistence filter (survival of the stable; Doolittle's selection through survival; Lenton's sequential selection); weak pre-template selection (Vasas 2012); cumulative selection with heredity, learning or design, with resolution ε (Axiom 7).

**How they depend on each other.**
- **K2 and K3 require P = held.** The direct basis is prior art. Lan, Sartori, Neumann, Sourjik & Tu 2012 (abstract): "adaptive processes are necessarily dissipative, and continuous energy consumption is required to stabilize the adapted state", which covers K2. Cao, Wang, Ouyang & Tu 2015 (abstract): an oscillator's "phase diffusion constant depends on the free energy dissipation per period", so an accurate clock needs throughput, which covers K3. SCALE_ENDS SE-E3 (memory about a drifting variable costs dissipation) is consistent with this but weaker, because Still et al.'s bound is on *non*-predictive information. K0 and K1 do not require upkeep: passive coupling can approach zero cost (SE-E3(c)).
- **The three-cost accounting** applies everywhere (Axiom 5; CM-J16 OPEN).
- **Theorem P** (with §2.0.3) gives the information floor wherever responses exist and blind is not viable.
- **Design predictions** need actions: S cumulative with the prize above ε.
- **Thermodynamic floors:**
  - Erasure costs at least kT ln 2 per bit (Landauer). A measure-and-reset cycle costs at least kT × the mutual information acquired (Sagawa & Ueda 2009), and measurement alone can in principle be reversible.
  - Still et al.'s bound assumes a single heat bath, Markov dynamics, an equilibrium start and no back-action on the drive (PHYSICS F8, from their setup). Stars, storms and planets violate these, so the bound is used for them only as an **analogy**. The same scope note applies to SCALE_ENDS SE-E3(c)'s "driven systems" clause (BK-P11).

| Structure | P | K (expected; tests in §2.0.2) | S | Design predictions? |
|---|---|---|---|---|
| Atom, nucleus, crystal | frozen | K0 | none | no (CM-N25) |
| Black hole | frozen (extreme) | K0 | none (Smolin's hypothesis aside) | no (CM-N26) |
| Star | held | K1 | none | no (SE9) |
| Galaxy (gas regulator) | held | K1 per the Lilly 2013 regulator model (candidate; observational test not defined) | none | no |
| Flame, dune, hurricane | held; hurricanes and flames transient | K1; K1s OPEN | none | no; hurricanes are outside GT-P's long-run statement |
| Driven chemistry, autocatalytic networks | held | K1 or K1s (BK-SEM); K2 OPEN | filter to weak cumulative (OPEN) | no |
| Template replicator, protocell | held | K1s–K2 | cumulative if below Eigen's threshold | in principle (CM-N28 OPEN) |
| Cell | held | K2–K3 | cumulative, strong | yes (CM-N24 INCONCLUSIVE; CM-N13 OPEN) |
| Brain, person | held | K3 | learning plus evolution | yes, moderate ε |
| Colony, firm, city | held | K2–K3 with levels | moderate to weak | yes, gated by ε |
| Earth system | mixed (§2.5) | geochemical thermostat: regulator without stakes (candidate); biosphere: K2–K3; technosphere: K3 | filter at planet scale; cumulative within | not at planet scale |
| Universe | — | not a tracker | — | IMPOSTER to say otherwise |

In one line: **knowing is held structure that frozen structure lets accumulate and burning structure pays for, and judgment is the part of knowing that acts ahead.**

---

## 3. Layers and governance, from the same spine

Each step keeps its source label and states where it fails.

1. **Persistence needs a throughput. Where lateness is costly, a model can pay** (GT §1, GT-P3 with actions). Models cost upkeep, reads and error (Axiom 5; one currency within an organization, A4).
2. **Shared drivers favour shared models.** TH-T3a (**PROOF; elementary; a sufficient condition, not a cutoff**): nesting is cheaper whenever √N·√(2cwq_u)·[√N(√(1+ρ) − 1) − √ρ] > h. At h = 0 this is N > (√(1+ρ)+1)²/ρ. In the formal layer the level's sensing class sets the onset exponent (CM-B3, CM-B9 PROVED (in-model)), and shared drift centralizes while private drift decentralizes (CM-C1 PROVED (in-model)). A level is a shared model of a common driver (THEORY §6). Flack 2012 and 2017 on slow, coarse-grained collective variables are the prior art for levels as shared slow variables (litmap). **Fails:** with no shared drift (nesting loses by its upkeep); below N\* (the bound says nothing there); when the driver is seen only through the facts (then it is an approximation).
3. **Separate clocks buy little and need separated time scales.** TH-T3b (**KNOWN**; Roundy 1985): at most 29% saving for two levels. TH-T3c (**NUMERIC; principle KNOWN**: Simon–Ando, Tikhonov, Borkar): decoupled nesting is near-optimal only when time scales separate. **Fails:** collapsed or inverted time scales.
4. **Self-similar when the world is.** TH-T7 (**PROOF (conditional); the unconditional claim FAILS**; v1.4.27: the proved direction is "scale-free world, power-law costs and the same loss at every level give a self-similar optimum"; that only such worlds do is not proved, and THEORY §1 N4 withdraws the "iff" layering claim). Testable forms (i)–(iii). **Flag:** T7(iii)'s "number of levels grows as L^{2/3}" (L = log-span) predates THEORY v1.4. The (log-span)^{2/3} count is withdrawn (CM-K12 MATH-CORRECTED). The store count is now ∝ ln(span)·ln(stakes/upkeep) away from α = 2, with its rate marked conjectural in THEORY N4. BK-P8 marks it withdrawn in THEOREMS (applied). **Fails:** characteristic times, fixed setup costs, or different loss forms across levels.
5. **A whole is a knower like its parts only under strict conditions.** MATH_ATTACK §3.4 (**PROOF + NUMERIC**): a representative agent exists only under a Gorman-type condition, c_i/(w_iσ_i²) equal across parts. MATH_ATTACK §3.6: form invariance holds iff C1–C4 hold, and **the strong form is FALSE**. So "the same pattern at every level" is about relations measured level by level (CM-J6 OPEN). **Fails:** heterogeneous costs, non-fungible buffers, heterogeneous fix times, correlated shocks.
6. **Parts under-watch when the whole's failure cost does not reach them.** MATH_ATTACK §3.4 (**PROOF**): watching is too low by √(Λ_i/Λ_whole) when each part counts only its own Λ_i. This is the standard externality result in this cost form (public-goods prior art; Ostrom 2010, litmap; Ostrom 1990, classic, credited in THEORY §6). The source states it for a part's own failure hazard. **Reading it as "parts under-watch shared memory" is an extension [BK, new, unreviewed].** Lee, Flack & Krakauer 2024: stabilization is a public good, and when resources are shared "niche destructors" can evolve (as BIO reports from the published abstract).
7. **The remedy is shared fate or enforcement (HYPOTHESIS; CM-J9 OPEN; not a consequence).** MATH_ATTACK §3.4 names the routes: the failure cost is internalized "by incentives, **shared fate** or a central controller". Shared fate needs no one in charge, but it is usually **partial**. Workers (many cannot breed, but in many species workers lay male eggs) share the colony's fate through relatedness r, so Λ_i ≈ r·Λ_whole: in the α = 2 reset-read case watching falls to about √r of its optimum (r^{1/α} in general). r = 3/4 (full sisters under single mating) is the best case, giving ≈ 0.87 and ≈ 13% under-watching, not zero; with multiple mating r is lower and under-watching is larger. Frank 1995's abstract says self-restraint through relatedness "is not sufficient: mutual policing and enforcement … are also required" to explain how "small, individual replicators formed cooperative groups", and the same problem recurs in insect and human societies. So enforcement is the other route, and the two usually combine. Worker policing in eusocial Hymenoptera is the subject of Ratnieks 1988, which, per the 18 November 2026 technical review's reading of its abstract, ties policing to multiple mating (lower r); it is best documented in bees and wasps and is not universal in ants (per BIO R2-2). The qualitative claim is **PRIOR ART** (Ostrom; Frank 1995). GTAO's own part is the √(Λ_i/Λ_whole) scaling and the predicted placement. CM-J9 stays OPEN. CM-J8 ("no one in charge, at every level") stays **WITHDRAWN**. CM-J7 (fractal vigilance, qualitative) is **PRIOR ART**, and its quantitative version is untested on a valid instrument. Revision 1's identification of CM-E6 with fractal vigilance is withdrawn (MATH_LOGIC finding 12). **Flag (fixed):** THEORY §6's example "as with ants on a trail they themselves follow" for "privately rewarded" was **shaky**. Workers mostly do not reproduce, so their "private reward" is colony-level fitness (partly shared fate), and some social insects police. BK-P10 rewords it (applied). **Fails:** if enforcement is as common where shared memory is privately rewarded or fate is shared, or if staleness does not rise with users per maintainer.
8. **Signal delay forces federation; light delay is the floor (with no shortcut; conditional cases in `WORMHOLES.md` §4b).** LAT-1 (**CM-N27 OPEN**; the bound is elementary): with hold-last-value reads, a tracker of extent L holds a target only if q·ℓ^{α−1} is below tolerance, where ℓ ≥ L/c. On Earth, ℓ is set by processing, conduction and decision time. Light crossing half of Earth's circumference takes about 0.07 s (PHYSICS F15), so c is rarely the binding delay for human organizations on Earth, but it is a latency cost for latency-critical distributed systems (cross-continental round trips; PACELC) and a hard cap off-planet. **Fails:** if at fixed q the central share does not depend on ℓ. **Weighting:** spacecraft autonomy is engineered against light delay, so a pass there is weak (confirmation by design), and geo-distributed firms carry more weight.

**How this follows from the spine.** The second law forces upkeep. Upkeep makes duplicate models wasteful, so shared drivers get shared models. Shared models are commons, so they need shared fate or enforcement. Signal delay caps how far one model reaches, so, absent shortcuts, wholes federate. Every step is an economy of knowing under a physically forced budget. None adds a new physical principle. **Downward:** the first "level" was likely a compartment shared by cooperating replicators, which is exactly Frank 1995's opening case (PRIOR ART).

---

## 4. Implications if GTAO is right, level by level

"If right" means: strongly selected systems sit near the optima once α, q, N and stakes are measured on the same system, with the same relations at every level (CM-N13, CM-J6, OPEN). **Rows marked CLASSIFICATION are not predictions.**

| Level | Placement (§2.7) | What follows if right | Testable consequence (status; weaknesses) |
|---|---|---|---|
| **Chemistry** | held; K1→K1s/K2; filter→weak cumulative | Survival-relevant information can precede heredity. Design optimization starts with heredity | **BK-G2** (designed-system test of the mapping; HYPOTHESIS, design OPEN). **BK-IMP in chemistry:** robust perfect adaptation in a non-hereditary network (OPEN). Whether the Landauer floor binds before the cell is **OPEN**; the bacterial margin (CM-N28) says nothing about prebiotic systems (PHYSICS F8c) |
| **Cell** | K2–K3; strong selection | Read rate, memory time and store count near the §2.2 optima. The floor shapes exponents, not existence | **SENSE-CELL-MATCHED** (CM-J11 OPEN; CM-N24 INCONCLUSIVE). **O5/BH-1 on cellular tiers**, with drift measured independently of tier turnover (HYPOTHESIS) |
| **Organism, brain** | K3; learning | Energy per stimulus tracks predictable information. Higher levels track slower causes | **H4** (HYPOTHESIS; must be positioned against the existing repetition-suppression vs expectation literature, which BIO names and this author did not open). **H80 tier test** on a named system: the Intel Berkeley Research Lab sensor traces named in C13 (HYPOTHESIS) |
| **Colony, society** | levels; moderate selection | Levels where shared drift is large for its N. Shared fate or enforcement where memory is a public good | **TH-T3a/CM-C1 factorial** (FRAMEWORK §6.4; OPEN). For ants specifically: THEORY's own species-by-patchiness test (THEORY N2; OPEN). That policing should rise as relatedness falls follows from textbook kin-selection theory and Frank 1995's model (abstract); Ratnieks 1988 is not read. It is PRIOR ART, not a GTAO test |
| **Firm** | levels; weak–moderate selection | Watching rises with stakes. Drift reduction substitutes for watching. Under-watching scales as √(Λ_i/Λ_whole) | **SAME-SYSTEM-AQN** (first CM-N13 test; OPEN). The contract-length vs volatility prediction (THEORY §5) needs a transaction-cost literature check before it counts as GTAO's (OPEN) |
| **City** | levels; weak selection | Monitoring sublinear and tiered | **CM-I14** (OPEN). z ∝ N^{b−H−θ/2} (MATH_ATTACK §3.5, CONJECTURE) |
| **Civilization** | levels at planetary extent | Federation forced by latency (light delay: a latency cost on Earth, a hard cap off-planet; absent shortcuts, `WORMHOLES.md` §4b) | **LAT-1** (CM-N27 OPEN), weighted toward geo-distributed firms |
| **Planet** | mixed (§2.5) | Earth regulates through its biosphere, plus an integrator-like geochemical cycle that is a regulator without stakes. Life reduces the drift it tracks. The technosphere adds forecasting | **Microcosm substitution (HYPOTHESIS, redesigned per BIO finding 9):** externally manipulate drift (buffered vs fluctuating medium) across replicate evolving lines, and predict lower investment in sensing and regulation in buffered lines at matched stakes. A pass is weak, because loss of unused regulation under relaxed selection is known (Mitchell et al. 2009). **BK-IMP on carbonate–silicate box models** (OPEN; a classification, not a knowing test). No test at planet scale for design predictions (n = 1) |
| **Star** | held; K1 | — | CLASSIFICATION. SE9 kill; MV7 calibration case |
| **Galaxy** | held; K1 per the Lilly 2013 regulator model | — | CLASSIFICATION; an observational BK-IMP form is not defined (OPEN). Not a calibration case |
| **Black hole** | frozen extreme | Nobody's usable memory | CLASSIFICATION. BH-1 = O5 is tested only in ordinary storage hierarchies (HYPOTHESIS) |
| **Cosmos, heat death** | gap closing | Knowing can last no longer than the last usable gradient, which may be black-hole evaporation long after the stars. In an accelerating universe the total recoverable information is finite and "life cannot be eternal" (Krauss & Starkman 2000, via SCALE_ENDS). Dyson-style hibernation does not rescue indefinite computation, by Krauss & Starkman's argument | CLASSIFICATION; PRIOR ART relabelled (SE14). Revision 1's ordering "knowing ends first, burning next, keeping last" is withdrawn (PHYSICS F13) |

---

## 5. Prior art credited

- **Thermodynamics and information:** Prigogine 1978; Landauer 1961; Sagawa & Ueda 2009; Still, Sivak, Bell & Crooks 2012; England 2013 (replication heat bound, Q4); England 2015 and Perunov, Marsland & England 2016 (dissipative adaptation, Q2).
- **Semantic information and adaptivity:** Kolchinsky & Wolpert 2018; Di Paolo 2005; autopoiesis (Maturana & Varela; classic, not fetched).
- **Internal models and adaptation:** Francis & Wonham 1976 (internal model principle); Barkai & Leibler 1997 (robust adaptation without fine-tuning); Yi, Huang, Simon & Doyle 2000 (integral feedback in chemotaxis); Ma, Trusina, El-Samad, Lim & Tang 2009 (the two adaptive core topologies); Briat, Gupta & Khammash 2016 (antithetic integral feedback, metadata only); Lan, Sartori, Neumann, Sourjik & Tu 2012 (adaptation is necessarily dissipative); Cao, Wang, Ouyang & Tu 2015 (oscillator accuracy costs free energy); Conant & Ashby 1970 (good regulator; the "model" is only a homomorphism, per GENERAL_THEOREM §2's notes); Rosen 1985 (anticipatory systems; litmap).
- **Origins:** Eigen 1971; Kauffman 1986; Hordijk, Hein & Steel 2010 (metadata only); Gánti (chemoton; classic, not fetched); Vasas, Szathmáry & Santos 2010; Vasas, Fernando, Santos, Kauffman & Szathmáry 2012; Pross 2011 (dynamic kinetic stability, for replicators).
- **Acting ahead:** Woelfle et al. 2004; Mitchell et al. 2009; Tagkopoulos et al. 2008; Sterling 2012 (allostasis; litmap).
- **Gaia:** Lovelock & Margulis 1974; Watson & Lovelock 1983; Lenton et al. 2018; Doolittle 2014; Rubin, Parr, Da Costa & Friston 2020 (rival); Frank, Grinspoon & Walker 2022; Walker, Hays & Kasting 1981 (metadata only).
- **Niche construction:** Lee, Flack & Krakauer 2024. **Biodiversity insurance:** Yachi & Loreau 1999.
- **Levels and governance:** Simon 1962; Roundy 1985; Gorman 1953 (as in MATH_ATTACK); Flack 2012 and 2017; Ostrom 1990 and 2010; Frank 1995; Ratnieks 1988 (metadata only); Beer and Mintzberg (THEORY §6).
- **Astrophysics and cosmology:** Lilly et al. 2013; Sana et al. 2012; Egan & Lineweaver 2010; Hayden & Preskill 2007; Smolin 1992 and 2004; Krauss & Starkman 2000.
- **Rival:** the free-energy principle (Friston 2010, 2013; Friston et al. 2023; Rubin et al. 2020). The critique that it is "trivially true or ill-defined at scale" (Aguilera et al. 2022; Bruineberg et al. 2022; litmap THREATS) applies equally to any GTAO definition of "model" that every driven system satisfies. §2.0.2's tests exist to avoid that.
- **Litmap conflict, acknowledged (BIO finding 3).** litmap/LITMAP.md files dissipative adaptation (England 2015; Perunov et al. 2016) as CONTRADICTS: "a rival physical route needs no prediction". Under revision 1 those systems became "models", which dissolved the threat by redefinition. Under revision 2 they are K1 or K1s (correlation or survival-relevant information, no structural model). The threat stands: dissipative adaptation is a route to drive-matched persistence without a model. THREATS C6 now says so (BK-P12, applied).

---

## 6. Changes to canonical wording: final text, applied in this PR

**Process.** Revision 2 listed these proposals. Round 2 of the three reviews amended them: MATH_LOGIC R2-1…R2-4, PHYSICS proposal table, BIO R2-1, R2-2, R2-3 and R2-5. Revision 3 applies them as amended (Chad delegated theory decisions at t1927; the instruction to apply came via Ace). **No CLAIM_MAP status label changes.** The wording or conditions of CM-N25, CM-N26 and CM-N28 change. CM-N26's PROVED (in-model) scope narrows to pre-Page-time holes. New rows N30–N35 are added. THEORY goes to v1.4.20 and CLAIM_MAP to v2.41.

- **BK-P1 — SCALE_ENDS §2 class table, class 2 (amended per MATH_LOGIC R2-2).** Class 2 becomes "**Held structure, no structural model**: self-regulation, or a proportional/drive-slaved response to an exogenous variable; may carry survival-relevant information (BOOKENDS BK-SEM)". The "(H80's thermostat tier)" label is removed. In §4.1, "H80's feedback tier" becomes "self-regulation (a proportional restoring effect); not H80's thermostat rung, which predicts an exogenous target". *Applied.*
- **BK-P2 — SCALE_ENDS §2: the four notions, and class 3 vs 3s (amended per PHYSICS and BIO R2-1).** A note after the class table defines (a) correlation, (b) survival-relevant information, (c) a structural model *of a variable bearing on the entity's own ruin*, and (d) a selected model. A structural model with nothing at stake is a **regulator without stakes** and stays in class 2 with a note; the candidate is the carbonate–silicate cycle. Galaxies-as-K1 is a candidate classification. Class 3 (held model) may include unselected systems. **Class 3s (selected model)** is where GTAO's design predictions apply. *Applied.*
- **BK-P3 — SCALE_ENDS §2: class 3 condition (amended per MATH_LOGIC R2-2).** The class-3 "Needs" cell becomes "E1 fails for a *response* with world-dependent payoff (BOOKENDS §2.0.1), E2 fails, a flux (E3), and a structural model of an exogenous drifting target bearing on the entity's own ruin (internal model principle; BOOKENDS BK-IMP)". Class 3s adds "selection over designs (Axiom 7: heredity, learning or design)". *Applied.*
- **BK-P4 — SCALE_ENDS §3.3 and SE4 kill (a pre-data revision, logged with its reason; amended per PHYSICS and BIO R2-5).** §3.3 becomes "They need D > 0. They are class 2 unless they hold a structural model; whether they carry survival-relevant information is tested by BOOKENDS BK-SEM". SE4's kill becomes three kills:
  - (i) a structure holding survival-relevant information about a drifting variable **with no flux** (not merely a vanishing one; passive quasi-static coupling, SE-E3(c), is excluded);
  - (ii) a structure passing BK-IMP for an exogenous step **with no flux** (prior art says adaptation is necessarily dissipative: Lan et al. 2012);
  - (iii) **a non-hereditary, non-learning structure whose design sits measurably nearer a GTAO optimum than unselected controls** (a design prediction met without heredity or learning). This kill tests "selected models need heredity" (CM-N28 as reworded).

  *Reason:* SCALE_ENDS IR-FIX10 found the heredity clause near-definitional under the Axiom-7 reading. Under the response/action split, kill (iii) makes it non-definitional. *Applied.*
- **BK-P5 — THEORY §2.3 ("ends of the scale" bullet), the THEORY status block, SCALE_ENDS §0 item 6, and the CM-N28 text.** "Models switch on only with heredity, …" becomes "*Selected* models (design optimization) switch on only with heredity, a world-dependent action, drift inside the hold band, and a first nat that pays; survival-relevant information and minimal (integral-feedback) models are not excluded earlier (`theory/BOOKENDS.md` §2.1)". CM-N28 stays OPEN. *Applied.*
- **BK-P6 — CM-N25 note (label unchanged; amended per MATH_LOGIC R2-4 and PHYSICS).** Added note: "Under a response (unselected) reading the conclusion follows from SE-E2 alone: blind persistence is viable, so Theorem P allows I_pred = 0, and semantic information is expected to be 0 (physical argument, not computed; BOOKENDS §2.0.4)." *Applied.*
- **BK-P7 — CM-N26, THEORY §2.3 and status block, SCALE_ENDS §0 item 3, SE10 and §4.2 (label unchanged; scope narrowed per MATH_LOGIC R2-3).**
  - Condition (i) becomes "SE-E2 + SE-E4 (or the Axiom-7 reading)".
  - The PROVED (in-model) scope is **pre-Page-time holes (all astrophysical holes today)**, with retrieval delay ≥ ~t_Page, unitary evaporation assumed.
  - Post-Page-time holes are stated *outside* that scope: new information returns after ~the scrambling time, only to a holder of the earlier radiation, at a decoding cost (Hayden & Preskill 2007). Their lookup-edge placement is conditional on Harlow–Hayden's conjecture.

  *Applied.*
- **BK-P8 — `theory/THEOREMS.md` T7(iii).** The L^{2/3} level count (L = log-span) is marked **withdrawn**. It predates THEORY v1.4; see CLAIM_MAP K12 (MATH-CORRECTED) and THEORY N4 for the current store count (rate conjectural). The T7b "Number of levels" bullet gets the same pointer. *Applied.*
- **BK-P9 — the spine (theory content; applied).** BK-P9 is a sentence about *what the theory says*, its headline framing. It is not about publication or personal data, so under t1927 it is applied: as the opening paragraph of THEORY §0 and as the README's plain headline. Final text: "Everything obeys the second law: total entropy rises, though local order can grow by exporting entropy. That law, together with gravity, the speed of light, quantum physics and the universe's low-entropy start, sets the stage; GTAO adds no new physics. Atoms and crystals carry information but have no use for a model; stars regulate themselves on a flow (self-regulating fusion, convection, dynamos, layered composition) but anticipate nothing outside; cells, people, firms and cities last only by staying matched to a world that changes and can ruin them, and once acting late is costly, carrying a model and acting ahead can pay. That is judgment: not a new physical principle, but a way of staying alive under the old one." The **12 Nov framing** (second law as backbone; judgment = acting ahead to stay alive under it) is this sentence. *Applied.*
- **BK-P10 — THEORY §6 example (amended per BIO R2-2).** "(each contributor's own use pays for its deposits, as with ants on a trail they themselves follow)" becomes "(each contributor's own use pays for its deposits). Social insects mostly fit the other routes: sterile workers *partly* share the colony's fate (relatedness; watching falls only to about √r of its optimum, ≈ 0.87 for r = 3/4, so under-watching is small, ≈ 13%, but not zero), and since self-restraint through relatedness is not sufficient on its own (Frank 1995), some bees, wasps and ants also police." "**Otherwise expect enforcement**" becomes "**Otherwise expect shared fate or enforcement, usually both**". THEORY §6's citation "MATH_ATTACK §3.5" becomes §3.4. *Applied.*
- **BK-P11 — SCALE_ENDS SE-E3(c), §0 item 1, E2, SE9 and §4.1 (amended per PHYSICS).**
  - "A read … costs at least kT ln 2 per bit erased" becomes "erasing a bit costs at least kT ln 2 (Landauer); a measure-and-reset cycle at least kT × the information acquired (Sagawa & Ueda); measurement alone can be reversible".
  - SE-E3(c) gains: "Still et al. formalize this for isothermal Markov systems (single bath, no back-action on the drive); elsewhere it is an analogy."
  - Galaxies are removed from SE9's known-negative group. The galaxy is "K1 per the Lilly 2013 regulator model; observational test not defined".
  - §4.1's "upkeep h is its luminosity L" becomes "free-energy throughput L (not a maintenance cost)", and "ruin fixed by its mass" becomes "for an isolated star; most massive stars interact with a companion (Sana et al. 2012)".

  *Applied.*
- **BK-P12 — litmap/THREATS.md: new entry C6** (dissipative adaptation gives drive-matched persistence without a structural model; the threat stands). C3 and D3 also gain "shared fate", and LITMAP gains rows for the prior art opened in this work. *Applied.*
- **BK-P13 — CLAIM_MAP new rows N30–N35.**
  - N30: definitions (response/action, four notions, ruin-variable clause, regulator without stakes): DECIDED.
  - N31: BK-SEM and BK-IMP tests: OPEN.
  - N32: BK-G2: OPEN; design OPEN, not preregistered.
  - N33: the finite-horizon corollary: PROVED (in-model) under its supermartingale condition; Markov form OPEN; the τ_mix caveat is in the row (§2.0.3 uses the same label).
  - N34: Earth classification (biosphere-carried regulation, selected within and filtered at planet scale; a geochemical regulator without stakes; technosphere K3): PRIOR ART.
  - N35: microcosm drift substitution: OPEN.

  *Applied.*
- **BK-P14 — `tools/check_consistency.py`.** `theory/BOOKENDS.md` is added to MAINTAINED. The script's work moves into `main()` (no `chdir`/`sys.exit` at import), so pytest can collect `tools/`. `test_check_consistency.py` reads the current version instead of a hard-coded one, and exposes a pytest test. *Applied.*

---

## 7. Open questions

1. **The mapping lemma and the finite-horizon bound (§2.0.3).** MATH_LOGIC round 2 checked the lemma's algebra and the bound under its supermartingale condition. Still owed: the case where the structure alters its feed (A1 fails), and the **mixing-adjusted (Markov) form** of the bound.
2. **Operational BK-SEM.** A scrambling intervention at fixed fluxes with a dose-matched sham, for storms, galaxies or planets. It is probably infeasible outside designed systems, so those placements stay CLASSIFICATION.
3. **A persistence filter as selection.** Doolittle 2014 argues qualitatively that it is selection, and that persistence-promoting traits accumulate even at n = 1. Nobody has given it an Axiom-7 resolution ε. The claim that its ε is large is a HYPOTHESIS here.
4. **Density versus readability.** Gravity guarantees only that the densest possible store (a black hole) is unreadable on useful time scales. Below that limit no physical principle links density to read cost. DNA is very dense and read routinely. O5/BH-1 is an empirical hypothesis about selected storage hierarchies.
5. **The t1908 disagreement** (is the physics decorative?) stays OPEN. SENSE-CELL-MATCHED is the test.
6. **Theorem P's stochastic internal-model conjecture** (GENERAL_THEOREM §2). If proved, it would tie Theorem P's *amount* of information to the IMP's *structure*, closing the gap between §2.0.2's rows.
7. **A redundancy-aggregation result** that gives "fragile only to correlated shocks" without fungible buffers (for the biosphere argument).
8. **Consciousness:** out of scope.
9. **Field status:** every real-system row in §4 is untested. GTAO stays **untested, not refuted**.

---

## References

Marks: (abstract), (page) or (metadata only) = opened by this author this session; (litmap) or (via SCALE_ENDS) = DOI already in the repo.

- Caldeira K, Kasting JF 1992, "The life span of the biosphere revisited," *Nature* 360:721–723, doi 10.1038/360721a0 (metadata only; named per PHYSICS F12)
- Barkai N, Leibler S 1997, "Robustness in simple biochemical networks," *Nature* 387:913–917, doi 10.1038/43199 (abstract)
- Briat C, Gupta A, Khammash M 2016, "Antithetic integral feedback ensures robust perfect adaptation in noisy biomolecular networks," *Cell Syst* 2:133, doi 10.1016/j.cels.2016.02.010 (metadata only)
- Cao Y, Wang H, Ouyang Q, Tu Y 2015, "The free-energy cost of accurate biochemical oscillations," *Nat Phys* 11:772–778, doi 10.1038/nphys3412 (abstract)
- Chen Z-Q, Benton MJ 2012, "The timing and pattern of biotic recovery following the end-Permian mass extinction," *Nat Geosci* 5:375–383, doi 10.1038/ngeo1475 (metadata only)
- Di Paolo EA 2005, *Phenom Cogn Sci* 4:429, doi 10.1007/s11097-005-9002-y (abstract)
- Doolittle WF 2014 (online 2013), "Natural selection through survival alone, and the possibility of Gaia," *Biol Philos* 29:415–423, doi 10.1007/s10539-013-9384-0 (page: abstract and notes)
- Egan CA, Lineweaver CH 2010, *ApJ* 710:1825, doi 10.1088/0004-637X/710/2/1825 (abstract, arXiv 0909.3983)
- Eigen M 1971, *Naturwissenschaften* 58:465, doi 10.1007/BF00623322 (via SCALE_ENDS)
- England JL 2013, *J Chem Phys* 139:121923, doi 10.1063/1.4818538 (abstract); England 2015, *Nat Nanotechnol* 10:919, doi 10.1038/nnano.2015.250 (litmap); Perunov N, Marsland R, England JL 2016, *PRX* 6:021036, doi 10.1103/PhysRevX.6.021036 (litmap)
- Francis BA, Wonham WM 1976, "The internal model principle of control theory," *Automatica* 12:457, doi 10.1016/0005-1098(76)90006-6 (litmap; title verified)
- Frank AA, Grinspoon D, Walker SI 2022, "Intelligence as a planetary scale process," *Int J Astrobiol* 21:47, doi 10.1017/S147355042100029X (abstract)
- Frank SA 1995, "Mutual policing and repression of competition in the evolution of cooperative groups," *Nature* 377:520, doi 10.1038/377520a0 (abstract)
- Friston K 2010, doi 10.1038/nrn2787; 2013, doi 10.1098/rsif.2013.0475 (litmap); Friston K et al. 2023, doi 10.1016/j.plrev.2023.08.016 (via SCALE_ENDS)
- Hayden P, Preskill J 2007, *JHEP* 09:120, doi 10.1088/1126-6708/2007/09/120 (via SCALE_ENDS)
- Hordijk W, Hein J, Steel M 2010, "Autocatalytic sets and the origin of life," *Entropy* 12:1733–1742, doi 10.3390/e12071733 (metadata only)
- Kauffman SA 1986, doi 10.1016/S0022-5193(86)80047-9 (via SCALE_ENDS)
- Kolchinsky A, Wolpert DH 2018, *Interface Focus* 8:20180041, doi 10.1098/rsfs.2018.0041 (abstract)
- Krauss LM, Starkman GD 2000, *ApJ* 531:22, doi 10.1086/308434 (via SCALE_ENDS)
- Kussell E, Leibler S 2005, doi 10.1126/science.1114383 (via SCALE_ENDS)
- Lan G, Sartori P, Neumann S, Sourjik V, Tu Y 2012, "The energy–speed–accuracy trade-off in sensory adaptation," *Nat Phys* 8:422–428, doi 10.1038/nphys2276 (abstract)
- Lin AL, Hagberg A, Meron E, Swinney HL 2004, "Resonance tongues and patterns in periodically forced reaction-diffusion systems," *Phys Rev E* 69:066217, doi 10.1103/PhysRevE.69.066217 (abstract)
- Ma W, Trusina A, El-Samad H, Lim WA, Tang C 2009, "Defining network topologies that can achieve biochemical adaptation," *Cell* 138:760–773, doi 10.1016/j.cell.2009.06.013 (abstract)
- Lee, Flack & Krakauer 2024, "Constructing stability: optimal learning in noisy ecological niches," *Proc R Soc B* 291:20241606, doi 10.1098/rspb.2024.1606 (litmap)
- Lenton T, Daines S, Dyke J, Nicholson A, Wilkinson D, Williams HTP 2018, *Trends Ecol Evol* 33:633–645, doi 10.1016/j.tree.2018.05.006 (abstract)
- Lilly SJ, Carollo CM, Pipino A, Renzini A, Peng Y 2013, "Gas regulation of galaxies," *ApJ* 772:119, doi 10.1088/0004-637X/772/2/119 (abstract; authors per Crossref)
- Lovelock JE, Margulis L 1974, doi 10.3402/tellusa.v26i1-2.9731; Watson AJ, Lovelock JE 1983, doi 10.3402/tellusb.v35i4.14616 (litmap; abstract not available)
- Mitchell A et al. 2009, *Nature* 460:220, doi 10.1038/nature08112; Tagkopoulos I, Liu Y-C, Tavazoie S 2008, *Science* 320:1313, doi 10.1126/science.1154456 (litmap)
- Ostrom E 2010, *AER* 100:641, doi 10.1257/aer.100.3.641 (litmap); Ostrom 1990 (classic; THEORY §6)
- Flack JC 2012, doi 10.1098/rstb.2011.0214; Flack 2017, doi 10.1098/rsta.2016.0338 (litmap)
- Prigogine I 1978, doi 10.1126/science.201.4358.777 (via SCALE_ENDS)
- Pross A 2011, *J Syst Chem* 2:1, doi 10.1186/1759-2208-2-1 (abstract)
- Ratnieks FLW 1988, "Reproductive harmony via mutual policing by workers in eusocial Hymenoptera," *Am Nat* 132:217–236, doi 10.1086/284846 (metadata only)
- Rosen R 1985, *Anticipatory Systems* (litmap; book not fetched)
- Rubin S, Parr T, Da Costa L, Friston K 2020, "Future climates: Markov blankets and active inference in the biosphere," *J R Soc Interface* 17:20200503, doi 10.1098/rsif.2020.0503 (abstract)
- Sagawa T, Ueda M 2009, *PRL* 102:250602, doi 10.1103/PhysRevLett.102.250602 (via SCALE_ENDS)
- Sana H et al. 2012, "Binary interaction dominates the evolution of massive stars," *Science* 337:444, doi 10.1126/science.1223344 (page summary)
- Smolin L 1992, doi 10.1088/0264-9381/9/1/016; 2004, arXiv hep-th/0407213 (via SCALE_ENDS)
- Sterling P 2012, *Physiol Behav* 106:5, doi 10.1016/j.physbeh.2011.06.004 (litmap)
- Still S, Sivak DA, Bell AJ, Crooks GE 2012, *PRL* 109:120604, doi 10.1103/PhysRevLett.109.120604 (litmap; wording and setup as quoted by PHYSICS F1/F8)
- Vasas V, Szathmáry E, Santos M 2010, *PNAS* 107:1470, doi 10.1073/pnas.0912628107 (abstract)
- Vasas V, Fernando C, Santos M, Kauffman S, Szathmáry E 2012, "Evolution before genes," *Biol Direct* 7:1, doi 10.1186/1745-6150-7-1 (abstract)
- Walker JCG, Hays PB, Kasting JF 1981, *J Geophys Res* 86:9776, doi 10.1029/JC086iC10p09776 (metadata only)
- Woelfle MA et al. 2004, doi 10.1016/j.cub.2004.08.023 (via SCALE_ENDS)
- Yachi S, Loreau M 1999, "Biodiversity and ecosystem productivity in a fluctuating environment: the insurance hypothesis," *PNAS* 96:1463, doi 10.1073/pnas.96.4.1463 (abstract)
- Yi T-M, Huang Y, Simon MI, Doyle J 2000, "Robust perfect adaptation in bacterial chemotaxis through integral feedback control," *PNAS* 97:4649, doi 10.1073/pnas.97.9.4649 (abstract)
- Petrov V, Ouyang Q, Swinney HL 1997, "Resonant pattern formation in a chemical system," *Nature* 388:655–657, doi 10.1038/41732 (metadata only; named per PHYSICS F11)
- Project files as cited by path and section.
