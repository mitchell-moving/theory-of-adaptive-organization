# PREREG: composite ruin-capped contest (two records, later-chosen local readouts)

*Tuesday 24 November 2026. Written and committed before any result-producing script for this contest is committed or run. This file is not edited after that commit. Any deviation is logged in `theory/COMPOSITE_CONTEST_2026-11-24.md` or in `theory/composite_contest_checks/DEVIATIONS.md`, not by rewriting this file.*

*Base: `upstream/main` = fork `main` = `0f3791890078161a1172277162df5ac13ebbff46`. Read-only input, not a parent of this branch: `upstream/ace-probe-memos-2026-11-23` at `e3e0e70116fc9cabce11af7e1c25d93d18405b0b`, folder `theory/probes-2026-11-23/`. Reviews there take precedence over the memos. Mirror memo filename: `MIRROR_MEMO.md`. Nothing here is merged from that branch.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Labels used later in the memo, and already here for the proofs below: **PROVED (in-model)**, **KNOWN**, **CONJECTURE**, **ELEMENTARY**.

## 0. Question

On one locked composite task, with one locked price, does a complex two-qubit record beat real-number quantum theory, a classical hidden-variable record, a generalized probabilistic theory whose parts do not combine by local tomography, and the two controls R4a and R4c from the mirror review?

This is the composite step the single-system duel could not take. That duel, and its review, are the reason the task is shaped as it is (`theory/probes-2026-11-23/reviews/DUEL_REVIEW.md` §0 and §6; `theory/probes-2026-11-23/duel/DUEL_MEMO.md` §0). One generator on one system uses only a (2N−1)-dimensional section, and a blurred classical rotor matches every readout law on that section, so a one-system contest is capped at a tie. Müller and Masanes (New J. Phys. 15:053040, 2013, doi 10.1088/1367-2630/15/5/053040) already show that single-system direction postulates give a ball in every dimension, and that local tomography together with a continuous reversible interaction between two bits is what forces three dimensions and qubit theory. The walls review states the same gate (`theory/probes-2026-11-23/reviews/WALLS_REVIEW.md` §4–§5). The mirror review's proposed next simulation does not select complex structure at the level of one whole; it asks that R4a and R4c be controls inside this contest (`theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md` §4; `theory/probes-2026-11-23/MIRROR_MEMO.md` §9).

This prereg does not claim to derive quantum theory. A win, a tie, or a loss is a result about this task and this price.

## 1. Why the price is the operational dimension

Two prices were considered before any run. Only one of them can produce a complex-quantum win. The other is reported, and is predicted to tie.

**Information price, rejected as the primary price.** `CORE.md:52` fixes the memory coordinate as mutual information. The task draws the readout settings only after the record is fixed, and draws them independently of the record (section 2). For every contestant, that mutual information is identically zero (Lemma I0). Any price that charges only this coordinate is blind: every contestant who hits loss 0 pays the same, and the real simulation R4c hits loss 0 (Lemma R4c). The contest would be capped at a tie before it started. That is the failure mode the duel review named (`DUEL_REVIEW.md` §6.4). So the information coordinate is not the primary price. It is still computed and reported for every contestant, and it is the secondary score in section 6.

**Orbit dimension, rejected as the primary price.** A protocol that prepares one state and holds it has orbit dimension 1, whether the state is the singlet or a cheaper imitation. Charging only that dimension is also blind among the contestants who hit loss 0.

**Primary price, locked.** Charge λ per nat of the theory's own composite operational dimension K_AB (Hardy's count: the dimension of the real vector space of unnormalized states). This is the record-size price used in the walls memo and in the duel, applied to the composite the theory actually has. Local tomography is not imposed from outside. If a theory satisfies it, K_AB = K_A K_B falls out. If it does not, the extra coordinates are priced. No contestant may replace K_AB by the dimension of one protocol's orbit.

Nonnegative prices are the further assumption A8 in the same `CORE.md:52` paragraph. The heat floor (`CORE.md:70`) is not in the primary sum: every contestant here is scored on a one-shot closed preparation, not on a steady learning rate. The T68 clock term prices repeated looks at a drifting phase; this contest is one preparation and one later readout, so that term is not charged.

## 2. Task

Two wings, one composite record, then separation. After separation the referee draws a setting pair and each wing answers locally. No message between the wings at readout.

**Menu.** Both wings are asked a direction from the same list of five unit vectors:

