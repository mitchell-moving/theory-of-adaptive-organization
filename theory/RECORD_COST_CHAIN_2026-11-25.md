# Record cost under drift: what a self-tracking world can copy, and which records cost least

*Wednesday 25 November 2026 (America/New_York). Side R&D, consolidated from a private session into one note. Status words are those at `CORE.md:169`. `THEORY.md` and `CORE.md` are unchanged. The memory-coordinate definition was locked first, in `theory/record-cost-2026-11-25/PREREG.md` (sha256 in `PREREG.sha256`). Scripts and their outputs are in `theory/record-cost-2026-11-25/scripts/`; Lean is in `formal/lean/GTAO/Rnd/`. The adversarial review of this note is `theory/reviews/RECORD_COST_CHAIN_REVIEW_2026-11-25.md`. Nothing here derives quantum theory, general relativity, holography, or gravity.*

The hypothesis sentence is the one at `CORE.md:7`. Selecting state spaces by their cost applies that hypothesis by assumption. It is not tested here.

**Labels.** **PROVED (in-model)**: proved inside the stated toy model, and machine-checked where the Lean column says so. **OBSERVED (numerical)**: computed by a script in the stated toy model, not proved. **KNOWN**: published and credited. **HYPOTHESIS**: a reading or a premise. **OPEN** and **open miss** as at `CORE.md:169`.

## 1. Claim, narrowed

**Premise CD (stated, not derived): the world drifts continuously.** Reversible change is a compact connected group acting non-trivially on the state space, relative to the tracker.

Under premise CD, and the further premises in §2, the cost of keeping records selects quantum-like records in the toy models below: only drift-fixed distinctions can be copied, a copyable one-bit record that survives free drift needs a state space of affine dimension at least 3, polygons pay an irreversibility cost the disk does not, and the qubit ball is the smallest space in the transitive class that passes (that last step rests on the named assumption NA1, §5). **That is the whole claim: cost selects quantum-like records under drift.** Without drift the claim does not hold in these models (§4, open miss 1).

The steps are mostly known (§6). What is new is only the chain: the same cost read through self-tracking premises links the known steps. This is a SYNTHESIS in the sense of `CORE.md:169`, built from PROVED (in-model) steps. It is not a new theorem about quantum mechanics, and it does not derive quantum theory.

What carries which label: the copy ban (S1), the dimension bound (S2) and the polygon cost bound (S3) are PROVED (in-model) under the named assumptions of §5. The cost comparisons that rank the polygons, boxworld and the ball are OBSERVED (numerical) in stated models. That the lowest-cost state space is the one found in nature is the HYPOTHESIS, applied by assumption.

## 2. Premises and the toy model

- **State spaces.** A system is a compact convex set with affine effects into [0,1] (the generalized probabilistic theory frame; Barrett 2007). No Hilbert space, no ħ, no heat.
- **No outside frame (HYPOTHESIS).** The tracker is part of the world it tracks. It knows the drift only through a finite internal record.
- **Finite capacity.** Each perfectly distinguishable alternative costs more than zero, so a finite cost means a finite capacity \(N\).
- **Continuous drift (premise CD above).**
- **Records survive the drift.** A record of a distinction is kept only if the drift leaves it fixed.
- **Cost (toy reading).** \(J=\kappa I_{\mathrm{mem}}+q\cdot(\text{errors})+\lambda\Sigma\), with \(\Sigma\) the path irreversibility (KL rate between forward and reversed path measures) of a tracker that follows the drift, and \(q\) the stake. \(I_{\mathrm{mem}}\) on a GPT memory is §4.
- **Selection (HYPOTHESIS).** The lowest-cost state space persists. This is the hypothesis sentence applied to state spaces by assumption.

## 3. The chain, step by step

Session labels used in the Lean doc comments map to these steps: R2a′ → S1; R3 and §R3.4 item 3 → S2; the polygon C3 of the no-cloning route → S3; the self-reference C3 and §R3.4 item 4 → S4; P1, P2 → S5; B1 → S6; C2 → S7; C4 → S8; R1d → S9; R4a → S10; §R3.4 item 5 (F1) → open miss 2.

