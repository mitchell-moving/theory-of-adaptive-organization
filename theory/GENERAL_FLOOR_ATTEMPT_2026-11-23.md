# A general heat-floor attempt

*Monday 23 November 2026 (America/New_York). An attempt at one general heat floor, not a change to `THEORY.md` or the hypothesis sentence. Written against `main` `f9874f0`. DOIs below were resolved on the Crossref API the same day (`theory/general_floor_checks/crossref.out`). No new simulation. Open-work row T57. Independent review of PR #229 applied label and citation nits and confirmed READY the same day.*

Labels follow the repo: **PROVED (in-model)** is a result inside a named class. **KNOWN** is published and credited, only for what that source states. **ELEMENTARY** is a direct consequence of a proved or known inequality, not a new named theorem. **CONJECTURE** is a named bet, not a result. **SKETCH** is an argument with a stated gap. **OPEN** is not derived. A lower bound is not a derivation of the cost.

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Bottom line

The heat floor the theory wants is two inequalities composed, not one.

The first is thermodynamic: the bath of the memory gives off heat at least \(kT\) times the rate at which the memory's own transitions learn. That inequality is **KNOWN** for bipartite jump processes (Horowitz and Esposito 2014; Proposition JP-heat in `theory/GENERALITY_2026-11-22.md`) and **PROVED (in-model)** for additive-noise diffusions (Proposition EQ-heat). The same shape extends to many subsystems with a well-defined split (Horowitz 2015). Landauer's bound, the Sagawa–Ueda generalized second law, Still's prediction bound, the thermodynamic uncertainty relations, and one-shot information-thermodynamic identities do not replace it, and none of them is a floor on steady heat in terms of tracking error.

The second is informational: that learning rate is at least some function \(\Phi\) of the tracking error and the world's law. If \(\Phi\) is defined as the infimum of the learning rate at a fixed error, the inequality is a definition. A useful, design-independent lower bound on \(\Phi\) is the step that does not go through in general. It holds in the named classes: the telegraph, one-dimensional equilibrium diffusions (and the Ornstein–Uhlenbeck evaluation), and, as an information inflow rather than a heat, linear drifting worlds (`theory/THEOREM_P_DRIFT.md`, pending re-confirm). The missing assumption is a quantitative mixing or amplification inequality for the world. Without one, a frozen world can hold a small error at vanishing steady heat after a one-time write, and a world without a Fisher, entropy-power, or contraction structure does not yet yield a closed form.

So the candidate general statement, under the assumptions of the thermodynamic step and with \(\Phi\) left as the causal learning-rate–distortion function of the world, is the composition of GF-T (**KNOWN** for bipartite chains; **PROVED (in-model)** for additive-noise diffusions) with GF-I (**ELEMENTARY**). It is not a closed-form floor for every adaptive system. That is the exact break. It is an open question about what extra structure the world must have.

## 1. The cost, with named terms

The method is the same as everywhere in the theory: write the cost, find its minimum, and read off the design. Whether a real system sits near that minimum is Part 2, and is not decided here.

Inside the physics display of `CORE.md` §1 and `theory/GENERAL_FORM_PHYSICS_2026-11-22.md`, the cost of judgment is the memory-bath heat plus a stake on the decision loss, with the ruin cap outside the sum:

\[
J=\dot Q_M+w\,\mathbb{E}[\ell]\qquad\text{subject to}\qquad P(\mathrm{ruin})\le\varepsilon.
\]

Named terms:

- \(\dot Q_M\) is the energy flow into the bath that implements the memory's transitions, in energy per unit time, in a steady state or as a long-run average.
- \(kT\) is Boltzmann's constant times that bath's temperature.
- \(\dot I_M\) is the information flow of those same memory transitions, in nats per unit time (the Horowitz–Esposito flow; \(I_{\mathrm{alt}}\) in JP-heat; \(\dot I_M\) in EQ-heat).
- \(\ell\) is a chosen distortion, a function of an action \(A=f(M)\) and of the world \(X\), or of a lead of \(X\). The expected loss is \(d=\mathbb{E}[\ell]\).
- \(w\) converts that loss into the currency of the heat. Temperature does not set \(w\).
- The ruin cap \(\varepsilon\) is a constraint, not a term in the sum.
- A link price, a constant layer upkeep, and a separate read price stay assumed when they appear in the five-term display of `THEORY.md` §3. This note does not adopt the physics display into `THEORY.md` (T40 remains open).

