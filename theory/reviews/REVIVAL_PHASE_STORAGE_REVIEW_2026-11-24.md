# Independent review: revival phase storage (T83)

*24 November 2026 (UTC). Independent review of fork PR #21, head `dc24e7633891784865fbb851adcc7ddd68f91020`, branch `forge-revival-phase-storage`, parent `d2aeb8100e22870dc5aee2529356de970c82a820`. This file does not edit the preregistration, the memo, `THEORY.md`, or `CORE.md`.*

## Lock

Preregistration commit `f97d11fa2154a846c56bc5a002ff553e90f933a3`, author and committer Chad Mitchell, 2026-11-24T20:40:40Z, parent `d2aeb81`. Score commit `dc24e76`, 2026-11-24T20:53:05Z, parent the preregistration. The blob of `PREREG.md` is the same at both commits. sha256 `0397c70ea558bdbd58e6a4657213c12aee7582d6deea3a555c862f5e4cdc0144`, matching `PREREG.sha256`. At the lock the tree has the preregistration, the hash file, and a run log whose only entry says no script has been run. The score commit appends three lines to `RUN_LOG.md` and adds the script, the stored output, the memo, and `DEVIATIONS.md`. `THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b` and `CORE.md` blob `dbf0d2322ce9fe751a5359e85859ca6f9448ec66` match the parent.

`python3 tools/check_consistency.py`: PASS (0 FAIL) once `origin/main` is the PR base `d2aeb81`. `python3 tools/check_open_work.py`: PASS. `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE`: 291 passed, 1 skipped in 373s. The skip is `tools/test_lean.py:124`, "Lean 4 / lake is not installed". The ignored path imports numba. Two runs of `revival_phase_checks.py` matched the stored stdout byte for byte, including `FAILS 6`.

## What was recomputed

An independent sum, not the author's script, reproduces the stored Gauss-sum window. For every lowest-terms \(p/q\) with \(q\le 8\) other than \(q=7\), \(R\) on \(N=120\) and \(|a_0|^2\) sit on the locked height, and \(N_c\) matches. For all six numerators of \(q=7\), \(|a_0|^2=1/7\) and \(N_c=7\), while the window misses by \(2.6\times 10^{-3}\) to \(5.0\times 10^{-3}\), the same misses as `revival_phase_checks.out:16`–`:21`. At \(N=840\), all six numerators sit within \(3\times 10^{-12}\) of \(1/7\). The copy identity, checked on the author's packet at 48 mid-bin points, stays under \(2\times 10^{-14}\) at \(1/3\), \(1/4\), \(1/6\), and also at \(1/5\), \(2/5\), \(3/8\), \(1/7\), \(1/8\), and \(3/7\). The \(q=7\) miss is the unbalanced window. The shifted-copy formula holds there.

Nine irrational probes: the largest is \(R=0.011284563682\) at the seventh golden-ratio probe, under \(0.012\) and under the locked \(0.05\). \(\ln 120=4.787491742782046\). \(h(1/3)=0.636514168295\). Odd-mode coefficients from quadrature of \(\sqrt{2}\sin(n\pi x)\) on \((0,1)\) match \(2\sqrt{2}/(n\pi)\) to \(9\times 10^{-16}\), and the slope of \(\ln|c_n|^2\) against \(\ln n\) is \(-2\). Commensurate \(R(2\pi)=1\). Incommensurate \(R(2\pi)=0.116259270951\). On the locked grid \(t=0.37k\) the maximum is \(0.997501976263\) at \(k=435\). A step of \(0.001\) on the same interval reaches \(0.999999447963\) and stays below \(1-10^{-8}\).

Quadrature of \(\int_0^1 2\sin(n\pi x)\sin(m\pi x)\,x^2\,dx\) matches the corrected antiderivative \(2(-1)^r/(r^2\pi^2)\). \(\langle 1|x^2|2\rangle=-0.180126548697\). The printed \(I(r)\) gives \(-0.360253097395\). For even separations the printed element is \(0\) and the integral is not: \(\langle 1|x^2|3\rangle=0.037995443866\). Numpy's `eigh` on the printed matrix gives \(R(2\pi)=0.472533712464\) and grid maximum \(0.994552216198\). On the integral it gives \(0.929538906895\) and \(0.989130295842\). A twenty-times finer grid keeps both maxima below \(1-10^{-6}\) and above \(0.95\).

## Citations

Crossref, 24 November 2026, HTTP 200 for all nine DOIs. Titles, authors, volumes, and start pages match the preregistration. Berry 1996 is Journal of Physics A 29, 6617–6629, "Quantum fractals in boxes". His equation (7) is \(D_f=\tfrac12(5-\beta)\) when \(|a_m|^2\sim|m|^{-\beta}\). The abstract and §2–§4 give \(D_{\mathrm{time}}=7/4\) for almost every position and, in one dimension, \(D_{\mathrm{space}}=3/2\) for almost every time. At \(\tau=p/q\) his half-integer propagator is a sum of \(q\) shifted copies. The note says that convention is his, and that the integer-well count is proved in the preregistration. That separation is right: the integer count is \(q\), \(q/2\), or \(q/2\) with a zero return, and the algebra in `PREREG.md:85`–`:105` checks out when every residue appears equally often.

