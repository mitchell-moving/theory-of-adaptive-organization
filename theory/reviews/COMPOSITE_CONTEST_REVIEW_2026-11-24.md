# Independent review: composite contest and worst-question pivot (T69)

*24 November 2026. Reviewed branch `forge-composite-contest` at `d30f65ab3ad09db6bc6b2d3f1e7b6623d435d6d0`. Adversarial review. The author's files are not edited. Reviewer scripts: `theory/reviews/composite_contest_review_checks/`. Environment: Python 3.12.3, numpy 2.5.5, scipy 1.18.1 (HiGHS).*

## Summary

The reproduction is exact, the preregistration order holds, the DOIs resolve, and the wording follows the rules. The central lemma is false. **Lemma R (rebit floor 1/25, and 1/9 in the pivot) does not hold under the prereg's own rules.** A real singlet with real local observables reaches loss 0 at `K_AB = 10`, both in the mean and in the worst pair. Every `λ > 0` cell in both grids is then LOSE for the complex record. The other problems are smaller, and with the rebit at loss 0 none of them can change a label.

## Problems, by severity

**1. Critical: the rebit reaches loss 0, so Lemma R, Theorem W, P1, P3, Q1 and Q3 are false.**
`theory/composite-contest-2026-11-24/PREREG.md:93` lists `I, X, Z` as the local rebit observables. `±I` is a legal ±1 readout: it outputs a fixed sign. `theory/composite-contest-2026-11-24/PREREG.md:152` (Lemma R) and `theory/composite-contest-2026-11-24/PREREG_2.md:39` assume that every readout is a traceless `r·(X,Z)`. The direction `y` is orthogonal to every other menu vector, so the `y` row and column of the target are 0 except `T_yy = −1`. Take the real singlet `(|01⟩−|10⟩)/√2`, which Lemma C's real path reaches. Use `x→X`, `z→Z`, `p,m→(±X+Z)/√2`, and `y→+I` on Alice and `−I` on Bob. Then `C = T` exactly.

```
python theory/reviews/composite_contest_review_checks/rebit0.py
mean loss L = 1.1e-32   worst-pair L_inf = 4.9e-32   (all observables real, eigenvalues ±1)
```

With the rebit at `J_R = λ ln 10`, `Δ = λ ln(10/16) = −0.47λ` against a tie band of `0.028λ` (`rescore.py`). C LOSES every `λ > 0` cell in both grids. The first contest goes from MIXED (21/3) to LOSE (0/24). The pivot headline goes from MIXED (6/2) to LOSE (0/8). Both P1 (`theory/composite-contest-2026-11-24/PREREG.md:200`) and Q1 (`theory/composite-contest-2026-11-24/PREREG_2.md:88`) fail.

The code passed because it shares the proof's assumption. The rebit seesaw searches only traceless effects in the unit disk (`search.py:211–312`, `best_disk`). Check L4 builds only planar traceless effects (`lemmas.py:135–189`). The pivot never searches the rebit and hard-codes the floor (`run_pivot.py:144–147`). The memo's "rebit's mean error is exactly 1/25" (`COMPOSITE_CONTEST_2026-11-24.md:63,127`) is the minimum over the restricted effect set, not R's minimum. "The rebit stays infeasible below 1/9" (`:129`) is false.

**2. High: classical records are priced by atom count, not by the Hardy dimension of the composite.**
`theory/composite-contest-2026-11-24/PREREG.md:84,95` sets `K_AB = M` (shared atoms) and also says "local tomography: yes (a simplex)". With local tomography, `K_AB = K_A·K_B`. Responses are "functions of the local ontic point", and the preparation is a column-to-diagonal permutation, so the joint ontic set is `m_A × m_B`. C is charged the full 16 of its theory. H is charged the support of one protocol, which `theory/composite-contest-2026-11-24/PREREG.md` §1 forbids for every other contestant ("No contestant may replace K_AB by the dimension of one protocol's orbit").

