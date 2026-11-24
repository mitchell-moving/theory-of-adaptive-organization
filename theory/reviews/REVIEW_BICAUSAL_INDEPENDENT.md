# Independent review

Head `2df1925d96f7992b29eb2905fd32b1db36c9e6d8` on `forge-record-ratio-bicausal`. Scope is the three commits `6849d6a`, `9c004d7`, and `2df1925`, their parents back to `5660367007438f6cfa68c4f93cc38a140bebbe97`, the two preregistration files, and the files on this branch and on main that those commits cite. The recomputation below does not import `bicausal_checks.py`. It uses the antipodal closed form and checks that form against `functionals` to `5.6×10^{-17}`.

P1–P5 miss, and the miss is what the locks score. The headline numbers recompute. No blocker. Three limits sit under the headline: the parent's continuous best reply is the constant root `0.6` wherever `P_D>0`; the wide rationalizing sets are the equator-end formula already on this branch; the path-KL paragraph locks two different boundary terms, and the run scores the displayed equation.

## Checks

`python3 tools/check_consistency.py`: `FAIL: 0`, `INFO (frozen records): 29`, `RESULT: PASS`. Maintained docs scanned `31`, wording FAILs `0`. Frozen records scanned `503`. CLAIM_MAP section N: `68` rows, `123` references, `0` mismatches. Process-rule FAILs `0` (`14` self-review headers, `392` CLAIM_MAP rows, `124` tables). Core-rule FAILs `0`. Two advisory length warnings: THEORY.md main text `11325` words, README.md `1857` words.

`python3 tools/check_open_work.py`: `items.json not-DONE: 62`; `QUEUE.md not-DONE: 90`; `union missing from OPEN_WORK.md: 0`; `RESULT: PASS`.

`python3 tools/check_fresh.py`: `STATUS.md main is d592662`; window `0f37918 d592662 f4ec246 341b7de b611a68`; `RESULT: PASS`. The freshness FAIL that appears only because the fork's `origin/main` lags did not appear.

`python3 -m pytest -q tools`: `313 passed, 1 skipped` in `390.14s`, exit `0`. The skip is `tools/test_lean.py:124`, `Lean 4 / lake is not installed`.

`python3 theory/record-ratio-bicausal-2026-11-24/bicausal_checks.py`: exit `0`. Stdout is byte-identical to `bicausal_checks.out` (`458` lines). Summary:

- `G-parent PASS`, `G-rev PASS`, `G-iter PASS`
- `P1 FAIL unpinned=71 of 72`
- `P2 FAIL bad=71 pinned=1`
- `P3 FAIL same=46`
- `P4 FAIL bad=119`
- `P5 FAIL` with the sixteen reason tags printed in the file
- `B-blanket CONTRADICTED`, `S-share NOT-MET`, `F-copy REPRODUCED`, `F-bulk REPRODUCED`, `H-iface REPRODUCED`
- `FAILS 5`
- `ADV-nocost cells=24 unique0=16 multi=8 empty=0 alpha0_with_0_in_R=24`

The three bicausal commits do not edit the T78 errata. Those lines exist on `forge-record-ratio-persistence` at `b96d499`, which is after the branch point `5660367`. A tip-to-tip diff shows them as removed because the branches diverged. A merge keeps them.

## Preregistration

Each lock is its own commit, and the scored script is absent from both.

| File | Commit | sha256 | Blob at the lock and at HEAD |
|---|---|---|---|
| `PREREG.md` | `6849d6abaf7611c412633d51f1411c2643ccedcd` | `b78addd0edf765e9fa76c1f0d82cfdc88a30d9105b8bb0ddd5a4e6410a37e39e` | `7ca121a8c59684fdfa5fa263cb404aeda8dcd645` |
| `PREREG_3.md` | `9c004d7ac266181f4e3f1ca2ca27ac2998be5b18` | `6f89428bca13a08d9714f08cca260c83e4719ae4a7f735055f815ad5c66430c9` | `d83ea010d41d930b94c26bd768382ecb77633f4c` |

The sha256 files match the bytes. `THEORY.md` is blob `6caadae569116a94a74563398be94cebf6e99e9b` at `5660367` and at HEAD.

