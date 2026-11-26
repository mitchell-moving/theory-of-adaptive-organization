# THEOREMS: GTAO's structural results, stated and proved in the model class of AXIOMS.md

Sunday 2026-11-15; final revision 02:22 ET. Grok Bot executor for Chad (via Ace). Private. Nothing was posted, sent or committed; the theory repo was only read.

> **Status banner (19 Nov 2026, ET; added with THEORY v2.0).** Frozen derivation, public in this repository since 18 Nov 2026; "Private" above is from its drafting. The `s*.out` checks cited below are now in `reviews/night1/formal/checks/` (recovered from the off-repo working copy and re-run on 19 Nov 2026: all twelve reproduce byte for byte). Errata in force: Lemma 1(viii) and Theorem 5 (15 Nov, inline); **Theorem 5 item 6 (19 Nov, inline below; CLAIM_MAP E5)**. The canonical statement is `THEORY.md`; these theorems were written against THEORY v2.0.

**How to read this file.** Each result names the axioms it uses (AXIOMS.md §2), states its hypotheses exactly, gives a complete proof, and gives counterexamples showing that each hypothesis is needed. Every algebra step was checked, either symbolically in sympy or, where sympy would not simplify, by high-precision (50-digit) identity checks at random points. Every inequality was checked numerically over random parameters. The base cost formula was also checked by first-principles Monte Carlo (s12). The scripts are in `checks/` (run them with `/tmp/rv/bin/python checks/sN_*.py`; the outputs are in `checks/sN_*.out`). The adversarial pass and its fixes are logged in `FIXES.md`. The proofs below already include those fixes.

**Status labels.** **KNOWN**: published, with a verified source. **ASSEMBLY**: known parts, combined here. **NEW**: not found in the literature the project has read. That is not an exhaustive search, so "new" means "new as far as we know". **NUMERICAL**: shown by computation, not proved.

**One-line summary.** In 𝓜, a tracker's *sensing technology* fixes two exponents (a, b). The **level's** (a, b) fixes the exponent of when a shared level forms (e_g) and whether hierarchies fill top-down or bottom-up (κ\*). The members' b fixes the private-drift exponent (e_u). With one common technology, (a, b) also fix how vigilant a level is at birth. Under a bundled loss this holds whatever the loss function is. Levels are complements, and they accrete when upkeep falls. They can **dissolve** when lookup gets cheap.

---

## Lemma 1 (sensing classes and the power class) — uses Ax1, Ax3, Ax5, Ax8. `s1_classes.out`

**Statement.** For one tracker with pooled stakes W, drift rate q and information price p:

| Technology | Minimized cost φ | a | b | Info-spend share of φ |
|---|---|---|---|---|
| (i) R1, fBm Hurst H, quadratic loss | ∝ c^{2H/(1+2H)} (Wq)^{1/(1+2H)} | 1/(1+2H) | 1/(1+2H) | 2H/(1+2H) |
| (ii) R2, Brownian, quadratic | √(2λWq) | ½ | ½ | ½ |
| (iii) A_θ, Brownian, quadratic | ∝ c′^{1/(1+2θ)} W^{2θ/(1+2θ)} q^{θ/(1+2θ)} | 2θ/(1+2θ) | θ/(1+2θ) = a/2 | 1/(1+2θ) |
| (iv) R1, Brownian, \|e\|^p loss, *separable* | ∝ (W q^{p/2})^{2/(p+2)} | 2/(p+2) | p/(p+2) | p/(p+2) |
| (v) R1, α-stable, \|e\|^p (p < α) | ∝ (W q^{p/α})^{α/(α+p)} | α/(α+p) | p/(α+p) | p/(α+p) |

Further:
- (vi) **Homogeneity.** φ(λp, λW, q) = λφ(p, W, q) for every technology, so φ = p^{1−a}W^a f(q) whenever φ is a power in W.
- (vii) **Periodic reading is optimal in R1 (Brownian, quadratic).** Over any horizon with n reads at gaps T_k, the cost is nc + (Wq/2)ΣT_k². By Jensen, at fixed n and ΣT_k this is minimized by equal gaps.
- (viii) **Effort elasticities equal (a, b).** Information effort (read rate, information rate, precision) equals spend/price = s·φ/p, with s the class's constant spend share. A lone member's measured elasticities of effort with respect to stakes and drift are therefore (a, b).
  **Erratum (15 Nov 2026, about 5:25 PM ET; QUEUE EFFORT-UNITS-ERRATUM, pick 25; from `reviews/night2/N12_REFEREE.md` C3, re-derived in `reviews/night2/EFFORT_UNITS_ERRATUM_checks/units_check.py`).** "Effort = spend/price" is the read rate in R1 and the information rate in R2 (spend linear in effort), but in A_θ it is r^{−θ} = precision^θ, which is precision only at θ = 1. For A_θ the precision elasticities are (a/θ, b/θ) = (2/(1+2θ), 1/(1+2θ)); (a, b) are the elasticities of spend/price. The ratio b/a, every sign, and the a = b test are unchanged. Rows (i), (ii), (iv), (v) and A₁ (θ = 1) are unaffected. The text above is left as written; this note governs.
- (ix) **When a = b.** If the expected loss can be written W·q·f(z) and the spend as g(z), for a control z whose price does not depend on q ("drift-invariant pricing"), then φ depends on (W, q) only through Wq, so a = b. R1 (z = interval: loss WqT/2, spend c/T) and R2 (z = ι: loss Wq/(2ι), spend λι) satisfy this. This is a sufficient condition; we do not claim the converse. A_θ does not: its error is √(qr), so per-precision prices make the spend depend on q at fixed relative accuracy, and b = a/2.

**Proof.** (i)–(v): minimize spend + loss over the scalar control. The first-order conditions and the closed forms are in s1 (FOC residual ≤ 10⁻¹⁷¹ at random rational points; a and b equal the claimed forms to the same precision). Convexity: d²J/dT² > 0 at T\*. For (iii), the Kalman–Bucy steady state 0 = q − P²/r gives P = √(qr) (checked by integrating the Riccati ODE: 0.774597 vs 0.774597). Minimizing W√(qr) + c′r^{−θ} gives the row. For (ii), Duncan's theorem gives an information rate P/(2r) = √(q/r)/2 = ι, so P = q/(2ι) (sympy). (vi): scaling p and W by λ leaves the argmin unchanged and scales the objective by λ. (viii): in each row, spend at the optimum is a constant fraction s of φ (sympy), so effort = sφ/p. (ix): min_z[Wq f(z) + g(z)] is a function of Wq. ∎

