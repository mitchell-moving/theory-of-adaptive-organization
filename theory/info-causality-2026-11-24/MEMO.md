# MEMO: paid information and information causality

*24 November 2026 (UTC). Desk derivation, written after the prereg commit and not before it. Self-check, then the independent review at `theory/reviews/INFO_CAUSALITY_REVIEW_2026-11-24.md`. `THEORY.md` is unchanged. Open-work row T71. KNOWN and CONJECTURE below are the status words defined at `CORE.md:169` (header at `:167`). Relabel is the prereg's stopping word (`PREREG.md:44`). Model implication is plain language for the priced comparison, not a status word in that paragraph.*

## Why this approach

The conjecture needs a ceiling: after \(m\) communicated bits, Bob's total Shannon information about Alice's bits is at most \(m\). The premises on hand are a price list and a heat bound. A price ranks designs that are already on the menu. A7 takes the world's distribution as given (`theory/REPRESENTATION.md:62`). The heat floor bounds the bath heat of a memory's own transitions (`CORE.md:70`). The cheapest test is to ask which of those sentences, if any, is the ceiling. A search over boxes cannot supply a ceiling the sentences do not state, so no script is run unless one of them does.

The task is Pawłowski, Paterek, Kaszlikowski, Scarani, Winter and Żukowski, *Nature* 461, 1101–1104 (2009), DOI `10.1038/nature08400`, read from arXiv:0905.2292. Alice holds \(N\) independent bits, Bob holds an index \(b\), Alice sends \(m\) classical bits, a no-signaling resource may be shared, and Bob guesses \(\beta\). Their necessary condition is \(I\le m\), with \(I\) the sum of \(I(a_K:\beta\mid b=K)\) over the \(N\) indices. They derive it from three properties of a mutual information that has to make sense for the shared resource: consistency with Shannon information on classical parts, data processing for local operations, and a chain rule. For one perfect Popescu–Rohrlich box in van Dam's protocol they state \(P_{\mathrm I}=P_{\mathrm{II}}=1\) and \(I=2\) at \(m=1\).

## Results

| Check | Input | What came out | Label |
|---|---|---|---|
| P1 | van Dam, one perfect box, \(N=2\), \(m=1\) | A1–A8 leave \(I=2\) on the menu | relabel |
| P2 | same box, against `CORE.md:70` | the floor's hypotheses are not met | relabel |
| P3 | text of A6 and R1 | properties (1)–(3) for a no-signaling share are not stated there | relabel |
| P4 | message priced at \(\kappa\) per nat, stake \(w\) on the error | the box scores \(\kappa\ln 2\); the classical one-bit protocol scores \(\kappa\ln 2+w/4\) | model implication |
| P5 | classical protocol of P4 | the Shannon sum is 1 bit; the heat floor is unused | KNOWN, classical scope of A6 |

The column is not a list of `CORE.md:169` status words. KNOWN is one of those words. Relabel is the stopping word. Model implication is plain language.

**P1.** Theorem R1 (`theory/REPRESENTATION.md:84-92`) says a continuous cost representing the preorder is a price sum. The memory coordinate is Shannon mutual information for a finite alphabet, and the Gelfand–Yaglom–Dobrushin supremum when the mutual information is finite (`theory/REPRESENTATION.md:114`, `CORE.md:52`). A6 fixes which functional that coordinate is: the gross stock \(I(M_t;X^t)\), a different functional from the net learning rate (`theory/REPRESENTATION.md:60`). A8 makes a concatenating price nonnegative (`theory/REPRESENTATION.md:64`). A5 says there is no capacity ceiling on that coordinate (`theory/REPRESENTATION.md:56`). A nonnegative price on a coordinate that may be arbitrarily large leaves the random-access sum free of the ceiling \(I\le m\). A7 keeps the joint on the menu. No sentence in A1–A8 removes the perfect box or forces \(I\le 1\) on it.

**P2.** `CORE.md:70` bounds bath heat by \(kT\) times the net information flow of the memory's own transitions, under a memory/world split and local detailed balance, or the Einstein relation for additive-noise diffusions, in a steady state or a long-run average. The perfect box is a one-shot conditional distribution. It has no transition rates and no bath. The named processes are bipartite jump processes and additive-noise diffusions. The box is neither. The paper states that classical correlations have \(S\le 3\) and the perfect box has \(S=4\) (KNOWN, their CHSH accounting). A process of the kind `CORE.md:70` names therefore does not have this box as its stationary input-output distribution. The floor is silent on the input where the inequality fails. Silence is not a derivation of \(I\le m\).

**P3.** The step that produces \(I\le m\) for a general no-signaling resource is Pawłowski et al.'s (1)–(3) applied to the shared resource, plus independence of that resource from Alice's data. A6 and R1 state Shannon information, and its Gelfand–Yaglom–Dobrushin extension, for ordinary random variables. They do not state a data-processing inequality or a chain rule for a no-signaling box. Adding (1)–(3) on that box is adding the hypothesis from which the paper proves the inequality.

