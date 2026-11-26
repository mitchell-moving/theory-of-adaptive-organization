# Gate read v2: PR #287, `theory/two-route-2026-11-25/PREREG_2.md`

*Independent paper read, Wednesday 25 November 2026, about 10:30 ET (America/New_York). Branch `forge-two-route-prereg`, head `57ffd7c`, lock commit `64c8b53`. Gate spec: draft PR #263, `process/PREREG_GATE.md` at `8c4b3c0` (still #263's head; the fetched file matches a local copy of PR #263 `process/PREREG_GATE.md` at `8c4b3c0`). Prior read: `gate_read_287.md`. Nothing in the checkout was edited. Side computations ran in an isolated temporary copy with the PR's own `checks/route_a_w2.py`: (i) the §1.4 paper step, (ii) the A-C5 paper numbers, and (iii) a well-posedness probe of A-T1′'s joint-minimum term. Only where the minimum sits and whether it moves are reported. No Nash search was run, no G was computed, and B-T2′ was not run.*

References are `PREREG_2.md:line` unless stated otherwise.

## Table

| # | Item | Result | file:line | Note |
|---|---|---|---|---|
| 1 | Gate at the top, cites #263 head | PASS | :3, :9-21 | Cites `8c4b3c0`, which is #263's current head. The Gate is the first section, after the title, the hypothesis sentence and the label key. |
| 2 | v1 BLOCKING 1 (A-T3 ill-posed) → A-T3 demoted to A-C5 | PASS | :15, :41-47, :107 | The demotion is correct. (a) With η free, the tracking term 2√(θaT0w) shrinks like η^-1/2 while W stays bounded, so J has no minimizer for any Tc≤T0. Bounding Tc<T0 does not fix that, as the file says. (b) With η=1 fixed, the optimum is a one-line closed-form minimization, so G2 fails and the label is right. I reproduced it: Tc*=0.1285 (w=10^3) to 0.0225 (10^6), slope **−0.5070**. The result is structural, because θ=(1+Tc)/2∈(T0/2,T0] limits the slope's departure from −1/2 to about 0.5·ln2/ln(10^3)≈0.05. A ≤−0.6 bar could never be reached. Caveat (non-blocking): \(\dot Q_c=\eta\Delta T/(1+\eta)^2\) is an overdamped construction. Two-bath heat flow through a particle is mass-dependent once inertia is kept (the standard form is ∝ηΔT/(m(1+η))), and then "W→0 as η→∞" (:45) is not true. The conclusion still holds: I get −0.5097 with that variant, and the η-free case still has no minimizer. |
| 3 | v1 BLOCKING 2 (B-T1 cannot miss) → B-C4 | PASS (label nit) | :20, :61-63, :108 | It is relabeled and not run, and its RI rival is dropped. Nit: #263 attaches `CONSISTENCY_CHECK` to a G2 failure. A G1 failure is "gate: stopped". The row says "Fails G1". Since R(k)≈x*²/k is computed on paper, G2 also fails, so the label stands, but the row should cite G2. |
| 4 | v1 BLOCKING 3 (A-T1 rival) → A-T1′ | PASS (formal) | :16, :49-59, :109 | One scored number, G=J_tot(Nash)/min J_tot−1. The rival (G=0) gives a value for that same number. The gap to the band edge is 0.10, against a resolution of 0.01. The cross-term error is corrected at :36. For the substance (rival honesty, well-posedness), see rows 15-19. |
| 5 | v1 BLOCKING 4 (A-T2 rival value) | PASS | :3, :110; DEVIATIONS.md:9-12; RESULTS.md:39 | ρ_RI=0.8774 is derived, and the v1 "+0.045" sentence is withdrawn. The value matches the prior read. No locked text was edited. No fresh A-T2′ is locked, and the reason (trend already seen) is sound (:25). |
| 6 | v1 BLOCKING 5 (A-T2 before the gate read) | PASS | :91, :111; process/FAILURES.md:43-45; DEVIATIONS.md:8 | Logged as `FORGE-GATE-1`. §5 step 0 requires a fresh gate read before any run. |
| 7 | CONSISTENCY_CHECK labels only on identities | PASS | :13-15, :17-20, :33-37 | A-C3: closed form. A-C4: detailed balance iff D⁻¹A is symmetric (agD_M=γcD), which I checked by algebra, plus F3/F4/CA1. A-C5: closed-form minimization (row 2). B-C1/B-C2/B-C3: known theorems. B-C4: paper estimate (row 3). Only B-C3 runs, as a code gate, and it carries no score (:19, :87). |
| 8 | No TEST is secretly an identity | PASS | :16, :21 | A-T1′ is the Nash point of a non-potential two-bath game, with no closed form. B-T2′ is an enumeration of stochastic potentials over random landscapes, also with no closed form. |
| 9 | Paper-step check, A-T1′ | PASS | :53 | Reproduced: at (6.884, 0.592, g=0), Σ=(1, 0.5172, 0.4516), the slope is 1.1453 and gc=0.678. |
| 10 | A-T1′ G1: miss band and odds | PASS (weak) | :16, :55, :59 | The miss is G<0.10, or no settling. The 0.55 odds rest on one best-reply step plus a qualitative "near the boundary" argument. That is plausible but is not a paper estimate of G. |
| 11 | A-T1′ G2 | PASS | :16 | The scored quantity is a Nash point of a non-potential game. |
| 12 | A-T1′ G3: same quantity, gap | PASS (formal) | :16, :57-59 | Same quantity G. The gap of 0.10 exceeds 2× the resolution. |
| 13 | A-T1′: is G=0 an honest rival? | FAIL (weak, non-blocking) | :16, :51 | G=0 is the simplest null, and a weak one. Each party's cost leaves out its effect on the other's heat and stake. Cost shares therefore do not match stakes, so by the logic of CA1/CT31 (`CORE.md:127`) the model makes Nash≠joint minimum except by coincidence. The rival is close to refuted by the game's own construction, as v1's f=0 was by F6, and it is not labeled weak. The open question is the size of G: G≥0.10 against 0<G<0.10. No rival predicts a value in (0, 0.10), so a miss at G∈(0.02, 0.10) refutes the hypothesis and the rival together. |
| 14 | A-T1′: could RI predict the same? | PASS (wording) | :16, :57 | No. RI per party is the best-reply map, so it predicts where the system sits (the Nash point), not a value of G. RI is silent on G rather than "predicting the Nash number" (:16). It cannot coincide with the hypothesis and is correctly left out as a rival. |
| 15 | A-T1′: defined optimum (G1/G2 well-posedness) | **FAIL** | :55, :83-84 | **The joint minimum is a boundary optimum, set by the 0.95 confinement margin.** Probe (γ optimized along g=c): J_tot falls monotonically as gc→1 (gc 0.25: 14.63; 0.81: 10.43; 0.90: 9.85; 0.98: 9.39; 0.998: 9.28). Σxx diverges (1.3 to 438), and the loss stays bounded because the slow mode is x=gm. A full joint minimization under margins 0.95 and 0.99 lands exactly on gc=0.95 and gc=0.99 respectively, and min J_tot moves by more than 1% between them. The denominator of G is therefore a function of an arbitrary locked number, not of the model, at a shift larger than the 0.01 resolution. The boundary rule (:84) makes G computable but not meaningful. This is the same pattern as v1 BLOCKING 1 (an optimum set by a bound), now in stated form. The prereg anticipates it (:55) and still uses it to set the odds. |
| 16 | A-T1′ world stake | NOTE (non-blocking) | :51 | Since \(J_w=(a^2+w_w)E[(x-gm)^2]-aD\), the world's best reply is argmin E[(x−gm)²] for any w_w. The stake w_w=10 changes only J_tot, and so the joint minimum and G, not the Nash point. That is worth stating, since G then depends on an accounting weight that the world's behavior ignores. |
| 17 | A-T1′ G4 | PASS | :16 | `CORE.md:127` (coupling that settles) and `CORE.md:80` (memory steers the world) exist and fit. |
| 18 | A-T1′ G5 | PASS | :16 | Hit, miss and no-settling lead to different next steps. |
| 19 | A-T1′ grid | PASS (minor) | :81-86 | The start grid, Brent bounds, joint grid, damping and round caps are stated. c has a start grid but no box, although the boundary rule refers to a "box edge". |
| 20 | B-T2′ G1: band [0.10, 0.35], odds 0.45 | PASS | :21, :67-69 | The paper heuristic gives f≈0.1-0.2, which straddles the lower edge, so 0.45 is honest. The lower edge moved from 0.05 to 0.10 after the gate read, with no B-T2 data seen (no Route B output exists in git or on the box). Note: the edge was moved to meet the 0.10-gap rule, not on theoretical grounds, and it now sits on the heuristic's low end. |
| 21 | B-T2′ G2 | PASS | :21 | Enumeration with no closed form. |
| 22 | B-T2′ G3 | PASS (weak) | :21 | f=0: gap exactly 0.10. f=0.5: gap 0.15. 2SE≤0.032 at n=1000 (binomial SE ≤0.0158 checked). The f=0 rival is in-model contrary to F6 (`CLAIM_MAP_v2.md:890`), so the random-basin null is the honest rival. RI is silent, correctly. |
| 23 | B-T2′ G4/G5 | PASS | :21 | `CORE.md:127`; F6 row :890. Hit and miss lead to different steps. |
| 24 | B-T2′ procedure | PASS | :69, :87 | The seed, draws and qualification rule are those of PREREG.md §3.5 (:129-135). There is a brute-force cross-check, a code gate at c=(1,1), and a 30-minute CPU cap. |
| 25 | §5 budget, order and stop rule | PASS | :89-91 | Order 0→1→2→3. One executor session per route plus one review round. A test not scored in its session counts as a process miss. No recompute under a changed model. |
| 26 | §6 balanced criterion | PASS | :93-101 | 2·2+1=5 for each route. |
| 27 | §6 "resolved" defined | FAIL (minor) | :21, :101 | It is defined, but for B-T2′ it is ambiguous. (a) The Gate row calls the resolution "2SE", so "2× the stated resolution" means 4SE, while :101 writes "2SE of f". (b) It does not say which of the two rivals (f=0 or 0.5) the distance is measured from. |
| 28 | §6 pre-banked status change | FAIL (minor) | :46-47, :101 | "Narrowed by … a PAPER result" counts toward S. §1.3 is already a PAPER result that narrows CL11 (no minimizer with η free, RI scaling with η fixed), so Route A can collect 2 points from text written before any run. §1.5 is a comparable PAPER statement on CX2 for Route B. §6 should say whether PAPER results already in the prereg count. |
| 29 | sha256 from its own folder | PASS | PREREG_2.sha256:1 | `cd theory/two-route-2026-11-25 && sha256sum -c PREREG_2.sha256` gives `PREREG_2.md: OK` (57d1caab…e01ce293). The blob at `64c8b53` hashes the same. |
| 30 | Lock commit contents | PASS | `64c8b53` (09:31:45 ET) | Only PREREG_2.md (+128) and PREREG_2.sha256 (+1). |
| 31 | No bar run after the lock | PASS | git log `64c8b53..57ffd7c`; mtimes | Later commits touch only STATUS.md, OPEN_WORK.md and theory/GAP_PLAN.md, and there is no diff in the folder. All folder mtimes are ≤09:31:45 ET. `checks/` holds only route_a_w2.py (08:52:40) and .out (08:53:01). The gitignored `__pycache__` is from 09:28:33, before the lock, consistent with the `stats()` recomputation in DEVIATIONS.md:9-12. No A-T1′/B-T2′ script or output exists on the box. As before, git proves order, not where pre-lock exploration happened. |
| 32 | Wording: forbidden terms | PASS | whole file | None of "theory of everything", "solved", "bill", "kill", "dead", "verdict" or "puzzle" appears. |
| 33 | Wording: "law" | PASS | :5 | Appears only in the hypothesis sentence, byte-identical to `CORE.md:7`. |
| 34 | No GR/QM/holography/gravity claim | PASS | whole file | None of these is mentioned. |
| NB1 | Gate at top | PASS | :9 | |
| NB2 | A-C1 run although an identity | PASS | :116 | Acknowledged. v2 runs only B-C3, as a code gate. |
| NB3 | A-T2 paper attempt / v2 paper attempts | PASS (weak) | :117; DEVIATIONS.md:9-12; :53, :67 | The RI value is computed. The v2 paper attempts exist, but neither estimates the scored number itself. |
| NB4 | A-T3 reach to THEORY.md:37 | PASS | :47 | `THEORY.md:37` is the open-lever/responding-world line. The A-C5 Gate row lists G4 as "—", which is fine for a CHECK. |
| NB5 | B-T2 f=0 rival "labeled weak" | FAIL (minor) | :21, :119 | §7 says it is labeled weak, but the Gate row (:21) and §1.6 do not say so. |
| NB6 | Gap ≥0.10 on every scored number | PASS | :21-23 | True: 0.10 exactly for B-T2′ and A-T1′. |
| NB7 | Order fixed, v1 deviation logged | PASS | :91; DEVIATIONS.md:13 | |
| NB8 | §6 balanced and "resolved" defined | PASS (partial) | :101 | Balanced, yes. "Resolved" is ambiguous for B-T2′ (row 27), and the PAPER pre-bank is open (row 28). |
| NB9 | sha256 from the folder | PASS | row 29 | |
| NB10 | crossref.out | PASS | :124 | No action needed. |
| NB11 | Git shows order only | PASS | :91, :125 | Mitigated by step 0, the second reader. |
| NB12 | 09:05 stamps | PASS | DEVIATIONS.md:14; RESULTS.md:40 | Corrected to 08:53 ET by appended lines. |
| NB13 | Grid stated | PASS (minor) | :79-87 | Stated. Row 19 (no c box) and row 15 (the margin sets G) still apply. |
| NB14 | "second law" in RESULTS.md | PASS | RESULTS.md:41; process/PROCESS.md:39 | PROCESS.md:39 allows "law" in physics names. |