**Status.** (i)–(ii) KNOWN (EOQ, Harris 1913; Kalman–Bucy; Duncan 1970; Sims 2003 for entropy pricing). (iii)–(v) are standard calculus. The organizing facts, that (a, b) classify technologies, that drift-invariant pricing implies a = b (sufficient; the converse is not claimed), and that averaging technologies have b = a/2, are ASSEMBLY, with the classification as stated NEW.

**Counterexamples / scope.**
- R1 for H ≠ ½ uses the hold-last-value estimator. For fBm, a predictor using the path does better, so R1(H ≠ ½) is a restricted technology.
- Outside P(a, b): a read-rate cap with |e|^p loss and p > 2 makes φ convex in q at high drift. That is used as the counterexample in T6. Bounded fallbacks give min(φ, μu), which is concave but not a power.

---

## Definitions used from here on

- **Single-source architecture class 𝒜₁.** N homogeneous members, x_i = g + u_i, ρ = q_g/q_u, a common technology in P(a, b), member price p, level price p_g.
  - Flat: J_F = N φ(w, q_g + q_u; p).
  - Level: J_L = φ(Nw, q_g; p_g) + N φ(w, q_u; p) + h + Nκ_b.
- **Gain** G(N) = J_F − J_L; onset N\* = inf{N ≥ 1 : G(N) > 0}.
- **Units.** Write h′ = h/(k p^{1−a} w^a q_u^b) and κ′ = κ_b/(k p^{1−a} w^a q_u^b). With equal prices, G/(k p^{1−a} w^a q_u^b) = N[(1+ρ)^b − 1 − κ′] − N^a ρ^b − h′.

Within 𝒜₁ every statement below is an exact "iff". (T3a in the repo was "sufficient" only because it compared against a better, unspecified joint filter. Here the architecture class is fixed.)

---

## Theorem 1 (pooling onset) — Ax1–Ax8 with quadratic or separable loss, κ_b = 0. `s2_onset.out` §1, §3–§6

**Hypotheses.** P(a, b) with 0 ≤ a < 1 and 0 < b < 1; h ≥ 0; κ_b = 0.

**Statement.**
1. **Single crossing.** G is strictly convex in N, with G(N) < 0 for small N when h > 0 or a > 0. So N\* is unique and the level is optimal **iff N > N\***.
2. **Exact onset (h = 0, equal prices):** **N\* = [ρ^b / ((1+ρ)^b − 1)]^{1/(1−a)}.** At a = b = ½ this is T3a's (√(1+ρ)+1)²/ρ, identically.
3. **Small-share law (h = 0):** **N\*·ρ^{(1−b)/(1−a)} → Π\* = b^{−1/(1−a)}** as ρ → 0. So e_g → −(1−b)/(1−a) and e_u → +(1−b)/(1−a). At a = b = γ: Π\* = γ^{−1/(1−γ)} (4 at γ = ½).
4. **Exact elasticity (h = 0):** e_g(ρ) = [b/(1−a)]·[1 − ρ(1+ρ)^{b−1}/((1+ρ)^b − 1)], which is negative for all ρ > 0. It tends to −(1−b)/(1−a) as ρ → 0 and to 0 as ρ → ∞, and N\* → 1 as ρ → ∞.
5. **Upkeep (h > 0), ρ → 0:** e_g → −(1−b)/(1−a) if a > b, and e_g → −1 if a ≤ b. In the intermediate regime 1 ≪ ρ ≪ h′^{1/γ} at a = b = γ, e_g ≈ −γ (the "duplicated-effort" value).
6. **Prices:** at h = 0 and first order in ρ, N\* ∝ p_g/p.
7. **Scale effects:** multiplying both drift rates by λ multiplies G + h by λ^b. Multiplying stakes by s multiplies it by s^a. So at h = 0 the onset is invariant to total volatility and to stakes. With h > 0, N\* strictly decreases in both: **more total volatility makes levels form at smaller N.**
8. **Mixed technologies (added by the adversarial pass, FIXES F12).** Suppose the level uses P(a_L, b_L) and the members use P(a_m, b_m). Then at h = 0, as ρ → 0, **e_g → −(1−b_L)/(1−a_L)**, set by the *level's* technology, and **e_u → +(1−b_m)/(1−a_L)**. N\* then depends on q_g and q_u separately, not only through ρ. The opposite signs of T3 survive whenever b_m < 1 and b_L < 1. Items 2–3 are the special case of a common technology.
9. **N\* > 1 at equal prices (more generally whenever p_g ≥ p):** G(1) = (1+ρ)^b − 1 − (p_g/p)^{1−a}ρ^b − h′ < 0 for b < 1, by subadditivity. A one-member "level" never pays. If p_g < p, G(1) can be positive: that is just a cheaper technology for g, not pooling (found in the adversarial pass, F17).

**Proof.**
1. In normalized units G(N) = NA − N^aB − h′ with A = (1+ρ)^b − 1 > 0 and B = ρ^b > 0. Then G″ = a(1−a)N^{a−2}B > 0 for a > 0 (G is linear if a = 0), and G(0) = −h′ ≤ 0. Since A > 0, G → +∞. A convex function that starts at or below 0 and diverges to +∞ crosses 0 exactly once from below on (0, ∞). When h = 0 and a > 0, G < 0 near 0 because N^a dominates N.
2. Set G = 0 with h′ = 0: N^{1−a} = B/A. Sympy confirms the a = b = ½ identity with T3a.
3. (1+ρ)^b − 1 = bρ + O(ρ²), so B/A·ρ^{1−b} → 1/b (sympy limits for b = ½, ⅓, ⅔, ⅕). Raise to 1/(1−a). The e_u statement follows from 2, because N\* depends on (q_g, q_u) only through ρ at h = 0.
4. Differentiate ln N\* = [b ln ρ − ln((1+ρ)^b − 1)]/(1−a). Sympy gives the formula and both limits.
5. Let N₀ be the h = 0 root, N₀ ~ ρ^{−(1−b)/(1−a)}. At N₀ the level's own cost is N₀^aρ^b ~ ρ^{(b−a)/(1−a)}. If a > b this diverges as ρ → 0, so the constant h′ is negligible at the root and the h = 0 exponent survives. If a < b it vanishes, so the root is set by the savings Nbρ against h′: N\* ≈ h′/(bρ) and e_g → −1. If a = b both terms scale alike, and γΠ − Π^γ = h′ has a root Π\*(h′) independent of ρ, so e_g = −1. Intermediate large-ρ regime: for a = b = γ and ρ ≫ 1, G ≈ ρ^γ(N − N^γ) − N − h′. When h′ρ^{−γ} ≫ 1 the root is N\* ≈ h′ρ^{−γ}, so e_g ≈ −γ. Numerically: −0.650, −0.549, −0.514, −0.503 at ρ = 10, 10², 10³, 10⁴ with h′ = 10⁶ (s2 §5).
6. Level cost ∝ p_g^{1−a} and member costs ∝ p^{1−a}, so the first-order condition reads (N\*)^{1−a} ∝ (p_g/p)^{1−a}.
7. φ is homogeneous of degree b in q and a in W.
8. The saving is N·∂_qφ_m(w, q_u)·q_g ∝ N q_u^{b_m−1}q_g (envelope), and the level cost is ∝ N^{a_L}q_g^{b_L}. Equating gives N^{1−a_L} ∝ q_g^{b_L−1}q_u^{1−b_m}. Checked at four mixed pairs in `s9_attack.out` (1): exact to 4 decimals, e.g. a level in (⅔, ⅓) over members in (½, ½) gives e_g = −2.0000 and e_u = +1.5000.
9. Subadditivity of x ↦ x^b. ∎

