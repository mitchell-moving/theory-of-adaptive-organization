# Independent review: nesting fixed point, 24 November 2026

Reviewed `forge-layer-fixed-point` at `2be9290fd86fa39a6b42940a92f980dd58e9ec82`. The reviewer did not write the folder. Nothing here edits `THEORY.md` or the author's scripts.

## Commands

Fresh clone of this branch into `/tmp/tao-lfp-review` (HEAD `2be9290`). Upstream `main` is `0f3791890078161a1172277162df5ac13ebbff46` (`git ls-remote https://github.com/Chad-Mitchell/theory-of-adaptive-organization.git refs/heads/main`). `git diff 0f3791890078161a1172277162df5ac13ebbff46 HEAD -- THEORY.md` is empty. `origin/main` is that same commit, and `HEAD:THEORY.md` equals `origin/main:THEORY.md` (`6caadae569116a94a74563398be94cebf6e99e9b`).

```
sha256sum theory/layer-fixed-point-2026-11-23/nest_map.out \
          theory/layer-fixed-point-2026-11-23/nest_map.json \
          theory/layer-fixed-point-2026-11-23/unit_choice_gate.out \
          theory/layer-fixed-point-2026-11-23/unit_choice_gate.json
python3 theory/layer-fixed-point-2026-11-23/nest_map.py
python3 theory/layer-fixed-point-2026-11-23/unit_choice_gate.py
python3 tools/check_consistency.py
python3 -m pytest -q
git log --format='%H %cI %s' --name-status -- \
  theory/layer-fixed-point-2026-11-23/PREREG.md \
  theory/layer-fixed-point-2026-11-23/PREREG_ADDENDUM.md \
  theory/layer-fixed-point-2026-11-23/PREREG_ADDENDUM_2.md
git log -p -- \
  theory/layer-fixed-point-2026-11-23/PREREG.md \
  theory/layer-fixed-point-2026-11-23/PREREG_ADDENDUM.md \
  theory/layer-fixed-point-2026-11-23/PREREG_ADDENDUM_2.md
```

Crossref: `GET https://api.crossref.org/works/<doi>` for each DOI below (colon DOI percent-encoded). Mirror memo: `git fetch` of `ace-probe-memos-2026-11-23` from `Chad-Mitchell/theory-of-adaptive-organization` (the object is not on this fork). That ref is `e3e0e70116fc9cabce11af7e1c25d93d18405b0b`.

Sha256 before and after the rerun, both scripts, stdout included:

| File | sha256 |
|---|---|
| `nest_map.out` | `85e0146042b52699f02587591d16d784818e3560505ba5f8c093aa9181c4d4ca` |
| `nest_map.json` | `496d9796c170171dbe4ca275e4ac46c4855991900209f398e2a2f54df9b94d5d` |
| `unit_choice_gate.out` | `024123a667067d702a49076cdb376db1470e8044ce309bb50adbc7bcaac4e1df` |
| `unit_choice_gate.json` | `81ddfc58089a6cec71de905239113735ab542f3c1c5ecc1dc373a352f8e90d3d` |

`check_consistency.py`: FAIL 0, RESULT PASS. `pytest -q`: 287 passed, 1 skipped. The two new scripts use the standard library. Collection needed pytest plus numpy, scipy, numba, and sympy; the run also had networkx, matplotlib, pandas, mpmath, statsmodels, scikit-learn, lifelines, diptest, requests, lxml, and rdata installed.

Commit order, committer dates, each prereg file added once and never modified:

| Commit | Date | What landed |
|---|---|---|
| `da9c817` | 2026-11-24T04:33:58Z | `PREREG.md`, `criteria.json`, `crossref.out` |
| `43ad8c6` | 2026-11-24T04:44:03Z | `PREREG_ADDENDUM.md` only |
| `8977f8f` | 2026-11-24T04:45:56Z | `PREREG_ADDENDUM_2.md` only |
| `2be9290` | 2026-11-24T04:54:30Z | scripts, both outputs, `MEMO.md`, `RUN_LOG.md`, `OPEN_WORK.md`, the pytest |

`git log -p` on the three prereg files shows pure adds. No result digit (`1.20021282055`, `1.45735693345`, `4.021`) appears in those patches. `nest_map.py` and `unit_choice_gate.py` are not in git until the same commit as both outputs.

