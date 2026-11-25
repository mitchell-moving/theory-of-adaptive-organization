# Independent review: information causality, 24 Nov 2026

Reviewed `745b983769b8c7069bf42492599f4e3d28f21f07` on `forge-info-causality` (same SHA as `origin/forge-info-causality` before this review). The desk check was not written here. No file of it was edited.

## Commands

Fresh clone of that SHA, then from the clone root:

- `python3 tools/check_consistency.py` — PASS, FAIL 0. The length notes on `THEORY.md` and `README.md` are the pre-existing advisory.
- `python3 tools/check_open_work.py` — PASS, 0 missing.
- `python3 -m pytest -q tools` — 285 passed, 1 skipped, 405 s. The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). Pytest 9.2.0, NumPy 2.5.5, SciPy 1.18.1, and SymPy 1.14.0 were installed for the run.
- `git log -p -- theory/info-causality-2026-11-24/PREREG.md` — one commit, `5d33d156fde0d01d1d24e7e22e01dc02b96949f3` (2026-11-24 04:47:21 UTC), file added as `@@ -0,0 +1,101 @@`. No later hunk.
- `git diff 5d33d15 745b983 -- theory/info-causality-2026-11-24/PREREG.md` — empty. The memo commit `745b983` (05:04:47 UTC) adds `MEMO.md` and edits `OPEN_WORK.md` only.
- `git diff 0f3791890078161a1172277162df5ac13ebbff46 HEAD -- THEORY.md` — empty. That SHA is `upstream/main`.
- `GET https://api.crossref.org/works/<doi>` for the five DOIs below.
- Pawłowski et al. and Allcock et al. read from the arXiv e-prints `0905.2292` (`infocaus2.tex`) and `0906.3464`.
- This review enumerated the uniform 16-atom van Dam joint and the classical protocol. Not a repo script.

## Findings

**Relabel: A1–A8 plus the heat floor do not imply \(I\le m\). Confirmed.**

Nothing in the allowed premises is that ceiling. Attacks that do not produce it:

- A5 (`theory/REPRESENTATION.md:56`) says there is no capacity ceiling on a concatenating coordinate. That is a statement about the cost, and a nonnegative price ranks a menu. It does not force \(I\le m\).
- The ruin cap is A2's feasibility constraint (`theory/REPRESENTATION.md:45`, `:96`). A zero-error box is easier to keep inside the cap, not harder.
- The stake \(w\) (`CORE.md:29`) multiplies the loss. Raising it makes the perfect box cheaper by the same \(w/4\).
- Layers (`CORE.md:100`) are a reset stack. They are not a random-access bound.
- Pricing the message by its mutual information with the data, the prereg's choice M (`PREREG.md:61`), gives \(I(M;\vec a)=0\) on the perfect box (one-time pad). The cost falls to the stake, which is 0. The box is cheaper. That is still not \(I\le m\).
- Shannon data processing and the chain rule do apply to the classical bits of this joint, and on it the random-access sum is 2 bits with \(m=1\). So those theorems, which A6 already has for ordinary variables (`theory/REPRESENTATION.md:60`), do not imply the ceiling. The step that does is Pawłowski et al.'s (1)–(3) on the shared resource (arXiv source lines 146–151 and 166–184). Adding that calculus, or information causality itself, is a new axiom (`MEMO.md:35`). The relabel is not premature.

**\(I\le m\) needs those three properties as an added axiom. Confirmed.** The properties in the prereg match the paper: consistency with Shannon information, data processing for allowed local maps, and the chain rule. The paper says \(I(\vec a:\vec x,B)\) is not theory-independent for a general no-signaling share (source lines 138–144). A6 and R1 state Shannon information and the Gelfand–Yaglom–Dobrushin stock for ordinary variables (`theory/REPRESENTATION.md:58-60`, `:114`). They do not state (1)–(3) for a no-signaling box.

