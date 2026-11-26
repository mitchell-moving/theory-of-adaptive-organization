# Gate read v4: PR #287, `theory/two-route-2026-11-25/PREREG_4.md`

*Independent paper read, Wednesday 25 November 2026, about 11:35 ET (America/New_York). Branch `forge-two-route-prereg`, head `47eb804` (same as `fork/forge-two-route-prereg`), lock commit `b9a2710`. Gate spec: draft PR #263, `process/PREREG_GATE.md` at `8c4b3c0`. Prior reads: `gate_read_287.md`, `_v2.md`, `_v3.md`. The worktree was not edited. Checked in an isolated temporary copy.*

*Side computations used the closed-form W2 expressions, which were verified symbolically in v3 (`p4.py`). They covered: the memory best reply at fixed g for each w_x ∈ {0.5, 1, 2}; the 1-step world reply; the full joint minimum; local gradients and curvatures at the joint minimum, with the 1D g- and c-surpluses; and the g=c slice. No Nash iteration was run and no G was computed. B-T2′ was not run.*

References are `PREREG_4.md:line` unless stated otherwise.

## Table

| # | Item | Result | file:line | Note |
|---|---|---|---|---|
| 1 | Gate at top, cites #263 head, append-only | PASS | :3, :9-21 | Supersedes A-T1″ only. PREREG.md, PREREG_2.md and PREREG_3.md are unchanged since their lock commits. The cited hashes match. |
| 2 | Shared w_x·E[x²] in J_m and J_w | PASS | :29-37 | As stated. J_tot carries 2w_x·Σxx. So v4 at w_x=0.5 equals v3's J_tot at w_x=1, and the joint-minimum numbers are consistent with my v3 probe. |
| 3 | Labeled a modeling choice | PASS | :39, :16 (G4) | This follows v3 row 8. It is described as a chance constraint, i.e. a variance cap, not a penalty. w_x=1 is a choice of units, and F3's loss of confinement is real (OPEN_WORK.md:249). The CORE.md:27 link is explicitly qualified. |
| 4 | (1) Memory best reply interior at all three w_x | PASS | :48-52 | Every claimed gc_BR value was reproduced to 3 decimals over g ∈ {0.5, 0.7, 0.9, 0.95, 0.97, 1.00, 1.02, 1.10}. The peaks are 0.656 (w_x=0.5, g=0.95), 0.543 (w_x=1, g=0.9; the file says 0.544) and 0.409 (w_x=2, g=0.7, reproduced as 0.408). Everything is ≤0.66, far from the guard. This fixes the v3 blocker. Caveat: this bracket covers only g∈[0.5, 1.1], which contains all three 1-step world replies. |
| 5 | 1-step world reply | PASS | :47 | g = 1.1338, 0.9686, 0.7603 (gc 0.672, 0.574, 0.450), reproduced. "Σxx=1 at g=0, so the g=0 memory optimum is unchanged" holds from the closed form. |
| 6 | Joint minimum interior at all three w_x | PASS | :46 | Reproduced: (5.7205, 0.8583, 0.7347; gc 0.6306; 14.0087), (5.7787, 0.8030, 0.6118; 0.4913; 16.1186), (5.9392, 0.7282, 0.4293; 0.3126; 19.2769). All interior. The relative shifts of −13.1% and +19.6% check. The g=c slice at w_x=1 has its minimum at gc 0.512 (16.31), with 44.41 at 0.95 and 1669.5 at 0.999, all reproduced. |
| 7 | Local gradients and curvatures | PASS | :55-58 | ∂_gJ_w = −2.859/−2.808/−2.783, ∂_cJ_w = −4.550/−3.699/−2.478, and ∂²_gJ_tot = 34.38/24.12/17.12, ∂²_cJ_tot = 52.43/39.39/31.33, all reproduced. ∂_cJ_m = +∂_cJ_w in absolute value, as claimed. |
| 8 | (3) Is the 1D surplus of about 0.04 grounded? | PASS (number) | :59 | Δg = 0.176/0.234/0.307 and g-surplus = 0.0381/0.0411/0.0419, reproduced. The file's Δg uses ∂²_gJ_w (16.23/11.98/9.06), which is consistent, though :59 only prints the J_tot curvatures. |
| 9 | (3) Are the branch odds grounded? | FAIL (weak, non-blocking) | :59-66 | The paper numbers point below the bar, not across it. The analogous 1D c-surplus (memory step Δc = −∂_cJ_m/∂²_cJ_m = −0.105/−0.107/−0.084) is **0.021/0.014/0.006**. The naive sum is about **0.059/0.055/0.048**, under 0.10 at all three w_x. The memory's γ-gradient (0.27/0.19/0.10) is also left out. Δg>0 and Δc<0 push gc in opposite directions, so the cross term has no definite sign. The stated "0.04–0.15 regime" upper end (:59) is not derived. For a hit, the Nash fixed point must roughly double the 1-step surplus at **all three** w_x. That is possible, since a fixed point with both players moving can exceed one step, so the hit odds are not ≈0. But 0.35 for the hit branch looks generous against this paper evidence; something like 0.15–0.25 seems closer. The miss odds (0.65) are, if anything, understated. Suggest a linearized best-reply (quadratic-model) Nash estimate on paper to set the odds. |
| 10 | (2) Can it honestly miss? | PASS | :16, :62-66 | Yes. The paper surplus is about 0.05–0.06, below the edge. |
| 11 | (2) Can it honestly hit? | PASS (weak) | :16, :61 | Yes, but only if iteration amplifies the 1-step surplus about 2× at all three w_x (row 9). The all-three rule is strict, but each clean outcome stays reachable. |
| 12 | (2) Robustness rule | PASS | :16, :62-63, :74 | Hit and clean miss need all three w_x to agree; a mixed result is `sensitivity-dependent`. This stops w_x=1 alone from deciding the outcome, and it is pre-committed. Minor: the signed size G(1)−0.10 for a mixed "miss" (:63) can be positive. Report max and min instead. |
| 13 | (2) Scoring: mixed = 0, no settling = 1 | FAIL (non-blocking, §6 skew) | :16, :64, :78 | (a) "no settling" at **any** w_x scores 1, while a w_x-dependent mixed result scores 0. That breaks the sweep's own logic: no settling at one w_x only is also w_x-dependent. (b) "No settling" is defined by the solver: alternating best replies, 200+200 rounds, damping 0.5. Cycling of best-reply iteration does not show that selection fails to settle when a Nash point exists, so "a W2 counterexample to settling for CX2" (:16 G5) overclaims. (c) CX2 is a **Route B** scope row (`PREREG_2.md:101`), so a Route A outcome could move Route B's row, or be claimed by Route A. This is unassigned. The expected skew is small (0.09 × 1 point), but it falls only on Route A's side: B-T2′'s INCONCLUSIVE scores 0. Fix: no settling scores 1 only if it occurs at all three w_x and survives damping; otherwise it is `sensitivity-dependent` (0). Also say which route a CX2 change counts for. |
| 14 | §6 "resolved" for A-T1″′ | PASS (minor ambiguity) | :74, :78 | Defined. The "…at all three w_x, **or** at w_x=1 with \|G(1)\|>0.02" clause at :78 reads two ways; :74 says G(1) is used. Pick one. |
| 15 | Boundary-hit rule | PASS | :65, :73 | Open miss, 0 under §6, odds 0.01. This is consistent with rows 4 and 6 (everything ≤0.68). The v3 contradiction is resolved. A half-tolerance failure is flagged `measurement/code` not-resolved (0). |
| 16 | A-T1″′ G2 | PASS | :16 | Nash point of a non-potential game, with no closed form. |
| 17 | A-T1″′ G3: weak G=0 rival | PASS | :16 | Labeled weak, with the reason. No rival in (0, 0.10). Gap 0.10, resolution 0.01, threshold 0.02. RI is silent on G. |
| 18 | A-T1″′ G4 | PASS | :16 | CORE.md:127 and :80. The CORE.md:27 link is qualified as a modeling stand-in. |
| 19 | A-T1″′ G5 | PASS (see 13b) | :16 | Hit, clean miss, mixed, no settling and boundary each lead to a different step. The no-settling step overclaims (row 13). |
| 20 | Boxes, grids, tolerances | PASS | :72 | Carried from PREREG_3 §2.1 and run at each w_x. |
| 21 | CONSISTENCY_CHECK labels; no TEST is an identity | PASS | :13-21 | Carried over. A-C5 now carries the caveat. |
| 22 | B-T2′ (carried) | PASS | :21, :79 | Unchanged from v3. |
| 23 | §5 order and stop rule | PASS | :79 | Step 0 is a fresh gate read of this file, then A-T1″′, then B-T2′, then the deliverables. |
| 24 | sha256 from own folder | PASS | PREREG_4.sha256:1 | `sha256sum -c PREREG_4.sha256` gives `PREREG_4.md: OK` (b16b3c2b…0f14914c). The blob at `b9a2710` hashes the same. |
| 25 | Lock commit contents | PASS | `b9a2710` (11:10:58 ET) | Only PREREG_4.md (+79) and PREREG_4.sha256 (+1). |
| 26 | Nothing run after the lock | PASS | `b9a2710..47eb804`; mtimes | 47eb804 (11:11:11 ET) appends one line each to DEVIATIONS.md and RESULTS.md ("No v2, v3, or v4 bar has been run") and adds pointers in OPEN_WORK.md and GAP_PLAN.md. `checks/` is unchanged since 08:53 ET. There is no A-T1″′ or B-T2′ script or output on the box. Git proves order only. |
| 27 | Wording: forbidden terms | PASS | whole file | None of "theory of everything", "solved", "bill", "kill", "dead", "verdict" or "puzzle". |
| 28 | Wording: "law" | PASS | :5 | Hypothesis sentence only, byte-identical to CORE.md:7. |
| 29 | No GR/QM/holography/gravity claim | PASS | whole file | None. |
| NB1 | v3: w_x motivation overstated, CORE.md:27 cite | FIXED | :39, :16 | |
| NB2 | v3: lock a w_x sweep | FIXED | :16, :72-74 | Made a scored robustness rule, which is stronger than the unscored sweep asked for. |
| NB3 | v3: paper-number slips (slice min, 841) | FIXED | :27; DEVIATIONS.md (last line) | |
| NB4 | v3: odds qualitative, branches not split | PARTIAL | :60-66 | Split into five branches summing to 1.00. Grounding is weak (row 9). |
| NB5 | v3: boundary-hit wording contradictory | FIXED | :73 | |
| NB6 | v3: A-C5 caveat not carried | FIXED | :15 | |
| NB7 | v3: git proves order only | UNCHANGED (inherent) | — | Step 0 remains the mitigation. |

