# M4 design pass: can locality arise from the cost? Prior art, a desk check, and a judgment

*Friday 27 November 2026 (EST). Prereg PREREG_M4_DESK_2026-11-27.md, SHA-256 34be3a6d5f570286d77e0f9bddb8ba149599accb9b04e086188e37f744bf8129, locked 00:25:20 EST. Output: m4_desk.out. Labels as before. No physics is derived or claimed.*

## Prior art (Crossref-verified, crossref_m4.out)
- **Emergent locality from a designed graph Hamiltonian:** Konopka, Markopoulou & Severini 2008, PRD 77:104029, doi 10.1103/PhysRevD.77.104029 (arXiv 0801.0861). Low-valence, local graphs come from chosen energy terms, so the input is moved (W13).
- **Geometry from entanglement structure:** Van Raamsdonk 2010, GRG 42:2323, doi 10.1007/s10714-010-1034-0; Cao, Carroll & Michalakis 2017, PRD 95:024031, doi 10.1103/PhysRevD.95.024031. Here geometry is read off a given state's correlation pattern.
- **Network geometry:** Krioukov et al. 2010, PRE 82:036106, doi 10.1103/PhysRevE.82.036106 (hidden hyperbolic metric); Bianconi & Rahmede 2016, PRE 93:032315, doi 10.1103/PhysRevE.93.032315.
- **Spatial networks: structure follows distance-dependent link costs.** Barthélemy 2011, Phys. Rep. 499:1, doi 10.1016/j.physrep.2010.11.002.
- **Small-world shortcuts:** Watts & Strogatz 1998, Nature 393:440, doi 10.1038/30918.
- **Selection on given graphs:** Lieberman, Hauert & Nowak 2005, Nature 433:312, doi 10.1038/nature03204.
- **Dimension:** Tegmark 1997, CQG 14:L69, doi 10.1088/0264-9381/14/4/002 (3+1 from stability, an anthropic argument); Ambjørn, Jurkiewicz & Loll 2005, PRL 95:171301, doi 10.1103/PhysRevLett.95.171301 (scale-dependent spectral dimension in CDT).

## Desk check (in-model, 144 judges; cost = link upkeep + need × hops; greedy selection)
| world | seeds | links | diameter | spectral dimension d_s | prediction | score |
|---|---|---|---|---|---|---|
| calibration: 12×12 grid | – | – | – | 1.92 (valid) | – | – |
| calibration: random graph | – | – | – | 4.64 | – | – |
| uniform need | 1–3 | 392–400 | 4 | 7.81–7.98 | D1: no low-dimensional locality | **PASS 3/3** |
| need from hidden 2D positions | 1–3 | 415–442 | 5 | 7.28–7.71 | D2: low-dimensional (1.5–3) | **FAIL 0/3** |

## Hostile review
1. **D1 passing is close to known.** Without a metric, cost-optimal graphs are shortcut-rich (Watts–Strogatz; Barthélemy).
2. **D2 failed, so my prediction was wrong.** Even when *need* is local, link upkeep plus hop lateness favors shortcuts, and the graph comes out high-dimensional (d_s ≈ 7.5). Post hoc, and consistent with Barthélemy: a low-dimensional graph needs link **prices** that grow with distance in a pre-existing space. Local need alone is not enough. This is not preregistered.
3. **Prices, search and size are all limited.** One price pair (L 40, w 1), greedy search, N 144, and the d_s estimator is coarse on small graphs (calibrated, but rough).
4. **Scope.** This checks a recorded wall; it is not a new result.

## Judgment on the physics route (M4 and beyond)
- **In-model:** the GTAO cost does not create locality. It does not create it from uniform need, and it does not even inherit it from local need at these prices. Locality appears to require a metric already built into link prices. "Locality stays an input" is now supported in-model, more strongly than before.
- Every published route from a cost to gravity's form (Jacobson, Verlinde, inverse-square via Gauss's theorem) needs locality and three dimensions as inputs. M4 therefore blocks them, and so do M2 and M3 (W8, W6).
- **EIV of further M4 work:** a variant with distance-dependent link prices would reproduce the input (W13). A search for a cost that *chooses* a dimension would need a price ratio tuned to give 3 (W2). Either way, p(a failable, non-known result) ≤ 0.05, EIV ×0.6 ≈ 0.01 bits for several hours. That is below the hold price λ 0.02 bits/h.
