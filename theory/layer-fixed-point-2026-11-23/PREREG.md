# PREREG: does CT34 nesting have a renormalization fixed point?

*Tuesday 24 November 2026. Locked before any script that produces a result. The claim under test is a **CONJECTURE**. `THEORY.md` is not edited. Nothing here is a hypothesis about nature, and nothing is compared to a measured physical constant.*

Branch `ace-probe-memos-2026-11-23` at `e3e0e70116fc9cabce11af7e1c25d93d18405b0b` is cited and not merged. Its memo `theory/probes-2026-11-23/MIRROR_MEMO.md` §6 conjectures that a fixed point of a nested-layer map would be a dimensionless number in the sense of Feigenbaum's δ. The independent review `theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md` (reviews outrank memos) leaves that row as **CONJECTURE, untested**, and finds no route from this cost to a running coupling. This preregistration tests only the fixed-point question.

## 0. What would count

Feigenbaum's δ is the expanding eigenvalue of the period-doubling operator at its fixed function (Feigenbaum 1978, 1979; Coullet and Tresser 1978; a computer-assisted proof, Lanford 1982). It is not an exponent fixed by dimensional analysis. The clock-term onsets 6 and 4 (`theory/CLOCK_TERM_2026-11-23.md`, the fixed-price onset and the information-priced onset of 4κ/λ nats) are the other kind: the only dimensionless group left by a scale symmetry. Those onsets are not the object here.

A **SUPPORT** outcome is one number ρ, read off the nesting operator below, with |ρ| ≥ 1.05, the same to 0.02 across the locked deformations, the locked fit windows, the finite-difference check, and the two locked cap strengths. Anything else is a **puzzle** with a named cell, and the next step is a diagnosis.

Odds, stated before the run, as a judgment and not a result: about 1 in 10 that the cell is SUPPORT. The cost's own two-power family is proved below to be superattractive (multiplier 0). An expanding direction has to live outside that family and still be forced by the cost.

## 1. The cost and the operator

**Cost.** CT22 on the scalar path (`THEORY.md` B.9, the paragraph that sets α = wσ²/2 and β = w²σ⁴/3). The reserve's own noise is off, so the fluctuation is the tracking loss. Then β = (4/3)α², and

\[
J(\tau)=\frac{c}{\tau}+\alpha\tau,\qquad s^2(\tau)=\frac{4}{3}\alpha^2\tau^3,\qquad \theta=\frac{2(y-J)}{s^2}.
\]

Time unit τ_E = √(c/α), cost-rate unit J_1 = √(cα). In those units the expected cost rate is

\[
f_*(t)=t+\frac{1}{t},\qquad V_*(t)=\frac{4}{3}t^3,\qquad \Theta(t)=\frac{2(\hat y-f(t))}{V(t)}.
\]

The ruin cap stays outside the sum (`CORE.md` lines 27 and 66). Nonnegative prices are A8 (`CORE.md` line 52); this note does not use the memory coordinate beyond that.

**Nesting.** CT34 (`THEORY.md` B.10): min_{x,y}[F(x)+G(y;θ(x))] = min_x[F(x)+J*_T(θ(x))]. The dyadic reading used here, declared as the period-doubling analogue and not as a theorem of CT34: the team is the same cost at the parent's time divided by an integer b, and the parent fixes that clock before the team is scored. With b = 2 (primary) and b = 3 (reported beside it, not required to agree):

\[
F_f(t)=f(t)+f(t/b).
\]

Currency and time are the two units. Let t_0 = argmin_{t>0} F_f(t) and F_0 = F_f(t_0). The slack operator is

\[
(Tf)(u)=\frac{2 F_f(t_0 u)}{F_0}.
\]

**Lemma A (hand; the script only checks it).** If f(t) = A t + B/t with A, B > 0, then (Tf)(u) = u + 1/u for every b > 0. In particular T f_* = f_*, and one application erases (A, B). On this family the multiplier is 0. Proof: F(t) = A(1+1/b)t + B(1+b)/t, the minimizer is t_0 = √(b B/A), and F(t_0 u)/F(t_0) = (u + 1/u)/2.