**Recomputation the prereg required (C4).** Perfect box: \(A\oplus B=xy\) with probability 1, local outputs uniform. Alice inputs \(x=a_0\oplus a_1\) and sends \(M=a_0\oplus A\). Bob inputs \(y=b\) and outputs \(\beta=M\oplus B\). Then \(\beta=a_0\oplus xy\). At \(b=0\), \(\beta=a_0\). At \(b=1\), \(\beta=a_1\). Each requested bit is fair and recovered exactly, so each Shannon term is \(1-h(1)=1\) bit and the sum is 2 bits, against a one-bit message. This agrees with the paper's \(I=2\). The message itself is independent of \(a_0\): \(A\) is uniform and independent of the inputs, so \(H(M)=\ln 2\) nats. The information is in the pair \((M,B)\), which is why a bound by \(H(M)\) needs a hypothesis about \(B\)'s share and not only Shannon information of the message.

**P5, classical menu (C3).** Shared randomness independent of \((a_0,a_1)\), message \(M=a_0\), guess \(M\) when \(b=0\) and an independent fair bit when \(b=1\). Then \(I(a_0:\beta\mid b=0)=1\) bit and \(I(a_1:\beta\mid b=1)=0\). The sum equals \(m\). The same pattern is the classical case of the paper's argument: if a classical share \(R\) is independent of \(\vec a\) and the guess is a function of \((M,b,R)\), Shannon's chain rule and data processing give \(I\le H(M)\). That is the mutual information A6 already names for classical records. The heat floor is not used. The perfect box has no such classical \(R\). This case does not rule the box out.

**P4 (C5).** The locked formula is \(J=\kappa H(M)+w\,\mathbb E[a_b\oplus\beta]\), \(b\) uniform, \(H\) in nats, \(\kappa>0\), \(w>0\). The box has error 0 and \(H(M)=\ln 2\), so \(J=\kappa\ln 2\). The classical protocol has error \(\tfrac12\cdot 0+\tfrac12\cdot\tfrac12=\tfrac14\), so \(J=\kappa\ln 2+w/4\). The box is cheaper by \(w/4\) at every positive price and every positive stake. A1–A8 add no further infinite cost on the box. A finite message price prefers the box. Section 4 of the prereg words the price as mutual information with the data. On this box the message is a one-time pad, so that mutual information is 0 and the cost falls to the stake term, which is also 0. The ordering is unchanged. Details are under Deviations.

## Conclusions

**Result: relabel.** For a general no-signaling resource, \(I\le m\) needs Pawłowski et al.'s information calculus, and A1–A8 plus the heat floor (`CORE.md:70`) do not supply it. That calculus is not added as an axiom. Paid-information accounting leaves correlations stronger than quantum on the menu.

**KNOWN, classical scope.** On classical shared randomness independent of Alice's data, \(I\le H(M)\) is Shannon's chain rule and data processing. A6 already uses that mutual information for classical records (`CORE.md:52`). It is the classical case of the 2009 argument. It is not a bar on a Popescu–Rohrlich box, and it is not the heat floor.

**Model implication.** A price per nat is a slope, and A5 refuses a ceiling (`theory/REPRESENTATION.md:56`). A finite nonnegative slope cannot impose a hard cap \(I\le m\). The heat floor prices the bath heat of a memory's own transitions, and only where that memory has transitions and a bath (`CORE.md:70`). A one-shot box has neither, so the cost has no term that caps one-shot correlations. No run. R1's coordinate for a classical message is its mutual information with what it records (`CORE.md:52`; `theory/REPRESENTATION.md:60`, `:114`), so \(I(M;\mathrm{data})\) is the reading the definitions support, and the locked \(\kappa H(M)\) is a conservative upper bound (\(I\le H\)). The scored cell stays \(\kappa H(M)\). The Holevo quantity used at `theory/probes-2026-11-23/duel/PREREG.md:27` on `ace-probe-memos-2026-11-23` stays an unadopted modeling choice. Under either reading of the message price, the perfect box is the cheaper design.

**Conjecture, still open.** Whether a heat bound outside the processes named at `CORE.md:70` could price a nonlocal box is a different hypothesis. This desk check does not support it. Information causality, even where the 2009 argument applies, is not known to single out the whole quantum set: the paper says so for correlations that respect the Tsirelson value \(E\le 1/\sqrt{2}\), and Allcock, Brunner, Pawłowski and Scarani (DOI `10.1103/PhysRevA.80.040103`; arXiv:0906.3464) report that part of the quantum boundary emerges from the principle. Quantum mechanics stays an input of that argument.

## Where the sentences are