## Findings

| Claim | Findings |
|---|---|
| Rerun byte-identical; consistency PASS; pytest 287 passed, 1 skipped | **confirmed** |
| `THEORY.md` unchanged versus upstream `main` | **confirmed** |
| Ten DOIs resolve on Crossref and match `PREREG.md` §5 / `crossref.out` | **confirmed** |
| Wording in the new folder and the T69 row | **confirmed** |
| Unit arm: mean `1.20021282055` moves by `1.93622895495e-13` under `(μ,γ)=(4,4)` | **confirmed** |
| Spread of the three slack quotients is `3.35211337112` | **confirmed** |
| Quotients `1.45735693345`, `2.74769744966`, `−0.604415921464` | **confirmed** |
| Gate string `FAIL_CHOICE`, `yielded none` | **confirmed** |
| `b=2` to `b=3` moves the candidate mean by 4.022 | **problem** |
| Locked cell is `MODE_DEPENDENT` | **problem** |
| No dimensionless number is yielded, read as a fact about CT34 | **problem** |
| Choice half of the gate was committed before it could have failed | **problem** |
| Unit arm had not been run when `8977f8f` was committed | **could not check** |
| Nesting operator is derived from CT34 | **problem** (invented analogue; the citation of the identity is real) |
| `b` is fixed by CORE | **confirmed** that it is not. CORE does not set a nesting integer |
| Negative Rayleigh quotient is a bug | **confirmed** that it is not |
| `FAIL_CHOICE` is only an artifact of this operator | **problem** as a claim that no reading yields a number; **confirmed** that this operator's spectrum depends on `k` and `b` |
| Preregistered cell rule can return SUPPORT, and can fail | **confirmed** |
| Addendum-2 gate can yield and can fail in both arms, on the locked test | **problem** |
| Each locked prediction names an input on which it fails | **problem** for SUPPORT and for the unit-arm demonstration |
| Prior-art log | **problem** on the "only in `PREREG.md`" sentence; the three section pointers are real |
| Ace's working conjecture is stated and labeled | **confirmed** |
| Mirror memo §6 is CONJECTURE, untested, no route to a running coupling | **confirmed** on upstream `e3e0e701` |

## Where the claims break

**1. Under the frozen argmin the cell is BROKEN, and ρ is not to be interpreted.** `PREREG.md:71` and `criteria.json:17–18` lock a golden section on `ln t ∈ [−8, 8]` at tolerance `1e-14`, and `PREREG.md:91` says S1 fails if `max |Tf*−f*| ≥ 1e-12`. `PREREG.md:91–93` then says BROKEN wins and ρ is not interpreted. Calling that golden section on their `f_*` at `b=2` gives `max |Tf*−f*| = 1.669e-7`. Scan plus golden section, still without Newton, gives `5.032e-9`. Both miss `1e-12`. The reported cell uses `newton_polish` (`nest_map.py:94–115`), which is not in the prereg. It is disclosed only with the results (`MEMO.md:53`). With Newton, S1 is `1.776e-15` and the scorer returns MODE_DEPENDENT (`nest_map.py:257–269`). The scripts themselves were first committed in `2be9290`, with the outputs.

The numbers of the exact minimizer are real. For `φ(t)=t^k+t^{−k}` the slack operator is diagonal in that mode. With `L=ln b` and `D=cosh(L/2)+s cosh(k L/2)`, the Rayleigh quotient on their trapezoid is `[cosh(k L/2)/D] (1 − ⟨t+1/t, φ⟩/⟨φ,φ⟩)`. At `s=1e-4`, `(Z,N)=(2,64)` this equals the printed values to every digit they print: `1.45735693345` and `2.74769744966` at `b=2`, and `2.26681080169` and `6.76937700018` at `b=3`. The factors at `s=0` are `3/2` and `11/4` (`MEMO.md:19`). The deficit is the gauge overlap, as that sentence says. An independent even-function evaluation of `φ_3=exp(−(ln t)^2)`, minimizer fixed at `ln(b)/2` by symmetry, gives `−0.604415921458` against the printed `−0.604415921464`. The sign is the inner product of a non-eigenmode after normalization removes `t+1/t`. Modes 3 and 5 already differ by `1.290`, so the spread `3.352` does not depend on the sign. Equal weights instead of the trapezoid ends (`PREREG.md:67` says "trapezoid (equal weights)") move `φ_3` to `−0.607` and do not flip the comparison.

