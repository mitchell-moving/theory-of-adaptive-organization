# Does the cost of judgment on a fractal world scale with dimension?

*Sunday 22 November 2026. A self-check, not an independent review. The lock is `theory/fractal_checks/PREREG.md`, commit `5da0f73`, and that file was not edited after the script ran. Checks: `theory/fractal_checks/fractal_checks.py`, run at `nice -n 19`. 161 required checks passed, 0 required checks failed, 4 open misses. The fetched records are `theory/fractal_checks/crossref.out`.*

*Status against current main (23 November 2026). Proposed for main as the follow-up to `theory/HOLOGRAPHIC_2026-11-22.md` on Sierpiński graphs. The lock, the script, and the numbers are unchanged. Labels stay as in §5: identities that the locked script checks are **PROVED** (in-model, class F, code-checked); a dimension law for the cost is **FAILS**; four locked bands remain open misses. This is still a self-check, not an independent review. OPEN_WORK T54 is that review and those open misses.*

The hypothesis sentence is unchanged:

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

## 0. The answer

On these graphs the minimum cost scales with the sites the decision names. It does not scale with the Hausdorff dimension or the spectral dimension.

The field is the equilibrium Gaussian field of the holographic note, \(Q=\alpha I+\beta L\), with \(kT=\alpha=\beta=1\) and tolerance \(\varepsilon=1/18\). The heat floor of holding every mode at that tolerance is \(N/\varepsilon-\operatorname{tr}(Q)\). The trace is the degree sum. Two fractals and the square lattice therefore share one formula, \(17\) minus the mean degree:

| World | Mean degree in the limit | Cost per site in the limit | At the largest locked size |
|---|---|---|---|
| Sierpiński gasket | 4 | 13 | \(N=1095\), cost \(14241\), per site \(13.005479452055\) |
| Periodic square | 4 | 13 | \(n=16\), cost \(3328\), per site \(13\) |
| Sierpiński carpet | \(3.2\) | \(13.8\) | \(N=4096\), cost \(56784\), per site \(13.86328125\) |

The gasket matches the lattice. The carpet is higher by the bonds the holes remove, \(4-3.2=0.8\). Neither gap is \(d_s\) or \(d_f\). At gasket generation 6 the per-site cost differs from \(13\cdot d_s/2=8.873881\) by \(4.132\) and from \(13\cdot d_f/2=10.302256\) by \(2.703\).

A decision that names only the outer boundary pays for those sites. On the gasket the boundary is the three corners at every generation, the lower bound is \(45\), and the achieved uniform load settles at \(46.936432434714\) (ratio \(1.043032\) to the bound) from generation 4 through generation 6. The all-site cost at generation 6 is \(14241\). On the carpet the bound is \(172\cdot 3^{n-1}-52\), and the achieved load tracks it: ratios \(1.007385\), \(1.042121\), \(1.050481\), \(1.053014\) at generations \(1\) through \(4\). The power \(d_b/d_f-1\) is the power of \((\text{boundary count})/N\). It is not a second factor on the cost per named site.

The spectral dimension is real, and it is a fact about the Laplacian, not a factor in the heat. The gap ratio moves toward \(5\). The counting function on generation 6 ends at the step \(\log 3/\log 5=0.682606\). The heat of the \(47\) modes in \((0,0.2]\) is \(794.925887\), and \(794.925887\cdot d_s/2=542.621\) is a different number.

The layer count depends on the mass. At the holographic mass \(\alpha=1\), rates are \(1+\lambda\) and a stake ratio \(1.44\) compresses four decimation bins and \(48\) modes into layer-count \(1\) under both locked formulas. At \(\alpha=10^{-8}\) the equilibrium formula \(K_E=\lfloor\log R/\log 25\rfloor+1\) equals the bin count \(4\), and the unsquared formula \(K_U=\lfloor\log R/\log 5\rfloor+1\) equals \(7\). The count that matches is the number of ratio-\(5\) bins in the window. It does not multiply the cost of each mode, and it is not the generation index.

The spatial mean, held at half its prior variance, costs \(1\) on every graph that was checked.

## 1. What this is not