**Numerical checks (s2).** The exact roots give e_g at ρ = 10⁻⁵ of −1.0000, −2.0000, −1.5000, −4.0000 for (a, b) = (½, ½), (⅔, ⅓), (½, ¼), (0.8, 0.2), at h′ = 0, 1 and 100. For a < b, e_g moves from −0.5000 at h′ = 0 to −0.996 and −0.9998 at h′ = 1 and 100, exactly as in item 5. The invariants come out as 4.00000, 27.00003, 16.00001, 6.34961 and 4.60504 against b^{−1/(1−a)}. Total-volatility and stakes elasticities are +0.0000 at h = 0 and −0.349 at h′ = 5 (a = b = ½).

**Counterexamples (each hypothesis is needed).**
- a = 1 (cost linear in stakes): G = N[φ(q_g+q_u) − φ(q_u) − φ(q_g)] − h ≤ −h, by subadditivity of a concave φ with φ(0) = 0. **No level at any N** (s2 §2: N\* = ∞). Concavity *in stakes* is necessary for pooling. This is POOLING_REVIEW's corrected Corollary 2.
- b = 1 (cost linear in drift, e.g. hard tolerance): e_u = 0 (s2 §2). The private-drift effect vanishes.
- κ_b > 0: see Theorem 2. The ρ^{−…} law is replaced by a ρ threshold.
- ρ not small: e_g → 0 (h = 0) or ≈ −γ (h′ large). The −1 is a small-share law only.

**Status.** The ρ^{−1} onset for a = b with large upkeep is KNOWN in substance: Veldkamp & Wolfers 2007, Prop. 2 (static, entropy cost; verified by POOLING_REVIEW), and Wilson 1975. The exact closed form in P(a, b), the general exponent −(1−b)/(1−a) with its upkeep dichotomy (item 5), and the scale effects (item 7) are NEW as far as we know. They are elementary.

---

## Theorem 2 (the broadcast break) — Ax1–Ax8 with κ_b > 0. `s2_onset.out` §8, `s8_broadcast.out`

**Statement.**
- (a) **Per-member link cost per unit time.** In P(a, b), a level is optimal for **some** N iff (1+ρ)^b − 1 > κ′, i.e. **ρ > ρ_b = (1+κ′)^{1/b} − 1** (≈ κ′/b for small κ′). As ρ ↓ ρ_b, N\* → ∞. For ρ ≤ ρ_b there is no level at any N.
- (b) **Per-read broadcast in R1 (γ = ½).** The level's read cost is c + Nc_b, i.e. each read must be pushed to every member. With t = c_b/c, a level is optimal for some N iff **ρ > 4t/(1−t)²** when t < 1, and never when t ≥ 1.

**Proof.**
- (a) G = N[A − κ′] − N^aρ^b − h′. If A ≤ κ′, then G < 0 for every N. If A > κ′, the single-crossing argument of T1.1 applies.
- (b) G(N)/N = √(2cw(q_g+q_u)) − √(2(c/N+c_b)wq_g) − √(2cwq_u) − h/N. This is increasing in N and tends to √(2cw(q_g+q_u)) − √(2c_bwq_g) − √(2cwq_u). The limit is positive iff √(tρ) + 1 < √(1+ρ). Sympy solves the boundary: ρ = 4t/(1−t)². ∎

**Checks.** At κ′ = 10⁻³: N\* = ∞ at ρ = 0.001 and 0.002, and finite (2.2 × 10³) at ρ = 0.005, against ρ_b = 0.002001. In the per-read case, N\* = ∞ at 0.9ρ_b and 0.99ρ_b, and N\* = 10⁶, 10⁵, 10⁴ at 1.01ρ_b, 1.1ρ_b, 2ρ_b.

**Reading.** When the level must talk to each member, the onset is a threshold in ρ, not in N·ρ. This is the same structure as a percentage resolution floor (Proposition 10). Garicano's (2000) communication cost is this term (POOLING_REVIEW).

**Status.** The statement is elementary and NEW in this form as far as we know. The mechanism, that communication costs limit hierarchy, is KNOWN in kind (Garicano 2000 [PR]).

---

## Theorem 3 (shared and private drift have opposite effects) — Ax1–Ax8, κ_b = 0. `s2_onset.out` §2

**Hypotheses.** P(a, b) with 0 ≤ a < 1 and 0 < b < 1; any ρ > 0; any h ≥ 0; any prices.

**Statement.** **∂N\*/∂q_g < 0 < ∂N\*/∂q_u** at every ρ, not only for small ρ. Shared volatility makes a level form at a smaller group size, and private volatility makes it form at a larger one.

**Proof.** By T1.1, G_N(N\*) > 0. By the implicit function theorem, sign ∂N\*/∂q = −sign G_q.
- G_{q_u} = N[φ_q(w, q_g+q_u) − φ_q(w, q_u)] < 0, because φ_q is strictly decreasing (b < 1). So ∂N\*/∂q_u > 0.
- G_{q_g} = k b p^{1−a} w^a N^a [N^{1−a}(q_g+q_u)^{b−1} − (p_g/p)^{1−a} q_g^{b−1}]. Take equal prices first. At the h = 0 root, N₀^{1−a} = ρ^b/((1+ρ)^b − 1). The bracket is positive iff N^{1−a} > ((1+ρ)/ρ)^{1−b}. At N₀ that inequality reads ρ > (1+ρ) − (1+ρ)^{1−b}, i.e. (1+ρ)^{1−b} > 1, which is true. The bracket is increasing in N, and N\*(h) ≥ N₀, so G_{q_g} > 0 at N\*(h) for every h ≥ 0.
- Unequal prices: write the h = 0 root with prices, N₀^{1−a} = (p_g/p)^{1−a}ρ^b/((1+ρ)^b − 1). Then the same inequality holds with both sides multiplied by (p_g/p)^{1−a}. ∎