| step | statement | status | Lean (`formal/lean/GTAO/Rnd/`) | attribution |
|---|---|---|---|---|
| S1 | No linear map clones every point of a circle orbit through a state the drift moves. Only drift-fixed distinctions can be copied. Covers every compact connected drift. | PROVED (in-model); the Lie setting is assumption NA5 | `SelfRef/R34.lean` `fourier_core`, `no_linear_clone_gpt`; `SelfRef/CircleOrbit.lean` `no_linear_clone_circle` | KNOWN in substance: einselection (Zurek 2003); superselection without a reference frame (Bartlett, Rudolph, Spekkens 2007); no-broadcasting (Barnum, Barrett, Leifer, Wilce 2007) |
| S2 | A state space with free continuous drift and \(N\) jointly distinguishable drift-fixed states has affine dimension \(d\ge N+1\). For one bit, \(d\ge3\): every simplex fails, the disk (rebit) fails, the qubit ball meets it with equality. | PROVED (in-model) under assumption NA2 | `SelfRef/R34.lean` `R3_full`; `SelfRef/DimBound.lean` `dim_bound` | KNOWN in substance: Hardy 2001; Müller and Masanes 2013; Masanes, Müller, Augusiak, Pérez-García 2013; Barnum, Müller, Ududec 2014 |
| S3 | A polygon tracker following drift by jumps pays \(\lambda\Sigma\ge\lambda\cdot2\Theta^2/V\) for any number of corners; finite and discrete groups have no non-trivial continuous one-parameter subgroup; SO(2) has one. | PROVED (in-model) with definitions NA3, NA4 taken | `PolygonDrift.lean` `ring_bound`, `factor_ge_two`, `discrete_oneParam_trivial`, `disk_oneParam`, `disk_strictly_cheaper` | The general bound is the thermodynamic uncertainty relation, KNOWN (Barato and Seifert 2015; Gingrich et al. 2016) |
| S4 | In \(d=3\), a reversible group transitive on pure states with a connected drift fixing a distinguishable pure pair makes the state space a ball (in the invariant inner product). The double cone and cylinder are excluded. | Group step PROVED (in-model); the rest rests on assumption NA1 | `SelfRef/Ball.lean` `normal_fixer_bot`, `normal_nontrivial_fixes_nothing`; `SelfRefRun/Round2.lean` `normal_fixer_trivial` | Ball as the minimal case: Hardy 2001; Müller and Masanes 2013. Transitivity as the reading of "no outside frame" is close to bit symmetry (Müller and Ududec 2012) |
| S5 | A price that depends only on a count, is nondecreasing, and adds over independent records is \(c\log\) of that count. Linear parameter pricing is not additive; \(c\log K\) is additive exactly in locally tomographic theories. | PROVED (in-model) | `Composition.lean` `P1`, `log_additive_iff`, `P2_entries` | Completely additive monotone functions: a classical result; the application is ours |
| S6 | Sharp records plus an injective answer pattern beyond capacity cannot be cloned (Lemma B1). | PROVED (in-model) | `LemmaB1.lean` `lemmaB1`, `lemmaB1_k`, `clone2_to_k`; controls in `Controls.lean`, `SquareBit.lean`; toy-theory cloning in `Spekkens.lean` | Close to Barnum et al. 2007; toy theory of Spekkens 2007 |
| S7 | Discrete ticks do not escape S1 if the world keeps producing reversible novelty: polytope symmetries have finite order. | PROVED (in-model) | `SelfRefRun/Basic.lean` `perm_periodic` | Complements Pfister and Wehner 2013 |
| S8 | A tracker inside its world that records which datum arrived has no state fixed by two different writes, so zero drift holds only for a tracker that acquires nothing. | PROVED (in-model) | `SelfRefRun/Round2.lean` `no_zero_drift_while_recording` | ours, elementary |
| S9 | A self-referential flip with a fixed state gives each outcome probability exactly ½. True in classical probability too, so it separates deterministic from indefinite worlds, not classical from quantum. | PROVED (in-model) | `SelfRef/Liar.lean` `liar_half`, `sharp_flip_no_fixed` | The ½ is one line. Context for the fixed-point side: Lawvere 1969; Hasegawa 1997 (Theorem 3.1, text read); Fox 1976 |
| S10 | Cost dial between the stake direction and the conserved axis: stationary at the midpoint exactly when \(\rho=2wRD/(q\kappa)=1/(2\cos(\beta/2))\), which is \(1/\sqrt3\) at \(\beta=60^\circ\). | Stationarity PROVED (in-model); that it is the global minimum is OPEN | `SelfRef/CostDial.lean` `Jdial_stationary_iff`, `Jdial_midpoint`, `Jdial_midpoint_60` | A cost version of Zurek's redundancy (Zurek 2009); the refresh term is a modelling choice |

