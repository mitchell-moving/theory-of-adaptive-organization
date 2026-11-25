# Independent review: constants as exchange rates (2026-11-24)

Reviewed `forge-constants-exchange-rates` at `587c99f` (prereg `0846e2e`). The reviewer did not write the note. Nothing in the author's files was edited.

## Commands

Fresh clone of this branch at `587c99f`, then, from that tree:

- `python3 theory/constants-exchange-2026-11-24/dimension_check.py` exited 0. Stdout matched `dimension_check.out` byte for byte (1901 bytes).
- `python3 tools/check_consistency.py` exited 0. `FAIL: 0`, `RESULT: PASS`. Length warnings on `THEORY.md` and `README.md` are the pre-existing advisory counts.
- `python3 -m pytest -q`: 287 passed, 1 skipped. The skip is `tools/test_lean.py:124` because Lean 4 / lake is not installed. `tools/test_constants_exchange.py` is in the passing set.
- `sha256sum theory/constants-exchange-2026-11-24/PREREG.md` is `777532926d93ba8b2ce53efce56a9aa8bea9311d232ccf68066a93beda4fb6b9`, the same digest as `PREREG.sha256` and `tools/test_constants_exchange.py:9`.
- `git log -p 0846e2e..HEAD -- theory/constants-exchange-2026-11-24/PREREG.md` is empty. `git diff 0f37918 HEAD -- THEORY.md` is empty.
- `git ls-remote` of `Chad-Mitchell/theory-of-adaptive-organization` `refs/heads/main` is `0f3791890078161a1172277162df5ac13ebbff46`, the parent of `0846e2e`.
- `curl https://api.crossref.org/works/<doi>` for all 15 DOIs in `crossref.out`. Each returned HTTP 200.
- arXiv `export.arxiv.org` abstracts for `quant-ph/9710043`, `quant-ph/9908043`, and `1705.08023`.

The image had no sympy, pytest, scipy, or numba. Those were installed to run the author's scripts. The dimension-check bytes still matched the committed log.

## Findings

**Prereg order. Confirmed.** `0846e2e` (author and committer `2026-11-24T04:53:04Z`) is the parent of `587c99f` (`2026-11-24T05:03:45Z`). The first commit adds `PREREG.md`, `PREREG.sha256`, and `crossref.out`. The second adds `MEMO.md`, `dimension_check.py`, `dimension_check.out`, `tools/test_constants_exchange.py`, and the `OPEN_WORK.md` row. No later commit exists, and the prereg file is unchanged after the lock. The lock is that git order. Both commits are the same author, about ten minutes apart. There is no external timestamp.

**`THEORY.md` versus upstream main. Confirmed.** Upstream `main` is `0f37918`. This branch does not change `THEORY.md`.

**Crossref. Confirmed.** Title, authors, and year match `PREREG.md:59-67` and `crossref.out` for all 15 DOIs. The erratum title carries HTML bold markup around the volume number in the API; the words match. A title-plus-author query for the Mandelstam–Tamm paper returns the 1991 reprint `10.1007/978-3-642-74626-0_8` first. No 1945 journal record appeared in that page. The negative claim in `PREREG.md:63` and `crossref.out:26` stands. The 1945 text itself was not opened here.

**Dimension identities. Confirmed.** The basis in `dimension_check.py:13-17` is the usual one: \(k_B\) is energy per temperature, \(\hbar\) is energy times time, \(c\) is length per time, \(G\) is \(L^3/(M T^2)\). \(k_B T\) is an energy, \(k_B T\) times a rate is a power, \(\hbar/E\) is a time, \(ER/(\hbar c)\) is dimensionless, and \(GM^2/(\hbar c)\) is dimensionless. The script reports those identities, and a hand check agrees. `DIMENSIONS OK`, 4 passes, 6 fails, with the sixth fail labeled as not an identity (`dimension_check.out:29-32`).

**Classical \(k_B\) pass, as a reading of the cited lines. Confirmed.** Each cited formula is \(kT\) times a count or a rate, with \(k\) Boltzmann's constant:

