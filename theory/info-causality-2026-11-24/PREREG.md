# PREREG: does paid information imply information causality?

*24 November 2026 (UTC). Desk check only. Written and committed before `MEMO.md`, before any derivation, and before any script. Branch `forge-info-causality`, cut from `upstream/main` `0f3791890078161a1172277162df5ac13ebbff46`. `THEORY.md` is not edited. A miss below is a puzzle to diagnose. Nothing here is a derivation of quantum mechanics.*

**Question (CONJECTURE).** Do representation axioms A1–A8 plus the heat floor imply the information-causality inequality of Pawłowski et al. for a random-access task, and does that inequality rule out correlations stronger than quantum?

The target inequality is not a premise. It is the statement under test.

## 0. Target, as checked before the derivation

Crossref, queried 24 November 2026 for `10.1038/nature08400`, returned: Pawłowski, Paterek, Kaszlikowski, Scarani, Winter, Żukowski; title "Information causality as a physical principle"; *Nature*, volume 461, issue 7267, pages 1101–1104; issued October 2009. The same DOI is the journal reference on arXiv:0905.2292 (*Nature* 461, 1101 (2009)).

What that paper states, and what this prereg uses as the target (arXiv:0905.2292v3 text, not a new formula):

- The task is a random-access code. Alice holds \(N\) independent bits \(\vec a=(a_0,\ldots,a_{N-1})\). Bob holds an index \(b\). Alice sends him \(m\) classical bits. They may have shared a no-signaling resource. Bob outputs a guess \(\beta\) of \(a_b\).
- The necessary condition they derive, once a mutual information with the three properties below exists, is \(I\le m\), where \(I\) is the sum of the Shannon mutual informations \(I(a_K:\beta\mid b=K)\) over Bob's indices.
- For one Popescu–Rohrlich box in van Dam's protocol, they state \(P_{\mathrm I}=P_{\mathrm{II}}=1\), hence \(I=2\) when \(m=1\).
- The three properties that do the work in their argument are: (1) consistency with Shannon mutual information on classical parts; (2) a data-processing inequality for local operations the theory allows; (3) a chain rule. Quantum theory enters because von Neumann mutual information has those three properties. The paper says the same mutual-information expression is not theory-independent for a general no-signaling box.
- For isotropic no-signaling boxes the paper writes the correlator as \(E\) in \(P(A\oplus B=ab\mid a,b)=\tfrac12(1+E)\), and states the Tsirelson value \(E\le 1/\sqrt{2}\), against \(E\le 1/2\) for classical correlations and \(E=1\) for the perfect box. The conditional script in §6 uses that boundary value only if C1 passes.
- The paper's own limit on the claim: among correlations that do not beat the Tsirelson bound, it is not known whether information causality singles out exactly the quantum ones.

Caveat, checked the same day, before the derivation. arXiv:0906.3464, DOI `10.1103/PhysRevA.80.040103` (Crossref title: "Recovering part of the boundary between quantum and nonquantum correlations from information causality"; Allcock, Brunner, Pawłowski, Scarani; *Physical Review A* volume 80; Crossref page field empty; arXiv journal reference Phys. Rev. A 80, 040103(R) (2009)). Abstract sentence used here: part of the boundary of quantum correlations emerges from information causality. Popescu and Rohrlich, "Quantum nonlocality as an axiom," *Foundations of Physics* 24, pages 379–385 (1994), DOI `10.1007/bf02058098`, is the box they axiomatize. No other paper is cited.

The html rendering of arXiv:0905.2292 writes one summation upper limit as \(N\) and the supplementary lower bound as a sum through \(N-1\). This prereg does not pick a third formula. The prose result it uses is the paper's \(I=2\) at \(m=1\) for the perfect box, and the sum is over the \(N\) indices the task defines.

## 1. Allowed premises, and nothing else

The derivation may use only these.

1. **A1–A8**, as written in `theory/REPRESENTATION.md:43-64`. In particular A6 (`:58-60`) fixes the memory coordinate as Shannon mutual information of a finite alphabet, in nats, and, when the mutual information is finite, the Gelfand–Yaglom–Dobrushin supremum of discrete mutual informations (`theory/CONTINUOUS_A6_2026-11-23.md`, summarized at `CORE.md:52` and `theory/REPRESENTATION.md:114`). A7 (`theory/REPRESENTATION.md:62`) takes the distribution of the world as given. A5 (`theory/REPRESENTATION.md:56`) says there is no capacity ceiling on a concatenating coordinate.
2. **Theorem R1** (`theory/REPRESENTATION.md:84-92`): a continuous cost representing the preorder is an additive price sum, up to one positive scale and one additive constant. Prices on concatenating coordinates are nonnegative only with A8 (`:64`, `:92`). R1 does not choose the coordinate list (`CORE.md:52`).
3. **The heat floor** (`CORE.md:19-21`, `CORE.md:70`): under a memory/world split and local detailed balance, or the Einstein relation for additive-noise diffusions, in a steady state or a long-run average, bath heat is at least \(kT\) times the net information flow of the memory's own transitions. The citation printed at `CORE.md:19` is Horowitz and Esposito 2014, DOI `10.1103/PhysRevX.4.031015`. That DOI was not re-queried for this prereg. The worked class (`CORE.md:86`) is an exogenous equilibrium Ornstein–Uhlenbeck signal, independent signals of that kind, or the two-state telegraph. The memory does not move the signal.

