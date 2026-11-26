# A heat floor when the memory acts on the world

*Monday 23 November 2026 (America/New_York). A follow-up to the finite-state learning-rate floor, not a change to `THEORY.md` or the hypothesis sentence. Written against `main` `41e2eda` (after PR #234, the CORE consolidation of T57–T60; drafted against `fba3f93` after PR #233). DOIs below were resolved on the Crossref API the same day (`theory/feedback_floor_checks/crossref.out`). A check script on linear Langevin loops and small bipartite jump systems, not a new simulation of a real system. Open-work row T61. T57–T60 are on `main` as of pull requests #229–#233 and are not rewritten here except for a pointer from T60. The acting-loop and acting-derivation notes (T46, T47) are used, not re-derived, for the linear class they already treat. independent review reported in [the T61 row of the retired work list](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L112); no review record committed.*

Labels follow the repo: **PROVED (in-model)** is a result inside a named class. **KNOWN** is published and credited, only for what that source states. **ELEMENTARY** is a direct consequence of a proved or known inequality, not a new named theorem. **CONJECTURE** is a named bet, not a result. **OPEN** is not derived. A lower bound is not a derivation of the cost.

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Bottom line

The general heat-floor attempt and its finite-state follow-ups (T57–T60) assumed an exogenous world: the memory does not move \(X\). That was (S5) of T57, and the case T60 left open as CX2.

Once the memory may act, the thermodynamic step still holds and the informational step does not.

The heat bound \(\dot Q_M\ge kT\,I_{\mathrm{alt}}\) under local detailed balance on the memory is **KNOWN** for bipartite jump processes (Horowitz and Esposito 2014; Proposition JP-heat), and the same split for additive-noise diffusions is Lemma D of `theory/ACTING_DERIVATION_2026-11-22.md` (EQ-heat). Those papers already allow the world's rates, or the plant drift, to depend on the memory. In a steady state the net learning rate of the memory equals the information flow used to steer the world, \(I_{\mathrm{alt}}=-I^X\). That identification is **KNOWN** (Horowitz and Esposito 2014, equations (10)–(11); Horowitz and Sandberg 2014). It is not a new identity.

The T60 destruction identity is another matter. It used that \(W_X\) was a property of the world alone. Under feedback the occupied flux is part of the design, and the same identity written with the marginal world rates is not equal to \(I_{\mathrm{alt}}\). A design-independent lower bound on the memory's heat that sees only a bare world rate and a tracking error is false. Acting can reduce \(I_{\mathrm{alt}}\) below the exogenous floor \(r\,L(\varepsilon)\), and can reverse its sign: the world's jumps then create the correlation, and the memory's jumps destroy it. When \(I_{\mathrm{alt}}<0\), JP-heat does not force a positive memory heat. These statements are **PROVED (in-model)** for finite-state bipartite chains and, for the sign change, already in the linear class LG-b of T47.

The precise boundary is the actuation class.

- If the task is to hold a fixed target in a world the design may trap with a conservative potential of \(X\) itself, an open-loop tilt already does it at vanishing ongoing heat, with a Boltzmann residual. That is T57's loophole applied to the plant. Feedback is not needed, and there is no positive ongoing floor on \(\dot Q_M\) or on the world's bath.
- If the force, or the world's rates, may depend only on the memory, a conservative *coupling* energy on the pair \((X,M)\) is still a joint equilibrium: ongoing heats vanish and the error is Boltzmann. The same loophole, now on the coupled system.
- If the design is restricted to additive feedback of the memory into a plant whose process noise is held fixed — the linear class of T46 and T47 — then a conservative trap of \(X\) is not on the menu, and a genuine trade-off appears.

In that last class two solvable implementations have to be kept apart.

1. *Compensated Kalman–Bucy / linear-quadratic-Gaussian control.* The filter knows the control and subtracts it. At a fixed observation noise the learning rate equals the exogenous formula of T46, \(L=a(\theta/p-1)\), and does not depend on the gain. Realized as a linear Langevin memory in the LG-b class of T47, the memory-bath heat is also independent of the gain, and equals twice \(kT_M\,I_{\mathrm{alt}}\), with \(kT_M=D_M\) the Einstein temperature of the memory bath. That is the same factor of two as the path-sufficient spring of T58, now under feedback. The world-bath heat is the actuation cost,

\[
\dot Q_X=\frac{g\bigl(D K_f+D_M g\bigr)}{2a+g+K_f},
\]

and diverges as the regulated variance is pushed down to the estimation error \(p\). Acting does not reduce the tracking floor. It spends world-side heat to bring the task variance down toward \(p\), and cannot go below \(p\). To hold \(v\le v^*\) the estimator must satisfy \(p\le v^*\), so \(I_{\mathrm{alt}}\ge a(\theta/v^*-1)\) is necessary in this family, but the world heat needed to actually reach \(v^*\) is a further, gain-dependent cost. These identities are **PROVED (in-model)** as an instance of Lemma LG of T47 together with the Kalman–Bucy matching.

2. *Uncompensated spring (class LG-b).* T47 already computed the heats. Both baths depend on the gain, and \(I_{\mathrm{alt}}\) changes sign when \(K>D c\gamma^2/(D_M a b)\). The uncontrolled spring formula is not the heat of the controlled loop. A search over this family finds a positive total heat at every \(v<\theta\), but a closed-form infimum of \(\dot Q_M+\dot Q_X\) at fixed \(v\), over all physical designs, is **OPEN**.

A world the memory cannot move still has the T59/T60 floor. In particular, an exogenous telegraph that the memory tracks, while a different plant is slaved to the memory, keeps the floor \(r\,L(\varepsilon)\) on the exogenous coordinate, whatever the slave rates. Acting on something else does not cancel that floor. This is **PROVED (in-model)** for a tripartite jump system in the check script.

## 1. The cost, with named terms

The method is the same as everywhere in the theory: write the cost, find its minimum, and read off the design. Whether a real system sits near that minimum is Part 2, and is not decided here.

**World and memory.** A bipartite process \((X,M)\): the two do not jump together, or, in the diffusion class, the two noises are additive and independent. Memory rates obey local detailed balance at a single bath temperature, as in Proposition JP-heat, or the memory is an overdamped coordinate with Einstein noise, as in Lemma D. The world's rates, or the plant drift, may now depend on \(M\). That is the relaxation of T57's (S5). The pair is in a steady state, or is averaged in the long run so that the Shannon entropy of \(M\) stays bounded (T57's (S4)).

**Two actuation classes.** *Conservative actuation* means that, for each frozen memory state, the world's rates satisfy local detailed balance with respect to a potential \(V(x,m)\), or that the plant drift is the gradient of a potential of \(X\) (a trap the design may deepen). *Additive feedback at fixed process noise* means the plant is

\[
dX=(-aX-g M)\,dt+\sqrt{2D}\,dW_X,
\]

with \(D\) held fixed as \(g\) varies. Open loop, this is an equilibrium Ornstein–Uhlenbeck process of variance \(\theta=D/a\). The added drift \(-g M\) is not a potential of \(X\) alone.

**Named terms of the cost.** In the class where both baths are charged and the task is a long-run error, the cost of judgment as a long-run rate, subject to the ruin cap, is

\[
J=\dot Q_M+\dot Q_X+w\,\varepsilon_{\mathrm{task}}.
\]

- \(\dot Q_M\) is the energy flow into the bath that implements the memory's transitions. Under local detailed balance, Proposition JP-heat gives \(\dot Q_M\ge kT\,I_{\mathrm{alt}}\), **KNOWN**. In the linear diffusion class, Lemma D gives \(\dot Q_M=D_M\,\mathrm{Sr}_M\) and \(\mathrm{Sr}_M\ge I_{\mathrm{alt}}\), so \(\dot Q_M\ge D_M I_{\mathrm{alt}}\) with \(kT_M=D_M\).
- \(\dot Q_X\) is the energy flow into the world's bath, the control work in this accounting. It is zero when the world is an exogenous equilibrium process, and it is the actuation cost when the design breaks that equilibrium. Sagawa and Ueda (2010) bound a one-shot work by a free-energy change minus \(kT\) times a mutual information; that is a cycle inequality, not this steady rate, and it is not stacked on JP-heat as a second price for the same nats (the warning already in T47).
- \(I_{\mathrm{alt}}\) is the net information flow of memory jumps, or the EQ-heat flow \(\int J_M\,\partial_M\ln p(X\mid M)\) in the diffusion class. In a steady state, \(I_{\mathrm{alt}}=-I^X\). The bound uses the *net* flow, as T59 corrected: JP-heat does not charge the gross copy-restoration rate.
- \(\varepsilon_{\mathrm{task}}\) is the task error: the regulated variance \(v=\mathbb{E}[X^2]\) in the linear class, or \(\mathbb{P}(X\neq x^*)\) for a two-state target, or, when the task is tracking, the Bayes error of \(X\) given \(M\). The tracking error and the task error need not coincide once the memory also steers.
- \(w\) converts the task error into the currency of the heats. Temperature does not set the stake. The ruin cap stands outside the sum. A one-time write, or a one-time tilt of a potential, is a finite cost, not a rate, as in T59.

A lower bound on \(\dot Q_M\) alone, at a fixed task error, is a lower bound on \(J\) only if the world-side heat is dropped or is known to be nonnegative. Under feedback that drop is not always justified, and a positive lower bound on \(\dot Q_M\) itself is not always true.

## 2. Prior art: what each source establishes, and what is new

Every DOI in this section was resolved on `api.crossref.org` on 23 November 2026. A repository search was done first. Nothing below is claimed as new except the in-model composition in §3–§6, and that composition is labeled. The gap each source leaves is stated for that source, not as a criticism of the paper.

**Horowitz and Esposito (2014),** *Phys. Rev. X* 4:031015, doi 10.1103/PhysRevX.4.031015. The bipartite split used as JP-heat, including the case where each subsystem's rates depend on the state of the other. In their equations (10)–(11), the information flows of the two sides sum to the time derivative of the mutual information, and each bath's entropy production bounds that side's flow. They do not introduce a tracking error or a task variance, and they do not evaluate a design-independent floor on the memory heat in those variables. **Horowitz (2015),** *J. Stat. Mech.* 2015:P03006, doi 10.1088/1742-5468/2015/03/p03006, extends the split to many subsystems. Still no tracking error.

**Horowitz and Sandberg (2014),** *New J. Phys.* 16:125007, doi 10.1088/1367-2630/16/12/125007. Second-law-like inequalities with information, compared on an analytically tractable model of feedback cooling of a Brownian particle. They show that several information measures form a hierarchy, and they interpret each as the least thermodynamic cost of a distinct measurement procedure. Their cooling problem is underdamped: a conservative trap of position does not reduce the kinetic temperature, so feedback cooling is a genuine nonequilibrium task. The overdamped position-regulation class of §5 is different, because a conservative trap of \(X\) does reduce \(v\). This note uses their identification of the information flow, already in the repo, and does not re-derive their hierarchy.

**Sagawa and Ueda (2009),** *Phys. Rev. Lett.* 102:250602, doi 10.1103/PhysRevLett.102.250602, with the 2011 erratum doi 10.1103/PhysRevLett.106.189901, bound the sum of measurement work and erasure work in one cycle by \(kT\) times one mutual information. **Sagawa and Ueda (2010),** *Phys. Rev. Lett.* 104:090602, doi 10.1103/PhysRevLett.104.090602, the feedback Jarzynski identity, with the consequence \(\langle W\rangle\ge\Delta F-kT\langle I\rangle\): feedback can lower the work done on the controlled system by the information the controller obtained. **Sagawa and Ueda (2012),** *Phys. Rev. Lett.* 109:180602, doi 10.1103/PhysRevLett.109.180602, a fluctuation theorem with information exchange. **Parrondo, Horowitz, and Sagawa (2015),** *Nat. Phys.* 11:131, doi 10.1038/nphys3230, the review that puts those statements in one frame. **Fujitani and Suzuki (2010),** *J. Phys. Soc. Jpn.* 79:104003, doi 10.1143/JPSJ.79.104003, modify the Jarzynski equality for a linear Langevin plant observed with sensor noise, estimated by a Kalman filter, and controlled by a linear regulator. **Suzuki and Fujitani (2012),** *J. Phys. Soc. Jpn.* 81:084003, doi 10.1143/JPSJ.81.084003, study the corresponding generalized second law numerically. These are cycle or one-shot inequalities, including in the same linear class as §5. They are not a steady floor on memory heat at a fixed task error, and they are not stacked on JP-heat. Already booked that way in T47 and T57.

**Ito and Sagawa (2013),** *Phys. Rev. Lett.* 111:180603, doi 10.1103/PhysRevLett.111.180603, and **Ito and Sagawa (2015),** *Nat. Commun.* 6:8498, doi 10.1038/ncomms8498, bound a subsystem's entropy production by an information flow on a causal network, or by a transfer entropy in a biochemical feedback loop. That is the same thermodynamic step already credited to Horowitz and Esposito, not a design-independent floor on memory heat against a task error. Already booked that way in T57.

**Barato, Hartich, and Seifert (2014),** *New J. Phys.* 16:103024, doi 10.1088/1367-2630/16/10/103024. A learning rate is at most the entropy production of the learning subsystem. Their receptor example also shows that another bath can pay. **Hartich, Barato, and Seifert (2016),** *Phys. Rev. E* 93:022116, doi 10.1103/PhysRevE.93.022116, define a sensory capacity, and recover a factor-of-two efficiency bound when the capacity is one. Neither paper is a design-independent floor on memory heat against a task variance under feedback.

**Touchette and Lloyd (2000),** *Phys. Rev. Lett.* 84:1156, doi 10.1103/PhysRevLett.84.1156, and **Touchette and Lloyd (2004),** *Physica A* 331:140, doi 10.1016/j.physa.2003.09.007. Feedback can reduce the entropy of a controlled system by at most the information gathered. Already in the repo as the control analogue of a directed-information bound, and as the remark that an agent can buy persistence by changing the world rather than by modeling it. Their inequality bounds an entropy change by an information, not a memory-bath heat by a task error. It is compatible with the identity \(I_{\mathrm{alt}}=-I^X\), and it is not a substitute for the cost \(J\) above.

**Tatikonda, Sahai, and Mitter (2004),** *IEEE Trans. Automat. Control* 49:1549, doi 10.1109/TAC.2004.834430, and **Kostina and Hassibi (2019),** *IEEE Trans. Automat. Control* 64:4525, doi 10.1109/TAC.2019.2912256. Rate-cost trade-offs for linear control over a communication channel, already used in Theorem P and T58. They bound an information rate needed to achieve a control cost. They do not evaluate the physical bath heats of a Kalman–Bucy implementation under feedback.

**Kalman and Bucy (1961),** *J. Basic Eng.* 83:95, doi 10.1115/1.3658902, the filtering Riccati. **Wonham (1968),** *SIAM J. Control* 6:312, doi 10.1137/0306023, the separation theorem of stochastic control, already used in T46 for the independence of the linear-quadratic gain from the estimation error. **Bar-Shalom and Tse (1974),** *IEEE Trans. Automat. Control* 19:494, doi 10.1109/TAC.1974.1100635, the boundary where certainty equivalence fails (a cap, or a loss whose marginal value of variance is not constant), already named in T46. **Sandberg, Delvenne, Newton, and Mitter (2014),** *Phys. Rev. E* 90:042119, doi 10.1103/PhysRevE.90.042119, the factor-of-two implementation cost of a demon that keeps the path, already used in T58. The companion note **Sandberg, Delvenne, Newton, and Mitter (2014),** *Proc. Allerton* 550–555, doi 10.1109/ALLERTON.2014.7028503, bounds the external power supply of a physical Kalman–Bucy filter for a class of linear port-Hamiltonian systems, and records a trade-off between that supply and the filter's back-action on the measured plant. It is an implementation cost of the estimator, already booked in T57 and T58. It is not the identification below of both bath heats of a compensated controlled loop, and it is not a design-independent floor on memory heat against a task error.

Already in the repository, and used rather than re-derived: Propositions JP-heat and EQ-heat in `theory/GENERALITY_2026-11-22.md`; Lemma D and Lemma LG, including the sign change of \(\dot I_M\) in class LG-b, in `theory/ACTING_DERIVATION_2026-11-22.md`; the independence of the Kalman–Bucy learning rate from the gain, and the variance identity \(v=p+a(\theta-p)/(a+g)\), in `theory/ACTING_LOOP_2026-11-22.md`; the factor-two memory heat of a path-sufficient spring, without feedback, in `theory/DRIFT_HEAT_LIFT_2026-11-23.md`; the two-state and finite-state exogenous floors, and the still-open frozen loophole, in `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md` and `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`. T46 charged \(kT\,L\) for the Kalman loop and left the physical heat of a spring tracking a controlled plant as a conjecture. The present note settles that conjecture for the compensated linear implementation, inside LG-b, and treats the jump case T47 left out.

**What is new here, if anything.** The thermodynamic step and the linear uncompensated heats are already in the repo. The addition is the floor statement in the T57–T60 program: that a design-independent positive floor on \(\dot Q_M\) alone, in terms of a task error, is false once the memory may act, with the exact boundary between conservative actuation and additive feedback at fixed process noise; the identification, in the compensated linear-quadratic-Gaussian realization, that the exogenous learning rate and the factor-two memory-bath heat of T58 persist independently of the gain, while the world-bath heat is the actuation cost and diverges as the regulated variance approaches the estimation error; the failure of the T60 identity under feedback, with examples where \(I_{\mathrm{alt}}\) falls below \(r\,L(\varepsilon)\) or changes sign, while JP-heat still bounds the net flow; and the preservation of the T59 floor on an exogenous coordinate that the memory tracks while it slaves a different plant. T57's loophole is not closed. It is extended to the plant.

## 3. The identity under feedback

**Assumptions for this section:** bipartite jumps, a steady state, and world rates \(W_X(x\to x'\mid m)\) that may depend on the memory. Local detailed balance is not required for the flow identity; it is required only to pass from \(I_{\mathrm{alt}}\) to heat.

The Horowitz–Esposito flows are unchanged in form,

\[
I_{\mathrm{alt}}=\sum_{x,m,m'}\pi(x,m)\,w(m\to m'\mid x)\ln\frac{\pi(m'\mid x)}{\pi(m\mid x)},
\qquad
I^X=\sum_{x,x',m}\pi(x,m)\,W_X(x\to x'\mid m)\ln\frac{\pi(x'\mid m)}{\pi(x\mid m)}.
\]

In a steady state, \(I_{\mathrm{alt}}=-I^X\). This is **KNOWN**. If \(W_X\) does not depend on \(m\), the second display reduces to T60's flux-weighted sum of KL divergences of the memory's conditionals, after the stationary flux term drops. If \(W_X\) does depend on \(m\), that reduction fails: the fluxes cannot be pulled out of the memory state, and the same sum written with the marginal rates

\[
\bar W(x\to x')=\sum_m\pi(m\mid x)\,W_X(x\to x'\mid m)
\]

is not equal to \(I_{\mathrm{alt}}\). The check records an enslaving two-state world with a copy memory at energy \(1\) and coupling \(3\), attempt rates \(1\), for which \(I_{\mathrm{alt}}=-0.675396079423\) while the marginal-rate formula gives \(1.113089395109\).

The exogenous telegraph bound is likewise not inherited. On that same design the Bayes tracking error is \(\varepsilon=0.119202922022\), the T59 floor \(r\,L(\varepsilon)\) equals \(1.523188311912\), and \(I_{\mathrm{alt}}\) lies strictly below it and is negative. A sluggish copy at energy \(0.2\) and attempt \(0.2\), enslaved at coupling \(4\) with world attempt \(2\), has \(I_{\mathrm{alt}}=-0.592743580181\). JP-heat still holds on both designs: \(\dot Q_M\ge I_{\mathrm{alt}}\) in units \(kT=1\), including the cases where both sides are negative. The bound uses the net flow. A leak still cancels from that net flow, as in T59; it is not added to a gross restoration rate.

An adversarial relabelling, a memory with the opposite copy energy on an exogenous telegraph, is the T59 copy under a flipped label. The Bayes error and the net learning rate equal those of the matching copy (\(h=\pm 2\) both give \(\varepsilon=0.268941421370\) and \(I_{\mathrm{alt}}=0.462117157260\)). A Hamming score would look worse. The bounds use the Bayes error, as in T60. Relabelling does not evade the exogenous floor. Acting on the world can.

In the linear class LG-b, T47's closed form already gives the same sign change: \(I_{\mathrm{alt}}<0\) when \(K>D c\gamma^2/(D_M a b)\), for positive parameters. At \(a=b=D=c=D_M=1\) and \(\gamma=2\), the threshold is \(K=4\), where \(I_{\mathrm{alt}}=0\), and at \(K=8\) one has \(I_{\mathrm{alt}}=-0.366972477064\), with memory heat \(6.666666666667\) and world heat \(26.666666666667\). The uncontrolled values at \(K=0\) are \(I_{\mathrm{alt}}=0.615384615385\), memory heat \(1.333333333333\), and world heat \(0\).

## 4. Conservative actuation, and the loophole

If every rate of the joint process satisfies local detailed balance with respect to a single energy \(E(x,m)\), the four-state chain is at equilibrium. All information flows vanish, and both bath heats vanish. The task error is the Boltzmann occupancy of that energy. The check records a static tilt \(E=2x\), for which the task error is \(1/(1+e^{2})=0.119202922022\) at zero ongoing heat, and a joint copy or enslaving energy, for which the heats likewise vanish at a finite Bayes error.

An open-loop tilt of \(X\) alone, with an unused memory, is the same Boltzmann residual at zero ongoing heat. For a fixed target, and a design that may apply a conservative potential of \(X\), feedback is not needed, and there is no positive ongoing floor on \(\dot Q_M+\dot Q_X\). This is **PROVED (in-model)** in the two-state jump class, and it is **ELEMENTARY** for an overdamped plant: raising the stiffness \(a\) at fixed Einstein noise \(D\) lowers \(v=D/a\) and leaves \(\mathrm{Sr}_X=0\).

That is T57's loophole, now on the plant. A one-time work that deepens a well is a finite cost, not a rate. The loophole is not a license to ignore process noise that the design is forbidden to cancel by a potential of \(X\). The next section is that restricted class.

## 5. Additive feedback at fixed process noise

**Plant and filter.** The plant is the controlled Ornstein–Uhlenbeck process of §1, mobility one, \(kT_X=D\), open-loop variance \(\theta=D/a\). An observation \(dY=X\,dt+\sqrt{r}\,dV\) drives the Kalman–Bucy filter that knows the control \(-g M\). The error variance \(p\) satisfies the same Riccati equation as the uncontrolled plant, \(p^2/r+2ap-2D=0\), or \(p=-ar+\sqrt{a^2r^2+2Dr}\). The filter SDE is an instance of class LG-b, with memory rate \(\gamma=a+g+K_f\), spring coefficient \(c=K_f/\gamma\), Kalman gain \(K_f=p/r\), and memory noise \(D_M=D-ap\). The Einstein temperature of the memory bath is \(kT_M=D_M\), which is not in general equal to the plant temperature.

**Identities, PROVED (in-model) in this implementation.** Lemma LG of T47, evaluated on those parameters, together with the variance identity of T46, gives

\[
I_{\mathrm{alt}}=a\Bigl(\frac{\theta}{p}-1\Bigr),\qquad
\dot Q_M=2\,D_M\,I_{\mathrm{alt}}=2(D-ap)\,a\Bigl(\frac{\theta}{p}-1\Bigr),\qquad
v=p+\frac{a(\theta-p)}{a+g},
\]

and the world-bath heat displayed in §0. The first two displays do not depend on \(g\). At \(a=D=1\) and \(r=\tfrac12\), one has \(p=(\sqrt{5}-1)/2=0.618033988750\), \(I_{\mathrm{alt}}=0.618033988750\), \(D_M=0.381966011250\), and \(\dot Q_M=0.472135955000\). At gain \(g=1\), the task variance is \(v=0.809016994375\) and \(\dot Q_X=0.381966011250\). At \(g=4\), \(\dot Q_X=1.527864045000\). As \(g\to\infty\), \(v\downarrow p\) and \(\dot Q_X\) diverges (\(24.445824720007\) at \(g=64\); \(97.783298880027\) at \(g=256\)), while \(\dot Q_M\) stays put.

So acting does not reduce the tracking floor in this implementation. The memory pays the same heat as it would pay to track the uncontrolled plant at the same estimation error. What acting buys is a reduction of the task variance toward that error, paid as world-bath heat. The regulated variance cannot undercut \(p\). Holding \(v\le v^*\) therefore requires \(p\le v^*\), and

\[
I_{\mathrm{alt}}\ge a\Bigl(\frac{\theta}{v^*}-1\Bigr)
\]

is necessary in this family. Equality would need \(g=\infty\) at \(p=v^*\), which is not a finite design; the world heat on the way to that edge diverges.

The factor two is the path-sufficient accounting of T58 and of Sandberg, Delvenne, Newton, and Mitter, and of Hartich, Barato, and Seifert at sensory capacity one, now checked under feedback for this implementation. It is an implementation cost, not the EQ-heat infimum. A fast uncompensated spring can have a different ratio, and can reverse the sign of \(I_{\mathrm{alt}}\); that is the LG-b family already computed in T47, not this compensated filter.

**The uncompensated spring.** For completeness, the LG-b formulas of T47 stand. Feedback can make \(I_{\mathrm{alt}}\) smaller than the open-loop learning rate at a comparable tracking error, and can change its sign, while both heats typically rise. The minimum of \(\dot Q_M+\dot Q_X\) at a fixed \(v<\theta\), over \(\gamma,c,D_M,g\), is **OPEN** as a closed form. The check does not claim a number for that infimum.

## 6. The minimum, and what is read off

On the Kalman family, with \(a=D=1\) so that \(\theta=1\),

\[
J(r,g)=\dot Q_M(r)+\dot Q_X(r,g)+w\,v(r,g).
\]

The blind design — no observation, no gain — has \(J=w\). Any finite observation at zero gain leaves \(v=\theta\) and adds a strictly positive memory heat, so it is dearer than the blind line. The ruin cap stands outside.

At the named point \(r=\tfrac12\), \(g=1\), the cost is \(J=7.326237921249\) at stake \(w=8\), which is strictly cheaper than the blind line \(8\), and is \(J=1.663118960625\) at stake \(w=1\), which is strictly dearer than the blind line \(1\). The design those two stakes read off is therefore not the same: at the low stake the named loop is not used; at the high stake it is cheaper than doing nothing. That is the same qualitative split T46 already had for a priced channel. The present numbers charge the physical baths of this implementation, not \(kT\,L\) alone. A full minimization of \(J(r,g)\) over the family is a numerical exercise, not a closed form, and is not claimed as a theorem. The design that approaches the necessary bound \(I_{\mathrm{alt}}=a(\theta/v^*-1)\) at a prescribed \(v^*\), at finite world heat, is **OPEN**.

When a conservative trap of \(X\) is allowed, the minimum of the ongoing rate \(\dot Q_M+\dot Q_X+w v\) at a fixed \(v\) is the Boltzmann, or Einstein, residual of that trap, at vanishing ongoing heat, plus the one-time work of setting the well. The ongoing minimum is then the stake term alone. That design is not in the additive-feedback family of §5.

## 7. What this does and does not close

- **T57, T59, T60.** The thermodynamic step is unchanged, and already covered feedback. The useful exogenous bound on \(\Phi\) is not inherited by a world the memory moves. The frozen-world loophole stays open, and is extended to a plant the design may trap conservatively. A general design-independent \(\Phi\) for every feedback kernel is not claimed.
- **T46, T47, T58.** Not edited. The independence of the Kalman–Bucy learning rate from the gain is reused, and is here identified with the Horowitz–Esposito / Lemma D flow and with the physical memory-bath heat of the compensated LG-b realization, including the factor two and the world-bath actuation cost. T46's conjecture on the heat of a spring tracking a controlled plant is settled for that compensated realization, and remains the T47 calculation for the uncompensated spring. Dual control, in the sense of Bar-Shalom and Tse — acting in order to learn — is still **OPEN**.
- **CX2.** Not closed as a whole. This note treats the heat floor on a memory that also steers, in the named classes. Co-adaptation of several parties, Bode limits, and a world whose noise intensity the design may change are not treated. The selection-level statements are `theory/COADAPTATION.md` F3 and F4. They are a different object: F3 is a linear copy gain on a cost, and F4 is delayed push-back with gain below −1. This note's plant need not optimize. Joining the two accounts is open (`README.md` ranked table, BICAUSAL).
- **T48, T49, T40.** Not applied. `THEORY.md` is not edited. No system has been shown to qualify under THEORY §3.

## 8. Numerical checks

The script `theory/feedback_floor_checks/feedback_floor_checks.py` records the algebra and the in-model evaluations used above: the LG-b Lyapunov identities and the sign change of the learning rate; the Kalman–Bucy matching, including independence of the gain, the factor-two memory heat, the world-heat display, the variance floor \(v\ge p\), and the necessary sensing bound at a prescribed \(v^*\); the named costs at stakes \(1\) and \(8\); the exogenous telegraph recovery of T59 and T60; joint-equilibrium and open-loop tilts at zero ongoing heat; the failure of the marginal-rate identity under feedback, with designs that reduce or reverse \(I_{\mathrm{alt}}\) while JP-heat still holds on the net flow; an adversarial relabelling that does not evade T59; and a tripartite exogenous reference whose T59 floor is independent of the slave. The run used for this note reports `FAILS 0`. These are not measurements of a real system.

## 9. References

DOIs resolved on Crossref, 23 November 2026, America/New_York. The log is `theory/feedback_floor_checks/crossref.out`.

- Kalman, R. E. and Bucy, R. S. 1961. New Results in Linear Filtering and Prediction Theory. *J. Basic Eng.* 83:95. doi 10.1115/1.3658902.
- Wonham, W. M. 1968. On the Separation Theorem of Stochastic Control. *SIAM J. Control* 6:312. doi 10.1137/0306023.
- Bar-Shalom, Y. and Tse, E. 1974. Dual effect, certainty equivalence, and separation in stochastic control. *IEEE Trans. Automat. Control* 19:494. doi 10.1109/TAC.1974.1100635.
- Touchette, H. and Lloyd, S. 2000. Information-Theoretic Limits of Control. *Phys. Rev. Lett.* 84:1156. doi 10.1103/PhysRevLett.84.1156.
- Touchette, H. and Lloyd, S. 2004. Information-theoretic approach to the study of control systems. *Physica A* 331:140. doi 10.1016/j.physa.2003.09.007.
- Tatikonda, S., Sahai, A. and Mitter, S. 2004. Stochastic Linear Control Over a Communication Channel. *IEEE Trans. Automat. Control* 49:1549. doi 10.1109/TAC.2004.834430.
- Sagawa, T. and Ueda, M. 2009. Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure. *Phys. Rev. Lett.* 102:250602. doi 10.1103/PhysRevLett.102.250602. Erratum: *Phys. Rev. Lett.* 106:189901 (2011), doi 10.1103/PhysRevLett.106.189901.
- Fujitani, Y. and Suzuki, H. 2010. Jarzynski Equality Modified in the Linear Feedback System. *J. Phys. Soc. Jpn.* 79:104003. doi 10.1143/JPSJ.79.104003.
- Sagawa, T. and Ueda, M. 2010. Generalized Jarzynski Equality under Nonequilibrium Feedback Control. *Phys. Rev. Lett.* 104:090602. doi 10.1103/PhysRevLett.104.090602.
- Suzuki, H. and Fujitani, Y. 2012. Numerical Study on the Generalized Second Law for a Brownian Particle under the Linear Feedback Control. *J. Phys. Soc. Jpn.* 81:084003. doi 10.1143/JPSJ.81.084003.
- Sagawa, T. and Ueda, M. 2012. Fluctuation Theorem with Information Exchange: Role of Correlations in Stochastic Thermodynamics. *Phys. Rev. Lett.* 109:180602. doi 10.1103/PhysRevLett.109.180602.
- Ito, S. and Sagawa, T. 2013. Information Thermodynamics on Causal Networks. *Phys. Rev. Lett.* 111:180603. doi 10.1103/PhysRevLett.111.180603.
- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Horowitz, J. M. and Sandberg, H. 2014. Second-law-like inequalities with information and their interpretations. *New J. Phys.* 16:125007. doi 10.1088/1367-2630/16/12/125007.
- Barato, A. C., Hartich, D. and Seifert, U. 2014. Efficiency of cellular information processing. *New J. Phys.* 16:103024. doi 10.1088/1367-2630/16/10/103024.
- Sandberg, H., Delvenne, J.-C., Newton, N. J. and Mitter, S. K. 2014. Maximum work extraction and implementation costs for nonequilibrium Maxwell's demons. *Phys. Rev. E* 90:042119. doi 10.1103/PhysRevE.90.042119.
- Sandberg, H., Delvenne, J.-C., Newton, N. J. and Mitter, S. K. 2014. Thermodynamic costs in implementing Kalman-Bucy filters. *Proc. Allerton* 550–555. doi 10.1109/ALLERTON.2014.7028503.
- Horowitz, J. M. 2015. Multipartite information flow for multiple Maxwell demons. *J. Stat. Mech.* 2015:P03006. doi 10.1088/1742-5468/2015/03/p03006.
- Parrondo, J. M. R., Horowitz, J. M. and Sagawa, T. 2015. Thermodynamics of information. *Nat. Phys.* 11:131. doi 10.1038/nphys3230.
- Ito, S. and Sagawa, T. 2015. Maxwell's demon in biochemical signal transduction with feedback loop. *Nat. Commun.* 6:8498. doi 10.1038/ncomms8498.
- Hartich, D., Barato, A. C. and Seifert, U. 2016. Sensory capacity: An information theoretical measure of the performance of a sensor. *Phys. Rev. E* 93:022116. doi 10.1103/PhysRevE.93.022116.
- Kostina, V. and Hassibi, B. 2019. Rate-Cost Tradeoffs in Control. *IEEE Trans. Automat. Control* 64:4525. doi 10.1109/TAC.2019.2912256.

Already in the repository, and used rather than re-derived: Propositions JP-heat and EQ-heat in `theory/GENERALITY_2026-11-22.md`; Lemma D and Lemma LG in `theory/ACTING_DERIVATION_2026-11-22.md`; the Kalman–Bucy loop identities in `theory/ACTING_LOOP_2026-11-22.md`; the factor-two spring of T58 in `theory/DRIFT_HEAT_LIFT_2026-11-23.md`; the exogenous two-state and finite-state floors in `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md` and `theory/GENERAL_FLOOR_FINITE_2026-11-23.md`; the general-floor attempt and its loophole in `theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`.

## 10. What this note does not do

It does not edit `THEORY.md` or the hypothesis sentence. It adds a pointer, and a short class paragraph, in `CORE.md` §3 for the feedback case, and it does not otherwise rewrite CORE. It does not add a CLAIM_MAP row, and it does not change the status of IP3, IP11, T40, T46, T47, T48, T49, T57, T58, T59, or T60 except to point at this follow-up from T60 and from the open-work rows. It does not edit the T46–T60 files except for that pointer from T60. It does not prove a closed-form floor for every feedback kernel, and it does not treat an in-model statement as a fact about a real system. It does not claim to close T57's loophole, and it does not claim to close CX2. No system has been shown to qualify under THEORY §3.

## Class summary (moved here from the retired [`STATUS.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/STATUS.md), 25 November 2026)

*Feedback boundary* (T61, proved-in-model, `theory/FEEDBACK_FLOOR_2026-11-23.md:13-35`; independent review reported in [the T61 row of the retired work list](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L112); no review record committed). T61 is heat accounting for a passive plant. It is not co-adaptation F3/F4. \(\dot Q_M\ge kT\,I_{\mathrm{alt}}\) with \(I_{\mathrm{alt}}=-I^X\) still holds when the memory steers the world, while T60's exogenous bare-rate floor (T60, proved-in-model, in its exogenous class) fails (acting can lower or reverse \(I_{\mathrm{alt}}\)); conservative traps have vanishing ongoing heat, whereas additive linear feedback separates compensated Kalman–Bucy control from uncompensated loops.
