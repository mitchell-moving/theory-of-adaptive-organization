# Real-system test screen after T49, T50, T61 and the freeze-or-hold floors (23 November 2026)

*Monday 23 November 2026, afternoon (America/New_York). Written on branch `realsys-screen-2026-11-23` against `main` `79ed045` (PR #241, T50); later merged with `main` after PR #242 (T64), without editing T64. A screen by one author for Chad Mitchell. Independently reviewed on PR #243; the reviewer's text and rival-gate fixes are applied. It is not a lock, not a preregistration, and not a run. No outcome data was downloaded or opened. It does not edit `THEORY.md`, `CORE.md`, `measurement/CLAIM_MAP_v2.md`, or any locked file. Open-work row: RS-SCREEN.*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Answer

The brief asked for one preregistered, hash-locked real-system test built on today's merged floors, with (a) a public dataset reachable without sign-in or paywall, (b) a quantitative prediction that can fail and would move the odds, and (c) a derivation by the method, with inputs measured independently of the outcome. **No candidate clears all three bars today, so no preregistration is locked here.** Locking a weaker test would repeat the lesson of `theory/DISCRIMINATING_CANDIDATES_2026-11-21.md` (lock only after the theory's design and a named rival's design are computed on the same quantity, with the rival outside the band) and of SENSE-CELL (a proxy that does not match the floor's quantity is not evidence either way).

What the screen did find is one quantity, the argmin already proved as T49 C4 (reset shocks) and in class A (diffusion), compared here across world types and against named rivals: **at a fixed stake, the cost-minimizing tracking error grows linearly with the shock rate in a reset-shock world, but with the square root of the rate in a diffusive world with the same second-order statistics. A linear filter with fixed sensor noise gives the square root in both** (§2; checks G1–G3, R1, S1 in `theory/realsys_screen_checks/`). The exponent is price-free: it does not depend on \(kT\), on the price per nat, or on the stake, as long as the stake is held fixed across conditions. It separates this theory from a fixed-noise linear filter. It does not separate it from rational inattention, and it does not cleanly separate it from a correctly specified fixed-noise Bayesian change-point filter (§2). What is missing is a public dataset of a strongly selected tracker measured across shock rates. The two best candidates and what each needs are in §4.

## 1. What was read first, and what is already on the record

