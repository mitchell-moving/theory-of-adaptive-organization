# Gate read v3: PR #287, `theory/two-route-2026-11-25/PREREG_3.md`

*Independent paper read, Wednesday 25 November 2026, about 11:20 ET (America/New_York). Branch `forge-two-route-prereg`, head `768ce28` (the same as `fork/forge-two-route-prereg`), lock commit `78ff15a`. Gate spec: draft PR #263, `process/PREREG_GATE.md` at `8c4b3c0`. Prior reads: `gate_read_287.md` and `gate_read_287_v2.md`. The worktree was not edited. Checked in an isolated temporary copy.*

*Side computations, all on paper and in closed form, from `verify.py`, `probe3.py` and `probe4.py` there:*
- *a sympy check of every §1.1 expression;*
- *the 1-step world reply at w_x ∈ {0.5, 1, 2};*
- *the g=c slice;*
- *the full joint minimum at w_x ∈ {0.5, 1, 2};*
- *the memory's best reply on a grid of fixed world gains g.*

*No Nash iteration was run and no G was computed. B-T2′ was not run.*

References are `PREREG_3.md:line` unless stated otherwise.

## Table

| # | Item | Result | file:line | Note |
|---|---|---|---|---|
| 1 | Gate at top, cites #263 head, append-only | PASS | :3, :9-21 | Supersedes A-T1′ only. PREREG.md and PREREG_2.md are untouched; their hashes are cited and their files are unchanged since their lock commits. |
| 2 | §1.1 closed forms (Σxm, Σxx, Σmm, Q̇_X, Q̇_M, E[(x−gm)²], E[(x−m)²]) | PASS | :29-43 | Each expression was checked symbolically against the 2×2 Lyapunov solution; all match exactly. Cross-check :45 reproduced: E[(x−gm)²]=0.773134 and Q̇_M=1.849987. |
| 3 | v2 limit 2√44−4 | PASS | :47 | min over γ of ((1−γ)²+40)/(1+γ) = 9.266499, which agrees with the v2 probe (9.278 at gc=0.998). |
| 4 | v2 blocker: joint minimum set by the margin | PASS | :53-61 | With w_x=1, the full joint minimum is interior: γ≈5.72, c≈0.858, g≈0.735, **gc≈0.631**, J_tot≈14.01, Σxx≈2.49. This is well inside every box and far from the 0.999 guard. The claim that J_tot diverges as gc→1⁻ holds: Σxx∼(1−gc)⁻¹ for g,c>0. It also holds as γ→0⁺: at g=1 the 1/γ term of E[(x−m)²] cancels, but w_x·Σxx still diverges, so it depends on w_x>0. |
| 5 | g=c slice numbers | PASS (minor errors) | :16, :67, :75 | The values at gc = 0.25, 0.5, 0.7, 0.8, 0.9, 0.95 and 0.99 reproduce to 2 decimals. Two errors: (a) the slice minimum is at **gc≈0.64** (14.11), not "near 0.70" (14.20 there, and 14.14 at 0.6). (b) :75 says J_tot>900 at gc=0.999 along g=c; I get **840.8**. Neither changes the conclusion. |
| 6 | 1-step world reply | PASS | :16, :66 | Reproduced: g=0.9686, gc=0.5737, J_w=8.0144. The v2 claim at :52 (γc²=2.415>2, unconstrained reply g=γc/2=2.038) also checks. |
| 7 | ∂J_w/∂g at g=0 = −(1+w_w−w_x)γc/(1+γ) | PASS | :62 | Checked. w_w now enters the world's reply, fixing v2 row 16. |
| 8 | Is w_x motivated by the model? Do the CORE cites support it? | **FAIL** (non-blocking) | :16, :53, :60; CORE.md:5, :27, :66 | CORE.md:5 says "under a cap on the chance of ruin", and :27 and :66 say "subject to P(ruin)≤ε". These are chance constraints on ruin. They are not a quadratic penalty on the world's coordinate. For a Gaussian x, P(\|x\|>X)≤ε is exactly a cap on Σxx, which is option (i), and :51 rejects that option as an arbitrary cutoff. So the cites support the rejected option more than the chosen one. w_x·E[x²] is at most a Lagrangian stand-in, with w_x as a free multiplier. "w_x=1 matching a=D=D_M=1" (:53) is a choice of units, not a derivation. Calling the g=c=1 zero mode "unphysical" (:60) overstates it: it is F3's loss of confinement, a phenomenon the CX2 row names. The term was added after the v2 read and before any run. That is allowed for a prereg, and no G information leaked. It should be labeled a modeling choice with a free stake, not "justification from the model" (:59). |
| 9 | Is w_x=1 arbitrary in a way that decides G? | NOTE (cannot settle without a Nash run) | :56 | Joint-minimum sensitivity: w_x=0.5 gives gc≈0.735 and J_tot≈12.57 (−10.3%). w_x=2 gives gc≈0.491 and J_tot≈16.12 (+15.1%). The 1-step world reply moves from gc 0.672 (w_x=0.5) to 0.574 (w_x=1) to 0.450 (w_x=2). Both ends of G move by 10-15% over a factor of 2 in w_x. That is the same order as the 0.10 band edge, so w_x can plausibly decide the side of 0.10, as w=w_w=10 can. Recommend reporting G as a reference-point number with an unscored w_x ∈ {0.5, 2} sweep, locked as "reported, not scored". |
| 10 | Nash side is interior (well-posedness of the scored Nash point) | **FAIL** | :61, :68, :79 | w_x enters J_w only. The memory's own cost J_m=Q̇_M+w·E[(x−m)²] keeps the g=c=1 zero mode. Memory best reply at fixed world g: gc=0.917 (g=0.95), **0.950 (g=0.97)**, 0.983 (g=0.99), **0.999, on the guard (g=1.00)**, then 0.966 (g=1.02) and 0.826 (g=1.1). The paper's own first world reply is g≈0.969, which lands where the memory's reply is at gc≈0.95 and rising steeply toward the guard. "Forcing a strictly interior minimum" (:61) is shown for J_tot and J_w, not for the Nash point. A Nash search may end on gc=0.999, which :79 makes "not resolved / boundary-hit". That branch has no stated odds. |
| 11 | A-T1″ G1: miss band and odds 0.50 | FAIL (weak) | :16, :68 | The 0.50 is a two-sided qualitative argument and still not a paper estimate of G. The outcome set is hit / miss / no settling / boundary-hit (row 10). The non-hit odds are split among those branches without being stated. |
| 12 | A-T1″ G2 | PASS | :16 | The Nash point of a non-potential game, with no closed form. |
| 13 | A-T1″ G3: weak G=0 rival | PASS | :16, :69 | Labeled **weak**, with the reason (each party's cost omits its externality). States that no rival predicts a value in (0, 0.10), and that a miss in (0.02, 0.10) rejects both. Gap 0.10, resolution 0.01, threshold 0.02. |
| 14 | RI wording | PASS | :16 | "predicts the Nash point and is silent on G". |
| 15 | A-T1″ G4 | PASS (minor) | :16 | CORE.md:127 and :80 fit. The added CORE.md:27 is a ruin chance constraint, not a confinement cost on the world (row 8). |
| 16 | A-T1″ G5 | PASS | :16 | Hit, miss and no settling lead to different next steps. |
| 17 | Coordinate boxes | PASS | :75-78 | lnγ∈[−3,5], c∈[−2,3], g∈[0,3], all stated. The joint minimum is interior (row 4). Memory start grid c∈{−1,…,3} lies inside the box. |
| 18 | Solver guard at gc≤0.999 and boundary rule | FAIL (minor) | :75, :79 | The guard is sound for the joint minimum: J_tot is about 841 at the guard against about 14 inside. But :79 calls a boundary hit both "not resolved" and "logged as an open miss". State whether a boundary hit counts as a miss of the hypothesis or only as unresolved (0 under §6), and give its odds (row 10). |
| 19 | CONSISTENCY_CHECK labels on identities only; no TEST secretly one | PASS | :13-20 | Carried from v2. B-C4 now cites G2 and G1, which fixes v2 NB. A-T1″ and B-T2′ have no closed form. |
| 20 | B-T2′ (carried) | PASS | :21, :93 | Band [0.10, 0.35], odds 0.45. f=0 is labeled weak. The lower edge is disclosed as set by the gap rule. Primary rival f=0.5, gap 0.15. |
| 21 | §5 budget, order, stop rule | PASS | :97 | Carried: step 0 is a fresh gate read of this file, then A-T1″, then B-T2′, then the deliverables. |
| 22 | §6 balanced; "resolved" defined | PASS | :88-92 | 5 and 5. A-T1″: \|G\|>0.02 or no settling. B-T2′: \|f−0.5\|>4SE (>0.064 at n=1000), measured from the non-weak rival. Unambiguous. A boundary hit is not resolved (but see row 18). |
| 23 | §6 pre-banked PAPER points | PASS | :89 | §1.3 and §1.5 of PREREG_2 explicitly do not count. |
| 24 | sha256 from own folder | PASS | PREREG_3.sha256:1 | Inside the folder, `sha256sum -c PREREG_3.sha256` reports `PREREG_3.md: OK` (06610e7a…1354c8d). The blob at `78ff15a` hashes the same. |
| 25 | Lock commit contents | PASS | `78ff15a` (10:53:21 ET) | Only PREREG_3.md (+97) and PREREG_3.sha256 (+1). |
| 26 | Nothing run after the lock | PASS | `78ff15a..768ce28`; mtimes | 768ce28 (10:53:49 ET) appends one line each to DEVIATIONS.md and RESULTS.md ("No v2 or v3 bar has been run") and edits OPEN_WORK.md and GAP_PLAN.md pointers. `checks/` is unchanged since 08:53 ET (pycache 09:28). There is no A-T1″/B-T2′ script or output on the box. As before, git proves order only. The §1.2 slice numbers imply pre-lock paper computation off-repo; that is allowed as PAPER, and no Nash or G values are present. |
| 27 | Wording: forbidden terms | PASS | whole file | None of "theory of everything", "solved", "bill", "kill", "dead", "verdict" or "puzzle". "ruin" is CORE's own term. |
| 28 | Wording: "law" | PASS | :5 | Hypothesis sentence only, byte-identical to CORE.md:7. |
| 29 | No GR/QM/holography/gravity claim | PASS | whole file | None. |
| NB1 | v2: G=0 rival weak; no rival in (0, 0.10) | FIXED | :16, :69 | |
| NB2 | v2: RI "Nash number" wording | FIXED | :16 | |
| NB3 | v2: 0.50 odds not a paper estimate of G; w_w cancels in the world reply | PARTIAL | :62, :68 | The w_w point is fixed. The odds are still qualitative (row 11). |
| NB4 | v2: no box on c | FIXED | :75 | |
| NB5 | v2: A-C5 overdamped heat-formula caveat | NOT FIXED (minor) | :15 | The A-C5 row is carried over unchanged, with no caveat. The conclusion is unaffected. |
| NB6 | v2: B-C4 should cite G2 | FIXED | :20 | |
| NB7 | v2: B-T2′ lower edge set by the gap rule; f=0 not labeled weak | FIXED (by disclosure) | :21, :93 | Labeled and disclosed. The edge itself is unchanged. |
| NB8 | v2: §6 "resolved" ambiguous; pre-banked PAPER points | FIXED | :89-92 | |
| NB9 | v2: git proves order only | UNCHANGED (inherent) | — | No action is possible. Step 0, the fresh reader, remains the mitigation. |

## BLOCKING

1. **A-T1″'s Nash point is not shown to be interior. The fix removes the zero mode from J_w and J_tot but not from J_m (rows 10, 11, 18).** The memory's best reply at fixed world gain rises steeply to the gc=0.999 guard as g→1 (gc 0.95 at g=0.97, on the guard at g=1.00). The paper's own first world reply is g≈0.969. A Nash search can therefore end on the guard, which :79 makes "not resolved" (and also, ambiguously, an "open miss"), and the 0.50 odds give that branch no probability. Before A-T1″ runs, do one of the following:
   - (a) give the memory a confinement term too (for example price E[x²] or E[m²] in J_m, stated as a modeling choice);
   - (b) show on paper that the alternating best replies stay inside gc<0.999;
   - (c) state the odds of a boundary hit separately and fix whether a boundary hit is a miss or only unresolved.

## NON-BLOCKING

- The w_x motivation is overstated (row 8). CORE.md:5, :27 and :66 state a ruin chance constraint, which for Gaussian x is the Σxx cap rejected at :51, not a quadratic penalty. w_x=1 is a choice of units. The F3 zero mode is a real phenomenon, not an "unphysical" one. Relabel the term as a modeling choice with a free stake, and drop or qualify the CORE.md:27 reach cite (row 15).
- w_x moves the joint minimum by −10% to +15% (gc 0.73 to 0.49) over w_x∈[0.5, 2], so it can plausibly decide the side of 0.10. Lock an unscored w_x sweep alongside the scored reference point (row 9).
- Paper-number errors: the slice minimum is at gc≈0.64 (14.11), not ≈0.70, and J_tot at gc=0.999 on g=c is 841, not >900 (row 5).
- The 0.50 odds are still qualitative and do not split the hit / miss / no-settling / boundary branches (row 11).
- The boundary-hit wording at :79 is contradictory ("not resolved" and "open miss") (row 18).
- The A-C5 overdamped heat-formula caveat from v2 was not carried in (NB5).
- Git proves order only. This is inherent and unchanged (NB9).
