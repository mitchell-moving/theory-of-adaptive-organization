# Acting memory: probes, capped losses, and volatility

*Sunday 22 November 2026. Draft. A self-check, not an independent review. The hypothesis sentence is unchanged. `THEORY.md`, `CORE.md`, and `README.md` are not edited. T43 is the antifragility turnover draft, PR #191, and T44 is the boundary draft, PR #194. This note's open-work row is T45. The locked preregistration names only the reservation of T43. The preregistration is `theory/acting_memory_checks/PREREG.md`, commit `0f452d5`, sha256 `bdf86e0379297c84f59856261419e66286c8c3b3f48ce24e8e22fd7812ddd4b8`, locked by `e95b6be` before this computation (rebased onto `b6e351e` from pre-rebase branch ids 06976862, authored and committed 20:55:49Z, and 4d74bd52, authored and committed 20:55:53Z). The `PREREG.md` sha256 is unchanged, and the author-timestamp order is unchanged. Checks: `theory/acting_memory_checks/acting_checks.py`, run at `nice -n 19` (54 checks, FAILS 0, one locked grid clause recorded as a miss). DOIs resolved on the Crossref API on 22 November 2026 are in `theory/acting_memory_checks/crossref.out`.*

Labels: **PROVED** (the argument is on this page, in the class named with it, and the arithmetic is in the checks), **PROVED (in-model)** (the same, at the frozen point the checks recompute), **KNOWN** (published, fetched this session or already in this repository, and only for what that source states), **MISSES** (a locked sentence the evaluation contradicts, with the numbers and a diagnosis), **CONJECTURE** (named, not run), **METAPHOR** (the name adds no comparison the cost does not already make), **OPEN** (outside this class).

## 0. The answer

The scored action is an open-loop intensity. The world equation contains no action.

The choice of \(\alpha=(4-\pi)/(6\pi)\) builds the critical point at \(r^*=1/2\) and \(\theta=1\). The admissible cost there is \(5.182159696490\), and the envelope slope is
\[
\frac{\mathrm d J^*}{\mathrm d\theta}=-\frac{A(r^*)}{\theta^2}=-0.182159696490.
\]
Along the minimizing path the split is probe \(-0.130861161564\), heat \(+0.187741986525\), and sign \(-0.239040521451\). The drop in level comes from the probe price of a fraction falling as \(1/\theta\). The number \(2/3\) is the heat slope at fixed intensity \(u=4\). One decision loses \(16\) with probability \(1/4\), and \(P(\mathrm{loss}>16)=0\).

The second derivative \(0.313020858054\) and the spread penalty \(0.001577268119\) are the variability score. This point fails that score: a random spread of the variance hurts. On the repository's reading of Taleb and Douady, a concave cost would gain from that spread. This cost is convex in \(\theta\).

Two routes lower a cost as \(\theta\) rises, and they have different bookkeeping. One is a shrinking price for a loss that depends on \(\theta\) only through the error fraction \(r\). The other is a capped premium on an expectation that grows with \(\sqrt{\theta}\), with no channel. A mean-square loss, and a payment that does not measure the world, keep a nonnegative slope.

The comparison of \(J^*(8)=4.998066177768\) with \(5\) remains an open miss. The diagnosis is in §4. The preregistration is not edited.

## 1. Already in the repository

None of the following is a result of this note.

- The heat floor. For an exogenous equilibrium Ornstein–Uhlenbeck signal the learning rate of a Gaussian conditional with variance \(p\) is \(L=a(\theta/p-1)\), and the memory-bath heat is at least \(kT\,L\) (`theory/INFO_PHYSICS_ATTAINABILITY.md`). The shape is Horowitz and Esposito. This note charges the floor and does not re-prove it. Attainment by a finite-rate spring is proved in that note for a mean-squared decision loss. It is not proved here for the sign loss. A gap above the floor that grew with \(\theta\) could reverse the level drop. That case is **OPEN**.
- Variation. `theory/ROBUSTNESS.md` §6 reads Taleb and Douady as: the payoff is antifragile to a stressor when it is convex in the stressor, and the cost is then concave in the stressor. In their fixed-design linear-Gaussian model the best cost is concave and nondecreasing in the variance scale (R4(a), CT40). This note keeps that reading and asks a different question: whether the level of \(\theta\) can lower the cost once the action chooses the channel.
- PR #191 is on `main` at `40232f6`. It reports an interior minimum for identical units through realignment, and it reports that the heterogeneous arm minimizes at no shock. This note does not rescore it. Section 5 records the conditional-independence reason a failure time that ignores \(X\) adds nothing about \(X\).

