# Static bias, metastable retention, and the JP-heat floor

*Monday 23 November 2026 (America/New_York). A follow-up to the general heat-floor attempt, not a change to `THEORY.md` or the hypothesis sentence. Written against `main` `ce6c938`. DOIs below were resolved on the Crossref API the same day (`theory/freeze_or_hold_floor_checks/crossref.out`). A small check script, not a new simulation of a real system. Open-work row T59. T58 is on `main` as of pull request #230 and is not edited here. This text corrects an earlier draft on this branch (`b279ad0`) that an independent review rated not ready: that draft equated the JP-heat learning rate with the gross copy-restoration rate \((r+\Gamma)L(\varepsilon)\). A self-check of the correction, not an independent review of this text.*

Labels follow the repo: **PROVED (in-model)** is a result inside a named class. **KNOWN** is published and credited, only for what that source states. **ELEMENTARY** is a direct consequence of a proved or known inequality, not a new named theorem. **CONJECTURE** is a named bet, not a result. **HYPOTHESIS** is a claim about the world, not a theorem. **OPEN** is not derived. A lower bound is not a derivation of the cost.

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Bottom line

The general heat-floor attempt (`theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`, T57) broke at a frozen world. If the world never mixes, a one-time write can leave a small tracking error at vanishing steady heat. That is not a random gap. It is the freeze corner the theory already has (H9 in [`history/2026-11-18_CURRENT_BRIEF.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-18_CURRENT_BRIEF.md); CT11; `theory/SCALE_ENDS.md`; the frozen class in [`reference/THEORY_v2.0.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/reference/THEORY_v2.0.md)).

This note asks whether thermal escape of the record closes that loophole. It does not, not under the thermodynamic step the repo already uses. Three cases have to be kept apart.

1. *Static bias.* A two-state record held by a static energy bias, with memory rates in local detailed balance, can sit at a finite Boltzmann error in a frozen world. The copy-plus-leak pair is then at equilibrium. The ongoing memory-bath heat is zero. The one-time Landauer write is a finite cost, not a rate. This is T57's loophole, still open.
2. *Metastable retention.* A high barrier in a symmetric well, after a one-time write and with no ongoing drive, holds a small error only for a lifetime of order \(1/\Gamma\), with \(\Gamma=\nu\exp(-\Delta E/kT)\) the high-barrier Kramers rate. That lifetime is a resource. It is not a steady heat floor.
3. *Irreversible refresh, or write and erase.* A protocol that is not in local detailed balance can pay a Landauer cost per reset or an irreversible-lowering work per logical switch. Those costs need their own assumptions. This note states a model term for irreversible lowering and does not prove a general Landauer-per-reset floor.

Under Proposition JP-heat, which requires local detailed balance on the memory rates, the information flow that lower-bounds the memory-bath heat is the *net* flow of memory jumps, \(I_{\mathrm{alt}}=r\,L(\varepsilon)\), with \(L(\varepsilon)=(1-2\varepsilon)\ln((1-\varepsilon)/\varepsilon)\). The leak rate \(\Gamma\) cancels: leak jumps are memory jumps, and they enter the net flow with the opposite sign to the copy. The heat bound in this class is therefore

\[
\dot Q_M\ge kT\,r\,L(\varepsilon).
\]

This is **PROVED (in-model)** for a two-state telegraph world and a two-state memory with local detailed balance, from Proposition JP-heat and the steady-state master equation. It is not claimed to be the weakest such bound outside this class. At \(r>0\) and \(\Gamma=0\) it is the proved telegraph floor (IP3). At \(r=0\) it is zero at every finite error a static bias can hold. A frozen world, in this class, has zero ongoing memory-bath heat at every finite Boltzmann error; the stake term \(w\varepsilon\) remains, and is smallest as \(\varepsilon\to 0\).

The cost of judgment, as a rate, is the heat of remembering plus stake times expected error, subject to the ruin cap. Minimizing the JP-heat bound plus the stake over the Hamming error \(\varepsilon\) is the usual telegraph tradeoff, independent of the barrier. If an irreversible-lowering work \(\chi\Delta E(r+\Gamma)(1-2\varepsilon)\) is added as a model assumption, that work is nonnegative and is minimized at \(\Delta E=0\). The critical-barrier identity of the earlier draft, which treated \(kT(r+\Gamma)L(\varepsilon)\) as the heat, is retracted as a fact about the JP-heat cost.

