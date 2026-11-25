# The cost of judgment

*Chad Mitchell. Public working draft, CC0. Not peer reviewed. The full argument, with every number, is [`CORE.md`](CORE.md); the front page is [`README.md`](README.md).*

Thermodynamics tells an engineer the best an engine can do, and how far a real one falls short. This theory aims to do the same for any system that must act before its world arrives: cells, colonies, brains, teams, firms, AI and robot systems. Its object is the cost of judgment, defined for any adaptive system: the heat a memory spends, plus the stake on being wrong, under a cap on the chance of ruin.

$$J = \dot Q + w\,\mathbb{E}[\ell] \qquad\text{subject to}\qquad P(\text{ruin})\le\varepsilon.$$

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

If that holds, the gap to the minimum says where a system wastes and what would close it. The hypothesis is untested: no real system has been shown to sit at the minimum. The floor and the designs hold by proof, each inside named classes. Only the hypothesis can miss a measurement.

**What is proved, and where.** For bipartite Markov chains and additive-noise diffusions, in steady state the heat is at least \(kT\) times the rate at which the memory learns its world (Horowitz and Esposito 2014). Beyond those classes the floor is open. In the worked class of an exogenous equilibrium Ornstein–Uhlenbeck signal of rate \(a\) and variance \(v\), with mean-square loss and a memory that does not move its signal, the stake ratio is \(x=wv/(kT\,a)\). At or below \(x=1\) the cheapest design is blind and no memory pays. Above it the minimum cost is \(2\sqrt{kT\,a\,v\,w}-kT\,a\). The two-state telegraph, with Hamming loss and a memory that does not move its signal, is in that worked class and has a separate closed form.

These further results hold without a Gaussian or linear step: for systems meeting the representation axioms on at least three essential interval coordinates, a representing cost is a priced sum and the memory coordinate is Shannon information (the axioms do not choose the coordinates); memory costs heat in the classes above; on a fixed menu with the ruin cap slack, judgment spend does not fall as the stake rises; a boundary can be enough. In a Markov world with local precision the blanket is enough for a decision outside a region (T44). Through a finite-capacity boundary the tracked learning rate scales with area when capacity per area is bounded; frozen storage is not capped, and this is not the holographic bound (T62, `theory/AREA_LAW_PROBE_2026-11-23.md`; review fixes recorded at d79e766; independent review reported by T63 §1; no standalone review record). At a fixed per-site error a changing field costs heat with volume, and with a cut only when the decision names the cut (T41). Convex payoffs gain from shocks, and caps can reverse that gain; zero-gain control drops out. When the memory steers its world, in the named classes of T61, the heat bound holds on the net learning rate and no design-independent floor on memory heat alone exists (`theory/FEEDBACK_FLOOR_2026-11-23.md`; independent review reported in OPEN_WORK; no review record committed).

**The method.** Write the cost, find its minimum — or let a search scored by the cost find it — and read off the design. No single closed-form design exists for every system. In named classes, each in its own model, the minimum yields when memory pays, how many layers, what to share, where a boundary is enough, when a shock should strengthen a system rather than harm it, and when acting beats sensing alone. A team's minimized cost folds into its parent's problem, so the method nests, with a stated error when the team's cost does not enter as upkeep. Under weak-mutation selection with fitness linear in the cost, near a quadratic minimum in \(d\) coordinates the predicted excess is \(d/(2\beta)\), which shrinks as selection strength \(\beta\) rises. That route holds only under four conditions, each with a counterexample in our own runs or proofs: strong selection, a minimum the search can reach, a cost that includes everything that matters, and a coupling that settles. A beta-potential game settles near a Nash point, equal to the joint optimum when cost shares match stakes. A strongly monotone game can settle without being a potential game (CA5). A copy gain above one runs away, and a copy gain of one loses confinement. The world is a party we chose not to model as a player (CX2, `theory/COADAPTATION.md`). The stay rule assumes the part does not move the signal.

**What would count against it, and what is next.** Before a measurement is a test, a class must qualify: a cost-to-fitness map, a population proxy, a band that excludes a named rival, and a redesign time with at least ten of those times in the same world. A qualifying design outside that band is a miss for that class, logged with its signed size and the update it drives (`process/PROCESS.md`). Without that check, a field result is not a test of the hypothesis. Every scored field row so far is NOT A TEST or INCONCLUSIVE. The live work list is `OPEN_WORK.md`. T48 and T49 are on main. Next is the ranked gap list there, then qualify one strongly selected system, preregister and hash-lock the prediction, and measure.


<!-- claims-view:begin -->
Derived from the headline ledger in measurement/CLAIM_MAP_v2.md. Refresh this block from that ledger. A disagreement is a miss of a public claim.
HYP | hypothesis | no qualified real test
JP-HEAT | known | Horowitz and Esposito 2014, credited
EQ-HEAT | proved-in-model | in-model proof; not the whole physical argument
T57 | proved-in-model | T57 note; closed forms are named classes only
T60 | proved-in-model | proved in-model, one direction
T61 | proved-in-model | independent review reported in OPEN_WORK; no review record committed
T41 | proved-in-model | reviewed holographic note
T42 | proved-in-model | reviewed holographic-memory note
T44 | proved-in-model | reviewed boundary note
T62 | proved-in-model | review fixes recorded at d79e766; independent review reported by T63 §1; no standalone review record
T63 | proved-in-model | Independently reviewed (PR #240; commit 911a71c)
CX2 | open | reviewed, `reviews/coadaptation_2026-11-21/REVIEW.md`, CONFIRM2 READY at 93add78, merged as b16193d
CT31 | proved-in-model | Appendix B.10, proved in the model
CT32 | proved-in-model | Appendix B.10, proved in the model
CT34 | proved-in-model | Appendix B.10
CA1 | proved-in-model | CONFIRM2 READY at 93add78
CA5 | proved-in-model | CONFIRM2 READY at 93add78
F3 | proved-in-model | CONFIRM2 READY at 93add78
F4 | proved-in-model | CONFIRM2 READY at 93add78
F6 | proved-in-model | CONFIRM2 READY at 93add78
CL11 | open | open lever of section 3
SWARM-STAY | proved-in-model | swarm note, proved in that class
WORLD-PARTY | interpretation | interpretation of the co-adaptation setup
BICAUSAL | open | open row; pieces are not one result
GROWTH | proved-in-model | growth-bridge note
T40 | open | needs a reviewed adoption
T49 | proved-in-model | Independently reviewed (PR #238)
FOUR | proved-in-model | the fourth condition is the proved settling scope, not an if and only if
IP5 | false | claim-map section Y
LEAN-SCOPE | open | batch reviews recorded on main
T31 | open | parked
T71 | known | relabel; classical scope known
T73 | proved-in-model | self-check
T74 | open | routes stop
T72 | open | in flight upstream
GATE | open | open miss of the design interpretation in this ledger
<!-- claims-view:end -->