P4, the claim that the pinned ratio is a function of `τ` alone, is locked in `PREREG.md` at the heading `P4`, line `223`, in commit `6849d6a`. That commit contains only `PREREG.md` and `PREREG.sha256`. `bicausal_checks.py` does not exist there. Its absence would have been blocking. It is present.

P5 is locked in `PREREG_3.md`, commit `9c004d7`, still before the script. There is no `PREREG_2.md`. The run log says the timescale clause was inside the first lock. That is where it is.

The locks do not contain the scored grid's distinctive outputs (`1.075559`, `1.551351`, `1.706013`, `71 of 72`). `RUN_LOG.md` says no deviation and that neither preregistration was edited after its commit. The blobs agree. Every miss is a `FAIL` line in the stdout and a puzzle section in `MEMO.md`. One internal clash in the P5 lock is recorded under Medium below. It was present at `9c004d7`. It is not a later edit.

## Independent recomputation

Parent root. With `c=(1-α)/2` and `u'(α)=(1/(2 ln 2)) ln((1-c)/c)`, the equation `u'(α)=1` is `(1-c)/c=4`, so `c=1/5` and `α=1-2/5=0.6`. Evaluated `u'(0.6)=1`. On the equator, `P_D=0.09637237851`, the grid costs at `α=0.58` and `α=0.62` sit `4.29×10^{-5}` and `4.40×10^{-5}` above `α=0.6`. The small-tie return is `0.600000`. With `κ_{D,p}=0` the unique return is `0`.

Single pin. Child accounting, `τ=0.5`, `w=2`, small tie rule: one Nash pair, `θ=1.075559`, `α=0.600000`, `β=0.300000`, `I=0.02061162696`, `P_D=0.07576075155`. On the locked ratio grid the rationalizing set is `{0.30}`. The continuous interval on which that grid angle stays optimal is `(0.299874, 0.300038)`, width `1.65×10^{-4}`. The gaps at `q=0.28` and `q=0.32` are `2.05×10^{-4}` and `2.04×10^{-4}`, both far above the `10^{-9}` tie. The singleton is the charged share, and it is sharp. The large tie rule on the same cell adds the pointer at `α=1`, with grid set `[0.38, 2.00]` and midpoint `1.19`.

Two-cycle. Child accounting, `τ=0`, `w=2`, small tie rule: the exhaustive Nash set is empty. Best-reply iteration from `(θ,α)=(0,0)`, from `(π/2, 1)`, and from `(π/4, 0.2)` all enter the cycle `(0, 0) ↔ (π/2, 0.60)`. The large tie rule on that cell has a pure Nash at `α=1`. Stackelberg on the empty cell is `0.38`.

`R=[0, 0.64]` at `τ=0`, `w=1`, small tie rule. The Nash is the equator at `α=0.6`. The grid set has `33` points, from `0` through `0.64`, midpoint `0.32`. The continuous upper edge is `0.64000010`. The same edge at effective stake `2` is `0.28000021`, grid `[0, 0.28]`, midpoint `0.14`. At `κ_c=2` the normalized stake is `1/2`, the edge is `0.82000005`, the grid set is `[0, 0.82]`, and the midpoint is `0.41`.

Entropy production, child Nash cloud, equation as scored. Steady `σ` runs from `1.7060134×10^{-8}` to `1.5513515×10^{-2}`. The minimum has `q_hat=0.32`. The maximum has `q_hat=0.30`. Path KL from the three locked starts spans `0.359032` to `1.565091`, `7.068414` to `8.675755`, and `1.071406` to `4.336982`. The union is `0.359032` to `8.675755`. Each start's minimum is the cell `τ=0`, `w=1`, large tie, `α=1`, `q_hat=1.35`. The steady minimum is `τ=0`, `w=1`, small tie, `α=0.6`.

Headline recount: `72` cells, `1` pinned, `71` unpinned, `8` empty Nash sets, `46` cells where the unique Nash return equals the Stackelberg return.

## Attacks tried