Aronstein and Stroud 1997, abstract: at all times the well is a superposition of translated copies, in a parity-conserving arrangement. Landauer 1961 is IBM J. Res. Dev. 5, 183–191, "Irreversibility and Heat Generation in the Computing Process". Bocchieri and Loinger 1957 is Phys. Rev. 107, 337, "Quantum Recurrence Theorem". The other five records match the printed titles.

Hogg and Huberman 1982 is the right paper (Phys. Rev. Lett. 48, 711). Its abstract says a nonresonant bounded quantum system under a time-periodic Hamiltonian reassembles itself infinitely often. The clause "its destruction once the spectrum is effectively irregular" (`PREREG.md:43`) is not that abstract. The scored incommensurate return is the close approach the recurrence theorems describe.

## Findings

### MEDIUM

1. **The keep-cost, the pinch entropy, the dephasing entropy, and the dimension link are constants in the script.** `revival_phase_checks.py:249`–`:255` sets the printed purity to \((\sum |c_n|^2)^2\), which is \(1\) for any normalized list, and the pass string contains the characters `Q_keep=0`. `revival_phase_checks.py:257`–`:267` sets the gap to \(|h(R)-h(R)|\). `:269`–`:274` compares \(\ln 120\) with \(\ln 120\) and prints both times from that one number. `:350`–`:354` records `C-link` as `True`. `PREREG.md:29` says a match that holds by the algebra already written is not evidence. The memo cites `out:39`–`:45` and `out:51` as the score. The numbers themselves are the right ones for this state: a pure flat packet has purity \(1\), a binary Born outcome has entropy \(h(R)\), and the flat Shannon entropy is \(\ln 120\). The bars cannot miss.

2. **`CORE.md:78` is a static record in a frozen or disconnected world.** The sentence at `CORE.md:78` is a memory that holds a fixed label, or a static record, after a one-time write, with the world frozen or disconnected. This well is a pure state whose phases wind, and `PREREG.md:49` already says the well has no memory/world split, so `CORE.md:70` does not apply and does not prove a zero. `theory/pointer-basis-stakes-2026-11-24/MEMO.md:68` says a record kept as an unmeasured state was not taken up. `PREREG.md:51` then reads the undefined terms as zero. The output `no_pinch=0` is the constant `0.0` at `revival_phase_checks.py:261`. The zero is the absence of a bath term in the model. Calling it the frozen-storage sentence is a reading past the hypotheses of that sentence. The note labels the reading a relabel and says it is not a derivation that the keep-cost is zero (`PREREG.md:51`, `PREREG.md:121`).

3. **MINIMAL-RETURN is a disclosed substitute for T81's flow ratio.** On `f625bb74c2702a6a9b1f7d5b8afff922f90cf8b3`, T81 defines \(q(T)\) as the fraction of displaced excitations that have made a first entrance into the agent region of a lazy path (`theory/record-ratio-measured-2026-11-24/PREREG.md`, the return display in §2). That chain has a mixing time and no revival time. `PREREG.md:59`–`:67` says so, names \(R(\tau)=|\sum |c_n|^2\exp(-2\pi i n^2\tau)|^2\) as MINIMAL-RETURN, and says that in this note the phrase "flow-ratio return share" means \(R\). The same disclosure is in the memo, the script header, `OPEN_WORK.md`, and `theory/README.md`. The swap is in the lock, before the run. \(R\) is the Born survival probability of the initial packet. Across \(t/T_{\mathrm{rev}}\) it is the known revival: Gauss-sum heights where the window is balanced, and values below \(0.012\) on the nine irrational probes. Ace's flow-ratio question, the share of destroyed-record cost that comes back, is not computed on this well. The locked score answers the survival probability.

### LOW

4. **The printed off-diagonal is zero on even separations.** `DEVIATIONS.md:7` is right that the boundary term dropped a factor of \(x\), and right about \(\langle 1|x^2|2\rangle\). That pair is an odd separation, where the printed value is twice the integral. Even separations are a different error: the printed \(I(r)\) is identically \(0\), and the integral is \(2(-1)^r/(r^2\pi^2)\). The unscored integral in the script is the corrected antiderivative. Both matrices, printed and integral, sit on the passing side of every P-well bar, on the locked grid and on a finer one. The six B-shape fails stay fails. `DEVIATIONS.md` is a new file; it does not edit the preregistration.