- Axioms A1–A8: `theory/REPRESENTATION.md:43-64`. Ceiling refused: `:56`. Gross stock, not the learning rate: `:60`. Exogenous world: `:62`. Nonnegative prices: `:64`.
- R1: `theory/REPRESENTATION.md:84-92`. Memory coordinate: `:114`. Summary: `CORE.md:52`.
- Heat floor, hypotheses included: `CORE.md:70`. Worked class, a different list: `CORE.md:86`.
- Holevo as a duel pricing, not a premise: `theory/probes-2026-11-23/duel/PREREG.md:27` on `ace-probe-memos-2026-11-23`.
- No PR-box contestant on `upstream/main` at `0f37918` or on `upstream/ace-probe-memos-2026-11-23`. On the ace-probe branch the maximal tensor product is named only as a future composite to declare: `theory/probes-2026-11-23/reviews/DUEL_REVIEW.md:111`. That is the search the prereg logged. It is not a fork-wide claim. `origin/forge-composite-contest` at `e271ea971a10fbff4d58484cd2942c98dca12518` (2026-11-24 03:59:25 UTC), before this prereg, names Gmax, the maximal tensor product of two Bloch balls (`theory/PREREG.md:89` and `:105` on that commit). Gmax is not a Popescu–Rohrlich box. The task is a ruin-capped composite contest. That naming does not give \(I\le m\).
- Target and the value \(I=2\): Pawłowski et al. 2009, DOI `10.1038/nature08400`.

## Deviations

Two notes, neither a change to a locked pass/fail. The prereg was not edited.

The price section says a classical record is priced by its Shannon mutual information with the data it records. P4 and C5 write the formula as \(\kappa H(M)\) and the value \(\kappa\ln 2\). On the perfect-box protocol those two functionals differ: \(A\) is uniform and independent of \((a_0,a_1)\), so \(M=a_0\oplus A\) is independent of Alice's bits and the mutual information is 0, while \(H(M)=\ln 2\). C5 is scored as locked, on \(H(M)\). Under the mutual-information wording the box's information price is 0. In both readings the box is strictly cheaper than the classical protocol, and in both readings the cost leaves \(I=2\) in place.

One extra comparison. Reason: the same price section says that charging \(kT\) times the random-access sum, as if that sum were the learning flow, is a further choice and is outside the allowed premises. On the entropy pricing, that charge gives \(J_{\mathrm{box}}=(\kappa+2kT)\ln 2\) and \(J_{\mathrm{classical}}=(\kappa+kT)\ln 2+w/4\). The box remains cheaper when \(w>4kT\ln 2\). The added charge is still a finite price. It is not the ceiling \(I\le m\).

No script and no `RUN_LOG`. C1 fails and C6 forbids both. No PR-box contestant turned up on the trees the prereg searched. Gmax, already named on `forge-composite-contest`, is a different task and is not a script for this inequality.

## Score against the prereg

C1 fail. C2 pass (this memo names the added axiom and stops). C3 pass (sum is 1 bit). C4 pass (sum is 2 bits). C5 pass (the box is cheaper by \(w/4\)). C6 pass (no script).

## Errata

Response to `theory/reviews/INFO_CAUSALITY_REVIEW_2026-11-24.md` (commit `b70c81c`). The relabel stands. `PREREG.md` is unchanged. This desk check is open-work row T71.

1. **Number.** The row was first written as T69. Four branches collided on that number. The allocation is layer T69, constants T70, this desk check T71, composite T72. The science is the same.

2. **Contestant sentence.** The prereg's search of `upstream/main` and the ace-probe branch found no PR-box and no maximal-tensor implementation. That search stands. The reuse sentence in the first memo was wider than the search. `origin/forge-composite-contest` commit `e271ea9` (2026-11-24 03:59:25 UTC), before the prereg, names Gmax, the maximal tensor product of two Bloch balls. Gmax is not a PR box. The task is a different contest. It does not give \(I\le m\). The conditional script stays unrun.

3. **Labels.** `CORE.md:169` defines GENERAL, EXAMPLE, PROVED, KNOWN, SYNTHESIS, CONJECTURE, OPEN, and open miss. This memo uses KNOWN and CONJECTURE in that sense. Relabel is the stopping word locked in the prereg. Model implication is plain language for the priced comparison. The opening line that said the labels follow `CORE.md:167-169` was too wide, and it is corrected above.

4. **Answers on PR #250.** The relabel stays, and information causality is not added as an axiom. The scored cell stays \(\kappa H(M)\). \(I(M;a_0,a_1)\) stays the sensitivity row under Deviations and is not rescored. The named cost terms (`THEORY.md:26-34`: nats held, layer upkeep, the stake on the loss, acquisition, telling) and the heat floor (`CORE.md:70`) price a use. \(I(M_t;X^t)\) prices what a record holds about the world it tracks (`theory/REPRESENTATION.md:60`). None of them prices a shared resource by its correlations. `CORE.md` has no nonlocal, no-signaling, or CHSH term. That angle stops here.