**Under \(\kappa H(M)\) the perfect box is cheaper by \(w/4\). Confirmed.** Both messages are fair, so \(H(M)=\ln 2\) nats. Box error 0. Classical protocol "send \(a_0\); fair independent guess if \(b=1\)", \(b\) uniform: error \(\tfrac12\cdot 0+\tfrac12\cdot\tfrac12=\tfrac14\). Difference of \(J\) is \(w/4\) at every \(\kappa>0\), \(w>0\). The protocol matches the paper's van Dam figure (source lines 251–263): input \(a_0\oplus a_1\), message \(a_0\oplus A\), guess \(x\oplus B\). The paper's \(P_{\mathrm I}=P_{\mathrm{II}}=1\) and \(I=2\) at \(m=1\) (source lines 281–284) match a direct recomputation. The extra \(kT\) comparison in `MEMO.md:58` is also right: the box stays cheaper when \(w>4kT\ln 2\). That charge is outside the premises, as the memo says, and it is still not the ceiling.

**The heat floor does not apply to a one-shot box. Confirmed.** `CORE.md:70` needs a memory/world split, local detailed balance or the Einstein relation, and a steady state or long-run average. The flow is the net information flow of the memory's own transitions, for bipartite jump processes or additive-noise diffusions. A Popescu–Rohrlich box is one conditional distribution. It has no rates and no bath. The paper's classical bound is \(S\le 3\) and the perfect box has \(S=4\) (source lines 277–281), so no classical joint in that class has the box as its input-output law. A repeated embedding would still be a heat lower bound, not \(I\le m\).

**A1–A8 readings. Confirmed.** Checked against the files at this head:

| Claim | Where it is |
|---|---|
| A1–A8 | `theory/REPRESENTATION.md:43-64` |
| A5, no capacity ceiling | `:56` (axiom starts at `:53`) |
| A6, Shannon stock \(I(M_t;X^t)\), not the learning rate | `:58-60` |
| A7, world law fixed, not set by the design | `:62` |
| A8, concatenating coordinates are bads | `:64` |
| R1, price sum; signs need A8 | `:84-92` |
| Memory coordinate, finite mutual information | `:114`; summary `CORE.md:52` |
| Heat floor, hypotheses included | `CORE.md:70` |
| Worked class | `CORE.md:86` |
| Horowitz–Esposito citation | `CORE.md:19` |
| Status words | `CORE.md:169` (header at `:167`) |

A7 does not place the box on a menu. It also does not remove it. The sentence that carries the relabel is the negative one (`MEMO.md:21`): no sentence of A1–A8 forces \(I\le 1\) or deletes the box. That sentence is right.

**No PR-box contestant on the trees they searched. Confirmed.** `git grep` of `information causality`, `PR-box`, `PR box`, `Popescu`, `Rohrlich`, `maximal tensor`, `random access`, `Tsirelson`, `boxworld` on `0f37918` is empty. On `upstream/ace-probe-memos-2026-11-23` the same box and access phrases are absent. The maximal-tensor hit is `theory/probes-2026-11-23/reviews/DUEL_REVIEW.md:111`, a review instruction to name the products in advance. Holevo at `theory/DIRECTIONS_2026-11-22.md:58` on `0f37918` is a conjecture to test later. P-info at `theory/probes-2026-11-23/duel/PREREG.md:27` on that branch is the Holevo pricing they refused. Janotta et al. are in `theory/probes-2026-11-23/duel/checks/crossref.out:13`. No Python on this branch implements a box.

**"No maximal-tensor contestant is available" as a fork-wide sentence. Problem.** `origin/forge-composite-contest` names Gmax, the maximal tensor product of two Bloch balls, in `theory/PREREG.md` (commit `e271ea9`, 2026-11-24 03:59:25 UTC, before this prereg). There is no Python, it is not a PR box, and the task is a different contest. It does not imply \(I\le m\), and the conditional script was correctly not run. The logged search of `upstream/main` and the ace-probe branch is accurate. The reuse sentence is wider than that search.