The repository already had a fractal question, and it was about time. `theory/HT_INDEX.md`, the conditional statement kept with T7, the withdrawn framing N46, and the T20 check are about the spectrum of a scalar process. A search before the lock found no Sierpiński graph and no spectral dimension of a Laplacian. This note is the geometry of the domain.

Canyellas, Liu, Arouca, Eek, Wang, Yin, Guan, Li, Wang, Zheng, Liu, Jia, and Morais Smith, Nature Physics **20**, 1421–1428 (2024), doi `10.1038/s41567-024-02551-8`, Crossref HTTP 200 on 22 November 2026. The Crossref record has no abstract. The arXiv record `2309.09860v2`, HTTP 200 the same day, says that edge and corner modes arise in Sierpiński triangles formed by bismuth deposited on indium antimonide. **KNOWN** as that fetched statement. Nothing in either record is a heat floor. Reading those edge modes as this cost is **METAPHOR**.

The cost equation is the one already proved for an equilibrium Ornstein–Uhlenbeck mode (IP11, IP12) and for a designated cut (`theory/HOLOGRAPHIC_2026-11-22.md`: bound \(13\) per cut site, achieved about \(13.61\)). Class F is that equation on the graphs named in the lock. This note does not edit `THEORY.md`, `CORE.md`, or `README.md`.

## 2. Every site

**PROVED (class F, code-checked).** Degree sums, edge counts, and corner distances match the lock on every locked graph. The heats match to the printed identity.

Gasket, cost \(13N+6\):

| Generation | \(N\) | Cost | Per site |
|---|---|---|---|
| 0 | 3 | 45 | 15 |
| 1 | 6 | 84 | 14 |
| 2 | 15 | 201 | 13.4 |
| 3 | 42 | 552 | 13.142857142857 |
| 4 | 123 | 1605 | 13.048780487805 |
| 5 | 366 | 4764 | 13.016393442623 |
| 6 | 1095 | 14241 | 13.005479452055 |

The log-log slope on generations \(3\) through \(6\) is \(0.996878303620\), standard error \(9.537\times 10^{-4}\), against the locked value of the same four heats.

Carpet, cost \(\tfrac{69}{5}N+\tfrac{16}{5}\,3^n\):

| Generation | \(N\) | Edges | Cost | Per site |
|---|---|---|---|---|
| 1 | 8 | 8 | 120 | 15 |
| 2 | 64 | 88 | 912 | 14.25 |
| 3 | 512 | 776 | 7152 | 13.96875 |
| 4 | 4096 | 6424 | 56784 | 13.86328125 |

Periodic square: costs \(208\), \(832\), \(3328\) at sides \(4\), \(8\), \(16\), which is \(13N\). Periodic path: \(60\), \(120\), \(240\), which is \(15N\). Open square: \(224\), \(864\), \(1920\), \(3392\) at sides \(4\), \(8\), \(12\), \(16\), which is \(13n^2+4n\).

**FAILS** as a claim that the per-site cost scales with \(d_s\) or \(d_f\). The gasket and the degree-4 lattice have different dimensions and the same limit \(13\).

**Open miss, the carpet band.** The lock asks for \(|\text{per site}-13.8|<0.01\) at generation \(4\), and the same lock states the excess \(3.2\,(3/8)^n\). At generation \(4\) that excess is \(0.06328125\), and the code returns \(13.86328125\). The band and the closed form cannot hold together. Next test, degree sum only, outside the lock: generation \(5\) has \(52040\) edges against the same formula, cost \(452976\), per site \(13.823730468750\), excess \(0.023730468750\); generation \(6\) has \(418264\) edges, cost \(3619920\), per site \(13.808898925781\), excess \(0.008898925781\), which is under \(0.01\). The identity was already the result. The band arrives two generations later.

**Open miss, the carpet Hausdorff gap.** The lock asks the gap from \(13.8\cdot d_f/2\) to exceed \(2\). The code's gap is \(0.803035\) (alternative \(13.060246\)). At the limit the gap is \(0.739754\), because \(d_f/2=0.946395\). No generation can clear a gap of \(2\). The spectral-dimension comparison does clear it: gap \(4.443316\) from \(9.419965\). The cost that the identity returns is \(17\) minus the mean degree. It is not \(13.8\cdot d_f/2\).

## 3. Only the boundary

