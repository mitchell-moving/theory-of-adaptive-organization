# Frontier-form re-read of past field attempts (22 November 2026)

*Sunday 22 November 2026, about 12:20 AM ET (America/New_York). Written on branch `frontier-reread-2026-11-22` beside `main` `b421b22` (PR #156 directions note merged). This is a planning note for agreed step 4 (DIRECTIONS §1.3): a read-only re-analysis of past real-data and field attempts under the frontier form, then a proposal for one new preregistered real-data test. It is **not a lock, not a prereg and not a result**. It adds no CLAIM_MAP row and changes no status. No locked prereg is re-scored, no past RESULTS file is edited, and no new data are scored. Misses are open misses to diagnose, not outcomes to patch. The hypothesis sentence is unchanged: "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment."*

*Status against current main (23 November 2026). This note is proposed for main so the path already cited by `theory/TEST_SEARCH_2026-11-22.md` is present. It remains **not a lock, not a prereg and not a result**. Later work: TEST_SEARCH continued the search for a public comparison that can fail; DIRECTIONS Direction A (AI agents) has since been developed on main as `theory/SWARM_RULE_2026-11-23.md` and `applications/AI_AGENT_OVERSIGHT_2026-11-23.md`. The attempt-by-attempt diagnoses in §§2–5, and Candidate A in §6.1 (an antitone test of in-use package designs, with the world measured from upstream cadence on no-account sources), were not otherwise folded into main. Candidate A stays a recommendation, not a preregistration. OPEN_WORK T31 points here.*

**The question.** Additive \(J = \kappa I_{\mathrm{mem}} + hK + w\mathbb{E}[\ell] + A + L\) subject to \(P(\mathrm{ruin})\le\varepsilon\) may be a special case. The candidate general form is a price-free Pareto frontier over memory held, information bought, error, attention and ruin risk; prices only pick the point. Did past field attempts stall because they tried to score a point on that front (a weighted-sum minimum) where a dominance or ordering prediction would have been testable instead?

**The short answer.** Sometimes the interpretation changes; rarely does that, by itself, make a stalled attempt a fair official test. DIR1 was already a price-free directional test and was INCONCLUSIVE. PRICE_FREE (21 November) and REVEALED_PRICES already recorded that dropping absolute fitness-unit prices leaves a narrower bottleneck: a distinctive relation, a measured world, and a class that can qualify. The frontier form adds one genuinely different official question — is a selected design strictly inside the front, with no measurable reason? — which almost no past attempt scored. That question is weaker than minimizing additive \(J\), is prior art as geometry (Farrell, Debreu, Geoffrion, Shoval; already in SHANNON S2–S3 and CORE), and becomes a test of this theory only when the feasible set is bounded from the world's statistics and the information floors, not fitted to a cloud of traits.

## 0. What was read, and what is already in the repository

Before anything below is called new, the tree was searched (THEORY.md, CORE.md, FRAMEWORK.md, [`history/2026-11-12_X_POST.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-12_X_POST.md), CLAIM_MAP section H and P, tests/, prereg/, theory/measured/, PRICE_FREE, REVEALED_PRICES, DISCRIMINATING_CANDIDATES, VIS1F_DROP, FIELD2_FEASIBILITY, DIRECTIONS, SHANNON, OPEN_WORK §8, litmap/LEFT_ON_THE_TABLE.md). Already on the record, and not presented as new:

- CORE already states the split: selected systems sit near the world's frontier (the technical half, which needs no prices) and at the point their prices select (the allocative half). SHANNON Theorems S2–S3 already define a price-free frontier of \((I, r, K, D)\) and the weighted-sum equivalence under convexity.
- PR #154 §7 (OPEN, not merged; `theory/REPRESENTATION.md` on `representation-2026-11-21`) states Hypothesis F (CLAIM_MAP V5 OPEN): a selected design lies on the Pareto front of \((I_{\mathrm{mem}}, \iota, e, a, \rho)\). Theorem F1 / V6: every positive-price minimizer is Pareto; the converse needs convexity (the three-point dent is the miss); a coordinate cap \(\rho\le\varepsilon\) on a convex score set preserves convexity; a chance constraint that is not a half-space in the scored coordinates can still break it. The antitone shape of the front and the information floors survive with no prices. CT33 and Master Theorem (ii) need a stake (or another parameter) with single crossing; they are not fully price-free. \(K^\star(R)\), CT24 shares and \(d/(2\beta)\) need a ratio or a scalar cost. Layer caps survive as dominance only under an extra monotonicity.
- PRICE_FREE already classifies scalar theorems into price-free, price-ratio-only and absolute-price, and short-listed PF2, PF7 and PF6/PF10. REVEALED_PRICES already found that the binding constraint after dropping fitness units is distinctiveness plus a measured world, not prices, and locked nothing. DIR1 already ran D1–D5 on the published record (INCONCLUSIVE; D5 unscored, \(n=2\)).
- DIRECTIONS §1.3 already asked the two questions this note checks attempt by attempt: is a selected system strictly inside the front with no measurable reason; which way does it move along the front when stakes or drift change?

PR #154 is still in review. Statements about V5/V6 and the coordinate-cap correction are taken from that OPEN draft, not treated as merged.

## 1. How the frontier form changes a test (the rule used below)

An attempt **depended on a point** when the official prediction located a unique design, a numerical \(K^\star\) or \(\tau^\star\), a currency saving, a cost share, or an exact slope or elasticity that cannot be formed without a weight or a price ratio.

An attempt was already **price-free (dominance or ordering)** when it scored a sign, an antitone relation, a floor as a constraint, or “not strictly dominated.” Comparative statics in a stake or drift (DIR1 D1–D4, CT33, CAISO year-to-year \(w\)) are ordering predictions, but they still need that parameter (PR #154 §7.3). They are not fully price-free in the frontier sense.

Under this re-read, an attempt:

- **changes** if a dominance or ordering prediction, writable from the same measured coordinates, would have been testable without fixing prices, and the official result hinged on a point-like quantity;
- **stays the same** if the official prediction was already price-free, or if the binding blocker was qualification, a missing world, an instrument, prior art, or power — not prices;
- **would be worse** if rewriting the official miss as a frontier pass would patch a locked prediction, or if a price-free structural claim would collapse into a named rival (whitening, any \(S+wE\) optimizer, Chow / five-minute-rule engineering).

No official status is moved by this classification.

## 2. Inventory: every past real-data or field attempt found

“Attempt” here means a preregistered or locked-prediction test, a scored literature check, a qualification or feasibility gate that stopped a planned field test, or a CLAIM_MAP section-H row whose data were public. In-silico and purely numerical runs are listed in §3 so they are not mistaken for missing field tests. Official wording is taken from the cited RESULTS or CLAIM_MAP files.

| ID | Attempt | What was predicted | Data | Official result (as recorded) | How it was diagnosed | Frontier verdict |
|---|---|---|---|---|---|---|
| F-BIO1 | BIO1 | Memory / adaptation timescales track environmental drift (T1); energy–accuracy; immune lifetime tracks pathogen drift (P3a); ant trail fade untested | Published papers (literature test; not blind) | Core qualitative claim holds at every scale checked, but is almost entirely prior art; P3a contradicts the naive “shorter memory when the pathogen drifts faster”; global contradiction rule not met | Prior art must be credited; P3a later revisited in COLLAPSE1 as partly a half-life artifact | **same** |
| F-COL1 | COLLAPSE1 | Timescale collapse across substrates; exponent-space and code-need checks | Papers plus codebases (numpy, django, rails); SEC-derived firm tables | Timescale collapse not diagnostic (selection bias; slopes did not sort by class). Immune “half-lives” largely a measurement artifact. Code re-edit need is a power law, exponents ~0.6 | Artifact, not a clean class test; CLAIM_MAP H17/H18 later NOT A TEST (qualification not established; proxy failed) | **same** |
| F-MAT1 | MATCH1 news / need exponents | Memory decay exponent matches need exponent in the same system, within a locked band | ABC headlines; Meeter et al. 2005 recall; Wikipedia; 26 repos | Exact match **fails** on news (need ~0.71–0.78, memory ~0.24; ratio outside [0.5, 2]). Power-law *form* survives (prior art). Cross-domain need exponents 0.6–0.8 later **NOT EVIDENCE** (H10) | Recurrence is not drift; heterogeneity; Anderson’s scaled-exponent model | **same** |
| F-MAT2 | MATCH1 measles freeze-or-hold | Need decays steeply; memory should be decoupled (“frozen”) | tsiR measles; Antia 2018 antibodies | Passed its preregistered freeze test on this proxy; CLAIM_MAP H9 **NOT A TEST** (qualification not established; proxy: passed). Substance prior art (Mayer 2016) | Town-level presence ≠ individual exposure; small informative lags | **same** |
| F-DR1 | DRIFT1 | Which public domains are scale-free (T7’s condition) | GitHub, Wikipedia, EDGAR, NYC 311; person-scale arm withheld | Mixed: 311 mostly scale-free across items, not in time; Wikipedia peaked across items; GitHub range too short; EDGAR bunched. CLAIM_MAP H20 **OPEN** (event rates, not target drift \(q\)) | Proxy for \(q\); quantization; calendar leakage | **same** |
| F-C3 | C3 | Shock \(\times\sqrt{\tau}\div\) buffer predicts open-source dormancy; \(\tau\) coefficient and interaction | 896 PyPI/GitHub projects | Under the prereg text, **INCONCLUSIVE**; \(\tau\) coefficient about zero in every version; buffer works (known). CLAIM_MAP H15 **NOT A TEST** (qualification not established; proxy: failed) | \(\sigma\) is demand, not an exogenous shock; \(\tau\) partly tracker habit; one event-coding discrepancy | **changes** (see §4) |
| F-C3b | C3b | Follow-up index / mechanism test | Pre-shock screen, \(n\) bound 2,294 | **Not run.** MV10 power gate not met at the largest \(n\) the frame supplies; stages 3–6 not started | Power and collinearity, not prices | **same** |
| F-F1 | F1 | Same index on US public firms (bankruptcy) | SEC XBRL, 4,112 firm-cohorts | Prereg **INCONCLUSIVE** (no locked fail rule fired; hit criteria failed). Slow cost adjustment predicts bankruptcy, but that is published cost stickiness and, exploratorily, mostly fixed-cost share. CLAIM_MAP H14 **NOT A TEST** (qualification not established; proxy: failed) | \(\tau\) overlaps operating leverage and thin margins | **changes** (weakly; see §4) |
| F-DB | DECISIVE banks | \(\tau\) predicts failure at fixed shock and buffer; identity / elasticities | FDIC, 7,837 banks, 419 failures 2008–14 | Sign-only, not a HIT; identity and some elasticity predictions failed. CLAIM_MAP H11 **NOT A TEST** (qualification not established; proxy: failed) | Proxy and qualification; sign is the known part | **changes** |
| F-DG | DECISIVE glucose | Fixed-spread slope \(-1\) (sampling-corrected target also locked) | REPLACE-BG and Shanghai T1D | Sign right, size off on the full sample; the literal slope rule fired. CLAIM_MAP H12 **NOT A TEST** (qualification not established; proxy: failed) | Sampling, proxy, qualification; not a field miss of the class | **changes** |
| F-DP | DECISIVE populations | Fixed-spread slope (literal and sampling-corrected) | GPDD, 274 series | Sampling-corrected target met in the prereg write-up; the literal slope rule fired; cold-regime and collapse checks failed. CLAIM_MAP H13 **NOT A TEST** (qualification not established; proxy: failed) | Same family as glucose | **changes** |
| F-DIR1 | DIR1 | Price-free signs D1–D5 on the published record (QC tier) | 220 records screened, 42 included after coding corrections | **INCONCLUSIVE.** Pooled 29/42; animals support (20/27); firms fail the class gate (6/10); cells \(n=5\) do not count. D5 unscored (\(n=2\)). D1–D4 do not separate \(J\) from any \(S+wE\) optimizer | Two animal minuses diagnosed (site fidelity; fat draw-down). Firm nulls include threat-rigidity humps | **same** |
| F-SX | STAKES_EXOGENOUS | Identify stakes \(w\) on CAISO forecast error \(\times\) price spread, to locked precision | CAISO OASIS, 2024 and 2025 | **INCONCLUSIVE:** sign positive in both years; primary-year precision gate failed (half-width \(0.70\,\hat w>0.5\)) | Errors-in-variables; one-year precision | **same** |
| F-SS | STAKES_SHIFT_CAISO | When \(w\) changes, forecast MSE moves with the locked elasticity | Same CAISO system, 2024–26 | **INCONCLUSIVE** by gates: G0 failed (stakes fall not established on the like-for-like error), G2 failed (naive MSE rose \(2.17\times\)). The earlier “\(4\times\) fall” in \(w\) is mostly a proxy artifact | Weather-year, BTM solar in “actual” load | **same** (still needs a stake) |
| F-LFK | LFK_SPF | SPF forecasters vs the optimal noisy filter of each variable’s spectrum | Philadelphia Fed SPF | **INCONCLUSIVE** (fewer than 8 variables passed the gates; \(n=6\)). Underpowered by the pre-lock dry run | Sample size; MV8 | **same** |
| F-SPN | SPF_NOISE_PROXY | White-observation-noise premise of a dispersion proxy; contamination pattern | SPF (subset) | White-noise premise **failed** on the locked tests; priced-variable contamination **inconclusive** | Broad contamination, not a clean \(N\) | **same** / slightly **worse** for a filter-point test |
| F-SPR | SPF_RIGIDITY_OOS | Out-of-sample rigidity vs optimal \(\beta^G\) | Nine unseen SPF variables | **GATE NOT MET**; no prereg locked; no outcome computed | MV10 | **same** |
| F-D3 | D3_OOS | Renewal vs Cox on held-out GitHub and Wikipedia series | 27 repos; 5 Wikipedia groups | Some non-discriminating checks passed on proxy; the renewal hypothesis failed on a within-file gap-correlation proxy | Process class, not prices | **same** |
| F-LAB | LAB_AKLMT_TAU | Implied persistence of lab forecasts moves with \(\rho\) as the optimum does | AKLMT Exp. 1 (MTurk) | **Passed on proxy, at the boundary.** Participants moved about 53% of the optimum’s move; the point 0.98 is missed by many SE. Lab humans are not a strongly selected class | Conservative CI; causal-contrast sensitivity recorded as a later item | **same** |
| F-KER | KERNEL_MEASURE | A tracking kernel can be measured (VIX on Parkinson variance) | Public VIX / range-variance series | **PASSED on proxy**, exploratory, not decisive; first kernel measured in any GTAO test | Exploratory; not a hypothesis test of the class | **same** |
| F-SEN | SENSE-CELL | Sensing-class \(\theta\), \(\beta_{\mathrm{phys}}\in[1,10]\), cell-vs-neuron ordering | Keegstra 2017 source data; Lan 2012 floor | Locked H2 output FAIL, then re-labeled **INCONCLUSIVE** (proxy mismatch). H1 and H3 **INCONCLUSIVE**. H4 data gap | Floor vs mixed-array accuracy; Method A/F disagreement | **changes** (mildly) |
| F-WD | WIKIDATA-BAND | Signs only: lookup rises with drift; shared-store benefit with \(N\); hold vs freeze | Wikimedia APIs, 2,693 pages | Known-groups instrument **failed**, so the instrument does not count. P1–P3 **INCONCLUSIVE**; P4 **PASS** on proxy, weak. Tier 3 | Store corrections counted as drift; policy/template-driven mode; empty regime-A set | **same** |
| F-VIG | vigil-ona | Outside-unit advice-seeking rises with rank (and related elasticities) | Four published ONA networks (Krackhardt, Lazega, Cross & Parker) | H1–H3 **PASS** on the locked directional rules, Tier 3, also predicted by Mintzberg. Leave-one-out without Lazega loses H1/H2. H8 (firms as a whole) stays **OPEN** | Small networks; one study dominates the pool; no named driver | **same** |
| F-SN1 | SN1 / SN1-F1 | Store-noise inequality \(\lambda\tau\ge(1-s)/(2s)\) on a new system; Model S in a counting-limited relative | Seven candidate systems in locked order | **0 of 7 scorable.** SN1-F1 **INVALID** (V. ordalii noise is \(6.6\times\) the counting bound) | The binding input \(s\) has been measured, as found, only in *E. coli* | **same** |
| F-EC1 | ECOLI-MEM P1/P3/P4 | \(\tau^\star\) minimizes \(J\) at the measured world (Model S); rival “set at \(\tau_v\)”; degree-2 world gets two stores | Mattingly et al. 2021 and locked box; not blind to the measured 9.9 s | Arm B: predicted 1.09–1.17 s vs 9.9 s, **failed on this proxy/setup**. Rival also failed. Two-store count passed, weakly. CLAIM_MAP P1/P3 **NOT A TEST** (qualification not established; proxy: failed); P4 **NOT A TEST** (proxy: passed). Not a qualifying test of the class | Binding noise is the store’s own; objective and Model S are part of the miss | **changes** (interpretation; not a re-score) |
| F-EC2 | ECOLI F2, D, Y4, qualification | Noise vs memory exponent; remaining factor (objective, speed price, habitat); class \(\sigma,N_e,T_{\mathrm{red}}\) | Park 2010, Keegstra 2017, Lan dissipation, literature | F2 **INCONCLUSIVE** (neither noise model). Remaining-factor arms inconclusive or untested (Y4). Qualification record: **NOT ESTABLISHED** (item (b) \(N_e\) later established; (a),(c)–(e) not) | Missing term, then an open remainder; no fitness map | **same** on the blockers that remain |
| F-GR | GRID-1, 1b, 2, 3, 4/4b, S, DX | Layer count by degree and interlacing; world vs market mode; GB qualification; cost-minimizing count and sterling saving; cross-grid rank of closeness to the minimum | Open TSO/NESO/Netztransparenz and related public files, with many later 403 / account / form gates | GRID-1 **INVALID** by premise. GRID-2/3: GB **not qualified** (\(N_e=1\)); G1 **FAIL on proxy** (four layers vs a one-layer sensing-limited prediction under ruin slack). GRID-S: slow German mode stayed near 50–55 min after the market step changed (supports “world,” not the market-step account, on that proxy). DX Part B **INCONCLUSIVE** (ruin binds; saving needs measured \(h,w\)). P25 / GRID-CROSS **UNTESTED** (only one complete \(d_1\); class not qualified; leave-one-out and power limits at \(n_{\min}=5\)) | Ruin binding vs waste; engineered product times; missing pre-control spectra | **changes** (ruin as a coordinate; priced saving stays blocked) |
| F-VIS | VIS-1F | Priced cutoff or count in dipteran early vision vs whitening (Pass 1 only; not locked) | Laughlin 1998, Niven 2007, Markow & Manning 1980, van Hateren series (opened or Crossref-checked; no official Pass 1 fit) | **DROPPED** under the written pre-Pass-1 rule: \((h,w)\) not both sourced independently, and L3 left both a finite \(K^\star\) and a priced cutoff undefined. The outline forbade a price-free structural path | No error-cost curve; metabolic cost per bit is not \(w\); continuum of time scales | **changes** (a new dominance prereg is thinkable; as a test of the hypothesis it may be **worse**) |
| F-F2 | FIELD2 feasibility | Cross-field ladder ratios need \(\theta\), \(\gamma\), and an observed tier ladder | Five-minute-rule papers; non-silicon candidates | Not a test. Cache \(\gamma\) compiled as an anchor, not independent support. Recommendation (not locked): research-library print storage, conditional on a Pass 1 \(\theta\) check | \(\gamma\) is itself a price-latency exponent; silicon is engineered | **same** / **worse** as independent support |
| F-REV | REVEALED §9 search | Fair-test requirements R1–R4; find a discriminating public dataset | Dunlap figshare, Sung/Lynch tables, Tetrahymena Dryad, chipmunks (no deposit), wolf Dryad | **Decision: nothing locked.** Best-formed open set (Dunlap 2017 bees) is not discriminating. Binding constraint: R3 plus a measured world, not prices | Classic sampling model already tested; lab task; no selection ranking | **same** |
| F-H | Earlier CLAIM_MAP H rows not already above (H1–H8, H16) | News-recall slope; PIAAC supervisor reading, specificity, span, size; Enron external mail share; firm vigilance; BIO1 P3a as a map row | PIAAC, Enron corpus, news-recall studies (not re-opened this session) | H1, H2, H7 **NOT A TEST** (qualification not established; proxy failed). H3 **NOT A TEST** (proxy passed; prior art). H4–H5 **OPEN** (proxy nulls). H6 **NOT EVIDENCE**. H8 **OPEN**. H16 **OPEN** | Instrument and qualification, not a missing price | **same** |
| F-SELF | night2 SELF | Ace’s own change rates and attention vs drift and stakes | This bot’s logs, not a field class | P1b and P2 **INCONCLUSIVE**; a deadline rival fits attention much better | Not a test of the law in nature | **same** (out of class) |
| F-RS | ROBUST-SLACK | Reserves above a plug-in minimum, growing with world uncertainty | **No dataset chosen** at lock | Prereg exists; not a completed attempt | — | not scored |

SN1, GRID-4b, Y4, C3b, SPF_RIGIDITY_OOS, GRID-CROSS and VIS-1F are attempts that stopped before a hypothesis verdict. They are included because the question is whether the frontier form would have made them runnable.

## 3. In-silico and numerical attempts (not field tests)

These were found in the same sweep and are listed so the inventory is not silently incomplete. They are designed worlds or numerical checks. Prices, when they exist, are set by the experimenter (the T30 path). The frontier form does not turn them into field tests.

| Attempt | Official result (as recorded) | Note |
|---|---|---|
| EVO1 | PC, W1, W2 passed on the proxy; W3 INVALID (ruin gate); W4 and W4b failed on the proxy (reachability / valley; W10); S031 and S07 inconclusive | Designed-world evolution; reachability is a dynamics question (DIRECTIONS §3), not a price question |
| ANTS1 | NOT EVIDENCE by construction; three SIM-FAILs (`reviews/night1/ANTS1_WRITEUP.md`) | Simulation |
| LEARNSIM | Mixed INCONCLUSIVE / some in-model passes; T3 private-drift cells inconclusive; several text-vs-code disagreements moved toward INCONCLUSIVE | Designed learners; T3 signs are already price-free and still mostly unscored there |
| ONSET_ACROSS_ALPHA | PASSED in-model (onset exponent independent of \(\alpha\)) | Simulation of PF10’s technology-not-\(\alpha\) piece |
| LOCK1 | Mostly FAIL in-model (rhythm / locking rows); B4 PASS | Numerical; not field |
| T25 WF-HSV, T27, T28 SIM-1, and other in-model official runs in OPEN_WORK | As recorded there (T25 and T27 FAILED in-model; T28 PASSED in-model) | Not re-read as field attempts |

## 4. Attempt by attempt: does the frontier form change the interpretation?

**Already price-free, so the official result stands as a frontier-relevant result.** DIR1, WIKIDATA-BAND, vigil-ona, DRIFT1, MATCH1’s freeze-or-hold arm, BIO1’s qualitative tracking claim, and the sign parts of DECISIVE/C3/F1 were not waiting on fitness-unit prices. DIR1 is the one completed official price-free field test: INCONCLUSIVE, with firms failing and D5 unscored. That does not become a pass under a new geometry. PR #154 also says the stake- and drift-conditioned signs still need a parameter with single crossing. CAISO (STAKES_EXOGENOUS, STAKES_SHIFT) therefore stays in the same bin: the test needed a measured stake change, the clean proxy did not establish one, and dropping prices does not replace that lever.

**The official prediction was a point; a dominance or ordering question is weaker and sometimes still open.** This is the live change, and it must not be used to rewrite a locked file.

- *E. coli* P1/P3 scored a unique \(\tau^\star\) under Model S and a chosen objective. That is a point on a scalarization. Under Hypothesis F, a 9.9 s memory can be undominated if it cuts error, store-generated noise, or ruin relative to a 1.1 s store. The repository already diagnosed the missing store-noise term and an open remainder; F2 did not close it. That is an open miss, not a reason to treat P1 as passed. Qualification is still not established. A *new* dominance comparison among attested designs would not need fitness-unit \((h,w)\). It would be a new prereg, and the contamination risk is high (the same papers were read before and after the P1 lock).
- GRID G1 and DX Part B compared a four-layer suite to a one-layer sensing-limited \(K^\star\) under ruin slack, and could not score a sterling saving without \(h\) and \(w\). On the frontier, extra layers that do not cut tracking error can still be undominated if they cut ruin risk. GRID-DX already said the ruin constraint binds; the frontier form is the right language for that diagnosis. A dominance test in (holdings, lag, residual imbalance, a published LOLE or largest-loss coverage) might be writable without fitness units. The blockers that remain are qualification (\(N_e=1\) for GB), missing pre-control \(d_1\) for a cross-grid front, and engineering circularity. The priced saving stays blocked.
- C3, F1 and DECISIVE locked an index or a slope (a scalar \(J\) form). A price-free ordering is “higher \(\tau\) does not go with lower ruin at fixed shock and buffer.” Banks already showed that sign. Glucose and populations had the right sign and the wrong literal slope. C3’s \(\tau\) coefficient was about zero, so even the sign was absent on that proxy — an open miss that a frontier re-label does not remove. None of these become official support without a new lock, and none were qualifying tests of a class.
- SENSE-CELL’s numeric band \(\beta_{\mathrm{phys}}\in[1,10]\) is a tightness-to-floor claim (a scale). The ordering “cells sit closer to the physical floor than neurons” (H3) is the price-free piece and held in every finite reading, but was not counted as support. The frontier form prefers that ordering over the numeric band. H4 remains a data gap.

**Would be worse, or not a rescue.** Using the frontier form to declare a locked point-miss a pass would be a patch. VIS-1F’s written outline forbade a price-free structural path because a filter shape can be fitted to whitening (efficient coding). A new dominance prereg in (dark ATP, information rate, error) is the kind of thing DIRECTIONS §1.3 flagged, but as a test of *this* hypothesis it may be worse: agreement with Niven / van Hateren / Atick–Laughlin would not discriminate. FIELD2’s \(\gamma\) *is* a price; a tier-dominance plot in storage hierarchies is what the five-minute-rule literature already engineers. REVEALED_PRICES already said the remaining bottleneck is distinctiveness and a measured world; the frontier form does not clear that. SN1, C3b and qualification records were not price-blocked.

## 5. Honest summary

Several stalled attempts did depend on fixing prices or a weighted point (VIS-1F; *E. coli* \(\tau^\star\); GRID savings and \(K^\star(R)\); exact DECISIVE/C3/F1 slopes). For those, a dominance or sign prediction is the fairer official question under Hypothesis F, and that is why the interpretation **changes**. It does not, in the files, produce a qualifying, discriminating, uncontaminated field test that could have been scored already. The attempts that were already price-free (DIR1 first among them) **stay the same**. Rewriting a locked miss, or substituting a Shoval-style fitted trait front for a world-computed feasible set, would be **worse**.

That is the same bottleneck PRICE_FREE §4 and REVEALED_PRICES §9 already named, with one addition: the distinctive official prediction the frontier form actually adds is interiority versus a *computed* front, not another sign from \(S+wE\).

## 6. Three candidate price-free predictions for one new real-data test

None of these is locked. None is a re-score of a past prereg. Qualification under THEORY §3 / FRAMEWORK §9 is not established for any of the classes below; a pass would be at most a proxy result. Cities, nations and the biosphere stay excluded. Lab humans stay excluded as a strongly selected class.

### 6.1 Candidate A (recommended) — antitone / not-strictly-dominated package designs, with the world measured from upstream cadence

**Claim.** In one locked language ecosystem, among packages that remain in use over a locked window, update effort (releases and dependency bumps: attention / information bought) and residual known-vulnerability or pin-staleness (error, with critical unpatched status as a ruin-risk coordinate) are antitone in size-and-age bands: a package is not strictly dominated by another attested package in the same band. Independently, upstream release and advisory cadence (the world) is measured on a split disjoint from the scored residual, so the comparison is not a trait front fitted to the same cloud (the SHANNON / CORE warning about Shoval). The predicted miss is a systematic interior cloud: packages that both update often and remain more stale or more exposed than peers with the same upstream world.

**Public data, verified this session without an account.** HTTP 200, no authentication challenged:

- deps.dev API docs `https://docs.deps.dev/api/` and package endpoint `https://api.deps.dev/v3alpha/systems/NPM/packages/react` (JSON);
- npm registry `https://registry.npmjs.org/react` (JSON);
- PyPI JSON `https://pypi.org/pypi/requests/json`;
- OSV query `https://api.osv.dev/v1/query` (HTTP 200 JSON; a single existence query was sent for the PyPI package name `requests` and was not scored);
- GH Archive hourly dumps, e.g. `https://data.gharchive.org/2024-01-01-0.json.gz` (HTTP 200, `application/gzip`; not downloaded).

**What would fail it.** A preregistered fraction of in-use packages in the band are strictly dominated, or the locked rank correlation of update effort with residual exposure is significantly positive in the wrong direction, after the locked size/age and upstream-cadence controls.

**Why it can fail.** Template copying, fashion, abandoned-but-still-downloaded packages, or genuinely wasteful maintenance can put mass in the interior. The test is not stacked to pass.

**Why it could move the odds.** It is the first official dominance / antitone test aimed at Hypothesis F’s geometry rather than at a priced point, on public no-account data, with a world measured off the scored residual. A clean interior cloud would be a problem for “selected designs sit on the front.” A clean antitone front would be weak support: it is also what any tradeoff, and Shoval et al. 2012, already say, and FRAMEWORK already rates public software as lacking strong selection. The GTAO-specific half (front bounded from the world’s statistics and the floors) is only lightly present, via the upstream-cadence split. That limit should be locked in the open.

**Contamination.** C3, D3_OOS and DRIFT1 already used GitHub and PyPI, but they scored dormancy, gap processes and rate distributions, not this dominance claim. `litmap/LEFT_ON_THE_TABLE.md` already proposed GH Archive plus PyPI/npm for a *different* test (shared-wrapper adoption vs \(N^\star(\rho)\)). FRAMEWORK §5 already ranks public software second among real-world public beds. deps.dev and OSV were not found as scored sources in the tree. Residual risk: ecosystem familiarity from C3/D3. Official scoring must use a locked, dated cohort not previously used as a C3 outcome sample, and must not open the scored residual before lock.

### 6.2 Candidate B — opposite signs of shared versus private drift on the same public software data (PF6 / DIR1 D5, as a measurement test)

**Claim.** For organizations or packages that share an upstream dependency, the later appearance of a shared wrapper or a common pin policy is more likely when shared (upstream) drift is higher and less likely when private (repo-specific) churn is higher, at comparable group size. This is Lemma B3 / FRAMEWORK §6.4 / PRICE_FREE PF6 / DIR1 D5, not a new sign. DIR1 could not score D5 (\(n=2\)). The rival is a single sign for total volatility (contingency / threat-rigidity).

**Public data.** The same verified no-account sources as §6.1 (GH Archive, npm, PyPI, deps.dev).

**What would fail it.** Both factors have the same sign with CIs excluding zero, or the private-drift effect is positive with a CI excluding zero, on the locked adoption outcome.

**Why it can fail.** Orgs copy templates; “shared wrapper” can be policy, not cost; DIR1 already saw firm-level re-centralization under uncertainty.

**Why it could move the odds.** It is the one DIR1 prediction with opposite-sign rivals, still unscored as a measurement test. A clean opposite-sign pair would do more to the odds than another D1–D4 sign. It is only weakly a *frontier-form* test: it is a comparative static that needs drift as a parameter (PR #154 §7.3).

**Contamination.** LEFT_ON_THE_TABLE already wrote this design. C3/D3 used related ecosystems. Not a re-score of DIR1 (DIR1 coded papers, not these series).

### 6.3 Candidate C — dominance among dipteran photoreceptors in (dark ATP, information rate), without a priced cutoff

**Claim.** Across the homologous R1–6 photoreceptors of the species reported in Niven, Anderson & Laughlin 2007, no species’ design is strictly dominated in (dark / fixed ATP cost, information rate under a common stimulus, and any published error or SNR that can be locked without using the same spectra as a fitted cutoff). This is a new prereg, not a re-opening of the dropped VIS-1F outline, and not an official Pass 1 fit to fly kernels.

**Public data, verified this session.** Niven et al. 2007 is CC, DOI 10.1371/journal.pbio.0050116; the publisher printable PDF returned HTTP 200, 721,474 bytes, matching the size already recorded in `theory/VIS1F_DROP_2026-11-21.md`. The paper, not a separate deposit, is the data source.

**What would fail it.** One reported species is worse on every locked coordinate than another, with no locked habitat or body-size covariate accounting for it.

**Why it can fail.** The four species can come in a dominated order; dark cost and rate can move together in the wrong way once size is locked.

**Why it could move the odds — and why it may not.** It asks the dominance question VIS-1F could not ask once \((h,w)\) and L3 failed. It would not move the odds much if it agrees with efficient-coding / whitening accounts already on the record. Qualification is not established. This is the scientific risk the VIS-1F outline named when it forbade a price-free structural path.

**Contamination.** High. Laughlin 1998, Niven 2007, and the van Hateren context were opened in the VIS-1F drop note. Numbers in the PDF have been seen. A lock after those reads is not blind to the likely order of dark cost and rate.

## 7. Ranking and recommendation

1. **Candidate A — recommend this one as the next prereg to draft, not to lock tonight.** It is the only candidate that is both a genuine dominance / antitone test of Hypothesis F and tied to no-account sources that returned HTTP 200 to this client this session. It can fail. It could move the odds if an interior cloud appears. It does not rewrite any locked file. The limits (weak selection, partial distinctiveness, residual C3/D3 familiarity) should be on the first page of any later prereg. Do not lock until a dated cohort, a dominance definition, a world split, and a qualification record are written, and until PR #154’s Hypothesis F wording is either merged or quoted as still OPEN.

2. **Candidate B.** Stronger discrimination (opposite-sign rivals) but less specific to the frontier form; already designed in LEFT_ON_THE_TABLE and attempted, underpowered, as DIR1 D5. Worth a later lock, or a second arm in the same prereg as A if the two outcomes stay disjoint, not as the headline test of the frontier re-read.

3. **Candidate C.** The stalled attempt DIRECTIONS named first, now asked as dominance rather than as a priced cutoff. High contamination and a serious collapse risk into efficient coding. Not the first lock.

Not recommended as the one test, with reasons: *E. coli* dominance on already-read papers (contamination; would look like a patch of P1); GRID physical-coordinate dominance (GB not qualified; \(d_1\) still missing for a computed front); Dunlap 2017 bees (REVEALED already: not discriminating; this session did not re-verify the figshare file as downloadable — the DOI resolved, the figshare landing returned 403/202 to this client); Bedford 2014 HI on Dryad (landing page HTTP 200, CC0, already DATA-VERIFIED 15 November, but file-stream HEAD returned 403 to this client, and freeze/hold on pathogens is prior art plus MATCH1/BIO1 contamination); SPF rigidity (gate, premise, and contamination); InventoryBench (HTTP 200 landing, already rejected for CT12: assigned costs, no observed selected \(T^\star\)).

## 8. Sources fetched or verified this session

No accounts were created, no paywalls were signed into, and no one was contacted. Official test data were not scored. Large bodies (GH Archive gzip, registry JSON, OSV arrays, Dryad files, the Niven PDF) were not used as a result.

| Source | This session | Notes |
|---|---|---|
| deps.dev docs and `.../systems/NPM/packages/react` | HTTP 200 | No account |
| `https://registry.npmjs.org/react` | HTTP 200 JSON | No account |
| `https://pypi.org/pypi/requests/json` | HTTP 200 JSON | No account |
| OSV `POST https://api.osv.dev/v1/query` | HTTP 200 JSON | Existence check only; not scored |
| `https://google.github.io/osv.dev/` | HTTP 200 | Docs |
| GH Archive `https://data.gharchive.org/2024-01-01-0.json.gz` | HEAD HTTP 200, `application/gzip` | Not downloaded |
| Niven et al. 2007 printable PDF | HTTP 200, 721,474 bytes | Matches the VIS-1F recorded size; not re-read as a score |
| Dryad Bedford landing `https://datadryad.org/dataset/doi:10.5061/dryad.rc515` | HTTP 200; license CC0 1.0 | File-stream HEAD 403 to this client; not treated as re-verified downloadable |
| Dryad Mersch landing `https://datadryad.org/dataset/doi:10.5061/dryad.8d8h7` | HTTP 200 | Same limit; not recommended here (FRAMEWORK: no measured foraging-target drift) |
| Figshare / doi 10.6084/m9.figshare.4769539 (Dunlap 2017) | DOI resolved; figshare landing 403/202 | Not treated as verified downloadable this session |
| Philadelphia Fed SPF `meanLevel.xlsx` | HTTP 200 | Already used in LFK/SPF tests; not a new candidate |
| InventoryBench dataset page | HTTP 200 | Already assessed in PRICE_FREE §3.2 |
| NESO data portal | HTTP 200 landing | Not used as a new download |

## 9. What this file is not

It is not a lock, a prereg, a CLAIM_MAP edit, or a status change. It does not recommend sending review requests (DIRECTIONS step 5 still needs Chad). It does not claim a field pass or a field miss of the hypothesis. It does not claim Pareto efficiency, weighted-sum scalarization, or Shoval-style trait fronts as new.

## 10. Checks

Run at `nice -n 19`. `lake build` was not run.
