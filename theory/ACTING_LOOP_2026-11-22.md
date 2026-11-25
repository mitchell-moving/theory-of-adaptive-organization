# The predict-act-correct loop

*Sunday 22 November 2026. Draft. A self-check, not an independent review. The hypothesis sentence is unchanged. `THEORY.md`, `CORE.md`, and `README.md` are not edited. The master equation is not edited. The acting-memory preregistration is not edited. T45 is that note. This note's open-work row is T46. The preregistration is `theory/acting_loop_checks/PREREG.md`, commit `774e88f`, sha256 `fdf494e9b7f85ca24d9d877ea1610cbaf539dc50127a45106285165b925259a0`, locked by `d77f448` before this computation. Checks: `theory/acting_loop_checks/acting_loop_checks.py`, run at `nice -n 19`. 36 checks, FAILS 0. The 33 lines in §5 of the preregistration evaluate the expressions in §4 of that file, or restate a sign §4 already gives. The preregistration says the decimals are the values of those expressions and that a later script may only evaluate them. The lock is six seconds after the commit that contains the decimals. Misses 0 is agreement with that arithmetic. This run contained no prediction that could miss. DOIs resolved on the Crossref API on 22 November 2026 are in `theory/acting_loop_checks/crossref.out`. 23 November 2026: §8 now points to `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md`; CORE §4 and README item 5 carry that reading.*

Labels: **PROVED** (the argument is on this page, in the class named with it, and the arithmetic is in the checks), **PROVED (in-model)** (the same, at the frozen point), **KNOWN** (published, fetched this session, and only for what that source states), **CONJECTURE** (named, not proved), **METAPHOR** (the name adds no comparison the cost does not already make).

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. The answer

Closed-loop acting is strictly cheaper than sensing alone when the channel is not priced, by
\[
\Delta_{\mathrm{full}}(\theta,a)=(q-2aP(a))\,\theta,
\]
with \(P(a)=-a+\sqrt{a^2+q}\) at unit control price and unit action gain. At stake \(q=1\) the factor is \(0.171572875254\) at \(a=1\), \(0.381966011250\) at \(a=1/2\), and \(0.055728090001\) at \(a=2\).

With the heat floor and the probe price charged, the gap at fraction \(r\) is
\[
\Delta(\theta,a,r)=(1-r)\Bigl[(q-2aP(a))\,\theta-\frac{a}{r}-\frac{2\alpha a}{\theta r^2}\Bigr].
\]
At \(q=a=\theta=1\) this gap is negative at every \(r\in(0,1)\). At \(r=1/2\) it equals \(-1.096373258863\): the closed loop is dearer by that amount. At stake \(q=4\) the minimizing fraction is \(0.856768708291\) and the gap is \(+0.033889928154\).

Feedback shrinks the mutual-information stock \(\tfrac12\log(v/p)\). The learning-rate heat stays fixed. The separated gain does not depend on the error variance. A tight variance cap, and a capped loss, each move that gain. At stake \(1\) the minimum is the blind cost \(q\theta\), whose second derivative is \(0\). The second derivative \(-0.321714500038\) is the closed-loop cost at fixed intensity \(u_o=4\), and that design costs more than doing nothing.

## 1. The class

**AL-X.** \(dX=-aX\,dt+b u_a\,dt+\sqrt{2a\theta}\,dW\). At \(b=0\) the world is the exogenous signal of the acting-memory note.

**AL-Y.** \(dY=X\,dt+u_o^{-1/2}\,dV\). The error variance \(p\) solves the Riccati \(u_o p^2+2ap-2a\theta=0\). The action cancels in the error equation.

**AL-K.** \(u_a=-Km\). The state variance is \(v=p+a(\theta-p)/(a+bK)\). The learning rate \(L=a(\theta/p-1)\) does not depend on \(K\).