**Checks.** 17,065 random draws (a ∈ [0, 0.95], b ∈ [0.05, 0.95], ρ ∈ [10⁻⁴, 10⁴], h ∈ {0} ∪ [10⁻³, 10³], random stakes and prices) gave 0 sign violations for either elasticity.

**Counterexamples.**
- b = 1: e_u = 0 (no private effect).
- **Convex member cost** (b > 1 locally, e.g. a read-rate cap with quartic loss; T6 counterexample): G_{q_u} > 0, so private drift then *promotes* levels. The sign needs concavity in drift.
- a = 1: no level exists at all (T1).

**Corollary 3.1 (against contingency theory).** At fixed ρ, total volatility is neutral at h = 0 and promotes levels when h > 0 (T1.7). Contingency theory says volatile environments call for more decentralized, organic structure (Burns & Stalker 1961; Lawrence & Lorsch 1967 [M, not re-read]). The formal versions say more uncertainty means smaller spans (Geanakoplos & Milgrom 1991 [R in CORE_AUDIT]). Those predict one sign for volatility. GTAO predicts **opposite signs for shared and private volatility**, and agrees with GM on the private side.

**Status.** The qualitative "centralize common information, decentralize local information" is probably old (Hayek lineage; Alonso, Dessein & Matouschek 2008 [M]). The signed statement at every ρ, with exponents, is NEW as far as we know.

---

## Theorem 4 (bundling: the sensing technology, not the loss, sets the exponent) — Ax1 Gaussian, Ax2 bundled, Ax3–Ax8. `s3_bundling.out`

**Hypotheses.**
- (H1) Drift is Gaussian and trackers are linear (R1 hold-and-read, or Kalman–Bucy), so each tracking error is Gaussian with a known, time-varying variance: V_g(t) for the level and V_u(t) for the residual tracker.
- (H2) The loss is bundled: member i pays w ℓ(e_g + e_u). Errors are independent, with random phases (Ax6).
- (H3) L(v) = E ℓ(N(0, v)) is differentiable on (0, ∞), and κ_ℓ := E_t[L′(V_u(t))] < ∞, where the average is over the private tracker's cycle. For ℓ = |e|^p with R1 this holds iff p > 0, because E[s^{p/2−1}] < ∞.
- (H4) Small shared share (ρ → 0); h = 0 for the exponent statement.

**Statement.** To first order in q_g, the nested cost per member is
  J_L/N = φ_ℓ(w, q_u) + (1/N)·φ₂(N w κ_ℓ, q_g) + o(q_g),
where φ₂ is the level technology's **quadratic-loss** cost. Hence
  **e_g = −(1 − b₂)/(1 − a₂)**,
with (a₂, b₂) the technology's quadratic-loss exponents: **−1 for R1 and R2 under every loss satisfying H3, and −(1+θ) for A_θ.** The loss shape changes only constants (Π\*, and κ_ℓ inside it).

**Proof.**
1. **Gaussian closure.** e_g + e_u is Gaussian with variance V_g + V_u, so E ℓ(e_g + e_u) = E L(V_u + V_g).
2. **Expansion.** L(V_u + V_g) = L(V_u) + L′(V_u)V_g + R. With independent phases, E[L′(V_u)V_g] = κ_ℓ·E V_g. So the shared error costs each member w κ_ℓ E V_g. That is a *variance-linear*, i.e. quadratic-equivalent, loss, and across N members the level faces quadratic loss with stakes Nwκ_ℓ. Its optimal cost is φ₂(Nwκ_ℓ, q_g), with exponents (a₂, b₂) from Lemma 1. Since E V_g ∝ q_g·(interval) at the level's optimum, the term is O(q_g).
3. **Remainder.** For ℓ = |e|^p, L(v) ∝ v^{p/2}.
   - p = 2: L is linear, so R ≡ 0.
   - p > 2: averaging L″(V_u)V_g² over the private cycle is finite, or log-divergent at p = 4 only through the lower limit. So R = O(V_g²), and the relative correction is O(ρ) up to logs.
   - 0 < p < 2: L″ ∝ v^{p/2−2} is not integrable at 0. Split the private cycle at V_u = V_g. On V_u ≥ V_g, ∫ (q_u s)^{p/2−2} V_g² ds = O(V_g^{1+p/2}/q_u). On V_u < V_g, which has probability O(V_g/(q_uT_u)), |R| = O(V_g^{p/2}), giving O(V_g^{1+p/2}) again. Relative to the linear term O(V_g), the correction is O(V_g^{p/2}), i.e. **O(ρ^{p/2})**: o(1), but slow for small p.
   - The numerics confirm the rate: the local slopes for p = ½ are −1.0176, −1.0096 and −1.0052 per decade toward ρ = 10⁻⁶. Their deviations shrink by ≈ 0.55 per decade, against 10^{−p/2} = 0.56.
4. **Saving side.** The flat member pays φ_ℓ(w, q_g + q_u). By the envelope theorem, φ_ℓ(w, q_g + q_u) − φ_ℓ(w, q_u) = ∂_qφ_ℓ(w, q_u)·q_g + o(q_g). The private tracker's re-optimization in the nested design is second order.
5. **Onset.** N·∂_qφ_ℓ·q_g = k₂(Nwκ_ℓ)^{a₂}q_g^{b₂}p_g^{1−a₂} + h. At h = 0, N^{1−a₂} ∝ q_g^{b₂−1}, so N\* ∝ q_g^{−(1−b₂)/(1−a₂)} at fixed q_u. ∎

**Checks (s3, exact, with joint optimization of both intervals and no expansion).**

| Loss and technology | Exact slope e_g | Lone-member (a, b) would predict | Theorem 4 predicts |
|---|---|---|---|
| R1, \|e\|^{0.5}, bundled | −1.032 at ρ ∈ [10⁻³, 10⁻²], converging −1.018 → −1.010 → −1.005 as ρ → 10⁻⁶ | −4 | −1 |
| R1, \|e\|¹, bundled | −1.007 | −2 | −1 |
| R1, e², bundled | −0.998 | −1 | −1 |
| R1, \|e\|⁴, bundled | −0.997 | −½ | −1 |
| R1, \|e\|¹, *separable* | −1.996 | −2 | (separable: −2) |
| R1, \|e\|⁴, *separable* | −0.499 | −½ | (separable: −½) |
| A₁, \|e\|¹, bundled | −1.989 | −4 | −2 |

