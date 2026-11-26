# How general the results are

*Sunday 22 November 2026, evening (America/New_York; 23 November UTC). An audit of the proofs on `main`, including the acting-derivation note merged with PR #203. This note does not edit `THEORY.md`. The master equation is unchanged. The hypothesis sentence is unchanged:*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

*PR #203 is merged on `main` at `ddba436` (merge `3a364d8`). T47 is the acting-derivation row. The proposal diff is not applied. The generator question is answered below and is not an adoption into `THEORY.md`.*

Labels: **(A)** the published proof, or the proof already in this repository, uses no Gaussian, linear, Ornstein–Uhlenbeck, or telegraph assumption. **(B)** a short proof is on this page, and it likewise uses none of those assumptions. **(C)** a named step uses one of those assumptions, and the closed form does not survive its removal. A lower bound is not a derivation of the cost.

Checks: `theory/generality_checks/generality_checks.py`, run at `nice -n 19`. DOIs resolved on the Crossref API on 22 November 2026 ET (23 November UTC) are listed in `theory/generality_checks/crossref.out`.

## 0. What the five questions come to

The heat floor \(kT\,a(v-\varepsilon)/\varepsilon\) does not follow from Landauer or from Sagawa and Ueda for an arbitrary Markov memory. Landauer's theorem is an erasure bound of \(kT\ln 2\) for one bit of a symmetric memory. Sagawa and Ueda (2009), with the 2011 erratum, bound the sum of measurement work and erasure work in one cycle by \(kT\) times one mutual information. Sagawa and Ueda (2010) is a one-shot feedback identity, \(\langle e^{-\beta(W-\Delta F)-I}\rangle=1\), and the consequence \(\langle W\rangle\ge\Delta F-kT\langle I\rangle\). None of those statements is a steady learning rate, and none identifies the rate with \(a(v-\varepsilon)/\varepsilon\).

What does hold for a bipartite Markov memory is a floor by the information flow of that memory's own transitions. For a jump process under local detailed balance the identity is Proposition JP-heat. For an additive-noise diffusion, any smooth drift, the identity is Proposition EQ-heat. For a one-dimensional equilibrium diffusion with constant diffusion coefficient, Proposition EQ-learn replaces the Ornstein–Uhlenbeck evaluation of the lower bound by the Fisher information of the actual marginal. The Ornstein–Uhlenbeck number is the special case of that bound in which the Fisher information equals \(1/v\) and the Einstein relation is \(D=av\). Equality of the learning rate with that number also needs a Gaussian conditional of constant variance.

Boundary screening is a conditional-independence fact for any joint law that factorizes across the cut. It is not a fact about every joint law. The Gaussian trace cap is a separate calculation.

A loss that depends on the world only through a statistic \(Z\) is priced, at the level of mutual information, by \(Z\). The data-processing inequality gives that reduction for any joint law. A ruin constraint can only shrink the feasible set. Neither statement produces the factor-\(s\) heat ratio of identical Ornstein–Uhlenbeck modes.

Jensen's inequality applies to a convex payoff, for any law with a finite mean and a finite expectation of the payoff. A cap can destroy convexity. The comparison does not pass through an arbitrary cap.

Setting the coefficient of an additive control drift to zero returns the uncontrolled generator, for any generator in which the control enters only in that way. It does not produce the five-term sum, and it does not preserve the linear Lyapunov formulas.

## 1. Proofs

Throughout, a boundary term is assumed to vanish when an integration by parts is invoked. A density is regular when it is positive and smooth, the Fisher information below is finite, and those boundary terms vanish. \(kT\) is Boltzmann's constant times the bath temperature.

### 1.1 Proposition EQ-heat

**Proposition EQ-heat (B).** Let the memory coordinate \(M\) satisfy

\[
dM=F(X,M)\,dt+\sqrt{2D_M}\,dW,
\]

with \(D_M>0\) constant, \(W\) a Wiener process independent of the signal noise, and \(F\) smooth. The probability current of \(M\) is \(J=Fp-D_M\partial_M p\). Define

\[
\dot I_M=\int J\,\partial_M\ln p(X\mid M),\qquad
\mathrm{Sr}_M=\mathbb{E}[F^2+D_M\partial_M F]/D_M.
\]

In the steady state, \(\mathrm{Sr}_M\ge\dot I_M\). If the mobility is \(1\) and the Einstein relation sets \(kT=D_M\), the energy flow into the memory bath is \(D_M\,\mathrm{Sr}_M\ge kT\,\dot I_M\).

No Gaussian, linear, Ornstein–Uhlenbeck, or telegraph assumption is used. \(F\) may be cubic.

*Proof.* The integrand \(J^2/(D_M p)\) is nonnegative, so

\[
\Sigma_M=\int\frac{J^2}{D_M p}\ge 0.
\]

Substitute \(J/p=F-D_M\partial_M\ln p\):

\[
\Sigma_M=\frac1{D_M}\mathbb{E}\big[(J/p)\,F\big]-\int J\,\partial_M\ln p.
\]

The integral splits into \(\dot I_M\) and \(\int j_M\,\partial_M\ln p_M\). The second piece equals \(-\mathrm d_t S_M\), because \(\partial_t p_M=-\partial_M j_M\). Integration by parts gives \(\mathbb{E}[F\,\partial_M\ln p]=-\mathbb{E}[\partial_M F]\), hence

\[
\Sigma_M=\mathrm{Sr}_M-\dot I_M+\mathrm d_t S_M.
\]

In the steady state the marginal entropy is constant, and \(\mathrm{Sr}_M\ge\dot I_M\). The energy-flow identification is the Einstein relation just stated. It is a choice of units for that bath. ∎

