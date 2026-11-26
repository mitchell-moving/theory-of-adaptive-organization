# Preregistration: the memory coordinate for a record held in a general probabilistic theory

*Wednesday 25 November 2026 (America/New_York). Locked before any further run on the record-cost chain (`theory/RECORD_COST_CHAIN_2026-11-25.md`). `THEORY.md` and `CORE.md` are not edited. Status words are those at `CORE.md:169`. Nothing here derives quantum theory, general relativity, holography, or gravity.*

The hypothesis sentence is the one at `CORE.md:7`. This file does not restate it.

## What this file is, and what it cannot be

The zero-drift numbers under both readings below were computed before this file was written, in a private side session (25 November 2026). This file is therefore **not blind** to them. What it locks is the definition used by every run after it, and the reason for that definition, which is taken from A6 and not from which design wins. The definition chosen here is the one under which quantum theory does **not** win at zero drift.

## The question

`CORE.md:52` names the memory coordinate as mutual information in the sense of A6: finite-law Shannon information on finite alphabets, and, when finite, the Gelfand–Yaglom–Dobrushin supremum of discrete mutual informations. That is a functional of one joint law of world and memory. A memory that is a general probabilistic theory (GPT) state space has no joint law with the world until a readout is fixed, and entropy and mutual information on a GPT are not unique (Short and Wehner 2010, NJP 12:033023, DOI `10.1088/1367-2630/12/3/033023`; the repo's own Route 4 in `theory/QUANTUM_RECORD_PRICE_2026-11-24.md` records the same stop). Two readings were used in the side session:

- **Total.** One mutual information between the whole world variable and the memory.
- **Per record.** The sum, over independent records the memory must keep retrievable, of the best mutual information a separate readout gets for each record: \(P_{\mathrm{rec}}(S)=\sup\sum_j I_{\mathrm{acc}}(X_j;S)\). This is information causality used as a price (Pawłowski et al. 2009, Nature 461:1101, DOI `10.1038/nature08400`).

## Definition D (locked)

Let \(W\) be the world variable, with a finite law, and let the memory \(S\) be in state \(\omega_w\) when \(W=w\). For every fine-grained measurement \(M\) on \(S\) (a finite set of allowed effects summing to the unit effect), \(p(w,m)=p(w)\,e_m(\omega_w)\) is one joint law, and \(I(W;M)\) is its Shannon mutual information. Define

\[
I_{\mathrm{mem}}(W;S)\;=\;\sup_{M} I(W;M).
\]

When the memory holds several records, \(W\) is the joint variable of all of them: one total, never a sum over separate readouts.

## Reason from A6 (and where it is weak)

1. A6's coordinate is the mutual information of **one** joint law (`CORE.md:52`). For each readout \(M\), D applies A6 verbatim to the law \((W,M)\). Nothing beyond Shannon information on a finite classical law is used, so D needs no GPT entropy of \(S\).
2. The Gelfand–Yaglom–Dobrushin step in A6 takes the supremum over finite discretizations of one law. D takes the supremum over finite readouts. This is the weak link: readouts of a GPT state are not partitions of one sample space, so the step is an analogy, not a consequence. It is stated as such.
3. The per-record reading adds mutual informations of different readouts that need not have any joint law with each other. That sum is not the mutual information of any one law, so it is outside A6. The repo already records that the representation axioms do not force information causality on a general no-signalling box (ledger T71; `theory/info-causality-2026-11-24/MEMO.md`). Per-record pricing is therefore an added premise, not a reading of A6.
4. A6 does not choose between D and a Holevo-type form built on a GPT entropy (Short and Wehner). D is chosen because it stays inside A6's classical domain. If a reviewer finds that reason insufficient, the coordinate is **open** on GPT memories and both readings are reported with equal weight.

## What D implies for the numbers already computed (stated before any further run)

On the encodings used in the side session, D equals the capacity price \(\log_2 N\) (composition route, round 2, R2.1). At zero drift and stake \(q=4\):

| comparison | total reading (D) | per-record reading (secondary, labelled) |
|---|---|---|
| single systems | square 1.50, ball 1.73: square cheaper | ball 1.73, square 2.50: ball cheaper |
| pairs | boxworld 3.00, quantum 4.04: boxworld cheaper | quantum 4.04, boxworld ≥ 5.00: quantum cheaper |

Under the per-record reading the rivals win again above \(q\approx 7.7\) (pairs) and \(q\approx 12.4\)–\(17.6\) (single systems). Under D the zero-drift result stays an **open miss**.

## Rules for runs after this lock

- R1. Every later run that prices a GPT memory reports \(I_{\mathrm{mem}}\) by D as the headline, and the per-record value beside it, labelled "per-record (information-causality price; not A6)".
- R2. A quantum win that appears only under the per-record reading is not counted as a hit for the chain.
- R3. This file is not edited after the commit that adds `PREREG.sha256`. Changes go in a dated addendum.