The scored regulation cost is heat plus the probe price plus \(q v+\rho K^2 s\), with \(s=v-p\). The heat is \(kT\,L\), plus \(\gamma_1\theta\), or, when the finite-rate spring is charged, the Sekimoto heat \(Q_{\mathrm{fin}}\) in place of \(kT\,L\). At the frozen point \(L=1\), so the Sekimoto heat and the ratio of that heat to \(kT\,L\) are both \(10/9\). Those two numbers come apart as soon as \(L\neq 1\). AL-H's word "plus" has the wrong relation to that proposition and stays in the locked file. The checks charge \(kT\,L\) and report \(Q_{\mathrm{fin}}\) beside it. Ruin is a constraint. The frozen point is \(a=b=\rho=kT=\theta=1\), \(\alpha=(4-\pi)/(6\pi)\), \(B=16\), \(\varepsilon_r=1/20\).

In the master equation the heat stands where the memory term stands, the probe price where the read term stands, and the actuation price where effort on the drift stands. Layer upkeep and the link term are zero. That placement is this note's. The reduction at \(b=0\) is the proposal `theory/MASTER_EQUATION_ACTING_PROPOSAL_2026-11-22.md`. It does not edit the equation.

Three arms, one regulation cost. Action alone is a constant \(u_a\) and no observation. Observation alone is \(K=0\). Both together is the separated gain and \(u_o>0\).

## 2. Which arm is cheaper

**Proposition AL-arms (PROVED, under AL-X, AL-Y, AL-R).** For a zero-mean state, a constant action does not cut the variance, and an observation that is not acted on does not either. Both of those arms minimize at doing nothing, with cost \(q\theta\). They are equal.

**Proposition AL-full (PROVED).** With the state observed and the channel not priced, the gap against that common cost is \(\Delta_{\mathrm{full}}(\theta,a)\) above. It is strictly positive for \(q>0\), \(\theta>0\), \(a>0\). The three factors in §0 are that expression at \(q=1\).

**Proposition AL-priced (PROVED (in-model)).** With the floor and the probe price, \(\Delta(\theta,a,r)\) is the gap. At stake \(1\) and \((a,\theta)=(1,1)\) the bracket decreases as \(r\) falls, and its limit at \(r\to 1\) equals \(3-2\sqrt{2}-1-2\alpha<0\). No closed loop is cheaper. The direct cost at \(r=1/2\) exceeds \(q\theta\) by \(1.096373258863\). At stake \(4\) the unique interior stationary point of the gap solves \(K^2 r^3+(2\alpha-1)r-4\alpha=0\), lies at \(0.856768708291\), and the gap there is \(0.033889928154\).

*Proof.* The variance identities are §4 of the preregistration. The checks match the priced gap to the direct cost \(qv+\rho K^2 s+kT\,L+\alpha u_o\) at both stakes, and they match a Lyapunov evaluation of the estimate variance to \(s\). ∎

The answer to the first question is the pair of formulas. Full information, channel not priced: strictly cheaper, by \(\Delta_{\mathrm{full}}(\theta,a)\). Heat and probe priced: strictly cheaper only when the stake covers the first bit of observation. At the frozen price \(\alpha\) that happens at stake \(4\) and not at stake \(1\).

## 3. Feedback shrinks the mutual-information stock

Feedback shrinks \(\tfrac12\log(v/p)\), and the learning-rate heat stays fixed.

**Proposition AL-stock (PROVED).** At fixed error variance,
\[
v(K)-p=\frac{a}{a+bK}(\theta-p).
\]
For \(bK>0\) the right-hand side is strictly smaller than \(\theta-p\). The mutual information \(\tfrac12\log(v/p)\) falls with \(K\). The independence of the learning rate \(L=a(\theta/p-1)\) from \(K\) is **PROVED**: the action cancels in the error equation, so \(p\) and \(L\) do not contain \(K\).

The absence of \(K\) from \(Q_{\mathrm{fin}}\) is a property of the exogenous-spring formula in Proposition AT-attain of `theory/INFO_PHYSICS_ATTAINABILITY.md`. That formula does not cover a controlled plant. The physical heat of a spring tracking the controlled state stays the conjecture the proposal states.

At \(p=\theta/2\) and \(K=\sqrt{2}-1\), the state variance is \(0.853553390593\) against the uncontrolled value \(1\). The stock falls from \(0.346573590280\) to \(0.267399998370\). The learning rate is \(1\) on both sides. At that point the Sekimoto heat and the ratio of that heat to \(kT\,L\) are both \(10/9\), and only because \(L=1\).

Calling the heat a memory of the action would add a comparison these numbers do not make. That name is **METAPHOR**. The stock identity is the statement.

