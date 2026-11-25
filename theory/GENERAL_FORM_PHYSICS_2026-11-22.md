# The physics-derived general form of the cost of judgment

*Sunday 22 November 2026. Draft proposal. A self-check, not an independent review. Read from `main` at `6ca6b45`. It adds no CLAIM_MAP row and edits no locked preregistration. `THEORY.md` is not edited. Where this note and `THEORY.md` disagree, `THEORY.md` governs. The hypothesis sentence below is the sentence in THEORY §3, CORE, and README, copied and not rewritten.*

The selection form is `theory/GENERAL_FORM.md` (Lemma LY, PR #161, merged as `2dd04fa`; confirm #164 `01e4415`). The heat results this note consolidates are `theory/INFO_PHYSICS.md` (PR #175, merged as `f18f21f`; reviews #176 and #177), `theory/INFO_PHYSICS_ATTAINABILITY.md` (PR #178, merged as `b46bf9f`; review #179), and `theory/INFO_PHYSICS_GENERAL.md` (PR #180, merged as `d1d6ea5`; review #181). The dated correction is `theory/INFO_PHYSICS_CORRECTION_2026-11-22.md`. Nothing below re-proves those pages. A lower bound is not a derivation of the cost.

## 0. Hold this

Judgment, where the physics has been derived, costs two things. The bath that holds the memory gives off heat. The action taken from the memory is wrong by some amount, and a stake weights that error. Add the two. A limit on the chance of ruin stands beside the sum. It is not an item inside the sum.

The heat cannot fall below temperature times the rate at which the memory has to learn in order to hold its error. That rate is in nats per unit time, and the heat floor is temperature times the rate. The bound is proved for an equilibrium Ornstein–Uhlenbeck signal, for independent collections of those signals, and for a signal that flips between two states. For one equilibrium OU signal the rate's floor is the Kalman rate, and a fast linear memory approaches the heat floor while the heat stays finite. For the two-state signal the floor is a different formula, and a fast memory approaches that floor too.

Several independent equilibrium OU signals, each scored on its own, add their floors. A slow signal is worth tracking at a lower stake than a fast signal of the same size. When the speeds form a ladder, each a fixed multiple of the one before, the number of signals the design tracks goes up by one each time the stake is multiplied by that same multiple. When the loss is only the error in the sum, one memory, with one weight on each signal, approaches the floor. A separate memory for each signal costs more heat. When the signals are identical, separate memories cost exactly as many times the heat at the same error.

A price per nat stored, and a constant upkeep per layer, are not this heat. A machine can pay more than the floor. That extra is the machine: a finite speed, a readout that scores the wrong number, a state that keeps a history the action does not use, or a cycle that does not cut the error. The stake, the cost of handing someone a copy, and the ruin limit are still assumptions. The worlds are narrow. The sentence of the hypothesis is unchanged.

## 1. The form

**Selection.** Under H1–H3, every maximizer of long-run growth is Pareto in a chosen bad vector: a dominated design is not kept (Lemma LY, **PROVED (in-model)**, GF1). The lemma does not choose the vector. H3, that offspring falls in each coordinate with the others held fixed, is assumed. The selection axioms A1 and A2-L are not this lemma. They take a scalar cost as already defined.

**Physics.** In steady state the bath of the learning subsystem obeys \(\dot Q\ge kT\) times the learning rate (Horowitz and Esposito 2014). The learning rate of a sensor is at most the entropy production of that subsystem (Barato, Hartich, and Seifert 2014). Those are the second-law statements used here. They bound a heat. They do not list the terms of a cost.

**The cost, inside the class of §3.** With the ruin cap kept outside the sum,

\[
J_{\mathrm{phys}}=\dot Q+w\,\mathbb{E}[\ell].
\]

\(\dot Q\) is the medium heat rate of the memory's bath. \(w\) converts the decision loss into the same currency. The information flow and the Kalman rate are rates in nats per unit time. \(kT\) times either rate is a lower bound on \(\dot Q\). Equality with that floor is approached in a limit of diverging internal rate, at finite heat.

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

The sentence is unchanged. "Strongly selected" remains the five-part operational definition in THEORY §3.

## 2. How this sits next to the other general form

`theory/GENERAL_FORM.md` is the selection form. Copying, when offspring falls in each coordinate of a vector handed to it, refuses a dominated design. If the growth exponent is known, the selected set is its argmax. If only the monotonicity is known, the Pareto front is an identified set, and occupation of that front is not proved (V5 **OPEN**). A log-linear map makes growth minimize a nonnegative linear cost in growth units (corollary LY-c). That cost is not expected currency (V2). The coordinates are an input.

This note does not replace that form. It names two coordinates physics has priced, inside one class: memory-bath heat, and a decision loss. If H3 holds for those two, Lemma LY puts a growth-maximizing lineage on the non-dominated part of that front. The scalar \(J_{\mathrm{phys}}\) is the heat-plus-stake sum, which is expected currency plus a weight. It is not corollary LY-c, and it is not the five-term master equation. IP5 stays **FALSE**: the master equation is not the Lagrangian of the physical frontier.

Two other fronts stay different objects. Theorem S2's frontier is \((I,r,K,D)\). V5's five names are memory held, information bought, error, attention, and ruin risk. GF2 says attention is not a derived bad. This heat-and-error front is neither of those vectors.

## 3. Scope

The floor and the attainment are proved for the following, and not beyond it.

- **Signal.** An exogenous equilibrium Ornstein–Uhlenbeck process, \(dX=-aX\,dt+\sqrt{2av}\,dW\), variance \(v\). This is the stationary scalar Gauss–Markov diffusion. Independent collections of such modes are included. The two-state telegraph, flipping at rate \(\gamma\) each way, is included, and it is not a Gauss–Markov signal. The memory does not act back on the signal (P-X, A-X, G-X). A memory that moves its world is CX2, **OPEN**.
- **The signal's own bath pays nothing.** Its medium heat is zero. A driven signal, whose bath can pay, is the case already recorded in `theory/SCALE_ENDS.md` SE3 and in the receptor of Barato, Hartich, and Seifert 2014. A general rule for which bath pays is **OPEN**. This note adds no counterexample.
- **Loss.** Mean squared error of an action of the current memory state, \(\varepsilon=\mathbb{E}[(g(M)-X)^2]\). The smallest such error is the conditional error, at \(g(M)=\mathbb{E}[X\mid M]\). On the telegraph the proved floor is Hamming error, \(P(M\neq X)\). A loss that is not one of those two stays open.
- **Not this floor.** A discrete-time Gauss–Markov source, the information floor in CORE (efficiency \(0.9574\) on one world), and joint achievability of that information floor (Shannon note §3) are a different gap. They are not this heat.

The centered spring \(dM=-\lambda(M-X)\,dt\), scored by the raw coordinate error \(\mathbb{E}[(M-X)^2]\), remains the family the reviews of PR #175 scored. At fixed raw error below the signal variance, the heat falls toward \(kT\,av/\varepsilon\). The information flow, in nats per unit time, rises from the Kalman rate \(a(v-\varepsilon)/\varepsilon\) up to \(av/\varepsilon\). The heat's fast limit and \(kT\) times the Kalman rate differ by \(kT\,a\). That statement stands. It is a scoring gap once the loss is the decision, not the floor of the decision loss. The correction record says which sentences of the merged note are superseded, and for which loss.

## 4. The floor, and that a linear memory approaches it

**One equilibrium OU signal (IP11, PROVED (in-model)).** For a regular conditional, the learning rate is

\[
L=a\big(v\,\mathbb{E}[F(X\mid M)]-1\big)\ge R(\varepsilon)=a\frac{v-\varepsilon}{\varepsilon},
\]

with \(F\) the conditional Fisher information. The inequality is Fisher, then Jensen. Duncan's theorem is the path mutual information. It equals \(R\) at the path error, and it equals the learning rate only when the current state is a sufficient statistic of the path. Horowitz and Esposito put the memory-bath heat at least at \(kT\,L\), hence at least at \(kT\,R(\varepsilon)\).

A spring with rest point \(cX\), \(c=1-\varepsilon/v\), has finite Sekimoto heat at every finite rate, and the heat approaches \(kT\,R(\varepsilon)\) as the rate diverges. At \(a=v=kT=1\), \(\varepsilon=0.2\), rate \(10^6\), the heat is \(800000/199999=4.0000200001\), against the rate \(R=4\). The centered spring, raw coordinate error held at \(0.25\), read out by \(g(M)=\mathbb{E}[X\mid M]\), has decision error \(0.20000032\) and heat \(4.000012\). One design puts the gain in the force. The other puts it in the action. The constant \(kT\,a\) is what appears when the centered coordinate is scored by its raw error instead. At raw error \(0.2\) and the same rate the heat is \(5.000020\).

**The telegraph (IP3, PROVED (in-model)).** At Hamming error \(\varepsilon\) the information flow, in nats per unit time, is \(\dot I=\gamma(1-2\varepsilon)\ln((1-\varepsilon)/\varepsilon)\). The heat is \(kT\,\gamma(1-2\varepsilon)\ln\rho\) for every rate ratio \(\rho>(1-\varepsilon)/\varepsilon\). The infimum of the heat is \(kT\,\dot I\), approached as the memory rates diverge at the minimal affinity. At \(\varepsilon=0.2\), \(\gamma=1\), \(kT=1\), that infimum is \(0.6\ln 4=0.831776616672\). The flow is \(0.6\ln 4\) nats per unit time at every temperature; the heat infimum equals that number only because \(kT=1\). A finite affinity pays the excess \(kT\,\gamma(1-2\varepsilon)\ln(\rho/\rho_\star)\).

**Independent modes, each scored on its own (IP12, PROVED (in-model)).** The learning-rate bound of one joint memory at per-mode decision errors \(s_k\) is \(\sum_k R_k(s_k)\), in nats per unit time. An off-diagonal error covariance raises it. That sum is the steady Kalman–Bucy rate of the product filter at those variances. The heat infimum is \(kT\) times the sum. A product of fast shrunk springs approaches it. At \(kT=1\) the heats are \(4.000020\) and \(16.000320\) against floors \(4\) and \(16\).

**The sum of the modes (IP13, PROVED (in-model)).** The loss is \(\mathbb{E}[(g(M)-\sum_k X_k)^2]\). The minimum of the covariance bound at sum-error \(\varepsilon\) is the unique \(\mu\ge 0\) with

\[
\varepsilon=\sum_k\frac{a_k v_k}{a_k+\mu},
\]

and the minimum value of the learning rate is \(\mu\), in nats per unit time. The heat infimum is \(kT\mu\). The minimizing channel is rank one, with gains \(g_k=1/(a_k+\mu)\). One fast linear memory approaches heat \(kT\mu\). Extra coordinates cannot undercut the bound. For \(K\) identical modes the sum is one OU signal of variance \(Kv\), the floor is the scalar floor of that signal, and \(K\) separate memories cost exactly \(K\) times that heat at every matched error. At rates \((1,100)\), variances \((1,1)\), and sum-error \(0.5\), \(\mu=103.887732673340\). Separate memories at that error have heat \(141\), ratio \(1.357234\). The spring at rate \(10^6\) has sum-error \(0.500077\) and heat \(103.877719\). The floor at that error is \(103.856919\) (`reviews/heat_floor_general_2026-11-22/recompute.out`).

On the designs that approach the OU floor, the path rate stays large. At rate \(10^6\) and decision error \(0.2\) the path rate is \(999.503125\) and the sensory capacity \(L/\mathcal T\) is \(0.004002\). Hartich, Barato, and Seifert's factor \(2\), and Sandberg, Delvenne, Newton, and Mitter's factor \(2\) on the transfer entropy, cover a state that keeps the path. They do not apply to this design. A capacity-1 state at the same decision error costs \(8\).

## 5. The frontiers

Minimize heat floor plus \(w\) times error. \(w\) is supplied. \(kT\) does not set it.

**One OU signal.** The minimizer is blind, error \(v\), heat \(0\), cost \(wv\), when \(w\le kT a/v\). Above that stake the error is \(\sqrt{kT\,av/w}\) and

\[
J_{\mathrm{phys}}^{\star}(w)=2\sqrt{kT\,a\,v\,w}-kT\,a.
\]

At \(a=v=kT=1\) and stake \(2\) this frontier tracks, cost \(1.828427124746\). The centered spring scored by raw coordinate error is blind at that stake, cost \(2\), because its floor is higher by \(kT a\). The two objectives disagree on whether to track for stakes between \(kT a/v\) and \(4kT a/v\). Where both track, the constant \(kT a\) does not move the minimizing error.

**Per-mode loss.** The frontier is the sum of the scalar frontiers. Mode \(k\) is blind when \(w\le kT a_k/v_k\). For rates \(a,\,a\rho,\,a\rho^2,\ldots\) and equal variances, once the slowest mode pays and until the ladder runs out, the tracked count is

\[
\left\lfloor\frac{\log(wv/(kT a))}{\log\rho}\right\rfloor+1.
\]

Multiplying the stake by \(\rho\) adds one mode. Three modes at rates \((1,10,100)\), unit variance, stake \(2\): only the slowest is tracked, cost \(5.828427124746\).

**Sum loss.** The design is blind, cost \(w\sum v_k\), when

\[
w\le w_0=\frac{kT}{\sum_k v_k/a_k}.
\]

Above \(w_0\) one coordinate is optimal, with \(\mu\) set by \(\sum_k a_k v_k/(a_k+\mu)^2=kT/w\). No mode is exactly blind once \(\mu>0\). A mode with \(a_k\gg\mu\) keeps almost its whole prior variance inside the sum. The count of modes whose sum-error contribution is at least halved is \(\#\{k:a_k\le\mu\}\). On an infinite geometric ladder of equal variances, multiplying the stake by \(\rho\) raises that count by one. For four modes at rates \(1,10,100,1000\), equal variance, and \(kT=1\), \(w_0=1000/1111\). On that finite ladder the half-tracked count and the per-mode count are not the same integer at every stake. For \(K\) identical modes the sum-loss frontier is the scalar frontier of variance \(Kv\), and the blind stake is \(kT a/(Kv)\), which is lower than the per-mode threshold \(kT a/v\) by the factor \(K\).

## 6. Layer count

`measurement/LAYER_COUNT_RULE.md` (N65, T15) counts poles of a measured kernel by degree, and predicts \(K^\star\) as the leftmost minimizer of \(K+R(1+\varepsilon_K)\) with stake ratio \(R=w E_\infty/h\). When the decrements of \(\varepsilon_K\) are non-increasing, that minimizer is the from-0 count of Fox 1966 (N64). A closed form in the poles and the stake alone, without the curve \(\varepsilon_K\), is T18 and stays open. The constant \(h\) is an input of that rule. N65 is unchanged.

The counts in §5 do not use \(h\).

They agree with N65 on four points already stated in `theory/INFO_PHYSICS_GENERAL.md` §7. There is a blind regime. The count does not fall as the stake rises. On a per-mode memory the count is at most the number of separated real modes. Slow content comes first when variances are equal.

They differ on four points, from the same section. The price of a tracked mode here is the heat \(kT a_k(v_k-s_k)/s_k\), whose derivative at the prior is \(kT a_k/v_k\). N65 prices the next degree at \(h\), whatever the pole. The timescale ratio enters the per-mode count as the logarithm above. It enters N65 only by shaping \(\varepsilon_K\). On the sum loss the heat-optimal memory has one coordinate at every stake above \(w_0\), while the half-tracked mode count grows. N65's \(K^\star\) is a degree of a filter of the scalar series. When the rates are identical, the sum is one mode, and neither the heat floor nor the degree of that sum selects \(K\) separate memories.

Kolmogorov's reverse water-filling and Sims's mutual-information price allocate a \(\tfrac12\log\) rate. Gorbunov and Pinsker (1973, 1974) are the nonanticipative rate of that same shape. Crossref returned no work record for either English translation, so this note cites them with no DOI. Stavrou, Charalambous, Charalambous, Loyka, and Skoglund are that same shape of rate. Tanaka, Kim, Parrilo, and Mitter is the discrete-time sequential program in directed information. Tanaka, Skoglund, and Ugrinovskii minimize the Duncan rate of a continuous-time vector Gauss–Markov source under \(\operatorname{tr}(P)\le D\). That constraint is the sum of the marginal mean squares. It is not the square error of the sum, and the paper contains no bath heat. The allocation here is \(\sum a_k(v_k-s_k)/s_k\), or the single level \(\mu\). Those functionals meet \(\tfrac12\log\) only at isolated errors. The mode count is a count of rates below \(wv/(kT)\), not a count of peaks of a spectrum.

## 7. The map from the master equation

The equation in THEORY §3, which this note does not edit, is

\[
J=\kappa I_{\mathrm{mem}}+hK+w\,\mathbb{E}[\ell]+A+L
\qquad\text{subject to}\qquad P(\mathrm{ruin})\le\varepsilon_r.
\]

| Term of \(J\) | Inside the class of §3 |
|---|---|
| \(\kappa I_{\mathrm{mem}}\) | **Replaced** by the memory-bath heat \(\dot Q\). The floor on that heat is \(kT\) times the learning rate of §4. The gross past stock is not the coordinate. Still's per-update difference is a different functional. A rental \(\kappa\ge kT/\tau\) is the accounting in `core/bridge_2026-11-21/FLOOR.md` once a turnover time is chosen. The second law does not choose \(\tau\) |
| \(hK\) | **Not a term of the floor.** Separate baths add their heats. One bath has one heat. On the sum loss the heat-optimal memory has one coordinate. A constant \(h\) that the books still carry is implementation excess above the floor. The gap \(kT a\) on the raw coordinate is a scoring gap, not an upkeep |
| \(w\,\mathbb{E}[\ell]\) | **Survives.** \(w\) stays assumed. \(kT\) does not set it. Lateness counted as error is the reading of \(\ell\) already in THEORY. The losses for which the floor is proved are the mean square of §3 and Hamming error on the telegraph |
| \(A\) | **Stays assumed as a separate summand.** For a continuously coupled sensor the read is inside \(\dot Q\). A separate measurement-and-erasure operation is the Sagawa–Ueda sum, once, not a second price on the same nats. The inequality \(A\ge c\cdot r\) (S-A) is an assumption. It is not derived |
| \(L\) | **Stays assumed, and stays outside \(J_{\mathrm{phys}}\).** A copy that is made has a floor (Ouldridge, Govern, and ten Wolde; Ouldridge and ten Wolde). A design that does not copy does not pay it. Neither paper supplies a linear linking price on every design |
| \(P(\mathrm{ruin})\le\varepsilon_r\) | **Stays outside. Stays assumed.** None of these heat bounds is a statement about a reserve hitting zero |

**Implementation excess** is \(\dot Q\) minus the floor at the same decision error. It is not a new term. It is the machine:

- a finite memory rate, the factor \(\varphi\varepsilon/(\varphi(v+\varepsilon)-v)\) on the shrunk spring, above \(1\), where the fast fraction is \(\varphi=\lambda/(a+\lambda)\). The symbol \(\rho\) stays the telegraph rate ratio and the ladder ratio;
- scoring the centered coordinate's raw error, the added \(kT a\);
- a state that keeps the path, the factor \(2\) of Hartich, Barato, and Seifert, and of Sandberg, Delvenne, Newton, and Mitter, equation (46);
- a non-Gaussian conditional, the Fisher excess; the heat infimum on an equilibrium OU signal remains \(kT\) times the Gaussian learning rate, because the shrunk springs approach it;
- a futile affinity on the telegraph, \(kT\,\gamma(1-2\varepsilon)\ln(\rho/\rho_\star)\);
- separate memories of one sum, the factor \(K\) when the modes are identical, and the ratio \(1.357234\) at the unequal rates above.

A constant \(h\), or a stock rental \(\kappa I_{\mathrm{mem}}\) charged on top of the heat, is further excess of the same kind if the books still carry it. It is not forced by the balance.

The theorems in THEORY that minimize the five-term \(J\) are theorems about that display. Adopting §9 would not, by itself, re-prove them under \(J_{\mathrm{phys}}\).

## 8. What stays assumed, and what is open

**Assumed, and not half-derived.** Calling these open problems would overstate how close the physics came. They are absent from the bound.

- The stake \(w\).
- \(A\) as a separate summand, including S-A.
- \(L\) as a term of every design.
- The ruin cap.
- H3 on the heat and the error. Lemma LY applies to this front only if offspring falls in those coordinates. GB6 stays **FALSE** for "from first principles."
- Risk-neutral expected currency as the exact objective (V2). The diffusion limit of growth keeps \(\mu-\sigma^2/2\). It does not yield \(J\) or \(J_{\mathrm{phys}}\) (GB3, GB5, both **FALSE**).
- Which implementation is in use, and therefore which point on a fixed-error curve is paid.
- That the memory's bath is the bath that pays, outside the telegraph, the linear family, and the product of shrunk springs.

**Open, inside the physics, and not closed by this note.** These are IP10 and IP14, restated as one list. No status moves.

- A signal that is not an exogenous equilibrium OU and not the telegraph.
- A general rule for which bath pays. The case in which another bath pays is already on the record.
- A loss that is not a mean square of an action of the current state, and not Hamming error on the telegraph.
- A memory that changes the signal.
- The bath heat of a \(K\)-state channel. The learning rates are computed (a soft 64-bin channel at decision error \(0.2\) has learning rate \(4.022937\)). The heat equality is not. A hard bin is outside the regularity condition.
- Equality at a finite memory rate. The infimum is a limit, as on the telegraph. At rate \(6\) the shrunk-spring gain is \(1.2\), so the coordinate is not yet the conditional mean.
- Whether a capacity-1 design can pay less than twice the learning rate. Hartich, Barato, and Seifert prove it cannot for a bipartite process, under the fictitious-memory step in their §V. This note does not extend that theorem.
- A joint jump memory of several telegraphs, against \(K\) separate telegraph floors.
- Attainment for every error covariance of a coupled equilibrium diffusion. One numerical design, at rate \(10^5\), has heat \(7.999913\) against its static rate \(8\). That is one design, not the general attainment.
- A degree-\(K\) filter of the scalar series alone, with no mode-resolved gain, when the rates differ. The unweighted sum is optimal when the rates are equal, because then the sum is one OU signal.
- Whether a system that qualifies under THEORY §3 has a binding ratio near \(1\) (IP7). That measurement is already OPEN_WORK T10. This row is not a preregistration.

**Not this list.** N65, T15, and T18 are unchanged. Joint achievability of the Shannon information floor is unchanged. The public-test search (T35) and the parked currency sentence (T36) are unchanged.

Adopting the rewrite in §9 into THEORY §3 is OPEN_WORK T40. It is not done.

## 9. Proposed rewrite of the THEORY.md cost section

Not applied. The hypothesis sentence is not in either hunk. It stays, byte for byte,

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

**Hunk 1.** Replace THEORY.md from the heading `## 3. The master equation` through the paragraph that ends `the term list, the cap, and the linear prices stay assumptions.` Leave the hypothesis sentence, and everything after it, as they stand.

```diff
--- a/THEORY.md
+++ b/THEORY.md
@@
-## 3. The master equation
-
-A system that must act ahead of a world it does not control chooses its design 𝒟 to
-
-$$
-\min_{\mathcal D}\; J(\mathcal D) \;=\; \underbrace{\kappa\, I_{\text{mem}} + h\,K}_{\text{holding memory}} \;+\; \underbrace{w\,\mathbb E[\ell_{\mathcal D}]}_{\text{being wrong or late}} \;+\; \underbrace{A(\mathcal D) + L(\mathcal D)}_{\text{acquiring and sharing information}} \qquad \text{subject to}\quad P(\text{ruin}) \le \varepsilon_r .
-$$
-
-- **𝒟**, the design: the number of layers K, what each tracks, how and how often it senses, and what it shares.
-- **κ·I_mem + h·K**: the price κ per nat held per unit time, and the upkeep h of each layer, store or shared level.
-- **w·E[ℓ]**: the stake times the expected loss at the moment of use. Lateness counts as error, because a prediction that arrives after the moment to act buys nothing.
-- **A(𝒟)**: information-acquisition spend, priced per read (Σ c_k f_k, read price times read rate), per nat acquired (λ), or per unit of precision (c′·r^{−θ}).
-- **L(𝒟)**: link, telling and lookup costs: κ_b per member–level link, d per member told, u per lookup at use rate μ. This is what puts pooling and sharing inside J.
-- **Ruin**: a reserve that starts at buffer B, earns income y and pays J hits zero; ε_r is the tolerated chance.
-- **The world** is exogenous and enters only through its measured pattern of change: its spectrum or Markov kernel, the sensing noise N and the lead k at which actions meet it. The drift level q and spectral slope α are the scale-free special case.
-- **One currency per system** (heat, attention, money, compute). Physics sets floors on the prices (at least kT per nat acquired or erased by a measuring tracker, and kT·(I_mem − I_pred) for memory that does not predict: Landauer 1961, Still et al. 2012), not exchange rates between systems. In each system's own units the equation is the same problem at every scale: only dimensionless ratios matter, and the optimal cost shares are currency-free (CT24); the distance from the floor is one measured number per system.
-- **Open lever.** Effort g spent making the world drift less (homeostasis, buffers, contracts) belongs in the problem, but it makes the world depend on the design. Except for the coupled-party results of B.10 (CT29–CT32), the theorems of THEORY hold the outer world fixed at this g = 0. A responding world may be modelled as one more party. A potential theorem applies only when the beta-scaled game is an exact potential. Drift-intensity reduction itself stays open (CL11). T61 and co-adaptation F3/F4 are related and are not the same result.
-
-The equation is assembled from known parts; the repository already wrote it as Axiom 5 of `reviews/night1/formal/AXIOMS.md`. It is the theory's statement of the problem, not a theorem. When that form is forced, and when it is not, is `theory/REPRESENTATION.md`: on a product of intervals the cost is additive up to a positive affine transformation, nonnegative prices need the further assumption that each concatenating coordinate is a bad, and a discrete layer count is not part of the cited Debreu theorem. Storing, predicting, acting and staying solvent do not force it. Whether the equation is a limit of growth selection is `theory/GROWTH_BRIDGE.md` (CLAIM_MAP section X). On a gapped finite menu, weak selection recovers the ranking only. The diffusion limit keeps \(\mu-\sigma^2/2\). An interior stake separates the argmaxes. The term list and the cap are inputs. Whether dissipation forces those terms is `theory/INFO_PHYSICS.md` (CLAIM_MAP section Y). It does not: a free-energy rate is bounded below by an information flow, the bound is not the cost, and the term list, the cap, and the linear prices stay assumptions.
+## 3. The master equation
+
+A system that must act ahead of a world it does not control chooses its design 𝒟 to minimize a cost of judgment. Two displays are in use. They are not the same object. The theorems after this section are theorems about the five-term display. They are not, by this paragraph, theorems about the heat display.
+
+**Outside the class below,** and wherever a term has not been derived, the cost is
+
+$$
+\min_{\mathcal D}\; J(\mathcal D) \;=\; \underbrace{\kappa\, I_{\text{mem}} + h\,K}_{\text{holding memory}} \;+\; \underbrace{w\,\mathbb E[\ell_{\mathcal D}]}_{\text{being wrong or late}} \;+\; \underbrace{A(\mathcal D) + L(\mathcal D)}_{\text{acquiring and sharing information}} \qquad \text{subject to}\quad P(\text{ruin}) \le \varepsilon_r .
+$$
+
+- **𝒟**, the design: the number of layers K, what each tracks, how and how often it senses, and what it shares.
+- **κ·I_mem + h·K**: the price κ per nat held per unit time, and the upkeep h of each layer, store or shared level. Inside the class below, these two are not the memory cost. The memory cost there is the heat of the memory's bath, and a constant h is excess above that heat's floor.
+- **w·E[ℓ]**: the stake times the expected loss at the moment of use. Lateness counts as error, because a prediction that arrives after the moment to act buys nothing. The stake w is an input in both displays. kT does not set it.
+- **A(𝒟)**: information-acquisition spend, priced per read (Σ c_k f_k, read price times read rate), per nat acquired (λ), or per unit of precision (c′·r^{−θ}). This summand stays an assumption. For a sensor coupled continuously to its bath, that read is already inside the heat, and a second price on the same nats is not forced (Sagawa and Ueda 2009, the sum of measurement and erasure).
+- **L(𝒟)**: link, telling and lookup costs: κ_b per member–level link, d per member told, u per lookup at use rate μ. This is what puts pooling and sharing inside J. It stays an assumption. A copy that is actually made has a dissipation floor; a design that does not copy does not pay it.
+- **Ruin**: a reserve that starts at buffer B, earns income y and pays J hits zero; ε_r is the tolerated chance. The cap stays outside both displays. It is not a term of the heat.
+- **The world** is exogenous and enters only through its measured pattern of change: its spectrum or Markov kernel, the sensing noise N and the lead k at which actions meet it. The drift level q and spectral slope α are the scale-free special case.
+- **One currency per system** (heat, attention, money, compute). Physics sets floors on the prices (at least kT per nat acquired or erased by a measuring tracker, and kT·(I_mem − I_pred) for memory that does not predict: Landauer 1961, Still et al. 2012), not exchange rates between systems. In each system's own units the equation is the same problem at every scale: only dimensionless ratios matter, and the optimal cost shares are currency-free (CT24); the distance from the floor is one measured number per system. Inside the class below, the memory floor is kT times a learning rate, not a free price κ.
+- **Open lever.** Effort g spent making the world drift less (homeostasis, buffers, contracts) belongs in the problem, but it makes the world depend on the design. Except for the coupled-party results of B.10 (CT29–CT32), the theorems of THEORY hold the outer world fixed at this g = 0. A responding world may be modelled as one more party. A potential theorem applies only when the beta-scaled game is an exact potential. Drift-intensity reduction itself stays open (CL11). T61 and co-adaptation F3/F4 are related and are not the same result.
+
+**Inside one class,** the derived cost is the heat of the memory's bath plus the stake times the decision loss, and the ruin cap is kept outside the sum:
+
+$$
+J_{\mathrm{phys}}=\dot Q+w\,\mathbb E[\ell]\qquad\text{subject to}\quad P(\text{ruin})\le\varepsilon_r .
+$$
+
+The class is an exogenous equilibrium Ornstein–Uhlenbeck signal (the stationary scalar Gauss–Markov diffusion), or independent signals of that kind, or the two-state telegraph. The memory does not move the signal. The loss is the mean squared error of an action of the current memory state, or, on the telegraph, the Hamming mismatch. The rates below are in nats per unit time. At a fixed decision error the heat is at least kT times the learning rate: a(v−ε)/ε for one OU signal, the sum of those rates when each mode is scored on its own, the single level μ with ε = Σ a_k v_k/(a_k+μ) when the loss is the error in the sum, and γ(1−2ε) ln((1−ε)/ε) on the telegraph. A fast linear memory approaches the OU floors at finite heat, in the limit of a diverging rate. A fast memory approaches the telegraph floor in the same kind of limit. On a geometric ladder of equal-variance OU modes the per-mode tracked count is ⌊log(wv/(kT a))/log ρ⌋+1 once the slowest mode pays. On the sum loss, one rank-one memory is the heat-optimal memory. The proofs, the numbers, and the open edge of the class are `theory/INFO_PHYSICS.md`, `theory/INFO_PHYSICS_ATTAINABILITY.md`, `theory/INFO_PHYSICS_GENERAL.md`, and `theory/GENERAL_FORM_PHYSICS_2026-11-22.md`. This paragraph does not re-prove them. Anything the bath pays above that floor is the machine, not a further term.
+
+The five-term equation is assembled from known parts; the repository already wrote it as Axiom 5 of `reviews/night1/formal/AXIOMS.md`. It is the theory's statement of the problem outside the class above, not a theorem. When that form is forced, and when it is not, is `theory/REPRESENTATION.md`: on a product of intervals the cost is additive up to a positive affine transformation, nonnegative prices need the further assumption that each concatenating coordinate is a bad, and a discrete layer count is not part of the cited Debreu theorem. Storing, predicting, acting and staying solvent do not force it. Whether the equation is a limit of growth selection is `theory/GROWTH_BRIDGE.md` (CLAIM_MAP section X). On a gapped finite menu, weak selection recovers the ranking only. The diffusion limit keeps \(\mu-\sigma^2/2\). An interior stake separates the argmaxes. The term list and the cap are inputs. Whether dissipation forces the five terms in every world is `theory/INFO_PHYSICS.md` (CLAIM_MAP section Y, IP5). It does not. Inside the class above, the memory terms κ I_mem and hK are replaced by the heat, the continuous-coupling part of A is inside that heat, and A as a separate summand, L, the cap, and w stay assumptions.
```

**Hunk 2.** These two sentences contradict hunk 1 if hunk 1 is adopted and they are left in place. They are not the hypothesis sentence. Not applied.

In §1, the sentence that begins "The theory adds no physics to the second law." becomes:

> Inside the class in §3, the second law puts the heat of the memory's bath at or above \(kT\) times the learning rate, and a fast memory approaches that floor in the limit. Outside that class, physics enters as a floor under the prices (§3), which above the cell is slack. The theory prices what staying alive takes, and says the price sets the design:

The remainder of that sentence, from "where the world changes on several time scales", stays.

In §2, the sentence that begins "*Physics* supplies the reason upkeep exists" becomes:

> *Physics*, inside the class in §3, bounds the memory-bath heat from below by \(kT\) times the learning rate. A fast memory approaches that floor in the limit of a diverging rate, at finite heat. Outside that class it supplies the reason upkeep exists and a floor under every price (kT per nat, §3); above the cell those floors are slack (§9), so outside that class the claim above is a claim about the economics of judgment.

`CORE.md` is not in this rewrite. Its §1 still states the five-term cost. THEORY governs if the two are ever adopted apart.

## 10. Prior art, as the reviews credited it

Nothing in this list is claimed as new. The DOIs were resolved on Crossref in the reviews named below. This note does not resolve them again.

From the reviews of PR #175 (`reviews/info_physics_2026-11-22/REVIEW.md`, `reviews/info_physics_2026-11-22_round2/REVIEW.md`):

- Landauer 1961, the erasure floor.
- Still, Sivak, Bell, and Crooks 2012, the one-step equality and the protocol inequality for nonpredictive information. A different functional from the housekeeping heat of the continuous-time sensor.
- Sagawa and Ueda 2009, and the 2011 erratum: one floor on the sum of measurement and erasure, not two stacked prices.
- Horowitz and Esposito 2014, equation (11): in steady state the learning subsystem's bath satisfies \(\dot S_r\ge\dot I\).
- Barato and Seifert 2015: the reference sensor is one 4-cycle, affinity \(\ln 64\), inside their unicyclic theorem. Gingrich, Horowitz, Perunov, and England 2016 is the general jump-process theorem, not the first theorem that covers this sensor.
- Barato, Hartich, and Seifert 2014: a conditional-entropy learning rate bounded by the entropy production, and a receptor that learns while the cell's own dissipation is zero because another bath pays.
- Lan, Sartori, Neumann, Sourjik, and Tu 2012: a logarithmic accuracy cost at fixed adaptation speed. Their formula is not the telegraph floor.
- Bo, Del Giudice, and Celani 2015. Crossref lists the families as Bo, Giudice, and Celani. Extra memory about the sensory past, beyond the present reading, is bounded by extra entropy production. They do not derive this telegraph excess or a replacement for the master equation.
- Ouldridge, Govern, and ten Wolde 2017, and Ouldridge and ten Wolde 2017: floors for a copy that is made. Not a linear linking price on every design.

From the review of PR #178 (`reviews/attainability_2026-11-22/REVIEW.md`):

- Duncan 1970, the path mutual information.
- Hartich, Barato, and Seifert 2016: sensory capacity, and efficiency at most \(1/2\) when capacity is \(1\). Their centered family does not reach efficiency \(1\) at a positive learning rate.
- Horowitz and Sandberg 2014, second-law inequalities with an information flow.
- Mitter and Newton 2005: a statistical-mechanical analogy for the Kalman–Bucy filter. Not a lower bound on the bath heat of a physical memory, and not the shrunk spring.
- Sandberg, Delvenne, Newton, and Mitter 2014, equation (46): the implementation cost of a demon that keeps the path is \(2kT\) times the transfer-entropy rate. The Allerton paper, doi 10.1109/ALLERTON.2014.7028503, is the port-Hamiltonian account of that cost. The factor \(2\) is not the infimum of the learning-rate heat.

From the review of PR #180 (`reviews/heat_floor_general_2026-11-22/REVIEW.md`):

- Kalman and Bucy 1961, the linear filter. The scalar content of L1 is already booked as known.
- Kolmogorov 1956 and Sims 2003, the \(\tfrac12\log\) allocation.
- Fox 1966, the marginal count already cited for N64.
- Tanaka, Kim, Parrilo, and Mitter 2017, the discrete-time sequential program in directed information.
- Tanaka, Skoglund, and Ugrinovskii 2017, doi 10.1109/CDC.2017.8264246: the continuous-time vector Duncan minimization under a trace constraint. No bath heat.
- Gorbunov and Pinsker 1973 and 1974: the nonanticipative \(\tfrac12\log\) rate. Crossref returned no work record for either English translation. This note cites them with no DOI.
- Stavrou, Charalambous, Charalambous, Loyka, and Skoglund 2018, doi 10.1109/CDC.2018.8619725: the same shape of rate, on the eigenvalues of a prediction-error covariance.

The combination that is the repository's, and not those papers, is the one the three notes already list: the telegraph closed form; the shrunk spring and the centered spring read at its conditional mean; the reading of \(kT a\) as a scoring gap; the scalar, per-mode, and sum-loss frontiers, including the geometric counts; and the comparison with N65. This proposal adds the map and the unapplied rewrite. It does not add a bound.

## 11. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, or the hypothesis sentence. It does not add a CLAIM_MAP row, and it does not change the status of IP1–IP14, N65, or GF1. It does not run a lake build. It does not recompute the checks; the numbers in §§4–5 are the numbers those notes print (`theory/info_physics_checks/`, 61, 31, and 33 checks, FAILS 0, on the merged heads). It does not treat an in-model theorem as a fact about a real system. No system has been shown to qualify under THEORY §3.