5. **Two glosses sit past the sources.** `PREREG.md:131` calls the exact commensurate return an "Exact Poincaré return". The exact return at \(t=2\pi\) is the integer spectrum \(E_n=n^2\). Poincaré recurrence, and Bocchieri and Loinger, are the statement that a finite system comes arbitrarily close. `PREREG.md:43` adds a destruction clause to Hogg and Huberman that their abstract does not state. `PREREG.md:35` says the density is fractal at irrational times. Berry's statement is almost every time, with further slices of dimension \(5/4\). His \(\beta=2\) for \(D_{\mathrm{line}}=3/2\) is the spatial spectrum of \(P\) along a line (his equations (32)–(33)), for the uniform state in the half-integer basis. The odd-mode slope \(-2\) is the same exponent for the integer-well uniform state. The note already says a truncation slope is not his dimension (`PREREG.md:159`).

Wording in the new files: "law" appears only inside the quotation of `CORE.md:7`, which already says "(hypothesis)". "kill" and "verdict" appear only in the sentences that forbid them (`PREREG.md:7`, `PREREG.md:151`). The diff has no "theory of everything", "solved", or "bill". General relativity, quantum mechanics, holography, and gravity appear in the sentence that says the note does not derive them. No email, phone number, or other contact data is in the diff.

## Attacks tried

- sha256 of `PREREG.md`, blob identity from `f97d11f` to `dc24e76`, parent chain, and timestamps.
- `THEORY.md` and `CORE.md` blob equality with `d2aeb81`.
- `check_consistency.py` on the sandbox's stale `origin/main` `0f37918`: freshness FAIL, because `STATUS.md` points at `31aa997`. After `git fetch origin main`, the tip is `d2aeb81`, `31aa997` is inside the five-commit window, and the check passes.
- Full pytest with the numba path ignored: 291 passed, 1 skipped. The skip reason is the missing Lean toolchain.
- Two byte-comparisons of the scored script against `revival_phase_checks.out`.
- Independent Gauss sums, window sums, \(N=840\) for every numerator of \(7\), nine probes, \(\ln 120\), \(h(1/3)\), quadrature of the odd sine coefficients and their slope.
- Copy identity on six fractions the lock does not score, including \(q=7\).
- Incommensurate return on the locked grid and on a step of \(0.001\). The finer maximum is higher and still below \(1-10^{-8}\).
- Quadrature of \(\langle n|x^2|m\rangle\), and `numpy.linalg.eigh` of both matrices, on the locked time grid and on a finer one.
- Crossref for all nine DOIs, and Berry's paper (the author's PDF of J. Phys. A 29, 6617) for the dimension formulas, the half-integer clock, and the count of \(q\) copies.
- T81's preregistration at `f625bb7`, read from the fork, for the definition of \(q(T)\).
- Wording scan of the ten-file diff. Line checks of `CORE.md:7`, `:52`, `:70`, `:78`, `:161` and of T73 `MEMO.md:66` and `:68`.

## Clues for a torus or dephasing note

Rational \(\tau=p/q\) with a balanced window is a finite Gauss sum: \(R=1/N_c\) when a copy sits on the origin, and \(R=0\) when \(q\equiv 2\pmod 4\). Irrational probes on this window sit below \(0.012\). The \(q=7\) miss is an incomplete covering of the residues, the same arithmetic as a rational winding that does not close inside the mode window. \(N=840=\mathrm{lcm}(1,\ldots,8)\) closes it.

A commensurate spectrum \(E_n=n^2\) meets itself at \(t=2\pi\) because every phase \(n^2 t\) is a multiple of \(2\pi\). An incommensurate spectrum \(E_n=n^2+\sqrt{p_n}\) is a linear flow on a torus. At \(t=2\pi\) the quadratic part realigns and the irrational part leaves \(R=0.116259270951\). Later on the same flow the state comes within \(5\times 10^{-7}\) of a full return on a fine grid and does not hit \(1\). That close approach is the torus return.

Full energy dephasing replaces the off-diagonal phases that rebuild the packet. The Shannon entropy of the flat populations is \(\ln 120\) at every \(\tau\), because the populations do not move. A follow-up that wants dephasing to do something has to score the decay of \(R\), or of the off-diagonal revival, under a partial dephasing channel. Berry's half-integer clock (always \(q\) copies, \(D_{\mathrm{time}}=7/4\), \(D_{\mathrm{space}}=3/2\)) and the integer clock (\(N_c=q\) or \(q/2\)) are different propagators. \(R(\tau)\) is the survival probability. It is not the graph dimension of \(P(x)\), and it is not T81's hitting fraction.

## Result

Blockers remaining: 0. The Gauss-sum heights, the copy identity, the irrational probes, \(\ln 120\), the slope \(-2\), and both spectral returns recompute. The six \(q=7\) misses and the wrong off-diagonal stay logged, and the preregistration is unchanged. The keep-cost reading is a relabel past `CORE.md:78`'s hypotheses, scored by constants. The survival probability is the known revival. The flow-ratio question from T81 is still open.