## 4. Separation, and where it stops

**Proposition AL-ce (PROVED).** The gain that minimizes \(qv+\rho K^2 s\) at fixed \(p\) is
\[
K^\star=\frac{-a+\sqrt{a^2+qb^2/\rho}}{b}.
\]
It does not depend on \(p\), on \(u_o\), or on \(\theta\). At \(q=\rho=b=a=1\), \(K^\star=\sqrt{2}-1\). This independence of \(p\) is certainty equivalence for unconstrained linear-quadratic-Gaussian control, the scalar case of Wonham, doi 10.1137/0306023. A cap on \(v\), or a loss whose marginal value of variance is not \(q\), is the boundary named by Bar-Shalom and Tse, doi 10.1109/TAC.1974.1100635, already cited by title in the acting-memory note.

**Proposition AL-cap (PROVED (in-model)).** The reserve \(B=16\) at this operating point gives \(P(X^2>16)=0.000014940159\), inside \(1/20\). The cap does not bind. The tight cap \(v\le 3/5\) at \(p=1/2\) selects gain \(4\), not \(\sqrt{2}-1\). The gain then depends on the observation, through the cap. Separation does not survive that cap.

**Proposition AL-capped-loss (PROVED (in-model)).** For \(\varphi(v)=\mathbb{E}[\min(X^2,1)]\), the derivative of \(\varphi(v(K))+K^2 s(K)\) at the Riccati gain equals \(0.189957517375\). The quadratic derivative at the same gain is \(0\). The gain is not stationary for the capped loss, so certainty equivalence does not extend to it.

The break has one shape in both cases. The quadratic unconstrained cost separates because the best linear gain is a function of \((a,b,q,\rho)\) alone. A cap on \(v\), or a loss whose marginal value of variance is not the constant \(q\), makes the stationarity condition depend on \(p\).

## 5. Level and variability

The two scores stay apart, as in the acting-memory preregistration. Level is the sign of \(\mathrm d J/\mathrm d\theta\). Variability is the sign of \(\mathrm d^2 J/\mathrm d\theta^2\). On the reading in `theory/ROBUSTNESS.md` §6, a concave cost is the one that gains from a spread of \(\theta\).

**Proposition AL-shape (PROVED (in-model)).** At fixed \(u_o=4\), stake \(1\), and no quadratic gap, the slope is \(1.552284749831>0\) and the second derivative is \(-0.321714500038<0\). The spread at half-width \(1/10\) is \(-0.001612560843\). A higher level of \(\theta\) raises this fixed-intensity cost. A spread of \(\theta\) lowers this fixed-intensity cost. A linear gap \(\gamma_1\theta\) moves only the slope. This \(J\) is not the minimum at stake \(1\).

The witness \(\gamma(\theta)=\theta^2\) adds \(2\) to the second derivative of that same fixed-intensity cost. The threshold is \(0.160857250019\). Above it the second derivative is positive, and the witness lies above it.

The acting-memory variability score is the second derivative of the minimized sign cost, \(0.313020858054\). The fixed-fraction spread at half-width \(1/10\) is \(0.001839996934\) and the re-optimized spread is \(0.001577268119\). A spread of \(\theta\) raises that minimized cost. The second derivative \(-0.321714500038\) is the closed-loop cost at stake \(1\) and fixed intensity \(u_o=4\). P2 says that intensity is dearer than sensing alone. The minimizing design at stake \(1\) is the blind cost \(q\theta\), whose second derivative is \(0\), so a spread does not lower the cost the hypothesis minimizes at that stake. The fixed-intensity slice is concave for every \(\theta>0\). That concavity belongs to a design the cost does not select. This note does not score the spread of the minimizing closed loop.

A linear gap of \(1/10\) leaves the old sign slope negative, at \(-0.082159696490\). A linear gap of \(1/2\) makes it positive, at \(0.317840303510\). The gap reverses that level drop and does not change its convexity. On the closed loop the same linear gap steepens a slope that is already positive.

## 6. The sign floor, feedback, and the Cox clock

