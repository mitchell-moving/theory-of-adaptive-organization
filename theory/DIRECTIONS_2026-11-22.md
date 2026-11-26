# Directions after the classical core (22 November 2026)

*Written Saturday 21 November 2026, about 11:59 PM ET (America/New_York), from a conversation between Chad Mitchell and Ace. This is a planning note, **not a lock, not a prereg and not a result**. It adds no CLAIM_MAP row and changes no status. The hypothesis sentence is unchanged: "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." Everything below is a direction to test, not a claim.*

## 0. Order of work (agreed)

1. On main: the representation boundary and frontier form (PR #154, merged as `fb6c17f`; confirm #157 `797b14b`), the chain-to-diffusion limit for DS1 (PR #153, merged as `f84997c`; confirm #159 `37794bb`), and Lean batch 2 (PR #155, merged as `886d69b`; confirm #160 `eddf64e`). Lean is insurance on the load-bearing chain only, not a growing count.
2. Write one derivation chain in one document: axioms, then the frontier form (with additive J as the special case), then the principle, then the theorems, then the four rules (hold, estimate, watch, learn).
3. Freeze the core text and tag a snapshot release.
4. Re-read past field attempts under the frontier form (§1.3), then run one preregistered, hash-locked real-data test on a qualifying system.
5. Draft human-review requests to researchers. Chad approves and sends them; nothing goes out otherwise.
6. **Next direction A:** apply and test GTAO on AI agent systems (§2).
7. **Next direction B:** the dynamics of how systems reach the frontier (§3).
8. **Parked:** a quantum extension of the floors (§4).

## 1. The frontier form (status: hypothesis F, CLAIM_MAP V5 OPEN, PR #154 merged)

**1.1 The idea.** The additive master equation J = κI_mem + hK + wE[ℓ] + A + L is likely a special case, in the way the ideal gas law is a special case of thermodynamics. The candidate general form is price-free. A system's design yields a vector of goods it must spend or bads it must suffer: memory held, information bought, error, attention spent and ruin risk. Strongly selected systems sit on the efficient (Pareto) frontier of that vector, given the world's pattern of change. Physics and information theory (Landauer, Still, the single-letter floors) cut the feasible set. Prices only pick *which* frontier point a system lands on.

**1.2 What is known so far (first draft plus hostile review; PR #154 is merged).**
- **Additivity.** J is additive only under named axioms. PR #154's R1 needs an extra monotonicity axiom for nonnegative prices, and care with the discrete layer count (review `reviews/representation_2026-11-21/REVIEW.md`).
- **The scalarization converse.** The general form gives back the additive one when the feasible set is convex: every Pareto point then minimizes some nonnegative weighted sum. Without convexity it fails (three-point dent). Per the review, a plain coordinate cap ρ ≤ ε on ruin does **not** break convexity, so the earlier statement that it does was wrong.
- **Survives with no prices.** The antitone shape of the front; the information floors as limits on what is feasible; the layer cap only as dominance.
- **Needs a stake or a price ratio.** Monotone comparative statics (CT33, Master Theorem (ii)) need single crossing in a stake variable, so they are not fully price-free. K\*(R), the cost shares (CT24) and the selection gap d/(2β) need a ratio or a scalar cost.
- **Prior art.** Pareto efficiency and weighted-sum scalarization are standard (Debreu 1951; Farrell 1957; Geoffrion 1968). Low-dimensional trait fronts in evolution are Shoval et al. 2012. The repository's Shannon note (S2, S3) already has a price-free frontier. The GTAO-specific part is computing the front from the world's statistics and the information floors, rather than fitting a front to traits.

**1.3 Why it may matter for past data.** Several field attempts stalled on the same gate: prices measured independently, in fitness units (VIS-1F; *E. coli*; partly GRID-CROSS; [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md) §8). A frontier test asks only about dominance and direction:
- Is a selected system strictly inside the front with no measurable reason?
- Which way does it move along the front when stakes or drift change?

So some stalled attempts might become runnable. This is to be checked attempt by attempt after the freeze, and before any new data. No locked prereg is re-scored.

The attempt-by-attempt re-read is `theory/FRONTIER_REREAD_2026-11-22.md`. It is a planning note, not a lock, not a prereg and not a result. Sometimes the interpretation changes; it does not, by itself, turn a stalled attempt into a fair official test. DIR1 stays INCONCLUSIVE. The note's recommended next price-free real-data test is Candidate A: an antitone test of in-use package designs, with the world measured from upstream cadence on no-account sources. Candidates B and C are ranked below it. None of these is a preregistration. Direction A below (AI agent systems) has since been developed on main as `theory/SWARM_RULE_2026-11-23.md` and `applications/AI_AGENT_OVERSIGHT_2026-11-23.md`.

## 2. Direction A: AI agent systems

These are systems where the experimenter sets the read, upkeep and stake costs, so prices are known by construction (compare T30). Candidate questions:
- multi-agent swarms: pooling versus private models, and when a shared layer pays;
- memory design for agents: what to hold, when to re-read, when to act from a copy;
- layer counts in agent hierarchies as drift and stakes vary.

This is also the most immediately useful application. A prior-art check (for example Generative Agents, MemGPT/Letta, and the multi-agent literature) comes before any build.

## 3. Direction B: dynamics of reaching the frontier

How organizations form, merge and dissolve layers over time; how fast selection or learning moves a system toward the front (DS1, DS2 and N66 are the start); and when it gets stuck inside (valleys, EVO1's reachability finding W10, CT36 complements). This is the swarm-formation and origin-of-life direction, and the math there is thinnest.

## 4. Parked: a quantum extension of the floors

**Value judgment.** For cells, ants, firms and classical AI swarms, quantum mathematics adds nothing beyond the classical theory, because their judgment costs are classical. Proposed quantum effects in biology (photosynthetic energy transfer, magnetoreception, enzyme tunnelling) would at most change a sensing floor, which GTAO would take as an input. The current evidence is that long-lived coherence in photosynthesis is probably too weak to matter for function; this should be verified with sources before it is written anywhere canonical. So there is no "quantum theory of adaptive organization" as a replacement.

**Where it would genuinely change things: agents with quantum memory or quantum computation.** The no-cloning theorem (Wootters & Zurek 1982; Dieks 1982) says an unknown quantum state cannot be copied, and measuring it disturbs it. In GTAO terms:
- **Sharing.** Pooling cannot broadcast a quantum model. Agents must share reduced classical summaries or pay for entanglement and teleportation, so the cost of a shared layer gains a floor.
- **Watching.** Each read partly erases the state being tracked. The read rate then trades against self-inflicted decay, not only drift in the world.
- **History.** "Keep prior versions until a correction proves out" (rule 4) cannot hold for quantum states, only for classical records of them.
- **Acting from a copy (rule 5).** Copies of a quantum model are not available at all, so the copy-versus-current tradeoff changes form.

**Conjecture to test later.** The frontier form carries over unchanged with quantum information floors (Holevo bound, quantum channel capacities, quantum Landauer), and the same layered design falls out with a different price on copying. Prior art must be checked first (quantum resource theories, quantum thermodynamics of information), and no novelty is claimed.

Restart condition: after directions A and B have a first result, or earlier if a quantum agent system offers a clean test.

## References (to verify on Crossref before any canonical use)

- Debreu G 1951, "The coefficient of resource utilization," *Econometrica* 19(3):273–292.
- Farrell MJ 1957, "The measurement of productive efficiency," *J R Stat Soc A* 120(3):253–290.
- Geoffrion AM 1968, "Proper efficiency and the theory of vector maximization," *J Math Anal Appl* 22(3):618–630.
- Shoval O et al. 2012, "Evolutionary trade-offs, Pareto optimality, and the geometry of phenotype space," *Science* 336:1157–1160.
- Wootters WK, Zurek WH 1982, "A single quantum cannot be cloned," *Nature* 299:802–803.
- Dieks D 1982, "Communication by EPR devices," *Phys Lett A* 92(6):271–272.