**(a) Is "q stays a set" the linearity of `J` in `q` restated?** On the equator cells, yes, and the endpoints are a formula already printed here. `theory/RECORD_RATIO_DUAL_2026-11-24.md:5` records the T76 fact that `J` is linear in `q`, so a minimization cannot select an interior ratio, and on this menu it selects the boundary `0` when `P_D>0`. The same memo's equator-end formula is `1-w r^2=0.64` at `w=1` (`:21`). T78's memo at the branch point prints the equator-end quotient `0.640000050577` and says the restoration support is every ratio that installs the winning angle (`theory/record-ratio-persistence-2026-11-24/MEMO.md:15` and `:23`). `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md:5` records that T74's routes A1–A8 do not fix the ratio. The recomputed edges `0.64000010`, `0.28000021`, and `0.82000005` are `1-(w/κ_c) r^2` with `r=0.6`. The midpoints `0.32`, `0.14`, and `0.41` are half those edges. T79 adds three things this linearity does not already say: a pure Nash can be missing (the 2-cycle under the small tie rule); a leader can move the return (at `τ=0`, `w=1`, small tie, Nash `0.60` at the equator costs the parent `0.245347`, Stackelberg `0.70` at the pointer costs `0.243972`, gap `0.001375`); and the locked entropy production does not order `q`. The one pin is the remaining piece. Its continuous width is `1.65×10^{-4}` around `β=0.30`, which is the restoration identity at an interior grid angle. The memo says that.

**(b) Is `0.6` an artifact of a binary-entropy parent cost chosen by hand?** It is the closed form of that choice. `PREREG.md:110-148` states the choices and derives `α_★=1-2/(1+4^{κ_{D,p}/κ_p})`. The loss term in `J_p` does not depend on `α`, so the root does not depend on either stake. `G-parent` checks that the grid finds this root. The attack does not find a hidden substitution. The lock already says the factor is the binary-entropy derivative and is not a stake share.

**(c) Is time symmetry, or an assumed return, built in? Are the asymmetric starts asymmetric?** No assumed numerical return is an input. The functional form that forces `0.6` is an input, and section (b) covers it. The continuous parent root is `0.6` at every angle with `P_D>0`. On the grid the small tie rule returns a different index on three angles: the pointer, where `P_D=0` and every `α` ties, and the two neighbors (`P_D=4.95×10^{-7}` and `1.98×10^{-6}`), where the `10^{-9}` band covers more than one grid step around `0.6`. The child's angle does not move the continuous root. The two-way pieces that remain are that corner, which is the 2-cycle, and the leader's commitment, which is the `0.001375` gap.

The rate table does not copy reverse rates from forward rates. `K→U` and `D→U` are both `1`, the persistence clock. `D→K=α ρ (P_D+ε_0)+ε_0`. At `α ρ=1` that is still `P_D+2ε_0` against `K→D=P_D+ε_0`. The iteration starts are `(0,0)`, `(π/2, 1)`, and `(π/4, 0.2)`. The path starts are `(0.80, 0.15, 0.05)`, `(0.05, 0.20, 0.75)`, and `(0.50, 0.40, 0.10)`. Swapping `U` with `D` in any of them produces a triple that is not one of the three. None is uniform. `SEED=20261124` is assigned and unused. The script does not import a random module. On the empty cell all three iteration starts fall into the same cycle. On the path KL all three starts pick the same minimizing cell, and that cell differs from the steady minimum. The three starts agree with each other. The split the clause detects is path KL against steady `σ`.

**(d) Is the entropy production the path-space KL, forward against reversed?** The steady sum is. For a stationary chain, `Σ π_i k_{ij} ln(k_{ij}/k_{ji})` equals `Σ π_i k_{ij} ln(π_i k_{ij}/(π_j k_{ji}))`, because the extra `ln(π_i/π_j)` term cancels when inflow equals outflow. The recomputation agrees to `2.5×10^{-17}` on every headline pair. The sign is `ln(k_{ij}/k_{ji})`. Six equal off-diagonal rates give `σ=0` and `π=(1/3,1/3,1/3)`. `G-rev` passes for the right algebraic reason.

The finite-time object is where the lock disagrees with itself. `PREREG_3.md:71-77` displays

`σ_path = Σ_t Σ_{i≠j} p_t(i) P_{ij} ln(P_{ij}/P_{ji}) + (H(p_n)-H(p_0))`.

The code implements that expression. `H(p_n)-H(p_0)` is the expected system-entropy change, and the whole expression is the path KL against the time-reversed chain started from the final marginal. The sentence in the same paragraph names the boundary `E[ln p_0(x_0)-ln p_0(x_n)]` and a fixed reference `p_0` on both ends. That boundary differs from `H(p_n)-H(p_0)` by `KL(p_n‖p_0)`. Rescored with the fixed reference, the three child spans are `0.383303` to `1.630570`, `8.329348` to `10.027750`, and `1.236999` to `4.562968`. Each start's minimizing cell is unchanged. Steady `σ`, which carries the P5 clauses about `q` at `0` and at `1`, does not use this boundary. The printed path ranges are the equation's ranges. The miss of P5 stands under both boundaries.