**PROVED (class F, code-checked) as the named-site bound. METAPHOR if it is called a dimension law.**

Gasket corners, bound \(45\) at all seven generations. Achieved uniform load:

| Generation | Achieved | Ratio to 45 |
|---|---|---|
| 0 | \(45.350531909421\) | \(1.007790\) |
| 1 | \(46.718141226766\) | \(1.038181\) |
| 2 | \(46.932758339621\) | \(1.042950\) |
| 3 | \(46.936431631247\) | \(1.043032\) |
| 4–6 | \(46.936432434714\) | \(1.043032\) |

Generation \(0\) matches the locked closed form \((39+9\sqrt{33})/2\). The log-log slope of the achieved cost on generations \(2\) through \(6\) is \(0.000014\). A volume slope of \(1\) is not this number. Every ratio is under the locked tolerance \(1.15\).

Carpet outer boundary, bound \(120\), \(464\), \(1496\), \(4592\). Achieved \(120.886162\), \(483.544257\), \(1571.518835\), \(4835.442568\). Slope of \(\log(\text{bound})\) on \(\log B\) is \(0.988226953947\). Slope of \(\log(\text{achieved}/N)\) on \(\log N\) for generations \(2\) through \(4\) is \(-0.44634532\), inside \(0.05\) of \(-0.471679166426\). The bound's own slope on those three sizes is \(-0.44884568\).

Open square, bound \(172\), \(396\), \(620\), \(844\). Achieved \(181.289987\), \(423.010530\), \(664.730833\), \(906.451136\), ratios \(1.054012\), \(1.068208\), \(1.072147\), \(1.073994\). Slope of \(\log(\text{bound}/N)\) on \(\log N\) is \(-0.425058011513\), the locked finite-sample slope, \(0.075\) away from \(-1/2\) because the exact bound is \(56 N^{-1/2}-52 N^{-1}\).

The per-named-site achieved cost stays near \(15\) to \(16\). The holographic column, about \(13.61\) against a bound of \(13\), is the same construction on a different cut. Depth and dimension do not enter after the named sites and their degrees are counted.

## 4. The aggregate, the spectrum, and the layers

**Spatial mean. PROVED (class F, code-checked).** \(Q\mathbf 1=\mathbf 1\) on the graphs that were checked, \(1^{\top}Q^{-1}1=N\), and the half-prior cost of the mean is \(1\). Checked on the gasket at generations \(0\) and \(6\) (mean variances \(1/3\) and \(1/1095\)), on the carpet at generations \(1\) and \(4\), and on the open square at side \(16\).

**Slow modes. PROVED as the partial sum. FAILS as a \(d_s\) multiplier.** On gasket generation \(6\), \(47\) Laplacian eigenvalues lie in \((0,0.2]\). Their heat is \(794.925887441137\), matching the eigenvalues of \(Q\) in \((1,1.2]\). Multiplying by \(d_s/2\) produces \(542.621335\).

The counting function at \(5^{-4},5^{-3},5^{-2},5^{-1}\) is \(3,6,16,48\). Successive exponents: \(0.430677\), \(0.609423\), \(0.682606\). The last step is \(\log 3/\log 5\). The four-point slope is \(0.577754\), standard error \(0.0405\), inside the locked tolerance \(0.15\) of \(0.682606\). The early bins hold \(3\) and \(6\) modes, which pulls the fit down. The lattice control, exact eigenvalues, has slopes \(1.083170\), \(0.921414\), \(0.987078\) at sides \(32\), \(64\), \(128\), all inside \(0.15\) of \(1\).

**Gap ratio. The slope gate passes. Two early ratios are open misses.** Smallest positive Laplacian eigenvalues, generations \(0\) through \(6\): \(3\), \(1.69722436\), \(0.570310139\), \(0.134538029\), \(0.0282705251\), \(0.00574195847\), \(0.00115409405\). Ratios of generation \(g\) to \(g+1\) for \(g=3,4,5\): \(4.75895047\), \(4.92349870\), \(4.97529509\). The lock asks each to lie within \(0.05\) of \(5\). Generations \(3\) and \(4\) miss, by \(0.241\) and \(0.076\). Generation \(5\) is inside. The slope of \(\log\lambda_1\) on generations \(3\) through \(6\) is \(-1.58696131\), standard error \(0.00722\), inside \(0.05\) of \(-\log 5=-1.60943791\). The lattice gaps at sides \(16,32,64,128\) reproduce the locked slope \(-1.994169933238\), toward \(-2\), and the doubling ratios are \(3.961571\), \(3.990369\), \(3.997591\), toward \(4\).