A lower bound on \(\dot Q_M\) at fixed \(d\) is a lower bound on \(J\) at that \(d\). The minimum over designs is then at least the minimum over \(d\) of that bound plus \(wd\).

## 2. Prior art: what already gives, and what it lacks

Every DOI in this section was resolved on `api.crossref.org` on 23 November 2026. Nothing below is claimed as new. The gap to a heat-versus-error floor is stated for each result, not as a criticism of the paper.

**Landauer (1961),** *IBM J. Res. Dev.* 5:183, doi 10.1147/rd.53.0183. An erasure bound of \(kT\ln 2\) for one bit of a symmetric memory. It is a one-shot, or per-cycle, cost of resetting a memory. It is not a steady learning rate, and it does not mention a tracking error.

**Sagawa and Ueda (2008),** *Phys. Rev. Lett.* 100:080403, doi 10.1103/PhysRevLett.100.080403, the second law with discrete quantum feedback control; **Sagawa and Ueda (2009),** *Phys. Rev. Lett.* 102:250602, doi 10.1103/PhysRevLett.102.250602, with the 2011 erratum doi 10.1103/PhysRevLett.106.189901, a bound on the sum of measurement work and erasure work in one cycle by \(kT\) times one mutual information; **Sagawa and Ueda (2010),** *Phys. Rev. Lett.* 104:090602, doi 10.1103/PhysRevLett.104.090602, the feedback Jarzynski identity \(\langle e^{-\beta(W-\Delta F)-I}\rangle=1\) and the consequence \(\langle W\rangle\ge\Delta F-kT\langle I\rangle\); **Sagawa (2012),** *Prog. Theor. Phys.* 127:1, doi 10.1143/ptp.127.1, the longer account of information processing in small systems; **Parrondo, Horowitz, and Sagawa (2015),** *Nat. Phys.* 11:131, doi 10.1038/nphys3230, the review that puts those statements in one frame. These are the generalized second law with information. They bound a work, or a cycle cost, by a free-energy change and a mutual information. They do not identify a steady learning rate with a tracking error, and they do not produce \(kT\,a(v-\varepsilon)/\varepsilon\).

**Horowitz and Esposito (2014),** *Phys. Rev. X* 4:031015, doi 10.1103/PhysRevX.4.031015. For a bipartite system, in steady state, the learning subsystem's bath obeys \(\dot S_r\ge\dot I\): heat over temperature is at least the information flow of that subsystem's transitions. This is the thermodynamic step for jump processes. It has no distortion variable.

**Horowitz (2015),** *J. Stat. Mech.* 2015:P03006, doi 10.1088/1742-5468/2015/03/p03006. The same split for many subsystems whose noise is independent given the state (a multipartite, not only bipartite, split). Each bath still pays at least temperature times that subsystem's information flow. Still no tracking error.

**Ito and Sagawa (2013),** *Phys. Rev. Lett.* 111:180603, doi 10.1103/PhysRevLett.111.180603. On a causal network, the entropy production of a subsystem is bounded by an information flow (a transfer entropy) fixed by the network's topology. Again heat versus information flow, not heat versus error.

**Barato, Hartich, and Seifert (2014),** *New J. Phys.* 16:103024, doi 10.1088/1367-2630/16/10/103024. A learning rate is at most the entropy production of the learning subsystem. The same thermodynamic step, written as an efficiency. Their receptor example also shows that another bath can pay: a cell can learn while its own dissipation is zero. The floor is on the bath that implements the memory transitions, not on an arbitrarily chosen ledger. **Horowitz and Sandberg (2014),** *New J. Phys.* 16:125007, doi 10.1088/1367-2630/16/12/125007, give second-law inequalities with an information flow, in the same family.

**Still, Sivak, Bell, and Crooks (2012),** *Phys. Rev. Lett.* 109:120604, doi 10.1103/PhysRevLett.109.120604, and **Still (2020),** *Phys. Rev. Lett.* 124:050601, doi 10.1103/PhysRevLett.124.050601. Dissipation is bounded by the part of the memory that does not predict (the irrelevant information). A memory that keeps only what predicts can saturate a vanishing excess in that bound. The inequality charges useless memory. It does not force the heat to rise as the tracking error falls.