## BLOCKING

1. **A-T1′'s joint minimum is set by the locked confinement margin, not by the model (row 15).** J_tot falls monotonically as gc→1 (Σxx diverges along the slow mode x=gm while the loss stays bounded). Under margins 0.95 and 0.99 the joint optimum lands on gc=margin both times, and min J_tot shifts by more than 1%, which is above G's 0.01 resolution. So G, and the outcome against the 0.10 edge, depends on an arbitrary number. This is the same failure class as v1's A-T3. Before A-T1′ runs, do one of the following: derive the margin from the model (for example a stated settling-time or variance cap with its own cost in J_tot); add a cost that diverges as gc→1; define G at a stated interior target; or lock the bar on a limit or margin-sweep that is shown to converge. Then restate the odds.

## NON-BLOCKING

- A-T1′'s rival G=0 is the simplest null and weak. By construction cost shares ≠ stakes, so Nash = joint minimum only by coincidence. No rival predicts a size in (0, 0.10). Label it weak, or name a sized rival (row 13).
- A-T1′ :16 says RI "predicts the Nash number". RI predicts the Nash point and is silent on G (row 14).
- A-T1′'s 0.55 odds are not a paper estimate of G (row 10). The world's best reply ignores w_w, which moves only the joint minimum (row 16).
- No box on c, although the boundary rule refers to a box edge (row 19).
- A-C5: the overdamped heat-current formula is model-specific. "W→0 as η→∞" fails under an inertial formula, but the conclusion stands (row 2).
- B-C4 is labeled "Fails G1". #263's CONSISTENCY_CHECK label is for G2. Cite G2 (row 3).
- B-T2′'s lower edge was moved to 0.10 to meet the gap rule and now sits on the low end of the paper heuristic (row 20). The f=0 rival is contrary to F6 and not labeled weak in the Gate row, despite §7's claim (rows 22, NB5).
- §6: for B-T2′, "resolved" is ambiguous between 2SE and 4SE, and the rival is unnamed (row 27). The prereg's own PAPER results (§1.3, §1.5) could count as status changes. Say whether they do (row 28).
- Pre-lock exploration cannot be ruled out by git; only order is shown (row 31).
