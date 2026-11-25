# LEAN-PHYS plan

Written before any proof in this work order. The parent is upstream
`main` at `4f17326`. This file is not revised in place. Later notes are
appended at the bottom.

Work order: `OPEN_WORK.md:250` (row LEAN-PHYS, rank 4 of the ranked gap
plan). Formalize, with every assumption named, the general diffusion heat
step, the T60 pairwise and path bounds, and the T63 product argument.
Nothing here is a claim about a real system. `THEORY.md` and `CORE.md`
are not edited. T61 and T62 are not started. The aggregate audit digest
in `formal/lean/AUDIT.json` is not per-claim coverage; coverage is the
table below, one row per paper sentence.

Every hypothesis is a named argument or a named structure field. No
`axiom`, `sorry`, `admit`, or `native_decide`.

## Statement list

### EQ-heat, the general diffusion heat step

Source: `theory/GENERALITY_2026-11-22.md:31-68` (Proposition EQ-heat),
cited at `CORE.md:70` and as ledger row EQ-HEAT in
`measurement/CLAIM_MAP_v2.md`. New file `GTAO/DiffusionHeat.lean`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `current`, `learningRate`, `shannonRate`, `entropyProduction` | lines 39-44 and 52 | On a measure space, with joint density `p`, drift `F`, its memory derivative `dF`, the memory derivative `dp` of `p`, and the conditional score `sCond`: `J = F p - D dp`, `İ = ∫ J sCond`, `Sr = ∫ (F² + D dF) p / D`, `Σ = ∫ J² / (D p)`. |
| `EQHeatHyp` | lines 29 and 37-42 | A structure whose fields are the assumptions: `D > 0`; `p > 0`; the score split `dp/p = sCond + sMarg` (log of the joint is log conditional plus log marginal); integration by parts with vanishing boundary terms, `∫ F dp = -∫ p dF`; the marginal-entropy identity `∫ J sMarg = -dS` (continuity equation for the marginal, boundary terms vanish); integrability of `F² p`, `p dF`, `F dp`, `J sCond`, `J sMarg`. |
| `entropyProduction_nonneg` | line 52 | `Σ ≥ 0`. |
| `eq_heat_identity` | line 65 | `Σ = Sr - İ + dS`. |
| `eq_heat_steady` | lines 46 and 68 | In the steady state (`dS = 0`), `İ ≤ Sr`. |
| `eq_heat_floor` | line 46 | With the Einstein unit `kT = D`, `kT İ ≤ D Sr`. |

The two integral identities (integration by parts and the continuity
equation of the marginal) enter as hypotheses. They are not derived from
the SDE or a Fokker–Planck equation in Lean.

### T60 pairwise bound

Source: `theory/GENERAL_FLOOR_FINITE_2026-11-23.md:27` and `:115`.
New file `GTAO/FiniteFloorPairwise.lean`. Reuses `FiniteFloor.klSum`,
`Prob`, `AC`, `flux`, `iAltReal`, `iAlt`, `bayesError`, and `HeatFloor.L`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `log_sum_le` | line 113, "lumping does not raise" | Log-sum inequality on positive reals. |
| `edge_superadd` | same | `(A-B) log(A/B) ≤ Σ (a-b) log(a/b)` for positive `a, b`. |
| `overlap`, `jeffreys_ge_two_L` | line 113 | For probability vectors that are mutually absolutely continuous, `klSum p q + klSum q p ≥ 2 L(overlap/2)`, where `overlap = Σ min(p, q)`. |
| `overlap_le_bayes` | line 115, first sentence | For `i ≠ j`, `Σ_m min(π(i,m), π(j,m)) ≤ ε`. |
| `pairwise_L` | lines 27 and 115 | If `i ≠ j`, both directed fluxes are positive, `ε < min(π(i), π(j))`, and the two conditionals are mutually absolutely continuous, then `iAltReal ≥ min(j_ij, j_ji) · 2 L(ε / (2 min(π(i), π(j))))`. |
| `pairwise_L_ennreal` | same | The same bound on the extended `iAlt`, with no absolute-continuity hypothesis (a singular pair on a positive flux gives `⊤`). |
| `pairwise_telegraph` | line 27, "On the telegraph this is again `r L(ε)`" | On the fair telegraph of rate `r > 0`, for `ε < 1/2`, `iAlt ≥ r L(ε)`. Equality at the symmetric copy and the converse (`B2-telegraph`) are not targets. |

### T60 path bound

Source: `theory/GENERAL_FLOOR_FINITE_2026-11-23.md:26` and `:117-129`.
New file `GTAO/FiniteFloorPath.lean`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `binKl`, `binary_pinsker` | line 117, Pinsker in nats | `2 (a-b)² ≤ a log(a/b) + (1-a) log((1-a)/(1-b))` for `a ∈ [0,1]`, `b ∈ (0,1)`. |
| `pinsker` | same | `2 TV(p,q)² ≤ klSum p q` for probability vectors with `p ≪ q`. |
| `walkEdges`, `walkEnd`, `tv_walk_le` | line 117, triangle inequality | Total variation from the start of a walk to its end is at most the sum over its edges. |
| `bayes_le_chance`, `chance_sub_bayes_le` | lines 119-121 | `ε ≤ ε_0`, and at a mode `x*`, `ε_0 - ε ≤ Σ_x π(x) TV(p_x, p_{x*})`. |
| `PathSystem`, `pathWeight`, `pathK` | lines 123-127 | A target mode and, for each occupied state, a walk of positive-flux edges ending at the mode. `c_e² = (Σ_x π(x) · #uses of e)² / 2` and `K_X = Σ_e c_e² / j_e` over edges used. |
| `path_pinsker` | lines 26 and 127 | `(ε_0 - ε)² ≤ K_X · iAltReal` when every used edge carries a pair `p_u ≪ p_v`; `path_pinsker_ennreal` on `iAlt` without that hypothesis. |
| `pathSystem_exists` | line 117 | On a strongly connected occupied flux graph a path system to any occupied mode exists. |
| `telegraph_K` | line 129 | On the fair telegraph, `K_X = 1/(4r)`. |

