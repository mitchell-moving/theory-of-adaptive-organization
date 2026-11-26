# Gaining from volatility once the memory acts for a payoff

*Monday 23 November 2026 (America/New_York). Open-work row T50. Written against `main` `c67bc0b` (after PR #238, T49). A follow-up to `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md`, `theory/NON_GAUSSIAN_FLOOR_2026-11-23.md` (T49), and `theory/FEEDBACK_FLOOR_2026-11-23.md` (T61). Not a change to `THEORY.md`, `CORE.md`, or the hypothesis sentence. DOIs below were looked up on the Crossref API the same day (`theory/antifragile_loop_checks/crossref.out`). The check script is `theory/antifragile_loop_checks/antifragile_loop_checks.py` (closed forms, Gauss–Hermite quadratures, exact Gaussian steady states, linear programs, and one seeded Monte Carlo cross-check; not a simulation of a real system). Self-check by the author, then independently reviewed on PR #241 (text, credit, and scope fixes; no result changed).*

Labels follow the repo: **PROVED (in-model)** is a result inside a named class. **KNOWN** is published and credited, only for what that source states. **ELEMENTARY** is a direct consequence of a proved or known inequality, not a new named theorem. **NUMERICAL** is an in-model evaluation by the script. **CONJECTURE** is a named bet. **OPEN** is not derived.

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Bottom line

T49 could not close the loop: its worlds are exogenous and its memory only estimates. Here the memory reads an exogenous world, acts, and is paid by the world: the payoff depends on its action and on the world's state. The cost is memory heat minus the stake times the expected payoff, under a ruin cap. The answer to T50 in this class is conditional. Closing the loop is not what produces a gain from volatility. Owning an option is.

1. **The cost of knowing does not grow with the world's amplitude (Theorem AF-scale, PROVED (in-model)).** Rescale the world, \(X=\mu+\sigma Z\), and read the memory's design in units of \(Z\). The joint distribution of world and memory, the learning rate, and the memory-bath heat are then exactly the same at every \(\sigma\). In this class, physics charges for the fraction of the world learned, not for its size. A sensor whose noise floor is fixed in world units breaks this.
2. **With a payoff convex in the world's state for every action, a design family closed under amplitude, and a slack ruin cap (or bounded downside), the minimized cost never rises with amplitude, and its negative is convex in amplitude (Theorem AF-convex, PROVED (in-model)).** This covers a position sized after reading the memory, an act-or-abstain choice, a stop-loss, and any long option. The optimized value \(V^*=-J^*\) is convex and nondecreasing in \(\sigma\). Taleb and Douady's definition is met both in level and in spread. In the bet class (mean-zero world) it has a closed form, \(V^*=(\sqrt{w\theta/2c}-\sqrt{kTa})_+^2\). It equals the full-information payoff, which is linear in the variance \(\theta\), minus T49's minimized tracking cost, which is concave in \(\theta\). That identity is the join T50 asked for, in this class: the concavity T49 found is what makes the value of acting convex.
3. **With a loss the action pays to stay correct, amplitude hurts (Theorem AF-homeostatic, PROVED (in-model)).** The minimized cost is concave and increasing in \(\sigma^k\) for a degree-\(k\) loss. More amplitude never helps. A spread helps only through redesign per regime, as CT40 and T49 already found. The curvature of the action's payoff in the world's state, convex or concave, is what decides.
4. **Faster churn hurts at fixed amplitude (Theorem AF-rate, PROVED (in-model)).** When the payoff is a flow per unit time, the heat scales with the world's rate \(a\), and the payoff flow does not. So \(V^*\) is convex and nonincreasing in \(a\), and jointly convex in \((\sigma,a)\). In the bet class learning pays only above \(\theta_c=2c\,kTa/w\): the world must move enough per unit of churn. Below that the selected design abstains and keeps its reserve.
5. **A ruin cap on unbounded losses opens a fragile window (Propositions AF-ruin; monotonicity and thresholds PROVED (in-model), window NUMERICAL).** In the bet class the capped value stays nondecreasing in \(\sigma\). To keep earning in proportion to \(\sigma^2\), though, the memory must make sign errors less often than \(\eta\). That takes an error fraction \(r\le\sin^2(\pi\eta)\), a fixed precision premium of \(kTa\cot^2(\pi\eta)\approx kTa/(\pi\eta)^2\) in heat. Coarser designs earn a bounded payoff. When the loss budget is small, a window opens between the two, and there the value is concave in \(\sigma\), so a spread lowers it. With \(B=1\) and \(\eta=0.01\), it is concave on \(\sigma\in[2,7.2]\). Bounded downside (a stop-loss, limited liability) closes the window, and AF-convex applies.
6. **The barbell holds narrowly (Propositions AF-barbell).** A hard cap (\(\eta=0\)) excludes every unbounded-downside action. The cost of judgment is the reason: a perfect record needs infinite heat, so the posterior keeps full support (ELEMENTARY). With a linear stake, the optimum is then reserve plus the whole loss budget on one bounded-downside claim, or reserve alone. That is Taleb's barbell in form (ELEMENTARY, linear programming). Its form comes from the cap and the linear stake, not from the concavity of the cost. If the claims are priced at the prior, the barbell's value does not depend on \(\sigma\) at all (PROVED (in-model)). Above a hard cap, at \(\eta=0.01\), a capped linear position beats the best barbell in 38–92% of memory states. Those are the moderate states, while the barbell keeps the confident ones and most of the value (NUMERICAL). So the pure barbell is the optimum in form only at a hard cap.

So the conjecture in `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md` §3 holds in a named class and not as stated in general. It holds when the selected action keeps an option on the world (a convex payoff, owned rather than bought at a price that scales with volatility), the memory family is closed under the world's amplitude, the stressor is amplitude rather than churn, and the ruin cap is slack or the downside is bounded. It does not hold for pay-to-stay-correct tasks (level), for convexity bought at fair prior prices (neutral), or inside the ruin window (spread). The open miss to diagnose is which side of these lines real selected systems sit on. That is a measurement, not a result of this note.

## 1. The cost, with named terms

The method is the same as everywhere in the theory: write the cost, find its minimum, read off the design. Whether a real system sits near that minimum is Part 2, and is not decided here.

\[
J=\dot Q_M-w\,\mathbb E\bigl[u(\alpha(M),X)\bigr]\qquad\text{subject to}\qquad P\bigl(u(\alpha(M),X)<-B\bigr)\le\eta,\qquad V=-J .
\]

- **World.** \(X_t=\mu+\sigma Z_{at}\), where \(Z\) is a fixed stationary Markov process with mean 0 (diffusion or jump). \(\sigma\) is the amplitude and \(a\) the rate of change. The world is exogenous: the action does not move \(X\) (a price-taker, or a forager on a field it does not deplete). Worlds the action moves are T61's, and that join is **OPEN** here.
- **Memory.** A bipartite memory as in T49 (S2–S4), with transition rates or drift that may depend on the current world state. \(\dot Q_M\) is the memory-bath heat, with \(\dot Q_M\ge kT\,\dot I_M\) (JP-heat and EQ-heat; Horowitz and Esposito 2014).
- **Action and payoff.** The action \(\alpha(M)\) is chosen from a fixed set \(\mathcal A\) after reading the memory. \(u(a,x)\) is the payoff rate of action \(a\) in world state \(x\). The loss is \(\ell=-u\), so with \(u=-(x-a)^2\) this is the tracking cost of CORE §1 and T49.
- **Stake \(w\)** converts payoff into the currency of heat. **Ruin** here is the stationary probability that the instantaneous payoff falls below \(-B\). A ruin event over a whole horizon is a different object and is **OPEN**.
- **Closure assumptions.** (C1) *Amplitude closure:* if a design is allowed, the same design reading \(z=(x-\mu)/\sigma\) is allowed at every \(\sigma\). (C2) *Rate closure:* the design with every memory rate multiplied by \(a\) is allowed. All bipartite memories satisfy both, as does the Gaussian spring family with width proportional to \(\sigma\). A sensor with a noise floor fixed in world units does not satisfy (C1), and that is the setting of CT40.

## 2. Prior art: what each source establishes, and what is new

- **Antifragility as convexity.** Taleb and Douady 2013 define fragility and antifragility as negative or positive sensitivity to a semi-measure of dispersion (a left-tail "vega"). They prove a transfer function that maps this sensitivity to the second derivative of the exposure: concavity gives fragility and convexity gives antifragility. Jensen's inequality is the engine (KNOWN). The level half of AF-convex is that mapping applied to the optimized value \(V^*\); what this note adds is that the heat term does not move with amplitude (AF-scale). That concave or capped exposure with an unbounded left tail is fragile is also their point, and the fragile window of §7 is an in-model instance of it. Scaling up a mean-zero risk is a mean-preserving spread, and every convex payoff gains from one (Rothschild and Stiglitz 1970, KNOWN). Taleb's *Antifragile* (Random House 2012, a book with no DOI) names optionality as the source.
- **Options and real options.** A long option's value rises with volatility (Black and Scholes 1973; Merton 1973). Real-options theory values the right to act after information arrives (McDonald and Siegel 1986; Dixit and Pindyck 1994). A firm that re-optimizes per state gains from price variability (Oi 1961; Hartman 1972; Abel 1984), as CT40 already reads it.
- **Value of information.** Blackwell 1953 orders experiments by informativeness. The value of deciding after an experiment is a convex function of the posterior, which is why a more informative experiment is worth at least as much to every decision maker (KNOWN). AF-convex uses the same convexity, applied to the world's amplitude instead of the posterior. Rational inattention (Sims 2003) already gives, for a quadratic payoff with an information cost in bits, a threshold below which the agent does not learn. AF-bet's threshold \(\theta_c\) has the same shape, with the heat floor \(kTa(\theta/\varepsilon-1)\) in place of an entropy cost.
- **Kelly and ruin.** With fair odds, the growth gained from side information equals the mutual information (Kelly 1956). Growth trades against security (MacLean, Ziemba and Blazenko 1992), and the time average differs from the ensemble average (Peters and Gell-Mann 2016). `theory/DYNAMICS.md` §3–§4 places these against \(J\).
- **Bet-hedging.** Cohen 1966; Seger and Brockmann 1987 (*Oxford Surveys in Evolutionary Biology* 4:182–211; no DOI found on Crossref); Philippi and Seger 1989. Information in fluctuating environments: Kussell and Leibler 2005; Donaldson-Matasci, Bergstrom and Lachmann 2010; Rivoire and Leibler 2011.
- **Thermodynamics of bet-hedging and gambling.** Kobayashi and Sughiyama (2015, 2017) derive fluctuation relations between fitness and information for populations in fluctuating environments, read selection as passive information compression, and derive relations for the fitness gain from sensing in which a multivariate mutual information among phenotype, environment, and signal measures the information relevant to fitness. That is the closest published statement of a value of sensing in a fluctuating world; it is about the information measure, not about amplitude. Vinkler, Permuter and Merhav 2016 map gambling with side information onto measurement-based work extraction. Still, Sivak, Bell and Crooks 2012 tie dissipation to non-predictive information. These are the closest physics. None of them, to this search, states the amplitude-convexity result below.
- **Barbell under tail constraints.** Geman, Geman and Taleb 2015 show a barbell emerging from value-at-risk and maximum-entropy constraints (KNOWN). AF-barbell is a narrower in-model statement inside this cost.
- **Stochastic resonance.** Noise can raise the information a fixed threshold detector passes (Benzi, Sutera and Vulpiani 1981; Gammaitoni et al. 1998). Inside an amplitude-closed design family, injected sensor noise cannot raise \(V^*\): the noisier channel is already in the family. Resonance needs a fixed detector, which breaks (C1). This case is **OPEN** here.

**What is new here, if anything.** The thermodynamic step, the convexity facts, Kelly, and bet-hedging are prior art. The additions are their in-model compositions inside this cost: the amplitude invariance of the memory's heat (AF-scale) combined with convex per-action payoffs (AF-convex); the identity \(V^*=\) full-information payoff minus minimized tracking cost in the bet class; the opposite sign for homeostatic losses; the rate theorem; the ruin precision premium \(kTa\cot^2(\pi\eta)\) and the fragile window; and the barbell statements. The search can miss a paper. This note does not claim that no such composition is in print.

## 3. The cost of knowing is amplitude-free

**Theorem AF-scale (PROVED (in-model)).** Under (C1), let a design be specified by memory rates (or drift and noise) as functions of \((z,m)\). In the world \(X=\mu+\sigma Z\), the joint process \((Z,M)\) has the same distribution for every \((\mu,\sigma)\). Hence the learning rate \(\dot I_M\) and the memory-bath heat \(\dot Q_M\) do not depend on \((\mu,\sigma)\).

*Proof.* The world's dynamics in \(z\) do not depend on \((\mu,\sigma)\), and neither do the memory's rates, by construction. So the generator of \((Z,M)\) is fixed. The memory-bath heat is a functional of the memory's own transitions (jump rates and energy differences, or Stratonovich work for a diffusion memory), and so of the process \((Z,M)\) alone. The learning rate is an information flow between \(M\) and the world. Information is invariant under the bijection \(x\mapsto z\). ∎

Check S1 computes the exact Gaussian steady state of an Ornstein–Uhlenbeck world with a spring memory whose width is proportional to \(\sigma\). At \(\gamma=2,20,2000\) and two widths, heat, learning rate, and error fraction agree across \(\sigma=0.5,1,3,10\) to \(3\times10^{-15}\). Heat is at least \(kT\) times the learning rate, and in the fast limit the heat equals the OU floor \(kTa(\theta/\varepsilon-1)\).

**Read-off.** In this class physics prices the fraction learned, \(r=\varepsilon/\theta\), not the size of the world. The T49 floors confirm this class by class: \(D(1/\varepsilon-\mathcal I)\), \(\sum_sp_sD_s(1/\varepsilon_s-\mathcal I_s)\), and \(\lambda[\tfrac32\ln(v/\varepsilon)-1.27]\) are all unchanged when \(D\), \(v\), and \(\varepsilon\) scale together.

## 4. Payoffs convex in the world: gain in level and in spread

**Theorem AF-convex (PROVED (in-model)).** Assume (C1), a ruin cap that is slack (or no cap), \(\mathbb E|Z|<\infty\), and that \(u(a,\cdot)\) is convex for every \(a\in\mathcal A\), with \(\mathcal A\) fixed. Then for every \(\mu,w,kT\), \(V^*(\sigma)\) is convex and nondecreasing on \(\sigma\ge0\).

*Proof.* Fix a design \(D\) and let \(G_D(\sigma)=\mathbb E\sup_a\mathbb E[u(a,\mu+\sigma Z)\mid M]\), the payoff of the best rule. For each realization, \(\sigma\mapsto u(a,\mu+\sigma z)\) is convex. Conditional expectation, the supremum over \(a\), and the outer expectation all preserve convexity, so \(G_D\) is convex. By conditional Jensen, then Jensen with \(\mathbb E[\mathbb E[Z\mid M]]=0\), \(G_D(\sigma)\ge\mathbb E\sup_au(a,\mu+\sigma\,\mathbb E[Z\mid M])\ge\sup_au(a,\mu)=G_D(0)\). A convex function on \([0,\infty)\) that never drops below its value at 0 is nondecreasing. By AF-scale, \(\dot Q_D\) does not depend on \(\sigma\), so \(V^*=\sup_D[wG_D(\sigma)-\dot Q_D]\) is a supremum of convex nondecreasing functions. ∎

**Corollaries.**
- *Spread, with redesign.* If \(\sigma\) is drawn per regime and the system redesigns in each, \(\mathbb E V^*(\sigma)\ge V^*(\mathbb E\sigma)\). The cost of redesign and T49's switching surcharge are not in \(J\) (**OPEN**). Check S2d uses two regimes \(\sigma\in\{1,3\}\): mean value 0.6287 against 0.1716 at \(\sigma=2\). The calm regime abstains.
- *Which stressor.* Convexity is in the amplitude \(\sigma\), the variable in which the payoff is convex. If \(\mu=0\) and every \(u(a,\cdot)\) is positively homogeneous of degree \(k\), then \(V^*=\sup_D[\sigma^kwG_D(1)-\dot Q_D]\), which is convex in the variance \(\theta=\sigma^2\) when \(k\ge2\). For \(k=1\) it need not be. Check S2b: act-or-abstain (\(u(1,x)=x\), \(u(0,x)=0\)) over the Gaussian spring family is convex in \(\sigma\) and concave in \(\theta\) on \([400,3600]\).
- Check S2c: 12 random menus of convex payoffs \(\alpha x+\beta+\gamma(x-K)_+\) over the Gaussian family. Every \(V^*\) is convex and nondecreasing in \(\sigma\).

**Proposition AF-bet (PROVED (in-model)).** Take a mean-zero OU world (\(\mu=0\)) with variance \(\theta\) and rate \(a\), and a position payoff \(u(b,x)=bx-\tfrac c2b^2\), \(b\in\mathbb R\). Then

\[
V^*(\theta)=\Bigl(\sqrt{\tfrac{w\theta}{2c}}-\sqrt{kTa}\Bigr)_+^2 ,
\]

attained by the fast spring with the Bayes estimate and the position \(b=\mathbb E[X\mid M]/c\), at error fraction \(r^*=\sqrt{2c\,kTa/(w\theta)}\). Below \(\theta_c=2c\,kTa/w\) the selected design does not learn and holds no position. With \(\mu\ne0\), \(V^*\) gains the constant \(w\mu^2/2c\) from acting on the known mean, and the threshold then concerns only the learned part of the position.

*Proof.* The best position gives \(\mathbb E[\mathbb E[X\mid M]^2]/2c=(\theta-\varepsilon)/2c\), where \(\varepsilon\) is the Bayes error. T49 A2 with \(\mathcal I=1/\theta\) and \(D=a\theta\) gives \(\dot Q_M\ge kTa(\theta/\varepsilon-1)\). Maximizing \(w(\theta-\varepsilon)/2c-kTa(\theta/\varepsilon-1)\) over \(\varepsilon\in(0,\theta]\) gives the display. The fast spring attains it (T49 A3; check S1). ∎

**The join.** Write \(\beta=w/2c\). Then \(V^*=\beta\theta-J^*_{\rm track}(\theta)\), with \(J^*_{\rm track}=\min_\varepsilon[kTa(\theta/\varepsilon-1)+\beta\varepsilon]=2\sqrt{kTa\beta\theta}-kTa\), T49's OU minimum at stake \(\beta\) (check S2a). The full-information payoff is linear in \(\theta\), and the minimized cost of judgment is concave in \(\theta\). Their difference is convex. In this class, the concavity T49 found is exactly what makes acting for gain antifragile.

**Design read-off.** Abstain in a calm world. Above \(\theta_c\), learn, and learn a larger fraction as the world grows wilder (\(r^*\propto\theta^{-1/2}\)). Size positions to the estimate. Heat rises with stake and rate, not with amplitude.

## 5. Losses paid to stay correct: amplitude hurts

**Theorem AF-homeostatic (PROVED (in-model)).** Assume (C1), \(\mu=0\), \(u(a,x)=-\ell(x-a)\) with \(\ell\ge0\) convex and positively homogeneous of degree \(k\), and \(\mathcal A=\mathbb R\). Then \(J^*(\sigma)=\inf_D[\dot Q_D+w\sigma^kL_D]\), with \(L_D=\mathbb E\inf_{a'}\mathbb E[\ell(Z-a')\mid M]\ge0\) independent of \(\sigma\). So \(J^*\) is concave and nondecreasing in \(\sigma^k\).