1. `z = (0, 0, 1)`
2. `x = (1, 0, 0)`
3. `y = (0, 1, 0)`
4. `p = (1/√2, 0, 1/√2)`
5. `m = (−1/√2, 0, 1/√2)`

Settings on the two wings are drawn independently and uniformly. Outcomes are ±1. Write `C_ab` for the expected product of the two outcomes when the wings are asked menu vectors `u_a` and `u_b`.

**Target correlator.** `T_ab = − u_a · u_b`. This is the unique correlator that is linear in each direction, rotationally a scalar, and perfectly anti-correlated on equal directions (`T = −1` on the diagonal). It is fixed here by that symmetry, and Lemma C then shows that the two-qubit singlet meets it. The target is not "whatever a fit returns."

**Loss (the stake, weight 1).**

`L = (1/25) Σ_{a,b=1}^{5} (C_ab − T_ab)^2 = (1/25) Σ_{a,b} (C_ab + u_a · u_b)^2`.

**Ruin cap.** The record is feasible if and only if `L ≤ ε`. Otherwise its cost is infinite.

**Preparation rule, the same for every contestant.**

1. Start from a product state: each wing is prepared on its own. Local mixedness is allowed. Shared randomness that is already correlated across the wings is not a product state and is not granted at the start.
2. Apply one continuous one-parameter family of reversible automorphisms of that theory's state space (the interaction). The rate is the parameter along the family. The generator may be any element of that theory's allowed algebra, as defined per contestant in section 4.
3. Local offsets: each wing may apply a reversible local map from that theory before the readout, and may flip outcome signs.
4. Local readouts only. A joint effect may exist in the theory (it counts toward K_AB) but this task does not call it.

Shared randomness created by the interaction from local mixedness is allowed, because it is step 2, not a correlated start. Section 4 records which behaviors that produces for each theory.

**CHSH sub-block used in the proofs.** Alice's settings `z, x` and Bob's settings `p, m`. The signed sum is `S = C_zp + C_zm + C_xp − C_xm`. The target value is `−2√2` (Lemma CHSH).

## 3. Composite pricing rule (locked)

`J = λ ln K_AB + L` when the record is feasible and `K_AB` is finite, and `J = ∞` otherwise. `ln` is the natural logarithm. `λ` is in nats of operational dimension. The stake weight on `L` is 1.

`K_AB` is the Hardy dimension of that contestant's composite state space, the numbers in section 4, not a number fitted after the run. Holistic coordinates that some effect of the theory can see are included. Coordinates that no effect can see are not a dimension.

**Sensitivity, not the criterion.** `J` with `K_AB` replaced by the orbit dimension of the single prepared state is computed and stored, and is not used for the headline label. Under that replacement the information price and the orbit price are both predicted to be blind on the loss-0 contestants (section 7, P6 and P7).

**Secondary score, not the criterion.** `J_I = λ I_A6 + L`, with `I_A6` from Lemma I0. Predicted to be blind (P6).

## 4. Contestants

Same preparation rule, same loss, same cap, same rate and offset freedom. The freedoms differ only by what each theory's state space and reversible group actually are.

Operational dimensions below are ELEMENTARY counts of real parameters.

| Id | Theory | K_AB | Local tomography |
|---|---|---|---|
| C | Complex quantum, two qubits | 16 | yes, 4×4 = 16 |
| R | Real quantum, two rebits | 10 | no, 3×3 = 9, and 10 > 9 |
| H | Classical local hidden-variable record | M of the model chosen in §5 | yes (a simplex) |
| G | Complex quantum plus one holistic coordinate | 17 | no, 17 > 16 |
| R4a | Classical phase-space record with a velocity-flip mirror | same models as H | yes (a simplex) |
| R4c | Real quantum on the doubled space R^8 | 36 | not the complex product 16 |
| Gmin | Minimal tensor product of two Bloch balls | 16 | yes |
| Gmax | Maximal tensor product of two Bloch balls, local reversibles only | 16 | yes |

**C. Complex two-qubit theory.** States are 4×4 density matrices. Unnormalized Hermitian matrices have 16 real parameters, so `K_AB = 16`. A one-qubit factor has `K_A = 4`. Reversible group: unitaries. Local readouts: two-outcome measurements `u·σ`. Number of perfectly distinguishable states of the composite: 4.