**Lemma B (hand; the script only checks it).** At that minimizer for A = B = 1, F_0 = 2(1+b)/√b. For b = 2 this is 3√2 ≈ 4.24, which is greater than 2. Two copies at the same J_1 therefore cannot be a fixed point of an income rescaling that divides costs by F_0/2 and asks the income to come back unchanged: the renormalized income is at most half the old one. Same-scale copies are not a fixed point.

**Why a nontrivial number is still possible.** Lemma A is the tangent to one family. A deformation φ that is not of the form A t + B/t can have a Rayleigh quotient |ρ| ≥ 1.05 under DT, because the shift-sum φ(t)+φ(t/b) multiplies a log-mode of order k by a factor that depends on k (1 + b^{−k} before the normalization). The normalization is nonlinear. It can leave one direction expanding. That is the same mechanism as δ, and it is not guaranteed.

**Cap.** Variances add for two layers that share the reserve and have the same α in the coarse layer's units (`THEORY.md` writes s² = s_0² + βτ³; here s_0 = 0 and the fine interval is τ/b):

\[
V(t)=\frac{4}{3}\Big(t^3+(t/b)^3\Big),\qquad \Theta(t)=\frac{2(\hat y-F(t))}{V(t)}.
\]

The income is not a free fit. For a locked q it is the marginal income of the base shape f_*, computed at the unconstrained minimizer t_c of F_{f_*}:

\[
\hat y = F_{f_*}(t_c)+\frac{q}{2}V(t_c).
\]

The binding operator uses the same formula as T, with t_0 replaced by the minimizer of F on {t : Θ(t) ≥ q and F(t) < ŷ}. If that point is the critical point, the operator agrees with T.

## 2. What is computed

Deformations, all even in z = ln t, so a pure shift of the minimum is not smuggled in:

- φ_1(t) = t³ + t⁻³
- φ_2(t) = t⁵ + t⁻⁵
- φ_3(t) = exp(−(ln t)²)

Coefficient s = 10⁻⁴, checked at s = 10⁻⁵. Fit windows, trapezoid (equal weights) on a uniform z-grid: (Z, N) = (2, 64) and (3, 96). The argmin itself is a golden section on ln t ∈ [−8, 8], tolerance 10⁻¹⁴, and does not use the fit window.

Rayleigh quotient of a deformation:

\[
\rho(\varphi)=\frac{\langle Tf_s-f_*,\varphi\rangle}{s\,\langle\varphi,\varphi\rangle},\qquad f_s=f_*+s\varphi.
\]

**Cells for b = 2.**

| Cell | Rule |
|---|---|
| S1 | max_u \|T f_* − f_*\| < 10⁻¹² on the coarse window |
| S2 | Lemma A on the five pairs (A, B) = (1, 1), (0.3, 2), (4, 0.5), (1, 3), (2, 2), residual < 10⁻⁸, and Lemma B's F_0 = 3√2 for b = 2 |
| SUPPORT | S1 and S2 pass; the three slack ρ agree with their mean to 0.02; \|mean ρ\| ≥ 1.05; the mean agrees across the two windows to 0.02; s = 10⁻⁴ and s = 10⁻⁵ agree to 0.02; both q ∈ {0.5, 2} give a mean ρ within 0.02 of the slack mean; f_* + 10⁻⁴ φ_1 has positive second derivative on the coarse grid |
| CONTRACTING | S1, S2 pass and every \|ρ\| < 1.05 |
| MODE_DEPENDENT | the three slack ρ on the coarse window differ by more than 0.02 |
| CUTOFF | windows, or the two step sizes, differ by more than 0.02 |
| CAP_DEPENDENT | slack would support, but a locked q moves the mean by more than 0.02 |
| NONCONVEX | the φ_1 check loses f'' > 0 |
| BROKEN | S1 or S2 fails; do not interpret ρ |