**2. The choice arm was locked after its failure was already in hand.** `PREREG_ADDENDUM.md:5` says run 1 had been executed. `43ad8c6` contains no output. `PREREG_ADDENDUM_2.md:5` says the choice arm only reads that record, and that the unit arm had not been run. Run 1 already prints the `b=2`/`b=3` quotients and the three deformations (`nest_map.out:12–31`). Those already differ by more than `stable_tol` `0.02`. `8977f8f` contains the gate text and no result digits, nine minutes before `2be9290`. That commit is the first time either output, or either script, enters git, so the unit-arm process is not separately ordered. **Could not check** that the unit arm was unrun before `8977f8f`. The choice half could not have been prospective.

**3. 4.022 is not the movement of the candidate mean.** The candidate is defined as that mean (`PREREG_ADDENDUM_2.md:11`, `MEMO.md:15`). The means are `1.20021282055` and `2.87924521541`. The difference is `1.67903239486`. The figure `4.02167955053`, rounded to 4.022 in `MEMO.md:15` and `OPEN_WORK.md:120`, is `|ρ(φ_2,b=3)−ρ(φ_2,b=2)|`. `unit_choice_gate.py:91` sets `b_move` to the max of the mean move and the per-mode moves. The choice arm still fails on the mean alone (`1.679 > 0.02`). The printed gate is `FAIL_CHOICE` (`unit_choice_gate.py:99–107`, `unit_choice_gate.out:17–18`). The unit move `1.936e-13` matches `1.9e-13`. `OPEN_WORK.md:120` says `2e-13`.

The unit arm holds because it is an identity of this operator. For `H(t)=μ h(γ t)`, `F_H(t)=μ F_h(γ t)`, so `t_0` scales by `1/γ`, `F_0` by `μ`, and `TH=Th`. Any Rayleigh quotient of `TH` equals that of `Th`, up to rounding. A pass does not add evidence beyond the normalization in `PREREG.md:40`. A fail would have been a bug. The raw pair does scale: `t_0` `1.41421356237 → 0.353553390593`, `F_0` `4.24264068712 → 16.9705627485` (`unit_choice_gate.out:16`).

**4. The operator is not CT34, so "CT34 yields no number" is wider than the test.** CT34 is partial minimization: `min_{x,y}[F(x)+G(y;θ(x))]=min_x[F(x)+J*_T(θ(x))]` (`THEORY.md:497`, section B.10). The scalar cost `J=c/τ+ατ` with `α=wσ²/2` and `β=w²σ⁴/3` is the next paragraph of the CT22 proof (`THEORY.md:442`). `(4/3)α²=β` checks. The dyadic sum `F_f(t)=f(t)+f(t/b)` and `(Tf)(u)=2 F_f(t_0 u)/F_0` are declared "not as a theorem of CT34" (`PREREG.md:31–41`, `MEMO.md:9`). CORE does not choose `b`. The only `b` in the core list is a control coefficient (`CORE.md:58`). Ruin outside the sum is `CORE.md:27` and `CORE.md:66`. A8 and Theorem R1 are the paragraph at `CORE.md:52`. Calling `b` a free choice is right.

`FAIL_CHOICE` is the spectrum of this analogue, not a bad quadrature: `ρ(k,b)=cosh(k ln b/2)/cosh(ln b/2)` times a window factor. It does not say that every reading of CT34 is number-free. Lemma A (`PREREG.md:43`) already yields an invariant dimensionless multiplier, `0`, for every `b>0` on `At+B/t`. SUPPORT requires `|ρ|≥1.05` (`PREREG.md:85`, `criteria.json:13`), so that `0` is excluded on purpose. The memo's own limit is right: "This operator does not produce one dimensionless number" (`MEMO.md:17`). `OPEN_WORK.md:120` asks the question about CT34 nesting and answers "No number yielded."