The closed form E[(q_g s_g + q_u s_u)^β] = [(q_gT_g + q_uT_u)^{β+2} − (q_gT_g)^{β+2} − (q_uT_u)^{β+2}]/((β+1)(β+2)q_gq_uT_gT_u) was checked in sympy. At β = ½ it is W5_CHECK's 4/15 formula. The independent W5 check (another executor) found −1.008 in continuous time and −0.978 discretely.

**Corollary 4.1 (DP1 corrected).** "Measure (a, b) on lone members, then predict e_g" is valid **iff** the members' measured elasticities equal their technology's quadratic-loss exponents. That holds under quadratic loss, but not, for example, under absolute loss: there a lone R1 member shows (⅔, ⅓) and predicts −2, while the truth is −1. The right measurement is the **sensing technology's** exponents: how effort scales when the loss is locally quadratic, or the price structure itself (per read or per nat → (γ, γ); per unit of precision → b = a/2).

**Corollary 4.2 (when the separable model is right).** Separable loss, and with it the review's −2 (absolute), −½ (quartic) and −α/p (stable), is the right model **only** when the shared and private components drive *different decisions*. An example is a member who sets one action from g alone (for instance, a price) and another from u alone (for instance, a local schedule). It is wrong for a member acting on one target that sums them.

**Counterexamples.**
- (H3) fails at p → 0 in the limit where L′(V_u) has no finite mean. Indicator losses with τ > 0 are still fine: L is smooth for v > 0 and flat at 0.
- (H1) fails for α-stable drift: there is no Gaussian closure, and the bundled exponent there is **not derived (open)**.
- If the shared and private errors are correlated (the level's estimate feeds the members' reads), H2's independence fails. That is Proposition 11's setting, where the exponent survives but the constant moves.

**Status.** NEW as far as we know. It was found numerically tonight (POOLSIM W5, then W5_CHECK) and proved here. It overturns POOLING_REVIEW's "−1 fails for absolute loss" for the bundled case, and it corrects ARCH_EQUATION's DP1.

---

## Theorem 5 (vigilance at birth) — Ax1–Ax8, separable costs. `s2_onset.out` §7, `s8_broadcast.out`

**Definition.** V(N) = [level effort]/[flat member effort], with effort = spend/price (Lemma 1(viii)). Same technology, so V(N) = (p/p_g)^a N^a (ρ/(1+ρ))^b.

**Erratum (15 Nov 2026, pick 25; see Lemma 1(viii) erratum).** V here is in spend/price units. For A_θ with the same θ at the level and the members, the precision ratio is V^{1/θ}: item 3 becomes V ∝ ρ^{−1} in precision units (ρ^{−θ} in spend/price units), and item 5 becomes N^{a/θ}. Items 2 and 4 (V > 1, price invariance) hold in both units, since V^{1/θ} > 1 iff V > 1. Reset and entropy-priced classes (a = b) are unaffected. A vigilance test must name its unit.

**Statement.**
1. **Equal prices, any ρ:** V(N\*) = N\*^a (ρ/(1+ρ))^b. If a = b = γ, then V(N\*) = (N\*ρ/(1+ρ))^γ.
2. **Born more vigilant iff a ≥ b.** If a ≥ b, then V(N\*) > 1 for every ρ > 0, h ≥ 0 and price ratio (strengthened in the adversarial pass, F16). If a < b and h = 0, then V(N\*) → 0 as ρ → 0.
3. **Small-share value (h = 0, first order):** V(N\*) = b^{−a/(1−a)} ρ^{(b−a)/(1−a)}. This is constant across ρ **iff a = b**, where it equals γ^{−γ/(1−γ)} (**2 at γ = ½**, 1.50 at γ = 0.2, 2.44 at γ = 0.8). For A_θ, V ∝ ρ^{−θ}.
4. **Price invariance (h = 0, first order):** V(N\*) does not depend on p_g/p, and therefore does not depend on any per-read broadcast cost.
5. **Beyond onset:** V(N) grows as N^a. At N = 10N\*, γ = ½, V ≈ 6.3.
6. **With upkeep (a = b = γ):** V(N\*) = (Π\*(h′)·p/p_g)^γ, which rises with h′ and now depends on prices. At γ = ½ and small ρ it has the closed form **V(N\*) = 1 + √(1 + 2h′/r)**, with r = p_g/p and h′ in member-cost units: 2.73 at h′ = 1 and equal prices; 4.00, 2.73 and 2.22 at r = ¼, 1 and 4. So **V(N\*) ≥ 2 for every upkeep and price** in class R at small ρ. (Proof: with x = √(Nρ), the onset condition is x²/2 − √r·x − h′ = 0, so x = √r + √(r + 2h′) and V = x/√r. Added in the adversarial pass, FIXES F15.) **Erratum (19 Nov 2026, ET; CLAIM_MAP E5 MATH-CORRECTED, E6–E7).** "V(N\*) ≥ 2" is false as stated: it is the ρ → 0 limit of a first-order expansion, not a bound. The exact onset value in class R is V(N\*) = ½(1 + (1+ρ)^{−1/2})(1 + √(1 + 4h′(√(1+ρ)−1)/(rρ))), whose floor (h′ = 0) is **1 + (1+ρ)^{−1/2}**, which lies strictly between 1 and 2 for every ρ > 0 and tends to 2 only as ρ → 0. This note governs the sentence above.

**Proof.**
1. Substitute.
2. From the proof of T3, at N\*: N\*^{1−a} > (p_g/p)^{1−a}((1+ρ)/ρ)^{1−b}, i.e. M := N\*p/p_g > ((1+ρ)/ρ)^{(1−b)/(1−a)}. Since V = M^a(ρ/(1+ρ))^b, V(N\*) > 1 ⇔ M > ((1+ρ)/ρ)^{b/a}. Since (1+ρ)/ρ > 1, this is implied whenever (1−b)/(1−a) ≥ b/a ⇔ a ≥ b. With a < b and h = 0, item 3 gives V ∝ ρ^{(b−a)/(1−a)} → 0.
3. At h = 0 and first order, the onset condition is N b ρ φ_m = φ_L (in matching units), so φ_L/φ_m = bρN\*. Then V = (φ_L/p_g)/(φ_m/p) = bρN\*·(p/p_g). Insert N\* = b^{−1/(1−a)}ρ^{−(1−b)/(1−a)}(p_g/p) (T1.3, T1.6).
4. In item 3's last expression the factor p_g/p cancels. Per-read broadcast enters only as p_g = c + Nc_b, which the same cancellation absorbs. (Check: V(N\*) = 1.9998, 1.996 and 1.98 at 1.01ρ_b, 2ρ_b and 10ρ_b with c_b/c = 10⁻³, s8.)
5. Substitute.
6. Substitute T1.5's Π\*(h′). ∎