**Allcock et al. Problem-free. Confirmed.** Crossref title, authors (Allcock, Brunner, Pawłowski, Scarani), *Physical Review A* 80, issued 2009-10-14, page field empty. arXiv journal reference `Phys. Rev. A 80, 040103(R) (2009)`. Abstract sentence: "we show that part of the boundary of quantum correlations actually emerges from information causality." The prereg's shortening matches it. The body shows two slices where the information-causality condition cuts on the quantum boundary, and says that below Tsirelson it is not known that every post-quantum box violates the principle. Pawłowski et al., source lines 351–352: among correlations that do not violate the Tsirelson bound, it is not known whether information causality singles out the quantum ones. The \(E\) formula, \(E\le 1/2\) classical, \(E\le 1/\sqrt{2}\) quantum, \(E=1\) for the perfect box, is source lines 297–301. The sum index \(N\) versus \(N-1\) is in the source (main-text line 117 versus supplementary line 650). They use the paper's prose \(I=2\), not a third formula.

**Prereg before the memo, predictions unedited, each names a failure input. Confirmed.** Order and the empty diff are above. P1 names the van Dam input. P2 names that same input against `CORE.md:70`. P3 names the text of A6 and R1. P4 names the two protocols. P5 names the classical protocol. Choice M and the locked \(\kappa H(M)\) differ on the pad; the memo scores the locked formula and records the other reading (`MEMO.md:52-56`). The prereg file was not changed.

**DOIs. Confirmed** against Crossref on this review. The query clock printed in the prereg is not a logged transcript; the fields match the live records.

| DOI | Record |
|---|---|
| `10.1038/nature08400` | Pawłowski, Paterek, Kaszlikowski, Scarani, Winter, Żukowski; *Nature* 461:7267, pages 1101–1104; issued 2009-10 |
| `10.1103/PhysRevA.80.040103` | Allcock, Brunner, Pawłowski, Scarani; *Physical Review A* 80; page field empty |
| `10.1007/bf02058098` | Popescu, Rohrlich; "Quantum nonlocality as an axiom"; *Foundations of Physics* 24:3, pages 379–385; 1994 |
| `10.1103/PhysRevX.4.031015` | Horowitz, Esposito; "Thermodynamics with Continuous Information Flow"; *Physical Review X* 4; 2014. Matches `CORE.md:19`. The prereg says this one was not re-queried |
| `10.1088/1367-2630/13/6/063024` | Janotta, Gogolin, Barrett, Brunner; "Limits on nonlocal correlations from the structure of the local state space"; *New Journal of Physics* 13, page 063024; 2011 |

**Wording rules on the new files and the T69 row. Confirmed.** No "theory of everything", no "solved", no "bill", no holography or relativity derivation, no personal remark. "CONJECTURE" is the question label in `PREREG.md:5`. A miss is called a puzzle (`PREREG.md:3`, `:93`). The inequality is not claimed as derived. `THEORY.md` is unchanged, as above.

**"Labels follow `CORE.md:167-169`." Problem, small.** That paragraph (`CORE.md:169`) defines GENERAL, EXAMPLE, PROVED, KNOWN, SYNTHESIS, CONJECTURE, OPEN, and puzzle. The memo's table also uses "relabel" and "model implication". "Relabel" is the prereg's stopping word (`PREREG.md:91`). "Model implication" is plain language used elsewhere in the repo. Neither is a status word in that paragraph. KNOWN and CONJECTURE are.

**T69 number. Problem.** This row is `OPEN_WORK.md:120`. Three other branches of this fork use T69 for a different question, also at `OPEN_WORK.md:120`:

- `forge-composite-contest` — ruin-capped composite records and local tomography.
- `forge-constants-exchange-rates` — \(k_B\) and \(\hbar\) as exchange rates.
- `forge-layer-fixed-point` — a CT34 fixed point and a dimensionless number.

The collision is the bookkeeping. It does not change the relabel.

## What this review does not do

It does not edit the desk check, `THEORY.md`, `CORE.md`, or `OPEN_WORK.md`. It does not add a script.