- Erasure: at least \(kT\ln 2\) per bit (`theory/SCALE_ENDS.md:23`). One bit is \(\ln 2\) nats, so this is \(k_B T\) per nat.
- Ongoing heat: \(\dot Q_M\ge kT\,\dot I_M\) (`CORE.md:70`). Horowitz and Esposito 2014, eq. (11), is \(\dot S^X_i=d_t S_X+\dot S^X_r-\dot I_X\ge 0\), with \(\dot S_r=-\dot Q/T\) for one bath and \(k_B=1\) in the paper. In steady state the heat the memory gives off is at least \(k_B T\) times the information flow of its own jumps. That is the repository floor.
- Random walk: \(kT\cdot\sigma^2/(2D)\) with \(\sigma^2/(2D)\) in nats per time (`THEORY.md:295-297`). Same floor with error \(\varepsilon\) at `CORE.md:76`.
- OU: \(kT\,a(v-\varepsilon)/\varepsilon\) (`CORE.md:90`). Telegraph: \(kT\) times the flow (`CORE.md:94`).
- Clock: \(\dot Q\ge kT\,\omega'^2/D\) (`theory/CLOCK_TERM_2026-11-23.md:35`). Barato and Seifert's abstract costs an uncertainty \(\varepsilon\) at least \(2k_B T/\varepsilon^2\). With their phase convention \(\mathrm{Var}=2Dt\), the factors of 2 cancel and the displayed price follows. Phase is dimensionless there, so \(\omega'^2/D\) is a rate. The \(c\) in \(c/(\kappa kT)\) at `theory/CLOCK_TERM_2026-11-23.md:60` is the look price.

None of these expressions contains \(\hbar\), \(c\), or \(G\). Calling the result interpretation (`MEMO.md:7`) matches the prereg rule that the mapping is interpretation (`PREREG.md:53`).

**\(k_B\) pass as a check that could miss. Problem.** It cannot miss. `score()` is given `constants=("k_B",)` and kind `energy` or `power` (`dimension_check.py:72-111`). The identity \(k_B T\times(1\text{ or }1/\mathrm{time})\) equals energy or power is the definition of \(k_B\). P1–P3 miss only if the named formula is not monomial A (`PREREG.md:36-38`), and those sentences already say \(kT\) times a count or a rate. The script restates them. The fail input is named. Given the lines the prereg cites, the pass was fixed before the script ran.

**Margolus–Levitin and Mandelstam–Tamm, F3 for the tracking time. Confirmed.** The 1998 source states \(\tau_\perp\ge h/(4E)=\pi\hbar/(2E)\) above the ground state, so the orthogonalization rate is \(2E/(\pi\hbar)\). That is `theory/SCALE_ENDS.md:169` and Deffner and Campbell eq. (16). The abstract's "about \(3\times 10^{33}\) operations per second" per joule is the long-sequence rate \(2E/h\) in the same paper, half of \(2E/(\pi\hbar)\). `PREREG.md:62` says a pure number is not an input and does not choose between them. Either way the time is a number times \(\hbar\) over an energy. Mandelstam–Tamm is \(\tau=\pi\hbar/(2\Delta H)\) in Deffner and Campbell eq. (12), and the 1998 paper records the earlier bound \(\tau_\perp\ge h/(4\Delta E)\). The monomial \(\hbar/\Delta E\) is right. The 1945 text stays unchecked, as the note says.

The tracking-term fail is the locked F3: `energy_named` is false and the extra is an energy (`dimension_check.py:114-124`, `137-147`). The stake term in the rate cost is a power, the same currency as the heat (`CORE.md:27-29`; `THEORY.md:295` minimizes \(kT\cdot\sigma^2/(2D)+wD\)). It does not by itself name \(E-E_0\). Putting the erasure energy \(k_B T\) in that slot is the separate F1 row (`MEMO.md:42`), which the rule requires (`PREREG.md:28`, `:39`). A thermal width \(\Delta E\sim k_B T\) would be the same F1 for Mandelstam–Tamm. That composition is not a separate row. The unsubstituted F3 still stands.

**"The cost does not name the energy." Problem, low.** `MEMO.md:25` says the cost does not name \(E-E_0\). `MEMO.md:52` says that energy is not fixed by the cost unless one inserts \(k_B T\), and then says that on these bridges \(\hbar\) is the exchange rate in its own slot. The scored object is the memory and tracking terms. `MEMO.md:11` leaves the stake, the link price, and the ruin cap unscored, and `MEMO.md:48` already limits the fail to the tracking term's own time. A ruin reserve denominated in energy (`THEORY.md:34`) was not run. The F3 score for the tracking term is unchanged.

**Bekenstein and the printed entropy. Confirmed.** `theory/SCALE_ENDS.md:163` states \(E/S\ge\hbar c/(2\pi R)\). For a dimensionless nat count that is \(S\le 2\pi ER/(\hbar c)\), the same bound `theory/AREA_LAW_PROBE_2026-11-23.md:41` prints, and that line says the 1981 bound contains no \(G\). The table scores \(\hbar\) and \(c\) plus a length, F1+F3 (`MEMO.md:44`). It does not put \(G\) in the 1981 row. The printed entropy \(S=kA/(4\ell_p^2)=4\pi k GM^2/(\hbar c)\) is `theory/SCALE_ENDS.md:161`. Dividing out \(k\) leaves \(4\pi GM^2/(\hbar c)\). The script drops the pure \(4\pi\) and checks \(GM^2/(\hbar c)\) (`dimension_check.py:161-171`). That combination contains \(\hbar\), \(c\), and \(G\). The nat count \(1.05\times 10^{77}\) for one solar mass is \(4\pi GM^2/(\hbar c)\), so dividing \(k\) out is the count the table's number already is. A stake or a reserve does not remove \(c\) or the length from the 1981 bound, nor \(G\) from the printed entropy.

**Lloyd 2000. Problem.** The row is `fail F1+F3` with no formula checked (`MEMO.md:46`, `dimension_check.py:216-219`, where `n_fail += 1` is unconditional). The abstract (quant-ph/9908043) says the speed is limited by the energy, the information by the number of degrees of freedom, and that the limits explored are determined by \(c\), \(\hbar\), and \(G\). The log's paraphrase "limits set by \(c\), \(\hbar\), and \(G\)" matches that sentence. Naming the three constants across the paper is not one monomial. The speed limit inside that paper is the Margolus–Levitin bound, already its own row. The disclosure "abstract only, not checked" is accurate. The fail is stronger than the abstract. P6's miss input is a dimensionless count that is not A or B (`PREREG.md:41`). No such count was computed for Lloyd.

**Scope wording. Confirmed.** The cost alone is dimensionless and cannot set a scale (`PREREG.md:9`, `MEMO.md:3`, `OPEN_WORK.md:120`). Coupling is an open question, not an established limit (`PREREG.md:11-15`, `MEMO.md:3`, `MEMO.md:52`). The note rejects the stronger sentence and does not claim that \(\hbar\), \(c\), or \(G\) cannot arise. `MEMO.md:7` says the identities are not a derivation of those values and do not derive general relativity, quantum mechanics, or holography. Misses are puzzles in `MEMO.md:3` and in the `OPEN_WORK.md:120` row. The table's word "fail" is the score token from `PREREG.md:51-53`.

**Wording rules. Confirmed** for the new files and the new `OPEN_WORK` row. No "theory of everything", no "solved", no "bill", no personal remark about Chad. "Law" does not appear. The fine-structure aside points at a conjecture: upstream branch `ace-probe-memos-2026-11-23`, `theory/probes-2026-11-23/MIRROR_MEMO.md:113` begins with the sentence the prereg quotes, and line 147 is the claim-map row "Nested-layer fixed point gives a universal GTAO number", marked conjecture and untested. That branch is on upstream. It is not a head of this fork.

**One citation is loose. Problem, low.** `PREREG.md:11` says `theory/AREA_LAW_PROBE_2026-11-23.md:17` says the cost contains neither \(G\), \(\hbar\), nor \(c\). Line 17 says the extra input uses no \(\hbar\) or \(G\), and that a gravitational ingredient is one the cost does not supply. It does not name \(c\). The absolute sentence is `theory/PHYSICS_CHAIN_2026-11-23.md:73`, which is the other cite, and the memo's attribution to that line (`MEMO.md:3`) is right. Line 135 of the area-law note says the packing input does not use Newton's constant. It is not the sentence quoted.

**T69 collision. Problem.** `origin/forge-layer-fixed-point` (`2be9290`) also inserts a T69 row at `OPEN_WORK.md:120`. That row is the nested-layer fixed-point conjecture, preregistered `da9c817` at `2026-11-24 04:33:58 UTC`, about nineteen minutes before `0846e2e`. This branch's T69 is the exchange-rate question, same line number, same merge-base `0f37918`. The two rows are different work under one id. Merging both onto `main` conflicts on that line.

## What holds

The classical floors are \(k_B T\) per nat or per nat per time. \(\hbar\) prices a time over an energy, and using that time as the tracking term fails F3 under the locked rule because the tracking term does not name the energy. The 1981 stock bound brings in \(c\) and a length. The printed entropy count brings in \(G\) as well. Those scores are labeled interpretation. The Lloyd fail is not earned by a formula. The \(k_B\) pass restates formulas that were already written that way.