Next test, outside the lock: generation \(7\) has \(N=3282\) and \(\lambda_1=2.31192288\times 10^{-4}\). The ratio from generation \(6\) is \(4.99192279\), and \(|\text{ratio}-5|=0.008077\). The approach is monotone and the \(0.05\) band holds one generation after the lock's first miss. The cost identity does not use this ratio.

**Layers.** Locked arithmetic: \(K_U(R)\) is \(2,3,4,5,6,7\) and \(K_E(R)\) is \(1,2,2,3,3,4\) at stake ratios \(5,25,125,625,3125,15625\).

At \(\alpha=1\), generation \(6\), stake \(1.44\): \(K_U=K_E=1\), while \(M=48\) modes have rate at most \(1.2\) and \(4\) ratio-\(5\) bins meet \((0,0.2]\). The heat of those \(48\) modes is \(811.925887441137\). **FAILS** as a claim that either layer formula counts the modes, or the bins, when the mass sits on top of the hierarchy. The rates are \(1+\lambda\). A factor \(5\) in a small eigenvalue is not a factor \(5\) in the rate.

At \(\alpha=10^{-8}\), \(\lambda_1=1.15409405\times 10^{-3}\), window up to \(0.2\), stake ratio \(R=3.003102\times 10^{4}\). Bin count \(4\), \(K_E=4\), \(K_U=7\). **PROVED (class F, code-checked)** for this one window: the equilibrium threshold \(w=a^2\) makes the bin count \(\lfloor\log R/\log 25\rfloor+1\). **FAILS** for \(\lfloor\log R/\log 5\rfloor+1\), which overshoots by \(3\). The matching count is four bins, not six generations. It does not change the per-mode heat.

## 5. Labels

| Claim | Label |
|---|---|
| All-site cost \(=N/\varepsilon-\operatorname{tr}(Q)\), hence \(13N+6\) on the gasket and \(\tfrac{69}{5}N+\tfrac{16}{5}3^n\) on the carpet | **PROVED** (class F, code-checked) |
| That cost scales with \(d_s\) or \(d_f\) rather than with \(N\) and the degree sum | **FAILS** |
| Boundary cost is the named-site bound, achieved within \(1.15\) on every locked graph | **PROVED** (class F, code-checked) as the bound and the load; **METAPHOR** as a dimension law |
| Spatial mean at half its prior variance costs \(1\) | **PROVED** (class F, code-checked) |
| Heat of a set of modes equals the partial sum, with no \(d_s\) factor | **PROVED** (class F, code-checked). A \(d_s\) factor **FAILS** (\(794.926\) against \(542.621\)) |
| Gap ratio within \(0.05\) of \(5\) at generations \(3\) and \(4\) | Open miss. Generation \(5\) is inside. Generation \(7\), outside the lock, is inside |
| Counting-function slope within \(0.15\) of \(\log 3/\log 5\) | Inside the tolerance. The last step equals the target. Not a cost factor |
| \(K_U=\lfloor\log R/\log 5\rfloor+1\) counts the decimation bins of this equilibrium field | **FAILS** on both arms |
| \(K_E=\lfloor\log R/\log 25\rfloor+1\) counts those bins at \(\alpha=10^{-8}\) in the locked window | **PROVED** (class F, code-checked) for that window |
| Edge and corner modes of bismuth on indium antimonide | **KNOWN** from the fetched records. Not this heat |

## 6. What is still open

The four open misses (printed by the script as `PUZZLE`) are the two early gap ratios, the generation-\(4\) carpet band, and the impossible gap of \(2\) against \(13.8\cdot d_f/2\). The next tests named for the first two have been run and are in §2 and §4. They do not reopen the identities.

Not done, and not claimed: a continuum diffusion on the gasket, a non-Gaussian field, a decision whose loss is not a mean square, and any identification of the bismuth experiment with this cost. The carpet's spectral dimension was not a target. The equation in THEORY is unchanged.
