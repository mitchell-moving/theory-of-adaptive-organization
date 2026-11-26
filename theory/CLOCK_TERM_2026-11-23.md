# T68: the clock term — anticipating predictable change between paid looks costs heat

*Monday 23 November 2026, America/New_York. Written against `main` `d592662`. Labels follow `CORE.md:168`: **PROVED (in-model)** inside a named class; **KNOWN** published and credited, only for what the source states; **ELEMENTARY** a one-line consequence of a known inequality; **CONJECTURE**; **SPECULATION**; **OPEN**; **NUMERICAL**. `THEORY.md` is unchanged. No real-world data was opened. Nothing here bears on general relativity, quantum mechanics or holography, and nothing is claimed about them.*

*Review status. Sections 1–8 carry a result (class CK) that an independent reviewer checked on 23 November 2026, re-deriving the algebra, rerunning every script and adding the reviewer's own checks (`clock_term_checks/gen.py`, `clock_term_checks/cosloss.py`). Those sections are scoped exactly as that review scoped them. Section 9 (looks priced by the information they bring in) is new in this PR. A second independent reviewer checked it on 23 November 2026 (PR #248): re-derived the clockless stationarity, the small-clock expansion, \(b=a/2\) and the 4.83 trap by hand, reran every script (stored outputs reproduced byte for byte), and confirmed \(b/a=0.5\) and the global onset with separate code. The reviewer's edits are marked `[REVIEWER EDIT PR248]`.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

## 0. Bottom line (plain words)

- **A gap in the heat floor.** The floor at `CORE.md:70` charges \(kT\) times the learning rate. That charge is **zero for a world that changes predictably**, such as a regular rhythm, because deterministic change destroys no information. But a memory that must keep the phase *between paid looks* needs an internal clock, and a clock costs heat. The thermodynamic uncertainty relation (TUR, KNOWN) prices it: heat \(\ge kT\,\omega'^2/D\) for a clock with mean rate \(\omega'\) and phase diffusion \(D\). The repository already flagged the TUR as a second physics cost that GTAO did not use (`litmap/LITMAP.md:21`), and already recorded that an accurate clock needs throughput (`litmap/LITMAP.md:28`, `theory/BOOKENDS.md:272`, citing Cao et al. 2015). What is new to the repository is the term inside the cost and its closed form.
- **When a clock pays (class CK, fixed price per look).** With the loss written as \(a(\text{lag})^2/f^2+b\,D/f\), an internal clock appears exactly when one look costs more than \(c^*=2\kappa kT\,b/a\), where \(\kappa\ge1\) is the clock's excess over the TUR. That is \(6\kappa kT\) for the interval-averaged squared error, \(4\kappa kT\) for the error scored just before each look, and \(4\kappa kT\) for time-averaged error under looks that arrive at random (Poisson). The number is a fact about the scoring, not about clocks. Its independence from stake and frequency is forced by the scale symmetry of the small-angle model.
- **What the clock fixes, and what it does not.** Above onset the estimate deliberately lags (an under-advancing, shrunk estimate). The physical clock may run at any rate. The 1/3 loss share and the \(w^{1/3}\) scaling are **not** clock results: the no-clock design already has both, and the share is the repository's own share rule (`THEORY.md:101`).
- **Next step, done here (section 9): price each look by the information it brings in.** With looks on a schedule the memory knows, a perfectly regular world makes each look carry no new information, so the information price is zero and the CK price per look is really a timing price (section 9.1). With looks at times the memory cannot predict, a clean result comes out (section 9.3, PROVED in-model for the local onset, checked numerically for the global one): **a clock first pays exactly when the best clockless design's look brings in more than \(4\kappa/\lambda\) nats**, where \(\lambda\ge1\) is the look's excess over the Sagawa–Ueda floor. With both efficiencies at their floors that is 4 nats, about 5.8 bits. This is the fixed-price onset \(4\kappa kT\) with the price replaced by \(\lambda kT\) times the information, *exactly*, even though the information per look depends on the design. The reviewer's conjecture of "about \(6\kappa\) nats" holds in form, but the number is \(4\kappa/\lambda\) for random looks, and for scheduled looks there is no information threshold at all. The form "a pure number of nats" is itself forced by symmetry; the content is the value and the exact match.
- **How big a step this is.** A real fix to the floor's scope and a modest corollary of known inequalities, not a new principle. The searches did not find the closed form elsewhere, but a missing result in a search is not proof of novelty.