**5. The yield gate does not actually face both ways on the locked test.** `nest_map.py:254–281` can return SUPPORT, and the six failure cells. That rule is two-sided. For these deformations the closed form makes SUPPORT unreachable; that is a result, not a rigged scorer. `unit_choice_gate.py:99–106` has `PASS`, `FAIL_UNITS`, `FAIL_CHOICE`, and `FAIL_UNITS_AND_CHOICE`. On this operator the unit arm cannot fail, by the identity above, and the choice arm cannot pass, by the closed form. `raw_moves` is printed and is not an input to `unit_fail` (`unit_choice_gate.py:95–98`). `PREREG_ADDENDUM_2.md:34–36` says quoting `t_0` or `F_0` is the input that shows the gate can fire. The code does not score that input.

**6. Addendum 1's SUPPORT falsifier was written after the result.** Disclosed (`PREREG_ADDENDUM.md:5` and `:16`). S1 with prefactor 1, Lemma A on `(t+1/t)+(t^3+t^{−3})`, and Lemma B at `b=3` and `b=1` (`PREREG_ADDENDUM.md:13–15`) follow from the locked lemmas and do not use the printed quotients. The SUPPORT row names "mode order 5 in place of mode order 3", which is the locked comparison itself. The cells and `criteria.json` were not edited after `da9c817`.

**7. Prior-art sentence overclaims; the pointers are real.** At `43ad8c6`, `git grep` of Feigenbaum, Coullet, Lanford, and period-doubling hits `PREREG.md`, the addendum sentence that claims they appear only there (`PREREG_ADDENDUM.md:20`), and `criteria.json:20` ("Feigenbaum-sized"). Nothing outside `theory/layer-fixed-point-2026-11-23/`. The three notes exist: `theory/MATH_COMPLETENESS_AUDIT.md:313–317` §(iii); `theory/MATH_ATTACK.md:237` §3.1 and `:302` §3.6; `reviews/night1/CORE_AUDIT.md:165` §2.5(e). That line has `γ=1/2`, not `H=1/2`, and it does not say "eigenvalue of a nesting map." The mirror claim map, upstream `e3e0e701` `MIRROR_MEMO.md:113` and `:147`, reads "Nested-layer fixed point gives a universal GTAO number | CONJECTURE, untested" and "no route to α was found." `MIRROR_REVIEW.md` row 7 passes the "no route" claim. Ace's sentence is present and labeled not a result (`PREREG_ADDENDUM.md:36`, repeated at `PREREG_ADDENDUM_2.md:40` and `MEMO.md:19`). The older phrase "same relations (not constants)" is already in that mirror commit's history. The application to mode order and `b` was written after run 1.

The cap comparison is weak by construction. `ŷ = F_{f_*}(t_c)+(q/2)V(t_c)` (`PREREG.md:57–58`) puts `Θ(t_c)=q`, so the unconstrained minimizer stays feasible. The printed cap move `4.37e-6` (`unit_choice_gate.json`) is leakage at `s=1e-4`, not a showing that a binding cap cannot move ρ. It does not flip this cell, because MODE_DEPENDENT fires first.

## Wording

In `theory/layer-fixed-point-2026-11-23/*.md` and the T69 row (`OPEN_WORK.md:120`): no "theory of everything", no "solved", no "bill", no "law", no holography or GR derivation, no statement about Chad. The claim is labeled **CONJECTURE** (`PREREG.md:3`, `MEMO.md:3`). A non-SUPPORT cell is a puzzle (`PREREG.md:11`, `OPEN_WORK.md:120`). The only quantum sentence says no quantum-record price is used (`PREREG_ADDENDUM.md:32`).

## DOIs

All ten returned HTTP 200. Year, container, and authors match `crossref.out`. Wilson 1974 lists one author. Simon and Ando, page field `111`. Geoffrion's Crossref title adds "Part I: Concepts", which `crossref.out:51` has and `PREREG.md:122` omits. The DOI is the right paper.

`10.1007/BF01020332`, `10.1007/BF01107909`, `10.1051/jphyscol:1978513`, `10.1090/S0273-0979-1982-15008-X`, `10.1103/PhysRevB.4.3174`, `10.1016/0370-1573(74)90023-4`, `10.1109/9.280746`, `10.2307/1909285`, `10.1287/opre.8.1.101`, `10.1287/mnsc.16.11.652`.