**R. Real two-rebit theory.** Each factor is a real Hilbert space of dimension 2. Composite real dimension 4. States are real symmetric density matrices: `K_AB = 4·5/2 = 10`. Each factor has `K_A = 3`, and `3·3 = 9 < 10`, so local tomography fails. The extra coordinate is visible to a joint real observable and not to product observables. Local observables on one rebit are the real symmetric matrices, spanned by `I, X, Z`. There is no local `Y`. Reversible group: real orthogonal matrices. Every pure product vector can be sent to every pure real vector, because `O(4)` acts transitively on the sphere. The loss is convex in the state and linear in the correlators, so a minimum is attained at a pure state, and every pure state is reachable under the preparation rule. Number of perfectly distinguishable states: 4.

**H. Classical hidden-variable record.** Finite ontic set, reversible group the permutations of the joint ontic set (a finite phase space, permuted). A product distribution on a column, sent by one permutation onto a diagonal, is a shared random variable of any finite cardinality and any weights (section 2). Responses are arbitrary functions of the local ontic point and the later setting. The achievable behaviors are exactly the local hidden-variable behaviors. `K_AB = M`, the number of ontic atoms with positive weight in the model the rule in section 5 selects. `K_hv = M` for this contestant. A model with infinitely many ontic states is not given a finite price.

**G. Holistic composite.** States are pairs `(ρ, η)` with `ρ` a two-qubit density matrix and `η ∈ [−1, 1]`. The real vector space has dimension `16 + 1 = 17`. Every product effect ignores `η`. One joint effect, not a product effect, has probability `(1+η)/2`. States that differ only in `η` are therefore operationally distinct, and they are not distinguished by local readouts, so local tomography fails. Reversible group: unitaries on `ρ`, with `η` held fixed. Starting from a product and from `η = 0`, the interaction can reach the singlet at `η = 0`. Local correlators can match C. The joint effect is never called by the task. `K_AB = 17`.

**R4a. Velocity-flip control.** The mirror review's R4a is a classical phase-space composition whose time mirror flips the momentum and is not a positive form. Any finite classical model in H embeds in a finite phase space with permutation dynamics, so R4a realizes the same behaviors as H and is priced the same way. The control that is not the tracking score is Lemma W: on a two-point momentum, the odd function `f(p) = p` has mirror form `−1`. The code records that value. It does not enter `J`.

**R4c. Doubled real space.** The real-linear image of two-qubit quantum theory on `R^8`, as in Lemma R4c. This is the control the mirror review names: a real symmetric block matrix built from the real and imaginary parts of a complex Hamiltonian reproduces the complex probabilities, with a real-linear mirror. Unrestricted real states on `R^8` are the theory, so `K_AB = 8·9/2 = 36`. Restricting by hand to the complex-linear subspace is contestant C, not a second contestant. Local readouts are the real subspace projections that Lemma R4c shows match the complex Born rule. Number of perfectly distinguishable states of the real space: 8.

**Gmin.** States: convex hull of product two-qubit states, inside the tensor-product space, so the linear span has `K_AB = 16` (product operators `σ_i ⊗ σ_j` span the Hermitian matrices) and local tomography holds. Reversible group used here: local unitaries `SU(2)×SU(2)` and the swap. A product state stays a product. Correlators from a pure product have the form `f(u) g(v)`.

**Gmax.** State space: the maximal tensor product of two Bloch balls (every functional that is positive on product effects), which sits in the same 16-dimensional tensor-product space, so `K_AB = 16` and local tomography holds. The reversible group granted to this contestant is only the local rotation group `SO(3)×SO(3)` and the swap, both of which are automorphisms and send product states to product states. No other interaction is granted. Correlators reachable from a product therefore have the form `f(u) g(v)`, the same bound as Gmin. This contestant is that named group, not an unnamed larger automorphism group. Boxworld is not a separate row: its reversible dynamics are trivial (Gross, Müller, Colbeck, and Dahlsten, Phys. Rev. Lett. 104:080402, 2010, doi 10.1103/PhysRevLett.104.080402), so an interaction from a product only relabels locally and the correlator is again a product, already bounded by Lemma P.

## 5. Classical search (locked algorithm)

H and R4a use the same search. It returns a curve of `(M, L_M)`. At each cell the contestant takes the pair on that curve with `L_M ≤ ε` that minimizes `λ ln M + L_M`. If none is feasible, the contestant is infeasible.

Deterministic. No seed. Vertex order: a response is an integer in `0 .. 31`, bit `i` set means outcome `−1` on menu item `i`, bit clear means `+1`. A joint vertex is a pair `(α, β)` in lexicographic order, 1024 vertices. The correlator of a vertex is the rank-1 sign matrix `C_ab = ξ_α(a) ξ_β(b)`.