The world in this note stays exogenous. The action chooses the observation channel and pays for it. A memory that changes the drift of \(X\) is the open front already named as CX2. It is not scored.

## 2. Assumptions

The class is AM in the preregistration. The assumptions used below are these.

**AM-X.** \(dX=-aX\,dt+\sqrt{2a\theta}\,dW\), \(a>0\), \(\theta>0\). No action enters this equation.

**AM-Y.** For intensity \(u>0\), \(dY=X\,dt+u^{-1/2}\,dV\), with \(V\) independent of \(W\). At \(u=0\) there is no observation and the error is the prior variance \(\theta\).

**AM-H.** The heat charged is \(kT\,L\), with \(L\) the learning rate of the Gaussian conditional. This is the floor, not a measured bath.

**AM-S.** The decision is the sign of the conditional mean. One decision loses \(0\) or \(w\).

**AM-Q.** The decision loss rate is \(w\) times the posterior variance.

**AM-C.** The probe price is \(\alpha u\), deterministic.

**AM-U.** The probe price is \(\alpha u\,\theta\).

**AM-N.** The noise density is \(\theta/u\).

**AM-0.** The agent pays \(\alpha u\) and the conditional stays at the prior.

**AM-O.** No channel. The payoff is \(\max(X,0)\), premium \(c\) independent of \(\theta\).

Ruin is one decision's gross loss exceeding a reserve \(B\). It is a constraint. The frozen point is \(a=kT=1\), \(w=16\), \(\theta=1\), \(\alpha=(4-\pi)/(6\pi)\), \(B=16\), \(\varepsilon_r=1/20\), \(c=1\).

In the master equation the heat stands where the memory term stands, the probe price stands where the read term stands, and the loss rate is the stake term. Layer upkeep and the link term are zero in this scalar class. That placement is this note's. It does not edit the equation in THEORY.

## 3. The channel

**Proposition AM-riccati (PROVED, under AM-X and AM-Y).** The steady posterior variance \(p\) solves \(u p^2+2ap-2a\theta=0\) for \(u>0\), so
\[
p=\frac{-a+\sqrt{a^2+2a\theta u}}{u},\qquad
u=\frac{2a(1-r)}{\theta r^2},\quad r=\frac{p}{\theta}\in(0,1).
\]
The learning rate is \(L=a(1-r)/r=up/2\), and
\[
\frac{\partial L}{\partial u}=\frac{a\theta}{2\sqrt{a^2+2a\theta u}}>0.
\]
At the frozen point this derivative equals \(1/6\). The equation for \(p\) does not involve the path of \(Y\). Given \(u\), the error variance is deterministic.

*Proof.* The Kalman–Bucy variance of this pair is the scalar Riccati with process-noise intensity \(2a\theta\) and observation-noise density \(1/u\). The quadratic formula is the positive root below \(\theta\). Differentiating \(L=(-a+\sqrt{a^2+2a\theta u})/2\) gives the displayed partial. The checks recompute the residual \(0\) at \(u=4\), \(p=1/2\), and the partial \(1/6\). ∎

Choosing a larger intensity strictly raises the learning rate. That is the sense in which the action decides the observation. Because \(p\) does not depend on the realized path, the optimal intensity on this channel is open-loop. A control whose probing value depends on the current posterior needs a channel the Riccati does not cover. Bar-Shalom and Tse, fetched, title a dual effect of that broader kind. No abstract was in the Crossref record. Their separation theorem is not restated. Calling this open-loop intensity a dual effect is **METAPHOR**.