**Observed (numerical), in the stated models** (scripts in `theory/record-cost-2026-11-25/scripts/`). These are reruns of the scripts that produced the session's numbers, made from a fresh copy after the prereg lock; no new computation was made. Every printed output the session kept matches byte for byte, and every JSON output matches value for value:

- At fixed capacity price, non-simplex state spaces answer a later question with error from 0.125 (square) to 0.182 (disk), against 0.25 for the classical bit (`nocloning/polygons.py`). Polygon random-access advantages are studied by Massar and Patra 2014.
- Boxworld's reversible group on two gbits is finite, with 128 elements (`composition/t3_boxworld.py`; consistent with Gross, Müller, Colbeck, Dahlsten 2010). Under drift, the quantum pair (4.039) beats the boxworld pair once the total drift angle passes a crossover: between 0.3 and 1 rad at \(\lambda=0.05\), between 1 and 2 rad at \(\lambda=0.005\), at \(q=4\) (`composition/t5_bipartite_drift.py`). The joint-question blur model there is stylized.
- Complete-record test: the connected reversible maps that fix every state of a complete distinguishable record have dimension 0 in real quantum theory and \(N-1\) in complex quantum theory, for \(N=2,3,4,6,9\) (`composition/round2/r2_checks.py`; `selfref/e_round2.py`). Quaternionic quantum theory passes (open miss 3).

## 4. The memory coordinate: both readings, one definition

`CORE.md:52` names the memory coordinate as A6's mutual information of one joint distribution. On a GPT memory that is not unique (Short and Wehner 2010). Two readings, with the numbers under each, at zero drift and \(q=4\) (`composition/t6_pricing_additivity.py`, `composition/round2/r2_record_pricing.py`, `composition/round2/r2_checks.py`):

| comparison | total (one mutual information) | per retrievable record (information causality as a price) |
|---|---|---|
| single systems | square 1.50 vs ball 1.73: square cheaper (hexagon 1.67, octagon 1.69 and pentagon 1.70 also beat the ball) | ball 1.73 vs square 2.50: ball cheaper (the closest rival is the pentagon, 1.77) |
| pairs | boxworld 3.00 vs quantum 4.04: boxworld cheaper | quantum 4.04 vs boxworld ≥ 5.00: quantum cheaper |
| stake where the rivals win again | — | above \(q\approx7.7\) (pairs) and \(q\approx12.4\)–\(17.6\) (single systems) |

The stake \(q=4\) is the session's convention, not derived. The boxworld pair price under the per-record reading is a lower bound. At zero drift the disk (rebit) ties the ball and the real-quantum pair ties the quantum pair under both readings.

**Definition used (locked before any further run):** the total reading, \(I_{\mathrm{mem}}(W;S)=\sup_M I(W;M)\) over fine-grained readouts \(M\) of the memory, with \(W\) the joint variable of every record held. **Reason, from A6 and not from the outcome:** A6 is the mutual information of one joint distribution; each readout gives one distribution, so the definition applies A6 verbatim and needs no GPT entropy. The per-record sum adds mutual informations of readouts that need not share any joint distribution, so it is outside A6, and the repo already records that the representation axioms do not force information causality (ledger T71). The step from A6's discretization supremum to a supremum over readouts is an analogy, not a consequence. The full argument and its weak points are in the prereg. One further point, added after the lock and not changing the definition, is in `theory/record-cost-2026-11-25/PREREG_ADDENDUM_1.md`: on a classical memory, where A6 is unambiguous, the per-record sum already differs from A6 (a memory holding \(X_0\oplus X_1\) of two fair independent bits has A6 information 1 bit and per-record sum 0), so the per-record reading is not an extension of A6. If that reason is judged insufficient, the coordinate on GPT memories is **open**, and both columns carry equal weight.

Under this definition, quantum theory does **not** win at zero drift. The zero-drift result stays an **open miss**.

## 5. Named assumptions

Each is declared here and in `formal/lean/README.md` (section RND-RECORD-COST). None is a Lean `axiom`; each enters as a hypothesis of a theorem, or as a definition, or sits outside the formal statement.