Read on this base: [`STATUS.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/STATUS.md) (retired 25 November 2026), [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md) (§3), `CORE.md`, `measurement/FRAMEWORK.md` §9, `theory/TEST_SEARCH_2026-11-22.md`, `theory/DISCRIMINATING_CANDIDATES_2026-11-21.md`, `theory/NON_GAUSSIAN_FLOOR_2026-11-23.md` (T49), `theory/ANTIFRAGILE_LOOP_2026-11-23.md` (T50), the heads of `theory/FEEDBACK_FLOOR_2026-11-23.md` (T61) and `theory/FREEZE_OR_HOLD_FLOOR_2026-11-23.md`, `tests/README.md`, `tests/BIO1/RESULTS.md`, `prereg/vigil-ona/`, `prereg/SENSE-CELL/RESULTS.md`, and `theory/measured/ecoli/PREREG_Y4.md`. The tree was searched for "vigil", "Meeter", "persister" and "Van den Bergh". The independent review also searched human change-point and volatility tasks (Nassar et al. 2010, 2012; Behrens et al. 2007; later OSF deposits), animal foraging and vigilance deposits, bacterial persister-frequency data, and public electric-fish tracking archives; those checks are in §3. No outcome series was downloaded or opened.

Past attempts, read as open misses, and the lesson each gives this screen:

| Attempt | What happened | Lesson used here |
|---|---|---|
| E. coli P1/P3 (`theory/measured/ecoli/MEASURE_RESULT_2026-11-21.md`) | Rival R3's design sat inside the predicted box | compute the rival on the same quantity before any lock |
| SENSE-CELL (`prereg/SENSE-CELL/RESULTS.md`) | Locked output FAIL, relabeled INCONCLUSIVE: the measured precision was set by methylation saturation, not by energy | the measured quantity must be the floor's quantity, in the floor's regime |
| VIGIL_ONA (`prereg/vigil-ona/RESULTS.md`) | Direction passed, but Mintzberg predicts the same direction; Tier 3 | a direction shared with a rival does not move the odds |
| BIO1 (`tests/BIO1/RESULTS.md`) | "Memory tracks how fast the world changes" is prior art; the neural slope of about 1 does not separate this theory from scale-free dynamics | timescale-matching is not distinctive; an error exponent at fixed stake might be |
| TEST_SEARCH (`theory/TEST_SEARCH_2026-11-22.md`) | Bet-hedging and Kelly deposits do not test the cost of judgment | persistence and dormancy fractions follow from growth alone unless the information term is priced |
| DIR1, CAISO, GRID-DX, ANTS1 | INCONCLUSIVE, or in-model | qualification and power first |

## 2. The method on the candidate quantity

**Cost, with named terms** (T49, class A and class C; exogenous world, bipartite memory, mean squared error):
\(J(\varepsilon)=\dot Q_M(\varepsilon)+w\,\varepsilon\), with the memory-bath heat at its floor \(\dot Q_M\ge kT\,\dot I_M\) (KNOWN for bipartite chains, Horowitz and Esposito 2014), \(w\) the stake per unit squared error, and \(\varepsilon\) the steady mean squared error. The ruin cap is taken slack.

- Diffusive world (class A, noise \(D\)): \(\dot Q_M/kT\ge D\,(1/\varepsilon-\mathcal I(\pi))\).
- Reset-shock world (class C, rate \(\lambda\), Gaussian landing variance \(v\)): \(\dot Q_M/kT\ge\lambda\,[\tfrac32\ln(v/\varepsilon)-\gamma_E-\ln 2]\), attained within \((3.0033+\varepsilon/4v)\,\lambda\) nats per unit time by the core-plus-reserve memory.

**Minimum** (ELEMENTARY on the T49 floors; checks G1–G3):
- diffusive: \(\varepsilon^*=\sqrt{kT D/w}\), so \(\partial\ln\varepsilon^*/\partial\ln D=\tfrac12\) and \(\partial\ln\varepsilon^*/\partial\ln w=-\tfrac12\);
- reset shocks: \(\varepsilon^*=\tfrac32\,kT\lambda/w\), so \(\partial\ln\varepsilon^*/\partial\ln\lambda=1\) and \(\partial\ln\varepsilon^*/\partial\ln w=-1\). This argmin is T49 C4. Adding the attaining gap gives the exact slope \(1-\varepsilon^*/(6v)\), which at \(\varepsilon^*/v\le 0.01\) differs from 1 by at most \(1/600\approx 0.00167\) (G3).

**Read-off design.** At a fixed stake, a tracker selected to the minimum should loosen in proportion to the shock rate in a jump world, and in proportion to the square root of the rate in a diffusive world. The exponent is set by how the world moves, not by its spectrum: a reset world at rate \(\lambda\) and an Ornstein–Uhlenbeck world at rate \(\lambda\) with the same variance have the same autocovariance \(v e^{-\lambda|t|}\).

**Named rival on the same quantity** (check R1). A linear (Kalman–Bucy) filter with fixed white sensor noise \(R\) sees only the autocovariance. Its steady error is \(P=R(-\lambda+\sqrt{\lambda^2+2\lambda v/R})\approx\sqrt{2\lambda vR}\), exponent \(\tfrac12\) in both worlds, and exponent 0 in the stake. FRAMEWORK rival R2 (exponent \(\tfrac12\)) gives the same. So in a jump world the theory's exponent 1 and this rival's \(\tfrac12\) differ by \(\tfrac12\). A design with a few-fold range of shock rates and a 20% error measurement could resolve that gap; the power claim applies to this linear-filter rival, not to the Bayesian change-point filter below.

**Prior art on the same quantity.** Any cost linear in the same information-rate functional gives the same argmin, with \(kT\) replaced by the price per nat. That includes rational inattention in the sense of Sims 2003 applied to this functional; Sims 2003 does not itself compute the jump-world exponent. So exponent 1 separates an information-priced tracker from a fixed-noise linear filter. It does not separate this theory from rational inattention. The physical content this theory adds is that the price is at least \(kT\) per nat, which matters only for a level test, not for the exponent.

A correctly specified Bayesian change-point filter with fixed sensor noise — the ideal observer for this reset world (Fearnhead and Liu 2007; Nassar et al. 2010) — is a different rival. It uses the jump structure, not only the autocovariance, so it is not the linear filter. In the known-jump benchmark, after each reset the error falls as \(P(t)=1/(1/v+t/R)\), and the mean over exponential waiting times is \(\varepsilon=\lambda R\,e^{\alpha}E_1(\alpha)\) with \(\alpha=\lambda R/v\). The shock-rate exponent is then \(1+\alpha-1/(e^{\alpha}E_1(\alpha))\) (check B1). It approaches 1 only as \(\alpha\to 0\), and it is substantially below 1 at moderate precision (about 0.76 at \(\alpha=0.01\), 0.88 at \(\alpha=10^{-4}\)). Unknown jump times cannot beat this benchmark. Without an independent measurement of \(R\), that slope is not guaranteed to fall outside a band around 1 that a few-fold range of shock rates and a 20% error measurement would resolve. The stake elasticity does separate the two: this theory has \(\partial\ln\varepsilon^*/\partial\ln w=-1\); any fixed-noise filter, linear or Bayesian, has elasticity 0.

The adaptation-timescale results of Fairhall et al. 2001 and Wark et al. 2009 concern timescales, not error at fixed stake, and are not this quantity.

**Scope.** Exogenous world (the tracker does not move it; worlds it moves are T61's). Mean squared error. Fixed stake across conditions. High precision (\(\varepsilon\ll v\)). Ruin cap slack. Jumps that reset to a fresh Gaussian draw.

**What remains a measurement.** That a real tracker is strongly selected (FRAMEWORK §9 item 1); that its stake is the same across the conditions compared; the world's type (jump or diffusion) and its rate, measured from the world alone; and the tracker's steady error, measured from the tracker.

## 3. The screen

Each row is one read-off of today's merged floors. Bars: (a) public no-account data; (b) a quantitative prediction that can fail and that a named rival does not share; (c) inputs measured independently of the outcome.

| Read-off | Candidate system | (a) | (b) | (c) | Outcome of the screen |
|---|---|---|---|---|---|
| T49 class B: \(\varepsilon_s\propto\sqrt{D_s}\) by regime | any regime-switching tracker | varies | **no**: the fixed-noise linear filter and R2 give exponent \(\tfrac12\) too | yes | not discriminating |
| T49 class C: shock-rate exponent 1 at fixed stake (§2) | a selected tracker across shock rates | **none found** | yes vs linear filter; not vs rational inattention; not cleanly vs a fixed-noise Bayesian change-point filter (§2) | yes, if the world is logged | best candidate; no dataset |
| T49 class C: reserve \(\delta=\varepsilon/4v\), linear in \(\lambda\) | E. coli persister fraction vs antibiotic frequency (Van den Bergh et al. 2016) | **no**: not open access (Europe PMC: no PMC copy); source data not verified | **no**: Kussell and Leibler 2005 predict the same linear dependence | yes (frequency set by protocol) | not discriminating and not open |
| T50 AF-rate: learning pays only above \(\theta_c=2c\,kTa/w\) | loss of sensing systems across bacterial genomes | genomes yes | threshold numeric only if \(c\), \(w\) known | **no**: \(c\) and \(w\) not independently measurable | inputs unmeasurable |
| T50 AF-convex: owned options gain from amplitude | firms holding real options | partly | **no**: real-options theory and Taleb and Douady predict the same direction | partly | direction shared with rivals |
| T61: a passive trap holds at zero ongoing heat; tight feedback costs actuation heat | endotherm metabolic rate across ambient temperature | partly | **no**: the Scholander thermoneutral-zone model predicts the same shape | yes | prior art, same prediction |
| Freeze-or-hold: track only when the stake times the rate clears the threshold; otherwise hold or bet-hedge | sensing vs random switching in microbes | no dataset | **no**: Kussell and Leibler 2005 include a sensing cost and the same crossover | partly | prior art |

Public datasets checked on review, none of which clear all three bars. Human change-point and volatility tasks (Nassar et al. 2010, 2012; Behrens et al. 2007; later predictive-inference deposits such as https://osf.io/fsxh5 and Seow and Gillan 2020, https://osf.io/2z6tw) do not. Nassar 2010 and 2012 use a single hazard rate, so they cannot identify a shock-rate exponent; a public no-account deposit of the 2010 raw series was not found (the lab site hosts model code). Behrens 2007 compares two volatility regimes on a binary reward-probability task, not mean squared error of a continuous reset tracker, and a public no-account deposit was not found. The later OSF deposits have one or two hazards, not four spanning a factor of four, and in one case the raw series require an institutional access request. In all of these, human laboratory subjects fail THEORY §3 qualification (no recorded \(\sigma\) or \(N_e\)). Public animal vigilance and foraging deposits measure time budgets or giving-up densities, not tracking error at a fixed stake. Public weakly electric fish refuge-tracking archives measure continuous refuge motion, not a reset-shock sweep at four or more rates. Van den Bergh et al. 2016 is not open access (Europe PMC: no PMCID, `isOpenAccess=N`); no verified open source-data deposit was found; bar (b) fails in any case because Kussell and Leibler 2005 predict the same linear dependence. Lan et al. 2012 is open in PMC, but that is the paper, not a like-for-like deposit of adaptation error and dissipation in the same Tar-only cells in the energy-limited regime. No outcome series from any of these was downloaded or opened.

## 4. The best two, and what each needs

**Candidate 1 — SHOCK-EXPONENT (T49 class C, §2).** A strongly selected tracker of one continuous variable, measured at at least four shock rates spanning a factor of at least 4, with a matched diffusive arm at the same autocovariance, and with the stake fixed across arms. Prediction to lock against the linear-filter rival: slope of \(\ln\varepsilon\) on \(\ln\lambda\) in the jump arm in a band around 1 that excludes \(\tfrac12\) after measurement error, and slope \(\tfrac12\) in the diffusive arm. It can fail: a jump-arm slope near \(\tfrac12\) is the linear-filter design. That lock does not, by itself, exclude rational inattention or a correctly specified fixed-noise Bayesian change-point filter. A stake-elasticity arm (this theory \(-1\), any fixed-noise filter \(0\)) would. Needs: (i) a substrate where selection strength and population size are set by protocol, which in practice is the designed-world lab experiment of OPEN_WORK T7 (needs a partner, IRB if human, and Chad's go), because no public dataset of a selected tracker across shock rates was found; (ii) a qualification record under FRAMEWORK §9 item 1 before any design is read; (iii) a stated reason why rational inattention and a fixed-noise Bayesian change-point filter are not the rivals being tested, or a stake-elasticity arm those rivals do not share. Moves the odds on "selected trackers price information" against "selected trackers are fixed-noise linear filters". It does not, by the shock-rate exponent alone, move the odds against rational inattention or against a correctly specified fixed-noise Bayesian filter. It does not test \(kT\).

**Candidate 2 — SENSE-CELL-MATCHED (OPEN_WORK T10), the existing floor-proximity path.** E. coli chemotaxis adaptation error and dissipation in the same cells, Tar-only, at low background ligand where Lan et al. 2012 place the energy limit, scored as measured heat over the floor. E. coli has an established \(N_e\) (T1 item b). Needs: the like-for-like data (Lan-lab or new measurements; no public no-account deposit was found), and T1 items (a), (c), (d), (e). Today's floors do not change this path; T61's feedback floor bears on how the adaptation loop is classed and should be read before a lock.

## 5. What this note does not do

It does not lock, preregister or hash a test. It does not download or open any outcome series. It does not qualify a class or move a CLAIM_MAP row. It does not edit the hypothesis sentence, `THEORY.md` or `CORE.md`. It does not treat an in-model exponent as a fact about a real system.

## Checks

`theory/realsys_screen_checks/realsys_screen_checks.py` (closed forms and one-dimensional minimization; no data) reports `FAILS 0`; the stored output is `realsys_screen_checks.out`, and `tools/test_realsys_screen_checks.py` reruns it and compares the output byte for byte. Check B1 is the known-jump Bayesian change-point exponent, added on review.

## References (DOIs resolved on the Crossref API, 23 November 2026)

- Horowitz, J. M. and Esposito, M. 2014. Thermodynamics with Continuous Information Flow. *Phys. Rev. X* 4:031015. doi 10.1103/PhysRevX.4.031015.
- Sims, C. A. 2003. Implications of rational inattention. *J. Monetary Econ.* 50:665. doi 10.1016/S0304-3932(03)00029-1.
- Kussell, E. and Leibler, S. 2005. Phenotypic Diversity, Population Growth, and Information in Fluctuating Environments. *Science* 309:2075. doi 10.1126/science.1114383.
- Kussell, E., Kishony, R., Balaban, N. Q. and Leibler, S. 2005. Bacterial Persistence: A Model of Survival in Changing Environments. *Genetics* 169:1807. doi 10.1534/genetics.104.035352.
- Balaban, N. Q., Merrin, J., Chait, R., Kowalik, L. and Leibler, S. 2004. Bacterial Persistence as a Phenotypic Switch. *Science* 305:1622. doi 10.1126/science.1099390.
- Van den Bergh, B. et al. 2016. Frequency of antibiotic application drives rapid evolutionary adaptation of Escherichia coli persistence. *Nature Microbiology* 1:16020. doi 10.1038/nmicrobiol.2016.20.
- Lan, G., Sartori, P., Neumann, S., Sourjik, V. and Tu, Y. 2012. The energy–speed–accuracy trade-off in sensory adaptation. *Nature Physics* 8:422. doi 10.1038/nphys2276.
- Fairhall, A. L., Lewen, G. D., Bialek, W. and de Ruyter van Steveninck, R. R. 2001. Efficiency and ambiguity in an adaptive neural code. *Nature* 412:787. doi 10.1038/35090500.
- Wark, B., Fairhall, A. and Rieke, F. 2009. Timescales of Inference in Visual Adaptation. *Neuron* 61:750. doi 10.1016/j.neuron.2009.01.019.
- Mitchell, A. et al. 2009. Adaptive prediction of environmental changes by microorganisms. *Nature* 460:220. doi 10.1038/nature08112.
- Nassar, M. R., Wilson, R. C., Heasly, B. and Gold, J. I. 2010. An approximately Bayesian delta-rule model explains the dynamics of belief updating in a changing environment. *J. Neurosci.* 30:12366. doi 10.1523/JNEUROSCI.0822-10.2010.
- Nassar, M. R. et al. 2012. Rational regulation of learning dynamics by pupil-linked arousal systems. *Nat. Neurosci.* 15:1040. doi 10.1038/nn.3130.
- Behrens, T. E. J., Woolrich, M. W., Walton, M. E. and Rushworth, M. F. S. 2007. Learning the value of information in an uncertain world. *Nat. Neurosci.* 10:1214. doi 10.1038/nn1954.
- Fearnhead, P. and Liu, Z. 2007. On-line inference for multiple changepoint problems. *J. R. Stat. Soc. Ser. B* 69:589. doi 10.1111/j.1467-9868.2007.00601.x.
