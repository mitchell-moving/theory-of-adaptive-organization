# AXIOMS: the model class behind GTAO's structural results

Sunday 2026-11-15; final revision 02:22 ET, by a Grok Bot executor for Chad (via Ace). Private working file. Nothing was posted, sent or committed. The theory repo was only read.

> **Status banner (19 Nov 2026, ET; added with THEORY v2.0).** Frozen derivation, public in this repository since 18 Nov 2026; the "private working file" line above is from its drafting. The check scripts it cites as `checks/s*.py` are now in `reviews/night1/formal/checks/` (recovered and re-run byte-identically; see that folder's README). The canonical statement is `THEORY.md`; these axioms were written against THEORY v2.0.

**What this file is.** A minimal, explicit set of assumptions (the model class 𝓜). Every theorem in `THEOREMS.md` is a statement about 𝓜, with the axioms it uses named. Whether a real cell, colony, firm or AI system satisfies these axioms is an empirical question; `CLAIM_MAP.md` keeps that separate. Notation is fixed here once and used unchanged everywhere else.

**What is deliberately not assumed:** that organizations have goals beyond paying for what they track; that they minimize free energy; that thermodynamics binds above the cell; that real organizations are optimal. Optimality enters only through Axiom 7, with an explicit resolution ε.

---

## 0. Notation (fixed once)

| Symbol | Meaning |
|---|---|
| i = 1…N | members (cells, ants, people, teams, agents) |
| x_i(t) | the decision-relevant quantity member i must track (its *target*) |
| s_m(t), m = 1…M | shared *sources* (drivers): an upstream API, a price, a ligand, a food patch |
| u_i(t) | member i's private drift component |
| B_im | loading of member i on source m; x_i = Σ_m B_im s_m + u_i |
| q | drift rate: variance per unit time for Brownian drift; the scale in E(Δ_τ x)² = q τ^{2H} for fractional drift |
| q_g, q_u, ρ | rate of one shared source, rate of private drift, and the shared share ρ = q_g/q_u |
| H | Hurst exponent of the drift (H = ½ Brownian) |
| w_i, W | stakes of a member (loss per unit time per unit loss); pooled stakes of a tracker, W_m = Σ_i w_i B_im² |
| ℓ, L(v) | loss function of the tracking error; L(v) = E ℓ(Z), Z ~ N(0, v) |
| p | price of information in the tracker's technology (c per read in R1; λ per nat in R2; c′ in A_θ) |
| φ(W, q; p) | the minimized cost rate of one tracker (information spend + expected loss) |
| a, b | stakes and drift elasticities of φ: a = ∂ln φ/∂ln W, b = ∂ln φ/∂ln q |
| γ | the common value when a = b |
| θ | precision-cost exponent in averaging technologies (cost ∝ precision^θ) |
| h | upkeep per tracker per unit time (existence cost of a level, store, or layer) |
| κ_b | per-member link (broadcast/polling) cost of a level |
| c_b | per-read, per-member broadcast cost (T2b); t = c_b/c |
| ι | information rate of an R2 filter (nats per unit time) |
| κ_ℓ | E[L′(V_u)], the loss's variance-slope constant (T4) |
| u, μ, H_l | cost per lookup, use rate, and lifetime of an item |
| J | the organization's total cost rate |
| G(N) | gain from forming a level: J_flat − J_level |
| N\* | onset group size: the smallest N with G(N) > 0 |
| e_g, e_u | onset elasticities: e_g = ∂ln N\*/∂ln q_g, e_u = ∂ln N\*/∂ln q_u |
| Π\* | the onset invariant, the limit of N\*ρ^{(1−b)/(1−a)} as ρ → 0 with h = 0 |
| V | vigilance ratio: a level's information effort divided by a flat member's |
| κ, κ\* | sharing-decay exponent (q_s ∝ n_s^{−κ} across nested scopes) and its critical value (1−a)/(1−b) |
| ε | selection resolution |

---

## 1. The axioms

**Axiom 1 (World: drift).** Each target is a linear superposition x_i = Σ_m B_im s_m + u_i. The sources s_m and private parts u_i are mutually independent, zero-mean processes with stationary increments. The default drift class is Gaussian with E(Δ_τ)² = q τ^{2H}, with Brownian motion (H = ½) as the baseline. Two other classes appear only where a result says so: α-stable increments (scale (qτ)^{1/α}, used for counterexamples), and Poisson replacement at rate λ (used in the fallback result carried over from T5).

**Axiom 2 (Loss).** Member i pays w_i ℓ(e_i(t)) per unit time, where e_i = x_i − x̂_i is its tracking error. The default is quadratic, ℓ(e) = e². When a member's estimate is assembled from a level's estimate of a source and its own estimate of its residual, the member's true loss is **bundled**: ℓ(e_g + e_u). A **separable** loss ℓ(e_g) + ℓ(e_u) is a modeling shortcut. It is exact for quadratic loss with independent zero-mean errors, and also exact when the shared and private components drive *different* decisions. Otherwise it is an approximation whose consequences are examined in Theorem 4.

**Axiom 3 (Sensing technologies).** A tracker buys information about one readable object at a price. Three technologies are used:
- **R1 (reset by complete reads).** A read costs c and returns the object's current value exactly. Between reads the tracker holds the last value (zero-order hold) and reads periodically. For Brownian drift and quadratic loss, periodic reading is optimal among all schedules (Lemma 1(vii)). For H ≠ ½ the hold-and-read estimator is a restriction, because a better predictor exists; R1 is defined with that estimator.
- **R2 (entropy-priced filtering).** A Kalman–Bucy filter whose information rate ι (nats per unit time) is bought at λ per nat. By Duncan's theorem (Duncan 1970, SIAM J Appl Math 19:215–220, doi 10.1137/0119020 [DOI and abstract verified; the formula "information rate = error variance / (2 × observation-noise intensity)" is from memory of the theorem, consistent with the abstract]) the error variance is q/(2ι) for Brownian drift.
- **A_θ (precision-priced averaging).** A Kalman–Bucy filter on observations with noise intensity r, where precision is bought at cost c′r^{−θ}, θ > 0. θ = 1 is "cost proportional to samples or receptors".

A technology is in the **power class P(a, b)** if its minimized cost has the form φ(W, q; p) = k p^{1−a} W^a q^b with 0 ≤ a < 1 and 0 < b < 1. Lemma 1 shows R1, R2 and A_θ are in P with known (a, b).

**Axiom 4 (Readability).** A level for source m reads s_m directly, at a price that does not grow with N. Each member reads its own residual component directly (*component readability*). Proposition 11 relaxes this: when members can read only x_i and subtract the level's estimate, the exponents survive but the constants change.

**Axiom 5 (One budget, additive costs).** The organization's cost rate is
  J = Σ_trackers [information spend + pooled expected loss] + h·(number of trackers) + κ_b·(number of member–level links) + Σ_items (users × μ u if looked up).
All terms are in one currency (heat, attention, money, compute). This is the only sense in which GTAO is "one budget": a single exchange rate between information and loss within one organization. No cross-substrate exchange rate is assumed.

**Axiom 6 (Architectures).** An architecture specifies: (i) the set S of sources with a level (a shared tracker with pooled stakes W_m); (ii) each member's residual tracker for r_i = x_i − Σ_{m∈S} B_im ŝ_m, whose drift rate is R_i(S) = q_ui + Σ_{m∉S} B_im² q_m; (iii) per item, a mode: freeze (read once per lifetime), hold (track), or look up (read the source at each use); (iv) clocks (separately timed components) inside a tracker. Errors of different trackers are independent and zero mean, and different trackers' read schedules have independent uniformly random relative phases. Under Axioms 1, 2 (quadratic) and 4, the costs of an architecture therefore add exactly.

**Axiom 7 (Selection with finite resolution).** The realized architecture A satisfies J(A) ≤ min J + ε. Here ε ≥ 0 is the resolution of selection, learning or design. It is relative (a fraction of cost) or absolute (cost units). All theorems are stated at ε = 0 unless marked; Proposition 10 gives the ε > 0 consequences. This axiom is the formal content of "selection keeps the cheapest designs, to the resolution selection allows".

**Axiom 8 (Long run).** Costs are long-run time averages under stationarity. The one exception is freezing, which uses an item lifetime H_l.

---

## 2. Which result uses which axiom

| Result (THEOREMS.md) | Ax1 drift | Ax2 loss | Ax3 class | Ax4 read | Ax5 budget | Ax6 arch | Ax7 sel. | Ax8 |
|---|---|---|---|---|---|---|---|---|
| L1 sensing classes | Brownian/fBm/stable | any \|e\|^p | R1, R2, A_θ | — | ✓ | — | — | ✓ |
| T1 pooling onset | ✓ | quadratic or separable | P(a,b) | ✓ | ✓ | flat vs one level | ε = 0 | ✓ |
| T2 broadcast break | ✓ | as T1 | P(a,b); R1 for per-read | ✓ | +κ_b | ✓ | ε = 0 | ✓ |
| T3 opposite effects | ✓ | as T1 | P(a,b), b < 1 | ✓ | ✓ | ✓ | ε = 0 | ✓ |
| T4 bundling | Gaussian | **bundled, general ℓ** | any linear-Gaussian tracker | ✓ | ✓ | ✓ | ε = 0 | ✓ |
| T5 vigilance | ✓ | as T1 | P(a,b) | ✓ | ✓ | ✓ | ε = 0 | ✓ |
| T6 lattice/accretion | additive drift rates | quadratic | concave member cost | ✓ | ✓ | many sources | ε = 0 | ✓ |
| T7 hierarchy scales | nested shared drifts | quadratic | P(a,b) levels, concave members | ✓ | ✓ | nested tree | ε = 0 | ✓ |
| T8 freeze/hold/lookup | ✓ | quadratic (power class in (iii)) | R1 (P(a,b) in (iii)) | — | +lookup | item modes | ε = 0 | H_l |
| P9 clocks | independent components | quadratic | P(γ,γ) | per-component reads | ✓ | clocks | ε = 0 | ✓ |
| P10 resolution | ✓ | as T1 | P(a,b) | ✓ | ✓ | ✓ | **ε > 0** | ✓ |
| P11 readability | Brownian | quadratic | R1 | **relaxed** | ✓ | ✓ | ε = 0 | ✓ |

## 3. What the axioms rule in and out (scope, stated before any test)

- **In scope:** design variables under selection whose cost differences exceed the resolution ε: which drivers get a shared tracker, how often each tracker samples, whether an item is frozen, held or looked up, and how many nested scales carry a level.
- **Out of scope:** failure rates given a design (these are first-passage physics, not GTAO; CORE_AUDIT §1.3); goals; anything in weakly selected systems where ε exceeds the relevant prize (Proposition 10 makes "weakly" quantitative).
- **The axioms are falsifiable as a description of a substrate.** For example, a substrate where members can read only aggregates of other members violates Axiom 4; one where the level must message each member violates the κ_b = 0 case of Axiom 5. Such substrates are not tests of the results that need those axioms. They *are* tests of Theorem 2, which predicts what happens instead.