Under `K = m_A·m_B`, a MILP shows that no local model with `K ≤ 10` meets `ε ≤ 0.1` in the worst-pair cap (`lt.py`: (1,10), (2,5), (3,3), (2,4) all infeasible). Every `K ≥ 11` costs `J ≥ 0.1 ln 11 + 0.0429 = 0.283`, which loses to C by more than the tie band. So the pivot's classical win at `λ = 0.1` (`:129`; `pivot decisions.out:321`) depends on this pricing choice. It does not change any final label, because of problem 1.

**3. Medium: H1 uses a classical record bigger than needed, and the "information vs dimension" puzzle is an artifact of that.** <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->
Only the pairs `n = ±u` are scored. A shared sign bit, with both wings outputting `sign(n)` whatever the query, has loss 0 at `M = 2` (`K = 4` under product pricing) and carries `I = ln 2` (`rescore.py`). The quantum ensemble's Holevo quantity is exactly `ln 3`, because `|n⟩|n⟩` lies in the 3-dimensional symmetric subspace. `control.out:4` gives 1.0986122886681096, which the memo reports only as "about 1.099". The minimal classical record is cheaper under the dimension price and under the information price. "Two coordinates rank the same control in opposite directions" (`COMPOSITE_CONTEST:107–109`; `theory/composite-contest-2026-11-24/PREREG_R2.md:47`) holds only for the 6-state copy (`theory/composite-contest-2026-11-24/PREREG_R2.md:39`). H1's label (C loses) is right, and more robust than stated.

**4. Medium: promised outputs and contestants are not implemented, and these gaps are not logged as deviations.**
- The `pinfo` and `orbit` secondary labels (`theory/composite-contest-2026-11-24/PREREG.md:70–72,140`) are never computed. P6 and P7 are printed sentences, not checks (`decide.py:216–217`).
- `I_A6` is hard-coded to `0.0` (`decide.py:125,128`). Info rows exist only for C and R, although `theory/composite-contest-2026-11-24/PREREG.md` §9 requires them for every contestant.
- G and R4c are constants in the grid (`decide.py:141,143`: feasible, K, L = 0). G has no implementation at all. R4c is checked only through lemma L6 (real projections reproduce the Born rule; this passes).
- R4a is a copy of H (`decide.py:142`) plus the printed witness −1 (L7).
- Gmin and Gmax share the product seesaw. Gmax is given only local reversibles by construction (`theory/composite-contest-2026-11-24/PREREG.md:105`).
- `search_results.json`, `grid_results.json` and the SHA256 of the scripts (`theory/composite-contest-2026-11-24/PREREG.md:238–241`) are not produced. The pivot's `envelope.txt` (`theory/composite-contest-2026-11-24/PREREG_2.md:98`) is not produced either.
- The pivot prices one classical point (K = 6, `L_∞` minimal) in every cell. At `ε = 0.1`, five atoms suffice (`piv.py`). No label changes.

**5. Medium: "PREREG_2 changes only the cap" (`COMPOSITE_CONTEST:127`) is inaccurate.**
`theory/composite-contest-2026-11-24/PREREG_2.md:27` changes the stake as well (`L_∞` enters `J`). It also changes the ε grid (`:60`) and the search (`:68–84`), and `pivot DEVIATIONS.md` D1 then replaced that search with an LP. The pivot was designed after seeing that the rebit won through the mean (`theory/composite-contest-2026-11-24/PREREG_2.md:9`), and the cap was chosen to exclude it. This is disclosed. It is a forking path, and it rests on the false floor of problem 1.

**6. Low: the memo understates its own classical search.**
`:71,113` say the search did not reach the Lemma B floor, and that WIN cells are "against this search". The envelope value 0.013725830020304794 is the certified global minimum `2(3−2√2)/25`: NNLS gives 0.0137258300203048, and the Frank–Wolfe dual gap is `−1.6e−15` (`qp.py`, `qp2.py`). Its minimum support is 8 (MILP). Lemma B's floor `(3−2√2)/25` is not attainable. The WINs against H at `λ ≤ 10^{−3}` and at `ε = 10^{−2}` are therefore certified. At `λ = 0.01`, `ε ≥ 0.05`, the WIN against H depends only on M = 3 or 4 models, which were not certified here: it would take `L_3 ≤ 0.0165` or `L_4 ≤ 0.0141` to flip it.