**Checks.** 17,653 random draws with a ≥ b had a minimum V(N\*) of 1.0014 and 0 violations. The counterexample a = ⅓ < b = ⅔ gives V = 0.12, 0.012 and 0.0012 at ρ = 10⁻², 10⁻⁴ and 10⁻⁶. Price invariance holds: V = 2.0000 at p_g/p = 0.01, 1, 100 and 10⁴, and 90,003 in class A₁ at ρ = 10⁻⁴ against the formula's 90,000.

**Counterexamples.**
- a < b: the level can be born *less* vigilant (above).
- Upkeep breaks price invariance (item 6).
- Under component-unreadable reads (Proposition 11) and under bundled non-quadratic loss, V is **not derived (open)**.

**What this means for field tests (a correction).** "The lead samples the unit's common driver about twice as often" is the **onset** value in reset technologies with free upkeep. In established levels V grows as N^a (√span at γ = ½). VIGIL's P3 tested exactly this √span gradient and found 0.036 (CI −0.005 to 0.076) against 0.5, on a coarse self-report instrument (VIGIL/RESULTS.md).

**Status.** CORE_AUDIT derived V = √(N\*ρ/(1+ρ)) for γ = ½. The a ≥ b criterion, the class dependence and the **price invariance** are NEW as far as we know. Price invariance explains POOLSIM W3's unexplained V ≈ 2 under a broadcast cost.

---

## Theorem 6 (levels are complements; inclusion; lattice; accretion) — Ax1–Ax8, many sources. `s4_lattice.out`

**Hypotheses.**
- (H1) Member i's cost depends on the level set S only through its residual drift R_i(S) = q_ui + Σ_{m∉S} B_im² q_m. This holds when drift rates add (Brownian, or fBm with one common H) **and the member tracks its whole residual as one bundle**, as it does when its reads are indivisible (Ax4, Prop 9). If instead each unleveled source can be read separately at additive cost, the member cost is a sum over sources, J is **modular**, and levels for different sources are independent: no complementarity and no avalanche (`s9_attack.out` (2): marginal values identical to 3×10⁻¹⁴; FIXES F13).
- (H2) Each member cost ψ_i is concave and nondecreasing in R. This includes P(a, b) members, and also min(φ, μu) (lookup fallback) and freeze caps.
- (H3) The total level cost C(S) is submodular. That covers modular costs (one read per source) and economies of scope (bundled reads).
- (H4) Upkeep h per level (modular).

**Statement.**
- (a) **J(S) = C(S) + h|S| + Σ_i ψ_i(R_i(S)) is submodular.** Levels are complements: having one makes others for the same members more valuable.
- (b) **Inclusion.** With modular C, every source m with Σ_i ψ′_{i−}(R_i(∅))B_im²q_m > C({m}) + h (left derivatives) belongs to **every** optimal set.
- (c) **Lattice.** Optimal sets are closed under union and intersection. The largest optimal set is nonincreasing in h (Topkis 1978): **as upkeep falls, levels are only added.**
- (d) **Stakes accretion.** If additionally every ψ_i and C is positively homogeneous of the same degree a in a common stakes scale s (P(a, b), no fallback), the largest optimal set is nondecreasing in s.

**Proof.**
- (a) For fixed i, R_i(S) = R_i⁰ − Σ_{m∈S} δ_im with δ_im ≥ 0. The marginal member cost of adding m at S is −[ψ_i(R) − ψ_i(R − δ_im)] with R = R_i(S). For concave ψ, ψ(R) − ψ(R − δ) is nonincreasing in R, and R_i(S) is nonincreasing in S. So the saving from adding m is nondecreasing in S, i.e. member costs are submodular. A sum of submodular functions (C, h|S|, members) is submodular.
- (b) Exact saving of m at any S ≥ exact saving at ∅ (by (a)) ≥ first-order saving at ∅, because for concave ψ, ψ(R) − ψ(R − δ) ≥ ψ′₋(R)δ. If that exceeds C({m}) + h, adding m strictly improves any S ∌ m.
- (c) Submodularity gives J(S∪T) + J(S∩T) ≤ J(S) + J(T) = 2 min J, so both are optimal. For J(S; h) = J₀(S) + h|S| and S ⊂ T, the difference J(T; h) − J(S; h) = J₀(T) − J₀(S) + h(|T| − |S|) is increasing in h, so larger sets become relatively worse as h rises. Topkis's theorem (Topkis 1978, *Oper Res* 26:305, doi 10.1287/opre.26.2.305 [DOI and abstract verified]) gives that the largest minimizer is monotone.
- (d) J(S; s) = s^a J₀(S) + h|S|, which has the same argmins as J₀(S) + h s^{−a}|S|. Apply (c) with effective upkeep h s^{−a}. ∎

**Checks.** 300 random models with heterogeneous b_i ∈ (0.1, 0.95), half with lookup caps, random level exponents: 0/119,658 submodularity violations, 0/300 lattice failures, 0/300 inclusion failures. 2,320 h-steps: no level lost as h fell. 1,440 stakes steps without a fallback: no level lost.

**Counterexamples (each hypothesis is needed).**
- **(H2) convex member cost.** A read-rate cap with quartic loss makes ψ convex at high drift. Then J = 520, 432, 432, 504 for ∅, {1}, {2}, {1,2}. Each level pays alone, but they are substitutes: the second level's member saving drops from 320 to 160. The optima are {1} or {2}, so the union is not optimal and inclusion fails.
- **(H3) supermodular level costs** (span-of-control cost k|S|²): each level pays alone, the two together do not, and the lattice fails (s4 §6).
- **(d) without homogeneity (a bounded lookup fallback).** N = 100, ρ = 0.1, h = 0.5: the level is optimal at stakes s = 1 and lookup cost μu = 2. **At s = 4, or at μu = 1.4, it is not.** Members switch to lookup, and the level's saving drops to 0. So **cheaper lookup can dissolve levels** (s4 §4). Accretion in h still holds there, because (a)–(c) need only concavity.

**Correction to ARCH_EQUATION §2.3.** ARCH said bundled reads ("one read returns several sources") make J non-submodular. They do not: an indivisible bundled level costs √(2cΣ_{m∈S}W_mq_m), a concave function of a modular one, and so submodular. 0/93,207 violations (s4 §7). What breaks complementarity is a *supermodular* level side or a *convex* member side.