The steady numbers are small because the chain sits in the unrecorded state. At the minimum, `π=(0.999998, 9.67×10^{-7}, 1.03×10^{-6})`. Of `37` child Nash pairs, `35` have `σ<10^{-3}`. The two that do not are the interior pin under the two tie rules, and even there `π_U=0.980`. The memo's clue says this. The calculation of the locked chain is right, and the chain's dynamic range is that one interior point against an `ε_0` leak.

**(e) Do the common-cause targets cite real lines, and are the reproduced ones nontrivial?** The boundary, holographic, mirror, and T69 question lines say what the lock attributes to them.

- `CORE.md:7` is the hypothesis sentence.
- `theory/BOUNDARY_SUFFICIENCY_2026-11-22.md:13` states that the decision loss follows the blanket, with exterior variances `3/5` and `1/2`. Line `17` says the heat-minimizing channel on the blanket alone does not hold. Lines `45-51` are Proposition BS-loss, including the sentence that an exterior mean-square loss is a function of the blanket posterior alone.
- `theory/HOLOGRAPHIC_2026-11-22.md:13-17` says the bulk per-site cost is not a holographic encoding and does not encode a bulk on a boundary. Lines `40-44` are Proposition H-iface and the start of H-floor.
- `theory/FRACTAL_WORLD_2026-11-22.md:13-15` says the minimum cost scales with the sites the decision names and does not scale with Hausdorff or spectral dimension. Lines `76-78` are the heading "Only the boundary", a blank line, and the status line that the named-site bound is proved and a dimension reading is a metaphor. The named-site numbers begin at line `80`.
- `theory/SWARM_RULE_2026-11-23.md:40` is the opening sentence that parts each minimize their own cost. Line `46` is the leave/tamper item, where `D_i=0` at share `s_i=w_i/W`. The align sentence, the part's choice equals the whole's optimum if and only if `s_i=w_i/W`, is line `47`.
- Mirror review at `e3e0e701`, `theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md:31`, `:36`, and `:60`, and `MIRROR_MEMO.md:13`, `:46`, and `:168`, say what `PREREG_3.md` attributes to them, including the reviewer note that the conjugate was already in the real time-symmetric start.
- T69 at `dfb530d`, `theory/layer-fixed-point-2026-11-23/PREREG.md:1` and `:5`, ask whether a nested-layer map has a renormalization fixed point and say the lock tests that question. This review did not re-score that outcome.
- T78 `PREREG.md:84-93` is the restoration definition and `:102-110` is the ruin map. The base-selector dominance is the memo at line `11`, immediately above the cited `:13-17`.

`F-copy` doubles `(I, P_D, L)`. Any cost that is linear in those three scalars is unchanged in its argmin and doubles in value. The memo says this is homogeneity. `F-bulk` sets `bulk = 1.0 * 100.0` and never reads `bulk`. `H-iface` prints that same result a second time. The absolute distance `|0.32-0.25|=0.07` is outside `0.02`. The reproduced rows are the cost equation and an unused factor. The memo says a bulk match is not extra evidence. `B-blanket` and `S-share` fail for the reason in section (b): the return is a function of `P_D` through `u`, and hiding `P_D` or changing the stakes does not implement the cited targets. Those two labels match the run.

**(f) Hidden classical-record assumptions.** `PREREG.md:114` states that the child keeps a classical record. The path model is a classical three-state chain whose keep and destroy rates are the scalars `I` and `P_D` in those units, with reset rate `1` and floor `ε_0=10^{-6}`. The qubit ensemble supplies `(I, P_D, L)` and is not given a new state in the game. The locks say they do not derive quantum mechanics. This review does not find a further classical-record assumption tucked into a result sentence.