**7. Low: transcription slips in the memo.**
- `:56` gives R's `I_wings` as 1.3862943611198904; `decisions.out:5` has …841.
- `:63` gives CHSH −2.8284270928652244; `decisions.out:2` has …249.
- `:114` gives 3.4520245437103136e-02; `decisions.out:198` has …150.

## Findings per claim

| Claim | Finding |
|---|---|
| Mean cap: MIXED, 21 WIN / 3 LOSE of 24 | Code output confirmed (`decisions.out:276–278`). **Problem**: with a loss-0 rebit the result is 0/24, LOSE (problem 1) |
| LOSE cells are `λ = 0.1`, `ε ≥ 0.05` | Confirmed as output (`decisions.out:249–275`) |
| Rebit mean error exactly 1/25 | **Problem**: true only on the restricted effect set. R's minimum is 0 |
| `λ = 0` ties everywhere | Confirmed (`decisions.out:279`; G and R4c match L = 0, and now R does too) |
| `I_A6 = 0` for all contestants | Confirmed by construction (settings drawn after the record). Hard-coded, not computed |
| Bell floor `4.2893218813467290e-02` | Confirmed. Exact value `(3−2√2)/4 = ((√2−1)/2)^2 = 0.042893218813452427`, from Lemma B: `max|δ_i| ≥ (2√2−2)/4`. LP `s = 0.20710678118654757`, off by 1.5e-14 (solver). Not `1/2 − 1/(2√2)` (0.146) |
| 6-state classical record at that floor | Confirmed: minimum support 6 at `L_∞` min and at ε = 0.05 (MILP, `piv.py`). Fair under H's pricing rule; **problem** under consistent composite pricing (problem 2) |
| Rebit excluded below 1/9 | **Problem** (false; problem 1) |
| Pivot headline MIXED, 6 WIN / 2 LOSE, 0.22206916573627278 vs 0.2772588722239781 | Output confirmed (`pivot decisions.out:318–321,364`). The 6 WINs at `λ ≤ 0.01` are certified by the Bell floor against H. **Problem**: R makes all 8 LOSE |
| "Quantum win possible" proof (Theorem W) | **Problem**: rests on Lemma R. Lemmas C, CHSH, B, P, R4c, G and Tol checked and correct |
| Dimension pricing identical across contestants | **Problem** (problem 2) |
| Real-QM, GPT, R4a, R4c contestants implemented | Partly (problem 4) |
| Cell scores given the code's inputs | Confirmed: recomputed pair labels, the tie band and the aggregate rule |

## 1. Reproduction: confirmed

```
git clone --branch forge-composite-contest <origin> /tmp/fresh
cd /tmp/fresh/theory/composite_contest_checks
rm lemmas.out envelope.txt decisions.out control.out
PYTHONHASHSEED=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python run_all.py   # rc 0
sha256sum -c SHA256SUMS            # 5/5 OK; git status clean
cd ../pivot_worst_checks && rm decisions.out && python run_pivot.py && sha256sum -c SHA256SUMS   # OK
python tools/check_consistency.py  # RESULT: PASS, FAIL 0
python -m pytest -q                # 287 passed, 1 skipped (after installing numba, sympy)
```

No byte differences. `crossref.out` is not regenerated without `--with-crossref`. It was checked separately (section 4). HiGHS prints one stray line to stdout during the pivot. That is harmless.

## 2. Preregistration integrity: confirmed, with caveats

`git log --format='%H %cI %s' --name-status 0f37918..HEAD`:

- `e271ea9` 03:59 PREREG
- `18a36c0` 04:06 R2
- `99aff27` 04:17 scripts and outputs
- `e1d8af8` 04:18 PREREG_2
- `eb84314` 04:21 RUN_LOG and D1
- `d30f65a` 04:24 pivot script and output

Each prereg comes before the scripts and outputs it governs. Author and committer dates are equal. `git log --follow` shows each prereg file in exactly one commit, so no prediction was edited.