1. **M = 1, exact.** Minimize `L` over the 1024 vertices.
2. **M = 2, exact.** For every unordered pair of distinct vertices, the mixture `(1−t) C + t C'` has loss quadratic in `t`. Minimize the quadratic on `[0, 1]` in closed form.
3. **Frank–Wolfe.** Start at the uniform distribution on the 1024 vertices. For `k = 0 .. 7999`, step length `2/(k+2)`. The linear oracle scans every vertex and takes the lowest index on a tie. No away step.
4. **Support.** Atoms with weight `> 10^{−10}` after step 3. Reoptimize the weights on that support by projected gradient, 4000 iterations, exact line search along the feasible direction, tie-break toward the lowest index when a projection hits a face.
5. **Backward elimination.** While more than one atom remains, drop the atom whose removal, after a fresh 4000-iteration reoptimization, gives the smallest loss. Ties: drop the lowest index. Record `(M, L)` at each size. The curve used for the price is the lower envelope of steps 1, 2, and 5.

`L` on this curve for `M ≥ 3` is the loss of this search, which is an upper bound on the true minimum loss at that cardinality. A cell in which C loses to this H is a loss against a concrete model. A cell in which C beats this H is a win against this search, not a proof that no cheaper classical model exists. The cells in which H is infeasible do not depend on the search: Lemma B already forbids every local hidden-variable model from reaching loss 0, and it forbids every such model from meeting `ε ≤ 10^{−3}`.

## 6. Decision rule

Per cell, C against one competitor X:

- C feasible and X infeasible: C wins.
- C infeasible and X feasible: C loses.
- Both infeasible: the pair is excluded.
- Both feasible: `Δ = J_X − J_C`. C wins if `Δ > tol`, loses if `Δ < −tol`, ties otherwise, with `tol = 0.01 · max(J_C, J_X) + 10^{−12}`.

The cell outcome against the full set `{R, H, G, R4a, R4c, Gmin, Gmax}`: **WIN** if C wins against every non-excluded competitor, **LOSE** if C loses against any, otherwise **TIE**.

**Headline slice.** `ε = 0` and `λ ∈ {10^{−4}, 10^{−3}, 10^{−2}, 10^{−1}}`. The selection statement survives in the reviewer's sense if and only if every cell in this slice is WIN. This is the locked criterion.

**Full `λ > 0` aggregate,** reported, not the headline. Over the 24 cells with `λ > 0`: **WIN** if at least 90% are WIN and none is LOSE; **LOSE** if at least 50% are LOSE; **TIE** if at least 90% are TIE; otherwise **MIXED**.

**`λ = 0` cells,** reported separately, six of them, one per `ε`.

**Grid, locked.** `λ ∈ {0, 10^{−4}, 10^{−3}, 10^{−2}, 10^{−1}}`, `ε ∈ {0, 10^{−3}, 10^{−2}, 0.05, 0.2, 1}`. Thirty cells. The positive `ε` values sit on either side of the two analytic floors `10^{−3} < (3−2√2)/25 < 10^{−2} < 1/25 = 0.04 < 0.05`. They were chosen from those floors, not from a run.

**Secondary labels.** The same rule on `J_I`, stored as `pinfo`. The same rule on the orbit-dimension price, stored as `orbit`. Neither is the headline.

## 7. Proof that a complex-quantum win is possible

The headline slice is in fact a win by the lemmas in section 8, before any search is run. The code's job on that slice is to check the lemmas. The open part of the grid is the cells with `λ > 0` and `ε ≥ 10^{−2}`, where a cheaper contestant whose loss is only moderately worse can undercut `λ ln K`.

**Lemma C (C hits loss 0).** PROVED (in-model). Let `|s⟩ = (|01⟩ − |10⟩)/√2`. Let `A = |01⟩⟨10| − |10⟩⟨01|`, real and antisymmetric. Then `exp(θ A)|01⟩ = cos θ |01⟩ − sin θ |10⟩`, so `θ = π/4` is the singlet, reached from the product vector `|01⟩`. The Hamiltonian `H = i A` is Hermitian and `exp(−i θ H) = exp(θ A)`, so this is an allowed unitary rate for C. The singlet is the antisymmetric vector: `(U ⊗ U)|s⟩ = det(U) |s⟩` for `U ∈ SU(2)`, because `U ⊗ U` multiplies the Levi-Civita symbol by `det U`. Conjugating both factors therefore leaves every correlator fixed, while the adjoint action of `SU(2)` on the Paulis is all of `SO(3)`. The correlation matrix is `SO(3)`-invariant, hence a multiple of `δ_ij`. The multiple is `⟨ZZ⟩ = −1`, because `Z⊗Z` has eigenvalue `−1` on both `|01⟩` and `|10⟩`. Therefore `⟨(u·σ) ⊗ (v·σ)⟩ = −u·v` for every pair of directions, and `L = 0`. Offsets may be the identity. The rate `θ = π/4` is allowed. `J_C = λ ln 16` at `ε = 0`.