The first matching failure in the order BROKEN, NONCONVEX, CUTOFF, MODE_DEPENDENT, CONTRACTING, CAP_DEPENDENT wins. Otherwise SUPPORT. b = 3 is printed and is not part of the cell. Thresholds live in `criteria.json` beside this file. The script reads that file and does not restate them.

Effect size: 0.02 absolute on ρ. That resolves an O(1) number and does not treat a 5 percent wiggle about 1 as expansion (|ρ| ≥ 1.05).

No seed. No sweep beyond the locked list.

## 3. Analysis plan

One script, `nest_map.py`. It writes `nest_map.out` and `nest_map.json`. Pytest reruns it and checks the cell against the locked rules. If the cell is not SUPPORT, the memo names the assumption the cell points at, and a later preregistration changes that assumption. This file is not edited after the run.

## 4. Checkpoint, before any run

1. **Still the right question?** Yes. The conjecture names an eigenvalue of a nesting operator, not an EOQ share and not a fold exponent. Lemma A says the EOQ share's family has multiplier 0. That lemma is a check, not a substitute question.
2. **Is the answer built in?** The normalization uses currency and time only. b = 2 is the doubling analogue; b = 3 is reported and cannot flip the cell. q is the pair {0.5, 2}, not a searched value. A ρ that moves when the fit window moves is CUTOFF, so the window cannot be tuned into a number. Adding φ_1, φ_2, φ_3 asks whether one number is forced; it does not pick the prettiest mode after the fact.
3. **A cheaper test?** Lemma A is the cheaper test and is S2. It cannot see the complement of A t + B/t. Three Rayleigh quotients are the smallest set that can tell one expanding direction from a menu of mode-dependent rates.

## 5. Prior art

DOIs checked on Crossref on 24 November 2026 (`crossref.out`).

- Feigenbaum, M. J. 1978. Quantitative universality for a class of nonlinear transformations. *Journal of Statistical Physics* 19:25–52. doi 10.1007/BF01020332.
- Feigenbaum, M. J. 1979. The universal metric properties of nonlinear transformations. *Journal of Statistical Physics* 21:669–706. doi 10.1007/BF01107909.
- Coullet, P. and Tresser, C. 1978. Itérations d'endomorphismes et groupe de renormalisation. *Le Journal de Physique Colloques* 39:C5-25–C5-28. doi 10.1051/jphyscol:1978513.
- Lanford, O. E. III. 1982. A computer-assisted proof of the Feigenbaum conjectures. *Bulletin of the American Mathematical Society* 6:427–435. doi 10.1090/S0273-0979-1982-15008-X.
- Wilson, K. G. 1971. Renormalization group and critical phenomena. I. *Physical Review B* 4:3174–3183. doi 10.1103/PhysRevB.4.3174.
- Wilson, K. 1974. The renormalization group and the ε expansion. *Physics Reports* 12:75–199. doi 10.1016/0370-1573(74)90023-4. (Crossref lists one author.)
- Chou, K. C., Willsky, A. S. and Benveniste, A. 1994. Multiscale recursive estimation, data fusion, and regularization. *IEEE Transactions on Automatic Control* 39:464–478. doi 10.1109/9.280746.
- Simon, H. A. and Ando, A. 1961. Aggregation of variables in dynamic systems. *Econometrica* 29:111. doi 10.2307/1909285. (Crossref page field is 111.)
- Dantzig, G. B. and Wolfe, P. 1960. Decomposition principle for linear programs. *Operations Research* 8:101–111. doi 10.1287/opre.8.1.101.
- Geoffrion, A. M. 1970. Elements of large-scale mathematical programming. *Management Science* 16:652–675. doi 10.1287/mnsc.16.11.652.

CT34 already credits partial minimization to Dantzig and Wolfe and to Geoffrion, and near-decomposability to Simon and Ando. Chou, Willsky and Benveniste is the hierarchical-estimation analogue: a multiscale recursion for a state, not a fixed-point number for this cost. None of these sources states the operator in §1.