**Sign error (PROVED, under AM-S).** The conditional mean \(m\) is Gaussian, \(\mathbb{E}[m^2]=\theta-p\), and \(\mathbb{E}[(X-m)\mid m]=0\), so \(\mathrm{Corr}(X,m)=\sqrt{1-r}\). For a centered Gaussian pair of correlation \(\rho\), opposite signs occupy the angle \(\arccos\rho\), and
\[
\psi(r)=\frac{1}{\pi}\arccos\sqrt{1-r}.
\]
At \(r=1/2\), \(\psi=1/4\). The derivative is \(\psi'(r)=1/(2\pi\sqrt{r(1-r)})\). The checks match that derivative by a finite difference.

## 4. The frozen point, and the shape

**Proposition AM-point (PROVED (in-model), under AM-X, AM-Y, AM-H, AM-S, AM-C).** With the capped price,
\[
J(r,\theta)=\alpha\cdot\frac{2a(1-r)}{\theta r^2}+kT\,a\frac{1-r}{r}+w\,\psi(r).
\]
The price \(\alpha=(4-\pi)/(6\pi)\) is the unique value that puts a critical point at \(r=1/2\) when \(\theta=1\). That critical point is a strict local minimum: \(\partial_r^2 J=160\alpha+16>0\). The intensity is \(u=4\), the heat is \(1\), the sign loss is \(4\), and
\[
J\Bigl(\tfrac12,1\Bigr)=5+\frac{2(4-\pi)}{3\pi}=5.182159696490.
\]
The blind cost is \(8\). Write \(A(r)=\alpha\cdot 2a(1-r)/r^2\) for the probe price of holding the fraction \(r\), and write \(J=A(r)/\theta+C(r)\), with \(C\) the heat plus the sign loss. At an interior minimum the envelope theorem gives
\[
\frac{\mathrm d J^*}{\mathrm d\theta}=-\frac{A(r^*)}{\theta^2}.
\]
At this critical point that slope equals \(2/3-8/(3\pi)=-0.182159696490\). The sum \(2/3-8/(3\pi)\) is the derivative at fixed intensity \(u=4\): \(2/3\) is the heat slope on that fixed-intensity path, and \(-8/(3\pi)\) is the sign slope on the same path. Along the minimizing path, \(r\) moves. At \(\theta=1\) the three pieces are probe \(-0.130861161564\), heat \(+0.187741986525\), and sign \(-0.239040521451\). Their sum is the envelope slope. The drop in level is the probe price of a fraction falling as \(1/\theta\): a larger signal against noise that stays put makes a given fraction cheaper to hold.

*Proof.* The algebra of the critical point is the locked §4 of the preregistration. The checks recompute the first-order residual as \(0\), the cost, the fixed-intensity slope, and a minimizer at \(r=1/2\). A finite difference of the minimized cost matches that slope. The along-path split differentiates \(A(r)/\theta\), the heat, and \(w\psi(r)\) through \(r^*(\theta)\) at the same point. ∎

The operating point is admissible on the strict exceedance. \(P(\mathrm{loss}=16)=1/4\) and \(P(\mathrm{loss}>16)=0\), and \(0\) is within \(1/20\).

**Proposition AM-decrease (PROVED, under the same hypotheses, \(\alpha>0\)).** \(J^*(\theta)=\min_{r\in(0,1)}J(r,\theta)\) is strictly decreasing on \((0,\infty)\), lies strictly below \(8\), and converges to \(\inf_r C(r)\) as \(\theta\to\infty\), where \(C\) is the heat plus the sign loss. It converges to \(8\) from below as \(\theta\to 0\).

*Proof.* For each fixed \(r\in(0,1)\), \(\partial J/\partial\theta=-A(r)/\theta^2<0\) with \(A(r)=\alpha\cdot 2a(1-r)/r^2>0\). As \(r\to 0\), \(J\to\infty\). As \(r=1-\varepsilon\) with \(\varepsilon\downarrow 0\), the gap below \(w/2\) is \(-w\sqrt{\varepsilon}/\pi\) plus terms of order \(\varepsilon\), so some \(r\) undercuts the blind cost at every \(\theta>0\). A minimum is attained. For \(\theta_2>\theta_1\),
\[
J^*(\theta_2)\le J(r^*(\theta_1),\theta_2)<J(r^*(\theta_1),\theta_1)=J^*(\theta_1).
\]
\(C(1/2)=5\), so the floor is at most \(5\). The diagnostic minimization of \(C\) in the checks sits at \(r=0.441594095399\), value \(4.966383544211\). That diagnostic is not a locked score. ∎

**Proposition AM-not-concave (PROVED).** A cost that is strictly decreasing and bounded below on a right half-line is not concave on that half-line. \(J^*\) is not variation-antifragile on any \((\theta_1,\infty)\).

*Proof.* Suppose it were concave on \((\theta_1,\infty)\). The difference quotient from \(\theta_1\) to any \(s>\theta_1\) equals some \(\delta<0\). Concavity pushes later quotients down, so \(J^*(t)\le J^*(s)+\delta(t-s)\) for \(t>s\), which runs to \(-\infty\). The floor forbids that. ∎

**Proposition AM-convex-here (PROVED (in-model)).** At \(\theta=1\),
\[
\frac{\mathrm d^2 J^*}{\mathrm d\theta^2}=8\alpha-\frac{(16/\pi-4)^2}{160\alpha+16}=0.313020858054>0.
\]
The sign reduces to \(44+\pi>0\). The fixed-fraction spread at half-width \(1/10\) equals \(A\delta^2/(1-\delta^2)=0.001839996934\). The re-optimized spread at the same width is \(0.001577268119\). The second derivative and that spread penalty are the variability score. A random spread of the variance hurts. On the repository's reading in `theory/ROBUSTNESS.md` §6, a cost gains from such a spread when the cost is concave in the stressor. This cost is convex at the point.

The minimized cost on the locked grid:

| \(\theta\) | \(r^*\) | \(J^*\) |
|---|---|---|
| \(1/8\) | \(0.671238475860\) | \(5.911577251205\) |
| \(1/4\) | \(0.597650549677\) | \(5.584150440609\) |
| \(1/2\) | \(0.540374322719\) | \(5.343143969081\) |
| \(1\) | \(1/2\) | \(5.182159696490\) |
| \(2\) | \(0.474155421441\) | \(5.083843454099\) |
| \(4\) | \(0.458964128271\) | \(5.028073368003\) |
| \(8\) | \(0.450597167920\) | \(4.998066177768\) |

The column \(J^*\) is strictly decreasing and strictly below \(8\).

**The grid clause against \(5\). MISSES.** The preregistration predicted that the rightmost value would sit strictly above \(5\). It is \(4.998066177768\), short by \(0.001933822232\). The diagnosis stands. \(C(1/2)=5\) is the heat plus the sign loss at the frozen fraction, so it is an upper bound on the floor \(\inf C\). The diagnostic minimum of \(C\) is \(4.966383544211\) at \(r=0.441594095399\). \(J^*\) crosses \(5\) near \(\theta=7.5267\). Re-optimizing \(r\) as \(A(r)/\theta\) shrinks pulls the cost toward that floor, and by \(\theta=8\) the pull has crossed \(5\). The slope, the decrease, and the convexity statements do not use this comparison. The preregistration stays as locked. A later lock that scored the grid against \(\inf C\) would be a new file.

## 5. Where the hypothesis misses, and where the controls hold

The hypothesis said that a level drop arises exactly when the probe cost is capped and the probe measures the world, and that the cost is then concave. The scored reading is the one locked in the preregistration's §6.

**Squared loss, capped price, informative channel (PROVED).** At fixed intensity,
\[
\frac{\partial J}{\partial\theta}=\Bigl(w+\frac{kT\,u}{2}\Bigr)\frac{a}{a+up}>0.
\]
At \(u=0\) the cost is \(w\theta\) and the derivative is \(w\). On the admissible set the posterior variance is at most \(p_{\mathrm{cap}}=0.260317771627\). The two thresholds are the same cap. With \(z_\Phi=\Phi^{-1}(0.975)=1.959963984540\),
\[
p_{\mathrm{cap}}=\frac{B}{w z_\Phi^2}.
\]
The script's root is \(\mathrm{erfcinv}(1/20)=1.385903824350\), equal to \(z_\Phi/\sqrt{2}\), and \(B/(w\cdot 2 z^2)\) is the same number. Where the unconstrained minimizer lies above that cap, the minimum sits on the cap and the slope is \(\alpha\cdot 2a/p_{\mathrm{cap}}^2+kT\,a/p_{\mathrm{cap}}>0\). The admissible squared cost on \(\theta\in\{1/2,1,2,4\}\) is \(5.316961792302\), \(8.000711319618\), \(13.186217779633\), \(23.557230699662\), strictly increasing. At the sign point \((u,p)=(4,1/2)\) the squared ruin probability stays \(\mathrm{erfc}(1)=0.157299207050>1/20\), so that point is not the admissible comparison. The admissible squared cost rises with volatility. A capped probe price and an informative channel, together, leave this mean-square cost increasing.

**Uninformative payment (PROVED, AM-0).** The sign cost is \(\alpha u+8\), minimized at \(u=0\) with value \(8\), and that value does not depend on \(\theta\). The squared cost is minimized at \(u=0\) with slope \(w=16\). A payment that does not measure \(X\) does not produce a level drop.

**Failure time independent of \(X\) (PROVED).** If the failure time is independent of \(X\) given the part's quality, the conditional law of \(X\) given the failure and the quality equals the conditional law given the quality. The failure adds no information about \(X\). This is the uninformative arm. It is the reading this note gives of a failure rate that depends on quality and not on the world. PR #191 is on `main` at `40232f6`. Its heterogeneous numbers are that merge's report. This note does not rescore it.

**Uncapped probe price (PROVED, AM-U).** The product \(\alpha u\theta\) with \(u=2a(1-r)/(\theta r^2)\) equals \(\alpha\cdot 2a(1-r)/r^2\). That product removes the \(1/\theta\) scaling of the price of a fraction. Heat and sign loss depend on \(\theta\) only through \(r\). The minimized cost does not depend on \(\theta\). At the frozen \(\alpha\) the stationary point is again \(r=1/2\), and the constant cost equals \(5.182159696490\).

**Noise that scales with the variance (PROVED, AM-N).** With noise density \(\theta/u\), the intensity that holds a fraction \(r\) is \(u=2a(1-r)/r^2\), with no \(\theta\) left. This route also removes the \(1/\theta\) scaling: the intensity a fraction requires no longer falls as the signal grows. The checks confirm the Riccati fraction at \(\theta=1\) and at \(\theta=3\). The learning rate at the minimizer does not move with \(\theta\), because the minimizing fraction does not move. At the frozen \(\alpha\) that minimizer is \(r=1/2\) and the cost is the same constant \(5.182159696490\). The uncapped price and the scaled noise are different mechanisms. In this parameterization they leave the same function of \(r\). On the fixed-noise arm the learning rate rises because \(r^*\) falls as the probe becomes cheaper. That rise is the comparative static of the \(1/\theta\) scaling.

**Passive sign channel (PROVED (in-model)).** At fixed \(u=4\) the slope equals \(-0.182159696490\) at \(\theta=1\). At the same fixed intensity and \(\theta=4\), the fraction is \(0.296535165409\), the learning rate is \(2.372281323269\), and the slope is \(+0.177466031352\). The learning rate is higher than its value \(1\) at \(\theta=1\), and the cost slope is positive, because the heat grows like \(\sqrt{\theta}\) while the sign saving is bounded. Re-optimizing the intensity keeps \(J^*\) decreasing: the optimal intensity falls as \(1/\theta\) once the fraction has settled. Passive squared loss stays increasing, by the envelope above.

**Naked option (PROVED, AM-O).** \(\mathbb{E}[\max(X,0)]=\sqrt{\theta/(2\pi)}\) for \(X\sim\mathcal N(0,\theta)\). The cost \(1-\sqrt{\theta/(2\pi)}\) has slope \(-1/(2\sqrt{2\pi\theta})\), equal to \(-0.199471140201\) at \(\theta=1\) and still negative at \(\theta=4\). There is no channel and no heat. A capped premium and a payoff that is convex in \(X\) are enough for a level drop. Clause (b) is not necessary for every level drop.

**Optionality.** The sign bet has a loss in \(\{0,w\}\). The downside is capped, and so is the upside: the saving against a blind guess cannot exceed \(w/2\). The naked option has a capped premium and an expectation that grows like \(\sqrt{\theta}\), with no finite ceiling. That is the open upside. Its expected cost is convex in \(\theta\), because the second derivative of \(-\sqrt{\theta}\) is positive, so on the repository's reading it is fragile to a spread of \(\theta\) while it gains from the level of \(\theta\). Convexity of \(\max(X,0)\) in the shock \(X\) is a third statement. Taleb and Douady, fetched, title a mathematical definition of antifragility. No abstract was in the Crossref record. The concave-cost reading used here is the one already in `theory/ROBUSTNESS.md` §6. The financial name, applied to the sign bet, is **METAPHOR**: the sign bet does not have the open upside the option has.

**Two routes.** The measurement route is the envelope identity. Fixed observation noise, a probe price that is not proportional to \(\theta\), and a loss that at fixed \(r\) depends on \(\theta\) only through \(r\): the price of that fraction falls as \(1/\theta\), and that fall is \(\mathrm d J^*/\mathrm d\theta\). The option route is separate. A capped premium buys \(\mathbb{E}[\max(X,0)]\), which grows with \(\sqrt{\theta}\), and there is no channel and no heat. The comparison of \(J^*(8)\) with \(5\) stays an open miss. \(C(1/2)=5\) is an upper bound on the floor, \(\inf C=4.966383544211\), and the crossing is near \(\theta=7.5267\). The diagnosis in §4 stands.

## 6. What the literatures state, and what this page does not borrow

Fetched this session. Crossref HTTP 200 for each DOI. An abstract is quoted only to the extent printed below; a record with no abstract is cited for the title.

- Horowitz and Esposito, title fetched, doi 10.1103/PhysRevX.4.031015. **KNOWN** as the source of the shape already used in this repository. Not re-proved.
- Taleb and Douady, title fetched, doi 10.1080/14697688.2013.800219. **KNOWN** as the paper whose title names a mathematical definition. The stressor in this note is \(\theta\).
- Friston, FitzGerald, Rigoli, Schwartenbeck, and Pezzulo, abstract fetched, doi 10.1162/NECO_a_00912. The abstract splits the claim: action selection explained as minimizing variational free energy, with neuronal responses posed as a gradient descent on that free energy. **KNOWN** for that split. This note minimizes heat, probe price, and the sign loss. It does not minimize a free energy, and it does not identify the intensity with their gradient.
- Russo and Van Roy, abstract fetched, doi 10.1287/opre.2017.1663. The abstract says each action is sampled to minimize the ratio of squared expected single-period regret to the mutual information between the optimal action and the next observation. **KNOWN** for that criterion. The intensity here is a static price, not that ratio.
- Chaloner and Verdinelli, abstract fetched, doi 10.1214/ss/1177009939. The abstract presents experimental design as one decision problem. **KNOWN** for that framing. MacKay, abstract fetched, doi 10.1162/neco.1992.4.4.590, discusses objective functions that measure the expected informativeness of candidate measurements. **KNOWN** for that sentence. Lindley, title fetched, doi 10.1214/aoms/1177728069, no abstract in the record. Cited for the title. The derivative \(\partial L/\partial u>0\) is this channel's version of a measurement whose information depends on the action taken. It is not their utility function.
- Bar-Shalom and Tse, title fetched, doi 10.1109/TAC.1974.1100635. No abstract in the record. Cited for the title, in §3, and not for a theorem.

## 7. What is open

A failure intensity that depends on \(X\), a Cox clock, is the case in which a part's failure is itself the measurement. It is not scored. **OPEN.** A finite-rate spring whose heat sits above \(kT\,L\) by a gap that may grow with \(\theta\) is **OPEN**; every scored cost charges the floor. A probe that changes the drift of \(X\) is CX2 and is **OPEN**. A posterior-dependent probe on a nonlinear channel is **OPEN**; on this linear channel the optimal intensity is open-loop.

The next lock, if one is written, would be a new preregistration. It would freeze a Cox intensity and a finite-rate excess, and it would score the grid against \(\inf C\) rather than against \(C(1/2)\). It would not edit this file's preregistration.

## 8. Checks

`theory/acting_memory_checks/acting_checks.py`. 54 checks, FAILS 0. The prediction miss is printed as `PREDICTION-MISS`. The open miss is §4 and §5. The locked numbers are the numbers the script prints. The along-path split and the crossing are the derivatives of those closed forms.

## 9. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, `README.md`, or the hypothesis sentence. It does not adopt the heat floor into the master equation. It does not merge draft PR #191, and it does not rescore it. It does not call a self-check an independent review.