**Goldt and Seifert (2017),** *Phys. Rev. Lett.* 118:010601, doi 10.1103/PhysRevLett.118.010601. The information a network acquires about a classification rule is bounded by the thermodynamic cost of adjusting its weights. It is again heat versus acquired information, for a learning task, not a formula in a tracking error of a changing world.

**Barato and Seifert (2015),** *Phys. Rev. Lett.* 114:158101, doi 10.1103/PhysRevLett.114.158101, and **Gingrich, Horowitz, Perunov, and England (2016),** *Phys. Rev. Lett.* 116:120601, doi 10.1103/PhysRevLett.116.120601. Thermodynamic uncertainty relations: a current's relative uncertainty costs dissipation (in the 2015 paper, at least \(2k_BT/\varepsilon_{\mathrm{rel}}^2\) inside linear response, and for unicyclic networks beyond it; the 2016 paper is the general Markov-jump case). The uncertainty is that of a current, not the error of a memory that tracks a world. **Riechers, Boyd, Wimsatt, and Crutchfield (2020),** *Phys. Rev. Research* 2:033524, doi 10.1103/PhysRevResearch.2.033524, bound dissipation against logical error under time-symmetric control, with a cost that grows as the logarithm of the inverse error. That is the reliability of a computation or an erasure, not a tracking floor.

**Rate-distortion, as an information bound.** For a source and a distortion, Shannon's rate-distortion function gives \(I(A;X)\ge R(d)\). That is a stock of mutual information, not a heat, and not automatically a rate in time. The causal and sequential versions bound an information inflow against a distortion: **Tatikonda, Sahai, and Mitter (2004),** *IEEE Trans. Automat. Control* 49:1549, doi 10.1109/TAC.2004.834430, the scalar Gauss–Markov formula; **Kostina and Hassibi (2019),** *IEEE Trans. Automat. Control* 64:4525, doi 10.1109/TAC.2019.2912256, the vector entropy-power converse; **Tanaka, Kim, Parrilo, and Mitter (2017),** *IEEE Trans. Automat. Control* 62:1896, doi 10.1109/TAC.2016.2601148, the Gaussian sequential program; **Duncan (1970),** *SIAM J. Appl. Math.* 19:215, doi 10.1137/0119020, the continuous-time Kalman–Bucy rate. `theory/THEOREM_P_DRIFT.md` already packages those as an information-flow floor. None of those papers identifies the inflow with a bath heat.

**The factor-of-two accounting, still open as a minimum-power question.** **Sandberg, Delvenne, Newton, and Mitter (2014),** *Proc. Allerton*, doi 10.1109/ALLERTON.2014.7028503, and the companion paper *Phys. Rev. E* 90:042119, doi 10.1103/PhysRevE.90.042119, give an implementation cost of \(2kT\) times the transfer-entropy rate for a demon that keeps the path. **Hartich, Barato, and Seifert (2016),** *Phys. Rev. E* 93:022116, doi 10.1103/PhysRevE.93.022116, prove that when sensory capacity is \(1\), efficiency is at most \(1/2\). In the proved Ornstein–Uhlenbeck class, the infimum of the memory-bath heat at a mean-squared decision error is \(kT\) times the Kalman rate (factor one), approached at finite heat by a fast shrunk spring (`theory/INFO_PHYSICS_ATTAINABILITY.md`, T38). Those factor-two statements cover a path-keeping or capacity-one accounting. They are not the infimum of the learning-rate heat in that class, and they are not settled as a general prefactor. The Kalman–Bucy minimum-power factor-of-two question remains open, as `CORE.md` §3 already says.

The combination that is still missing from this list is a general identification of bath heat with a design-independent function of tracking error.

## 3. The candidate general statement

**Assumptions.**