## 1. The GTAO method on this problem

1. **Write the cost, with named terms.** In the physical class (`CORE.md:27, 66`), the long-run rate is
   \[J=\underbrace{\kappa kT\,\frac{\omega'^2}{D}}_{\text{clock heat}}+\underbrace{c\,f}_{\text{looks}}+\underbrace{w\,\mathbb E[\ell]}_{\text{stake}\times\text{loss}},\qquad P(\text{ruin})\le\varepsilon_r\ \text{(slack here)}.\]
   - \(\omega\): the world's phase rate (known, stored once at zero ongoing heat: the frozen corner, `CORE.md:78`).
   - \(\omega',D\): the internal clock's mean rate and phase diffusion. \(\kappa\ge1\) is its excess over the TUR floor.
   - \(f\): the look rate. \(c\): the price of one look. In sections 2–8 it is an assumed summand (the five-term \(A\), `CORE.md:42`). In section 9 it becomes \(\lambda kT\times\)(information per look).
   - \(w\): the stake. \(\ell\): the squared phase error (small angle).
   The memory-bath heat floor \(\dot Q_M\ge kT\,\dot I_M\) (`CORE.md:70`) does not double count with the clock term: between looks the clock only loses information, so its own learning-rate contribution is \(\le 0\), and the TUR term is a separate cost.
2. **Find the minimum.** Closed form in section 2 (fixed price) and section 9 (information price).
3. **Read off the design.** No clock below onset; a clock with a deliberately lagging estimate above it; the split of the non-loss part of the cost between clock heat and looks.
4. **Scope.** Perfectly regular worlds (\(D_w=0\)), small angles, large stakes relative to look cost, autonomous current-counting clocks (section 5), a read price that is assumed (sections 2–8) or information-priced in a named readout class (section 9).
5. **What would be a measurement.** In a qualified, selected rhythm-tracker with a measured world rhythm, measured clock dissipation and phase diffusion, a measured cost per look and a measured stake, whether an internal clock is present exactly when the look cost exceeds the onset for that system's loss scoring and look statistics. No such system is qualified, and no data was opened. As claims about nature, the onset and the lag are predictions a qualified system could miss.

## 2. Class CK and its minimum (fixed price per look)

**Class CK.** The world is a phase \(\theta_w(t)=\theta_0+\omega t\), optionally with phase diffusion \(D_w\). Looks are perfect, at rate \(f\), at price \(c\) each. Between looks the memory carries the phase on an autonomous clock (mean rate \(\omega'\), diffusion \(D\)). Loss is squared phase error at stake \(w\).

**Known input.** **TUR (KNOWN):** for an integrated current in a nonequilibrium steady state of a Markov jump process or an overdamped diffusion, \(\mathrm{Var}/\mathrm{mean}^2\ge2/\Sigma\) (Barato and Seifert 2015; general proof Gingrich et al. 2016). A clock phase with \(\mathrm{Var}=2Dt\) and mean \(\omega't\) then has \(\dot Q_{\rm clock}\ge kT\,\omega'^2/D\). Write \(\dot Q_{\rm clock}=\kappa kT\,\omega'^2/D\), \(\kappa\ge1\). Brownian clocks: Barato and Seifert 2016.

**Cost (periodic looks, interval-averaged squared error).**
\[J(f,\omega',D)=\kappa kT\frac{\omega'^2}{D}+cf+w\Big[\frac{(\omega-\omega')^2}{3f^2}+\frac{D+D_w}{f}\Big].\]

**General loss.** For a loss \(a(\omega-\omega')^2/f^2+b\,D/f\) (\(a=1/3,b=1\) interval-averaged; \(a=1,b=2\) scored just before each look; \(a=1,b=2\) time-averaged under Poisson looks, whose age at a random time is exponential), with \(K=\kappa kT\) and \(D_w=0\):

**PROVED (in-model, class CK).** Re-derived independently by the reviewer (sympy, `clock_term_checks/gen.py`):
1. \(D^*=\omega'\sqrt{Kf/(bw)}\) and \(\omega-\omega'^*=\sqrt{Kb}\,f^{3/2}/(a\sqrt w)\).
2. \(J(f)=2\omega\sqrt{Kbw}\,f^{-1/2}+(c-Kb/a)f\).
3. **Onset.** A clock is optimal iff \(c>c^*=2Kb/a\). Interval-averaged: \(6\kappa kT\). Pre-look or Poisson time-averaged: \(4\kappa kT\).
4. **Global optimality.** The interior clock branch exists only for \(f<f_{\max}\), where \(\omega'^*=0\), and the two branches meet continuously there. For the interval-averaged loss, the no-clock optimum \(f_0=(2w\omega^2/(3c))^{1/3}\) satisfies \(f_0\ge f_{\max}=(\omega^2w/(9K))^{1/3}\) iff \(c\le6K\), and the clock branch's stationary point lies inside its domain iff \(c>6K\). So the onset is exact and the transition is continuous.
5. Interval-averaged values: below onset \(J^*=(\tfrac94c^2w\omega^2)^{1/3}\) (no clock); above, \(J^*=3\big((c-3K)K\omega^2w\big)^{1/3}\). They agree at \(c=6K\).

## 3. The lag: an estimate that under-advances, not a slow clock

Above onset the estimate lags by the fraction \((Kb/a)/(c-Kb/a)\) (\(3K/(c-3K)\) interval-averaged). This is **a lag of the estimate**. An estimator \(\hat\theta=\theta_{\rm look}+\lambda_e\phi\) on a clock of rate \(\omega_c\) and diffusion \(D_c\) has effective rate \(\lambda_e\omega_c\) and diffusion \(\lambda_e^2D_c\), while the TUR heat \(\kappa kT\omega_c^2/D_c\) does not depend on \(\lambda_e\). So the physical clock may run at any rate. What the optimum fixes is a deliberately shrunk advance. PROVED (in-model).

## 4. What is not a clock effect: the 1/3 share and \(w^{1/3}\)

- The expected loss is exactly \(J^*/3\) in both regimes, and \(J^*\propto w^{1/3}\). The no-clock branch \(J^*=(\tfrac94c^2w\omega^2)^{1/3}\) already has both. They come from deterministic drift with paid resets (loss \(\propto1/f^2\), spend \(\propto f\)). The 1/3 share is then CT24, the repository's share rule (`THEORY.md:101`), at stake elasticity 1/3. **KNOWN form / ELEMENTARY.** Contrast: continuous diffusive tracking has \(J^*\propto w^{1/2}\) and loss share 1/2 (`CORE.md:91`).
- Clock-specific content: the onset, the lag, and the split of the other 2/3 into clock heat \((c-6K)/(3(c-3K))\) and looks \(c/(3(c-3K))\) (interval-averaged; both verified; they sum to 2/3).

## 5. Where the stake-free onset breaks, and the TUR caveats

**Why it is stake- and frequency-free.** The small-angle model has no angle scale: \(\theta\to\lambda\theta\), \(\omega\to\lambda\omega\), \(D\to\lambda^2D\), \(w\to w/\lambda^2\) leaves \(\omega'^2/D\) and \(J\) unchanged, so the only dimensionless group is \(c/\kappa kT\). Any onset in this model must be stake- and frequency-free. It breaks when a second scale enters:
- **World phase drift.** With \(D_w>0\) the onset rises and depends on the stake: at \(D_w=1\) it is \(c^*/kT\approx8.1\) at \(w=0.1\) and \(\approx26.6\) at \(w=100\) (`clock_term_checks/clock_dw.out`). The stake-free threshold is a property of perfectly regular worlds only.
- **Periodic loss \(1-\cos e\).** The onset is 6.0 for \(w/(c\omega)\gtrsim50\) but 5.5 at \(w/(c\omega)\approx5\) (`clock_term_checks/cosloss.out`).
- **The never-look regime.** At small stakes, never looking (cost \(w\) times the uniform-phase loss) beats every design that looks. Sections 2–4 apply only above that regime.

**TUR caveats (KNOWN).**
- The TUR covers time-antisymmetric currents in a steady state with time-independent rates. Finite-time use is a long-time approximation, exact for the uniform ring.
- **Externally driven clocks evade it.** A clock driven by a periodic variation of an external protocol "can achieve arbitrary precision at arbitrarily low cost" (Barato and Seifert 2016). That is the known basis of the remark that under continuous contact there is no clock term: a low-friction memory dragged by the coupling pays rotation heat \(kT\omega^2/D_M\to0\). The term exists only when contact is paid or intermittent.
- **Underdamped pendulum clocks** break the TUR (Pietzonka 2022), so \(\kappa<1\) is possible there. Then the onset is \(2\kappa kT\,b/a\) with the measured \(\kappa\); as \(\kappa\to0\) a clock always pays.
- **Optimal estimators from the full jump record** are bounded by the mean residual time, not by entropy production (Prech et al. 2025). So \(\kappa\ge1\) is a bound on current-counting clocks, not on every memory that keeps phase. A record-keeping estimator moves the cost into read-out and erasure, which class CK does not price.

## 6. The perfect-read gap (and why section 9 exists)

A perfect read of a continuous phase gains unbounded information. Under Sagawa–Ueda accounting (measurement plus erasure costs at least \(kT\) times the information; Sagawa and Ueda 2009) it cannot have a finite thermodynamic price. So "\(c>6\kappa kT\)" is a statement in physical units only once looks have finite precision and \(c\ge kT\times\)(information per look). Section 9 does that.

## 7. Prior art

**KNOWN.**
- Clock precision costs dissipation: Cao, Wang, Ouyang and Tu 2015; Barato and Seifert 2016; Erker et al. 2017; Pearson et al. 2021.
- Clock noise against entrainment or input noise: Pittayakanchit et al. 2018 (free-running against hourglass clocks; internal against external noise); Monti, Lubensky and ten Wolde 2018; Monti and ten Wolde 2016; Fei, Cao, Ouyang and Tu 2018 (dissipation lowers phase diffusion and raises phase sensitivity); Zhang, Cao, Ouyang and Tu 2020 (the energy cost of synchronization).
- Engineering, without the TUR: the optimal resynchronization interval between clock drift and message energy in duty-cycled sensor networks (Schmid et al. 2010), the same free-running-clock-plus-paid-resync structure.
- Already in the repository: an accurate clock needs throughput (`litmap/LITMAP.md:28`, `theory/BOOKENDS.md:272`, citing Cao et al. 2015); the TUR as an unused second cost (`litmap/LITMAP.md:21`); uncertainty relations do not by themselves supply a heat-versus-tracking-error floor ([`OPEN_WORK.md:108`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L108)), which stays true of tracking and does not cover anticipating predictable change between paid looks.
- Related, not used: Conant–Ashby good regulator and Francis–Wonham internal model (`litmap/LITMAP.md:43`). The clock term reads as a thermodynamic price of running an internal model of a rhythm. Brockett's minimum attention control (1997) is a different "cost of attention" (a control cost on \(\partial u/\partial x\)); recorded in `litmap/LITMAP.md` §3.

**Not found** (about ten targeted searches by the memo and the review): a closed form that prices clock heat by the TUR inside a cost alongside a per-look price and a stake; the onset \(2\kappa kT\,b/a\); the optimal estimate lag. CONJECTURE (novelty unverified). [REVIEWER EDIT PR248] Those searches predate section 9; its information-priced onset was checked only by one further search in the PR #248 review, which did not find it (section 9.6).

It also gives a running price to the repository's "one two-state (resonant) layer per rhythm" (`THEORY.md:109`), which had none.

## 8. Checks for sections 2–5 (NUMERICAL; rerun for this PR at nice 19)

| Script | Result |
|---|---|
| `clock_term_checks/clock_tur.py` | Closed form against a multistart minimum over \((f,D,\omega')\) plus the no-clock corner, 60 random \((c/\kappa kT,w,\omega,\kappa)\): max relative gap \(\sim10^{-16}\). Onset between 5.9 and 6.1 at three \((w,\omega)\). Loss share 0.3333 at \(c/kT=7,20,100,10^4\). Simulated (Gillespie) Markov ring clock between perfect looks: time-averaged squared error within 0.6% of the formula; heat 0.91161 above the TUR floor 0.90909 |
| `clock_term_checks/clock_dw.py` | \(D_w=0\): onset \(\approx6.1\) (grid) at every stake; \(D_w=1\): 8.09 at \(w=0.1\) and 26.6 at \(w=100\) |
| `clock_term_checks/gen.py` (reviewer) | Symbolic \(D^*\), \(\omega'^*\), \(J(f)\) and the coefficient \(c-Kb/a\) for the general loss |
| `clock_term_checks/cosloss.py` (reviewer) | \(1-\cos\) loss onset 5.5 / 6.0 / 6.0 / 6.0 as the stake grows; pre-look scoring onset between 3.95 and 4.05 at \(w=1\) and \(w=100\) |

## 9. Next step: looks priced by the information they bring in

The question (from the review): make every imperfect look cost at least \(kT\) times the information it brings in, and ask whether the onset becomes a pure information threshold, conjectured to be about \(6\kappa\) nats.

### 9.1 Scheduled looks: no information threshold (ELEMENTARY)

If looks come on a schedule the memory knows (periodic, interval \(T\)), then in a perfectly regular world the memory can step its estimate by \(\omega T\) at each look event without reading anything. After the first look, a look then carries no new information about the phase (only about read noise the memory could ignore), so the information price \(\ge kT\cdot0\) puts no floor on it, and the cost could be driven toward zero by looking more often. The CK price per look is then a price of **timing** (the look event acting as an externally driven tick, which Barato and Seifert 2016 show can be cheap), not of information. So the interval-averaged "6" cannot become an information threshold. A price per look in that class has to be a contact or actuation price.

### 9.2 Class CK-I: looks the memory cannot predict

- World as in CK with \(D_w=0\). Looks arrive as a Poisson stream at rate \(f\): the memory cannot predict when.
- Each look returns the phase plus Gaussian noise of variance \(r\).
- **Reset readout.** The memory adopts the read plus a constant offset, then advances on its clock (\(\omega',D\), heat \(\kappa kT\omega'^2/D\)).
- **Information price.** Each look costs \(\lambda kT\,I\), \(\lambda\ge1\), with \(I=I(\theta_w;Y\mid\text{memory state})\) (Sagawa and Ueda 2009: measurement plus erasure \(\ge kT\,I\)).
- **Pre-look error.** Old read noise (variance \(r\)) plus \(E=\mu W+\sigma\sqrt W Z\), with \(W\sim\mathrm{Exp}(1)\), \(\mu=(\omega-\omega')/f\), \(\sigma^2=2D/f\). \(E\) is asymmetric Laplace: \(E=s_+E_1-s_-E_2\) with independent unit exponentials, \(s_+-s_-=\mu\), \(s_+s_-=\sigma^2/2\). So \(I=h(E+G_{2r})-\tfrac12\ln(2\pi e r)\) exactly, and \(h(E)=1+\tfrac12\ln(\mu^2+2\sigma^2)\) (ELEMENTARY, checked).
- **Loss.** Time-averaged with the optimal constant offset: \(r+\mu^2+2D/f\) (age at a random time \(\sim\mathrm{Exp}(f)\)).
\[J=\kappa kT\frac{\omega'^2}{D}+\lambda kT\,f\,I(f,\omega',D)+w\Big[r+\frac{(\omega-\omega')^2}{f^2}+\frac{2D}{f}\Big].\]
- **Symmetry.** Under the small-angle rescaling plus a time rescaling, the only dimensionless groups are \(\kappa\), \(\lambda\) and \(\Pi=w\,r^{3/2}/(kT\,\omega)\). The information per look of the best clockless design, \(I_0\), is a function of \(\Pi\) and \(\lambda\) (decreasing in the stake in the runs: higher stakes buy more frequent, less informative looks) [REVIEWER EDIT PR248]. So **any** onset in this class can be written as "\(I_0\) exceeds some number of nats". That form is forced. The content is the number.

### 9.3 The onset (PROVED in-model for the local onset; NUMERICAL for the global one)

Write \(a=\mu\,\partial I/\partial\mu\) and \(b=\mu^2\,\partial I/\partial\sigma^2\) at the clockless point (\(\sigma=0\)).

1. **Clockless optimum.** \(I\) depends on \(f\) only through \(\mu=\omega/f\), so \(\partial J_0/\partial f=0\) gives \(\lambda kT(I_0-a)=2w\omega^2/f_0^3\).
2. **A small clock.** Take \(\omega'=\varepsilon\), \(D=\varepsilon d\). To first order in \(\varepsilon\), with \(q=f_0/\omega\) and the envelope theorem for \(f\), the change in cost per unit \(\varepsilon\), minimized over \(d\), is negative iff
   \[4\kappa\,(I_0-a+2b)<\lambda\,I_0^2 .\]
3. **\(b=a/2\) exactly, for any read noise \(r>0\).** To first order a small clock moves the forward scale \(s_+\) by \(\sigma^2/(2\mu)\), which is half of what the same change in \(\mu\) does, and it adds a backward exponential \(-s_-E_2\) with \(s_-=\sigma^2/(2\mu)\). Convolved with the read noise the density is smooth, and an added independent variable of size \(s_-\) changes a smooth density's entropy only through its mean at first order, which entropy ignores. So \(\partial I/\partial\sigma^2=(1/2\mu)\,\partial I/\partial\mu\), that is \(b=a/2\).
4. **Therefore** the condition reads \(4\kappa I_0<\lambda I_0^2\):
   \[\boxed{\text{a clock first pays when the best clockless look carries more than }4\kappa/\lambda\text{ nats.}}\]
   This is the fixed-price Poisson onset \(c^*=4\kappa kT\) (section 2, \(a=1,b=2\)) with \(c\) replaced by \(\lambda kT\,I_0\), exactly, even though the information per look depends on the design and on \(f\). The threshold in nats is the same at every read precision and every stake, because \(r\) and \(w\) enter only through \(I_0\). [REVIEWER EDIT PR248] It is a first-order (local) statement: the cancellation \(b=a/2\) holds for clocks small enough that the backward scale \(s_-\) is well below the read-noise width \(\sqrt{2r}\). Larger clocks are covered only by the global numerics in item 5.
5. **Global onset (NUMERICAL).** A multistart minimum over \((f,\omega',D)\) with the exact information shows no clock at \(0.98\times4\kappa/\lambda\) and a clock at \(1.02\times4\kappa/\lambda\), for \((\kappa,\lambda)=(1,1),(2,1),(1,2)\), and the clock fraction rises continuously from zero above onset. So the transition is continuous and the local onset is the global one in the cases checked. A proof of global optimality is OPEN.

### 9.4 A trap: the naive high-SNR formula gives the wrong number

Dropping the read noise inside the entropy (\(I\approx h(E)-\tfrac12\ln(2\pi er)\)) gives \(a=b=1\) and an onset at \((2\kappa/\lambda)(1+\sqrt{1+\lambda/\kappa})\), which is 4.83 nats at \(\kappa=\lambda=1\). That is not the onset of the class. The limits "clock \(\to0\)" and "noise \(\to0\)" do not commute: without noise the backward tail of a vanishing clock is resolved against the sharp edge of the exponential and is charged at first order; with any noise it is hidden. At fixed \(I_0\) the read noise cannot be sent to zero relative to the spread anyway (the symmetry above), so the exact class is the right one. The check script keeps the naive formula's onset (check vii) to show the gap.

### 9.5 Checks (NUMERICAL; `clock_term_checks/info_reads.py` → `info_reads.out`)

- (i) \(h(E)\) closed form against grid quadrature: max gap \(\sim10^{-5}\) (grid error).
- (ii) Exact \(b/a=0.50000\) at \(\mu/\sqrt{2r}=35.4\) and \(14.1\) (while \(a=0.975\) and \(0.938\), so the exact match does not need \(a=1\)).
- (iii) Exact local onset at \(I_0=4\kappa/\lambda\) within 0.6% for \((\kappa,\lambda)=(1,1),(2,1),(1.5,1),(1,2),(3,1)\), identical at \(r=10^{-4}\) and \(10^{-7}\) (the residual shrinks with the finite-difference step; at step \(10^{-6}\) it is \(2\times10^{-5}\) at \(\kappa=\lambda=1\)).
- (iv)–(v) Global multistart and continuity, as in 9.3 (5).
- (vi) Fixed-price control: Poisson looks, perfect reads, onset between \(c=3.9\) and \(4.1\) at \(w=0.1\) and \(10\).
- (vii) The naive closed form's onset sits at 4.83, as stated in 9.4.
- (viii) Scope: at onset (\(\kappa=\lambda=1\)), a filtering clockless memory that also counts looks, with its information accounted as Gaussian (which overstates it), costs 7% more than the reset design, and the many-weak-looks limit costs 7.4 times more. This does not bound what every filtering memory can do.

### 9.6 Where this fails or is messier (stated plainly)

- **The number is not \(6\kappa\).** For random looks with time-averaged scoring it is \(4\kappa/\lambda\). For scheduled looks there is no information threshold (9.1). The interval-averaged 6 belongs to a class where the look price cannot be informational.
- **It depends on the look efficiency \(\lambda\), not on \(\kappa\) alone.**
- **Readout class.** The result is for the reset readout. A memory that filters across looks, or that uses the look stream itself as a noisy clock (adding \(\omega/f\) per look gives a free clock with diffusion \(\omega^2/(2f)\)), is a different class. Near onset the one filtering design checked does not undercut the reset design (check viii), but that is not a bound. At large stakes, frequent weak looks with filtering cost about \(\lambda kT\omega/(2\sqrt r)\) at vanishing error, and a clock with continuous weak looks costs \(3(\kappa\lambda)^{1/3}(kT)^{2/3}(\omega^2w)^{1/3}\) (SKETCH, from the Kalman–Bucy learning rate \(D/\varepsilon\)). Where the onset sits in that regime is OPEN.
- **Small information per look.** For \(4\kappa/\lambda\lesssim2\) the clockless reset design may not reach that little information per look at its optimum (in the runs its information per look did not fall below about 1.85 nats). Then the clock pays at every stake. Not mapped.
- **Small angle.** At onset the spread between looks is \(\mu\approx e^{I_0-1}\sqrt{2\pi e\,r}\). Small angles need \(\sqrt r\) well below \(e^{1-I_0}/4\), about \(10^{-2}\) rad at \(\kappa=\lambda=1\).
- **Feedback TURs.** [REVIEWER EDIT PR248] Recent preprints show that measurement and feedback can make currents more precise than the plain TUR allows, at a cost that counts the information used (arXiv:2602.23110, arXiv:2602.22651; abstracts read, not checked further). Because a reset look is feedback on the clock, a design that uses looks to sharpen the clock itself may sit outside the \(\kappa\ge1\) price used here. Not analysed.
- **Prior art for section 9.** One search in the PR #248 review (TUR-priced internal clock against information-priced, randomly timed looks) did not find the \(4\kappa/\lambda\) onset. Novelty is unverified (CONJECTURE).
- **Other scorings.** CONJECTURE: for other look statistics and scorings where the look price can be informational, the onset in nats is the fixed-price onset divided by \(\lambda kT\). Checked only for Poisson looks with time-averaged squared error.

## 10. How it could fail as a claim about nature

- Clocks that beat the TUR (\(\kappa<1\)), or record-keeping estimators (section 5).
- Looks whose cost is mainly contact or actuation, not information: then sections 2–4 apply with a measured price, and section 9 does not.
- World phase noise (the onset then depends on the stake), non-quadratic loss at small stakes, or a memory that also steers the rhythm (T61's class).
- A qualified, selected rhythm-tracker could show a clock below onset or none above it. No data was opened.

The next in-model test, to be preregistered first, is a selection simulation (\(\pi\propto e^{-\beta J}\), `CORE.md` §5) over ring-clock genomes, asking whether selected designs show the onset for their own scoring and look statistics. **SPECULATION:** biochemical look costs are many \(kT\), so the class would favour internal clocks wherever a rhythm is regular and looks are not free. That is not a test.

## 11. Files

`clock_term_checks/`: `clock_tur.py`, `clock_dw.py` (the memo's checks), `gen.py`, `cosloss.py` (the reviewer's checks), `info_reads.py` (section 9), `review_pr248_indep.py` (the PR #248 reviewer's separate check of section 9), each with its stored `.out`; `crossref.sh` and `crossref.out` (all 23 DOIs below resolved on Crossref on 23 November 2026); `clock_term_checks.py` and `clock_term_checks.out` (the cheap subset), locked by `tools/test_clock_term_checks.py`.

## 12. References (DOIs verified on Crossref, `clock_term_checks/crossref.out`)

- Barato, A. C. and Seifert, U. 2015. Thermodynamic uncertainty relation for biomolecular processes. *Phys. Rev. Lett.* 114:158101. doi 10.1103/PhysRevLett.114.158101.
- Gingrich, T. R., Horowitz, J. M., Perunov, N. and England, J. L. 2016. Dissipation bounds all steady-state current fluctuations. *Phys. Rev. Lett.* 116:120601. doi 10.1103/PhysRevLett.116.120601.
- Barato, A. C. and Seifert, U. 2016. Cost and precision of Brownian clocks. *Phys. Rev. X* 6:041053. doi 10.1103/PhysRevX.6.041053.
- Pietzonka, P. 2022. Classical pendulum clocks break the thermodynamic uncertainty relation. *Phys. Rev. Lett.* 128:130606. doi 10.1103/PhysRevLett.128.130606.
- Prech, K., Landi, G. T., Meier, F., Nurgalieva, N., Potts, P. P., Silva, R. and Mitchison, M. T. 2025. Optimal time estimation and the clock uncertainty relation for stochastic processes. *Phys. Rev. X*. doi 10.1103/rpls-mp8z.
- Cao, Y., Wang, H., Ouyang, Q. and Tu, Y. 2015. The free-energy cost of accurate biochemical oscillations. *Nat. Phys.* 11:772. doi 10.1038/nphys3412.
- Erker, P. et al. 2017. Autonomous quantum clocks: does thermodynamics limit our ability to measure time? *Phys. Rev. X* 7:031022. doi 10.1103/PhysRevX.7.031022.
- Pearson, A. N. et al. 2021. Measuring the thermodynamic cost of timekeeping. *Phys. Rev. X* 11:021029. doi 10.1103/PhysRevX.11.021029.
- Pittayakanchit, W., Lu, Z., Chew, J., Rust, M. J. and Murugan, A. 2018. Biophysical clocks face a trade-off between internal and external noise resistance. *eLife* 7:e37624. doi 10.7554/eLife.37624.
- Monti, M., Lubensky, D. K. and ten Wolde, P. R. 2018. Optimal entrainment of circadian clocks in the presence of noise. *Phys. Rev. E* 97:032405. doi 10.1103/PhysRevE.97.032405.
- Monti, M. and ten Wolde, P. R. 2016. The accuracy of telling time via oscillatory signals. *Phys. Biol.* 13:035005. doi 10.1088/1478-3975/13/3/035005.
- Fei, C., Cao, Y., Ouyang, Q. and Tu, Y. 2018. Design principles for enhancing phase sensitivity and suppressing phase fluctuations simultaneously in biochemical oscillatory systems. *Nat. Commun.* doi 10.1038/s41467-018-03826-4.
- Zhang, D., Cao, Y., Ouyang, Q. and Tu, Y. 2020. The energy cost and optimal design for synchronization of coupled molecular oscillators. *Nat. Phys.* 16:95 (online 2019). doi 10.1038/s41567-019-0701-7.
- Schmid, T., Charbiwala, Z., Shea, R. and Srivastava, M. B. 2010. On the interaction of clocks, power, and synchronization in duty-cycled embedded sensor nodes. *ACM Trans. Sens. Netw.* doi 10.1145/1807048.1807053.
- Sagawa, T. and Ueda, M. 2009. Minimal energy cost for thermodynamic information processing: measurement and information erasure. *Phys. Rev. Lett.* 102:250602. doi 10.1103/PhysRevLett.102.250602.
- Brockett, R. W. 1997. Minimum attention control. *Proc. 36th IEEE Conf. Decision and Control*. doi 10.1109/cdc.1997.657776.
- Also verified for the companion edits in this PR: Ito et al. 2026 (doi 10.1103/19nl-c8fl), Matsumoto, Sasa and Dechant 2025 (doi 10.1088/1742-5468/adf4be), Hartich, Barato and Seifert 2016 (doi 10.1103/PhysRevE.93.022116), Kappen 2005 (doi 10.1103/PhysRevLett.95.200201), Todorov 2009 (doi 10.1073/pnas.0710743106), Doob 1957 (doi 10.24033/bsmf.1494), Horowitz and Esposito 2014 (doi 10.1103/PhysRevX.4.031015).

## Class summary (moved here from the retired `STATUS.md`, 25 November 2026)

*Clock term and Kalman–Bucy factor of two* (T68, `theory/CLOCK_TERM_2026-11-23.md:11-15, 125`; `theory/DRIFT_HEAT_LIFT_2026-11-23.md:128-129`): anticipating predictable change between paid looks needs a TUR-priced internal clock once looks cost more than \(4\kappa kT\) or \(6\kappa kT\) (fixed price) or carry more than \(4\kappa/\lambda\) nats (information-priced random looks); the Kalman–Bucy factor-of-two question is answered from the linear identity (\(\dot Q_M=kT\,\dot I_M(1+\dot I_M/N)\)) and Hartich–Barato–Seifert 2016 (with its transfer-entropy qualification).
