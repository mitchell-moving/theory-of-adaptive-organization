# Cross-field map: (world exponent, technology exponent) → dimensionless design numbers (21 November 2026)

*Saturday 21 November 2026, written about 11 AM–12 PM ET (America/New_York), on top of PR #134 (`cache-prior-art-2026-11-21`, `a07903c`) and beside PR #133 (`revealed-prices-2026-11-21`, `b8e4c39`). A derivation, a prior-art verdict and a data inventory. **Not a prereg, nothing locked, no field result.** The hypothesis sentence is unchanged: "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." "Proved" means proved in a model, not a claim about nature.*

## 0. The idea, and what is already here

Agreed with Chad (t2050): each field found its own local ladder pattern (Chow in caches and Roundy in inventory via optimization; Benna & Fusi in synapses by cascade design; Jaques empirically in firms). That part is prior art, novelty 0. What only a single law would predict is the **cross-field** part: systems in different substrates whose worlds share the same reuse exponent θ and whose technologies share the same cost exponent γ should share the same dimensionless design numbers, whatever they are made of. **Rival (R0):** each field's numbers are set locally, with no shared dependence on (θ, γ).

Already in the repository (grep of THEORY, CORE, FRAMEWORK, [`history/2026-11-12_X_POST.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-12_X_POST.md), litmap): CT24 (cost shares equal price elasticities, currency-free); T7b and L4 (geometric clocks for items log-uniform in rate, every α in (1, 3), "Roundy-type, known in substance"); CT21 (a single drifting signal, including a self-similar random walk, needs at most one layer); N4 (store count, prior art in form); T20 part A (K\* grows roughly linearly in log stakes R with scale range held fixed, official (A) gates 12/12 in-model; T20 overall not supported because (B) failed); PR #134 (Chow 1974/76, Welch 1978, Jacob et al. 1996 hold the cache versions of all three). "Only dimensionless ratios matter" (THEORY line 36) already says that the same problem has the same answer at every scale. What this note adds is the explicit map, its scope, and the inventory of what would test it.

## 1. Which worlds this covers (scope first)

The map below is for **reuse worlds**: many items or requests whose access rates are spread as a power law, served by a ladder of stores of increasing size and slowness. In repository terms that is the shared-clock, many-items model (T7b, L4), not the single-drifting-signal model. For a single drifting signal CT21 already says a self-similar random walk needs at most one layer, so **no ladder, and no cross-field ratio, is predicted there.** A cross-field test must therefore check, per field, that the world is a reuse world (a measured miss or need curve), not just that something "has power-law statistics".

## 2. Derivation (in-model)

### 2.1 Model

K levels. Level k has capacity s_k and access time (or response time, lag) t_k; s_0 = 1 is the unit of demand and s_K = S is the range that must be covered (the backing level holds everything).

- **World.** The share of demand that misses a store of capacity s is m(s) = s^{-θ}, θ > 0 (the reuse exponent; Hartstein et al. 2006 measure θ ≈ 0.3–0.7 in caches; Breslau et al. 1999 measure Zipf-like request popularity on the web).
- **Technology.** Holding one unit of capacity at access time t costs a·t^{-γ}, γ > 0 (faster storage costs more per unit; Welch 1978's "power function relating speed and cost").
- **Cost of judgment.** In J's terms, upkeep is λ·C with C = Σ_k a·t_k^{-γ}·s_k (h times what is kept), and the expected loss is the mean delay T = Σ_k m(s_{k-1})·t_k (w·E[ℓ] with a loss linear in delay). J = T + λC, ruin slack, no rhythm (see §4).

J is a posynomial in (s, t), so in log variables it is convex: this is a geometric program (as in Chow 1974), and any stationary point is the global minimum.

### 2.2 First-order conditions

Write D_k = m(s_{k-1})·t_k (level k's delay contribution; its share of delay is D_k/T) and C_k = a·t_k^{-γ}·s_k.

- ∂J/∂ ln t_k = 0 gives **D_k = γ·λC_k at every level.** Summing gives **T : λC = γ**, so D_k/T = C_k/C level by level (Chow 1974 Eq. 36; Welch 1978), and the loss share of J is γ/(1 + γ). This is CT24's elasticity reading for this J (for one tracker CT24 gives reads : error = α − 1).
- ∂J/∂ ln s_k = 0 (interior k) gives **λC_k = θ·D_{k+1}.**

### 2.3 The map

With x_k = ln(s_k/s_{k-1}) and y_k = ln(t_{k+1}/t_k) and q = 1/(θγ), the two conditions give y_k = ln q + θx_k and x_{k+1} = ln q + γy_k, so x_{k+1} − x\* = θγ·(x_k − x\*). When **θγ < 1** this contracts to a unique interior fixed point:

| Design number | Value at the fixed point | Depends on |
|---|---|---|
| adjacent capacity ratio r_s | ln r_s = −(1 + γ)·ln(θγ)/(1 − θγ) | θ, γ only |
| adjacent access-time ratio r_t | ln r_t = −(1 + θ)·ln(θγ)/(1 − θγ) | θ, γ only |
| adjacent cost ratio C_{k+1}/C_k (= delay ratio) | q = 1/(θγ) (exact for all finite K, S, even when θγ ≥ 1) | θ, γ only |
| delay share = cost share, per level | exact at every level | none |
| loss : upkeep over the design | γ | γ only |
| levels per decade of range | 1/log₁₀ r_s | θ, γ only |
| number of levels | ≈ ln(S/s_1)/ln r_s (once s_1 is pinned, or K is optimized against per-level upkeep h) | range (the edges) |

The prices (λ, a) and the stakes drop out of every ratio. They and the range set only where the ladder starts and stops. This is the precise sense of the boundary ("holographic") reading in PR #133 §5: **the interior is fixed by two exponents; the edges are fixed by prices and range.** Example with made-up exponents θ = γ = 0.5: r_s = r_t = 16, q = 4, about 0.83 levels per decade.

### 2.4 Checks

`theory/cross_field_checks/chow_map.py` (run by `tools/test_cross_field_map.py`; output in `chow_map.out`): (i) a direct convex solve of the K = 9 program from an even ladder (with S = exp(K·ln r_s) so every level sits on the fixed point) recovers ln r_s, ln r_t, q and D_k/(λC_k) = γ at the middle level to ≤ 4.7×10⁻⁴ relative error in the four well-conditioned cases; (ii) the exact first-order recurrence, started 2× off the fixed point, decays as (θγ)^k; (iii) a direct convex solve with mismatched S ≠ exp(K·ln r_s) (including θγ = 1 and θγ > 1) matches the exact finite-K formula x_k − x\* = (θγ)^{k−1}·(1 − θγ)/(1 − (θγ)^K)·(ln S − K x\*) and exact C_{k+1}/C_k = q to ≤ 3.1×10⁻⁵. Where q > 4 in Part 1, the lowest levels carry less than q^{-K} of J, and BFGS leaves them loose (shown as a diagnostic, not scored); Parts 2 and 3 are exact there.

### 2.5 Consequences that matter for any test

1. **Boundary transient (one-sided).** Because x_{k+1} − x\* = θγ·(x_k − x\*) and Σ_{k=1}^K x_k = ln S, the exact finite-K solution is x_k − x\* = (θγ)^{k−1}·[(1 − θγ)/(1 − (θγ)^K)]·(ln S − K x\*). When θγ < 1, deviations decay **from the small-s (k = 1) edge only** by (θγ)^{k−1} per level, while x_K is closest to x\*. Real hierarchies have three to five levels: with θγ = 0.25, level 2 is within 25% of the level-1 deviation; with θγ = 0.7, level 2 retains 70% of it. (And if K is too large for S, ln S < K x\* − x\*·[1 − (θγ)^K]/(1 − θγ), the unconstrained GP gives x_1 < 0, i.e. s_1 < s_0.) A cross-field test must either predict the full finite-K solution with the edges or restrict to upper levels with θγ small enough. Comparing raw adjacent ratios across fields without this would be unfair to the theory and to the rival alike.
2. **No universal ratio when θγ ≥ 1.** At θγ = 1, ln q = 0 gives x_k = (ln S)/K identically (set by S and K, not by (θ, γ)). When θγ > 1, the forward map repels and deviations decay backward from the large-s (k = K) edge, so the upper-level ratios are set by S and K. The map predicts no shared interior r_s or r_t there (only C_{k+1}/C_k = q).
3. **Only the product θγ and γ enter.** Two fields match only if both agree, so a test needs both exponents in each field, not only the world's.

## 3. Prior-art verdict (hostile search, 21 Nov; four web searches plus Crossref, not exhaustive)

| Piece | Prior art | Verdict |
|---|---|---|
| The map itself, (θ, γ) → constant adjacent ratios, count ∝ log range | **Chow 1974** (*IBM J. Res. Dev.* 18:194, doi 10.1147/rd.183.0194; public mirror `ibmrd1803B.pdf` verified), **Chow 1976** (doi 10.1109/tc.1976.5009230): power-law hit and cost functions give constant ratios of cost, access time and capacity. Chow 1974 Eqs. (36)–(60) already derive the geometric program, cost ratio 1/(θγ) (Eq. 39), the (θγ) recurrence (Eq. 41), and the closed forms for r_s, r_t, and n_opt. | **Novelty 0** in form and domain. §2.3 is a re-derivation of Chow's result. |
| Delay share = cost share per level | **Chow 1974** (Eq. 36, "fractional cost allocations are equal to the relative activity time distributions") and **Welch 1978** (doi 10.1109/tc.1978.1675120), verified. | Novelty 0. |
| Claim that hierarchies in *different substrates* share a ratio set by an optimization's exponents | **Lera & Sornette 2019**, *PLOS ONE* 14:e0214911, doi 10.1371/journal.pone.0214911 (Crossref verified; full text read): optimal discrete hierarchies from productivity vs. coordination cost, with a "universal preferred scaling ratio between 3 and 4" across human and animal hierarchies, set by the model's exponents. **Zhou, Sornette, Hill & Dunbar 2005** (doi 10.1098/rspb.2004.2970): measured ratio near 3, "very much a universal feature". **West, Brown & Enquist 1997** (doi 10.1126/science.276.5309.122; one optimization gives the same exponents across organisms). **Lee, Flack & Krakauer 2024** (doi 10.1098/rspb.2024.1606; a "universal" memory scaling τ_m ∼ τ_E^{1/2}). | The **template** is prior art: "one optimization ⇒ the same dimensionless numbers across substrates". Lera & Sornette is the closest and was **not credited in the repository** before this note. |
| This specific cross-substrate claim: memory or tracking ladders in silicon, synapses, inventory and firms share (r_s, r_t, q) when they share (θ, γ) | None found. Benna & Fusi 2016 (*Nat. Neurosci.* 19:1697, doi 10.1038/nn.4401; arXiv 1507.07580) treat their ratio of successive time scales n² as a free modeling choice, traded off against bumpiness and count, not set by any cost exponent. | **At most novelty 1 (same formula/idea, new domains), unverified.** Under `litmap/PRIOR_ART.md`, grade 2 requires a new formula or test; here the formula is Chow 1974 (0), the cross-substrate template is prior art (0), and no test is locked. A targeted search (econophysics hierarchy papers, the "uniform memory hierarchy" literature, Alpern, Carter & Feig, FOCS 1990, doi 10.1109/FSCS.1990.89581, Crossref verified, abstract read) must precede any public claim. |

What could be distinctive, if anything: not the map, but the bet that it is the **same** map in substrates that never shared engineers, with the reuse-world scope (§1) and the boundary transient (§2.5) stated in advance.

## 4. Where the map breaks

- **Ruin binding** (CT18, CT24): with a tail cap P(delay > x) ≤ ε, the feasible set depends on prices and the shares stop being exponent-only; one overall scale ratio comes back (PR #133 §3.1).
- **Rhythms** (CT21): a periodic world needs two-state modes; first-order stores in a geometric ladder do not fit it.
- **Drifting worlds** (CT21, L1): a single self-similar random walk needs at most one layer; no ladder (§1).
- **Non-power-law edges**: the map needs both laws to hold over the ladder's range. Hartstein et al. report power-law miss curves within a range; outside it, ratios bend.
- **CT34 scope**: the chain treats all levels in one currency with one technology law. Layers that pay in different currencies (a firm's levels paid in salary, a synapse's in protein turnover) need a measured γ per level or an exchange rate per boundary, and p grows (PR #133 §3.2). Layers with their own interests (CX2) break the single objective.
- **Integer and discrete effects**: capacities and team sizes are integers, and real ladders are short (§2.5 item 1).

## 5. Inventory of published values

"Independent" means measured without reference to the design being predicted.

| Field (substrate) | World exponent θ | Technology exponent γ | Design numbers (ratios, count) | n | Status |
|---|---|---|---|---|---|
| CPU caches and storage (silicon, magnetic) | **Measured, independent**: Hartstein et al. 2006 (doi 10.1145/1128022.1128064), θ ≈ 0.3–0.7; Cantin & Hill SPEC CPU2000 miss-rate tables (public, research.cs.wisc.edu). | **Obtainable, not compiled**: cost per byte and latency per tier (DRAM, flash, disk) in the five-minute-rule papers, Gray & Graefe 1997 (doi 10.1145/271074.271094) and Appuswamy et al. 2019 (doi 10.1145/3318163). SRAM vs. DRAM per-bit cost in public form not yet located. | **Measured**: per-chip capacities and latencies (7-cpu.com, vendor sheets). | Many chips, but a handful of independent technology generations; level count nearly collinear with time (PR #134). | **Closest to complete (1 field).** Engineers optimize with Chow-type models, so this field is an anchor, not independent support. |
| Web and CDN caching (silicon) | **Popularity only (not m(s) = s^{-θ})**: Breslau et al. 1999 (doi 10.1109/infcom.1999.749260) measure Zipf-like rank popularity α ∈ [0.64, 0.83] < 1, which gives hit ratio ∼ (s/N)^{1−α} and finite-catalog miss rate 1 − (s/N)^{1−α}, not scale-free s^{-θ} (which requires α > 1 with θ = α − 1). | Same technology as above. | Tier sizes mostly operator-private. | — | Same substrate as caches; does not add a field. |
| Synapses (biochemistry) | Need-probability curves measured for human memory's environment (Anderson & Schooler 1991, doi 10.1111/j.1467-9280.1991.tb00174.x), but these are behavioral, not synaptic; Benna & Fusi's 1/t, 1/√t are model choices. | **Missing.** No measured law for how the cost of holding a molecular state scales with its speed. | **Missing as data**: Benna & Fusi's ratio n² is chosen; no measured ratio of successive consolidation time constants located. | 0 | Missing γ and the design number. |
| Multi-echelon inventory (logistics) | Demand-popularity skew measured in retail generally; not tied to echelon data. | **Missing** (holding cost vs. replenishment speed is firm-specific, unpublished). | Roundy 1985 (doi 10.1287/mnsc.31.11.1416) power-of-two intervals are a policy rule, not a field measurement. | 0 | Missing all three as independent field data. |
| Firm strata (Jaques 1990) | **Missing.** | **Missing** (pay vs. time-span is in Jaques' data, but that's an output, not a technology law). | Time-span boundaries roughly geometric, reported by Jaques from his own practice. | Not public as data | Missing both exponents. |
| Social group sizes (Zhou et al. 2005; Hamilton et al. 2007, doi 10.1098/rspb.2007.0564) | **Missing.** | **Missing.** | **Measured**: ratio ≈ 3–4. | Dozens of societies | Missing both exponents; Lera & Sornette's model is a ready-made rival. |

**Count: 0 fields have all three measured and compiled today; 1 (caches/storage) can reach it with public data. The bar was 3. Nothing was locked.**

## 6. What is missing, and the cheapest data that would close it

1. **Caches, γ** (cheapest, hours): compile cost per byte and latency per tier from the two five-minute-rule papers plus one public SRAM vs. DRAM source, then fit γ. This completes one field (the anchor), not a test.
2. **A second, non-silicon substrate with a measured reuse curve, a measured speed–cost law and a measured ladder.** No public dataset was found. The likeliest kinds: (a) biological stores whose per-state maintenance cost and time constant are both measured (for example protein half-life vs. synthesis cost, with a measured ladder of consolidation stages); (b) library or archive systems (reading room, open stacks, closed stacks, off-site repository): circulation-vs-age curves are classically measured (a reuse world), storage cost per volume and retrieval delay per tier are often published in library reports, and the tier ratios are physical. Library tiers look like the cheapest second field, but they are institutional and may be weakly selected.
3. **A third.** Same search. Without three, the honest test shape is not "predict held-out fields" but "do two independently measured fields with similar (θ, γ) have similar ratios, while a field with a different θγ differs in the predicted direction". That shape is weaker and would need its own power check (PR #133 §3.3).

Counting rule (PR #133 §3.1): with both exponents measured in every field, p = 0 for the interior ratios, so every field is a scored observation, and a lock needs no fitting. If γ must be fitted in some field, that field moves to the fit set.

## 7. Usage

Shared weekly usage at writing: about 68% (resets Friday 27 Nov, 6:56 AM ET).