The reading that the cost of judgment is a face of how physics itself keeps records is a **HYPOTHESIS**, not a result of this note. What the model implies about black holes is stated in §5 and is labeled as following from the model. This note does not derive the area law or the Page curve; those remain inputs.

## 1. The cost, with named terms

The method is the same as everywhere in the theory: write the cost, find its minimum, and read off the design. Whether a real system sits near that minimum is Part 2, and is not decided here.

**World.** A two-state telegraph \(X\in\{0,1\}\), flipping each way at rate \(r\ge 0\). At \(r=0\) the world is frozen. The equilibrium Ornstein–Uhlenbeck world \(dX=-rX\,dt+\sqrt{2rv}\,dW\), of variance \(v\), is used only for the reduction in §3; its \(r=0\) limit is a frozen Gaussian.

**Record.** A two-state memory \(M\in\{0,1\}\) in a symmetric well of barrier \(\Delta E\ge 0\), at temperature \(T\), with attempt frequency \(\nu>0\). The Kramers escape rate is

\[
\Gamma=\nu\exp(-\Delta E/kT),
\]

the high-barrier form (**KNOWN**, Kramers 1940). The hold-side use of this formula at \(\Delta E=0\) is a model extrapolation, not the 1940 high-barrier result. A controlled copy drive of rate \(\mu\ge 0\) flips \(M\) toward \(X\). Two physically different realizations of \(\mu\) must be distinguished: a static energy bias, which keeps the memory rates in local detailed balance, and an irreversible protocol (barrier lowering that is not quasi-static, or a hard reset). Hamming error is \(\varepsilon=P(M\neq X)\). The stake \(w\) converts that error into the currency of the heat.

**Master equation.** By symmetry,

\[
\dot\varepsilon=(r+\Gamma)(1-\varepsilon)-\varepsilon(r+\Gamma+\mu).
\]

In steady state

\[
\varepsilon=\frac{r+\Gamma}{2(r+\Gamma)+\mu},\qquad\mu=\frac{(r+\Gamma)(1-2\varepsilon)}{\varepsilon},
\]

for \(\varepsilon\in(0,1/2]\). These identities are **ELEMENTARY** and are checked by the script.

**Transient destruction, and the net flow that JP-heat bounds.** For a fair stationary bit, the mutual information is \(I=\ln 2-h(\varepsilon)\) nats, with \(h\) the binary entropy in nats. If the copy is off, \(\dot\varepsilon=(r+\Gamma)(1-2\varepsilon)\) and

\[
\dot I\big|_{\mathrm{destroy}}=-(r+\Gamma)L(\varepsilon),\qquad L(\varepsilon)=(1-2\varepsilon)\ln\frac{1-\varepsilon}{\varepsilon}.
\]

That identity is **ELEMENTARY** as a *transient* derivative at \(\mu=0\). It is not the learning rate that Proposition JP-heat compares to the memory-bath heat.

Proposition JP-heat (`theory/GENERALITY_2026-11-22.md`; **KNOWN** for bipartite chains, Horowitz and Esposito 2014; stated and proved in the repo from local detailed balance) requires local detailed balance on the memory rates and bounds the memory-bath heat by the net information flow of memory jumps,

