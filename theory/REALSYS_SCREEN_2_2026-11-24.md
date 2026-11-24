# Real-system screen 2: public change-rate and stake datasets (24 November 2026)

*Tuesday 24 November 2026, evening (America/New_York). Written on branch `cursor/realsys-screen-2-2026-11-24-1aab` against fork `main` `d2aeb810`. A screen by one author for Chad Mitchell. It extends `theory/REALSYS_SCREEN_2026-11-23.md` (RS-SCREEN). It is not a lock, not a preregistration, and not a run. No outcome series was downloaded or opened. It does not edit `THEORY.md`, `CORE.md`, `measurement/CLAIM_MAP_v2.md`, or any locked file.*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 0. Answer

**No candidate clears all three bars of RS-SCREEN. No preregistration is drafted.**

The brief was a paper screen, not a run. A dataset entered only if it is a real experiment and the design description states either (i) at least four distinct shock or change rates of the tracked state, as separate conditions, or (ii) an experimental manipulation of stake in a continuous tracking task. Each entered dataset was then scored on RS-SCREEN's three bars: (a) public data that download with no account, (b) a quantitative prediction that can miss and that a named rival does not share, (c) inputs measured independently of the outcome. DOIs below were resolved on the Crossref API on 24 November 2026. A DOI that did not resolve was dropped and is not cited.

The prediction that separates this theory from a fixed-noise Bayesian change-point filter is the stake elasticity of steady squared error, not the shock-rate exponent. RS-SCREEN §2: at a fixed stake the cost-minimizing error has shock-rate exponent 1 in a reset world and 1/2 in a diffusive world; a fixed-noise linear filter has exponent 1/2 in both; a correctly specified fixed-noise Bayesian change-point filter is not held outside a band around 1 without an independent measurement of its sensor noise. The same section: this theory has ∂lnε*/∂lnw = −1, and any fixed-noise filter, linear or Bayesian, has elasticity 0. None of the designs below measures that elasticity. On each row the last column is no.