## BLOCKING

None.

## NON-BLOCKING

- The hit odds (0.35) are generous against the paper evidence. The 1D g-surplus (≈0.04) plus the 1D c-surplus (0.021/0.014/0.006) sum to about 0.05–0.06 at each w_x. The "0.04–0.15" upper end is not derived, and the memory's γ-shift is left out. Suggest a linearized-Nash paper estimate, or lower the hit odds (row 9).
- §6 skew from "no settling" (row 13). It scores 1 at any single w_x while a mixed result scores 0. It is defined by a best-reply solver, not by the selection dynamics, so "counterexample to settling for CX2" overclaims. CX2 is Route B's scope row, and which route gets credit is unassigned. Score it 1 only if it occurs at all three w_x and survives damping, and state the route.
- A mixed result's signed size G(1)−0.10 can be positive. Report the range instead (row 12).
- The resolution clause at :78 ("all three … or at w_x=1") is ambiguous (row 14).
- The memory-reply bracket covers g∈[0.5, 1.1] only. That suffices for the 1-step replies but is not a proof for every Nash path (row 4).
- Git proves order only. This is inherent (NB7).

## Gate status

**GATE PASS** on G1-G5 for A-T1″′ (and B-T2′ as carried). No blocking item remains. The non-blocking items, mainly the hit-odds grounding and the no-settling scoring, should be fixed in an appended note before the §6 comparison is scored. They do not block the run.