\[
I_{\mathrm{alt}}=\sum\pi\,w\,\ln\frac{\pi(m'\mid x)}{\pi(m\mid x)},\qquad\dot Q_M=\sigma_M+I_{\mathrm{alt}}\ge I_{\mathrm{alt}}.
\]

For the local-detailed-balance rates \(w(E\to C\mid x)=\Gamma+\mu\) and \(w(C\to E\mid x)=\Gamma\), a direct expansion is

\[
I_{\mathrm{alt}}=\bigl[\varepsilon(\Gamma+\mu)-(1-\varepsilon)\Gamma\bigr]\ln\frac{1-\varepsilon}{\varepsilon}.
\]

The bracket equals \(r(1-2\varepsilon)\) by the steady-state identity already displayed, so

\[
I_{\mathrm{alt}}=r\,L(\varepsilon).
\]

The \(\Gamma\) terms cancel. This identification is **PROVED (in-model)** in the present class and is checked by the script, including at the point \((r,\Gamma,\varepsilon)=(0.4,0.25,0.15)\) and at \(r=0\). The heat bound is therefore \(\dot Q_M\ge kT\,r\,L(\varepsilon)\), with units restored. At \(r=0\) the same identity gives \(\varepsilon(\Gamma+\mu)=(1-\varepsilon)\Gamma\): the copy-plus-leak pair is at detailed balance, \(\sigma_M=0\), and \(\dot Q_M=0\). A finite Hamming error is then the Boltzmann error of a static bias.

**Named terms.** The cost of judgment, as a long-run rate plus a one-time write, subject to the ruin cap, is

\[
C=C_{\mathrm{write}}+\tau\bigl(\dot C_{\mathrm{heat}}+\dot C_{\mathrm{barrier}}+w\varepsilon\bigr)
\]

over a horizon \(\tau\), or, as a rate when the cap is slack,

\[
J=\dot Q_M+w\varepsilon.
\]

The named pieces are:

- \(C_{\mathrm{write}}\): the one-time Landauer write, \(kT\) per nat stored. For a full reset of one bit the floor is \(kT\ln 2\). For a binary record left at error \(\varepsilon\) against a fair prior, it is \(kT\bigl(\ln 2-h(\varepsilon)\bigr)\). Amortized over a long horizon this term vanishes as a rate. It does not vanish as a total cost.
- \(\dot C_{\mathrm{heat}}\): the memory-bath heat. Under local detailed balance, JP-heat gives the design-independent bound \(kT\,r\,L(\varepsilon)\) at fixed error, in this class. At \(r=0\) this ongoing piece is zero.
- Metastable retention is not a heat term. In a symmetric well with the drive off, a written record survives for a time of order \(1/\Gamma\). On a horizon \(t\ll 1/\Gamma\) the error can remain small after a one-time write, without a steady heat floor.
- \(\dot C_{\mathrm{barrier}}\): work to control the barrier, when that control is priced. For an equilibrium well under quasi-static, reversible control this term can approach zero (**KNOWN** as a possibility of reversible computation, Bennett 1973, 1982, 2003). Under the irreversible-lowering model used as an optional term below, each logical switch pays \(\Delta E\), so \(\dot C_{\mathrm{barrier}}=\chi\Delta E\,(r+\Gamma)(1-2\varepsilon)\) with \(\chi=1\), at the copy-driven switch rate \(\mu\varepsilon=(r+\Gamma)(1-2\varepsilon)\). The parameter \(\chi\in\{0,1\}\) marks the two assumptions; it is not fitted to a material. This work term is a model assumption. It is not a substitute for JP-heat, and it does not apply as a proved heat if the protocol leaves local detailed balance.
- A Landauer cost per irreversible reset is **OPEN** as a steady floor in this note: JP-heat, as stated, does not cover a non-LDB refresh, and this note does not supply a separate proof.
- \(w\varepsilon\): stake times Hamming error.

Together, as a lower bound on the rate in the local-detailed-balance class, plus the optional work term,

\[
J(\varepsilon,\Delta E)\ge kT\,r\,L(\varepsilon)+\chi\Delta E\bigl(r+\nu e^{-\Delta E/kT}\bigr)(1-2\varepsilon)+w\varepsilon,
\]

with the one-time write standing outside the rate. The heat piece does not contain \(\Gamma\). A lower bound on \(\dot Q_M\) at fixed \(\varepsilon\) is a lower bound on \(J\) at that \(\varepsilon\). The minimum over designs is then at least the minimum of the right-hand side over \(\varepsilon\in(0,1/2]\) and \(\Delta E\ge 0\).

## 2. Prior art: what each source establishes, and what is new

Every DOI in this section was resolved on `api.crossref.org` on 23 November 2026. Nothing below is claimed as new except the in-model composition in §3–§4, and that composition is labeled. The gap each source leaves is stated for that source, not as a criticism of the paper. A repository search was done first; several of these papers are already cited in `theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`, `theory/INFO_PHYSICS.md`, `theory/SCALE_ENDS.md`, `theory/FREEZE_PROCESS_2026-11-21.md`, and `litmap/LITMAP.md`.

**Wheeler (1992),** *Ann. N. Y. Acad. Sci.* 655:349, doi 10.1111/j.1749-6632.1992.tb17083.x, "Recent Thinking about the Nature of the Physical World: It from Bit." A stated program: that physical things may be informational at root. It is **KNOWN** as a program, not as a theorem, and it does not give a heat-versus-error floor or a freeze/hold boundary.

**Landauer (1961),** *IBM J. Res. Dev.* 5:183, doi 10.1147/rd.53.0183. An erasure bound of \(kT\ln 2\) for one bit of a symmetric memory. It is a one-shot, or per-cycle, cost of resetting a memory. It is not a steady learning rate, and it does not mention a tracking error or a Kramers leak.

**Bennett (1973),** *IBM J. Res. Dev.* 17:525, doi 10.1147/rd.176.0525, logical reversibility of computation; **Bennett (1982),** *Int. J. Theor. Phys.* 21:905, doi 10.1007/BF02084158, the review of the thermodynamics of computation, including the cost of error and of memory; **Bennett (2003),** *Stud. Hist. Philos. Mod. Phys.* 34:501, doi 10.1016/S1355-2198(03)00039-X, notes on Landauer's principle, reversible computation, and Maxwell's demon. These establish that logically reversible operations can approach zero dissipation, that irreversible erasure cannot, and that holding a reliable memory is a thermodynamic problem. They do not compose a tracking floor with a Kramers leak, and they do not close T57's loophole at \(r=0\) under local detailed balance.

**Kramers (1940),** *Physica* 7:284, doi 10.1016/S0031-8914(40)90098-2. The escape rate over a barrier in a thermal bath, in the high-barrier form used here. It is a rate, not a cost, and it does not mention information or a stake. The high-barrier scope is the one respected here: use at \(\Delta E=0\) is a model extrapolation.

**Hopfield (1974),** *Proc. Natl. Acad. Sci. U.S.A.* 71:4135, doi 10.1073/pnas.71.10.4135. Kinetic proofreading: a biochemical scheme that spends free energy to buy copying accuracy. It supports the idea that keeping a fact current, or keeping a copy accurate, has an upkeep price. It is not a floor on tracking a telegraph or Ornstein–Uhlenbeck world, and it is not a freeze/hold boundary. The repo already books it that way in `litmap/LITMAP.md`.

**Still, Sivak, Bell, and Crooks (2012),** *Phys. Rev. Lett.* 109:120604, doi 10.1103/PhysRevLett.109.120604, and **Still (2020),** *Phys. Rev. Lett.* 124:050601, doi 10.1103/PhysRevLett.124.050601. Dissipation is bounded by the part of the memory that does not predict, and a later paper prices the cost and benefit of memory in that frame. As the general-floor note already says, those inequalities charge useless memory. They do not force the heat to rise as the tracking error falls, and they do not close the frozen-world loophole by themselves.

**Horowitz and Esposito (2014),** *Phys. Rev. X* 4:031015, doi 10.1103/PhysRevX.4.031015. The bipartite information-flow heat inequality used as JP-heat in the repo. It is the thermodynamic step. It bounds the memory-bath heat by a net information flow. It does not, by itself, turn a tracking error into a positive rate when the world is frozen: at \(r=0\), under local detailed balance, that net flow vanishes.

**Ouldridge, Govern, and ten Wolde (2017),** *Phys. Rev. X* 7:021004, doi 10.1103/PhysRevX.7.021004. Thermodynamic costs of computational copying in biochemical systems. **Lambson, Carlton, and Bokor (2011),** *Phys. Rev. Lett.* 107:010604, doi 10.1103/PhysRevLett.107.010604. Landauer-limit accounting for magnetic memory and nanomagnetic logic, including barriers. **Riechers, Boyd, Wimsatt, and Crutchfield (2020),** *Phys. Rev. Research* 2:033524, doi 10.1103/PhysRevResearch.2.033524. A dissipation–error tradeoff in computing. These are costs of maintaining, copying, or stabilizing bits. None of them writes the GTAO cost, and none of them supplies the net-flow identification \(I_{\mathrm{alt}}=r\,L(\varepsilon)\) used here.

**Bekenstein (1973),** *Phys. Rev. D* 7:2333, doi 10.1103/PhysRevD.7.2333, black-hole entropy; **Bekenstein (1981),** *Phys. Rev. D* 23:287, doi 10.1103/PhysRevD.23.287, the universal entropy-to-energy bound. These are the capacity and energy-per-nat inputs already used in `theory/SCALE_ENDS.md`. They classify how much memory a region can hold. They do not derive a no-anticipation claim, and this note does not re-derive the bound.

**England (2013),** *J. Chem. Phys.* 139:121923, doi 10.1063/1.4818538. A dissipation bound for self-replication. It is the closest Crossref-verified line in this sweep that links a thermodynamic cost to the persistence of organized matter. It does not treat freeze versus hold, it does not close the general-floor loophole, and it does not establish the physics hypothesis in §5.

**What is new here, if anything.** The pieces are known: Landauer for the write, Kramers for the leak as a rate, Hopfield and the memory-cost papers for paying to keep a copy accurate, Horowitz–Esposito and the repo's JP-heat / EQ-heat for the thermodynamic step, the telegraph and Ornstein–Uhlenbeck floors (IP3, IP11), and the freeze/hold band already in CT11 and `theory/FREEZE_PROCESS_2026-11-21.md` (including the known freeze-out criterion, which that note already credits). What this note adds, and only in the named class, is the composition: the cost with those named terms, the identification of the JP-heat flow with \(r\,L(\varepsilon)\) rather than with the gross restoration rate \((r+\Gamma)L(\varepsilon)\), the separation of static bias, metastable retention, and irreversible refresh, the minimum over barrier and refresh design, and the statement that T57's loophole stays open at \(r=0\) under JP-heat. The earlier draft's claim that \(r+\Gamma>0\) was the weakest condition closing that loophole, and the critical-barrier identity built on \(kT(r+\Gamma)L(\varepsilon)\), are retracted. The physics reading in §5 is a hypothesis, not part of that addition.

## 3. The minimum, and what is read off

**Reduction at \(r>0\), \(\Gamma=0\).** The ongoing heat floor is \(kT\,r\,L(\varepsilon)\). That is IP3, **PROVED (in-model)** for the telegraph, with the world's flip rate \(\gamma\) written as \(r\). At \(\varepsilon=0.2\), \(r=1\), \(kT=1\), the infimum is \(0.6\ln 4=0.831776616672\), the same number as in `theory/GENERAL_FORM_PHYSICS_2026-11-22.md`. For an exogenous equilibrium Ornstein–Uhlenbeck signal of rate \(a=r\) and variance \(v\), the proved learning-rate floor at decision error \(\varepsilon\) is the Kalman rate \(r(v-\varepsilon)/\varepsilon\) (IP11 / EQ-learn; T38). This note uses that identity as already proved. It does not add a Kramers leak to the Ornstein–Uhlenbeck class; that extension is **OPEN**.

**Reduction at \(r=0\).** The JP-heat bound is \(0\), at any finite error a static bias can hold. Together with the one-time write \(C_{\mathrm{write}}\), this is a finite write plus vanishing ongoing heat. It is **PROVED (in-model)** in the two-state local-detailed-balance class from Proposition JP-heat and the steady-state identity. An exponentially small *leak rate* at a high barrier is a retention bound, not a substitute heat floor. The loophole of T57, a vanishing ongoing heat at a finite error after a one-time write, remains at \(r=0\).

**Minimum over error, at a given world rate.** When the ruin cap is slack and barrier control is reversible or unpriced (\(\chi=0\)), the rate bound does not depend on \(\Delta E\):

\[
J(\varepsilon)\ge kT\,r\,L(\varepsilon)+w\varepsilon.
\]

The minimum over designs, in this class, is the minimum of the right-hand side over \(\varepsilon\in(0,1/2]\). At \(r=0\) that bound is \(w\varepsilon\), which is smallest as \(\varepsilon\to 0\): a strong static bias, ongoing heat zero, plus a one-time write that approaches \(kT\ln 2\) for a perfect bit. At \(r>0\) the usual telegraph tradeoff applies: \(J\to\infty\) as \(\varepsilon\to 0\), and \(J=w/2\) at \(\varepsilon=1/2\). A numerical grid in the check script, at stake \(w=2\) and \(kT=1\), has the minimizing error small at small \(r\) and approaching \(1/2\) at large \(r\). At large \(r\) and fixed stake, the record does not pay. That qualitative onset is a specialization, to Hamming error on a telegraph, of the same kind of threshold already recorded as CT4 for the first nat on the predictive-information curve. It is not CT4 itself, and it is not a new theorem.

**Barrier and refresh design.** Because the JP-heat piece at fixed \(\varepsilon\) does not depend on \(\Gamma\) or \(\Delta E\), the heat bound does not select a barrier. Any local-detailed-balance pair \((\mu,\Gamma)\) that realizes the minimizing \(\varepsilon\) is equivalent on that bound. Under the irreversible-lowering model (\(\chi=1\)), the extra work \(\Delta E(r+\Gamma)(1-2\varepsilon)\) is zero at \(\Delta E=0\) and strictly positive at every finite \(\Delta E>0\). The minimum over the barrier is therefore at \(\Delta E=0\), for every \(r\ge 0\). (At \(r=0\) the work also tends to zero as \(\Delta E\to\infty\), which is the freeze limit in which there is no leak to correct and no lowering to perform; it does not beat \(\Delta E=0\).) A stationary point of that work term at fixed \(\varepsilon\) can be written \((\Delta E-kT)\Gamma(\Delta E)=r\,kT\) for \(\Delta E>kT\), when it exists. It is not the global minimum, and it is not kept as a design identity. The critical-barrier identity of the earlier draft, \(\bigl(\Delta E+kT[\ln((1-\varepsilon)/\varepsilon)-1]\bigr)\Gamma=r\,kT\), was a calculus fact about the *displayed* objective that had put \(kT(r+\Gamma)L(\varepsilon)\) in the heat. That identity is retracted.

**A rate cap, as a constraint.** If the copy rate cannot exceed a multiple of \(\Gamma\), then for \(r>0\) a large barrier forces \(\varepsilon\to 1/2\): the record cannot track. That statement is **PROVED (in-model)** as a consequence of the master equation plus that rate cap, and it is not a claim that every physical write is so capped. It is a feasibility constraint, not a heat-floor selection of the barrier. The hold-side evaluation of the cap at \(\Delta E=0\) uses the escape formula outside the high-barrier Kramers regime, and is a model extrapolation.

The existing freeze/hold/lookup band (CT11; `theory/FREEZE_PROCESS_2026-11-21.md`) remains the cost-optimal band in the five-term display, with freeze-out at a drift \(q_f=2c/(W\tau^2)\). This note does not replace that band and does not identify a heat-floor barrier with \(q_f\).

## 4. What does, and does not, give a design-independent floor

T57 left \(\Phi\) as the causal learning-rate–distortion function of the world, and noted that a frozen world has \(\Phi(d)=0\) at any error a one-time write can achieve. That statement is correct, and it survives the inclusion of a leaky two-state record under local detailed balance. In this class the design-independent bound on the net flow is

\[
\Phi(\varepsilon)\ge r\,L(\varepsilon)\qquad\text{for }\varepsilon\in(0,1/2],
\]

and \(\dot Q_M\ge kT\,\Phi(\varepsilon)\). The bound is positive at \(r>0\) and \(\varepsilon<1/2\). It is zero at \(r=0\). Leakage of the record does not appear in \(\Phi\), because it cancels in \(I_{\mathrm{alt}}\). The condition that yields this floor is \(r>0\), in this class, under JP-heat. This note does not claim that \(r>0\) is the weakest such condition in every class, and it does not claim that \(r+\Gamma>0\) closes T57's loophole.

A general leak term for other classes, and a Landauer-per-reset floor for a non-LDB refresh, are **OPEN**. This is not a closed-form \(\Phi\) for every adaptive system. It does not supply the missing Fisher, entropy-power, or contraction bound for an arbitrary kernel.

## 5. The physics hypothesis, and black holes

**The physics hypothesis (HYPOTHESIS).** There is a serious line of physics, from Wheeler's "it from bit" through Landauer and Bennett to the information-thermodynamic work above, that treats information and its cost as more basic than the things that carry it. If that line is right, the cost of judgment is not only a rule that adaptive systems happen to follow. It would be a face of how physics itself keeps records. The split that this note actually supports is narrower than a claim that every record has an ongoing heat floor. Holding a static record can be free at equilibrium: a static bias in a frozen world pays no ongoing memory-bath heat, and a metastable well pays a lifetime rather than a rate. What the universe freezes can become structure at vanishing maintenance heat, after a write: the laws and the particles that stay put, and any other record whose barrier, or a conservation law, makes escape negligible on the time of interest. What keeps *changing in the world* has to keep paying. In this class that payment is the JP-heat floor \(kT\,r\,L(\varepsilon)\) at \(r>0\). "Why something rather than nothing" is not closed by that statement. The cost, as written, already assumes a system, a world, a bath, and a temperature. The math can still push on lifetimes of frozen structure, because those are questions about barriers, temperature, and leak rates, but those questions are retention questions, not a steady heat floor.

This remains a **HYPOTHESIS**. This note does not claim to have closed the gap of why there is something at all. England's dissipation bound on self-replication is a related program, not a derivation of the claim in the paragraph above. The hypothesis sentence of the theory is unchanged, and it is still a hypothesis about strongly selected systems.

What would make the hypothesis more testable: a frozen structure whose independently measured barrier and temperature predict its lifetime through a Kramers or Arrhenius rate; a static-bias memory in a frozen setting whose ongoing heat is consistent with zero at a finite Boltzmann error; or a tracker in a changing two-state world whose heat sits at or above \(kT\,r\,L(\varepsilon)\). What could show it wrong, as a reading of physics: a long-lived frozen structure with no barrier, no conservation law, and no other protection, whose persistence is not organized as a stability cost; a static-bias memory that dissipates a positive steady heat at \(r=0\) while remaining in the stated class; or a demonstration that record-keeping costs in physics have no remaining quantitative link to the cost the theory minimizes. A tracker that beats \(kT\,r\,L(\varepsilon)\) in this class would show the floor in §1 wrong, which is a narrower failure than the whole reading.

**Black holes, following from the model.** The rule kept here is the one already used in `theory/SCALE_ENDS.md`: say what the model implies, and label it as following from the model; do not claim to have derived the underlying gravitational or quantum physics. The area law and the Page curve are inputs, not outputs of this note. `theory/SCALE_ENDS.md` is not edited and is not enlarged.

Given that published physics, a black hole sits at the extreme of the frozen class: the most memory physics allows for its size, at the Bekenstein minimum energy per nat, with no tracking of a changing world and with nothing it can act on, so a model would buy it nothing. That classification is already in `theory/SCALE_ENDS.md` §4.2, with the stated conditions (the reading of action, and read latency at least the Page time for the lookup-edge claim). The corrected heat bound fits that classification: a frozen record has vanishing ongoing heat in this class, so a black hole, read as an extreme frozen memory, is not required by this model to pay a maintenance heat to hold what it holds. That is a model implication, not a gravitational result. This note adds one sharper implication, still labeled as following from the model, not as a derived gravitational result: a black hole should show no anticipation, meaning no behavior that responds to what is about to fall in rather than to what already did. That is what "extreme freeze, no tracking" says.

What would make the classification and the anticipation claim more testable: a clean observational contrast between response to already-infallen matter and response to matter that has not yet fallen in. What could show them wrong, as model implications: a reproducible observation that a black hole anticipates an infall, or, as `theory/SCALE_ENDS.md` already records, history-dependent readable hair or echoes, which would also falsify the no-hair physics the classification takes as an input. Post-Page-time decoding cost remains outside the proved scope of that earlier note, and this note does not enlarge that scope.

The question whether the cost of judgment, with the freeze-or-hold split, forces the maximum record a region can hold at bounded ongoing cost to scale with boundary area is taken up in `theory/AREA_LAW_PROBE_2026-11-23.md` (OPEN_WORK T62). The area law and the Page curve remain inputs of the black-hole classification above. This note does not enlarge `theory/SCALE_ENDS.md`.

## 6. What the checks verify

The script `theory/freeze_or_hold_floor_checks/freeze_or_hold_floor_checks.py` checks, as code identities and worked evaluations in this class, the master-equation inversion, the *transient* destruction-rate formula against a finite-difference derivative of \(I\), the JP-heat identification \(I_{\mathrm{alt}}=r\,L(\varepsilon)\) including at \((r,\Gamma,\varepsilon)=(0.4,0.25,0.15)\) and at \(r=0\), detailed balance and vanishing \(I_{\mathrm{alt}}\) at \(r=0\) with \(\Gamma>0\), the telegraph number \(0.6\ln 4=0.831776616672\), the Landauer write, the Kalman-rate identity, that the JP-heat floor \(\Phi(\varepsilon)=r\,L(\varepsilon)\) vanishes at \(r=0\) even when \(\Gamma>0\) and is positive at \(r>0\), that the irreversible-lowering work is minimized at \(\Delta E=0\), and a joint numerical minimum of the corrected bound in which the minimizing barrier is zero at every tested \(r\) and the minimizing error is small at small \(r\) and near \(1/2\) at large \(r\). They are not evidence about a real system, and a green script is not a proof of Proposition JP-heat itself.

## 7. Sources

- Wheeler, J. A. 1992. Recent Thinking about the Nature of the Physical World: It from Bit. *Ann. N. Y. Acad. Sci.* 655:349. doi 10.1111/j.1749-6632.1992.tb17083.x.
- Landauer, R. 1961. Irreversibility and Heat Generation in the Computing Process. *IBM J. Res. Dev.* 5:183. doi 10.1147/rd.53.0183.
- Bennett, C. H. 1973. Logical Reversibility of Computation. *IBM J. Res. Dev.* 17:525. doi 10.1147/rd.176.0525.
- Bennett, C. H. 1982. The thermodynamics of computation—a review. *Int. J. Theor. Phys.* 21:905. doi 10.1007/BF02084158.
- Bennett, C. H. 2003. Notes on Landauer's principle, reversible computation, and Maxwell's Demon. *Stud. Hist. Philos. Mod. Phys.* 34:501. doi 10.1016/S1355-2198(03)00039-X.
- Kramers, H. A. 1940. Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica* 7:284. doi 10.1016/S0031-8914(40)90098-2.
- Hopfield, J. J. 1974. Kinetic Proofreading: A New Mechanism for Reducing Errors in Biosynthetic Processes Requiring High Specificity. *Proc. Natl. Acad. Sci. U.S.A.* 71:4135. doi 10.1073/pnas.71.10.4135.
- Still, S., Sivak, D. A., Bell, A. J. and Crooks, G. E. 2012. Thermodynamics of Prediction. *Phys. Rev. Lett.* 109:120604. doi 10.1103/PhysRevLett.109.120604.
- Still, S. 2020. Thermodynamic Cost and Benefit of Memory. *Phys. Rev. Lett.* 124:050601. doi 10.1103/PhysRevLett.124.050601.
- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Ouldridge, T. E., Govern, C. C. and ten Wolde, P. R. 2017. Thermodynamics of Computational Copying in Biochemical Systems. *Phys. Rev. X* 7:021004. doi 10.1103/PhysRevX.7.021004.
- Lambson, B., Carlton, D. and Bokor, J. 2011. Exploring the Thermodynamic Limits of Computation in Integrated Systems: Magnetic Memory, Nanomagnetic Logic, and the Landauer Limit. *Phys. Rev. Lett.* 107:010604. doi 10.1103/PhysRevLett.107.010604.
- Riechers, P. M., Boyd, A. B., Wimsatt, G. W. and Crutchfield, J. P. 2020. Balancing error and dissipation in computing. *Phys. Rev. Research* 2:033524. doi 10.1103/PhysRevResearch.2.033524.
- Bekenstein, J. D. 1973. Black Holes and Entropy. *Phys. Rev. D* 7:2333. doi 10.1103/PhysRevD.7.2333.
- Bekenstein, J. D. 1981. Universal upper bound on the entropy-to-energy ratio for bounded systems. *Phys. Rev. D* 23:287. doi 10.1103/PhysRevD.23.287.
- England, J. L. 2013. Statistical physics of self-replication. *J. Chem. Phys.* 139:121923. doi 10.1063/1.4818538.

Already in the repository, and used rather than re-derived: Propositions JP-heat and EQ-heat in `theory/GENERALITY_2026-11-22.md`; the telegraph and Ornstein–Uhlenbeck heat infima in `theory/GENERAL_FORM_PHYSICS_2026-11-22.md` and `theory/INFO_PHYSICS_ATTAINABILITY.md`; the general-floor attempt and its loophole in `theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`; the freeze/hold band in CT11 and `theory/FREEZE_PROCESS_2026-11-21.md`; the scale-end classification of black holes in `theory/SCALE_ENDS.md`. The thermodynamic lift of the drifting information floor (T58) is `theory/DRIFT_HEAT_LIFT_2026-11-23.md` and is not edited here.

## 8. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, or the hypothesis sentence. It does not add a CLAIM_MAP row, and it does not change the status of IP3, IP11, T40, T48, T49, T57, or T58. It does not edit the T58 files. It does not replace CT11. It does not prove a closed-form floor for every adaptive system, and it does not treat the physics hypothesis or the black-hole anticipation claim as theorems. It does not treat an in-model statement as a fact about a real system. It does not claim to close T57's loophole. No system has been shown to qualify under THEORY §3.