**Sign grid (PROVED (in-model)).** On \(\theta\in\{1/8,1/4,1/2,1,2,4,8\}\) the minimized capped-sign cost lies strictly above \(4.966383544211\). The gap at \(\theta=8\) is \(0.031682633557\). The algebra is \(J^\star=A(r^\star)/\theta+C(r^\star)\) with \(A>0\), so the cost sits strictly above \(\inf C\) at every finite \(\theta\). The comparison of \(J^\star(8)\) with \(5\) remains the open miss recorded in the acting-memory note. This file does not edit that preregistration. The diagnosis there stands: \(5\) is the heat plus the sign loss at the frozen fraction, and the floor is lower.

**Feedback on the sign (PROVED (in-model)).** At the same error variance \(1/2\), the separated gain lowers the correlation from \(1/\sqrt{2}\) to \(\sqrt{\sqrt{2}-1}\). The sign loss rises from \(4\) to \(4.439079197657\). For this loss the closed loop is dearer than sensing alone. Shrinking the state shrinks the signal the sign is read from.

**Cox (PROVED (in-model)).** At \(\lambda(x)=1+x^2\), \(v=1\), and a failure at time \(1\), the posterior variance is \(1/2\). An independent failure at the same mean intensity leaves the variance at \(1\). The mean lifetime is \(0.655679542419\), against \(1/2\) for the constant intensity \(2\). A failure that depends on \(X\) is a measurement, and the part is then gone. A failure that ignores \(X\) adds nothing about \(X\). That second sentence is the one already proved for the acting-memory class. The numbers here are the first sentence, at one frozen law.

## 7. What the literatures state

Fetched this session. Crossref HTTP 200 for each DOI. An abstract is quoted only as far as the record prints it. A record with no abstract is cited for the title.

- Kalman, title and abstract fetched, doi 10.1115/1.3662552. The abstract derives the covariance equation of the optimal linear filter and states that filtering is the dual of the noise-free regulator. **KNOWN** for that duality. The scalar Riccati in §1 is this plant's variance equation.
- Kalman and Bucy, title and abstract fetched, doi 10.1115/1.3658902. The abstract derives the Riccati equation for the filtering error. **KNOWN** for that equation. Not a separation theorem.
- Wonham, title fetched, doi 10.1137/0306023. No abstract in the record. **KNOWN** for the title. The independence of \(K^\star\) from \(p\) in §4 is the scalar case of that separation theorem, evaluated at the frozen point.
- Bar-Shalom and Tse, title fetched, doi 10.1109/TAC.1974.1100635. No abstract in the record. **KNOWN** for the title. The cap on \(v\) and the capped loss in §4 are that boundary, evaluated at the frozen point. The acting-memory note already cited the title.
- Todorov and Jordan, title fetched, doi 10.1038/nn963. No abstract in the record. **KNOWN** for the title. This note does not identify the separated gain with a motor law.
- Sagawa and Ueda, title fetched, doi 10.1103/PhysRevLett.104.090602. No abstract in the record. **KNOWN** for the title, as the feedback equality. The heat charged here is the learning-rate floor plus a gap. It is not that equality.
- Horowitz and Esposito, title fetched, doi 10.1103/PhysRevX.4.031015. **KNOWN** as the source of the shape already used in this repository. Not re-proved.
- Friston, FitzGerald, Rigoli, Schwartenbeck, and Pezzulo, abstract fetched, doi 10.1162/NECO_a_00912. The abstract says action selection can be explained by minimizing variational free energy, and it asks whether neuronal responses can be described as a gradient descent on that free energy. **KNOWN** for that split, as related work. This note minimizes the regulation cost above. It does not minimize a free energy, and it does not identify the gain with their gradient.

## 8. How the pieces fit

This section is a synthesis. It is not a proof of one theorem that produces every layer, every shared store, every boundary, every turnover rate, and every action. What is proved is named as proved. The rest is a conjecture about how those proved pieces sit on one cost.

The cost in the master equation is memory, error, acquisition, and sharing, under a ruin cap. Limited fragile parts restrict the feasible set. A part holds a finite precision and it fails. That restriction is the same kind of object as the ruin cap. It is not another summand. The new assumption, used only in the proposal, is that the action enters the drift. When that coefficient is zero, the quadratic minimum is \(J=q\theta+\gamma_1\theta\). At \(\gamma_1=0\) the quadratic minimum equals the stake term \(q\theta\), because the minimum has set the channel, the actuation, the layer upkeep, and the link term to zero. Restoring a loss that uses the observation, and pricing memory at the heat and acquisition at the probe, is this proposal's scalar special case of the sum. It is not Theorem R1 applied at \(b=0\). The variance identity \(v=\theta\) is exact for every finite gain, and that identity is **PROVED**. The extended cost is a **CONJECTURE**. It is not an edit of the equation.