- **NA1. SO(3) connected-subgroup classification (Mathlib gap).** The closed connected subgroups of SO(3) are the trivial group, a conjugate of SO(2), or SO(3). This is not in Mathlib. S4's conclusion that the state space is a ball uses it, together with Krein–Milman and faithfulness on extreme points, which are not linked up in Lean. **Ball uniqueness is therefore assumed, not machine-checked.** The "ball" is round in the invariant inner product, an ellipsoid in the original coordinates.
- **NA2. Inner-product-preserving drift behind \(d\ge N+1\).** `R3_full` takes as a hypothesis (`hinv`) that the linear parts of the drift are isometries of one inner product and depend continuously on the group element. For a compact group this follows by Haar averaging, which is not formalized. The hypothesis says nothing about fixed points or dimension; without some such input the isometry step fails (a shear fixes a line in \(d=2\) and preserves no compact body).
- **NA3. Polygon \(V\) and \(\sigma\) taken as definitions.** The Skellam variance \(V\) and the entropy-production rate \(\sigma=(k_+-k_-)\ln(k_+/k_-)\) are definitions in `PolygonDrift.lean`, not derived from a Markov path measure. "A polygon tracker is a nearest-neighbour ring chain" is a modelling step.
- **NA4. "The disk pays 0" is a definition.** \(\Sigma=0\) for a deterministic invertible flow. Lean proves only that SO(2) has the continuous subgroup and discrete groups do not.
- **NA5. Lie setting for S1.** That a compact connected drift moving a state contains a circle subgroup moving it, and that circle orbits have finite integer-weight form, are standard facts used as the setting, not formalized.
- **NA6. Modelling fields.** The `CopyModel` fields in `LemmaB1.lean`; the tensor property assumed in `Composition.lean` `gbit_no_local_write`; and the refresh term \(wRD\sin^2\alpha\) in the cost dial.

## 6. Attribution, plainly

- The bound \(d\ge N+1\) is **known in substance**: Hardy 2001; Müller and Masanes 2013; Masanes, Müller, Augusiak, Pérez-García 2013; Barnum, Müller, Ududec 2014. No explicit statement of this form was found, but it follows from those results.
- "Copyable = drift-fixed" is **known**: Zurek's einselection (2003) and Bartlett, Rudolph, Spekkens (2007).
- The per-record pricing in §4 **is information causality** (Pawłowski et al. 2009) used as a price. Short and Wehner 2010 tie its failure in boxworld to non-subadditivity.
- The polygon bound is the thermodynamic uncertainty relation applied to a ring tracker.
- The qubit ball as the minimal case is Hardy's simplicity axiom and Müller and Masanes' result; the reconstructions themselves include Masanes and Müller 2011 and Chiribella, D'Ariano, Perinotti 2011.
- **New is only the chain through the cost:** self-tracking premises and one cost link the steps above, with explicit crossover numbers. Each structural conclusion matches an existing reconstruction axiom one to one (additivity to \(N_{AB}=N_AN_B\); link price to local tomography; drift to continuous reversibility).

## 7. Open misses