### T63 product argument

Source: `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:59-65` and `:75`
(Step 3). New file `GTAO/RepairTensor.lean`. Reuses `L_ge_four_entropy`.

| Lean name | Paper | Intended statement |
|---|---|---|
| `flipAt`, `cubeSigma`, `cubeD` | lines 59-65 | On `Fin n → Bool`, `σ_Γ[p] = Σ_i Γ_i Σ_{unordered edges} (p_x - p_{x^(i)}) log(p_x/p_{x^(i)})` (written as one half of the ordered sum) and `D(p‖u) = Σ p log(p 2^n)`. |
| `cube_tensorization` | line 75 | For every strictly positive probability `p` on `{0,1}^n` and leak rates `Γ_i ≥ Γ ≥ 0`, `4 Γ D(p‖u) ≤ σ_Γ[p]`, for every `n`. |

The proof planned is an induction on `n` that splits off one carrier,
uses the chain rule for `D(p‖u)`, homogeneity of each edge term, the
edge superadditivity above for the split-off carrier, and the one-carrier
comparison `L ≥ 4 (log 2 - h)` of batch 2. This is not the entropy
subadditivity route written in the note; if the induction does not close,
the subadditivity route is the fallback. Strict positivity of `p` is a
named hypothesis: a zero atom next to a positive atom makes the paper's
`σ` infinite, and Lean's `log 0 = 0` would not give that value.

## Not targets

- T61 and T62, the decoder data-processing step (`B2-decoder`), the
  telegraph equality and converse (`B2-telegraph`), a closed form of
  `Φ_X`, the Schnakenberg integral (`B2-repair-average`), and any
  derivation from an SDE or a generator beyond the named hypotheses.

## Can it fail, and the cheapest repair

Can it fail: a stated bound is false as written, or needs a hypothesis
the paper sentence does not name.
Cheapest way: do not patch the paper sentence. Prove the version with the
extra hypothesis, label it **WEAKER**, and append a miss row below with
a signed size, a location, and an update.

Can it fail: the product induction does not typecheck.
Cheapest way: ship the pieces that do, label the product statement
absent, and append the failed goal as a miss.

Can it fail: a new `axiom`, `sorry`, or `native_decide` would fail
`scripts/AxiomAudit.lean`.
Cheapest way: no new axiom.

## Miss log

Appended after the proofs.

Lock: plan commit `07ce4e5` on `forge-lean-phys` (sha256 of this file at
lock `2573b8934b60a742ea5a6ca93b3cfe0790712d8bd7dd3d548629fd97658f7d6f`).
Logged 25 November 2026 ET. Breach check: `none`.

Every row of the statement list above has a declaration with the planned
name. Two declarations are **WEAKER**; each is a row here. Formal labels
stay in `INVENTORY.md`.

| prediction_id | locked_prediction | outcome | miss | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| LP-eqheat | `Σ = Sr − İ + dS`, and `İ ≤ Sr` in the steady state, for the SDE `dM = F dt + √(2D) dW` with vanishing boundary terms. `theory/GENERALITY_2026-11-22.md:62-68` | `eq_heat_identity`, `eq_heat_steady`, `eq_heat_floor` at `DiffusionHeat.lean:102`, `:135`, `:144`; integration by parts and the marginal-entropy identity are fields of `EQHeatHyp` | short by the derivation of those two integral identities from the SDE and its Fokker–Planck equation | model | medium | both identities named as hypotheses; the substitution, the sign of `Σ`, and the steady-state bound are checked on any measure space | none |
| LP-tensor-zero | `σ_Γ[p] ≥ 4 Γ D(p‖u)` for every distribution on `{0,1}^n`. `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:75` | `cube_tensorization` at `RepairTensor.lean:162`, every `n`, leak rates `Γ_i ≥ g ≥ 0`, strictly positive `p` | short by the zero-atom case: there the note's `σ` is `+∞` and the bound is trivial, but Lean's `log 0 = 0` does not give `+∞` | model | low | strict positivity named; the product inequality for every `n` is checked by induction on the carriers, not by the note's entropy-subadditivity route | none |

Not misses, recorded so the coverage is exact. `pairwise_L` and
`path_pinsker` on the real sum `iAltReal` take absolute continuity on the
edges they use; `pairwise_L_ennreal`, `path_pinsker_ennreal`, and
`path_pinsker_stronglyConnected` on the extended `iAlt` take none, so the
paper sentences are checked without it. `iAlt` is the flux-weighted
divergence sum, the right side of the destruction identity; passing from
the net learning rate to that sum is `stationary_learning_rate`, which
stays **WEAKER** (B2-stationary-rate). `pathWeight` counts an edge with
its multiplicity in a walk; on walks with no repeated edge, such as
shortest paths, it is `√2 c_e` of the note.