- (S1) A well-defined memory/world split: the pair \((X,M)\) is bipartite, or more generally multipartite, in the sense that the noise or jumps that move \(M\) are conditionally independent of those that move \(X\) given the present state. No simultaneous jump of both.
- (S2) Local detailed balance of the memory transitions at a single bath temperature \(T\); or, for an additive-noise diffusion, a constant diffusion coefficient \(D_M>0\), a smooth drift, vanishing boundary terms, and the Einstein relation that identifies the energy flow into that bath with \(D_M\) times the entropy production of \(M\) (mobility \(1\), so \(kT=D_M\), as in EQ-heat).
- (S3) A distortion \(\ell\) and an action \(A=f(M)\), with finite expected loss \(d=\mathbb{E}[\ell]\).
- (S4) A steady state, or a long-run average in which the Shannon entropy of \(M\) stays bounded, so that its time derivative averages to zero.
- (S5) For the special-case checks that use an exogenous world, the design does not move \(X\) (the standing assumption of the two proved classes and of Theorem P's PD-A). A world the system moves is a different problem (CX2).

**The thermodynamic step (GF-T).** Under (S1), (S2), and (S4),

\[
\dot Q_M\ge kT\,\dot I_M.
\]

**The informational step (GF-I).** Define the causal learning-rate–distortion function of the world, for the chosen distortion,

\[
\Phi(d)=\inf\bigl\{\dot I_M:\text{designs obeying (S1)--(S5) with }\mathbb{E}[\ell]\le d\bigr\}.
\]

Then \(\dot I_M\ge\Phi(d)\) holds by construction, and so

\[
\dot Q_M\ge kT\,\Phi(d),\qquad J\ge kT\,\Phi(d)+wd,
\]

subject to the ruin cap. A lower bound on the frontier, when the cap is slack, is the minimum of \(kT\,\Phi(d)+wd\) over attainable \(d\). That bound is the frontier itself in those classes where the heat \(kT\,\Phi(d)\) is approached.

**What is claimed.** GF-T is **KNOWN** for finite-state bipartite chains under local detailed balance, and **PROVED (in-model)** for additive-noise diffusions under the Einstein relation of EQ-heat. Horowitz (2015) extends the same shape to multipartite systems that still have a split. GF-I with \(\Phi\) defined as that infimum is **ELEMENTARY**. A closed-form, design-independent lower bound on \(\Phi\) is a further claim, and is not part of the general statement as proved.

## 4. Attempted proof, and the exact break

**GF-T.** For a finite-state bipartite chain, local detailed balance writes the log of the rate ratio as the energy drop. The memory-edge entropy production is a sum of terms \((a-b)\ln(a/b)\ge 0\), and it splits as \(\dot Q_M/kT-\dot I_M\) (JP-heat; Horowitz and Esposito 2014, equation (11) in the steady state). For an additive-noise diffusion \(dM=F(X,M)\,dt+\sqrt{2D_M}\,dW\), the same nonnegativity is \(\int J^2/(D_M p)\ge 0\), and it splits as the entropy production of \(M\) minus \(\dot I_M\) plus a marginal-entropy term that vanishes in steady state (EQ-heat). The Einstein relation converts entropy production into bath heat. Those are the existing proofs. They are not redone here.

The argument uses the split (S1) and the identification of heat (S2). If \(X\) and \(M\) can jump together, the information-flow split is not the one those proofs use. If the control or the noise sits in a state-dependent diffusion coefficient, the Einstein identification of EQ-heat is not the one stated. If another bath pays, as in the receptor example of Barato, Hartich, and Seifert (2014), a ledger kept on the wrong bath can read below \(kT\,\dot I_M\). In a transient, the marginal-entropy term need not vanish; (S4) is there so that a time average recovers the inequality when \(S_M\) is bounded. None of those is a counterexample inside the stated class. Each is a place the hypothesis of GF-T fails.

**GF-I, as a definition, does not break.** The infimum \(\Phi(d)\) exists in \([0,\infty]\) whenever the set of designs is nonempty. The composition \(\dot Q_M\ge kT\,\Phi(d)\) then holds wherever GF-T holds.

**The useful bound on \(\Phi\) is the step that breaks.** A general proof would need, for an arbitrary world and an arbitrary finite-loss distortion, a number \(\phi(d;\text{world})\), computable from the world's law and the distortion alone, such that every design satisfies \(\dot I_M\ge\phi(d;\text{world})\). Three structures give such a number in named classes, and each uses an extra assumption on the world:

1. *Fisher / de Bruijn.* For a one-dimensional exogenous equilibrium diffusion, Proposition EQ-learn gives \(\dot I_M\ge D(1/d-\mathcal I(p_X))\) at residual variance \(d\). Equality needs a Gaussian conditional of constant variance, a Gaussian marginal, and the Einstein relation of the world. The step is Cauchy–Schwarz on the conditional score, then Jensen on \(1/\mathrm{Var}\). Without a vanishing probability current, the identity that replaces the learning rate by a Fisher difference is not the one proved there.
2. *Entropy power / linear amplification.* For a linear world \(X_{t+1}=AX_t+W_t\) with a density, the sharp inflow floor of PD1(b) is the Tatikonda–Sahai–Mitter / Kostina–Hassibi bound. A weaker Shannon lower bound, PD1(a), holds for any exogenous world. Both are bounds on an information inflow \(\bar r\), not on a bath heat.
3. *A two-state jump.* On the telegraph, the flow at Hamming error \(\varepsilon\) is \(\gamma(1-2\varepsilon)\ln((1-\varepsilon)/\varepsilon)\), and a fast memory approaches a heat of \(kT\) times that flow.

No one of those three structures is implied by (S1)–(S5) alone. A frozen world is allowed by those assumptions and has \(\Phi(d)=0\) at any error that a one-time write can achieve: once the memory is set, the world's transitions destroy no information, so the steady learning rate can vanish. That is the freeze corner the theory already has (`CORE.md` §4; CT11), and it is the reason a maintenance floor has to see how the world mixes or amplifies. A follow-up that applies JP-heat to the net information flow of a two-state record, and that separates a static bias, metastable retention, and irreversible refresh, is `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md` (OPEN_WORK T59; a self-check, not an independent review). In that class the memory-bath heat is bounded by \(kT\,r\,L(\varepsilon)\), so a frozen world still has vanishing steady heat at a finite Boltzmann error: the loophole named here stays open at \(r=0\). A further follow-up, for a general finite-state Markov-jump world, is `theory/GENERAL_FLOOR_FINITE_2026-11-23.md` (OPEN_WORK T60; a self-check, not an independent review): the unconditional positivity statement fails when the occupied flux graph is disconnected, and when that graph is strongly connected the net learning rate is bounded below by a world-only function of the Bayes error, reducing to \(r\,L(\varepsilon)\) on the telegraph. A general strong-data-processing or logarithmic-Sobolev bound would be a fourth structure of the same kind: it would turn residual information into a destruction rate, and rate-distortion would turn residual error into residual information. This note does not prove such a bound, and it does not claim one for an arbitrary kernel.

That is the exact break: the step from \(\dot I_M\ge\Phi(d)\) to a design-independent closed form \(\Phi(d)\ge\phi(d;\text{world})\). The extra assumption that would close it is a quantitative mixing or amplification inequality for the world, strong enough to convert a residual error into a rate.

## 5. Special-case checks

**Bipartite chains.** GF-T is JP-heat. For the telegraph, the known flow is a closed form of \(\Phi\), and the heat infimum is \(kT\) times that flow (`theory/GENERAL_FORM_PHYSICS_2026-11-22.md` §4). The candidate reduces to the proved telegraph floor. It does not, by itself, evaluate \(\Phi\) for an arbitrary finite-state world.

**Additive-noise diffusions.** GF-T is EQ-heat, with no Gaussian or linear step. For a one-dimensional exogenous equilibrium signal, EQ-learn lower-bounds \(\Phi\); for an equilibrium Ornstein–Uhlenbeck signal of rate \(a\) and variance \(v\), that bound is \(a(v/\varepsilon-1)\), and a fast linear memory approaches a heat of \(kT\) times that rate at finite heat (T38). The candidate reduces to the proved Ornstein–Uhlenbeck floor. The independent-mode and sum-loss extensions already in `theory/INFO_PHYSICS_GENERAL.md` are evaluations of \(\Phi\) in those subclasses, not a new general proof.

**Drifting linear worlds.** PD1 of `theory/THEOREM_P_DRIFT.md` is a lower bound on an information inflow \(\bar r\). If a physical implementation of that discrete-time filter has \(\dot I_M=\bar r\) in the sense of GF-T, the candidate would lift PD1 to a heat floor \(\dot Q_M\ge kT\,\bar r\). That identification is not proved in `theory/THEOREM_P_DRIFT.md`: that note has no thermodynamic assumption, and its own re-confirm is still pending. The continuous-time sampling limit of the scalar PD1 bound recovers the Kalman rate \(\sigma^2/(2D)-\theta\), which already matches the proved Ornstein–Uhlenbeck heat floor. That is a consistency check, not the missing lift. The lift itself is **OPEN**, and it is where the factor-of-two accounting would have to be faced for a discrete-time implementation.

In all three checks, the cost \(J\ge kT\,\Phi(d)+wd\) is the physics display already in use. The stake, the link price, and the ruin cap are not derived.

## 6. What this does and does not close

- **T11 / CX1.** The information-flow form of Theorem P stays as drafted, pending re-confirm. This note does not re-confirm it, and it does not supply the heat lift.
- **T48.** The continuous-information extension of representation axiom A6 is a different object: it is about the memory coordinate of the priced cost, not about bath heat. It stays open.
- **T49.** Non-Gaussian closed forms are evaluations of \(\Phi\) in further classes. The general attempt explains why those stay class by class. It does not compute them.
- **The Kalman–Bucy factor-of-two question.** Remains open. Section 2 locates it as an implementation-accounting question, already distinguished from the learning-rate heat infimum in the proved Ornstein–Uhlenbeck class.
- **T40.** Not applied. `THEORY.md` is not edited.

## 7. Cheapest next step

Re-confirm `theory/THEOREM_P_DRIFT.md`, which is already drafted. Then try the thermodynamic lift in that class: identify the discrete-time inflow \(\bar r\) with \(\dot I_M\) for one physical implementation, and say whether the heat is \(kT\,\bar r\) or whether a factor appears. That is the nearest missing special-case check, and it uses work already on the page.

A second cheap proof, not done here, would write the \(n\)-dimensional Fisher / de Bruijn form of EQ-learn for an exogenous equilibrium additive-noise diffusion, and state the bound in terms of the error covariance (or a looser trace form in the scalar mean square). That would enlarge the concrete-\(\Phi\) class without leaving the setting of EQ-heat.

The finite-state jump case of that job is `theory/GENERAL_FLOOR_FINITE_2026-11-23.md` (T60). A general strong-data-processing bound for an arbitrary kernel, including diffusions, remains a larger job, and is not the cheapest remaining move.

## 8. References

DOIs resolved on Crossref, 23 November 2026, America/New_York. The log is `theory/general_floor_checks/crossref.out`.

- Landauer, R. 1961. Irreversibility and Heat Generation in the Computing Process. *IBM J. Res. Dev.* 5:183. doi 10.1147/rd.53.0183.
- Sagawa, T. and Ueda, M. 2008. Second Law of Thermodynamics with Discrete Quantum Feedback Control. *Phys. Rev. Lett.* 100:080403. doi 10.1103/PhysRevLett.100.080403.
- Sagawa, T. and Ueda, M. 2009. Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure. *Phys. Rev. Lett.* 102:250602. doi 10.1103/PhysRevLett.102.250602. Erratum, 2011, doi 10.1103/PhysRevLett.106.189901.
- Sagawa, T. and Ueda, M. 2010. Generalized Jarzynski Equality under Nonequilibrium Feedback Control. *Phys. Rev. Lett.* 104:090602. doi 10.1103/PhysRevLett.104.090602.
- Sagawa, T. 2012. Thermodynamics of Information Processing in Small Systems. *Prog. Theor. Phys.* 127:1. doi 10.1143/ptp.127.1.
- Still, S., Sivak, D. A., Bell, A. J. and Crooks, G. E. 2012. Thermodynamics of Prediction. *Phys. Rev. Lett.* 109:120604. doi 10.1103/PhysRevLett.109.120604.
- Ito, S. and Sagawa, T. 2013. Information Thermodynamics on Causal Networks. *Phys. Rev. Lett.* 111:180603. doi 10.1103/PhysRevLett.111.180603.
- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Horowitz, J. M. and Sandberg, H. 2014. Second-law-like inequalities with information and their interpretations. *New J. Phys.* 16:125007. doi 10.1088/1367-2630/16/12/125007.
- Barato, A. C., Hartich, D. and Seifert, U. 2014. Efficiency of cellular information processing. *New J. Phys.* 16:103024. doi 10.1088/1367-2630/16/10/103024.
- Sandberg, H., Delvenne, J.-C., Newton, N. J. and Mitter, S. K. 2014. Thermodynamic costs in implementing Kalman-Bucy filters. *Proc. Allerton*. doi 10.1109/ALLERTON.2014.7028503.
- Sandberg, H., Delvenne, J.-C., Newton, N. J. and Mitter, S. K. 2014. Maximum work extraction and implementation costs for nonequilibrium Maxwell's demons. *Phys. Rev. E* 90:042119. doi 10.1103/PhysRevE.90.042119.
- Parrondo, J. M. R., Horowitz, J. M. and Sagawa, T. 2015. Thermodynamics of information. *Nat. Phys.* 11:131. doi 10.1038/nphys3230.
- Horowitz, J. M. 2015. Multipartite information flow for multiple Maxwell demons. *J. Stat. Mech.* 2015:P03006. doi 10.1088/1742-5468/2015/03/p03006.
- Barato, A. C. and Seifert, U. 2015. Thermodynamic Uncertainty Relation for Biomolecular Processes. *Phys. Rev. Lett.* 114:158101. doi 10.1103/PhysRevLett.114.158101.
- Gingrich, T. R., Horowitz, J. M., Perunov, N. and England, J. L. 2016. Dissipation Bounds All Steady-State Current Fluctuations. *Phys. Rev. Lett.* 116:120601. doi 10.1103/PhysRevLett.116.120601.
- Hartich, D., Barato, A. C. and Seifert, U. 2016. Sensory capacity: An information theoretical measure of the performance of a sensor. *Phys. Rev. E* 93:022116. doi 10.1103/PhysRevE.93.022116.
- Goldt, S. and Seifert, U. 2017. Stochastic Thermodynamics of Learning. *Phys. Rev. Lett.* 118:010601. doi 10.1103/PhysRevLett.118.010601.
- Still, S. 2020. Thermodynamic Cost and Benefit of Memory. *Phys. Rev. Lett.* 124:050601. doi 10.1103/PhysRevLett.124.050601.
- Riechers, P. M., Boyd, A. B., Wimsatt, G. W. and Crutchfield, J. P. 2020. Balancing error and dissipation in computing. *Phys. Rev. Research* 2:033524. doi 10.1103/PhysRevResearch.2.033524.
- Tatikonda, S., Sahai, A. and Mitter, S. 2004. Stochastic Linear Control Over a Communication Channel. *IEEE Trans. Automat. Control* 49:1549. doi 10.1109/TAC.2004.834430.
- Tatikonda, S. and Mitter, S. 2004. Control Under Communication Constraints. *IEEE Trans. Automat. Control* 49:1056. doi 10.1109/TAC.2004.831187.
- Kostina, V. and Hassibi, B. 2019. Rate-Cost Tradeoffs in Control. *IEEE Trans. Automat. Control* 64:4525. doi 10.1109/TAC.2019.2912256.
- Tanaka, T., Kim, K.-K. K., Parrilo, P. A. and Mitter, S. K. 2017. Semidefinite Programming Approach to Gaussian Sequential Rate-Distortion Trade-Offs. *IEEE Trans. Automat. Control* 62:1896. doi 10.1109/TAC.2016.2601148.
- Duncan, T. E. 1970. On the Calculation of Mutual Information. *SIAM J. Appl. Math.* 19:215. doi 10.1137/0119020.

Already in the repository, and used rather than re-derived: Propositions JP-heat, EQ-heat, and EQ-learn in `theory/GENERALITY_2026-11-22.md`; the telegraph and Ornstein–Uhlenbeck heat infima in `theory/GENERAL_FORM_PHYSICS_2026-11-22.md` and `theory/INFO_PHYSICS_ATTAINABILITY.md`; the drifting-world inflow floors in `theory/THEOREM_P_DRIFT.md`.

## 9. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, or the hypothesis sentence. It does not add a CLAIM_MAP row, and it does not change the status of IP1–IP14, PD1–PD8, or T40, T48, or T49. It does not re-confirm `theory/THEOREM_P_DRIFT.md`. It does not run a lake build or a new numerical check. It does not treat an in-model statement as a fact about a real system. No system has been shown to qualify under THEORY §3.