**(g) Banned wording.** A scan of `theory/record-ratio-bicausal-2026-11-24/` (including `bicausal_checks.py` and `bicausal_checks.out`), of the added `OPEN_WORK.md` row, and of the added `theory/README.md` row finds no `theory of everything`, no `solved`, no `bill`, no `kill`, and no `verdict`. The word `law` appears in the hypothesis sentence and not outside it. The preregistrations and the memo say that nothing here derives general relativity, quantum mechanics, holography, or gravity. The wording test in `tools/test_bicausal_checks.py` does not open the stdout file. The scan above did. It is clean.

**(h) DOIs, Crossref on this review.** Each returned HTTP `200`, and the author, year, venue, volume, and pages match the lock.

- `10.1103/PhysRevLett.78.2690`: Jarzynski, C., Nonequilibrium Equality for Free Energy Differences, Physical Review Letters `78`, `2690-2693`, `1997`.
- `10.1103/PhysRevE.60.2721`: Crooks, Gavin E., Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences, Physical Review E `60`, `2721-2726`, `1999`.
- `10.1088/0034-4885/75/12/126001`: Seifert, Udo, Stochastic thermodynamics, fluctuation theorems and molecular machines, Reports on Progress in Physics `75`, `126001`, `2012`.

No other DOI is introduced by the diff.

## Findings

### BLOCKING

None.

### HIGH

None.

### MEDIUM

1. The parent's continuous best reply is `0.6` at every angle with `P_D>0`. Interior Nash is the child best-responding to a return the formula fixed before the child moved. The child's angle changes the grid return only inside the three-angle tie corner at the pointer, and it changes the leader's return where commitment moves the child (`0.60` versus `0.70`, parent-cost gap `0.001375`). The coupling the introduction describes is that corner and that commitment.

2. On every equator Nash the rationalizing set is the grid sample of `[0, 1-(w/κ_c) r^2]`. The reported midpoints `0.320000`, `0.140000`, and `0.410000` are half of `0.64`, `0.28`, and `0.82`. Those edges are the equator-end formula in the T77 memo and the quotient T78 already printed. The memo reports them as the grid's sets. The `κ_c` movement from `0.32` to `0.41` is the normalized stake going from `1` to `1/2` inside that formula. The cycle, the Stackelberg gap, and the entropy-production miss are the parts that go past this identity. The pin's width `1.65×10^{-4}` is the restoration identity at one interior angle, which the memo states.

3. `PREREG_3.md:71-77` locks two boundary terms. The equation and the code use `H(p_n)-H(p_0)`. The sentence names a fixed reference `p_0` on both ends. The run log says no deviation. The file was not edited after `9c004d7`, so there was no silent change of the lock. The scored functional is a legitimate path KL, forward against the reverse started at the final marginal, and P5 still misses if the other boundary is substituted. The paragraph should say which boundary was scored.

### LOW

1. Line pointers. Swarm alignment is `theory/SWARM_RULE_2026-11-23.md:47`. Line `46` is the tamper sentence. Fractal `:76-78` is the section heading and the metaphor status line. The T78 base-selector sentence is memo line `11`, just above the cited `:13-17`. The other pointers checked in attack (e) match.

2. `P4 FAIL bad=119` counts `72` headline rows plus `48` scale rows, minus the one pin. Twelve of the scale rows are the repeated `(κ_c, κ_p, κ_{D,p})=(1,1,1)` cells. The lock says that triple is one cell, not a second weight. The unique headline-plus-scale count is `108` rows, `107` of them unpinned. P4 misses either way.

3. The P1 fail text in `PREREG.md:213` includes `q_hat` values under the two tie rules that differ by more than `0.02`. `bicausal_checks.py` marks a cell bad when that cell's own summary is unpinned, and it never compares the two tie rules. On this grid the only pin's partner is already unpinned, so `FAILS 5` does not depend on the missing comparison.

4. `F-copy`, `F-bulk`, and `H-iface` are the linear identity and one unused factor printed twice. The memo says the bulk match is not extra evidence. The `REPRODUCED` label is the lock's word for an untuned match to that identity.

5. Steady `σ` on `35` of `37` child Nash pairs is below `10^{-3}`, and the minimum cell has `π_U=0.999998`. The memo names the reset. The clause "entropy production does not order `q`" is true for this chain, and the chain's range is the `ε_0` leak plus one interior point.

6. The three path starts pick one minimizing cell. The memo's sentence that the answer depends on the start describes a path-versus-steady split on which the three starts agree. Clause 6 of the lock still fails, because that cell differs from the steady minimum.

Blockers remaining: 0