**Layers, the time axis. Proved earlier, for an exogenous world.** A stack is the cheapest design only when one store cannot reset every component, and a lumpy store's lifetime is set by its re-forming cost against the drift it faces. Those are the layer theorems already in the repository. **Conjecture:** under the closed loop the relevant reversion is \(a+bK\) rather than \(a\), so the same cost spaces the stores on the closed-loop rates. This note does not solve a multi-rate plant.

**Holographic memory, the shared store. Proved earlier in the Gaussian class, and one identity proved here.** A shared memory costs less when the decision is a sum of items, and it does not when every item is read alone. That is the holographic-memory note. The identity proved here is that feedback shrinks the stock \(\tfrac12\log(v/p)\) and does not shrink the heat. **Conjecture:** the store that remains worth sharing is the residual \(v(K)-p\), not the uncontrolled variance \(\theta\). The identity is the reason the conjecture is cheap to state. It is not a proof that the shared-store minimum moves.

**Boundary. Proved earlier for the Gaussian Markov field.** For a decision outside a region, the blanket is sufficient, and the interior is not. That is the boundary note. **Conjecture:** a feedback that damps the interior lowers the holding bound on that blanket. This note does not recompute a field.

**Turnover. Proved earlier inside its own class, and one comparison proved here.** Replacement of capacity-limited units can lower the long-run cost under the ruin cap for identical units, and the heterogeneous arm in that draft minimized at no shock. A failure time independent of \(X\) adds nothing about \(X\). The Cox calculation proved here is the other arm: at the frozen law the failure cuts the variance from \(1\) to \(1/2\), and the part is then gone. **Conjecture:** if the hazard rises with \(X^2\), shrinking \(X\) by feedback lowers the rate at which fragile parts fail, and the cost-minimizing turnover moves. The variance cut is proved. The move in the turnover rate is not computed.

**Acting. The calculation is in class AL.** The gap formulas and the stock identity are §2 and §3. The separation statement and its two breaks are that theorem and that boundary, evaluated at the frozen point. The full-information gap is the scalar linear-quadratic average cost, evaluated at three values of \(a\). The frozen decimals are the calculation. The fixed-intensity second derivative in §5 is the curvature of a design that, at stake \(1\), costs more than the blind line.

The conjecture that ties them is this. Under one cost, with parts that cannot hold an arbitrary precision and that fail, and under a ruin cap, the minimum spends control to shrink the variance a fragile part would otherwise have to carry, keeps a store only for the residual the control cannot see, shares that residual when the decision is a sum, screens it at the boundary when the decision is outside, and replaces the part when holding it is dearer than the failure. Each clause except the stock identity, the variance identity \(v=\theta\), and the minimum \(J=q\theta+\gamma_1\theta\) is a conjecture, or a theorem already proved in a class that did not contain the action. The extended cost is a conjecture. The hypothesis sentence is the bet that a strongly selected system sits near that minimum. This page does not test that bet. The antifragility reading of that synthesis — that the cost predicts when a system gains from disorder, and the conjecture that a general gain falls out of the closed loop — is stated in `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md` and in `CORE.md` §4. This section does not prove it.

## 9. Checks

`theory/acting_loop_checks/acting_loop_checks.py`. 36 checks, FAILS 0. The 33 lines in §5 of the preregistration evaluate the expressions in §4 of that file, or restate a sign §4 already gives. The preregistration says the decimals are the values of those expressions and that a later script may only evaluate them. The lock is six seconds after the commit that contains the decimals. Misses 0 is agreement with that arithmetic. This run contained no prediction that could miss. The locked numbers are the numbers the script prints.

## 10. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, `README.md`, the hypothesis sentence, or the master equation. It does not edit the acting-memory preregistration. It does not rescore T43 or T45. It does not call a self-check an independent review.