**Status.** Topkis is KNOWN. The application to tracking levels, with these hypotheses and counterexamples, is ASSEMBLY (NEW as an application as far as we know). The lookup counterexample is NEW.

---

## Theorem 7 (which scales of a nested hierarchy carry a level) — Ax1–Ax8, nested tree. `s6_depth.out`

**Setting.** Members sit in a symmetric nested tree. Scale s has groups of size n_s (increasing in s). Every member belongs to exactly one group per scale, with unit loading on that group's driver, at rate q_s = q₀ n_s^{−κ}. A level at scale s means one tracker per group, so it costs (N_tot/n_s)(φ(n_s w, q_s) + h). Level technology P(a, b); member costs ψ concave (H2 of T6).

Let c̃(n) = k p^{1−a} w^a n^{a−1} q(n)^b + h/n be the per-member cost of a level at scope n. Define **κ\* = (1−a)/(1−b) = 1/|e_g|**.

**Statement.**
- (a) **Exact ordering.** If c̃(n)/q(n) is strictly decreasing in n, every optimal set of scales is an **upper set**: levels fill from the broadest scale downward (top-down). If it is strictly increasing, every optimal set is a **lower set** (bottom-up). For q ∝ n^{−κ}:
  - h = 0: top-down iff κ < κ\*, bottom-up iff κ > κ\*;
  - h > 0: top-down if κ < min(κ\*, 1), bottom-up if κ > max(κ\*, 1).
- (b) **Class dependence.** κ\* is the **level** technology's (a, b), while member costs need only be concave. κ\* = 1 for R1 and R2, and κ\* = 1/(1+θ) for A_θ (½ at θ = 1). The same environment (κ = 0.7) builds top-down hierarchies with reset sensing and bottom-up ones with averaging sensing.
- (c) **First-order location.** With small shares and h = 0, scale s is kept iff n_s^{1−a} q_s^{1−b} > (p_g/p)^{1−a} R^{1−b}/b. With q_s = q₀n_s^{−κ} that is n_s^{(1−b)(κ\*−κ)} > (p_g/p)^{1−a}(R/q₀)^{1−b}/b, where R is the member's residual drift (which itself includes the untracked scales).

**Proof.**
- (a) Let L be optimal, s ∈ L, s′ ∉ L, with n_{s′} > n_s in the decreasing case. Write Δψ(q | R) = ψ(R) − ψ(R − q) and m(q | R) = Δψ/q, the mean of ψ′ over [R − q, R]. Optimality of L gives m(q_s | R_{L∖s}) ≥ c̃_s/q_s. The interval [R_{L∖s} − q_s, R_{L∖s}] = [R_L, R_L + q_s] lies to the right of [R_L − q_{s′}, R_L]. Because ψ′ is nonincreasing, m(q_{s′} | R_L) ≥ ψ′(R_L) ≥ m(q_s | R_{L∖s}) ≥ c̃_s/q_s > c̃_{s′}/q_{s′}. So adding s′ strictly lowers J, which contradicts optimality. The increasing case is symmetric. For the power form, c̃/q = K n^{−(1−b)(κ\*−κ)} + (h/q₀) n^{κ−1}, which gives the conditions.
- (b) Lemma 1.
- (c) This is T6(b)'s first-order rule for one scale. ∎

**Checks.**
- Heterogeneous concave members ψ_i = k_iR^{b_i} with a common residual gave 0/120 non-upper sets (`s9_attack.out` (3)).
- In class R, κ < 1 gave an upper set in 13/13 and 11/11 q₀ values. 150 random (a, b, κ < κ\*, h) gave 0 non-upper optimal sets. κ = 2 gave lower sets. The first-order set was a subset of the exact set in every case.
- One mismatch note: the class-A runs at the tested sizes (n ≤ 2¹⁴) mostly formed no levels, because N\*ρ² = 27 needs large groups. That is consistent, but thin evidence for (b) in class A.

**Proposition 7.1 (depth avalanches; NUMERICAL).** Because of complementarity (T6a), optimal depth can jump discontinuously as shared drift grows. In class R with κ = 1.4, depth is 0 for q₀ up to 10^{3.75}, then **14 (every scale)** at q₀ ≥ 10⁴, while the first-order rule keeps **no** scale. For κ = 0.3, depth grows 2 → 10 gradually, then jumps 10 → 14. Removing all shared drift raises every remaining level's shadow price ψ′(R) at once. Not proved in general.

**Status.** The ordering theorem with κ\* = 1/|e_g| is NEW as far as we know. It corrects ARCH §2.3(f), whose knife edge "κ = 1" holds only for a = b. The avalanche is a NUMERICAL observation. Willsky's multiscale trees (estimation on given trees) are the KNOWN neighbour [R-abs in ARCH].

---

## Theorem 8 (freeze, hold or look up; the fallback cliff) — Ax1–Ax8, one item. `s5_phase.out`

**Setting.** R1, quadratic loss, stakes W per user, drift q, read cost c, upkeep h, lifetime H_l, use rate μ, lookup cost u per use (μu > h). Hold cost min_{T ≤ H_l}[c/T + WqT/2] + h; freezing is the corner T = H_l; lookup costs μu.

**Statement.**
1. Freeze edge: T\* ≥ H_l ⇔ **q ≤ q_f = 2c/(WH_l²)**.
2. Lookup edge: lookup beats interior holding ⇔ **q > q_c = (μu − h)²/(2cW)**. The elasticity of q_c in u is 2μu/(μu − h), which is 2 at h = 0. For σ_c = √q_c it is 1 at h = 0.
3. **Hold band exists ⇔ μuH_l > 2c + hH_l**: holding any drifting item pays only if lifetime lookup spending exceeds two reads plus lifetime upkeep.
4. **Shared store** (N users: W → NW, lookup → Nμu): at h = 0, (q_c/q_f) is multiplied by **N²**, so the band widens by 2 ln N in log drift. A shared band survives until **u < (2c + hH_l)/(NμH_l)**.
5. **Cliff.** Effort just below q_c is (μu − h)/(2c) > 0, and above q_c it is 0. Effort is discontinuous: a cliff, not a hump.
6. **Power class.** With hold cost kW^aq^b + h, q_c = ((μu − h)/(kW^a))^{1/b}, its elasticity in u at h = 0 is 1/b (3 for A₁), and the shared edge rises N^{(1−a)/b}-fold.