**Lemma CHSH.** ELEMENTARY. For the target, `z·p = z·m = x·p = 1/√2` and `x·m = −1/√2`, so the four target correlators are `−1/√2, −1/√2, −1/√2, +1/√2` and `S = −2√2`. For any deterministic ±1 responses, `S = a_z (b_p + b_m) + a_x (b_p − b_m)`. The two parentheses are `{0, ±2}` in either order, so `|S| ≤ 2`. A mixture stays inside `[−2, 2]`. Since `√2 > 1`, `|S| = 2√2 > 2`. No local hidden-variable behavior matches the target on these four entries.

**Lemma B (classical floor).** ELEMENTARY, given Lemma CHSH. Let `δ` be the vector of the four sub-block errors and `η = (1, 1, 1, −1)`. Then `|η·δ| ≥ 2√2 − 2` and `‖η‖^2 = 4`, so the sum of those four squared errors is at least `(2√2 − 2)^2 / 4 = (√2 − 1)^2 = 3 − 2√2`. The other twenty-one squares are nonnegative, so `L ≥ (3 − 2√2)/25`. Now `√2 < 99/70` because `(99/70)^2 = 9801/4900 > 2`. Then `2√2 < 198/70 = 99/35`, and `3 − 2√2 > 3 − 99/35 = (105 − 99)/35 = 6/35`. Hence `L > (6/35)/25 = 6/875`. And `6/875 > 1/1000` because `6000 > 875`. So every local hidden-variable model, including every model the section 5 search can return, and including R4a, has `L > 10^{−3}`. At `ε ∈ {0, 10^{−3}}` both H and R4a are infeasible. C is feasible. C wins those pairs.

**Lemma R (rebit floor).** PROVED (in-model). On the three settings `x, y, z`, each local rebit effect has its Bloch vector in a fixed 2-plane. The 3×3 correlator block is `R_⊤ G S` with `R` and `S` of size 2×3, so its rank is at most 2. Let `A` be that block and `T = −I_3`. Some unit `q` has `A q = 0`. Then `‖T − A‖_F^2 ≥ ‖(T − A) q‖^2 = ‖q‖^2 = 1`. Those nine squared errors sum to at least 1, so `L ≥ 1/25 = 0.04`. At `ε ∈ {0, 10^{−3}, 10^{−2}}`, R is infeasible. C wins those pairs. The same rank bound is why a planar Bell test would not have separated R from C: `x, z, p, m` all lie in the `xz` plane, and the singlet is a real vector. The menu contains `y` for that reason.

**Lemma P (product floor).** ELEMENTARY. A pure product, and any local rotation or swap of one, has `C_ab = f(a) g(b)`. The 2×2 block on settings `z, x` has rank at most 1, so it has a unit kernel vector `q`, and the same estimate gives sum of four squared errors at least 1 against `−I_2`. Thus `L ≥ 1/25`. Gmin and Gmax are infeasible at `ε ≤ 10^{−2}`. C wins those pairs. Convexity of `L` puts the minimum at an extreme point, so mixed separable states do not beat the pure-product floor.