Upstream `process/PREREG_GATE.md` (draft PR #263, branch `process/falsifiability-gate-2026-11-24`) says a new prereg opens with a Gate section, G1 through G5, before any code or data. That file is not written here, because no row clears the three bars.

## 1. What was read, and what was not opened

Read: RS-SCREEN; upstream `process/PROCESS.md` on Chad-Mitchell `main`; upstream `process/PREREG_GATE.md` on draft PR #263; `measurement/FRAMEWORK.md` §9 item 1 and the qualification paragraph of `THEORY.md` §3, as the bar a later lock would still have to meet. The hypothesis sentence above is quoted from `CORE.md` and is not an edit.

Design pages, data-availability statements, repository file names, and one HTTP header check were read. No outcome file was downloaded. No trial table, trajectory, or choice series was opened. No code was run on data.

Vocabulary follows `process/PROCESS.md` §2. This note calls the work a theory. It uses cost for the objective. It does not use a generic outcome label in place of a miss. Nothing here is a locked prediction, so there is no miss or hit to log.

## 2. How a design entered

**Entered.** (i) The tracked state's own rate of change takes at least four distinct values, in separate conditions: a hazard or reset rate, a volatility, or the diffusion coefficient of that state. (ii) The experiment changes the stake on tracking error in a continuous tracking task.

**Not entered, and why.** An observation-noise or contrast sweep at one state-rate is not (i). A sum of many sinusoids in one stimulus is one trajectory, not four rates. Dot speed or flow speed, while the tracked state's own walk is held fixed, is a signal-strength manipulation, not a shock rate. A flat participation payment is not (ii). A dataset whose DOI did not resolve on Crossref is not cited.

Bars, copied from RS-SCREEN §3: (a) public no-account data; (b) a quantitative prediction that can miss and that a named rival does not share; (c) inputs measured independently of the outcome. The Bayesian column asks a further question from RS-SCREEN §2: whether any feasible prediction on that design separates this theory from the fixed-noise Bayesian change-point filter, rather than only from the linear filter. The separating quantity named there is the stake elasticity of steady mean squared error, with w the coefficient on that squared error.

Human laboratory subjects and trained monkeys, as used below, have no recorded cost-to-fitness map σ and no recorded N_e. FRAMEWORK §9 item 1 is therefore not met for any row. That is a further reason not to lock a test. It is recorded here and is not used to hide a row that otherwise clears (a), (b), and (c). None does.

## 3. Candidates

| Candidate | Enters on | (a) | (b) | (c) | Separates from the Bayesian change-point filter |
|---|---|---|---|---|---|
| Bonnen, Huk, and Cormack 2017, experiment II, frontoparallel arm | (i) five diffusion coefficients | no | no | no | no |
| Glaze, Kable, and Gold 2015 triangles task, reanalyzed by Glaze et al. 2018 | (i) seven hazard rates | no | no | no | no |
| Janssen and Brumby 2015 | (ii) payoff weight on a tracking component | yes | no | no | no |
| Joshua and Lisberger 2012 | (ii) juice volume during pursuit | no | no | no | no |
| Lixenberg and Joshua 2018 | (ii) juice volume during pursuit | no | no | no | no |

No row has (a), (b), and (c) all yes.

### 3.1 Bonnen, Huk, and Cormack 2017, five diffusion coefficients

Citation: Bonnen, K., Huk, A. C., and Cormack, L. K. 2017. Dynamic mechanisms of visually guided 3D motion tracking. *Journal of Neurophysiology* 118:1515. doi 10.1152/jn.00831.2016. Article page checked: https://doi.org/10.1152/jn.00831.2016.

**Rates.** Experiment II is continuous manual tracking of a target in a one-dimensional Brownian random walk. In the frontoparallel arm the step-size standard deviation takes five values: 4.04, 2.02, 1.01, 0.51, and 0.25 arcmin (stated pixel equivalents 3.49, 1.75, 0.87, 0.44, and 0.22). The largest is 16.16 times the smallest. The paper states that the walk is updated at 20 Hz. The motion-through-depth arm in the same experiment is a single standard deviation, 0.51 arcmin, and is not a four-rate sweep. Three observers served in the experiments; two were authors. The methods as fetched do not describe a stake or a payoff that changes across conditions.

**Account.** The article text contains no data-availability statement and no repository URL. A search on 24 November 2026 of OSF, Dryad, Zenodo, and figshare did not return a deposit of these trajectories. Download with no account: no.

**(a) (b) (c).** (a) no. (b) no. This is a diffusive world. RS-SCREEN §2 gives both this theory and a fixed-noise linear filter exponent 1/2 in diffusion, so the slope of log error on log diffusion coefficient is not a prediction the linear filter does not share. There is no stake arm, so the elasticity that separates this theory from a fixed-noise Bayesian change-point filter is not available on this design. (c) no. The five coefficients are set by protocol, which is the right kind of independence for a rate, but the series are not in a public log, the stake w is not recorded, and σ and N_e are not recorded.

**Bayesian change-point filter.** No feasible prediction on this design separates this theory from that filter. The diffusion exponent does not separate this theory from the linear filter, and the stake elasticity is not in the design.

### 3.2 Glaze, Kable, and Gold 2015, seven hazard rates

Citations: Glaze, C. M., Kable, J. W., and Gold, J. I. 2015. Normative evidence accumulation in unpredictable environments. *eLife* 4:e08825. doi 10.7554/eLife.08825. Article page checked: https://elifesciences.org/articles/08825. Glaze, C. M., Filipowicz, A. L. S., Kable, J. W., Balasubramanian, V., and Gold, J. I. 2018. A bias–variance trade-off governs individual differences in on-line learning in an unpredictable environment. *Nature Human Behaviour* 2:213. doi 10.1038/s41562-018-0297-4.

**Rates.** The triangles task asks which of two sources produced a star. The source switches at a hazard rate that is constant inside a block and is drawn, without replacement inside a session, from seven values: 0.05, 0.1, 0.3, 0.5, 0.7, 0.9, and 0.95. The 2018 paper reanalyzes that task and states those seven values; the 2015 paper states the same set. This meets (i). It is a binary source judgment, not mean squared error of a continuous estimate. The same 2015 paper's dots-reversal task uses two change rates, 0.1 Hz and 2.0 Hz, and does not itself meet (i). No stake is manipulated.

**Account.** The 2015 article page, as fetched, offers the article PDF and the figures PDF, not a raw-series deposit. The 2018 paper says the data that support the findings are available from the authors upon request. The public code folder https://github.com/TheGoldLab/ms_archived/tree/master/2018_GlazeEtAl_NHB contains figure scripts, model source, and a README. The README says to obtain the data by contacting Joshua Gold, then to point a loader at local directories named `Data/Analysis` and `Data/Raw`. That folder's file list has no raw-series file. Download with no account: no.

**(a) (b) (c).** (a) no. (b) no. The recorded quantity is a choice about a binary source. The ideal observer of this task is a change-point filter of the kind Glaze, Kable, and Gold fit. RS-SCREEN's exponent on steady squared error is not this quantity, so there is no prediction on these choices that the Bayesian change-point filter does not already make for its own task. (c) no. The hazard list is set by protocol, but the floor's outcome, steady squared error of a continuous tracker, is not what the task records, and σ and N_e are not recorded.

**Bayesian change-point filter.** No. This is that rival's task. Agreement with the normative hazard-dependent choice rule is the rival's prediction.

### 3.3 Janssen and Brumby 2015, a payoff weight on tracking

Citation: Janssen, C. P. and Brumby, D. P. 2015. Strategic Adaptation to Task Characteristics, Incentives, and Individual Differences in Dual-Tasking. *PLOS ONE* 10:e0130009. doi 10.1371/journal.pone.0130009. Article page checked: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0130009.

**Stakes and rates.** Participants keep a joystick-controlled cursor inside a circle while the cursor, when not held, takes a random-walk step about every 25 ms, and they also type a digit string. Only one task is visible at a time. Within subjects, the walk's standard deviation is 3 or 5 pixels, and the target radius is 80 or 120 pixels: two noise levels, not four. Between subjects, the payoff function changes. One group ("speed") puts more weight on finishing the typing quickly; the other ("accuracy") puts more weight on time spent with the cursor outside the circle. The tracking term is an exponential penalty in seconds outside the circle, with a floor of −£0.20 on a trial. Base pay is £5 in the speed group and £3 in the accuracy group, chosen so that each group has a guaranteed minimum of £5. Participants are told that both typing time and time outside the circle matter. They are not told the equations or which component weighs more. This is an experimental payoff manipulation on a task that includes continuous tracking, so it enters on (ii). The loss is not the coefficient w on squared tracking error.

**Account.** The article says all relevant data are in the manuscript and its Supporting Information. S1 File is described as a zip with an R script and an `.Rdata` file. A HEAD request to https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0130009.s001&type=supplementary on 24 November 2026 returned HTTP 200, content type `application/zip`, with no authentication challenge. The archive was not downloaded and was not opened. Download with no account: yes.

**(a) (b) (c).** (a) yes. (b) no. The scored behavior is how people interleave typing and tracking under a stated payoff. A payoff-maximizing agent moves its interleaving when those weights move. That direction is shared by a Bayesian dual-task agent and by this theory; it is not the elasticity of steady squared error. The weights are also confounded with a different base payment and were not shown to the participants as w. (c) no. The payoff parameters and the two noise levels are set by protocol, but the input the elasticity needs, a known coefficient on squared error at a logged continuous state, is not what this task records. σ and N_e are not recorded.

**Bayesian change-point filter.** No. The manipulated stake is not w on squared error, so the elasticity −1 versus 0 is not identified. A Bayesian agent that maximizes the stated payoff also changes when the payoff weights change.

### 3.4 Joshua and Lisberger 2012, juice volume during pursuit

Citation: Joshua, M. and Lisberger, S. G. 2012. Reward Action in the Initiation of Smooth Pursuit Eye Movements. *Journal of Neuroscience* 32:2856. doi 10.1523/JNEUROSCI.4676-11.2012. Article page checked: https://doi.org/10.1523/jneurosci.4676-11.2012.

**Stakes.** Monkeys pursue a target moving at constant velocity, 30°/s in the single-target and two-target designs as stated. Color cues the juice delivered at the end of the trial if gaze stays inside a 2–4° window. For monkey P the large reward is 0.2–0.4 ml and the small reward is 0.05–0.1 ml; the color association is reversed for monkeys I and S. A further two-target experiment uses three volumes, 0.1, 0.2, and 0.4 ml. This is an experimental stake manipulation during continuous pursuit, so it enters on (ii). The juice is a trial-completion reward for staying inside a window. It is not a coefficient on squared error along the path. The target motion is one speed, not four shock rates.

**Account.** The article text as fetched has no data-availability statement and no repository URL. Download with no account: no.

**(a) (b) (c).** (a) no. (b) no. A larger completion reward can raise pursuit gain through effort or motivation. A fixed-noise controller whose effort depends on expected reward, and a Bayesian agent maximizing expected juice, both move. That is not ∂lnε*/∂lnw = −1 against elasticity 0. (c) no. The volumes are set by protocol. Squared-error stake, steady mean squared error, σ, and N_e are not the recorded inputs.

**Bayesian change-point filter.** No. The design does not measure the elasticity of steady squared error.

### 3.5 Lixenberg and Joshua 2018, juice volume during pursuit

Citation: Lixenberg, A. and Joshua, M. 2018. Encoding of Reward and Decoding Movement from the Frontal Eye Field during Smooth Pursuit Eye Movements. *Journal of Neuroscience* 38:10515. doi 10.1523/JNEUROSCI.1654-18.2018. Article page checked: https://pmc.ncbi.nlm.nih.gov/articles/PMC6596260/.

**Stakes.** Color cues juice before a pursuit target steps and then moves. For monkey Y, large reward is 0.1–0.2 ml and small reward is 0.05 ml; the association is reversed for monkey X. Three interleaved conditions: large reward with fast motion (30°/s), small reward with fast motion, and large reward with slower motion (20°/s for monkey Y, 15°/s for monkey X). Two stake levels and two speeds. The juice is again a reward for keeping the eye inside a 2°×2° window, not w on squared error. This enters on (ii). It is not four shock rates.

**Account.** The PMC article page as fetched has no data-availability statement and no repository URL. Download with no account: no.

**(a) (b) (c) and the Bayesian column.** Same scoring as §3.4. (a) no. (b) no. (c) no. The Bayesian column is no, for the same reason: completion juice is not the coefficient on squared error.

## 4. Checked, and not entered

These were read far enough to apply §2. They are not rows in §3.

- Nassar, Wilson, Heasly, and Gold 2010, doi 10.1523/JNEUROSCI.0822-10.2010, already in RS-SCREEN §3. The methods state one hazard, 0.05 after a five-trial gap, and four observation-noise standard deviations, 5, 15, 25, and 35. Noise level is not the state's change rate. Not re-entered.
- Filipowicz, Glaze, Kable, and Gold 2020, doi 10.7554/eLife.57872. Three hazard rates, 0.01, 0.30, and 0.99. The article names the deposit https://osf.io/4ahkx/. The project page is public in search. Files were not downloaded. Three rates are below four, and there is no stake manipulation.
- Khaw, Stevens, and Woodford 2017, doi 10.1016/j.jmoneco.2017.09.001, with the trial record in Khaw, Stevens, and Woodford 2017, *Data in Brief* 15:469, doi 10.1016/j.dib.2017.10.007, PMC page https://pmc.ncbi.nlm.nih.gov/articles/PMC5647523/ (loaded with no account; the trial table was not downloaded). One regime-change probability, δ = 0.5% per draw. The score on each draw is 1 − (s − p̂)², paid at 2¢ per point plus a fixed $10. The coefficient does not change across conditions. Not (i) or (ii).
- Chow, Knöll, Madsen, and Spering 2021, doi 10.1167/jov.21.3.19, article https://jov.arvojournals.org/article.aspx?articleid=2772407. Experiment 2 sets translational speed to 0.5, 1, 1.4, 2.1, or 4.2 m/s, and also sweeps contrast and coherence. The paper states that the focus-of-expansion random walk is held fixed across those manipulations. Remuneration is a flat CAD 12 per hour. The article names no repository. Five signal-strength levels are not four shock rates of the tracked state, and the payment is not a stake manipulation.
- Knöll, Pillow, and Huk 2018, doi 10.1073/pnas.1807192115. Continuous eye tracking of one focus-of-expansion random walk. The deposit named on the public project page https://osf.io/h5rxv/ was not downloaded. One rate, no stake manipulation.
- Bonnen, Burge, Yates, Pillow, and Cormack 2015, doi 10.1167/15.3.14. Continuous tracking at one diffusion coefficient, one pixel per frame, and six blob widths (11, 13, 17, 21, 25, and 29 arcmin). Visibility is not the state's change rate, and there is no stake manipulation.
- Aydın, Ünlütabak, and Uyanık 2023, bioRxiv preprint, doi 10.1101/2023.11.02.565374. Four flow speeds, 0, 4.5, 11, and 15.5 cm/s, and one refuge trajectory that is a sum of 13 sinusoids. Flow speed is not a sweep of the refuge's shock rate. The preprint says the data will be released with the final article. A later archive DOI found in search did not resolve on Crossref and is not cited.

RS-SCREEN §3 already closed single-hazard and two-hazard predictive-inference deposits, two-volatility binary tasks, vigilance time budgets, and electric-fish refuge archives that are not a reset-shock sweep. This screen does not reopen them.

## 5. What this note does not do

It does not lock, preregister, or hash a test. It does not add a Gate section, because no candidate clears the three bars. It does not download or open any outcome series. It does not qualify a class or move a CLAIM_MAP row. It does not edit `THEORY.md` or `CORE.md`. It does not treat an in-model exponent as a fact about a real system. It does not claim that a juice volume, an exponential penalty on time outside a circle, or a diffusion sweep stands in for the stake elasticity in RS-SCREEN §2.

The missing dataset is unchanged from RS-SCREEN §4. It is a strongly selected tracker of one continuous variable, with the world's type and rate logged from the world alone, at a stake w that is the coefficient on squared error. Either that rate takes at least four values spanning a wide factor, with the rival's value computed on the same error, or w itself is manipulated so that elasticity −1 can miss against elasticity 0. No public no-account deposit of that design was found.

## References (DOIs resolved on the Crossref API, 24 November 2026)

- Aydın, E. Y., Ünlütabak, B., and Uyanık, İ. 2023. The Effects of Flow Speeds on Smooth Pursuit Tracking and Active Sensing Movements of Weakly Electric Fish. bioRxiv preprint. doi 10.1101/2023.11.02.565374.
- Bonnen, K., Burge, J., Yates, J., Pillow, J., and Cormack, L. K. 2015. Continuous psychophysics: Target-tracking to measure visual sensitivity. *Journal of Vision* 15(3):14. doi 10.1167/15.3.14.
- Bonnen, K., Huk, A. C., and Cormack, L. K. 2017. Dynamic mechanisms of visually guided 3D motion tracking. *Journal of Neurophysiology* 118:1515. doi 10.1152/jn.00831.2016.
- Chow, H. M., Knöll, J., Madsen, M., and Spering, M. 2021. Look where you go: Characterizing eye movements toward optic flow. *Journal of Vision* 21(3):19. doi 10.1167/jov.21.3.19.
- Filipowicz, A. L. S., Glaze, C. M., Kable, J. W., and Gold, J. I. 2020. Pupil diameter encodes the idiosyncratic, cognitive complexity of belief updating. *eLife* 9:e57872. doi 10.7554/eLife.57872.
- Glaze, C. M., Kable, J. W., and Gold, J. I. 2015. Normative evidence accumulation in unpredictable environments. *eLife* 4:e08825. doi 10.7554/eLife.08825.
- Glaze, C. M., Filipowicz, A. L. S., Kable, J. W., Balasubramanian, V., and Gold, J. I. 2018. A bias–variance trade-off governs individual differences in on-line learning in an unpredictable environment. *Nature Human Behaviour* 2:213. doi 10.1038/s41562-018-0297-4.
- Janssen, C. P. and Brumby, D. P. 2015. Strategic Adaptation to Task Characteristics, Incentives, and Individual Differences in Dual-Tasking. *PLOS ONE* 10:e0130009. doi 10.1371/journal.pone.0130009.
- Joshua, M. and Lisberger, S. G. 2012. Reward Action in the Initiation of Smooth Pursuit Eye Movements. *Journal of Neuroscience* 32:2856. doi 10.1523/JNEUROSCI.4676-11.2012.
- Khaw, M. W., Stevens, L., and Woodford, M. 2017. Discrete adjustment to a changing environment: Experimental evidence. *Journal of Monetary Economics* 91:88. doi 10.1016/j.jmoneco.2017.09.001.
- Khaw, M. W., Stevens, L., and Woodford, M. 2017. Forecasting the outcome of a time-varying Bernoulli process: Data from a laboratory experiment. *Data in Brief* 15:469. doi 10.1016/j.dib.2017.10.007.
- Knöll, J., Pillow, J. W., and Huk, A. C. 2018. Lawful tracking of visual motion in humans, macaques, and marmosets in a naturalistic, continuous, and untrained behavioral context. *Proceedings of the National Academy of Sciences* 115:E10486. doi 10.1073/pnas.1807192115.
- Lixenberg, A. and Joshua, M. 2018. Encoding of Reward and Decoding Movement from the Frontal Eye Field during Smooth Pursuit Eye Movements. *Journal of Neuroscience* 38:10515. doi 10.1523/JNEUROSCI.1654-18.2018.
- Nassar, M. R., Wilson, R. C., Heasly, B., and Gold, J. I. 2010. An approximately Bayesian delta-rule model explains the dynamics of belief updating in a changing environment. *Journal of Neuroscience* 30:12366. doi 10.1523/JNEUROSCI.0822-10.2010.