Caveats:
- Git dates are self-reported. Scripts and outputs land in one commit, so git cannot show that nothing was run before 04:17.
- R2 is a legitimate pre-run revision. It adds a control and demotes P1 without rewriting P1–P8. It also correctly called the ε = 0 slice an identity, although that identity is in fact false (problem 1).
- PREREG_2 changes more than the memo says (problem 5). Pivot D2 (K 11→6) came after the first solver result, but it went against C, and it is correct.

## 3. Ace's added standards

**(1) Does each prediction name an input under which it would fail? Problem.**
P1–P7 and Q1–Q6 are stated as consequences of proved lemmas (`theory/composite-contest-2026-11-24/PREREG.md:198`; `theory/composite-contest-2026-11-24/PREREG_R2.md:9–15`; `theory/composite-contest-2026-11-24/PREREG_2.md:88`). P8, Q7 and H2 lock no label, so nothing in them can fail. H1 was proved before the run. No prediction names an input that would make it fail while remaining a test. The identity checks were the place a failure could show, and they did not catch the false Lemma R, because the code used the same restricted effect set.

**(2) Prior art and literature check logged before the run? Partly confirmed, partly a problem.**
`theory/composite-contest-2026-11-24/PREREG.md:209–231`, committed before any script, lists 15 references, says "Verified on Crossref before this commit", and positions the contest against Müller–Masanes, Hardy–Wootters, McKague–Mosca–Gisin and Renou et al. The `crossref.out` artifact first appears in the results commit, so the logged evidence comes after the scripts. No search procedure (queries, databases) is logged. `theory/composite-contest-2026-11-24/PREREG_2.md` has no prior-art section.

**(3) Is the price of a quantum record stated as a choice with its reason, and does the result flip under the other choice? Stated: confirmed. Flips: yes on the singlet grid, not on H1.**
`theory/composite-contest-2026-11-24/PREREG.md:20–28` rejects mutual information (it is 0 by protocol) and orbit dimension, and adopts Hardy `ln K_AB`, which is not the CORE memory coordinate (`CORE.md:52`: Theorem R1 fixes the memory coordinate as mutual information; A8 is only nonnegative prices).

- Singlet grid under `I_A6` (Shannon MI): every `λ > 0` cell becomes TIE instead of MIXED or LOSE. This was predicted (P6) but never computed.
- Under Holevo χ (equal to MI here, also 0): the same.
- H1 under Holevo: the 6-state copy (`ln 6`) loses to χ = `ln 3`, which flips H1. The minimal 2-state record (`ln 2`) does not flip it (problem 3).

## 4. DOIs: confirmed

All 15 DOIs on added lines (`git diff up/main HEAD | rg '^\+' | rg -o '10\.\d{4,9}/…'`) returned HTTP 200 from `curl https://api.crossref.org/works/<doi>`. Title, first authors and year match the text:

- Müller–Masanes 2013
- Masanes–Müller 2011
- Chiribella–D'Ariano–Perinotti 2011
- Hardy–Wootters 2011
- Barnum–Wilce 2014
- McKague–Mosca–Gisin 2009
- Aleksandrova–Borish–Wootters 2013
- Wootters 2010
- Renou et al. 2021
- Barrett 2007
- Gross–Müller–Colbeck–Dahlsten 2010
- Cirel'son 1980
- Popescu–Rohrlich 1994
- Hardy 2004
- Montina 2008

None failed. Hardy 2001 is correctly left uncited.

## 5. Wording: confirmed

These checks were run with `rg -i` on the added lines:

- "theory of everything", "bill", "kill", "Chad", GR and holography: no hits.
- "law": only in the quoted "(hypothesis)" line.
- "solved": appears only as "resolved" (DOIs). The pivot deviation now says "computed by HiGHS".
- Derivation: "does not claim to derive quantum theory" (`theory/composite-contest-2026-11-24/PREREG.md:17`, memo `:3`).
- The miss is framed as "Puzzle, not a verdict" (`:109`), and model implications are labeled (`:103`).

`git diff --stat up/main HEAD -- THEORY.md` is empty (upstream main `0f37918` is the merge base). THEORY.md is untouched.
