# P1 (sieve-to-judge): prior-art check and early stop

*Thursday 26 November 2026, 22:11–22:17 EST. Local note only; nothing committed, pushed, emailed or posted. Scope: Chad lifted the hold for P1 only (t187u, 22:11 EST). Source of P1: `sidechat/JUDGMENT_PEAK_2026-11-26.md` §4 P1 (file SHA-256 `4d50fb2f848eb8ee8cca8c3f719c8f0f987f792c4d42cda57b9f693ec6a267d7`, re-checked 22:12 EST).*

**Labels:** observed · hypothesis · proved-in-model (PIM) · known (published) · elementary.

## 0. Bottom line

**No prereg was written and no test was run.** Under the brief's stop rule, P1 stops at step 1:
1. **Prior art.** Both of P1's stated predictions are already settled by published work, in its class (known). (a) The sieve limit is Zurek–Habib–Paz 1993, and Dalvit–Dziarmaga–Zurek 2005 already extend the sieve to monitored systems (records of the system's own trajectory). (b) "A finite price below which feedback pays" is quantum LQG feedback (Doherty–Jacobs 1999; Wiseman–Milburn 2009) plus information-priced LQG control (Tanaka–Esfahani–Mitter 2018; Sims 2003). Fields–Friston–Glazebrook–Levin 2022 is a framework (quantum observers as agents minimizing prediction error). It does not contain P1's priced model, so P1 is not "their paper". But P1's outcomes are fixed by the other sources, so running it could not fail.
2. **Prediction (a) cannot fail (desk check, elementary).** For the oscillator, any quadratic loss a·Var x + b·Var p averaged over whole periods equals (a+b)(V_x+V_p)/2, and ZHP's purity-loss rate averages to 2D(V_x+V_p). Both are minimized by the coherent state, **because the Hamiltonian rotates phase space**, not because of the cost or the sieve (`desk_check_symmetry.py` → `.out`: optimal squeeze r = 0.0000 at horizons 2π and 20π for all four losses; at horizon 0.25 the x-only loss picks r = 1.3139). This is the relabel the side study's own fix R1 flagged; it would score as a MISS by construction, and it teaches nothing about judgment.
3. **Prediction (b) re-hits W2 and W1.** The threshold c* is a price ratio (stake ÷ decoherence rate, in the side study's own words). W2: prices are free; only ratios predict. W1/F2: the medium sets the scale. The existence of c* is known from information-priced LQG.
4. **The brief's judge criteria re-hit W10 and W15-reverse.** "Anticipation" (acting on a model of a hidden world variable) and "heritable record reuse" (handing the estimate to the next episode) pay in a linear-Gaussian world iff the world has a hidden variable that drifts (finite drift) and whose correlation time exceeds the episode or record lifetime. That is the Kalman prior, and it is the recorded wall: W10 (records only under drift) and W15-reverse (finite drift, finite record lifetime; TRACKABLE_WORLD R3–R4). Again, the outcome is fixed before computing.
5. **The judge is external by construction (W12/W13 risk).** In every P1 variant the controller is designed by the optimizer we supply. "The quantum system starts behaving like a judge once feedback has a price" is then true by assumption. The quantum system does not become a judge; the apparatus we attach is one.

## 1. Sources (every DOI checked on Crossref 26 Nov 2026, 22:14 EST; `/tmp/p1_crossref.out` copied below as `crossref.out`)

| source | DOI | what it settles for P1 (read: abstract unless noted) |
|---|---|---|
| Zurek, Habib & Paz 1993, PRL 70 | 10.1103/PhysRevLett.70.1187 | sieve: coherent states minimize entropy production for the weakly damped oscillator |
| Dalvit, Dziarmaga & Zurek 2005, PRA 72:062101 | 10.1103/PhysRevA.72.062101 | sieve under monitoring: four classicality criteria agree; heterodyne unravelling optimizes all four; coherent states for the underdamped oscillator; short times favor x-squeezed states (abstract + intro read via arXiv quant-ph/0509174) |
| Zurek 2003, RMP 75:715 | 10.1103/RevModPhys.75.715 | einselection review (cited, not re-read this run) |
| Fields, Friston, Glazebrook & Levin 2022, Prog. Biophys. Mol. Biol. 173 | 10.1016/j.pbiomolbio.2022.05.006 | quantum FEP: generic quantum systems as observers/agents minimizing Bayesian prediction error; asymptotically equivalent to unitarity (their claim). No priced action, no ruin cap, no solvable oscillator test (from abstract; full text not read) |
| Doherty & Jacobs 1999, PRA 60:2700 | 10.1103/PhysRevA.60.2700 | continuous estimation + feedback cools and confines an oscillator; maps to classical LQG |
| Wiseman & Milburn 2009, *Quantum Measurement and Control* (CUP) | 10.1017/CBO9780511813948 | textbook for quantum LQG (cited for the field; chapters not re-read) |
| Tanaka, Esfahani & Mitter 2018, IEEE TAC 63:37 | 10.1109/TAC.2017.2709618 | LQG with directed information minimized: optimal policy is a Gaussian sensor + Kalman filter + certainty-equivalence controller; links to the Nair–Evans data-rate theorem |
| Sims 2003, J. Monetary Econ. 50 | 10.1016/S0304-3932(03)00029-1 | rational inattention: action under a per-nat information cost (cited for the field) |
| Sagawa & Ueda 2008, PRL 100:080403 | 10.1103/PhysRevLett.100.080403 | entropy bound with discrete quantum feedback (cited for the field; already on main in `theory/GENERAL_FLOOR_ATTEMPT_2026-11-23.md`) |
| Still, Sivak, Bell & Crooks 2012, PRL 109:120604 | 10.1103/PhysRevLett.109.120604 | nonpredictive memory = dissipated work: efficient memories must be predictive (anticipation, classical) |
| Grimsmo 2013, PRA 87:060302 | 10.1103/physreva.87.060302 | quantum version of the Still et al. result (found by Crossref bibliographic query; abstract read via arXiv 1302.5552) |
| Annby-Andersson et al. 2022, PRL 129:050401 | 10.1103/PhysRevLett.129.050401 | quantum Fokker–Planck master equation for continuous measurement + feedback (the dynamics P1 would have used) |
| Elliott, Gu, Garner, Thompson et al. 2022, PRX 12:011007 | 10.1103/PhysRevX.12.011007 | quantum adaptive agents with memory advantages (nearest "quantum judge" architecture; not a sieve link) |

Also read (arXiv only, no DOI): Ghose 2026, arXiv 2602.16286, "What Kind of World Supports Darwinian Evolution? Quantum Foundational Options" — heredity needs a decohered classical record sector; copy/delete exist only there. Consistent with the side study's "sieve = selection without heredity".

**Not found (search not exhaustive):** one cost with a stake and a ruin cap whose zero-action limit is the sieve and whose priced regime is a judge. The assembly is unpublished as far as this search found; its outcome is fixed by the rows above, so it would be a relabel, not a result.

## 2. What this means for the judgment-first hypothesis (hypothesis; plain words)

- The sieve and a judge are already known to be different things in physics: decoherence keeps the states that stay predictable (no memory of the world, no choice, no heredity), and feedback control adds a record and an action. Where the price of information is low enough, adding a record and an action pays. That is known control theory, not a GTAO result.
- The part of Chad's idea this cannot test: whether the judge **arises** from below rather than being attached. In every solvable P1 variant the judge is the optimizer we add.
- One repo-relevant finding (elementary, observed by desk check): the coherent state is the optimum of **every** period-averaged quadratic task loss, purely from the oscillator's symmetry. So a decohered oscillator would sit "at a GTAO optimum" for free. That trips SCALE_ENDS SE4 failure test (iii) ("a non-hereditary, non-learning structure whose design sits measurably nearer a GTAO optimum than unselected controls", CLAIM_MAP N28) **trivially**, unless "GTAO optimum" is read as a task-set point that differs from the medium's symmetric point. This is a wording gap in a recorded failure clause, not a score change. Proposal only; N28 stays OPEN; CLAIM_MAP is not edited.

## 3. If Chad and Ace want a P1 that can fail (proposals only; not run, not preregistered)

- **P1-S (emergence, not design).** Replace the optimizer with selection: a population of linear controllers with heritable gains and mutation, reproducing by persistence (ruin cap) in a dephasing oscillator world with a drifting force. Open question: does selection alone find the anticipating controller, and does it keep the sieve state when the price is high? Risk: W12 (growth ranks designs) and N28 (needs heredity by definition). It can fail.
- **P1-T (task vs medium split).** Use a horizon shorter than a period, or an anisotropic task, where the sieve's state and the task's optimum separate (desk check: r = 1.31 at T = 0.25). Operational split: a sieve's state is set by the medium only; a judge's state moves with the task. Risk: this is H1/F1 ("world sets points, medium sets scales") again, in a quantum class.
- **SE4 (iii) wording fix** (repo, for Ace): require "nearer a task-set GTAO optimum that differs from the medium's symmetric point".

## 4. Files
- `desk_check_symmetry.py`, `desk_check_symmetry.out` (SHA-256 below in WORKLOG).
- `crossref.out` (Crossref check of the DOIs above).