| # | open miss | diagnosis | next test |
|---|---|---|---|
| 1 | **Zero drift.** Without drift the square and boxworld are cheaper (§4, total reading). The per-record reading flips it only below \(q\approx7.7\)–\(17.6\). Self-induced read drift does not close it: a sure read of the square destroys its other bit, and with destroyed bits priced the square ties the classical \(N=4\) record while the ball still loses on repeated reads (errors 0.19 then 0.29–0.31; `selfref/f_selfdrift.py`, which borrows the qubit read rule). | The chain's selection needs drift. S8 does not close it: an acquiring tracker must drift itself, but that self-drift is a discrete write the square absorbs by permutation. | Compute the stake \(q\) strongly selected systems face in the worked classes, to see which side of the thresholds they sit on. |
| 2 | **Finite worlds before recurrence.** A finite reversible world is periodic; in the long run there is no differential persistence, so the hypothesis is idle there, not contradicted. Before recurrence, finite classical worlds have records and transient selection and evade S7. | S7 needs persistent novelty. | Ask whether a self-tracking world can know it is before recurrence. |
| 3 | **Quaternionic quantum theory passes the complete-record test.** S4's minimality excludes it only at \(N=2\). | The test separates real from complex, not complex from quaternionic. | A composition test (local tomography) on quaternionic pairs. |
| 4 | **Purification is not forced.** "No outside frame" and "no information lost for free" hold in a classical world with a mixed ancilla (`composition/t4_purification.py`). | Purification needs "the whole is pure", which the cost does not supply. | Keep it as a companion premise, labelled HYPOTHESIS (it is an axiom in Chiribella, D'Ariano, Perinotti 2010), or find a cost term that prices irreducible mixedness. |
| 5 | **Self-reference alone does not force no-cloning.** Lawvere-type arguments give "a part cannot copy the whole at once", true classically. The copy ban in S1 comes from finite capacity plus drift; self-reference supplies only the "no outside frame" premise. | The ban is a joint consequence. | None planned; stated as the honest scope. |

Also open: real against complex quantum theory separates only with an added premise (records that survive drift, or a link price); the cost-dial global minimum (S10); the step from S2 and S4 to "unique cheapest" uses a dimension price inside the transitive class, which additivity alone does not fix (S5).

## 8. Sources

DOIs resolved on the Crossref API on 25 November 2026 (Hardy 2001 on DataCite); title, authors, and year match. Raw output: `theory/record-cost-2026-11-25/doi_check.out` (script `doi_check.py`).

- Barato, Seifert 2015, PRL 114:158101, `10.1103/PhysRevLett.114.158101`
- Barnum, Barrett, Leifer, Wilce 2007, "Generalized No-Broadcasting Theorem", PRL 99:240501, `10.1103/PhysRevLett.99.240501`
- Barnum, Müller, Ududec 2014, NJP 16:123029, `10.1088/1367-2630/16/12/123029`
- Barrett 2007, PRA 75:032304, `10.1103/PhysRevA.75.032304`
- Bartlett, Rudolph, Spekkens 2007, RMP 79:555–609, `10.1103/RevModPhys.79.555`
- Chiribella, D'Ariano, Perinotti 2010, PRA 81:062348, `10.1103/PhysRevA.81.062348`
- Chiribella, D'Ariano, Perinotti 2011, PRA 84:012311, `10.1103/PhysRevA.84.012311`
- Fox 1976, Comm. Algebra 4:665–667, `10.1080/00927877608822127`
- Gingrich, Horowitz, Perunov, England 2016, PRL 116:120601, `10.1103/PhysRevLett.116.120601`
- Gross, Müller, Colbeck, Dahlsten 2010, PRL 104:080402, `10.1103/PhysRevLett.104.080402`
- Hardy 2001, "Quantum Theory From Five Reasonable Axioms", arXiv quant-ph/0101012, DataCite `10.48550/arXiv.quant-ph/0101012`
- Hasegawa 1997, LNCS 1210:196–213, `10.1007/3-540-62688-3_37`
- Lawvere 1969, LNM 92:134–145, `10.1007/BFb0080769`
- Masanes, Müller 2011, NJP 13:063001, `10.1088/1367-2630/13/6/063001`
- Masanes, Müller, Augusiak, Pérez-García 2013, PNAS 110:16373–16377, `10.1073/pnas.1304884110`
- Massar, Patra 2014, PRA 89:052124, `10.1103/PhysRevA.89.052124`
- Müller, Masanes 2013, NJP 15:053040, `10.1088/1367-2630/15/5/053040`
- Müller, Ududec 2012, PRL 108:130401, `10.1103/PhysRevLett.108.130401`
- Pawłowski, Paterek, Kaszlikowski, Scarani, Winter, Żukowski 2009, Nature 461:1101–1104, `10.1038/nature08400`
- Pfister, Wehner 2013, Nat. Commun. 4:1851, `10.1038/ncomms2821`
- Short, Wehner 2010, NJP 12:033023, `10.1088/1367-2630/12/3/033023`
- Spekkens 2007, PRA 75:032110, `10.1103/PhysRevA.75.032110`
- Zurek 2003, RMP 75:715–775, `10.1103/RevModPhys.75.715`
- Zurek 2009, Nat. Phys. 5:181–188, `10.1038/nphys1202`

## 9. Reproduce

- Scripts: from each folder under `theory/record-cost-2026-11-25/scripts/`, run `python3 <script>.py` (numpy, scipy; `t3_boxworld.py` also needs networkx). In `composition/round2/`, run `r2_record_pricing.py` before `r2_checks.py`. Outputs are the `.stdout` and `.json` files beside them.
- Lean: `tools/check_lean.sh` (in the dedicated Lean checkout), then `lake env lean scripts/RndAxioms.lean` in `formal/lean/` for `#print axioms` on the 62 exported theorems.