*Proof.* Substitute \(a=\sigma a'\), so \(\ell(\sigma Z-\sigma a')=\sigma^k\ell(Z-a')\), and use AF-scale. An infimum of nondecreasing affine functions of \(\sigma^k\) is concave and nondecreasing. ∎

This is CT40 (a) and (c), and T49 §8.1, in general form. Check S3 covers squared error (\(J^*=2\sqrt{kTaw\theta}-kTa\), concave and increasing in \(\theta\)) and absolute error (concave and increasing in \(\sigma\)). Both payoff classes give a \(V^*\) convex in their natural variable, so both gain from a spread under redesign. Only the convex-payoff class gains from a higher level.

## 6. Amplitude against rate of change

**Theorem AF-rate (PROVED (in-model)).** Assume (C2), and let the payoff be a flow per unit time. Then \(V^*(a)=\sup_D[wG_D-a\,\dot Q_D^{(1)}]\) is convex and nonincreasing in \(a\). With (C1) as well, \(V^*(\sigma,a)\) is jointly convex. If instead the payoff comes once per decorrelation time, so the flow is proportional to \(a\), then \(V^*(a)=a\,V^*(1)\), which is neutral in curvature.

*Proof.* Multiplying every memory rate by \(a\) maps designs for the unit-rate world one to one onto designs for the rate-\(a\) world. The stationary joint distribution is unchanged, and heat and learning rate scale by \(a\). An affine function of \(a\), supremized, is convex. \(wG_D(\sigma)-a\dot Q^{(1)}_D\) is jointly convex in \((\sigma,a)\). ∎

In the bet class, \(V^*=(\sqrt{\beta\theta}-\sqrt{kTa})_+^2\) has, as a function of \((\sigma,a)\), Hessian determinant \(\beta\sqrt{\beta kT}\,a^{-3/2}(\sigma-\sqrt{kTa/\beta})\ge0\) where the memory learns (check S4). **Read-off.** In an OU world the volatility \(D=a\theta\) can rise in two ways. Through amplitude at fixed rate, it helps. Through churn at fixed amplitude, it hurts. Learning pays only while \(\beta\theta>kTa\). How a finite top speed of the memory changes this is **OPEN**. T46 and T61 carry speed only through the Kalman–Bucy gain.

## 7. The ruin cap

Class: the bet class of §4 with the Gaussian spring family (error fraction \(r\)) and a shrunk position \(b=\lambda\,\mathbb E[X\mid M]/c\), \(\lambda\in[0,1]\). Ruin is \(P(U<-B)\le\eta\), with \(U=(\lambda mX-\lambda^2m^2/2)/c\) and \(m=\mathbb E[X\mid M]\). Units in the checks: \(kTa=1\), \(c=w=1\).

**R1. The capped value is nondecreasing in \(\sigma\) (PROVED (in-model)).** If \((r,\lambda)\) is admissible at \(\sigma_1\), then \((r,\lambda\sigma_1^2/\sigma_2^2)\) at \(\sigma_2>\sigma_1\) has, path by path, \(U_{\sigma_2}=\sigma_1^2[\lambda m_1X_1-\lambda^2(\sigma_1^2/\sigma_2^2)m_1^2/2]/c\ge U_{\sigma_1}\), in unit variables. Its heat is the same. So its ruin is no larger and its payoff no smaller. ∎

**R2. The precision premium (PROVED (in-model)).** \(P(mX<0)=\arcsin(\sqrt r)/\pi\), and \(P(U<0)=\arctan(1/k)/\pi\) with \(k=(1-\lambda/2)\sqrt{(1-r)/r}\). Both are the angle between two correlated Gaussians: two jointly Gaussian variables with correlation \(\rho\) disagree in sign with probability \(\arccos(\rho)/\pi\) (Sheppard 1899, KNOWN). Check S5a, Monte Carlo with \(4\times10^5\) draws, deviation at most 0.0016. Since \(U\le\lambda mX/c\), admissibility forces \(\lambda\sigma^2\le Bc/q_r\), where \(q_r>0\) is the root of \(P(m_1X_1<-q)=\eta\). Such a \(q_r\) exists exactly when \(r>\sin^2(\pi\eta)\). So every design coarser than \(r_\eta=\sin^2(\pi\eta)\) earns a gross payoff at most \(B(1-r)/q_r\), whatever \(\sigma\) is (check S5b). Earning in proportion to \(\sigma^2\) requires \(r\le r_\eta\), and so a heat of at least \(kTa\cot^2(\pi\eta)\): 39.9 at \(\eta=0.05\), 1013 at \(\eta=0.01\), in units of \(kTa\).

**R3. The cap is slack again at high volatility (PROVED (in-model)).** For \(\sigma\ge\sigma_{hi}=\sqrt{2c\,kTa/w}\,(1+4\cot^2(\pi\eta))\), the uncapped optimum \((r^*,1)\) has \(k\ge\cot(\pi\eta)\), so \(P(U<-B)\le P(U<0)\le\eta\), and \(V^*_\eta=V^*\). The selected memory learns more as the world grows wilder, and that alone eventually satisfies the cap (check S5c, \(\eta=0.05\)).

**R4. Bounded downside keeps AF-convex (PROVED (in-model)).** If \(u(a,x)\ge-B\) for all \(a,x\), the cap never binds and §4 applies. Check S5e takes a stop-loss payoff \(\max(bx-b^2/2,-0.3)\), which is convex in \(x\), with a fixed action set: \(V^*\) is convex and nondecreasing.

**The fragile window (NUMERICAL).** At \(B=1\), \(\eta=0.01\), the cap binds from the learning threshold on. The selected design shrinks its positions roughly as \(1/\sigma^2\) and its value saturates near 0.05. \(V^*_\eta\) is concave on \(\sigma\in[2,7.2]\). Inside the window a spread loses: the mean of \(V^*_\eta\) at \(\sigma=2\) and \(4\) is below its value at 3 (check S5d). Between \(\sigma=7.6\) and \(7.8\) the design switches to a precise memory with larger positions. That switch is a convex kink, and from there the value grows with \(\sigma^2\). At \(B=4\), the cap binds but \(V^*_\eta\) stays convex on the grid. The window opens when the loss budget is small next to the world's spread at the learning threshold. This is Taleb's fragility in-model: an unbounded downside under a ruin constraint turns convex exposure into a concave response, until the system pays the precision premium.

## 8. The barbell

**BB1. A hard cap excludes unbounded downside (ELEMENTARY).** At \(\eta=0\), an action whose payoff is unbounded below on the posterior's support is inadmissible. Every design of finite heat in the Gaussian family has \(r>0\), since the floor \(kTa(1/r-1)\) diverges as \(r\to0\), so its posterior has full support. T49's core-plus-reserve design has full support by construction. So only bounded-downside actions survive. The cost of judgment enters here: a perfect record would make a linear position safe, and it costs infinite heat.

**BB2. Bang-bang under a linear stake (ELEMENTARY).** Per memory state, suppose a hard cap, a loss budget \(B\), claims \(k\) whose loss is at most their premium \(\pi_k\), and a risk-neutral stake. The problem is a linear program, \(\max\sum_kn_k(\mathbb E[f_k\mid m]-\pi_k)\) subject to \(\sum_kn_k\pi_k\le B\) and \(n\ge0\). Its optimum is a vertex: reserve plus the whole budget on one claim, or reserve alone (check S6a, 200 random programs). That is a barbell in Taleb's form: maximal safety in one part, the full risk budget in the other. Which claim fills the risky end depends on the posterior and the prices, and need not be the most convex one. The form comes from the cap and the linear stake. The concavity of the heat cost plays no part in it. The cost sets only whether to learn and how precisely.

**BB3. Convexity bought at prior prices is amplitude-neutral (PROVED (in-model)).** If every claim's payoff scales with \(\sigma\) (strikes in units of \(\sigma\), as in check S6b) and every claim is priced at its prior expectation, premiums scale with \(\sigma\), and with \(B\) fixed the barbell's value is independent of \(\sigma\) (check S6b: \(\mathbb E V_B=2.13826\) at \(\sigma=0.5,1,2,5\)). AF-convex needs an owned option: a choice made after reading the memory, whose convexity no one charges for at a price that scales with volatility.

**BB4. Above a hard cap the pure barbell is not the optimum, though it carries most of the value (NUMERICAL).** Take a per-decision cap, \(B=0.2\), \(\sigma=1\), and calls and puts priced at the prior. Compare the best barbell (reserve plus claims) with a capped linear position \(nX\), \(|n|\le1\). The first number in each cell is the share of memory states where the linear position wins strictly. The second is the expected value of choosing the better of the two in each state, relative to the pure barbell:

| \(r\) | \(\eta=0\) | \(10^{-4}\) | \(10^{-3}\) | \(10^{-2}\) | \(5\times10^{-2}\) |
|---|---|---|---|---|---|
| 0.5 | 0; 1.000 | 0; 1.000 | 0.20; 1.000 | 0.38; 1.001 | 0.95; 1.085 |
| 0.2 | 0; 1.000 | 0.43; 1.009 | 0.92; 1.053 | 0.92; 1.109 | 0.92; 1.153 |
| 0.05 | 0; 1.000 | 0.92; 1.092 | 0.92; 1.100 | 0.92; 1.108 | 0.92; 1.110 |

The barbell keeps the confident memory states (for \(r\le0.2\) and \(\eta\ge10^{-3}\), \(|m|\) beyond about 1.9 standard deviations), where a claim priced at the prior pays many times its premium. Those states carry most of the expected value. The capped linear position takes most of the moderate states. So above a hard cap the optimum is not a pure barbell in form. In value, the better-of-two design is at most 15.3% above the pure barbell on this grid (three values of \(r\), five of \(\eta\)), and 0.1% above it at \(r=0.5\), \(\eta\le0.01\). Whether a mixed portfolio does better still was not scored (**OPEN**).

**BB5. A barbell of beliefs.** T49's core-plus-reserve memory, \((1-\delta)\mathcal N(x,\sigma^2)+\delta\pi\), is a barbell in belief space: a sharp commitment plus an uncommitted prior share. It comes within \((3.0033+\varepsilon/4v)\lambda\) of the shock-world floor. It is not the unique near-minimizer, since Student-\(t\) channels are also finite. The exact minimizer is **OPEN**.

`theory/DYNAMICS.md` already shows that where the cost-versus-ruin frontier is convex, mixing two extremes gains nothing. **Answer to the barbell question.** The ruin cap plus a reserve gives a barbell at a hard cap with a linear stake. Concavity of the cost does not produce it. Above a hard cap it is not exact in form, though in this class it keeps most of the value.

## 9. The method, explicitly

| Step | In this note |
|---|---|
| Cost, named terms | memory-bath heat \(\dot Q_M\ge kT\dot I_M\); stake \(w\) times payoff \(u(a,x)\); ruin cap \((B,\eta)\) outside the sum |
| Minimum | AF-convex and AF-homeostatic (general shape); AF-bet (closed form); R1–R3 and the window (under the cap) |
| Design read-off | abstain below \(\theta_c\); learn more as the world grows wilder; positions sized to the estimate; under a binding cap, either shrink positions or pay the precision premium \(kTa\cot^2(\pi\eta)\); at a hard cap, reserve plus one bounded-downside claim |
| Scope | exogenous world (action does not move \(X\)); bipartite memory; (C1), (C2); fixed action set; stationary per-instant ruin; Gaussian families where named |
| Measurements | the curvature of the action's payoff in the world state; whether that convexity is owned or priced; amplitude \(\sigma\) and rate \(a\) separately; \(w\), \(kT\), \(B\), \(\eta\); whether the sensor has a noise floor fixed in world units |

## 10. Proved, numerical, open

| Item | Status |
|---|---|
| AF-scale: heat and learning rate amplitude-free under (C1) | PROVED (in-model); check S1 |
| AF-convex: convex payoffs give \(V^*\) convex and nondecreasing in \(\sigma\) | PROVED (in-model); checks S2b–S2d |
| AF-bet closed form, threshold \(\theta_c\), join identity with T49's minimum | PROVED (in-model); check S2a |
| AF-homeostatic: concave nondecreasing cost in \(\sigma^k\) | PROVED (in-model); check S3 |
| AF-rate: convex nonincreasing in \(a\); joint convexity | PROVED (in-model); check S4 |
| R1 monotone under the cap; R2 precision premium; R3 slack above \(\sigma_{hi}\); R4 bounded downside | PROVED (in-model); checks S5a–S5c, S5e |
| Fragile window at \(B=1,\eta=0.01\); convex kink; no window at \(B=4\) | NUMERICAL; check S5d |
| BB1 and BB2 | ELEMENTARY; check S6a |
| BB3 amplitude neutrality of priced convexity | PROVED (in-model); check S6b |
| BB4 share and value table | NUMERICAL; check S6c |
| Worlds the action moves (market impact, depletion): joining T61 | OPEN |
| Redesign cost and switching surcharge in the spread corollary | OPEN |
| A fixed sensor noise floor (no (C1)); stochastic resonance | OPEN |
| Ruin over a horizon; compounding stakes (\(-\mathbb E\ln\)); the fragile window's boundary in closed form | OPEN |
| Infinite-mean worlds (\(\mathbb E\lvert Z\rvert=\infty\)), where AF-convex's level step needs a mean | OPEN |
| Whether any real selected system holds owned convex options in an amplitude-driven world | measurement, not a result |

## 11. Numerical checks

`theory/antifragile_loop_checks/antifragile_loop_checks.py` reports `FAILS 0`. Its stored output is `antifragile_loop_checks.out`. The pytest wrapper `tools/test_antifragile_loop_checks.py` reruns it and compares the output byte for byte. It runs in about 15 s. With `--crossref` it also looks up every DOI below and writes `crossref.out`. It checks that the hypothesis sentence is byte-identical in `THEORY.md` and here, and it screens this note's wording. None of this is a measurement of a real system.

## 12. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, or the hypothesis sentence. It does not add a CLAIM_MAP row. It changes only the T50 row in [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md), a pointer in `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md`, and the index in [`theory/README.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/theory/README.md). It does not treat an in-model statement as a fact about a real system. No system has been shown to qualify under THEORY §3.

## 13. References

- Taleb, N. N. and Douady, R. 2013. Mathematical definition, mapping, and detection of (anti)fragility. *Quantitative Finance* 13:1677–1689. doi 10.1080/14697688.2013.800219.
- Taleb, N. N. 2012. *Antifragile*. Random House. Book, no DOI.
- Geman, D., Geman, H. and Taleb, N. N. 2015. Tail risk constraints and maximum entropy. *Entropy* 17:3724–3737. doi 10.3390/e17063724.
- Rothschild, M. and Stiglitz, J. E. 1970. Increasing risk: I. A definition. *J. Econ. Theory* 2:225–243. doi 10.1016/0022-0531(70)90038-4.
- Sims, C. A. 2003. Implications of rational inattention. *J. Monet. Econ.* 50:665–690. doi 10.1016/S0304-3932(03)00029-1.
- Sheppard, W. F. 1899. On the application of the theory of error to cases of normal distribution and normal correlation. *Phil. Trans. R. Soc. A* 192:101–167. doi 10.1098/rsta.1899.0003.
- Black, F. and Scholes, M. 1973. The pricing of options and corporate liabilities. *J. Polit. Econ.* 81:637–654. doi 10.1086/260062.
- Merton, R. C. 1973. Theory of rational option pricing. *Bell J. Econ. Manag. Sci.* 4:141. doi 10.2307/3003143.
- McDonald, R. and Siegel, D. 1986. The value of waiting to invest. *Q. J. Econ.* doi 10.2307/1884175.
- Dixit, A. K. and Pindyck, R. S. 1994. *Investment under Uncertainty*. Princeton University Press. doi 10.1515/9781400830176.
- Oi, W. Y. 1961. *Econometrica* 29:58. doi 10.2307/1907687. Hartman, R. 1972. *J. Econ. Theory* 5:258. doi 10.1016/0022-0531(72)90105-6. Abel, A. B. 1984. *J. Econ. Dyn. Control* 7:39. doi 10.1016/0165-1889(84)90047-2.
- Blackwell, D. 1953. Equivalent comparisons of experiments. *Ann. Math. Stat.* 24:265–272. doi 10.1214/aoms/1177729032.
- Kelly, J. L. 1956. A new interpretation of information rate. *Bell Syst. Tech. J.* 35:917–926. doi 10.1002/j.1538-7305.1956.tb03809.x.
- MacLean, L. C., Ziemba, W. T. and Blazenko, G. 1992. Growth versus security in dynamic investment analysis. *Manag. Sci.* 38:1562–1585. doi 10.1287/mnsc.38.11.1562.
- Peters, O. and Gell-Mann, M. 2016. Evaluating gambles using dynamics. *Chaos* 26. doi 10.1063/1.4940236.
- Cohen, D. 1966. Optimizing reproduction in a randomly varying environment. *J. Theor. Biol.* 12:119–129. doi 10.1016/0022-5193(66)90188-3.
- Seger, J. and Brockmann, H. J. 1987. What is bet-hedging? *Oxford Surveys in Evolutionary Biology* 4:182–211. No DOI found on Crossref.
- Philippi, T. and Seger, J. 1989. Hedging one's evolutionary bets, revisited. *Trends Ecol. Evol.* 4:41–44. doi 10.1016/0169-5347(89)90138-9.
- Kussell, E. and Leibler, S. 2005. Phenotypic diversity, population growth, and information in fluctuating environments. *Science* 309:2075–2078. doi 10.1126/science.1114383.
- Donaldson-Matasci, M. C., Bergstrom, C. T. and Lachmann, M. 2010. The fitness value of information. *Oikos* 119:219–230. doi 10.1111/j.1600-0706.2009.17781.x.
- Rivoire, O. and Leibler, S. 2011. The value of information for populations in varying environments. *J. Stat. Phys.* 142:1124–1166. doi 10.1007/s10955-011-0166-2.
- Kobayashi, T. J. and Sughiyama, Y. 2015. Fluctuation relations of fitness and information in population dynamics. *Phys. Rev. Lett.* 115. doi 10.1103/PhysRevLett.115.238102.
- Kobayashi, T. J. and Sughiyama, Y. 2017. Stochastic and information-thermodynamic structures of population dynamics in a fluctuating environment. *Phys. Rev. E* 96. doi 10.1103/PhysRevE.96.012402.
- Vinkler, D. A., Permuter, H. H. and Merhav, N. 2016. Analogy between gambling and measurement-based work extraction. *J. Stat. Mech.* 2016:043403. doi 10.1088/1742-5468/2016/04/043403.
- Still, S., Sivak, D. A., Bell, A. J. and Crooks, G. E. 2012. Thermodynamics of prediction. *Phys. Rev. Lett.* 109. doi 10.1103/PhysRevLett.109.120604.
- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with continuous information flow. *Phys. Rev. X* 4. doi 10.1103/PhysRevX.4.031015.
- Benzi, R., Sutera, A. and Vulpiani, A. 1981. The mechanism of stochastic resonance. *J. Phys. A* 14:L453–L457. doi 10.1088/0305-4470/14/11/006.
- Gammaitoni, L., Hänggi, P., Jung, P. and Marchesoni, F. 1998. Stochastic resonance. *Rev. Mod. Phys.* 70:223–287. doi 10.1103/RevModPhys.70.223.

Already in the repository and used rather than re-derived: CT40 (`theory/ROBUSTNESS.md` §6); `theory/DYNAMICS.md` §3–§4 (bet-hedging, time average, barbell as randomization); T49 A2, A3, A5, B4, C3, C5 (`theory/NON_GAUSSIAN_FLOOR_2026-11-23.md`); T61 (`theory/FEEDBACK_FLOOR_2026-11-23.md`); JP-heat and EQ-heat (`theory/GENERALITY_2026-11-22.md`).