**Lemma R4c (the real simulation hits loss 0 at K = 36).** PROVED (in-model). Write a complex vector `ψ ∈ C^4` as the real vector `ψ_R = (Re ψ, Im ψ) ∈ R^8`. Let `J(Re, Im) = (−Im, Re)`, real-linear multiplication by `i`. For a complex unit vector `φ`, `⟨φ_R | ψ_R⟩ = Re ⟨φ|ψ⟩` and `⟨φ_R | J ψ_R⟩ = −Im ⟨φ|ψ⟩`, so the squared length of the projection of `ψ_R` onto the real plane spanned by `φ_R` and `J φ_R` equals `|⟨φ|ψ⟩|^2`. A local complex Pauli measurement has a +1 eigenspace that is a complex line on that wing (a real 4-plane in `R^8` once Bob's factor is included). Its Born probability is that squared length. All product-Pauli probabilities of the singlet are therefore reproduced by one real pure state on `R^8` and by real subspace projections, which are allowed readouts for R4c. Hence `L = 0`. The orthogonal path is the real image of the unitary path in Lemma C, so the preparation rule is met. `K_AB = 36` because every real symmetric 8×8 matrix is a state of this theory, not because the singlet's orbit is 36-dimensional. `J = λ ln 36` at loss 0.

**Lemma G (holistic composite hits loss 0 at K = 17).** PROVED (in-model), from Lemma C. Prepare the singlet at `η = 0`. Local effects ignore `η`, so the local correlators match C and `L = 0`. `K_AB = 17`.

**Lemma Tol (the gaps clear the 1% tie band).** ELEMENTARY. For a feasible loss-0 competitor with dimension `K > 16`, `Δ = λ ln(K/16)` and `tol = 0.01 λ ln K + 10^{−12}`. It is enough that `ln(K/16) > 0.01 ln K` and that the slack absorbs `10^{−12}` on this grid.

For G, `K = 17`. `ln(17/16) = ln(1 + 1/16)`. The alternating series gives `ln(1+x) > x − x^2/2` for `x = 1/16`, since the terms decrease and the first omitted term is positive. So `ln(17/16) > 1/16 − 1/512 = 31/512`. Also `ln 2 < 7/10`, so `ln 17 = 4 ln 2 + ln(17/16) < 14/5 + 1/16 = 229/80`, and `0.01 ln 17 < 229/8000`. Then `31/512 − 229/8000 = 2043/64000 > 3/100`. For every grid `λ ≥ 10^{−4}`, the slack `λ · 2043/64000` is greater than `2 · 10^{−6}`, which is greater than `10^{−12}`. So `Δ > tol`. C beats G on every cell where both are feasible and `λ > 0`, including the whole headline slice.

For R4c, `K = 36`, `ln(36/16) = ln(9/4) = 2 ln(3/2)`. The exponential series through order 4 at `2/5` sums to `2797/1875`. The remainder is smaller than `(2/5)^5 / 120` times `1/(1 − (2/5)/6) = 15/14`, which equals `2/21875`. Adding these fractions gives `97901/65625 < 3/2`, because `3 · 65625 − 2 · 97901 = 1073 > 0`. Hence `e^{2/5} < 3/2`, `ln(3/2) > 2/5`, and `ln(36/16) > 4/5`. Also `ln 2 < 7/10`, so `ln 36 < 5 · (7/10) + 1/8 = 29/8` (using `9/8 = 1 + 1/8` and `ln(1+y) < y`), and `0.01 · 29/8 = 29/800 < 4/5` because `29 · 5 = 145 < 800 · 4 = 3200`. The slack at `λ ≥ 10^{−4}` is far above `10^{−12}`. C beats R4c whenever both are feasible and `λ > 0`.

**Theorem W (headline).** PROVED (in-model), from the lemmas above. On every headline cell, C is feasible with finite `J`. R, H, R4a, Gmin, and Gmax are infeasible, so C wins those pairs. G and R4c are feasible and C beats them by Lemma Tol. No pair is a loss and no pair is a tie. Every headline cell is WIN. A complex-quantum win is not only possible: the locked criterion holds by this proof. A bug in the code can fail a check. It cannot change this argument. If a check fails, the memo logs it as a deviation and the criterion is not claimed on the code's authority.

## 8. Lemmas the code must check

The scripts recompute the following and stop on a mismatch. These are checks of section 7, not new measurements.

- L1. Singlet correlators against `−u·v` on the 25 menu pairs, maximum absolute error `≤ 10^{−12}`, and target `S = −2√2` within `10^{−12}`.
- L2. A deterministic ±1 assignment has `|S| ≤ 2`. A sample of mixtures stays inside `[−2, 2]`.
- L3. The four-entry classical floor: any behavior with `|S| ≤ 2` has sum of those four squared errors at least `3 − 2√2 − 10^{−12}`.
- L4. A rebit correlator block on `x, y, z`, built from a pure real state and planar effects, has Frobenius distance at least `1 − 10^{−9}` from `−I_3`.
- L5. A product correlator `f(u)g(v)` has 2×2 `z, x` block at distance at least `1 − 10^{−9}` from `−I_2`.
- L6. R4c's real projection probabilities match the complex Born rule on the singlet for every product Pauli pair in the menu, error `≤ 10^{−12}`, and the two wings' outcome statistics do not depend on the other wing's setting (no signaling), error `≤ 10^{−12}`.
- L7. Lemma W prints `−1` exactly for the two-point momentum.
- L8. `31/512 > 229/8000` and the headline gaps are positive after subtracting `tol`.

## 9. What is computed, not proved

For each contestant the code stores `K_AB`, `K_hv`, `I_A6`, `I_wings`, `I_out`, `L`, feasibility, and `J`.

- `I_A6 = I((U,V); record)`. Predicted 0 for every contestant (Lemma I0): the settings are drawn independently after the record is fixed.
- `I_wings`: for a quantum state, `S(ρ_A) + S(ρ_B) − S(ρ_AB)` in nats; for a classical model, the Shannon mutual information of the joint ontic distribution across the two wings. For the singlet this is `2 ln 2`. Reported, not priced.
- `I_out`: the average over the 25 setting pairs of the Shannon mutual information of the two ±1 outcomes. Reported, not priced.
- `K_hv`: for H and R4a, the `M` they use. For a product behavior, 1. For any behavior whose CHSH sub-block has `|S| > 2`, `∞` (no local hidden-variable model).

The searches: section 5 for H and R4a; a seesaw for R; a seesaw for Gmin and Gmax.

**Rebit seesaw, locked.** Alternate (i) exact minimization of each wing's Bloch vector inside the unit disk of the `xz` plane, the other wing and the state held fixed (a 2×2 trust-region problem, closed form), and (ii) projected gradient on a Cholesky factor of a real 4×4 density matrix, 2000 iterations, exact line search. Forty rounds, or stop when `L` improves by less than `10^{−15}`. Five deterministic starts: the real singlet with each menu direction replaced by its normalized `(x, z)` projection (the `y` direction uses angle 0); the singlet with all angles 0; the singlet with all angles `π/2`; the product `|00⟩` with projected angles; the real vector `(|00⟩ + |11⟩)/√2` with projected angles. Take the best `L`. Lemma R already makes R infeasible for `ε ≤ 10^{−2}` whatever this search returns. On looser caps the returned `L` is an upper bound on R's true minimum.

**Product seesaw, locked.** `C_ab = f_a g_b` with values in `[−1, 1]`. Alternate exact one-dimensional clippings, 200 rounds, from two starts: the top singular vector of `T`, and the constant vector `1`. Take the best `L`. Lemma P is the floor regardless.

## 10. Predictions

Written before the run. P1–P7 are consequences of section 7 and Lemma I0. P8 is the open part of the grid. A miss on P8 is a result, not a license to edit P1–P7.

- **P1.** Every headline cell (`ε = 0`, `λ > 0`) is WIN.
- **P2.** H and R4a are infeasible at `ε ∈ {0, 10^{−3}}`, for every `λ`.
- **P3.** R, Gmin, and Gmax are infeasible at `ε ∈ {0, 10^{−3}, 10^{−2}}`, for every `λ`.
- **P4.** For every `λ > 0` and every `ε`, C beats R4c and C beats G whenever the pair is scored (both feasible).
- **P5.** Every `λ = 0` cell is TIE. At `λ = 0`, `J = L` up to the cap. R4c and G match `L = 0`, so they tie C, and a single tie makes the cell a TIE. C does not lose a `λ = 0` cell.
- **P6.** `I_A6 = 0` for every contestant. The secondary score `J_I` therefore ties C with R4c and with G on every cell. Under the CORE memory coordinate the headline slice is TIE, not WIN. The dimension price is what the headline uses, for the reason in section 1.
- **P7.** The orbit-dimension price also ties C with R4c and with G on every cell, because each of those protocols prepares one state.
- **P8.** No label is locked for the cells with `λ > 0` and `ε ≥ 10^{−2}`, nor for the 24-cell `λ > 0` aggregate. Those cells are the measurement. If they come back WIN, the cap did not have to be tight. If they come back MIXED or LOSE, the selection on this task is confined to caps below the cheaper contestants' error, and the memo records that scope.

## 11. Prior art

The separations used as lemmas are known. This contest puts a locked cost on them. It does not replace a reconstruction theorem.

Verified on `https://api.crossref.org/works/<doi>` before this commit:

- Müller and Masanes 2013, New J. Phys. 15:053040, doi 10.1088/1367-2630/15/5/053040. Single-system balls of every dimension; interaction plus local tomography forces the qubit.
- Masanes and Müller 2011, New J. Phys. 13:063001, doi 10.1088/1367-2630/13/6/063001.
- Chiribella, D'Ariano, and Perinotti 2011, Phys. Rev. A 84:012311, doi 10.1103/PhysRevA.84.012311.
- Hardy and Wootters, Foundations of Physics, doi 10.1007/s10701-011-9616-6 (Crossref issued year 2011). Real-vector-space quantum theory and the failure of local tomography.
- Barnum and Wilce 2014, Foundations of Physics, doi 10.1007/s10701-014-9777-1. Local tomography and the Jordan structure.
- McKague, Mosca, and Gisin 2009, Phys. Rev. Lett. 102:020505, doi 10.1103/PhysRevLett.102.020505. Real Hilbert-space simulation of complex quantum theory.
- Aleksandrova, Borish, and Wootters 2013, Phys. Rev. A 87:052106, doi 10.1103/PhysRevA.87.052106. A universal real quantum bit.
- Wootters, Foundations of Physics 42:19–28, doi 10.1007/s10701-010-9488-1 (Crossref issued 2010).
- Renou, Trillo, Weilenmann, Le, et al. 2021, Nature, doi 10.1038/s41586-021-04160-4. A network experiment that real quantum theory cannot match. This contest is not that network. It is one composite and a later local menu.
- Barrett 2007, Phys. Rev. A 75:032304, doi 10.1103/PhysRevA.75.032304. Tensor products of generalized probabilistic theories.
- Gross, Müller, Colbeck, and Dahlsten 2010, Phys. Rev. Lett. 104:080402, doi 10.1103/PhysRevLett.104.080402.
- Cirel'son 1980, Lett. Math. Phys. 4:93, doi 10.1007/BF00417500. The quantum bound. Lemma C computes the value on this menu directly and does not invoke the general bound.
- Popescu and Rohrlich 1994, Foundations of Physics, doi 10.1007/BF02058098.
- Hardy 2004, Stud. Hist. Phil. Mod. Phys., doi 10.1016/j.shpsb.2003.12.001. Ontological excess.
- Montina 2008, Phys. Rev. A 77:022104, doi 10.1103/PhysRevA.77.022104.

Hardy 2001 (`quant-ph/0101012`) has no Crossref DOI. It is not cited as a verified reference. The dimension counts used here are recomputed in section 4. The probe memos quote that paper's axioms; this prereg does not.

## 12. Analysis plan

After this commit, and not before, add `theory/composite_contest_checks/` and run it.

- `lemmas.py` checks L1–L8 and writes `lemmas.out`.
- `search.py` runs the classical search, the rebit seesaw, and the product seesaw, and writes `search_results.json`.
- `decide.py` applies section 6 and writes `decisions.out` and `grid_results.json`.
- `crossref_check.py` rechecks every DOI in section 11 and writes `crossref.out`.
- `SHA256SUMS` covers the scripts and the outputs.
- A test in `tools/` reruns the checks and compares the stored outputs byte for byte.
- `theory/COMPOSITE_CONTEST_2026-11-24.md` reports the cells, with file and line references, and labels every model reading as a model implication. `OPEN_WORK.md` gains one row. `theory/README.md` gains one index row.

No script may tune `ε`, `λ`, `tol`, the menu, or `K_AB` after seeing a label. If a script is wrong relative to this file, fix the script or log a deviation. Do not edit this file.

Outputs use a fixed byte format: UTF-8, newline `\n`, no timestamps, JSON with sorted keys, floats written so that a second run on this interpreter matches byte for byte. `PYTHONHASHSEED=0` and one thread for any library that would otherwise parallelize.

## 13. Headline in one paragraph

The task asks two wings for a later local direction from a five-point menu and scores the correlator against `−u·v`, under a ruin cap on that squared error, at a price `λ ln K_AB`. Complex two-qubit theory meets the target at `K_AB = 16` by a unitary path from a product state to the singlet. Rebits, classical hidden-variable records, the velocity-flip control, and both tensor products miss it by an amount proved above, so a tight cap makes them infeasible. The real doubling meets it at `K_AB = 36`, and one holistic coordinate meets it at `K_AB = 17`; both lose to the dimension price by more than the tie tolerance as soon as `λ > 0`. The mutual-information coordinate is zero for every contestant, because the settings are chosen after the record, and under that coordinate the same cells tie. That split is the prediction. The loose-cap cells are not predicted.
