# Non-Gaussian heat floors: heavy tails, switching worlds, and rare shocks

*Monday 23 November 2026 (America/New_York). Open-work row T49 (priority 2). Written against `main` `4594eef` (after PR #235, T61). A follow-up to the floor notes T57–T61, not a change to `THEORY.md`, `CORE.md`, or the hypothesis sentence. DOIs below were resolved on the Crossref API the same day (`theory/non_gaussian_floor_checks/crossref.out`). The check script is `theory/non_gaussian_floor_checks/non_gaussian_floor_checks.py` (quadratures, code identities, and exact steady states of finite bipartite chains; not a simulation of a real system). Independently reviewed on PR #238; the reviewer's text and label fixes are applied. No proved bracket changed; the rounded gap constant 3.003 was corrected to \(3.0033+\varepsilon/4v\).*

Labels follow the repo: **PROVED (in-model)** is a result inside a named class. **KNOWN** is published and credited, only for what that source states. **ELEMENTARY** is a direct consequence of a proved or known inequality, not a new named theorem. **NUMERICAL** is an in-model evaluation by the script. **CONJECTURE** is a named bet. **OPEN** is not derived. A lower bound is not a derivation of the cost.

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Bottom line

The proved floors so far covered the Ornstein–Uhlenbeck (OU) world, one-dimensional equilibrium diffusions (Proposition EQ-learn, `theory/GENERALITY_2026-11-22.md` §1.3), the telegraph and finite-state jump worlds (T59, T60), a drifting random walk (T58), and worlds the memory steers (T61). This note carries the method to three classes beyond them. In each class the world is exogenous, the memory is bipartite, and the thermodynamic step \(\dot Q_M\ge kT\,\dot I_M\) is the one already in the repo (JP-heat, EQ-heat; Horowitz and Esposito 2014). The new work is on the informational side: an exact expression for the rate at which the world destroys what the memory holds, a design-independent lower bound on it at fixed error, and a memory that comes within a stated constant of that bound.

| Class | Floor on \(\dot Q_M/kT\) at mean squared error \(\varepsilon\) | Memory that nearly attains it | Gap | Status |
|---|---|---|---|---|
| **A. Heavy-tailed or any smooth stationary distribution, diffusive noise \(D\)** | \(D\,(1/\varepsilon-\mathcal I(\pi))\) | fast Gaussian copy | at most \(D\,\mathcal I(\pi)\), uniformly | PROVED (in-model); equilibrium case already EQ-learn |
| **B. Volatility-switching (regime) world** | \(\sum_s p_s D_s(1/\varepsilon_s-\mathcal I_s)\) | regime-tuned fast copy, \(\varepsilon_s\propto\sqrt{D_s}\) | \(\sum_s p_sD_s\mathcal I_s\) plus a stake-independent switching surcharge | PROVED (in-model); fast-limit heat NUMERICAL |
| **C. Rare reset shocks at rate \(\lambda\)** | \(\lambda\bigl[\tfrac32\ln(v/\varepsilon)-\gamma_E-\ln 2\bigr]\) (Gaussian landing distribution) | "core plus reserve" memory that keeps a small uncommitted share \(\delta=\varepsilon/4v\) | at most \((3.0033+\varepsilon/4v)\,\lambda\) nats per unit time | PROVED (in-model); fast-limit heat NUMERICAL |

Four read-offs follow, each inside its class.

1. **The floor's shape is set by how the world moves, not by its tails.** Continuous (diffusive) motion forces a floor that grows like \(1/\varepsilon\). Jumps force one that grows like \(\ln(1/\varepsilon)\), as the telegraph already did. Tail shape enters only through a bounded credit \(kT D\,\mathcal I(\pi)\) or through two constants \(h(\pi)\) and \(\kappa_\pi\), all finite for a Cauchy world.
2. **The minimum cost scales with the stake as \(2\sqrt{kTDw}\) in a diffusive world and as \(\tfrac32 kT\lambda\ln(vw/kT\lambda)\) in a reset-shock world.** At high stakes, tracking a shock world is far cheaper than tracking a diffusing one at the same decorrelation rate. Between shocks the world is frozen, and a frozen record is free (T59).
3. **In a shock world a light-tailed memory is the wrong design.** A Gaussian copy pays \(\lambda v/\varepsilon\), against a floor of order \(\lambda\ln(v/\varepsilon)\). Under heavy-tailed (\(\alpha\)-stable) shocks it pays infinite heat, while a memory with heavy-tailed conditionals pays a finite rate. The design the cost selects never fully commits: it keeps a reserve of prior mass of size \(\varepsilon/4v\).
4. **A regime-aware memory loosens in volatile regimes and tightens in calm ones,** with \(\varepsilon_s\propto\sqrt{D_s}\). Because the minimum is concave in volatility, it pays less than the floor of a constant world with the same mean volatility, once the stake passes an explicit threshold (§4.4).

Each class carries a ruin cap. In class C it gives a proved per-shock floor of \(\mathrm{kl}(1-\beta_b\,\|\,\eta)\approx(1-\beta_b)\ln(1/\eta)\) nats, so the price of ruin protection there is logarithmic. In classes A and B a ruin cap on a tail event is **OPEN**: Van Trees bounds a mean square, not a tail.

What stays open: a tight constant for local (non-reset) shocks; an attaining memory under MSE for infinite-variance reset worlds; hidden-regime tracking when the memory cannot read the regime directly; losses other than mean square in classes A–C; a ruin-capped floor in the diffusive classes; and every question about a world the memory moves (T61). §8 bears on T50, and does not claim it.

## 1. The cost, with named terms

The method is the same as everywhere in the theory: write the cost, find its minimum, read off the design. Whether a real system sits near that minimum is Part 2, and is not decided here.

\[
J=\dot Q_M+w\,\mathbb E[\ell]\qquad\text{subject to}\qquad P(\mathrm{ruin})\le\eta .
\]

- \(\dot Q_M\) is the long-run energy flow into the bath that implements the memory's transitions. Under local detailed balance (jump memory) or the Einstein relation (additive-noise diffusion memory), \(\dot Q_M\ge kT\,\dot I_M\), where \(\dot I_M\) is the net information flow (learning rate) of the memory's own transitions. This is **KNOWN** for bipartite jump processes (Horowitz and Esposito 2014; Barato, Hartich, and Seifert 2014) and **PROVED (in-model)** in the repo for additive-noise diffusions (EQ-heat).
- \(\ell=(X-\hat x(M))^2\) is the squared error of an estimate made from the current memory. \(\varepsilon=\mathbb E[\ell]\). The Bayes estimate gives the smallest \(\varepsilon\). Every floor below holds for any estimator.
- \(w\) converts error into the currency of the heat. Temperature does not set it.
- The ruin cap \(\eta\) stays outside the sum. Here ruin is the stationary probability that the error exceeds a margin \(b\): \(P(|X-\hat x(M)|>b)\le\eta\). A ruin event over a whole horizon is a different object and is **OPEN**.

**Assumptions used throughout.** (S1) The world \(X\) is exogenous: its dynamics do not depend on \(M\). (S2) Memory and world do not jump together, and their noises are independent. (S3) Steady state, so the world-side and memory-side information flows cancel, \(\dot I_M=-\dot I_X\). (S4) Regularity: densities positive and smooth where differentiated, and boundary terms vanish, as for A-R in `theory/INFO_PHYSICS_ATTAINABILITY.md`. A lower bound \(\varphi(\varepsilon)\) on \(\dot I_M\) gives \(J\ge kT\varphi(\varepsilon)+w\varepsilon\), and the minimum over designs is at least the minimum of that over \(\varepsilon\).

## 2. Prior art: what each source establishes, and what is new

The repository was searched first (`rg` for Van Trees, Fisher information, lautum, Bretagnolle, Donsker, regime switching, hidden Markov, shot noise, Lévy, reset). The Fisher-information form of the learning rate in a one-dimensional **equilibrium** diffusion, and its bound \(D(1/\varepsilon-\mathcal I(p_X))\), are already Proposition EQ-learn in `theory/GENERALITY_2026-11-22.md` §1.3. They are used and credited, not re-claimed. No repo file treats a switching or shock world as a heat floor.

- **Horowitz and Esposito (2014),** doi 10.1103/PhysRevX.4.031015, and **Horowitz (2015),** doi 10.1088/1742-5468/2015/03/p03006: the bipartite information-flow split and \(\dot Q_M\ge kT\dot I_M\). No tracking error, and no evaluation of the flow at fixed error.
- **Barato, Hartich, and Seifert (2014),** doi 10.1088/1367-2630/16/10/103024: the learning rate is at most the subsystem's entropy production, and the stationary identity \(l_y=h_x\) (learning by the memory equals destruction by the world). Every class below uses that identity. **Hartich, Barato, and Seifert (2016),** doi 10.1103/PhysRevE.93.022116: sensory capacity. **Brittain, Jones, and Ouldridge (2017),** doi 10.1088/1742-5468/aa71d4: what the learning rate does and does not measure.
- **Still, Sivak, Bell, and Crooks (2012),** doi 10.1103/PhysRevLett.109.120604: dissipation bounded by non-predictive memory. It charges useless memory. It does not force heat to rise as error falls.
- **Sandberg, Delvenne, Newton, and Mitter (2014),** doi 10.1109/allerton.2014.7028503: thermodynamic costs of Kalman–Bucy filters, the source of the factor-two accounting in T58. Gaussian and linear only.
- **Van Trees (1968; Wiley reprint 2001),** doi 10.1002/0471221082, and **Gill and Levit (1995),** doi 10.2307/3318681: the Bayesian Cramér–Rao (Van Trees) inequality \(\varepsilon\ge1/(\mathbb E[F]+\mathcal I(\pi))\). **KNOWN.** **Stam (1959),** doi 10.1016/S0019-9958(59)90348-1: the de Bruijn identity and \(\mathcal I\cdot N\ge1\) (entropy power \(N\)), so among distributions of a given variance the Gaussian has the smallest Fisher information (this also follows from Cramér–Rao, \(\mathcal I\,\mathrm{Var}\ge1\)).
- **Palomar and Verdú (2008),** doi 10.1109/TIT.2007.915715: lautum information \(L(X;M)=D(P_X\otimes P_M\,\|\,P_{XM})\). **Donsker and Varadhan (1975),** doi 10.1002/cpa.3160280102: the variational formula for relative entropy. **Bretagnolle and Huber (1979),** doi 10.1007/BF00535278: \(1-\mathrm{TV}\ge\tfrac12e^{-D}\). **Cover and Thomas,** doi 10.1002/047174882X: rate–distortion and the Shannon lower bound. All **KNOWN**.
- **Esposito and Van den Broeck (2011),** doi 10.1209/0295-5075/95/40004: the entropy produced by relaxation to equilibrium is the initial relative entropy. Used for the heat of a fast memory after a shock.
- **Nicoletti and Busiello (2021, 2022),** doi 10.1103/PhysRevLett.127.228301 and 10.1103/PhysRevE.106.014153: mutual information in systems driven by a switching environment, including switching diffusivities. They bound and decompose the information. They do not give a heat floor at fixed error.
- **Wonham (1964),** doi 10.1137/0302028: the optimal filter for a Markov regime in noise. A filter, not a heat bound. **Hamilton (1989),** doi 10.2307/1912559, and **Barndorff-Nielsen and Shephard (2001),** doi 10.1111/1467-9868.00282: regime-switching and Lévy-driven (non-Gaussian OU) world models, credited as the classes' origin. Neither has thermodynamics.
- The Cauchy relative-entropy closed form \(D(\mathrm{Cauchy}(0,s)\|\mathrm{Cauchy}(z,s))=\ln(1+z^2/4s^2)\) is in Chyzak and Nielsen (2019, arXiv:1905.10965, no DOI). The script checks it by quadrature (C7).

**What is new here, if anything.** The thermodynamic step and all the inequalities above are prior art. The additions are their in-model compositions: the destruction identity for non-equilibrium, switching, and jump worlds (§3); the uniform gap \(D\,\mathcal I(\pi)\) and the cost sandwich in class A (§3); the per-regime floor and regime-tuned design in class B (§4); and, in class C, the exact \(\lambda(I+L)\) identity, the \(\tfrac32\ln\) floor, the core-plus-reserve design within \((3.0033+\varepsilon/4v)\lambda\), and the ruin floor (§5). The search can miss a paper. This note does not claim that no such composition is in print.

## 3. Class A: heavy-tailed and other non-Gaussian stationary distributions

**World.** \(dX=f(X)\,dt+\sqrt{2D}\,dW\), with \(D>0\) and any smooth drift \(f\). The stationary density \(\pi\) may have heavy tails: Student-\(t\), Cauchy, or a double well. Detailed balance is **not** assumed. The world's Fisher information is \(\mathcal I(\pi)=\mathbb E[(\partial_x\ln\pi)^2]\). For Student-\(t\) with \(\nu\) degrees of freedom and scale \(s\), \(\mathcal I=(\nu+1)/((\nu+3)s^2)\). That is finite for every \(\nu>0\), including the Cauchy (\(\nu=1\), \(\mathcal I=1/2s^2\)), whose variance is infinite (check A1).

**A1. Destruction identity, any drift (PROVED, in-model; ELEMENTARY).** For any exogenous additive-noise world and any regular channel \(p(m\mid x)\), stationary or not,

\[
\dot I_X=\int J_X\,\partial_x\ln p(m\mid x)=-D\,\mathbb E\bigl[(\partial_x\ln p(M\mid X))^2\bigr].
\]

*Proof.* \(J_X=p(x,m)\bigl[v(x)-D\,\partial_x\ln p(m\mid x)\bigr]\), with \(v=f-D\partial_x\ln p(x)\) the world's own mean velocity, and \(v\) does not depend on \(m\). The \(v\) term integrates to \(\int p(x)\,v(x)\,\partial_x\!\int p(m\mid x)\,dm\,dx=0\). ∎ In steady state, \(\dot I_M=D\,\mathbb E[F]\), where \(F\) is the channel's Fisher information about \(x\). With state-dependent noise \(D(x)\) the same algebra gives \(\mathbb E[D(X)F]\). In \(d\) dimensions it gives \(\mathbb E[\nabla\ln p^{\top}D\,\nabla\ln p]\). Since \(\mathbb E[F]=\mathbb E[\mathcal I(X\mid M)]-\mathcal I(\pi)\), this is the de Bruijn identity (Stam 1959) for \(h(X)-h(X\mid M)\) under the noise. In one-dimensional equilibrium this is EQ-learn, rewritten with the channel score. The new part is that the drift term vanishes without detailed balance (check A3: four random non-equilibrium drifts and marginals, relative error at most \(2.4\times10^{-4}\) on the grid).

**A2. Floor (PROVED, in-model).** By Van Trees, \(\mathbb E[F]\ge1/\varepsilon-\mathcal I(\pi)\), so

\[
\dot Q_M\ \ge\ kT\,D\,\Bigl(\frac1\varepsilon-\mathcal I(\pi)\Bigr)_+ .
\]

In \(d\) dimensions, \(\mathbb E[F]\succeq\Sigma_\varepsilon^{-1}-\mathcal I(\pi)\) in the Loewner order gives \(\dot Q_M\ge kT\,[\mathrm{tr}(D\Sigma_\varepsilon^{-1})-\mathrm{tr}(D\,\mathcal I(\pi))]\). Heavy tails need only \(x\,\pi(x)\,p(m\mid x)\to0\) at infinity, which holds for the Cauchy. Check A2 runs 36 cases (Gaussian, Student-\(t\) with \(\nu=2\) and \(\nu=3\), a double well; linear, wiggly, and saturating channels; three noise levels). All satisfy the floor, and the Gaussian world with a linear channel meets it with equality, as Van Trees predicts.

**A3. A memory within \(kT D\,\mathcal I(\pi)\) of the floor (PROVED, in-model).** Take an Einstein spring: \(dM=-\gamma(M-X)\,dt+\sqrt{2\gamma\sigma^2}\,dW_M\), with potential \(kT(m-x)^2/2\sigma^2\), and write \(Y=M-X\). Two exact steady-state identities hold for any drift \(f\) and any \(\gamma\). They follow from Itô's formula on \(Y^2\) and on \(Y f(X)\):

\[
\dot Q_M=\frac{kT}{\sigma^2}\bigl(D-\mathbb E[Yf(X)]\bigr),\qquad \mathbb E[Y^2]=\sigma^2+\frac{D-\mathbb E[Yf(X)]}{\gamma},
\]

\[
\gamma\,\mathbb E[Yf]=\mathbb E[Y(ff'+Df'')]-\mathbb E[f^2]-2D\,\mathbb E[f'] .
\]

When \(\mathbb E[f^2]\), \(\mathbb E[f']\), and \(\mathbb E[(ff'+Df'')^2]\) are finite (true for Student-\(t\), including the Cauchy, whose drift is bounded), Cauchy–Schwarz gives \(\mathbb E[Yf]=O(1/\gamma)\). So \(\dot Q_M\to kT D/\sigma^2\), and the error of the estimate \(\hat x=M\) tends to \(\sigma^2\). The Bayes error \(\varepsilon\) is at most that. Then \(\dot Q_M/kT-D(1/\varepsilon-\mathcal I)\le D\,\mathcal I(\pi)\), because \(1/\varepsilon\ge1/\sigma^2\). The gap is uniform in \(\varepsilon\), so the ratio of heat to floor tends to 1 as \(\varepsilon\to0\). Check A2b confirms \(0\le D/\sigma^2-D(1/\varepsilon-\mathcal I)\le D\,\mathcal I\) on every world. Check A4 computes the exact steady state of a bipartite lattice chain (Student-\(t\), \(\nu=3\), with a spring memory). It finds \(Q\ge I_{\mathrm{alt}}\), \(I_{\mathrm{alt}}\) above the floor, and \(Q/(D/\sigma^2)=0.884,\ 0.982,\ 0.993\) at \(\gamma=5,50,500\).

**A4. The minimum (PROVED, in-model: a sandwich).** Minimizing the floor plus stake, and then the spring design over \(\sigma\):

\[
2\sqrt{kTDw}-kTD\,\mathcal I(\pi)\ \le\ J^*\ \le\ \min\bigl(2\sqrt{kTDw},\ w\,\mathrm{Var}(\pi)\bigr),
\]

The lower bound holds when \(w\ge kTD\,\mathcal I^2\). Below that it is \(w/\mathcal I\). On OU (\(\mathcal I=1/v\), \(D=av\)) the lower bound is the known minimum \(2\sqrt{kTavw}-kTa\) (check A5). The minimizing error of the floor is \(\varepsilon^*=\sqrt{kTD/w}\).

**Design read-off.** At high stakes the cost and the chosen error are set by the world's noise intensity \(D\) alone. The shape of the stationary distribution, heavy tails included, shifts the minimum by at most \(kTD\,\mathcal I(\pi)\). Since \(\mathcal I\,\mathrm{Var}\ge1\), with equality only for the Gaussian (Stam), the Gaussian world has the highest floor among distributions of a given variance and \(D\). An infinite-variance world has no blind regime: the blind cost \(w\,\mathrm{Var}\) is infinite, while tracking costs at most \(2\sqrt{kTDw}\). So at every positive stake the minimum tracks (Cauchy at \(kT=D=1\), \(w=10\): \(J^*\in[5.82,\,6.32]\)).

**Scope.** One exogenous additive-noise diffusion world, a bipartite memory, mean-squared error, steady state, and the regularity of (S4). The thermodynamic step is EQ-heat or JP-heat. **Measurements:** \(D\), \(\mathcal I(\pi)\) (from the stationary distribution), \(w\), and \(kT\). Whether a real tracker sits near \(\varepsilon^*\) is Part 2.

## 4. Class B: regime-switching (volatility-switching) worlds

**World.** A regime \(S\) jumps between finite states at rates \(r_{ss'}\). Given \(S=s\), \(dX=f_s(X)\,dt+\sqrt{2D_s}\,dW\). Regimes may switch the drift (mean shifts), the volatility \(D_s\), or both. The model follows Hamilton (1989), in continuous time. Write \(p_s\) for the regime distribution, \(\pi_s=p(x\mid s)\), and \(\mathcal I_s=\mathcal I(\pi_s)\).

**B1. Hybrid destruction identity (PROVED, in-model).** In steady state,

\[
\dot I_M=\sum_s p_s D_s\,\mathbb E\bigl[(\partial_x\ln p(M\mid s,X))^2\mid s\bigr]+\sum_{s\neq s'}\int p(s,x)\,r_{ss'}(x)\,D_{\mathrm{KL}}\bigl(p(\cdot\mid s,x)\,\|\,p(\cdot\mid s',x)\bigr)\,dx .
\]

The diffusive part is A1 within each regime, and the drift term vanishes for the same reason. The switching part is the jump form of the Barato–Hartich–Seifert destruction (T60 §3). Check B3 computes the exact steady state of a bipartite chain (two regimes, a lattice world, a spring memory with regime-tuned stiffness): memory learning rate equals diffusive part plus switching part to machine precision, at \(\gamma=20\) and \(400\).

**B2. Floor (PROVED, in-model).** Drop the nonnegative switching part, and apply Van Trees within each regime, with prior \(\pi_s\), to \(\varepsilon_s=\mathbb E[\ell\mid S=s]\). The estimate may use \(M\) only.

\[
\dot Q_M\ \ge\ kT\sum_s p_s D_s\Bigl(\frac1{\varepsilon_s}-\mathcal I_s\Bigr)_+,\qquad
J^*\ \ge\ \sum_s p_s\bigl[2\sqrt{kTD_sw}-kTD_s\mathcal I_s\bigr]
\]

The second bound holds when every regime is at high stake, \(w\ge kTD_s\mathcal I_s^2\). This holds for regime-blind and regime-aware memories alike. Check B2 covers four tuned and blind copies, with Bayes estimates from \(M\) only.

**B3. Regime-tuned design (PROVED, in-model, for the learning rate; heat NUMERICAL).** A fast copy whose width follows the regime, \(p(m\mid s,x)=\mathcal N(x,\sigma_s^2)\), has exactly

\[
\dot I_M=\sum_s p_s\frac{D_s}{\sigma_s^2}+\sum_{s\neq s'}p_s r_{ss'}\,\tfrac12\Bigl(\rho_{ss'}-1-\ln\rho_{ss'}\Bigr),\qquad \rho_{ss'}=\sigma_s^2/\sigma_{s'}^2 ,
\]

and error \(\varepsilon_s\le\sigma_s^2\) from \(\hat x=M\). The choice \(\sigma_s^2=\sqrt{kTD_s/w}\) gives \(J\le2\sqrt{kTw}\sum_sp_s\sqrt{D_s}+kT\,\Sigma_{\mathrm{sw}}\). The switching surcharge \(\Sigma_{\mathrm{sw}}\) uses \(\rho=\sqrt{D_s/D_{s'}}\), so it **does not depend on the stake**. The floor and this design differ by at most \(kT\sum_sp_sD_s\mathcal I_s+kT\Sigma_{\mathrm{sw}}\). In the fast-relaxation limit, a fast memory's heat equals \(kT\dot I_M\): A3 gives this within each regime, and the relaxation heat of each switch averages to \(kT\) times the switch's relative entropy, because the entropy terms cancel in stationarity. The script checks this on the exact chain rather than proving it at finite \(\gamma\): \(Q=4.320\) against the fast-limit value \(4.307\) at \(\gamma=400\) (B3c).

**B4. Regime awareness beats a constant world (PROVED, in-model, with an explicit threshold, given the fast-limit heat of B3, which is NUMERICAL).** Compare a constant OU world with the same mean volatility \(\bar D=\sum_sp_sD_s\) and stationary Fisher information \(\mathcal I_c\), at a stake where its floor formula applies (\(w\ge kT\bar D\,\mathcal I_c^2\)). By concavity of \(\sqrt{\cdot}\), \(\sum_sp_s\sqrt{D_s}<\sqrt{\bar D}\) whenever the \(D_s\) differ. The tuned design's cost is below the constant world's floor \(2\sqrt{kT\bar Dw}-kT\bar D\,\mathcal I_c\) as soon as

\[
w>w_{\mathrm{thr}}=\Bigl(\frac{kT(\Sigma_{\mathrm{sw}}+\bar D\,\mathcal I_c)}{2\sqrt{kT}\,(\sqrt{\bar D}-\sum_sp_s\sqrt{D_s})}\Bigr)^2 .
\]

In check B4 (\(D_s=0.25,4\); rates \(0.3,0.6\), so \(p_s=\tfrac23,\tfrac13\), \(\bar D=1.5\), \(\sum_sp_s\sqrt{D_s}=1\), \(\Sigma_{\mathrm{sw}}=0.225\); constant world with \(\mathcal I_c=2/3\), that is OU of variance 1.5), \(w_{\mathrm{thr}}=7.43\). At \(4w_{\mathrm{thr}}\) the design costs \(11.13\), below the constant-world floor of \(12.35\).

**Design read-off.** Track the regime, and set the error per regime as \(\varepsilon_s=\sqrt{kTD_s/w}\): looser in volatile regimes, tighter in calm ones. Reading the regime costs a fixed surcharge per switch. That surcharge is the relative entropy between two Gaussians of width ratio \((D_s/D_{s'})^{1/4}\), so it is worth paying above an explicit stake. Mean shifts between regimes enter only through \(\mathcal I_s\) and the switching part.

**Scope and open.** Exogenous regimes and world, mean-squared error on \(X\). The memory may read the regime directly. **OPEN:** the regime-label task (0-1 loss on \(S\)) when the memory sees the regime only through \(X\). Then \(X\) itself carries a record of \(S\), and neither T60's bounds nor the floor above apply as stated. **Measurements:** \(D_s\), \(r_{ss'}\), \(\mathcal I_s\), \(w\), and \(kT\).

## 5. Class C: rare shocks

### 5.1 Reset shocks

**World.** At rate \(\lambda\), \(X\) is replaced by a fresh draw from a landing distribution \(\pi\). Between shocks it is frozen. This is the jump-world extreme, and the frozen world of T59 is \(\lambda\to0\).

**C1. Exact identity (PROVED, in-model; ELEMENTARY).** By the jump form of the destruction identity, with one-way flux \(\pi(x)\lambda\pi(x')\),

\[
\dot I_M=\lambda\,\mathbb E_{X,X'\sim\pi\otimes\pi}\,D_{\mathrm{KL}}(p_X\|p_{X'})=\lambda\bigl[I(X;M)+L(X;M)\bigr],
\]

where \(L\) is the lautum information (Palomar and Verdú). For a Gaussian copy in a Gaussian world, \(I+L=v/\sigma^2\) exactly (check C1).

**C2. Floor (PROVED, in-model).** \(I\ge R_\pi(\varepsilon)\ge h(\pi)-\tfrac12\ln(2\pi e\varepsilon)\) (rate–distortion and the Shannon lower bound). Under the product distribution \(P_X\otimes P_M\) the estimate is independent of \(X\). Donsker–Varadhan with test function \(\ln(X-\hat x)^2\) then gives \(L\ge\kappa_\pi-\ln\varepsilon\), where \(\kappa_\pi=\inf_c\mathbb E_\pi\ln(X-c)^2\). Together:

\[
\dot Q_M\ \ge\ kT\lambda\Bigl[h(\pi)+\kappa_\pi-\tfrac12\ln(2\pi e)-\tfrac32\ln\varepsilon\Bigr].
\]

For a Gaussian landing distribution of variance \(v\), \(\kappa=\ln v-\gamma_E-\ln2\), and the floor is \(kT\lambda[\tfrac32\ln(v/\varepsilon)-1.2704]\) (check C2). For a Cauchy landing distribution of scale \(s\), with infinite variance, \(h=\ln4\pi s\) and \(\kappa=2\ln s\), and the floor is \(kT\lambda[\tfrac32\ln(s^2/\varepsilon)+1.1121]\). That is finite. Check C3 covers 17 channels (Gaussian, Student-\(t\), Laplace, core-plus-reserve): each part of the bound holds, and no channel comes within 1.27 nats of the floor.

**C3. Core-plus-reserve design within \((3.0033+\varepsilon/4v)\lambda\) (PROVED, in-model).** Let \(p_x=(1-\delta)\,\mathcal N(x,\sigma^2)+\delta\,\pi\). This is a mostly precise memory that keeps a share \(\delta\) of uncommitted prior mass. Since \(p_{x'}\ge\delta\pi\), \(D(p_x\|p_{x'})\le D(p_x\|\pi)+\ln(1/\delta)\). Convexity then gives \(I+L\le\tfrac12\ln(v/\sigma^2)+\sigma^2/2v+\ln(1/\delta)\) for a Gaussian \(\pi\). The estimate \(\hat x=M\) has error at most \(\sigma^2+2\delta v\). With \(\sigma^2=\varepsilon/2\) and \(\delta=\varepsilon/4v\), the error is at most \(\varepsilon\), and

\[
\Phi_{\mathrm{reset}}(\varepsilon)\ \in\ \lambda\Bigl[\tfrac32\ln\tfrac v\varepsilon-1.2704,\ \ \tfrac32\ln\tfrac v\varepsilon+1.7329+\tfrac{\varepsilon}{4v}\Bigr].
\]

The leading coefficient \(\tfrac32\) is tight. Check C4 finds gaps of 1.39–2.27 nats for \(\varepsilon\) from 0.3 down to 0.003, under the proved gap \(\gamma_E+\tfrac72\ln2+\varepsilon/4v\approx3.0032+\varepsilon/4v\). A fast memory realizes this at heat \(kT\dot I_M\). After each shock it relaxes in the landscape \(-kT\ln p_{x'}\). The heat released is \(kT[D(p_x\|p_{x'})+H(p_x)-H(p_{x'})]\) (Esposito and Van den Broeck), and the entropy terms cancel on average because \(x\) and \(x'\) share the distribution \(\pi\). Check C5 computes the exact steady state of a chain: \(I_{\mathrm{alt}}\) equals the world-side destruction, \(Q\ge I_{\mathrm{alt}}\), and \(Q/(\lambda\,\mathbb E\,D_{\mathrm{KL}})=0.715,\ 0.958,\ 0.9955\) at \(\gamma/\lambda=3,30,300\). So the fast-limit heat is NUMERICAL here, not proved at finite \(\gamma\). The relaxation must also be fast against \(\lambda v/\varepsilon\), or the transient error after each shock adds to \(\varepsilon\).

**C4. Minimum (PROVED, in-model: a bracket).** Minimizing the bracket plus \(w\varepsilon\) puts the error at \(\varepsilon^*=\tfrac32kT\lambda/w\) and gives

\[
J^*=\tfrac32kT\lambda\ln\frac{vw}{kT\lambda}+kT\lambda\,c,\qquad c\in[-0.379,\ 2.67]
\]

Here \(u=vw/kT\lambda\). The lower end \(\tfrac32\ln\tfrac23+\tfrac32-\gamma_E-\ln2\approx-0.3786\) holds for every \(u\). The upper end is \(\tfrac32\ln\tfrac23+\tfrac32+\tfrac52\ln2+3/(8u)\approx2.6247+3/(8u)\), so \(c\le2.67\) once \(u\ge8.3\). The upper end rests on the fast-limit heat of C3, which is NUMERICAL. Check C9 evaluates the bracket for \(u\) from 10 to \(10^4\). The cost grows only logarithmically in the stake. In OU and class A it grows as \(\sqrt w\).

**C5. Ruin cap (PROVED, in-model).** Data processing on the ruin indicator gives \(L\ge\mathrm{kl}(1-\beta_b\,\|\,\eta)\), with \(\beta_b=\sup_cP_\pi(|X-c|\le b)\), whenever \(\eta<1-\beta_b\) (under the product law the ruin probability is at least \(1-\beta_b\), and \(\mathrm{kl}(p\|q)\) rises in \(p\) and falls in \(q\) for \(q<p\)). So

\[
\dot Q_M\ \ge\ kT\lambda\Bigl[R_\pi(\varepsilon)+\max\bigl(\kappa_\pi-\ln\varepsilon,\ \mathrm{kl}(1-\beta_b\|\eta)\bigr)\Bigr].
\]

Check C6 confirms this on 51 cases. Tightening the cap from \(\eta\) to \(\eta/10\) costs about \(kT\lambda(1-\beta_b)\ln10\) more per unit time. With a ruin cap, the core-plus-reserve design needs \(\delta\lesssim\eta\), which gives coefficient 1 against the floor's \(1-\beta_b\). The tight ruin coefficient is **OPEN**.

### 5.2 Local shocks and heavy-tailed noise

**World.** Jumps \(x\to x+z\) at rate \(\nu(dz)\) (compound Poisson, or Lévy-driven OU as in Barndorff-Nielsen and Shephard), optionally plus a diffusion \(D\) and any drift.

**C6. Identity (PROVED, in-model).** \(\dot I_M=D\,\mathbb E[F]+\int\!\!\int\pi(x)\,\nu(dz)\,D_{\mathrm{KL}}(p_x\|p_{x+z})\,dx\). A deterministic drift destroys no information (A1 with \(D=0\)).

**C7. Per-shock floor (PROVED, in-model; coefficient not tight).** By Le Cam's two-point argument and Bretagnolle–Huber, for every pair (pointwise \((a-x)^2+(a-x-z)^2\ge z^2/2\), so \(e(x)+e(x+z)\ge\tfrac{z^2}2\int\min(p_x,p_{x+z})\ge\tfrac{z^2}4e^{-D_{\mathrm{KL}}}\); a Markov-inequality route gives 8 in place of 4), \(D_{\mathrm{KL}}(p_x\|p_{x+z})\ge\ln\bigl(z^2/4(e(x)+e(x+z))\bigr)\), where \(e(y)\) is the conditional error at \(y\) (check C8: 7140 pairs). Averaging with Jensen gives \(\dot I_M\ge\lambda[\mathbb E\ln Z^2-\ln4(\varepsilon+\varepsilon_\rho)]\), where \(\varepsilon_\rho\) is the error weighted by the landing distribution \(\rho\). It is at most \(c\,\varepsilon\) when \(\rho\le c\,\pi\). The coefficient on \(\ln(1/\varepsilon)\) is 1 here, against \(\tfrac32\) for resets. Whether \(\tfrac32\) holds for local shocks is **OPEN**. With a diffusion part as well, the floors add: \(\dot I_M\ge D(1/\varepsilon-\mathcal I)+(\text{jump floor})\). At small \(\varepsilon\) the diffusive \(1/\varepsilon\) term dominates.

**C8. Heavy-tailed noise needs a heavy-tailed memory (PROVED, in-model).** For a Gaussian copy, \(D_{\mathrm{KL}}(p_x\|p_{x+z})=z^2/2\sigma^2\). Under an \(\alpha\)-stable jump measure, \(\nu(dz)\propto|z|^{-1-\alpha}dz\) with \(\alpha<2\), \(\int z^2\nu(dz)=\infty\), so the Gaussian copy's learning rate and heat are infinite. A Cauchy-location copy has \(D_{\mathrm{KL}}=\ln(1+z^2/4\sigma^2)\), and \(\int\ln(1+z^2/4\sigma^2)\,\nu(dz)<\infty\) for every \(\alpha\in(0,2)\) (check C7: 12.7 at \(\alpha=1.5\), \(\sigma=0.3\), unit jump density \(|z|^{-1-\alpha}\)). Its mean-squared error in that world is **not** computed. That claim is about finiteness of the heat only.

**Design read-off for class C.** A shock world charges per shock, logarithmically in precision and in the ruin cap. The memory that comes within a constant of the floor keeps a small reserve \(\delta=\varepsilon/4v\) of uncommitted prior mass, so a shock never lands where the memory has ruled it out. A memory with light (Gaussian) tails pays \(\lambda v/\varepsilon\), and under \(\alpha\)-stable shocks it pays infinite heat.

**Scope and open.** Exogenous shocks, mean-squared error, steady state, and a fast memory for the heat realization. **OPEN:** an attaining memory under MSE for an infinite-variance landing distribution; the tight coefficient for local shocks; and losses other than mean square. **Measurements:** \(\lambda\), the landing distribution (\(v\), or \(h(\pi)\) and \(\kappa_\pi\)), \(b\), \(\eta\), \(w\), and \(kT\).

## 6. Summary: proved, known, open

| Item | Label |
|---|---|
| \(\dot Q_M\ge kT\dot I_M\) | KNOWN (jumps), PROVED (in-model, diffusions; EQ-heat) |
| Van Trees, Stam, lautum, Donsker–Varadhan, Bretagnolle–Huber, Shannon lower bound, relaxation entropy | KNOWN |
| Destruction identity for non-equilibrium, switching, and jump worlds (A1, B1, C1, C6) | PROVED (in-model); ELEMENTARY given BHS |
| Floors A2, B2, C2, C5, C7 | PROVED (in-model) |
| Gap \(\le kTD\,\mathcal I\) and sandwich (A3, A4) | PROVED (in-model) |
| Regime-tuned learning rate, surcharge, threshold (B3, B4) | PROVED (in-model); fast-limit heat NUMERICAL |
| Core-plus-reserve within \((3.0033+\varepsilon/4v)\lambda\); bracket on \(J^*\) (C3, C4) | PROVED (in-model); fast-limit heat NUMERICAL |
| Gaussian copy infinite under \(\alpha\)-stable shocks; Cauchy copy finite (C8) | PROVED (in-model) |
| Hidden-regime label tracking; local-shock tight constant; infinite-variance MSE design; ruin in A/B; non-MSE losses; a moved world | OPEN |

## 7. Numerical checks

`theory/non_gaussian_floor_checks/non_gaussian_floor_checks.py` reports `FAILS 0`. Its stored output is `non_gaussian_floor_checks.out`. The pytest wrapper `tools/test_non_gaussian_floor_checks.py` reruns it and compares the output byte for byte. It runs in about 25 s. Its checks are A1–A5 (Fisher closed forms, Van Trees on 36 cases, the non-equilibrium identity, an exact lattice chain, and the sandwich); B1–B4 (the regime distributions, the per-regime floor, the hybrid identity on an exact chain, and the threshold); and C1–C9 (the \(I+L\) identity, \(\kappa\), the floor on 17 channels, the reserve design, an exact reset chain, the ruin floor, Cauchy relative entropy and \(\alpha\)-stable finiteness, Bretagnolle–Huber, and the cost bracket). It also checks that the hypothesis sentence is byte-identical in `THEORY.md` and here. None of this is a measurement of a real system.

## 8. Bearing on T50 (noted, not claimed)

T50 conjectures that antifragility falls out of minimizing the cost of judgment once the predict–act–correct loop is closed (`theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md`). This note's worlds are exogenous. No loop is closed, so nothing here is evidence for T50. Three results bear on it.

1. **Concavity in the world's variability.** The minimum is concave in volatility (\(\propto\sqrt D\), class A) and, at leading order, in shock rate (\(\propto\lambda\ln(1/\lambda)\), class C). By Jensen, a memory that tracks the regime pays less in a world whose volatility varies than the floor of a constant world at the same mean, once the stake passes \(w_{\mathrm{thr}}\) (B4, proved for volatility). This is gain from variability in the world's parameters. It is not gain from shocks to the system itself. The shock-rate analogue, with its switching surcharge, is **OPEN**.
2. **The selected design keeps optionality.** In reset worlds the design within a constant of the floor never fully commits: a reserve \(\delta=\varepsilon/4v\) turns a shock's cost from \(v/\varepsilon\) into \(\tfrac32\ln(v/\varepsilon)\). That is an option-like structure chosen by the cost. Whether it extends to a closed loop is part of T50.
3. **Ruin protection is cheap in shock worlds.** Its price is logarithmic in \(1/\eta\) per shock (C5).

## 9. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, or the hypothesis sentence. It does not add a CLAIM_MAP row. It does not change T48, T50, or T57–T61, apart from the T49 row in [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md). It does not prove a floor for a world the memory moves, a loss other than mean square, or a hidden-regime label task. It does not treat an in-model statement as a fact about a real system. No system has been shown to qualify under THEORY §3.

## 10. References

DOIs resolved on Crossref, 23 November 2026, America/New_York. The log is `theory/non_gaussian_floor_checks/crossref.out`.

- Stam, A. J. 1959. Some inequalities satisfied by the quantities of information of Fisher and Shannon. *Information and Control* 2:101. doi 10.1016/S0019-9958(59)90348-1.
- Wonham, W. M. 1964. Some Applications of Stochastic Differential Equations to Optimal Nonlinear Filtering. *SIAM J. Control* 2:347. doi 10.1137/0302028.
- Donsker, M. D. and Varadhan, S. R. S. 1975. Asymptotic evaluation of certain Markov process expectations for large time, I. *Comm. Pure Appl. Math.* 28:1. doi 10.1002/cpa.3160280102.
- Bretagnolle, J. and Huber, C. 1979. Estimation des densités: risque minimax. *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 47:119. doi 10.1007/BF00535278.
- Hamilton, J. D. 1989. A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle. *Econometrica* 57:357. doi 10.2307/1912559.
- Gill, R. D. and Levit, B. Y. 1995. Applications of the van Trees inequality: a Bayesian Cramér–Rao bound. *Bernoulli* 1:59. doi 10.2307/3318681.
- Van Trees, H. L. 1968 (reprint 2001). *Detection, Estimation, and Modulation Theory, Part I.* Wiley. doi 10.1002/0471221082.
- Barndorff-Nielsen, O. E. and Shephard, N. 2001. Non-Gaussian Ornstein–Uhlenbeck-based models and some of their uses in financial economics. *J. R. Stat. Soc. B* 63:167. doi 10.1111/1467-9868.00282.
- Cover, T. M. and Thomas, J. A. *Elements of Information Theory.* Wiley. doi 10.1002/047174882X.
- Palomar, D. P. and Verdú, S. 2008. Lautum Information. *IEEE Trans. Inf. Theory* 54:964. doi 10.1109/TIT.2007.915715.
- Esposito, M. and Van den Broeck, C. 2011. Second law and Landauer principle far from equilibrium. *EPL* 95:40004. doi 10.1209/0295-5075/95/40004.
- Still, S., Sivak, D. A., Bell, A. J. and Crooks, G. E. 2012. Thermodynamics of Prediction. *Phys. Rev. Lett.* 109:120604. doi 10.1103/PhysRevLett.109.120604.
- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Barato, A. C., Hartich, D. and Seifert, U. 2014. Efficiency of cellular information processing. *New J. Phys.* 16:103024. doi 10.1088/1367-2630/16/10/103024.
- Sandberg, H., Delvenne, J.-C., Newton, N. J. and Mitter, S. K. 2014. Thermodynamic costs in implementing Kalman–Bucy filters. *52nd Allerton Conference*, 550. doi 10.1109/allerton.2014.7028503.
- Horowitz, J. M. 2015. Multipartite information flow for multiple Maxwell demons. *J. Stat. Mech.* 2015:P03006. doi 10.1088/1742-5468/2015/03/p03006.
- Hartich, D., Barato, A. C. and Seifert, U. 2016. Sensory capacity: An information theoretical measure of the performance of a sensor. *Phys. Rev. E* 93:022116. doi 10.1103/PhysRevE.93.022116.
- Brittain, R. A., Jones, N. S. and Ouldridge, T. E. 2017. What we learn from the learning rate. *J. Stat. Mech.* 2017:063502. doi 10.1088/1742-5468/aa71d4.
- Nicoletti, G. and Busiello, D. M. 2021. Mutual Information Disentangles Interactions from Changing Environments. *Phys. Rev. Lett.* 127:228301. doi 10.1103/PhysRevLett.127.228301.
- Nicoletti, G. and Busiello, D. M. 2022. Mutual information in changing environments: Nonlinear interactions, out-of-equilibrium systems, and continuously varying diffusivities. *Phys. Rev. E* 106:014153. doi 10.1103/PhysRevE.106.014153.
- Chyzak, F. and Nielsen, F. 2019. A closed-form formula for the Kullback–Leibler divergence between Cauchy distributions. arXiv:1905.10965 (no DOI; checked numerically, C7).

Already in the repository and used rather than re-derived: Propositions EQ-heat, JP-heat, and EQ-learn (`theory/GENERALITY_2026-11-22.md`); the OU and telegraph infima (`theory/GENERAL_FORM_PHYSICS_2026-11-22.md`, `theory/INFO_PHYSICS_ATTAINABILITY.md`); T57 (`theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`), T58 (`theory/DRIFT_HEAT_LIFT_2026-11-23.md`), T59 (`theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`), T60 (`theory/GENERAL_FLOOR_FINITE_2026-11-23.md`), and T61 (`theory/FEEDBACK_FLOOR_2026-11-23.md`).
