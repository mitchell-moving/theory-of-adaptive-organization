# T81 memo: the record ratio measured as a return flow

*Tuesday 24 November 2026. Self-check, not an independent review. The lock is `PREREG.md` (sha256 `2e31c41bbc175722a421b7547af1670551cf14d5b912a3158d7085b62dff501c`, commit `22993a8`), before `measured_checks.py`. That file was not edited after the commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every number below is in-model.

## Why this approach

Chad's framing, a hypothesis: \(q\) is the share of destruction that comes back to cost whoever did it. T74–T80 inferred a set of prices from a chosen angle. Forge's pivot, open to course-correction, is to measure the flow on a finite reversible walk and to keep T78's open sink as the case where destruction stays gone.

## Can it fail

Can it fail: yes. The collapse, the shape, the fixed point, and the histogram were all able to miss. Three of the scored lines did.

Cheapest way: two reservoirs at one nominal \(x\) whose returns differ by more than \(0.08\).

## Circularity and what could fail

The decoupled clock is not the return. \(\tau_{\mathrm{mix}}\) is \(1/(1-\lambda_2)\) of the environment path with the agent deleted and both ends reflecting. `G-decouple` passes: that matrix and the return restriction differ by \(0.25\) at the contact, and the return row at the contact sums to \(0.75\).

| Check | Could it fail? | What happened |
|---|---|---|
| M1-closed | No. A finite walk that can reach the contact hits it eventually. | holds by construction. At \(N=12\) and \(N=48\), \(q=1\) and \(0.9999999999998\). Not evidence. |
| M1-sink | No. The contact step is absent, so the agent counter stays at 0. | holds by construction. Both horizons print \(0\). Not evidence. |
| M1-scale | Yes. | FAIL. The five returns fall: \(0.081686009166\), \(0.024811974888\), \(0.001090083804\), \(0.000015717030\), \(0.000000000043\). The last gap is \(1.572\times 10^{-5}\), under the locked \(10^{-4}\). The fall is real. The bar on the last step is the miss. |
| M2-collapse | Yes. | PASS. \(\rho=0.052051664190\), under \(0.08\). Eight nominal \(x\) stayed paired. Evidence. |
| M2-shape | Yes. The series is not the chain. | PASS. Maximum gap \(0.006720277156\) on 20 cells, under \(0.08\). Evidence. |
| M2-interior | Yes. | PASS. At \(N=32\), \(q(0.5)=0.095799965060\) and \(q(1)=0.239059227845\), both inside \((0.05,0.95)\). Evidence. |
| M3-conv | Yes. A step map can cycle or split. | PASS. Four interior cells are `POINT`. Five starts agree to 12 decimals. \(\Phi\) width prints as 0. Evidence. Existence of a root was not scored. |
| M3-corner | Yes. A corner can cycle. | PASS. Both corners are `POINT` (\(5.869\times 10^{-6}\) and \(0.866153244874\)). A set would also have passed. |
| M4 | Yes. Closedness need not act only through \(x\). | FAIL. Total variation \(0.909090909091\). Evidence that the pushforward misses. |
| E-pair | Not scored. | Same \(x\), same closedness, two starts: \(0.239059227845\) and \(0.048343059332\), difference \(0.190716168513\). |
| G-gap | Yes. An instrument bar. | FAIL. At \(N=48\) the Jacobi and power clocks differ by \(1.221\times 10^{-8}\), past \(10^{-8}\). Smaller \(N\) sit under the bar. |

`G-equiv` passes with both sides at 0. The locked cell is \(N=12\), \(T=5\), and the start is six sites from the contact, so five steps cannot arrive. The two accountings agree. They do not yet agree on a positive hit.

## NUMERICAL

`measured_checks.out`, `FAILS 3`.

**Model implication.** On this path the cumulative return is a function of \(x=T/\tau_{\mathrm{mix}}\) to within \(0.052\), and the continuum series tracks it to within \(0.0067\). Feeding that return into \(J=I+q P_D+w L\) and iterating gives one point at each locked cell, not a set and not a cycle. The points move with \(x\): \(0.106409485164\), \(0.246706007043\), \(0.422916079022\) at nominal \(x=0.5,1,2\). Stake \(w=1\) and stake \(w=2\) print the same point at \(x=1\).

**M4, puzzle.** For \(c<1\) the decoupled leak time is \(1713\) to \(2741\), so \(x(c)\) sits near \(0.15\) to \(0.24\) and the M2 curve predicts a return under \(0.2\). At \(c=1\), \(x=0.999169215516\) and the curve predicts \(0.226\). The measured fixed points stay near \(0.245\) for every \(c\), because a horizon of one closed-world relaxation does not let the far-end leak change a midpoint hit. Ten predicted masses sit in the first bin and the measurements sit in the second. Closedness did not act as a pure rescaling of \(x\).

**E-pair, not scored.** Two equally closed worlds at the same \(x\) do not share \(q\) once the start moves from the middle to the far site. The scored collapse is inside one start rule.

## Report, not scored

Distances to the T79 singleton \(0.30\) and to the parent's root \(0.6\):

| cell | \(q^\star\) | to \(0.30\) | to \(0.6\) |
|---|---|---|---|
| m3-a | \(0.106409485164\) | \(0.193590514836\) | \(0.493590514836\) |
| m3-b | \(0.246706007043\) | \(0.053293992957\) | \(0.353293992957\) |
| m3-c | \(0.422916079022\) | \(0.122916079022\) | \(0.177083920978\) |
| m3-d | \(0.246706007043\) | \(0.053293992957\) | \(0.353293992957\) |

Neither figure was a target. The nearest approach to \(0.30\) is \(0.053\). The nearest approach to \(0.6\) is \(0.177\).

## Errata

None. The lock was not edited.
