# Co-adaptation: when coupled cost-of-judgment minimizers sit near a minimizer (T12, CX2)

*Saturday 21 November 2026, evening America/New_York. Branch `coadaptation-2026-11-21` off `main` `c92886a`; draft PR #148; updated after independent review (`reviews/coadaptation_2026-11-21/REVIEW.md`, blockers 1–3, should-fix 1, nits 1–3) with CA5–CA7, P1–P4/F6, and the single-basin bracket refutation folded in. CONFIRM2 is READY at `93add78` (`reviews/coadaptation_2026-11-21/CONFIRM2.md`); merged as `b16193d`. It does not change the Part 2 hypothesis sentence, any locked file, or the status of CX1, CX2, CT31, CT32 or CT34. Checks: `tools/coadaptation_checks.py`, run by `tools/test_coadaptation_checks.py` (23 tests).*

## 0. Bottom line

**In plain words.** Take several systems ("parties"), each a population selected on its own cost of judgment \(J_i\), where each party's cost depends on the others' designs (they compete, collaborate, or one is the other's world). Under the selection note's assumptions applied to each party separately (A1, A2-L, rare mutation) on connected party move graphs with equal edge clocks, the joint substitution chain is reversible (satisfies detailed balance with some positive stationary law \(\pi\)) **if and only if** the game whose costs are \(\beta_iJ_i\) is an exact potential game. Then the stationary distribution is unique (by irreducibility) and Boltzmann, \(\pi\propto e^{-\Psi}\), and when \(\Psi\) is confining (integrable \(e^{-\Psi}\)) with quadratic own wells, each party's expected **regret** (its cost above its best reply to the others) is \(d_i/(2\beta_i)\). That excess is near-minimization only when \(\sigma N_e\gg d\) (excess small against operating cost). What the group approaches at high selection strength in a single confining potential basin is the minimizer of the potential, which is a Nash equilibrium, not necessarily the joint optimum; when costs are aligned shares of one team cost with equal \(\sigma N_e\), the selection note's fractional excess \(d/(2\sigma N_e)\) returns for the team.

Outside potential games there is no Boltzmann form, yet an exact per-party virial identity still holds in the diffusion model (CA2), strictly monotone non-potential games remain stable at all speeds with excess controlled by the radial part of a Hodge split (CA5), and linear–quadratic translation drift adds \(\frac{1}{2}\sum_i\mathrm{Tr}\,Q_{ii}/v_i\) to the potential excess (CA7). For mismatched selection strengths on a finite discrete team landscape, a perturbative tree bound and a single-basin low-temperature limit hold (CA6), a PL flux bound holds with explicit loose constants (P2), and tree-shaped move graphs are exact (P3); however, **the finite-\(\gamma\) single-basin Gibbs bracket is FALSE** (refuted by a local negative derivative, an explicit \(2\times 2\) counterexample, and a \(2\times m\) entropic family (ratio \(34.64\) at \(m=64\); with the barrier held at 10 the scale-separation ratio tends to \(415.8\) as \(m\to\infty\)), even though 1,155 random draws missed it). Under strong selection with multiple basins, a group settles into whichever arrangement minimizes the stochastic potential of resistance trees (Young 1993; Freidlin & Wentzell 1984/2012), so **strongly selected members act as gatekeepers on exits** and clock speeds drop out (P4 / F6). Six failure classes (F1–F6) show with minimal counterexamples where near-minimization fails.

**The theorem in one line (CA1 + CA1b).** With \(\beta_i=\alpha_i\nu_i\) (selection note, SA1c) and connected party move graphs \(\mathcal{G}_i\),

\[
\text{reversible (detailed balance with a positive }\pi\text{)}\iff \beta_i\bigl[J_i(x_i',x_{-i})-J_i(x_i,x_{-i})\bigr]=\Psi(x_i',x_{-i})-\Psi(x_i,x_{-i})\ \ \forall i,x,x_i',
\]

and then (uniquely, by irreducibility) \(\pi(x)\propto e^{-\Psi(x)}\); when \(e^{-\Psi}\) is integrable with quadratic own wells in whitened coordinates,

\[
\mathbb{E}\bigl[J_i(x)-\min_{y}J_i(y,x_{-i})\bigr]=\frac{d_i}{2\beta_i},\qquad
\mathbb{E}[\Psi]-\Psi^\star=\frac{d}{2},\qquad d=\textstyle\sum_i d_i .
\]

**Status.** CA1–CA7, P1–P4, and failure classes F1–F6 are **PROVED (in-model)**; P2 carries explicit loose constants; the conjectured finite-\(\gamma\) single-basin discrete bracket is **FALSE**. The Boltzmann form for potential games under logit revision is **KNOWN** (Blume 1993), and the resistance-tree selection method of P4/F6 is **KNOWN** (Young 1993; Freidlin & Wentzell 1984/2012), applied here to cost-of-judgment co-adaptation rather than presented as a new method. Whether real coupled systems are \(\beta\)-potential games is **OPEN**; nothing here is a field result. CX1 and CX2 stay **OPEN**: no general near-minimization theorem holds for arbitrary coupling (CT32, and §9 here).

**The hypothesis sentence is unchanged.** It is, byte for byte,

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

## 1. Status words

As in `theory/SELECTION_AXIOMS.md` §1. **PROVED (in-model)** means proved inside the stated model, which says nothing by itself about nature. **NUMERICAL** means computed. **KNOWN** means published and credited. **OPEN** means not derived or not tested, not refuted.

## 2. Setup

There are \(n\) parties. Party \(i\) is a population of size \(N_i\) whose designs \(x_i\) live on a finite connected undirected design graph \(\mathcal{G}_i\) (in the quadratic statements, a uniform lattice in \(d_i\) whitened coordinates, as in SA1b). The joint state is \(x=(x_1,\dots,x_n)\). Party \(i\) bears the cost rate \(J_i(x_i,x_{-i})\ge 0\). "Acting on the world" is the case where one party is the world: a non-selected process that relaxes on its own cost (§9, F3).

- **CA-A (per party: the selection note's A1 and A2-L).** Party \(i\)'s Wrightian fitness is \(r_i=\exp(m_{0,i}-\alpha_iJ_i)\) with \(\alpha_i>0\) constant on the graph.
- **CA-B (no within-party frequency dependence).** A mutant's cost depends on the other parties' fixed designs and not on its own population's composition. If the "parties" are individuals in one population, this fails and the evolutionary-game case (ESS) applies instead; that case is not covered.
- **CA-C (joint weak mutation).** At most one party is polymorphic at a time: each party's origination rate \(N_i\mu_i\) times the longest fixation time is \(\ll 1\). Substitutions then arrive one party at a time (asynchronous revision).
- **CA-E (equal clocks).** Within party \(i\), every undirected edge of \(\mathcal{G}_i\) carries the same mutation clock \(u_i>0\). The clocks may differ between parties.

Then the joint fixed state is a continuous-time Markov chain whose moves change one party's design along one edge, at rate \(u_i\varphi_i(x_i\to x_i'\mid x_{-i})\), with \(\varphi_i\) the haploid-Moran fixation probability. From SA1's algebra,

\[
\frac{\varphi_i(x_i\to x_i'\mid x_{-i})}{\varphi_i(x_i'\to x_i\mid x_{-i})}=\exp\bigl(-\beta_i[J_i(x_i',x_{-i})-J_i(x_i,x_{-i})]\bigr),\qquad \beta_i=\alpha_i(N_i-1)
\]

(diploid Wright–Fisher: \(\beta_i=\alpha_i(2N_i-1)\), an approximation). Only this ratio is used in CA1. Any revision rule with the same ratio gives the same stationary law in CA1: logit (Glauber) revision as in Blume (1993), Metropolis, or a physical relaxation at inverse temperature \(\beta_i\). Selection, learning, and relaxation are interchangeable there.

## 3. The exact discrete result

**Theorem CA1 (reversibility iff \(\beta\)-scaled exact potential; PROVED (in-model)).** Under CA-A, CA-B, CA-C and CA-E on connected party move graphs \(\mathcal{G}_i\), the joint chain has a unique stationary distribution \(\pi>0\) (by irreducibility). It is reversible (satisfies detailed balance with some positive \(\pi\)) if and only if the game with costs \(\beta_iJ_i\) is an exact potential game (Monderer & Shapley 1996), that is, if some \(\Psi\) satisfies \(\Psi(x_i',x_{-i})-\Psi(x_i,x_{-i})=\beta_i[J_i(x_i',x_{-i})-J_i(x_i,x_{-i})]\) for every party and every unilateral change. Then \(\pi(x)\propto e^{-\Psi(x)}\), whatever the clocks \(u_i\).

*Proof.* Moran fixation probabilities are strictly positive and the Cartesian product of connected graphs \(\mathcal{G}_i\) is connected, so the joint chain is irreducible on a finite state space and its stationary law \(\pi>0\) is unique. (If) For a move of party \(i\) along an edge, \(\pi(x')/\pi(x)=e^{-[\Psi(x')-\Psi(x)]}=e^{-\beta_i\Delta J_i}=q(x\to x')/q(x'\to x)\); the clock \(u_i\) cancels. Detailed balance holds on every edge. (Only if) If the chain is reversible with positive \(\pi\), set \(\Psi=-\log\pi\). On every edge move of party \(i\), \(\Psi(x')-\Psi(x)=\log[q(x'\to x)/q(x\to x')]=\beta_i\Delta J_i\). For non-adjacent \(x_i,x_i'\), sum along a path in the connected graph \(\mathcal{G}_i\) with \(x_{-i}\) fixed; both sides telescope. So \(\Psi\) is an exact potential for \((\beta_iJ_i)\). □

Note why reversibility, rather than \(\pi\propto e^{-\Psi}\) alone, is the left side of the equivalence: every positive law \(\pi\) can be written as \(e^{-\Psi}\) with \(\Psi=-\log\pi\) (for example, matching pennies in F1 has uniform \(\pi\propto e^0\) at every \(\beta\), yet \(0\) is not a potential for matching pennies).

**Corollary CA1a (weighted potential games).** If \((J_i)\) is a weighted potential game with weights \(\omega_i>0\), \(\Delta_iJ_i=\omega_i\Delta_i\Phi\) (CT31's shared-driver class, \(\omega_i=w_i\)), and \(\beta_i\omega_i=\gamma\) for all \(i\), then \(\pi\propto e^{-\gamma\Phi}\). If \(\beta_i\omega_i\ne\beta_j\omega_j\) and \(\Phi\) has a nonzero mixed difference in \((x_i,x_j)\) somewhere, the chain is **not** reversible. *Proof.* The \(\beta\)-scaled sum around an elementary square in \((x_i,x_j)\) equals \((\beta_i\omega_i-\beta_j\omega_j)\) times the mixed difference of \(\Phi\), and reversibility needs it to vanish (Kolmogorov 1936). Terms of \(J_i\) that depend only on \(x_{-i}\) cancel in every \(i\)-move. □

So matching strengths is not a technicality. Even when every party bears a share of one team cost, unequal \(\beta_i s_i\) break reversibility and the Boltzmann form (CA3 and CA6 bound what is left).

**Theorem CA1b (the selection note's excess, lifted; PROVED (in-model)).** Assume CA1's conclusion with a confining potential (\(e^{-\Psi}\) integrable; on unbounded domains, \(\nabla^2\Psi\succ 0\)).

1. *Per party.* \(\pi(x_i\mid x_{-i})\propto e^{-\beta_iJ_i(x_i,x_{-i})}\) exactly, because \(\Psi-\beta_iJ_i\) does not depend on \(x_i\). If each \(J_i(\cdot,x_{-i})\) is a quadratic well in \(d_i\) whitened coordinates (SA1b's conditions, for every \(x_{-i}\)), the expected regret \(R_i=J_i(x)-\min_yJ_i(y,x_{-i})\) is \(\mathbb{E}[R_i]=d_i/(2\beta_i)\).
2. *Potential.* If \(\Psi\) is a quadratic well in \(d=\sum_id_i\) coordinates, \(\mathbb{E}[\Psi]-\Psi^\star=d/2\); with CA1a, \(\mathbb{E}[\Phi]-\Phi^\star=d/(2\gamma)\).
3. *Team.* Let \(J_T=\sum_iJ_i\), quadratic with Hessian \(H_T\succ 0\), and \(x^\Psi=\arg\min\Psi\). Then
\[
\mathbb{E}[J_T]-\min J_T=\underbrace{J_T(x^\Psi)-\min J_T}_{\text{absolute potential-to-team gap}\ \ge 0}+\tfrac12\mathrm{Tr}\bigl(H_T(\nabla^2\Psi)^{-1}\bigr).
\]
The first term does not shrink with selection strength. It is the **absolute** price-of-anarchy gap \(J_T(x^\Psi)-\min J_T\), which scales with \(J_T^\star=\min J_T\) (in CT31's class, it is the price-of-anarchy **ratio** \(\sum_i J_i(\mathrm{Nash})/J_T^\star\) that is bounded by \((N+1)/(2\sqrt N)\), so when \(J_T=\sum_i J_i\) the absolute gap is \((\text{ratio}-1)J_T^\star\le\bigl(\frac{N+1}{2\sqrt N}-1\bigr)J_T^\star\)). The second term is the scatter, \(O(1/\beta)\).

*Proof.* (1) For a fixed \(x_{-i}\), \(\pi(\cdot\mid x_{-i})\) is SA1's Boltzmann measure for the single cost \(J_i(\cdot,x_{-i})\); apply SA1b and average over \(x_{-i}\). (2) is SA1b for \(\Psi\) at \(\beta=1\). (3) Write \(x=x^\Psi+\delta\) with \(\delta\sim\mathcal N(0,(\nabla^2\Psi)^{-1})\); \(J_T\) is quadratic, so \(\mathbb{E}[J_T]=J_T(x^\Psi)+\tfrac12\mathrm{Tr}(H_T\,\mathrm{Cov}\,\delta)\). □

**Corollary CA1c (aligned shares recover the single-system formula).** If \(J_i=s_iJ_T+h_i(x_{-i})\) with \(s_i>0\) (CT31's stake-proportional cost shares are this with \(s_i=w_i/W\)), the potential is \(J_T\) and the Nash points are the stationary points of \(J_T\). When \(h_i=0\) and \(\sum_is_i=1\), the parties' summed cost is \(J_T\), so the potential-to-team gap is zero. The Boltzmann form needs \(\beta_is_i=\gamma\). With \(h_i=0\) and A2-L, \(\alpha_i=\sigma_i/J_i^\star\) and \(J_i^\star=s_iJ_T^\star\), so \(\beta_is_i=\sigma_i\nu_i/J_T^\star\). **The condition is equal \(\sigma N_e\) across parties**, with each elasticity measured at that party's own operating cost. Then \(\gamma=\sigma N_e/J_T^\star\) and
\[
\frac{\mathbb{E}[J_T]-J_T^\star}{J_T^\star}=\frac{d}{2\sigma N_e},\qquad d=\textstyle\sum_id_i,
\]
which is SA1c's form with the team's total number of soft coordinates. Near-minimization (small fractional excess) holds only when \(\sigma N_e\gg d\).

*Checks (NUMERICAL; labels are sections of `tools/coadaptation_checks.py`).* s1: on a 6×5 two-party grid with Moran fixation and \(\beta_i\omega_i\) matched, the exact stationary vector equals \(e^{-\gamma\Phi}\) to a relative \(10^{-8}\) for clock ratios 1, 1/20 and 20, and is clock-independent to \(8\times10^{-13}\) in total variation; with a 3× mismatch the square-cycle log ratio is 50.9 and the stationary vector moves with the clocks (total variation 0.010). s1c: on 60 random three-party games, reversibility agreed with the \(\beta\)-scaled exact-potential test 60/60. s2: a two-party quadratic potential game on a 0.01 lattice gives regrets 0.006246 and 0.015609 against \(d_i/(2\beta_i)=0.00625\) and 0.015625, potential excess 0.999996 against 1, and a team excess of 0.116671 against 0.116671 (gap 0.0585 plus scatter 0.0582). s3: explicit Moran populations (\(N=8\) each, every mutant's fate simulated birth by death) over 200,000 mutation attempts land at total variation 0.018 from \(e^{-\gamma\Phi}\).

## 4. Beyond potential games: virial identity and team mismatch (CA2, CA3)

The discrete chain has no closed form outside potential games. Its continuum limit does have an exact identity.

**Model CA-D (diffusion limit; an assumption).** On a lattice of spacing \(\epsilon_i\) with \(\epsilon_i\beta_i|\nabla_iJ_i|\ll 1\), the substitution chain is approximated by
\[
\mathrm dx_i=-v_i\beta_i\nabla_iJ_i(x)\,\mathrm dt+\sqrt{2v_i}\,\mathrm dW_i,
\]
with \(v_i=\bar q_i\epsilon_i^2\), where \(\bar q_i\) is the edge rate's symmetric part. This follows from the rate ratio \(e^{-\beta_i\epsilon_i\partial J_i}\): drift \(\epsilon(q_+-q_-)\approx-\bar q\epsilon^2\beta\partial J\), variance rate \(\epsilon^2(q_++q_-)\approx 2\bar q\epsilon^2\). The speed \(v_i\) carries the mutation supply. Stationary distributions of the chain do not depend on it in potential games (CA1); here they can.

**Theorem CA2 (per-party virial identity; PROVED (in-model)).** Under CA-D, suppose a stationary distribution with finite second moments exists. Then for every party \(i\) and every constant point \(c_i\),
\[
\mathbb{E}[\nabla_iJ_i(x)]=0,\qquad \beta_i\,\mathbb{E}\bigl[(x_i-c_i)\cdot\nabla_iJ_i(x)\bigr]=d_i,
\]
for any coupling, any speeds, and any \(J_i\), potential or not. *Proof.* Itô on \(x_i\) and on \(|x_i-c_i|^2\): \(\mathrm d\,\mathbb{E}|x_i-c_i|^2/\mathrm dt=-2v_i\beta_i\mathbb{E}[(x_i-c_i)\cdot\nabla_iJ_i]+2v_id_i\), which is zero in stationarity (the stochastic integral has mean zero under finite second moments). The first identity is the same computation for \(\mathbb{E}x_i\). □

In words, on average every party sits at its own first-order condition, so the stationary mean is a Nash point "in mean". Its own-gradient scatter carries exactly \(d_i/\beta_i\), as if it were alone. This is the virial (equipartition) identity of a stationary diffusion, read per party. It is a standard Itô computation; the game reading is the packaging.

**Corollary CA2a (linear–quadratic coupling).** Let \(\nabla_iJ_i=(Mx+m)_i\), \(B=\mathrm{diag}(\beta_i)\), \(V=\mathrm{diag}(v_i)\) (blockwise), and \(K=BM\).
1. A stationary distribution exists iff \(-VK\) is Hurwitz. It is Gaussian, with mean equal to the Nash point \(-M^{-1}m\) and covariance \(\Sigma\) solving \(VK\Sigma+\Sigma K^\top V=2V\). The virial identity reads \(\mathrm{Tr}_i(K\Sigma)=d_i\) blockwise, so \(\mathrm{Tr}(\tfrac12(K+K^\top)\Sigma)=d\).
2. If \(K+K^\top\succ 0\) (the \(\beta\)-scaled game is strictly monotone: Rosen's (1965) diagonal strict convexity with weights \(\beta_i\); "stable games" in Hofbauer & Sandholm 2009, with the sign reversed), the coupled adaptation is stable **for every choice of speeds**. *Proof.* If \(VKz=\lambda z\), then \(z^*Kz=\lambda z^*V^{-1}z\), and the real part of the left side is positive. This is the standard sufficient condition for D-stability (the notion is Arrow & McManus 1958). □
3. If \(K\) is symmetric (the \(\beta\)-potential case), \(\Sigma=K^{-1}=(\nabla^2\Psi)^{-1}\) for every \(V\), which recovers CA1 and CA1b. If \(K\) is not symmetric, \(\Sigma\) depends on the speeds and the per-party regret is not \(d_i/(2\beta_i)\) in general.

**Theorem CA3 (one team cost, mismatched strengths; PROVED (in-model)).** Let \(J_i=s_iJ_T\) with \(J_T=\tfrac12x^\top Qx\), \(Q\succ 0\), and \(\gamma_i=\beta_is_i\) (constant on party \(i\)'s block). For **every** choice of speeds,
\[
\frac{d}{2\gamma_{\max}}\;\le\;\mathbb{E}[J_T]-J_T^\star\;\le\;\frac{d}{2\gamma_{\min}},
\]
and both bounds equal \(d/(2\gamma)\) when all \(\gamma_i=\gamma\) (CA1c). *Proof.* \(A=V\Gamma Q\) with \(\Gamma=\mathrm{diag}(\gamma_i)\) is similar to \((V\Gamma)^{1/2}Q(V\Gamma)^{1/2}\succ 0\), so it is stable and the mean is \(\arg\min J_T\). Let \(\mathcal L(X)=AX+XA^\top\), with \(\mathcal L(\Sigma)=2V\). For \(\Sigma_0=(\gamma_{\min}Q)^{-1}\), \(\mathcal L(\Sigma_0)=2V\Gamma/\gamma_{\min}\succeq 2V\). Since \(\mathcal L^{-1}(Y)=\int_0^\infty e^{-At}Ye^{-A^\top t}\mathrm dt\) preserves order, \(\Sigma\preceq\Sigma_0\), and the lower bound follows the same way. Then \(\tfrac12\mathrm{Tr}(Q\Sigma)\) is bracketed by \(\tfrac12\mathrm{Tr}(Q\Sigma_0)=d/(2\gamma_{\min})\) and \(d/(2\gamma_{\max})\). □

So an aligned team with unequal \(\sigma N_e\) still settles at the team optimum, and its excess is set by its weakest-selected and strongest-selected members, whatever their speeds. *Checks (NUMERICAL).* s5a: a potential LQ game gives \(\Sigma=(\nabla^2\Psi)^{-1}\) at speed ratios 0.1, 1 and 10 to \(2\times10^{-16}\). s5b: opposed coupling (\(J_1=\tfrac12x_1^2+1.5x_1x_2\), \(J_2=x_2^2-1.5x_1x_2\)) gives Lyapunov covariances that move with the speed ratio (spread 0.29) while the virial identity holds to \(10^{-15}\); Euler–Maruyama gives virials 1.006 and 0.995. s5g: in a nonlinear non-potential game the Monte Carlo virials are 1.005 and 1.006 about \(c=0\), and 0.984 and 0.999 about \(c=1\). s5c: 3,000 random teams (\(d=2\)–4, \(\gamma_i\in[0.2,5]\), random speeds) gave no violation of the bracket, and equal strengths gave \(d/(2\gamma)\) to \(2\times10^{-13}\).

## 5. Nonlinear strictly monotone non-potential games (CA5, CA5′)

CA2a covered linear–quadratic coupling. In nonlinear games under diffusion CA-D, stack the \(\beta\)-scaled gradients as \(F(x)=(\beta_i\nabla_i J_i(x))_{i=1}^n\) in \(\mathbb{R}^d\) so \(\mathrm dx=-VF(x)\,\mathrm dt+\sqrt{2V}\,\mathrm dW\).

**Theorem CA5 (strongly monotone non-potential games, Hodge split; PROVED (in-model)).** Suppose \(F\) is \(m\)-strongly monotone in the Euclidean norm (\((x-y)\cdot(F(x)-F(y))\ge m|x-y|^2\), \(m>0\)) and locally Lipschitz, with unique Nash equilibrium \(x^\star\) (\(F(x^\star)=0\)). Then for **every** choice of speeds \(V=\mathrm{diag}(v_i I_{d_i})\succ 0\):

1. *Existence and radius.* A unique stationary distribution with finite second moments exists, \(\mathbb{E}[(x-x^\star)\cdot F(x)]=d\), and
\[
\mathbb{E}|x-x^\star|^2\le \frac{d}{m}.
\]
2. *Hodge / Helmholtz split: only the radial part of \(R\) shifts the excess.* Write \(F(x)=\nabla\Psi(x)+R(x)\) with \(\Psi\) convex and \(\nabla\Psi(x^\star)=0\) (so \(R(x^\star)=0\), \(\Psi^\star=\Psi(x^\star)\)). Define the inward and outward radial moduli
\[
\rho_{\mathrm{in}}:=\sup_{x\ne x^\star}\left(-\frac{(x-x^\star)\cdot R(x)}{|x-x^\star|^2}\right)_+,\qquad
\rho_{\mathrm{out}}:=\sup_{x\ne x^\star}\left(\frac{(x-x^\star)\cdot R(x)}{|x-x^\star|^2}\right)_+.
\]
Then \(\mathbb{E}[\Psi]-\Psi^\star\le d(1+\rho_{\mathrm{in}}/m)\). When \(\Psi\) is quadratic, the exact excess is \(\mathbb{E}[\Psi]-\Psi^\star=\frac{d}{2}-\frac{1}{2}\mathbb{E}[(x-x^\star)\cdot R(x)]\), giving the two-sided bound
\[
\frac{d}{2}\left(1-\frac{\rho_{\mathrm{out}}}{m}\right)\le \mathbb{E}[\Psi]-\Psi^\star\le \frac{d}{2}\left(1+\frac{\rho_{\mathrm{in}}}{m}\right).
\]
In particular, if \(R\) is purely rotational around \(x^\star\) (\((x-x^\star)\cdot R(x)=0\) everywhere, e.g. a linear antisymmetric field \(R(x)=A(x-x^\star)\) with \(A^\top=-A\)), then \(\rho_{\mathrm{in}}=\rho_{\mathrm{out}}=0\) and \(\mathbb{E}[\Psi]-\Psi^\star=d/2\) **exactly**, for any speeds.
3. *Per-party regret.* If each \(J_i(\cdot,x_{-i})\) is \(\mu_i\)-strongly convex in \(x_i\) and \(\nabla_i J_i\) is \(L_i\)-Lipschitz in the joint state \(x\), then
\[
\mathbb{E}[R_i]=\mathbb{E}\bigl[J_i(x)-\min_{y_i}J_i(y_i,x_{-i})\bigr]\le \frac{L_i^2 d}{2\mu_i m}.
\]

*Proof.* (1) Consider the Lyapunov function \(U(x)=\tfrac12(x-x^\star)^\top V^{-1}(x-x^\star)\). Its generator gives \(\mathcal L U(x)=-(x-x^\star)\cdot F(x)+d\le -m|x-x^\star|^2+d\), which establishes positive recurrence, uniqueness, and finite second moments; summing CA2 with \(c_i=x_i^\star\) gives \(\mathbb{E}[(x-x^\star)\cdot F(x)]=d\), and strong monotonicity gives \(m\mathbb{E}|x-x^\star|^2\le d\). (2) Convexity of \(\Psi\) gives \(\Psi(x)-\Psi^\star\le (x-x^\star)\cdot\nabla\Psi(x)=(x-x^\star)\cdot F(x)-(x-x^\star)\cdot R(x)\le (x-x^\star)\cdot F(x)+\rho_{\mathrm{in}}|x-x^\star|^2\); taking expectations yields \(d(1+\rho_{\mathrm{in}}/m)\). For quadratic \(\Psi\), \(\Psi(x)-\Psi^\star=\tfrac12(x-x^\star)\cdot\nabla\Psi(x)\), so taking expectations gives \(\frac{d}{2}-\frac12\mathbb{E}[(x-x^\star)\cdot R(x)]\), and bounding \(\mp(x-x^\star)\cdot R(x)\) by \(\rho_{\mathrm{in/out}}|x-x^\star|^2\) with \(0\le\mathbb{E}|x-x^\star|^2\le d/m\) yields both sides. (3) By \(\mu_i\)-strong convexity of \(J_i(\cdot,x_{-i})\), \(R_i(x)\le\frac{1}{2\mu_i}|\nabla_i J_i(x)|^2=\frac{1}{2\mu_i}|\nabla_i J_i(x)-\nabla_i J_i(x^\star)|^2\le\frac{L_i^2}{2\mu_i}|x-x^\star|^2\), and \(\mathbb{E}|x-x^\star|^2\le d/m\). □

**Corollary CA5′ (with exogenous translation drift; PROVED (in-model)).** In translation-invariant coordinates \(z=x-\theta_t\) where the exogenous world target \(\theta_t\) undergoes Brownian drift with covariance \(2Q\,\mathrm dt\) alongside adaptation noise \(2V\,\mathrm dt\) (\(\mathrm dz=-VF(z)\,\mathrm dt+\sqrt{2V}\,\mathrm dW_a-\sqrt{2Q}\,\mathrm dW_w\)), the generator of \(U(z)=\tfrac12(z-z^\star)^\top V^{-1}(z-z^\star)\) has trace term \(\mathrm{Tr}(V^{-1}(V+Q))=d+\mathrm{Tr}(V^{-1}Q)\). Replacing \(d\) by \(d+\mathrm{Tr}(V^{-1}Q)\) leaves every bound in CA5 intact.

*Checks (NUMERICAL).* s6a: five parameterizations of \(F(x)=Sx+a(-x_2,x_1)+b(\tanh x_2,-\tanh x_1)\) across speeds \((1,1), (1,0.3), (1,0.2), (0.3,1)\) all give virial sum \(1.987\)–\(2.009\) against \(d=2\), \(\mathbb{E}|x|^2\le d/m\), \(\mathbb{E}[\Psi]\) inside the two-sided Hodge bracket, per-party regret below \(L_i^2 d/(2\mu_i m)\), and exact \(b=0\) antisymmetric rotation at \(\mathbb{E}[\Psi]=0.994\approx 1\). s6b: adding drift \(Q=\mathrm{diag}(0.4,0.2)\) with \(V=\mathrm{diag}(1.0,0.5)\) gives virial \(2.815\) against \(d+\mathrm{Tr}(V^{-1}Q)=2.8\), \(\mathbb{E}|z|^2=2.113\le 4.677\), and \(\mathbb{E}[\Psi]=1.412\in[1.128,1.672]\).

## 6. Mismatched strengths in the discrete chain (CA6, P1–P3) and refutation of the single-basin bracket

We now return to the discrete substitution chain (§2–§3) for one team cost \(J\) shared across \(n\) parties with unequal strengths \(\gamma_i=\beta_i s_i\).

**Theorem CA6 (perturbative tree bound and low-temperature limit; PROVED (in-model)).**
1. *(a) Perturbative Markov-chain-tree bound.* Let \(Q_0\) be a reversible matched reference chain at strength \(\bar\gamma\) (\(\pi_0\propto e^{-\bar\gamma J}\)) and \(Q_1\) a mismatched chain on the same connected graph of \(|S|\) states, with \(|\log(q_1(x\to y)/q_0(x\to y))|\le\eta\) on every directed edge and \(a=(|S|-1)\eta\). Then for every state \(x\),
\[
e^{-2a}\le \frac{\pi_1(x)}{\pi_0(x)}\le e^{2a},\qquad \mathrm{TV}(\pi_1,\pi_0)\le\tanh\frac{a}{2}\le\tanh a,\qquad \mathbb{E}_{\pi_1}[J-J^\star]\le e^{2a}\,\mathbb{E}_{\pi_0}[J-J^\star].
\]
*Proof.* Every directed spanning tree rooted at \(x\) has \(|S|-1\) edges, so its tree weight changes by a factor in \([e^{-a},e^a]\); summing over trees (Freidlin & Wentzell 1984/2012, Ch. 6) gives unnormalized weights \(W_1(x)/W_0(x)\in[e^{-a},e^a]\). Normalizing gives \(e^{-2a}\le\pi_1/\pi_0\le e^{2a}\) and the excess bound; the worst-case TV over \(W_1/W_0\in[e^{-a},e^a]\) puts \(e^a\) on mass \(p=(e^a+1)^{-1}\) and \(e^{-a}\) on \(1-p\), yielding \((e^a-1)/(e^a+1)=\tanh(a/2)\). □
*(Honest caveat.)* Because \(a\) grows with \(|S|-1\), this bound is informative only for tiny perturbations (\(\eta\ll 1/|S|\)) and saturates at \(\mathrm{TV}\le 1\) for moderate mismatch (compare Candogan, Ozdaglar & Parrilo 2013 for near-potential Markov comparisons).
2. *(b) Low-temperature limit in a single unilateral basin.* If \(J\) on a finite connected product graph has a **unique** (strict) unilateral local minimum \(x^\star\) (necessarily the global minimum) and \(\gamma_i=\lambda c_i\) with fixed \(c_i>0\) and clocks \(u_i>0\), then \(\pi_\lambda(x^\star)\to 1\) as \(\lambda\to\infty\). *Proof.* By P4 (§9 F6), every state \(x\ne x^\star\) has a strictly downhill unilateral path to \(x^\star\) of zero resistance, giving stochastic potential \(\mathrm{SP}_c(x^\star)=0\), while every tree rooted at \(x\ne x^\star\) must exit \(x^\star\) uphill, giving \(\mathrm{SP}_c(x)>0\). □

### The finite-\(\gamma\) single-basin bracket is FALSE

An earlier exploratory note asked whether, whenever \(J\) has a single unilateral local minimum, the mismatched expectation \(\mathbb{E}_\pi[J]\) always stays inside the matched Gibbs bracket \([E_{\mathrm{Gibbs}}(\gamma_{\max}),\,E_{\mathrm{Gibbs}}(\gamma_{\min})]\), where \(E_{\mathrm{Gibbs}}(\gamma)=\sum_x J(x)e^{-\gamma J(x)}/\sum_x e^{-\gamma J(x)}\). **Random tests missed the violations:** 1,155 random single-basin draws across exploratory runs (including 400 random 2D/3D grids) produced zero violations, creating the false appearance of a conjecture. **Targeted search and analysis prove the bracket is FALSE:**

1. *Local negative derivative (`sign_search`).* In the single-basin \(2\times 2\) landscape \(J=\begin{pmatrix}0.867 & 0.2\\ 0.063 & 0.058\end{pmatrix}\) at matched \(\gamma=12.9466\), \(u=(3.9406,10.7713)\), party 2 has sensitivity \(a_2/\mathrm{Var}=-0.01130<0\) (see P1 below). Increasing \(\gamma_2=\gamma+\varepsilon\) immediately pushes \(\mathbb{E}[J]\) **above** \(E_{\mathrm{Gibbs}}(\gamma_{\min})\) (excess \(1.56\times 10^{-7}\), \(1.57\times 10^{-6}\), \(7.96\times 10^{-6}\) at \(\varepsilon=0.01,0.1,0.5\)).
2. *Explicit \(2\times 2\) single-basin counterexample.* On
\[
J=\begin{pmatrix}0.2487 & 1.0\\ 0.0 & 0.0161\end{pmatrix},\qquad c=(6.23,\,60),\qquad u_2/u_1=105.142,
\]
\(J\) has one unilateral local minimum at \((1,0)\). Yet \(\mathbb{E}_\pi[J]=0.037287\) while the Gibbs bracket is \([0.004438,\,0.032729]\), exceeding the upper endpoint by \(0.004558\) (\(16.1\%\) of the bracket width).
3. *Scale-separated \(2\times m\) entropic family.* Take \(x_1\in\{0,1\}\), \(x_2\in\{0,\dots,m-1\}\), with \(J(1,j)=\varepsilon j\) (near-free options), \(J(0,0)=\Delta>0\), and \(J(0,j>0)=B\) (blocked; the numerical family holds \(B=10\)). Here \((1,0)\) is the unique unilateral minimum. Send \(\varepsilon\to 0\) and \(\gamma_2\to\infty\) with \(\gamma_1\varepsilon\ll 1\ll\gamma_2\varepsilon\) at fixed \(\gamma_1\), \(\Delta\), and barrier height \(B\). Party 2 then pins both rows at \(j=0\), so the chain reduces to the two states \((1,0)\) (cost \(0\)) and \((0,0)\) (cost \(\Delta\)), and party 1's balance gives
\[
\mathbb{E}_\pi[J]\;\longrightarrow\;\frac{\Delta e^{-\gamma_1\Delta}}{1+e^{-\gamma_1\Delta}}.
\]
The matched Gibbs law at \(\gamma_{\min}=\gamma_1\) still includes the barrier states \((0,j>0)\),
\[
E_{\mathrm{Gibbs}}(\gamma_1)\;\longrightarrow\;\frac{\Delta e^{-\gamma_1\Delta}+B(m-1)e^{-B\gamma_1}}{m+e^{-\gamma_1\Delta}+(m-1)e^{-B\gamma_1}}.
\]
At \(\gamma_1=1\), \(\Delta=0.5\), \(B=10\), the ratio of those limits tends to \(415.8\) as \(m\to\infty\), and stays bounded. The arrow
\[
\frac{\mathbb{E}_\pi[J]}{E_{\mathrm{Gibbs}}(\gamma_{\min})}\;\longrightarrow\;\frac{m+e^{-\gamma_1\Delta}}{1+e^{-\gamma_1\Delta}}
\]
is the limit only if the barrier states are deleted or \(B\to\infty\) with \(m B e^{-\gamma_1 B}\) kept negligible against \(\Delta e^{-\gamma_1\Delta}\); in that limit the ratio is unbounded in \(m\). The finite chain at \(m=64\) (\(\varepsilon=10^{-5}\), \(c_1=1\), \(c_2=10^6\)) already has ratio \(34.64>1\), which refutes the bracket (mechanism: **entropy** — strong selection on one party strips the weak party's near-free alternatives, raising the relative weight of its costly excursions).

### What holds instead: P1, P2, P3

**Proposition P1 (local criterion near matched strengths; PROVED (in-model)).** Let \(\gamma=\gamma_0\mathbf{1}\) give \(\pi_0\propto e^{-\gamma_0 J}\), write \(L_i=-Q_i(\gamma_0)\) for party \(i\)'s negative generator, \(L=\sum_i L_i\), and \(\tilde J=J-\mathbb{E}_{\pi_0}[J]\). Then
\[
\left.\frac{\partial \mathbb{E}_\gamma[J]}{\partial \gamma_i}\right|_{\gamma=\gamma_0\mathbf{1}}=-a_i,\qquad a_i:=\langle L_i J,\,L^{-1}\tilde J\rangle_{\pi_0},\qquad \sum_{i=1}^n a_i=\mathrm{Var}_{\pi_0}(J).
\]
To first order in \(\gamma-\gamma_0\mathbf{1}\), the Gibbs bracket holds for all small perturbations if and only if \(a_i\ge 0\) for every party \(i\). Moreover, when the generators \(L_i\) commute in \(L^2(\pi_0)\) (for example, when \(J\) is separable across parties, in which case the bracket holds globally at all \(\gamma\)), every \(a_i\ge 0\).

*Proof.* Differentiating \(\pi^\top L=0\) at \(\gamma_0\mathbf{1}\) gives \((\partial_i\pi)^\top L=-\pi_0^\top\partial_i L_i\). Differentiating detailed balance \(\pi_{\gamma_i}(x)q_i(x\to y;\gamma_i)=\pi_{\gamma_i}(y)q_i(y\to x;\gamma_i)\) gives \((\pi_0^\top\partial_i L_i)(y)=\pi_0(y)(L_i J)(y)\). Solving \(Lh=\tilde J\) (\(\mathbb{E}_{\pi_0}[h]=0\)) yields \(\partial_i\mathbb{E}[J]=(\partial_i\pi)^\top Lh=-\langle L_i J,h\rangle_{\pi_0}=-a_i\), and \(\sum_i a_i=\langle L\tilde J,L^{-1}\tilde J\rangle_{\pi_0}=\mathrm{Var}_{\pi_0}(J)\). Since \(E_{\mathrm{Gibbs}}(\gamma_0+\delta)=\mathbb{E}_{\pi_0}[J]-\mathrm{Var}_{\pi_0}(J)\delta+O(\delta^2)\), \(\sum_i a_i\delta_i\) lies between \(\mathrm{Var}(\pi_0)\min_i\delta_i\) and \(\mathrm{Var}(\pi_0)\max_i\delta_i\) for all small \(\delta\) iff every \(a_i\ge 0\). When \([L_i,L_j]=0\) in \(L^2(\pi_0)\), \(L_i\) and \(L^{-1}\) are simultaneously diagonalizable PSD operators, so \(a_i\ge 0\). □

**Proposition P2 (discrete PL flux bound, with explicit loose constants; PROVED (in-model)).** On a finite connected product graph where \(J\) has a single unilateral local minimum \(J^\star=\min_x J(x)\), define the uphill flux at \(x\) by \(U(x):=\sum_{i=1}^n\sum_{y\sim_i x,\,J(y)>J(x)} u_i\varphi_i(J(y)-J(x))\bigl(J(y)-J(x)\bigr)\) and the discrete Polyak–Łojasiewicz steepness by
\[
\theta:=\min_{x:\,J(x)>J^\star}\frac{\max_{y\sim x}\bigl(J(x)-J(y)\bigr)_+}{J(x)-J^\star}>0.
\]
Then
\[
\mathbb{E}_\pi[J-J^\star]\le \frac{N_{\max}\,\max_x U(x)}{u_{\min}\,\theta}.
\]
*Proof.* Let \(V(x)=J(x)-J^\star\ge 0\). Because every beneficial move has Moran fixation probability \(\varphi_i(\Delta J<0)\ge 1/N_i\ge 1/N_{\max}\), the steepest downhill move from any \(x\) with \(J(x)>J^\star\) contributes at least \(u_{\min}\theta V(x)/N_{\max}\) to \(-(QV)(x)\), while all uphill moves contribute at most \(U(x)\). Thus \((QV)(x)\le \max_{x'}U(x')-(u_{\min}\theta/N_{\max})V(x)\) for all \(x\). Taking expectations under \(\pi\) (\(\mathbb{E}_\pi[QV]=0\)) gives the bound. □

Each summand in \(U(x)\) is bounded by \(u_i\kappa(N_i,\beta_i)\) with \(\kappa(N,\beta)=\sup_{\Delta>0}\varphi(\alpha,\Delta,N)\Delta=O(1/(N\beta))\) (for large \(N\), \(N\beta\kappa(N,\beta)\to\sup_{y>0} y^2/(e^y-1)\approx 0.648\)). **Explicit looseness caveat:** because \(N_{\max}/(u_{\min}\theta)\) mixes the slowest clock and worst steepness with the fastest uphill flux, the bound is conservative (on 400 random single-basin grids, 0 violations, median ratio \(\mathbb{E}[J-J^\star]/\text{bound}=0.058\), max \(0.490\)).

**Proposition P3 (exact on tree-shaped state graphs; PROVED (in-model)).** If the active move graph of the chain is a tree (no cycles), Kolmogorov's cycle criterion holds trivially for **any** choice of party strengths \(\gamma_i\) and edge clocks \(u_i>0\). Thus the chain is reversible and \(\pi(x)\propto e^{-\Psi_c(x)}\), where \(\Psi_c(x)\) is the \(\gamma\)-weighted path integral of \(\Delta J\) along the unique path from a fixed root \(x_0\) to \(x\), independent of \(u_i\).

*Checks (NUMERICAL).* s7a: 100/100 random 3×3 perturbation trials satisfy \(e^{-2a}\le \pi_1/\pi_0\le e^{2a}\), \(\mathrm{TV}\le\tanh(a/2)\), and \(\mathbb{E}_{\pi_1}[J-J^\star]\le e^{2a}\mathbb{E}_{\pi_0}[J-J^\star]\). s7b: on a 6×6 single-basin grid with 1:8 mismatch, \(\pi_\lambda(x^\star)\) rises from \(0.144\) (\(\lambda=2\)) to \(0.99993\) (\(\lambda=128\)). s7c: verifies \(a_2/\mathrm{Var}=-0.01130\), the \(2\times 2\) counterexample (\(16.1\%\) above upper bracket), and the \(2\times m\) entropic family at \(m=64\) (ratio \(34.64\) with \(\varepsilon=10^{-5},\Delta=0.5,c_1=1,c_2=10^6\); with the barrier held at 10 the scale-separation ratio tends to \(415.8\) as \(m\to\infty\)). s7d: 400/400 random single-basin grids satisfy P2 with median tightness \(0.0579\) and max \(0.4903\). s7e: on a 6-node two-party tree with mismatched strengths \((2.5,14)\) and speeds \((1.3,7.9)\), \(\pi\) matches \(e^{-\Psi_c}/Z\) to \(6\times 10^{-17}\) in TV and detailed balance holds to \(3.5\times 10^{-18}\).

## 7. Drift plus co-adaptation (CA7; PROVED (in-model))

Combine CA2a/CA3 with exogenous translation drift of the target \(\theta_t\) (noise covariance \(2Q\,\mathrm dt\) alongside adaptation diffusion \(2V\,\mathrm dt\), with party diagonal blocks \(Q_{ii}\)):
\[
\mathrm dz=-VKz\,\mathrm dt+\sqrt{2V}\,\mathrm dW_a-\sqrt{2Q}\,\mathrm dW_w,\qquad K=S+A,\quad S=S^\top\succ 0,\quad A=-A^\top,
\]
where \(\Psi(z)=\tfrac12 z^\top S z\) is the potential part and \(A\) is any antisymmetric non-potential coupling.

**Theorem CA7 (LQ drift plus co-adaptation; PROVED (in-model)).**
1. *Exact potential-part excess.* For **any** antisymmetric coupling \(A\), any drift covariance \(Q\succeq 0\), and any speeds \(V=\mathrm{diag}(v_i I_{d_i})\succ 0\), \(-VK\) is Hurwitz and
\[
\mathbb{E}[\Psi]-\Psi^\star=\frac{1}{2}\left(d+\sum_{i=1}^n\frac{\mathrm{Tr}\,Q_{ii}}{v_i}\right).
\]
2. *Per-party virial.* Blockwise on party \(i\), \(\beta_i\,\mathbb{E}[z_i\cdot\nabla_i J_i(z)]=\mathrm{Tr}_i(K\Sigma)=d_i+\mathrm{Tr}\,Q_{ii}/v_i\).
3. *Team mismatch bracket with drift.* When \(J_i=s_i J_T\) with \(J_T=\tfrac12 z^\top S z\) and \(K=\Gamma S\) (\(\gamma_i=\beta_i s_i\)), let the eigenvalues of \(V^{-1/2}QV^{-1/2}\) lie in \([q_{\min},q_{\max}]\). Then for all speeds,
\[
\frac{d(1+q_{\min})}{2\gamma_{\max}}\le \mathbb{E}[J_T]-J_T^\star\le \frac{d(1+q_{\max})}{2\gamma_{\min}}.
\]
4. *Negative finding on per-party regret.* Under coupling plus drift, per-party expected regret \(\mathbb{E}[R_i]\) does **not** equal the naive uncoupled scaling \(\frac{d_i}{2\beta_i}\bigl(1+\frac{\mathrm{Tr}\,Q_{ii}}{v_i d_i}\bigr)\): breaking detailed balance via \(Q\not\propto V\) shifts the conditional variance of \(z_i\mid z_{-i}\).

*Proof.* The stationary covariance solves \(VK\Sigma+\Sigma K^\top V=2V+2Q\). Left-multiplying by \(V^{-1}\) gives \(K\Sigma+V^{-1}\Sigma K^\top V=2I+2V^{-1}Q\). Taking the \(i\)-th block trace gives \(2\mathrm{Tr}_i(K\Sigma)=2d_i+2\mathrm{Tr}\,Q_{ii}/v_i\), proving (2). Summing over \(i\) and using \(\mathrm{Tr}(A\Sigma)=0\) (antisymmetry of \(A\) against symmetric \(\Sigma\)) gives \(\mathrm{Tr}(S\Sigma)=d+\sum_i\mathrm{Tr}\,Q_{ii}/v_i\), proving (1). For (3), \(q_{\min}V\preceq Q\preceq q_{\max}V\) implies \(2(1+q_{\min})V\preceq 2V+2Q\preceq 2(1+q_{\max})V\), and the order-preserving Lyapunov inverse of CA3 brackets \(\Sigma\) between \((1+q_{\min})(\gamma_{\max}S)^{-1}\) and \((1+q_{\max})(\gamma_{\min}S)^{-1}\). □

*Checks (NUMERICAL).* s8a: across 2,000 random 3-party LQ systems with non-symmetric \(K=S+A\) and correlated \(Q\), the potential excess matches \(\frac12(d+\sum\mathrm{Tr}\,Q_{ii}/v_i)\) to relative error \(1.1\times 10^{-14}\), per-party virials match to \(2.8\times 10^{-13}\), and 0/2,000 violate the drift mismatch bracket. s8b: in a coupled 2-party potential game with drift, static (\(Q=0\)) regrets match \(1/(2\beta_i)=0.1,0.2\) to machine precision, while with drift actual regrets are \(0.1330\) and \(0.3196\) against the naive formula's \(0.1300\) and \(0.3500\).

## 8. The parent's upkeep, lifted (CT34 under selection)

CT34 says that a team's optimized cost enters the parent exactly as upkeep when the parent sees the team only through quantities fixed before the team optimizes. Under co-selection, with parent design \(x\), team design \(y\), \(J=F(x)+G(y;\theta(x))\), the parent selected on \(J\) at strength \(\beta_P\) and the team on \(G\) at \(\beta_T\), the game is an exact potential game with potential \(J\) (weights 1, 1).

**Theorem CA4 (PROVED (in-model)).**
1. *Fixed \(\theta\) (CT34 (ii)).* \(J=F(x)+G(y)\) has no mixed term, so the \(\beta\)-scaled game has potential \(\beta_PF+\beta_TG\) for **any** \(\beta_P,\beta_T\). The stationary distribution is the product \(e^{-\beta_PF(x)}e^{-\beta_TG(y)}\), and for quadratic wells \(\mathbb{E}[J]=F^\star+d_P/(2\beta_P)+J_T^\star+d_T/(2\beta_T)\). **The team enters the parent as upkeep \(J_T^\star+d_T/(2\beta_T)\)**: CT34's upkeep plus the team's own selection scatter, a constant.
2. *\(\theta(x)\), equal strengths \(\beta\).* \(\pi\propto e^{-\beta J}\), and the parent's marginal is \(\propto\exp(-\beta[F(x)+\mathcal F_T(\theta(x))])\) with the team's free energy \(\mathcal F_T(\theta)=-\beta^{-1}\log\sum_ye^{-\beta G(y;\theta)}\). For a quadratic team well, \(\mathcal F_T=J_T^\star(\theta)+(2\beta)^{-1}\log\det H_T(\theta)+\text{const}\). The parent sees the team through its free energy, not its optimized cost. The correction moves the parent's argmin only if the team's curvature depends on what the parent passes down, and it is \(O(1/\beta)\).
3. *\(\theta(x)\), unequal strengths.* Reversibility fails (CA1a). In the LQ diffusion model only own gradients enter, and \(\nabla_yG=\nabla_yJ\), so this is CA3 with \(s=1\): the mean is \(\arg\min J\), and \(d/(2\beta_{\max})\le\mathbb{E}[J]-J^\star\le d/(2\beta_{\min})\).

*Proof.* (1), (2) by CA1 and integration over \(y\); the Gaussian integral gives the \(\log\det\). (3) as stated. □

*Check (NUMERICAL, s5h).* With \(h(x)=1.5+0.8\tanh x\), the parent's exact marginal matches the free-energy form to \(7\times10^{-17}\) in total variation, against 0.029 for "team as upkeep only". With \(\theta\) fixed and \(\beta_T=11\), the team's expected scatter is 0.045455 against \(1/(2\beta_T)=0.045455\).

## 9. Failure classes, each with a minimal counterexample (PROVED (in-model))

Each is a place where the near-minimizer conclusion does not follow. None settles the hypothesis either way; misses are open items to diagnose (measurement, inputs, hidden cost, or the claim itself).

- **F1. Non-potential coupling with no pure equilibrium: permanent cycling.** Matching pennies with costs in \(\{0,1\}\): \(J_1=\mathbf 1[x_1\ne x_2]\), \(J_2=\mathbf 1[x_1=x_2]\), binary designs, equal clocks and sizes. Every state has one downhill and one uphill exit, and in-rates equal out-rates, so \(\pi\) is uniform at **every** \(\beta\). Then \(\mathbb{E}[J_i]=\tfrac12\) while each best reply costs 0: regret does not shrink with selection. A probability current circulates (0.025, 0.106, 0.223 at \(\beta=1,5,20\); check s4).
- **F2. Spiral instability (unstable focus) in J's class (costs ≥ 0, a unique Nash point).** Three parties, \(J_i=\tfrac12(x_i+cx_{i+1})^2\) (indices mod 3), each chasing the next. The game Jacobian is \(I+cP\), with eigenvalues \(1+c\,e^{2\pi ik/3}\). With equal \(v_i\beta_i\), the unique Nash point \(x=0\) is unstable, through a complex pair (an unstable focus: trajectories spiral outward rather than forming a periodic orbit in the linear model), iff \(c>2\) (min real part 0.25, 0.05, −0.05, −0.5 at \(c=1.5,1.9,2.1,3\); check s5d). Not \(\beta\)-potential: the cross-curvatures are \(c\beta_i\) one way and 0 the other.
- **F3. A system whose action moves its own world by more than one-for-one.** System cost \(J_s=\tfrac12(x-\theta)^2\ge 0\); the world relaxes on \(J_w=\tfrac12(\theta-gx)^2\), so it copies the design with gain \(g\). For \(g>0\) this particular model is a weighted potential game (\(\beta_w=\beta_s/g\) makes it \(\beta\)-potential). An arbitrary pair of costs, each with a cost of its own, need not be. \(\det\nabla^2\Psi\propto 1-g\). For \(g>1\) the potential is a saddle unbounded below (\(e^{-\Psi}\) is not integrable). With any strengths and speeds, \(\det(VK)\propto 1-g<0\), so the coupled system runs away even though every cost is \(\ge 0\) (check s5e). At \(g=1\) the determinant is zero: there is no confining normalizable quadratic Gibbs distribution on the unbounded domain, and this note does not assert deterministic runaway at equality. This copy gain is not THEORY's drift-intensity lever (CL11/K17), which stays open, and it is not T61's heat accounting for a passive plant. F4 below is delayed push-back with gain below −1, not this positive gain.
- **F4. Acting faster than the feedback can be tracked (delay).** \(\dot x=-k\,(x(t)-g\,x(t-\tau))\) with \(k=v\beta\), the system seeing a world that pushes back with gain \(g<-1\) after delay \(\tau\). Without delay it is stable for every \(k\). With delay it is asymptotically stable iff \(k\tau<\arccos(1/g)/\sqrt{g^2-1}\) (Hayes 1950; 1.209 at \(g=-2\); neutral oscillation at equality; the amplitude ratio is \(5\times10^{-5}\) at 0.8× the bound and 193 at 1.2×; check s5f). **Stronger selection or faster origination (larger \(k\)) can destabilize**, so with delayed feedback "strongly selected" does not imply "near the minimizer".
- **F5. Bode / feedback limits move the minimum, not the gap.** When the coupled loop acts on a world with open-loop unstable poles \(p_k\), every stabilizing design with an open loop of relative degree at least two obeys \(\int_0^\infty\ln|S(i\omega)|\,\mathrm d\omega=\pi\sum_k\mathrm{Re}\,p_k\) (Freudenberg & Looze 1985; Seron, Braslavsky & Goodwin 1997). That is a floor inside \(J^\star\), so it raises the minimum. Selection then brings \(J\) near a minimum that already includes the floor. Whether the sampled-read waterbed of `theory/DYNAMICS.md` §5 enters \(\arg\min J\) is unchanged and **OPEN**. F4 is where feedback limits do break the near-minimizer conclusion: through the adaptation dynamics, not through \(J^\star\).
- **F6 (Proposition P4). Multi-basin trapping under mismatched strong selection: resistance trees and gatekeepers.** Let a team cost \(J\) on a finite connected product graph have multiple unilateral local minima (basins), with party strengths scaling as \(\gamma_i=\lambda c_i\) (\(c_i>0\) fixed, \(\lambda\to\infty\)) and positive clocks \(u_i>0\). Each directed edge \(x\to y\) moved by party \(i\) has rate \(q_\lambda(x\to y)=\Theta(e^{-\lambda r_c(x\to y)})\) with resistance \(r_c(x\to y)=c_i\bigl(J(y)-J(x)\bigr)_+\) (more generally \(c_i(J_i(y)-J_i(x))_+\) for any game \((J_i)\); clock prefactors \(u_i\) give \(O(1)\) and vanish in \(\lambda^{-1}\log\)). By the Markov-chain-tree / stochastic-stability theorem (**Young 1993**, *Econometrica* 61:57–84; **Freidlin & Wentzell 1984/2012**, Ch. 6), as \(\lambda\to\infty\) the stationary law \(\pi_\lambda\) concentrates on the state(s) minimizing the **stochastic potential**
\[
\mathrm{SP}_c(x):=\min_{T\in\mathcal T(x)}\sum_{(u\to v)\in T} r_c(u\to v),
\]
and **adaptation clock speeds \(u_i\) drop out completely**. For two basins \(A\) and \(B\) whose lowest-resistance escape paths require party \(i\) to climb uphill increments summing to \(a_i\) out of \(A\) and \(b_i\) out of \(B\) (\(R_c(A\to B)=\sum_i c_i a_i\), \(R_c(B\to A)=\sum_i c_i b_i\)),
\[
\lim_{\lambda\to\infty}\frac{1}{\lambda}\log\frac{\pi_\lambda(B)}{\pi_\lambda(A)}=R_c(B\to A)-R_c(A\to B)=\sum_i c_i b_i-\sum_i c_i a_i,
\]
so the worse basin \(B\) is selected iff \(\sum_i c_i b_i>\sum_i c_i a_i\).
*Method attribution and organizational reading.* This is an **application of Young's (1993) and Freidlin–Wentzell's stochastic-stability method to cost-of-judgment co-adaptation, not a new method**. Plain organizational reading: **strongly selected members act as gatekeepers on exits** — under strong selection, a group settles into whichever arrangement its most strongly selected members would have to take a temporary loss to leave, so an arrangement they guard sticks even when a better one exists, and how fast anyone adapts does not change the winner in that limit.
*Check (NUMERICAL, s9).* On \(J=\begin{pmatrix}0.0 & 10.0\\ 1.0 & 0.3\end{pmatrix}\) (\(A=(0,0)\) with \(J=0\), \(B=(1,1)\) with \(J=0.3\), saddle \((1,0)\) with \(J=1.0\)) at \(c=(1,3)\), spanning trees confirm \(\mathrm{SP}_c(A)=2.1\) and \(\mathrm{SP}_c(B)=1.0\); the predicted threshold \(c_2/c_1>1/0.7\approx 1.4286\) is confirmed at \(\lambda=40\) (\(\pi_B=0.027, 0.310, 0.707, 0.992\) at \(c_2/c_1=1.3, 1.4, 1.46, 1.6\)); and at \(c=(1,3)\) the slope \(\lambda^{-1}\log(\pi_B/\pi_A)=1.1000\) is exact across speed ratios \(u_2/u_1\in\{1, 50, 1/50\}\).

- **Excluded (assumptions, not counterexamples).** Within-party frequency dependence (CA-B). Simultaneous revision: CA-C delivers one-at-a-time revision, and without it the Boltzmann form and potential-maximizer selection need not hold even in exact potential games (Alós-Ferrer & Netzer 2010). Copying that is only monotone in cost (A2-M; no Boltzmann form, as in the selection note). Non-quadratic wells (Laplace approximations only).

## 10. Prior art and what is new

| Piece | Status | Source |
|---|---|---|
| Logit (log-linear) revision in a potential game has a Boltzmann stationary distribution in the potential | KNOWN | Blume 1993; potential games, Monderer & Shapley 1996; textbook treatment, Sandholm 2010 (book, no Crossref DOI found) |
| Stochastic stability and resistance trees (\(\min\mathrm{SP}\) as noise vanishes) | KNOWN | Freidlin & Wentzell 1984 / 2012; Young 1993 |
| Near-potential games and Markov perturbation comparison | KNOWN | Candogan, Ozdaglar & Parrilo 2013 |
| The weak-mutation fixation ratio \(\exp(-\beta\Delta J)\), \(\beta=\alpha\nu\) | KNOWN | Sella & Hirsh 2005; the selection note SA1 |
| Reversibility iff cycle products balance | KNOWN | Kolmogorov 1936; Kelly 1979 (book) |
| Gibbs form and potential-maximizer selection depend on asynchronous revision | KNOWN | Alós-Ferrer & Netzer 2010 |
| Unequal rationality parameters make the stationary distribution depend on revision probabilities (2-player coordination, closed form) | KNOWN | Rajab, Anubi & Vasconcelos 2025, consistent with CA1a |
| Strict monotonicity implies stability of weighted gradient play; D-stability | KNOWN | Rosen 1965; Hofbauer & Sandholm 2009; Arrow & McManus 1958 |
| Delay stability bound | KNOWN | Hayes 1950 |
| Bode integral with unstable poles | KNOWN | Freudenberg & Looze 1985; Seron et al. 1997 |
| Virial / equipartition identity and Foster–Lyapunov drift for diffusions / chains | KNOWN techniques | standard (Itô; Markov chain tree / Foster–Lyapunov) |
| CA1 with the origination–fixation chain as the revision rule and unequal \(\beta_i\), as an iff | PROVED (in-model); new packaging, an immediate corollary of the above | this note |
| CA1b per-party regret \(d_i/(2\beta_i)\); team split into absolute potential-to-team gap plus scatter; CA1c equal \(\sigma N_e\) condition | PROVED (in-model); new packaging | this note |
| CA2 read per party for games; CA2a speed-free iff potential | PROVED (in-model); new packaging | this note |
| CA3 bracket for one team cost with mismatched strengths; CA7 drift + co-adaptation | PROVED (in-model); not found in the sources searched (a short search, not a review) | this note |
| CA4 lift of CT34: upkeep plus scatter; free energy; bracket | PROVED (in-model); new packaging of standard statistical mechanics | this note |
| CA5 / CA5′ Hodge split (radial-only shift) and regret bound for strongly monotone games | PROVED (in-model); application of standard monotone-operator / Itô bounds | this note |
| CA6 / P1–P3 discrete mismatch results and refutation of the finite-\(\gamma\) single-basin bracket | PROVED (in-model); new packaging (P2 constants loose) | this note |
| F6 / P4 gatekeeper selection across basins under mismatched selection | PROVED (in-model); application of Young 1993 and Freidlin–Wentzell, not a new method | this note |

A prior-art search on 21 November 2026 found no source stating CA3, CA4, or CA7 in this co-adaptation setting. That search was short, so "new" here means "not found", and any expert reader may know a source.

## 11. What is open

- **Which real couplings are \(\beta\)-potential games.** Shared-driver and aligned-share classes are (CT31, CA1c). Predator–prey, arms races and pursuit are not. A measurement test needs the cross-curvature symmetry \(\beta_i\,\partial^2J_i/\partial x_i\partial x_j=\beta_j\,\partial^2J_j/\partial x_j\partial x_i\), which is checkable in principle but has not been measured anywhere.
- **Non-monotone or non-strongly-monotone nonlinear games** (CA5 solves the \(m\)-strongly monotone diffusion case; bounds without strong monotonicity or outside CA-D stay open).
- **Tight finite-\(\gamma\) non-perturbative bounds for mismatched strengths in general discrete coupled chains** (the single-basin Gibbs bracket is FALSE; CA6(a) is perturbative, P2 has explicit loose constants, and P4/F6 is asymptotic in \(\lambda\to\infty\); finite-\(\lambda\) speed corrections and tight non-perturbative bounds stay open).
- **Drifting worlds under co-adaptation beyond Brownian translation drift** (CA5′ and CA7 solve Brownian translation drift; non-translation, non-Brownian, and discrete drifting worlds stay open).
- **Dual control** (acting to learn, Bar-Shalom & Tse 1974) is listed in `reviews/widenet_2026-11-20/SCAN.md` and is not treated here.
- **Whether Bode or the sampled-read waterbed changes \(\arg\min J\)** (`theory/DYNAMICS.md` §5) stays OPEN; F5 only places it.

## 12. Numerical checks

`tools/coadaptation_checks.py` (about 26 s at `nice -n 19`), run by `tools/test_coadaptation_checks.py` (23 tests). **NUMERICAL.**

## References

Verified on Crossref, 21 November 2026, America/New_York, unless marked as a book.

- Alós-Ferrer, C. & Netzer, N. 2010, *Games and Economic Behavior* 68:413–427, doi 10.1016/j.geb.2009.08.004, "The logit-response dynamics."
- Arrow, K. J. & McManus, M. 1958, *Econometrica* 26:448, doi 10.2307/1907624, "A Note on Dynamic Stability."
- Bar-Shalom, Y. & Tse, E. 1974, *IEEE Transactions on Automatic Control* 19:494–500, doi 10.1109/TAC.1974.1100635, "Dual effect, certainty equivalence, and separation in stochastic control."
- Blume, L. E. 1993, *Games and Economic Behavior* 5:387–424, doi 10.1006/game.1993.1023, "The Statistical Mechanics of Strategic Interaction."
- Candogan, O., Ozdaglar, A. & Parrilo, P. A. 2013, *Games and Economic Behavior* 82:66–90, doi 10.1016/j.geb.2013.07.001, "Dynamics in near-potential games."
- Freidlin, M. I. & Wentzell, A. D. 1984 (3rd ed. 2012), *Random Perturbations of Dynamical Systems*, Springer, doi 10.1007/978-1-4684-0176-9 (3rd ed. doi 10.1007/978-3-642-25847-3).
- Freudenberg, J. & Looze, D. 1985, *IEEE Transactions on Automatic Control* 30:555–565, doi 10.1109/tac.1985.1104004, "Right half plane poles and zeros and design tradeoffs in feedback systems."
- Hayes, N. D. 1950, *Journal of the London Mathematical Society* s1-25:226–232, doi 10.1112/jlms/s1-25.3.226, "Roots of the Transcendental Equation Associated with a Certain Difference-Differential Equation."
- Hofbauer, J. & Sandholm, W. H. 2009, *Journal of Economic Theory* 144:1665–1693, doi 10.1016/j.jet.2009.01.007, "Stable games and their dynamics."
- Kelly, F. P. 1979, *Reversibility and Stochastic Networks*, Wiley (book; no Crossref DOI used).
- Kolmogoroff, A. 1936, *Mathematische Annalen* 112:155–160, doi 10.1007/bf01565412, "Zur Theorie der Markoffschen Ketten."
- Monderer, D. & Shapley, L. S. 1996, *Games and Economic Behavior* 14:124–143, doi 10.1006/game.1996.0044, "Potential Games."
- Rajab, Fat-Hy O., Anubi, Olugbenga M. & Vasconcelos, Marcos M. 2025, *IEEE Control Systems Letters* 9:2741–2746, doi 10.1109/lcsys.2025.3641882, "Log-Linear Learning for Coordination With Heterogeneous Bounded Rationalities."
- Rosen, J. B. 1965, *Econometrica* 33:520, doi 10.2307/1911749, "Existence and Uniqueness of Equilibrium Points for Concave N-Person Games."
- Sandholm, W. H. 2010, *Population Games and Evolutionary Dynamics*, MIT Press (book; no Crossref DOI found).
- Sella, G. & Hirsh, A. E. 2005, *Proceedings of the National Academy of Sciences* 102:9541–9546, doi 10.1073/pnas.0501865102, "The application of statistical physics to evolutionary biology."
- Seron, M. M., Braslavsky, J. H. & Goodwin, G. C. 1997, *Fundamental Limitations in Filtering and Control*, Springer, doi 10.1007/978-1-4471-0965-5.
- Young, H. P. 1993, *Econometrica* 61:57–84, doi 10.2307/2951778, "The Evolution of Conventions."