Not premises, even if a step would like them: Pawłowski's properties (1)–(3) applied to a no-signaling box; the Holevo quantity; Tsirelson's bound as an assumption; a claim that the menu of joints is the quantum set.

## 2. Derivation plan

The memo tries three identifications and stops at the first point where the target inequality needs a statement that is not in §1.

- **D1. Price, not a ceiling.** Identify the random-access sum, or the message entropy, with R1's memory coordinate. A1–A7 make that coordinate linear in the cost. A8 makes the price nonnegative. A5 refuses a ceiling. Check whether a nonnegative price can force \(I\le m\). The expected answer is no: a price ranks menus, and A7 does not delete a joint from the menu.
- **D2. Classical records only.** Restrict the shared resource to classical randomness independent of \(\vec a\), and the message to a classical record. Shannon's chain rule and data processing then apply to the mutual information A6 names. Check whether that yields \(I\le m\) on that menu, and whether the same sentences apply when Bob's output also depends on a Popescu–Rohrlich box.
- **D3. Heat floor.** Ask whether `CORE.md:70` 's object is the random-access sum. The floor's flow is the net information flow of the memory's own transitions. The box is a one-shot conditional distribution. Check whether any generator inside the floor's hypotheses has that box as its stationary input-output distribution. Classical bipartite jump processes have classical joints. The paper's perfect box is outside the classical bound the paper states (\(S\le 3\), against \(S=4\) for the perfect box). If the box is outside the hypotheses, the floor does not speak about it, and silence is not a derivation of \(I\le m\).

Stopping rule, fixed now. If \(I\le m\) for a general no-signaling resource follows only by adding information causality, or Pawłowski's (1)–(3) on that resource, as a new axiom, the memo says **relabel** and does not add a script. A classical special case that is Shannon's theorem inside A6's scope is recorded as that scope. It is not, by itself, a premise that rules out a Popescu–Rohrlich box, and it does not authorize the script.

## 3. Prior art, logged before the derivation

Commands and what they returned. Working tree is `upstream/main` at `0f37918`.

- `rg` over the working tree for `information causality`, `PR-box`, `PR box`, `Popescu`, `Rohrlich`, `maximal tensor`, `random access`, `Tsirelson`, `boxworld`: no matches.
- `Holevo` in the working tree: one conjecture, not a derivation, at `theory/DIRECTIONS_2026-11-22.md:58` (Holevo named beside quantum channel capacities as a floor to test later).
- `git grep` of the same box and access phrases on `upstream/ace-probe-memos-2026-11-23`: no information-causality item, no random-access item, no Popescu–Rohrlich item, no PR-box contestant.
- The one maximal-tensor hit on that branch is a review instruction, not a contestant: `theory/probes-2026-11-23/reviews/DUEL_REVIEW.md:111` says a future composite pricing must name minimal and maximal tensor products in advance. No code implements them.
- The same branch's duel citation list includes Janotta, Gogolin, Barrett and Brunner 2011, DOI `10.1088/1367-2630/13/6/063024` ("Limits on nonlocal correlations from the structure of the local state space"), in `theory/probes-2026-11-23/duel/checks/crossref.out`. That is a different limit, from the shape of the local state space. It is not a random-access contestant and it is not used as a premise here.
- No existing PR-box or maximal-tensor-product contestant is available to reuse. The conditional script in §6 would have to be new, and §2's stopping rule forbids writing it if the desk result is a relabel.

Literature used for the target is §0. Nothing in §0 is a premise of §1.

## 4. Price of a communicated or quantum record (modeling choice)

**Choice M, fixed before the derivation.** A communicated classical record, if it is priced, is priced at \(\kappa\) per nat of Shannon mutual information between that record and the data it records, \(\kappa\ge 0\) only when A8 is assumed. Reason: A6 and R1 fix that coordinate for classical records (`CORE.md:52`, `theory/REPRESENTATION.md:114`) and do not fix a quantum information quantity.

A quantum record is not given a price by A1–A8. On branch `ace-probe-memos-2026-11-23`, `theory/probes-2026-11-23/duel/PREREG.md:27` chose, as a secondary pricing called P-info, a price per nat of record–world mutual information, and set the quantum case equal to the Holevo quantity \(\chi\). That choice is not adopted. Reason: the conjecture under test is whether A1–A8 plus the heat floor already imply the inequality. Putting \(\chi\) in by hand would add the bound the duel assumed.