Horowitz and Esposito (2014), doi 10.1103/PhysRevX.4.031015, prove the corresponding split for a bipartite jump process. This note does not re-prove that paper. Proposition JP-heat is the jump identity used by the check, proved from local detailed balance rather than quoted. Barato, Hartich, and Seifert (2014), doi 10.1088/1367-2630/16/10/103024, bound a learning rate by the entropy production of the learning subsystem. Still, Sivak, Bell, and Crooks (2012), doi 10.1103/PhysRevLett.109.120604, bound dissipation by the part of the memory that does not predict. Neither bound is \(a(v-\varepsilon)/\varepsilon\).

### 1.2 Proposition JP-heat

**Proposition JP-heat (B).** Let \((X,M)\) be a finite-state continuous-time Markov chain, with \(X\) and \(M\) jumping alternately. Suppose the memory rates satisfy local detailed balance at temperature \(T\),

\[
\frac{w(m\to m'\mid x)}{w(m'\to m\mid x)}=\exp\big((E(x,m)-E(x,m'))/kT\big),
\]

with \(kT=1\) in the display below. Let \(\pi\) be the stationary law. The memory-edge entropy production

\[
\sigma_M=\sum_{x,m\neq m'}\pi(x,m)\,w(m\to m'\mid x)\,\ln\frac{\pi(x,m)\,w(m\to m'\mid x)}{\pi(x,m')\,w(m'\to m\mid x)}
\]

is nonnegative, because each opposing pair contributes a term of the form \((a-b)\ln(a/b)\). The heat flow into the bath and the conditional flow

\[
\dot Q=\sum\pi\,w\,(E(x,m)-E(x,m')),\qquad
I_{\mathrm{alt}}=\sum\pi\,w\,\ln\frac{\pi(m'\mid x)}{\pi(m\mid x)}
\]

satisfy \(\dot Q=\sigma_M+I_{\mathrm{alt}}\ge I_{\mathrm{alt}}\).

*Proof.* Nonnegativity is the pair contribution. For the identity, \(\pi(x,m)/\pi(x,m')=\pi(m\mid x)/\pi(m'\mid x)\), so

\[
\ln\frac{\pi(x,m)\,w}{\pi(x,m')\,w_{\mathrm{back}}}=\ln\frac{\pi(m\mid x)}{\pi(m'\mid x)}+\ln\frac{w}{w_{\mathrm{back}}}.
\]

Local detailed balance makes the second logarithm the energy drop. Summing against \(\pi w\) gives \(\sigma_M=\dot Q-I_{\mathrm{alt}}\). ∎

\(I_{\mathrm{alt}}\) is the flow of the conditional law of \(M\) given \(X\). It is not the Ornstein–Uhlenbeck rate \(a(v-\varepsilon)/\varepsilon\). The check's three-state chain has a cycle in \(X\) and a bias \((m-x)^2\). It is not a two-state telegraph.

### 1.3 Proposition EQ-learn

**Proposition EQ-learn (B).** Let the signal be a one-dimensional diffusion

\[
dX=\mu(X)\,dt+\sqrt{2D}\,dW,\qquad D>0,
\]

exogenous, with a stationary density \(p_X\) whose current vanishes, so \(\mu=D\,\partial_x\ln p_X\). Let \(M\) be any regular conditional, and write \(u=\partial_x\ln p(x\mid m)\), \(F(m)=\int u^2\,p(x\mid m)\,dx\), and \(\mathcal I(p_X)=\int(\partial_x\ln p_X)^2 p_X\,dx\). The learning rate \(L=-\langle(J_X/p)\,u\rangle\) equals

\[
L=D\big(\mathbb{E}[F(X\mid M)]-\mathcal I(p_X)\big).
\]

If \(\varepsilon=\mathbb{E}[\mathrm{Var}(X\mid M)]\in(0,\infty)\), then \(L\ge D(1/\varepsilon-\mathcal I(p_X))\).

*Proof.* The joint current of an exogenous signal is \(J_X/p=\mu-D\,u=D(s_X-u)\), where \(s_X=\partial_x\ln p_X\). Therefore

\[
L=-\mathbb{E}[(J_X/p)\,u]=D\,\mathbb{E}[u^2]-D\,\mathbb{E}[s_X u].
\]

For each \(m\), integration by parts gives \(\int s_X\,u\,p(x\mid m)\,dx=-\int p(x\mid m)\,\partial_x s_X\,dx\). The same integration on the marginal gives \(\mathcal I(p_X)=-\mathbb{E}[\partial_x s_X]\). The cross term equals \(\mathcal I(p_X)\), which is the first display.

Cauchy–Schwarz on the conditional, against the centered coordinate, gives \(F(m)\ge 1/\mathrm{Var}(X\mid m)\): the score integrates to zero against \(p(x\mid m)\), and against \((x-\mathbb{E}[X\mid m])\,p\) it integrates to \(-1\). The function \(s\mapsto 1/s\) is strictly convex on \((0,\infty)\), so Jensen's inequality gives \(\mathbb{E}[1/\mathrm{Var}]\ge 1/\varepsilon\). ∎

Equality in Cauchy–Schwarz holds when the conditional score is affine in \(x\), that is when the conditional is Gaussian, and equality in Jensen holds when the conditional variance is almost surely constant. If in addition \(p_X\) is Gaussian of variance \(v\), then \(\mathcal I(p_X)=1/v\). If also \(D=av\), the bound is \(a(v/\varepsilon-1)\). Both of those last two sentences are extra assumptions. They are the step that Proposition AT-learn and Proposition G-learn use when they write \(j/p=-ax-av\,u\) or \(j/p=-D\Sigma^{-1}x-Du\), and when they replace the marginal Fisher information by \(\Sigma^{-1}\).

On the quartic equilibrium of the cubic drift \(\mu(x)=-x^3\), with \(D=1\), the check records \(\mathcal I(p_X)=2.027935\) and \(1/v=1.479338\). The same grid, with a three-state channel, records a learning rate \(1.395822\) against the bound \(1.010946\), while \(D(1/\varepsilon-1/v)=1.559543\). The Ornstein–Uhlenbeck expression is not this bound.

### 1.4 Proposition BL-screen and Proposition BL-loss

**Proposition BL-screen (B).** Let \(R\), \(B\), and \(E\) be coordinates on a product space. Suppose the joint law admits a density or a mass function

\[
p(x_R,x_B,x_E)=f(x_R,x_B)\,g(x_E,x_B)
\]

with respect to a product measure, up to one normalizing constant. Then \(X_R\perp X_E\mid X_B\). In particular, the conditional law of \(X_E\) given \((X_R,X_B)\) equals the conditional law given \(X_B\).

*Proof.* The product \(f\,g\) separates in \((x_R,x_E)\) once \(x_B\) is fixed. The conditional mass, or the conditional density, of \((X_R,X_E)\) given \(X_B\) is therefore a product, almost everywhere with respect to that conditional law. A product conditional is conditional independence. Conditioning further on \(X_R\) does not change the \(E\)-factor. ∎

The hypothesis is the factorization. It is the global Markov property at this cut when \(B\) separates \(R\) from \(E\) in an undirected graph and the law factors on the cliques. Besag (1974), doi 10.1111/j.2517-6161.1974.tb00999.x, proves that a strictly positive local Markov property implies such a factorization. This note uses only the direction proved above, which does not need positivity and does not need the 1971 manuscript. A joint law that does not factor need not screen. The check's product on \(\{0,1,2\}^3\) has conditional gap \(0\). The same check's non-product joint has a positive gap. On the path of three the screening identity evaluates to \(\mathrm{Var}(X_E\mid X_B)=\mathrm{Var}(X_E\mid X_R,X_B)=1/2\). The variance given the region alone is \(3/5\). Those two numbers are the Gaussian calculation. They are not the identity.

**Proposition BL-loss (B).** Suppose \(X_E\perp Y\mid X_B\), and the regular conditional \(p(x_E\mid x_B)\) does not depend on \(Y\). Then

\[
p(x_E\mid y)=\int p(x_E\mid x_B)\,p(x_B\mid y)\,dx_B.
\]

Any expected loss whose action is a function of \(Y\) and whose loss depends on the world only through \(X_E\) is determined by the posterior of \(X_B\).

*Proof.* Expand \(p(x_E\mid y)=\int p(x_E\mid x_B,y)\,p(x_B\mid y)\,dx_B\) and replace the inner kernel by \(p(x_E\mid x_B)\). The Bayes risk is an integral of the loss against \(p(x_E\mid y)\). ∎

The decomposition \(\mathrm{Var}(X_E\mid Y)=Q_{EE}^{-1}+M\,\mathrm{Var}(X_B\mid Y)\,M^\top\), and the trace cap \(\operatorname{tr}(Q_{BI}Q_{II}^{-1}Q_{IB})\), use a Gaussian conditional covariance and a precision update. Those displays are (C).

### 1.5 Proposition RD-hold

**Proposition RD-hold (B).** Let \(Z=f(X)\) be a statistic of the world, and let the action be a function of the memory \(M\).

1. \(I(Z;M)\le I(X;M)\), for any joint law on which the mutual informations exist.
2. If the loss depends on \((X,M)\) only through \((Z,M)\), the Bayes risk depends on \(M\) only through the conditional law of \(Z\) given \(M\). A coordinate that does not change \(p(x\mid m)\) does not change that risk.
3. Among memories that meet a distortion constraint and a ruin constraint \(P(\mathrm{ruin})\le\varepsilon_r\), the minimal mutual information is at least the minimum over the memories that meet the distortion constraint alone.

*Proof.* Since \(Z\) is a function of \(X\), the chain rule gives \(I(X;M)=I(Z;M)+I(X;M\mid Z)\). The second term is nonnegative. That is the data-processing inequality for a function of the source. The Bayes risk is the infimum of an integral of the loss against \(p(z\mid m)\). Adding a constraint removes feasible memories, so the infimum of a nonnegative functional on the smaller set is at least the infimum on the larger set. ∎

Shannon's paper is the reprint Crossref returns at doi 10.1109/9780470544242.ch1 (year field 2009, title "A Mathematical Theory of Communication"). The three lines above do not quote it. The argument does not say that a shared memory of a sum costs \(1/s\) as much heat as \(s\) item memories. That ratio is Proposition M-sum, and its step is the scalar Kalman rate of a sum of identical equilibrium Ornstein–Uhlenbeck modes.

A ruin constraint does not select a split. The memory note already records a Gaussian example in which two copies meet the cap more cheaply than the split.

### 1.6 Proposition JN-pay, Proposition JN-cap, and Proposition AF-menu

**Proposition JN-pay (B).** Let \(\varphi:\mathbb{R}\to\mathbb{R}\) be convex, and let \(X\) be a real random variable with \(\mathbb{E}|X|<\infty\) and \(\mathbb{E}|\varphi(X)|<\infty\). Then \(\mathbb{E}[\varphi(X)]\ge\varphi(\mathbb{E}[X])\).

*Proof.* Convexity supplies a slope \(\lambda\) with \(\varphi(x)\ge\varphi(\mu)+\lambda(x-\mu)\) for every \(x\), where \(\mu=\mathbb{E}[X]\). Take expectations. The linear term vanishes. ∎

If \(\varphi\) is strictly convex, a supporting line meets the graph only at \(\mu\), so \(\varphi(X)>\varphi(\mu)+\lambda(X-\mu)\) on \(\{X\neq\mu\}\). If that event has positive probability, the expectation is strict. Rothschild and Stiglitz (1970), doi 10.1016/0022-0531(70)90038-4, name the order in which every such \(\varphi\) rises. The supporting-line argument does not need their paper, and it does not need a Gaussian law.

The check uses \(\varphi(t)=(1+t)^{3/2}\) on the heavy-tailed masses \((1+k)^{-2.5}\) for \(k=0,\ldots,499\). The expectation is \(5.063876\) against \(\varphi\) of the mean \(2.579402\). The second moment is \(29.5050\) against a squared mean near \(0.78\).

**Proposition JN-cap.** The same conclusion does not hold for \(\min(\varphi,M)\) merely because \(\varphi\) is convex. Cap the square at \(1\), and put mass \(1/2\) on \(0\) and on \(4\). The mean is \(2\). Then \(\mathbb{E}[\min(X^2,1)]=1/2\) and \(\min((\mathbb{E} X)^2,1)=1\). The capped expectation lies strictly below the capped value at the mean. The uncapped expectation is \(8>4\).

The proof is the arithmetic. SymPy checks the rationals in the script. A cap from above removes the slope that Jensen uses. A floor under a convex payoff, \(\max(\varphi,c)\), stays convex, and Proposition JN-pay still applies. The naked-option formula \(\mathbb{E}[\max(X,0)]=\sqrt{\theta/(2\pi)}\) is the Gaussian integral. Convexity of \(\max(x,0)\) is not.

**Proposition AF-menu (B).** Let each design \(\mathcal{D}\) in a menu that does not depend on a real parameter \(a\) have a cost \(J(\mathcal{D},a)\) affine in \(a\). Then \(J^\star(a)=\inf_{\mathcal{D}} J(\mathcal{D},a)\) is concave in \(a\). If each \(J(\mathcal{D},\cdot)\) is nondecreasing, so is \(J^\star\).

*Proof.* A pointwise infimum of affine functions is concave. A pointwise infimum of nondecreasing functions is nondecreasing. ∎

Taleb and Douady (2013), doi 10.1080/14697688.2013.800219, is the paper whose title names a mathematical definition of antifragility. The repository's reading, in `theory/ROBUSTNESS.md` §6, applies the concave-cost side of that definition to \(J^\star\). The reading is not re-proved here. What R4(a) adds, and what is (C), is the affinity \(E=a\,V_S(\mathcal{D})+V_N(\mathcal{D})\) inside the linear-Gaussian model. Without that affinity, Proposition AF-menu does not say that the minimized cost falls, or rises, with volatility. Proposition AM-not-concave, already proved in `theory/ACTING_MEMORY_2026-11-22.md`, uses no Gaussian step: a cost that is strictly decreasing and bounded below on a right half-line is not concave there, because a negative difference quotient that keeps falling is unbounded below.

The turnover calculation in T43 is not an instance of Proposition JN-pay. Its heat is the Ornstein–Uhlenbeck learning rate of a precision pool, and its build term uses a Gaussian stock. The heterogeneous arm on that grid does not lower the cost. Proposition JN-pay does not force a positive replacement rate.

### 1.7 Proposition GN-zero

**Proposition GN-zero (B).** Let \(G_0\) be a Markov generator that does not depend on a feedback rule \(u\) or on a real coefficient \(b\): a bounded rate matrix, or an Itô generator whose drift and diffusion coefficient are locally Lipschitz and do not depend on \((b,u)\), with a well-posed martingale problem. Let the controlled generator be

\[
G_{b,u}=G_0+b\,u\,\partial_x,
\]

where \(\partial_x\) acts only on the world coordinate and \(u\) is a measurable function of the memory. Then \(G_{0,u}=G_0\) for every \(u\). If the martingale problem for \(G_0\) is unique, the law at \(b=0\) does not depend on \(u\).

*Proof.* The second term is the zero operator when \(b=0\). Uniqueness passes the generator to the law. ∎

\(G_0\) may be a cubic drift, \(-x^3\partial_x+D\partial_{xx}\), or a three-state rate matrix. The check's birth-death chain for the potential \(x^4/4-b\,u\,x\) has the same stationary distribution at \(b=0\) for \(u=0\) and for \(u=5\), and the mean moves from \(0\) to \(0.622433\) at \(b=1\), \(u=1\). The controlled three-state chain has the same world marginal at \(b=0\) for two memory speeds, and those marginals differ when \(b=1\).

The proposition stops at the law. It does not produce a sum of prices. An additive priced sum is Theorem R1, under A1–A7, and it is not a consequence of a generator. R1 does not choose the coordinate list of the THEORY §3 display. On a given list it leaves the prices unsigned without A8, and it does not cover \(hK\) without an extra separability assumption. If the control enters inside a diffusion coefficient, or as a nonlinear function of \(u\) with no separate coefficient \(b\), the hypothesis of Proposition GN-zero is false and the conclusion is not claimed.

On `main`, Corollary LG and Corollary LG-K evaluate the bath rates by the Lyapunov equation of a linear diffusion. That evaluation is (C). The ordering of two gains on a cubic plant is a conjecture there. Proposition GN-zero does not resolve that conjecture. Recording the class is not an adoption into `THEORY.md`.

## 2. The table

A row is one named result. "(A)" means the proof of that statement does not use a Gaussian, linear, Ornstein–Uhlenbeck, or telegraph step. The assumptions column quotes what the proof does use. For a (C) row, the last column is the step that uses the worked class. Numerical examples inside a note are not separate rows.

### 2.1 Propositions proved on this page

| Result | Class | Assumptions | Class-specific step |
|---|---|---|---|
| EQ-heat | B | Additive constant noise, smooth drift, vanishing boundary terms, steady state; Einstein relation only for the unit \(kT=D_M\) | None. The Ornstein–Uhlenbeck rate is not this inequality. Lemma D in the acting-derivation note is the same split, with the marginal-entropy term set to zero in steady state |
| JP-heat | B | Finite-state bipartite chain, local detailed balance | None. A telegraph is a special case, not a hypothesis |
| EQ-learn | B | One-dimensional exogenous equilibrium diffusion, constant \(D\), regular conditional | None. Equality with \(a(v-\varepsilon)/\varepsilon\) needs a Gaussian conditional of constant variance, a Gaussian marginal, and \(D=av\) |
| BL-screen | B | The joint factors as \(f(x_R,x_B)\,g(x_E,x_B)\) | None. Not true for a joint that does not factor |
| BL-loss | B | \(X_E\perp Y\mid X_B\) and a kernel that does not depend on \(Y\) | None. The Schur variance display is Gaussian |
| RD-hold | B | Mutual informations exist; the loss depends on the world through \(Z=f(X)\); ruin is a constraint | None. The factor-\(s\) heat ratio is not this statement |
| JN-pay | B | Convex \(\varphi\), finite mean, finite \(\mathbb{E}\lvert\varphi\rvert\) | None |
| JN-cap | B | The counterexample: cap \(1\) on \(x^2\), two-point law | The capped comparison is false. No further class is required to see that |
| AF-menu | B | Menu independent of \(a\); each cost affine in \(a\) | None. Affinity of the linear-Gaussian error is a further assumption |
| GN-zero | B | Control enters only as the additive drift \(b\,u\) | None. Lyapunov bath rates are not this statement |

### 2.2 Axioms and the representation

| Result | Class | Assumptions | Class-specific step |
|---|---|---|---|
| A1–A8 | A | Stated as assumptions in `theory/REPRESENTATION.md`. None is a Gaussian, linear, Ornstein–Uhlenbeck, or telegraph hypothesis. A6 for a general pair is the Gelfand–Yaglom–Dobrushin mutual information when that number is finite (`theory/CONTINUOUS_A6_2026-11-23.md`); the finite-law uniqueness theorem is not extended to differential entropy | None for the coordinate identification once mutual information is finite. The Gaussian differential formula is the special case in which the densities exist |
| Lemma C, Lemma P, Lemma C\(_\mathbb{Z}\), Lemma M | A | Cauchy's equation on \((0,\infty)\) or on the nonnegative integers; monotonicity or continuity; A8 only for the sign | None |
| Theorem R1 | A | A1–A7; at least three essential intervals; closed contour sets; concatenation; mutual information in the scope of A6, now including the Gelfand–Yaglom–Dobrushin extension when that number is finite. Nonnegative prices need A8. The term \(hK\) needs an extra separability assumption | None for the additive form. Debreu's year field on Crossref is empty (doi 10.1017/ccol052123736x.010). The von Neumann–Morgenstern record is the 2007 edition, doi 10.1515/9781400829460 |
| Theorem R2 | A for Kelly; C for the Lundberg argmins | Kelly growth is a different objective from expected currency cost. The Lundberg comparison is the scalar diffusion path | The intervals \(0.2362\) and \(0.3162\) are those argmins. They are the step that separates the Lundberg objective from expected cost. The Kelly separation does not use them |
| Lemma F-A | A | Pareto points of a slice | None |
| Theorem F1 | A | Free disposal; convexity only in part (ii) | None |
| R1′ | A | A1–A6 and A7′; at least three essential intervals; closed contour sets; concatenation; mutual information in the scope of A6, including the Gelfand–Yaglom–Dobrushin extension when that number is finite. Nonnegative prices need A8. The term \(hK\) needs the extra separability assumption. At \(b=0\) the effort coordinate is absent and the law is exogenous, so the cost is Theorem R1's five-term equation, each term kept, before minimization | None for the additive form. The drift does not produce the sum. GN-zero is the generator half of the reduction |
| Lemma D | A | Bipartite additive noise, smooth drift, vanishing boundary terms; steady state for \(\Sigma=\mathrm{Sr}-\dot I\) | None. EQ-heat is the memory coordinate of this identity, with the marginal-entropy term kept |
| Corollary LG, LG-0, LG-K | C | Linear bipartite diffusion, Lyapunov equation | The closed bath rates and the gain comparison |
| T47, cubic ordering | conjecture | The preregistered grid on the cubic plant. Not a theorem | GN-zero and Lemma LG do not decide it. The continuous gains are \(K_E=0.2327\) and \(K_H=0\). The locked grid difference \(0.25\) is one step of that grid |

### 2.3 THEORY.md

| Result | Class | Assumptions | Class-specific step |
|---|---|---|---|
| Master equation, THEORY §3 | A as a definition | Assembled from the named parts. Not a theorem. R1 says when the additive form is forced | None in the definition. Nonnegative prices are A8 |
| CT33, judgment spend | A | \(J=S+wE\) on a menu that does not depend on \(w\); ruin slack or absent at the stakes compared | None. The proof is the rearrangement of two optimality inequalities |
| CT20 (i), the bound \(K^\star\le J(\mathcal{D}_1)/h\) | A | \(J\ge hK\) with \(h>0\) | None |
| CT20 (i), existence | C | Continuous cost on a compact set of rates | Continuity is the linear-Gaussian filter on that rate box. Weierstrass is not the class-specific step |
| CT20 (ii), sensing fixed | A | Ruin slack or absent; \(E_K\) nonincreasing in \(K\); \(J=hK+wE_K\) | None. Topkis and Milgrom–Shannon supply the monotone selection. With reads chosen, the count can fall; that counterexample is also free of a Gaussian step |
| CT21, L1–L3 | C | Model S: sums of Ornstein–Uhlenbeck modes, or a non-rational spectrum of a stationary Gaussian process | The degree count is the Wiener filter. L1 quotes the Kalman–Bucy filter of one pole |
| CT22, price of survival | C | One check interval; \(J=c/\tau+\alpha\tau\); diffusion variance \(s_0^2+\beta\tau^3\); Lundberg root \(2m/s^2\) | The variance's \(\tau^3\) growth and the root \(2m/s^2\) are the diffusion path of Lemma B9 |
| CT24, cost shares | A | \(J^\star\) homogeneous of degree 1 in the prices; feasible set independent of the prices | None. A binding ruin constraint is the case the proof excludes. The tracker share \((\alpha-1)/\alpha\) needs the power cost of CT12 |
| CT12, read-rate rule | A | Exact reset; cost \(c/T+w\,q\,T^{\alpha-1}/\alpha\) from a self-similar error of exponent \(\alpha-1\) | None of the four worked classes. The square root is \(\alpha=2\) |
| Theorem P, CT1–CT3 | A | Stationary ergodic reserve; the action is a function of memory; rate–distortion function of the loss | None. The proof is data processing, the definition of \(D(R)\), and the ergodic theorem |
| CT4, first bit, the threshold \(\kappa<2\ln 2\cdot a^2\mathrm{Var}\) | C | Scalar Gaussian source | That threshold is the Gaussian rate–distortion function. The sign "a model can pay" is CT1 |
| Lemma B8 | C | Periodic reset, one-sided barrier | \(\mathrm{erfc}\) is the Brownian reflection principle |
| Lemma B9, Theorem L | C | Diffusion reserve, cycle-end ruin, squared error between checks | The \(\tau^3\) growth of loss variance is the Brownian calculation |
| Lemma B12, Theorem S, S1–S3 | A | Homogeneity in one currency; loss \(w\lvert e\rvert^p\); self-similar error of exponent \(H\) | None of the four worked classes. \(p=2\), \(H=1/2\) is a conjecture the note already separates. S4 is an example of unequal scaling |
| CT7, physics floor on a random walk | C | Error held on a walk of variance rate \(\sigma^2\) | The floor \(kT\,\sigma^2/(2D)\) is that walk. EQ-learn is the equilibrium-diffusion replacement, and a pure walk has no stationary density |
| Lemma B2, B3, B5, B6, onset and clocks | C | The power technology \((a,b)\) and the quadratic or stated loss inside that technology | The exponent \(-(1-b)/(1-a)\) is the power specification. It is not an Ornstein–Uhlenbeck step, and it is not a theorem for an arbitrary sensing price |
| CL12, L4 | A | The stated penalty \(p(u)\) strictly convex; band cost evaluated by the envelope theorem | None of the four worked classes. Jensen supplies equal widths |
| Nesting, formal Theorems 6 and 7, broadcast | C | The technology class and the drift-sharing exponent of the formal notes | The threshold \(\chi^\star=(1-a)/(1-b)\) uses that technology |

### 2.4 CORE.md and FRAMEWORK.md

*Dated note (sweep, 22 November 2026): this table audits `CORE.md` as it stood before the front-page rewrite of PR #206, now [`history/2026-11-22_CORE_before_front.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-22_CORE_before_front.md); "CORE §5" below is that file's section. The current `CORE.md` prints the heat-plus-stake cost and the five-term sum of THEORY §3 as different objects.*

| Result | Class | Assumptions | Class-specific step |
|---|---|---|---|
| CORE, the cost display | A as a definition | Same object as THEORY §3 | None |
| S1, information floor | A | Stationary exogenous world; assumption S-A that the read price is at least linear in the directed-information rate | None for the inequality. The scalar Gauss–Markov curve and the efficiency \(0.9574\) are a worked world |
| S2, S3 | A | The frontier as a set in the resource coordinates; free disposal; a convex feasible set only for the converse in S3 | None. A binding ruin cap need not preserve convexity; the note already says so |
| Stack cheaper only when a layer cannot reset the whole state | C | The specialized stack: each layer resets only its own component, quadratic loss | The comparison of a joint reset with the sum of part costs uses that model |
| \(T^\star=\sqrt{6k/(w\sigma^2)}\) | C | Brownian gap, quadratic running loss, zero discount, lump reset | The square root is \(H=1/2\), \(p=2\). Chalkley's formula is this case. The general exponent is Theorem S, S3 |
| Lifetime ratio in a stack | C | The same specialized stack, equal stakes | The ratio of two Brownian lifetimes |
| Fast-local / slow-shared | C | Shared-only delay; \(k_S<N k_L\); Brownian driver with fixed-period refresh for the proved sign | The Ornstein–Uhlenbeck driver is numerical in the note. Equal delays cancel the sign without a further Gaussian step |
| CORE §5, swarm limit | not a theorem | An analogy, as the page says | The square-root scaling is the lifetime formula |
| FRAMEWORK | a protocol | Measurement definitions and gates. Not a theorem about a generator | The sampling-rank gradient \(a-\kappa b\) in §6.9 inherits the power technology of the onset exponent |

### 2.5 The T-entries and the notes they point to

| Result | Class | Assumptions | Class-specific step |
|---|---|---|---|
| T41, H-iface, the conditional dependence | B as EQ-learn | Equilibrium diffusion, regular conditional | The note's identity \(L=a(v\mathbb{E}[F]-1)\) uses the Ornstein–Uhlenbeck current. The dependence on the conditional law does not |
| T41, H-floor \(kT\,a(v-\varepsilon)/\varepsilon\) | C | Exogenous equilibrium Ornstein–Uhlenbeck signal, mean-square decision, regular conditional | Fisher equality and \(D=av\). Attainment uses the linear spring |
| T41, H-volume, H-surface, the cut bound | C | Gaussian field \(Q=\alpha I+\beta L\), diffusion matrix a multiple of the identity, heat equal to \(\operatorname{tr}\Phi\) | The trace evaluation and the Loewner bound \(\Sigma\preceq\alpha^{-1}I\) |
| T42, M-sum, the factor \(s\) | C | Identical equilibrium Ornstein–Uhlenbeck modes, mean square of the sum | The sum is one Ornstein–Uhlenbeck signal of variance \(sv\), and the heat is the scalar Kalman rate |
| T42, alignment of a separable precision cost | C | Gaussian channel, precision matrix, loss \(\operatorname{tr}(US)\) | The trace rearrangement uses that covariance. RD-hold is the statement that survives without it |
| T42, ruin selects the split | false in the note's own example | The note's heat and upkeep | Not a generality question. The reading does not hold at those numbers |
| T43, turnover | C | Ornstein–Uhlenbeck heat of a precision pool, Gaussian stock in the build cost, the stated failure rules | The whole grid is that class. JN-pay does not imply a positive replacement rate. The heterogeneous arm stays at no shock |
| T44, BS-screen | B as BL-screen | Factorization, which the Gaussian precision supplies through \(Q_{RE}=0\) | The block-diagonal precision is the Gaussian route to a factorization the general proof does not need |
| T44, BS-loss variance, BS-cap | C | Gaussian conditional covariance; heat \(\operatorname{tr}\Phi\) | The Schur complement and the trace cap |
| T44, interior sites are not boundary-sufficient | C for the constant \(1/5\) | Degree at most \(4\), \(\alpha=\beta=1\), conditional variance \(1/Q_{ii}\) | The constant uses that precision. The sign "the blanket does not price an interior tolerance" is BL-loss applied to an interior coordinate, which the blanket does not screen |
| T45, AM-riccati, AM-point, the level drop along that channel | C | Linear-Gaussian channel, capped probe price, sign loss | The Riccati equation |
| T45, AM-not-concave | A | Strictly decreasing and bounded below on a half-line | None |
| T45, naked option, the square-root formula | C | Standard normal integral | Convexity of \(\max(x,0)\) is JN-pay. The formula \(\sqrt{\theta/(2\pi)}\) is Gaussian |
| T46, closed-loop gap, stock, separation, \(v=\theta\) | C | \(dX=-aX\,dt+b u_a\,dt+\sqrt{2a\theta}\,dW\), linear feedback | Every closed form in the row uses that linear diffusion. The note already says the \(b=0\) reduction used there is not Theorem R1 |
| T46, certainty equivalence fails for a capped loss | C for the number \(0.189957517375\) | The same linear plant, \(\varphi(v)=\mathbb{E}[\min(X^2,1)]\) | The derivative is computed on that Riccati gain. JN-cap is why a cap can move a stationary point |
| S1–S3 in the Shannon note | A | S-A and \(L\ge 0\) for S1; support function for S2; supporting hyperplane for S3 | The Gauss–Markov minimizer over \(P\) is a worked curve, not the theorem |
| PD1(a) | A | Causal memory; innovation entropy bounded below; the maximum-entropy inequality | The Gaussian density is the maximizer used as a bound. The world is not assumed Gaussian |
| PD1(b), PD7 | C | Linear dynamics \(X_{t+1}=AX_t+W_t\) for the sharp constants; the equality case is Gaussian noise and the Kalman filter | The entropy-power step is general. The closed form \(N^\star(r)\) uses the linear recursion |
| IP-chain | A | Exogenous Markov world; memory generated from the past and from independent noise | None |
| IP-flow, IP-ray, the telegraph floor | C | Two-state rates, Hamming error | Equality at the minimal affinity is that family. JP-heat is the jump inequality without two states |
| AT-learn, the bound \(L\ge R(\varepsilon)\) | C | Equilibrium Ornstein–Uhlenbeck signal | The current \(j/p=-ax-av\,u\). The Fisher and Jensen steps are the ones EQ-learn keeps |
| AT-attain, the spring | C | Linear memory drift | The Lyapunov moments |
| G-learn as stated | C | Linear equilibrium diffusion, Gaussian marginal \(\Sigma\) | \(j/p=-D\Sigma^{-1}x-Du\) and the replacement of the marginal Fisher information by \(\Sigma^{-1}\). The Loewner bound on a conditional Fisher matrix is not that step |
| G-sum, G-trace, G-fast, the frontiers | C | Product of equilibrium Ornstein–Uhlenbeck modes, or one linear spring | The scalar rate, summed or minimized under a quadratic constraint |
| Theorem B, layer convexity in the band model | A | Signal-to-noise ratio nonincreasing in frequency; ideal band scores | None of the four worked classes. A rhythm can break convexity; the note already gives the example |
| SA1 | A | Haploid Moran chain, weak mutation, fitness linear in the cost, static world | None of the four worked classes |
| SA1b, the excess \(d/(2\beta)\) | C | Quadratic well and a Gaussian integral in whitened coordinates | Equipartition is that integral |
| R4(a)–(c) | C at the affinity; B at the envelope | Menu of costs affine in the volatility scale, for AF-menu and for Jensen on a concave \(J^\star\) | The affinity is the linear-Gaussian error. A binding ruin constraint makes the menu depend on the scale |
| L1 in `theory/LAYERS.md` | C | One Ornstein–Uhlenbeck pole or one random walk, Kalman–Bucy | The filter of a scalar first-order state |

`measurement/FRAMEWORK.md` adds no further theorem. Reach, cosmic-web, wormhole, and torus notes are scope extensions. Where they invoke a theorem already in this table, the class is that row's class. They do not contain a second proof that removes a (C) step.

## 3. What can be stated

For every system that meets A1–A7, on at least three essential interval coordinates, a continuous cost that represents the preorder is an additive price sum up to one positive scale and one additive constant. The memory coordinate in that sum is mutual information in the scope of A6: finite-law Shannon information on finite alphabets, and, when the mutual information is finite, the Gelfand–Yaglom–Dobrushin supremum of discrete mutual informations, which agrees with a differential mutual information when the densities exist (`theory/CONTINUOUS_A6_2026-11-23.md`). Nonnegative prices need A8. The term in the layer count needs the extra separability assumption, and the ruin restriction is a constraint, not a summand. On a menu that does not depend on the stake, for a cost \(S+wE\) with ruin slack or absent, judgment spend does not fall as the stake rises, and the error does not rise. A minimizer of a linear cost at strictly positive prices is undominated in the coordinates those prices charge. A joint law that factorizes across a cut screens the two sides. When the loss depends on the world only through the exterior and the decision is a function of the screened side, the expected loss is a function of the blanket posterior. A bipartite memory's bath is bounded below by \(kT\) times the information flow of its own transitions, in the sense of EQ-heat or JP-heat. For a one-dimensional equilibrium diffusion the learning rate equals \(D(\mathbb{E}[F]-\mathcal I(p_X))\) and is at least \(D(1/\varepsilon-\mathcal I(p_X))\). Equality with \(a(v-\varepsilon)/\varepsilon\) needs the further assumptions named on the EQ-learn row. An uncapped convex payoff has expectation at least the payoff of the mean. If the control enters the generator only as an additive drift \(b\,u\), and the martingale problem for the uncontrolled generator is unique, the law at \(b=0\) is the uncontrolled law. The closed heat \(kT\,a(v-\varepsilon)/\varepsilon\), the factor-\(s\) memory ratio, the square-root lifetime, the Wiener degree count, the Gaussian trace cap, and the gain selected by feedback heat are calculations inside a worked class. They are not consequences of the axioms. That strongly selected systems sit near the minimum is the hypothesis sentence. It is not a theorem.

## 4. Checks

`theory/generality_checks/generality_checks.py` checks BL-screen on a three-state factorized joint and on a joint that does not factor, EQ-learn on the cubic drift, JP-heat on a three-state chain, JN-pay on the heavy-tailed masses, JN-cap in exact arithmetic, and GN-zero on the cubic birth-death chain and on the controlled three-state chain. The run used for this note reports FAILS 0.

## 5. References

Resolved on the Crossref API, 22 November 2026 ET (23 November UTC). The record is `theory/generality_checks/crossref.out`.

- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Barato, A. C., Hartich, D. and Seifert, U. 2014. Efficiency of cellular information processing. *New J. Phys.* 16:103024. doi 10.1088/1367-2630/16/10/103024.
- Sagawa, T. and Ueda, M. 2009. Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure. *Phys. Rev. Lett.* 102:250602. doi 10.1103/PhysRevLett.102.250602. Erratum, 2011, doi 10.1103/PhysRevLett.106.189901.
- Sagawa, T. and Ueda, M. 2010. Generalized Jarzynski Equality under Nonequilibrium Feedback Control. *Phys. Rev. Lett.* 104:090602. doi 10.1103/PhysRevLett.104.090602.
- Landauer, R. 1961. Irreversibility and Heat Generation in the Computing Process. *IBM J. Res. Dev.* 5:183. doi 10.1147/rd.53.0183.
- Besag, J. 1974. Spatial Interaction and the Statistical Analysis of Lattice Systems. *J. R. Statist. Soc. B* 36:192. doi 10.1111/j.2517-6161.1974.tb00999.x.
- Still, S., Sivak, D. A., Bell, A. J. and Crooks, G. E. 2012. Thermodynamics of Prediction. *Phys. Rev. Lett.* 109:120604. doi 10.1103/PhysRevLett.109.120604.
- Debreu, G. Topological methods in cardinal utility theory. doi 10.1017/ccol052123736x.010. The year field came back empty.
- von Neumann, J. and Morgenstern, O. Theory of Games and Economic Behavior, 60th Anniversary Commemorative Edition, 2007. doi 10.1515/9781400829460.
- Shannon, C. E. A Mathematical Theory of Communication. Reprint doi 10.1109/9780470544242.ch1. Crossref returns year 2009 for this record.
- Taleb, N. N. and Douady, R. 2013. Mathematical definition, mapping, and detection of (anti)fragility. *Quantitative Finance*. doi 10.1080/14697688.2013.800219.
- Rothschild, M. and Stiglitz, J. E. 1970. Increasing risk: I. A definition. *J. Econ. Theory*. doi 10.1016/0022-0531(70)90038-4.