**Proof.** Elementary; sympy gives the edges, factors q_c − q_f = (H_l(μu − h) − 2c)(H_l(μu − h) + 2c)/(2H_l²Wc), and confirms the N² ratio and the 1/b elasticity. ∎

**Checks.** 2,000 random parameter sets on a 1,400-point q grid: 0 mismatches in band existence, and edge errors within one grid step.

**Counterexamples.**
- If μu ≤ h, holding never pays.
- If lookups return stale values or carry their own lag, the lookup cost is no longer flat in q and the edge moves (not derived).
- With unbounded loss and no fallback, effort rises without bound: no cliff (T5 in the repo).

**Carried-over Poisson case (repo T5, KNOWN core: Cho & Garcia-Molina 2003).** For change rate λ, use rate μ, bounded miss loss W_b and refresh cost c, f\* > 0 iff λ < μW_b/c. 0/3,000 mismatches (s5 §5).

**Status.** The cliff is KNOWN (Cho & Garcia-Molina; T5b). The hold-band existence condition, the N² widening and the power-class generalization are NEW as far as we know (ASSEMBLY). Qualitative offloading is prior art (Risko & Gilbert 2016; Sparrow et al. 2011 [M]).

---

## Proposition 9 (clocks) — KNOWN. `s7_misc.out` (a)

With K independent, separately readable components at additive read cost in P(γ, γ), separate clocks save **at most 1 − K^{−(1−γ)}** (29.3% for K = 2, γ = ½): 5.1%, 14.3% and 22.6% at separations 2, 4 and 10. With **indivisible** reads (one read returns all components), separate clocks **never** save, because Σ(q_k)^γ ≥ (Σq_k)^γ. Checks: 20,000 random cases, saving in [0, cap), and 0 positive savings with indivisible reads. KNOWN (Cauchy–Schwarz/Hölder; Roundy 1985 [M, unverified]).

## Proposition 10 (selection resolution makes onset a threshold in ρ) — Ax7 with ε > 0. `s7_misc.out` (b)

In 𝒜₁, a level's largest possible fractional saving (N → ∞) is **1 − (1+ρ)^{−b} ≤ bρ**. With a relative resolution ε, **no level is selected at any N when ρ ≤ (1−ε)^{−1/b} − 1 ≈ ε/b**: 0.020 at ε = 1% and 0.108 at ε = 5% (b = ½). An absolute resolution acts like upkeep: T1.5 applies, so the exponent survives but the N·ρ collapse does not. Proof: per-member nested cost → φ(w, q_u) as N → ∞ (a < 1). Bernoulli's inequality gives the bound (0/20,000 violations). This is the formal version of POOLSIM's findability rule. Status: elementary; the use is NEW.

## Proposition 11 (readability: the exponent survives, the constant does not) — Ax4 relaxed. `s7_misc.out` (c). NUMERICAL

Suppose members can read only x_i, not u_i, and set û_i = x_i(t) − ĝ(t) at their own read times t (R1, quadratic, Brownian, independent phases). The member's error then contains the level's error at the member's read time as well as now. When the member's reads coincide with level reads, the shared term is the component-readable T_g/2 per unit q_g. As T_g/T_u → 0, a level read almost surely falls between member reads, and the shared term approaches E[σ′ + σ] = T_g. That doubles the level's effective stakes and gives Π\* → 2 × 4 = 8. There is no general lower bound: if members read much more often than the level, the shared term is smaller. Numerically, N\*ρ = **7.35 at ρ = 0.03 and 7.28 at ρ = 0.01** (against 4.06 and 4.02 with component readability), so the local e_g = −0.99. **The −1 survives. The constant "4" depends on the readability axiom.** Vigilance under this scheme is not derived.

## Carried over, not re-proved here (see the repo's `theory/THEOREMS.md`)

T1 (EOQ/Kalman; cosh robustness, KNOWN); T2 (cheap watcher, EOQ algebra); T4 (√N shared-trace fade, Kalman averaging, KNOWN math); T6 (Still et al. 2012, KNOWN); T7b (geometric clocks, Roundy-type, known in substance); T8–T9 (KNOWN; T9's link is analogy).

---

## Summary table

| # | Result | Status in 𝓜 | Novelty | Key hypotheses whose failure is shown to break it |
|---|---|---|---|---|
| L1 | (a, b) per technology; drift-invariant pricing ⇒ a = b; averaging b = a/2 | Proved | ASSEMBLY (classification NEW) | estimator restriction for H ≠ ½ |
| T1 | N\* = [ρ^b/((1+ρ)^b−1)]^{1/(1−a)}; e_g → −(1−b)/(1−a); upkeep dichotomy; volatility/stakes effects | Proved | KNOWN in substance (V&W 2007); exact form NEW | a = 1 (no level), b = 1 (e_u = 0), ρ large, κ_b > 0 |
| T2 | Broadcast: onset is a ρ threshold; per-read ρ_b = 4t/(1−t)² | Proved | NEW form; mechanism known (Garicano) | — |
| T3 | ∂N\*/∂q_g < 0 < ∂N\*/∂q_u at every ρ | Proved | NEW signed form | convex cost, b = 1, a = 1 |
| T4 | Bundled loss: e_g set by technology, not loss (−1 for R; −(1+θ) for A_θ) | Proved (remainder by estimate) + exact numerics | NEW | separable decisions; α-stable (open); correlated errors |
| T5 | Vigilance > 1 iff a ≥ b; 2 at γ = ½; price-invariant; ∝ ρ^{−θ} in A_θ; grows as N^a | Proved | NEW (except V formula, CORE_AUDIT) | a < b; upkeep (price-dependence) |
| T6 | Submodular J; inclusion; lattice; accretion in h; in stakes without fallback | Proved | KNOWN theorem (Topkis), ASSEMBLY | convex member cost; supermodular level cost; lookup fallback breaks stakes/u monotonicity |
| T7 | Top-down iff κ < κ\* = 1/\|e_g\| (exact ordering) | Proved | NEW | non-monotone c̃/q; h > 0 needs κ vs 1 too |
| P7.1 | Depth avalanches | NUMERICAL | NEW | — |
| T8 | Freeze/hold/lookup edges; band iff μuH_l > 2c + hH_l; N² widening; cliff | Proved | cliff KNOWN; rest ASSEMBLY/NEW | μu ≤ h; stale lookups |
| P9 | Clock ceiling 1 − K^{−(1−γ)}; 0 with indivisible reads | Proved | KNOWN | — |
| P10 | Resolution ε ⇒ no level for ρ ≲ ε/b | Proved | NEW use | — |
| P11 | Readability changes Π\* (4 → ≈7.3), not e_g | NUMERICAL | NEW | — |