The heat floor is not the price of the message and not the price of the box. Reason: `CORE.md:70` prices a learning flow under a memory/world split. The random-access sum is information Bob can read about Alice's data after a message and a shared resource. Those are different objects. Charging \(kT\) times the random-access sum, as if it were that learning flow, is a further choice, and §5 says how that choice is scored. It is not in the allowed premises.

## 5. Predictions, each with an input on which it fails

Expectations only. The memo recomputes them. If one misses, the memo records a puzzle and does not edit this file.

**P1.** A1–A8 do not imply \(I\le m\) for a general no-signaling random-access task.
Fails on the van Dam input (one perfect box, \(N=2\), \(m=1\), the paper's \(P_{\mathrm I}=P_{\mathrm{II}}=1\)) if some sentence of A1–A8, used as written, forces \(I\le 1\) or removes that box from the menu.

**P2.** The heat floor does not imply \(I\le m\) on that same input.
Fails if a generator that meets `CORE.md:70` (memory/world split, local detailed balance or the Einstein relation, steady state or long-run average) has the perfect box as its stationary input-output distribution and the floor inequality is then \(I\le m\).

**P3.** Pawłowski's (1)–(3), applied to a no-signaling share, are not theorems of A1–A8.
Fails if A6 or R1 already states a data-processing inequality and a chain rule for a no-signaling box plus a message.

**P4.** Choice M does not rule the perfect box out. Score \(J=\kappa H(M)+w\,\mathbb E[a_b\oplus\beta]\) with \(b\) uniform on \(\{0,1\}\), \(\kappa>0\), \(w>0\), and \(H\) in nats. On the box protocol the paper describes, the error is 0 and the message is one fair bit, so \(J=\kappa\ln 2\). On the classical protocol "send \(a_0\); guess the message if \(b=0\) and an independent fair bit if \(b=1\)", the error is \(1/4\) and \(J=\kappa\ln 2+w/4\). Then the box scores strictly lower.
Fails if, on these two inputs, the error is not \(0\) and \(1/4\), or if \(J\) for the box is not strictly smaller at every \(\kappa>0\), \(w>0\). Also fails if A1–A8 assign the box an infinite cost that this \(J\) leaves out. A pass of P4 is not a pass of "the premises imply the inequality." It is a pass of "a finite message price prefers the box."

**P5.** On the classical protocol of P4, the Shannon sum equals 1 bit, and the heat floor is not used.
Fails if that sum is not 1 bit, or if the only way to get the sum is `CORE.md:70`.

## 6. Code-scored pass and fail

No parameter is fitted. A later reader can score the memo against this list without adding a premise.

- **C1, derives.** Pass only if every step cites an allowed premise from §1 and the last step is \(I\le m\) for every no-signaling resource, including the perfect box. Fail if any step uses Pawłowski's (1)–(3) on that resource, the Holevo quantity, or a ban on the box that §1 does not state.
- **C2, relabel.** Pass if C1 fails and the memo names the added axiom (information causality, or (1)–(3) on the shared resource) and stops. Fail if the memo calls that addition a derivation from §1, or if a script is added after C1 fails.
- **C3, classical scope.** The P5 arithmetic. Pass is not a pass of C1. Fail if the sum on that input is not 1 bit.
- **C4, box witness.** From the conditional distribution of the perfect box alone, Bob's guess matches the requested bit with probability 1, so each Shannon term is 1 bit and the sum is 2 bits, against \(m=1\). Fail if that recomputation gives a sum of at most 1 bit with no extra premise. A disagreement with the paper's stated \(I=2\) is a puzzle about the reading, not a silent edit.
- **C5, message price.** The P4 comparison. Pass if the box's \(J\) is strictly smaller. Fail if it is not, on the stated inputs. A pass does not pass C1.
- **C6, script gate.** If C1 fails, no script and no `RUN_LOG` are added. Fail if either file exists. The script below is pre-registered so it cannot be redesigned after a look at its output, and it is run only if C1 passes.

Conditional script, only after a pass of C1. Two judges, Alice's bits and Bob's guess. Price \(\kappa\) per communicated nat under choice M. Stake \(w\) on the error \(a_b\oplus\beta\). Compare minimal \(J\) for three resources: classical shared randomness independent of \(\vec a\), a quantum strategy whose correlator is the paper's Tsirelson value \(E=1/\sqrt{2}\), and the perfect box. Fixed seed, byte-reproducible. Before any run, a two-line `RUN_LOG`: (a) the run can fail, and either outcome would change what the derivation claims; (b) it is the cheapest test of the premise that passed C1. Pass if the ordering of minimal \(J\) is the ordering that premise forces. Fail on any other ordering or on seed dependence. Reuse a PR-box or maximal-tensor contestant if one exists; §3 found none.

## 7. What this file does not do

It does not derive the inequality. It does not score P1–P5. It does not edit `THEORY.md`, `CORE.md`, or `OPEN_WORK.md`. Those steps, if they happen, are later commits.
