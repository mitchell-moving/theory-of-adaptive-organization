# Addendum: contestants that can leave the lemmas

*Tuesday 24 November 2026. Committed before any script for this addendum. `PREREG.md`, `PREREG_R2.md`, `PREREG_2.md`, `PREREG_3.md`, and their stored outputs are not edited. This addendum does not derive quantum theory.*

The third review found that the tilted-menu replacements recompute the lemmas. This addendum scores different model classes. The price stays Hardy `λ ln K_AB`. The stake stays the mean of the 25 squared errors. `ε = 0`. `λ` is the same five values. Tie band unchanged. No random seed.

## Models

**G.** States are a two-qubit density matrix plus a coordinate `η` that is not one of the 16 product-Pauli expectations. The scored menu is product Paulis. The joint effect `(1+η)/2` is computed and is not scored.

**Gmin.** Minimal tensor product: correlators `(n·u)(m·v)` with Bloch vectors in the unit ball. Powell, the fixed starts in the script, at most 80 iterations.

**Gmax.** Maximal tensor product of the two local state spaces, not the orbit of a product under local rotations. A behavior with correlator `T` and nonnegative product-effect probabilities is inside that set. `K = 16`. This is the departure from `PREREG.md` §4, which granted Gmax only local rotations.

**H.** Mean loss of a Frank–Wolfe run on the 1024 local vertices. Uniform start, step `2/(k+2)`, 2000 iterations. The squared worst-entry error is stored and is not the stake.

**R4a.** Its own phase space. Each wing has `q ∈ {0,1}` and `p ∈ {+1,−1}`. The outcome of menu vector `u` is `p` when `|u_x (1 if q = 0 else −1) + u_z| < 10^{-12}`, and otherwise `p` times the sign of that quantity. Frank–Wolfe on the 16 joint atoms, uniform start, 500 iterations. `K` is the number of atoms with weight above `10^{-8}`.

**R4c.** The real plane of `lemmas.py`: real and imaginary parts of the singlet, and the Born weight on the plane spanned by `φ_R` and `J φ_R`. Not the complex modulus.

**Witness.** For each model, the scored `yy` entry of that model's correlator. Not the mean of `p(−p)`.

**Information.** Mutual information of the 25 settings with a one-point record, from the entropies of the explicit product distribution. Holevo of that one state, from its eigenvalues. The claim that either number separates contestants is dropped.

## Predictions, and the input that fails each one

- **P-span.** The product Paulis span 16 real dimensions. Fails if that rank is not 16.
- **P-blind.** The scored correlator at `η = 1` matches `η = 0` to `10^{-12}`. Fails if any entry moves by more. Then this menu cannot tell the complex record from that extension except by dimension. That comparison is a puzzle, not a pass.
- **P-gmax.** Every product-effect probability of the singlet is at least `−10^{-9}`, so Gmax has loss at most `10^{-8}` at `K = 16`. Fails if a product probability is below `−10^{-9}`. Then every positive-price cell is TIE, not WIN.
- **P-gmin.** Gmin's loss is at least `1/25 − 10^{-6}`. Fails if the fit returns less.
- **P-r4c.** The real-plane loss is at most `10^{-8}`. Fails if it returns more.
- **P-H.** H's mean loss is at least `(3−2√2)/25 − 10^{-4}`. Fails if Frank–Wolfe returns less.
- **P-r4a.** R4a's stored loss is not H's stored loss. Fails if the two numbers are one variable.
- **P-wit.** Some model's `yy` correlator differs from `−1` by more than `10^{-3}`. Fails if every model reports `−1`.
- **P-mi.** The computed mutual information is at most `10^{-12}`. Fails if the entropy sum returns more.
- **P-k.** Where both losses are under `10^{-8}`, the sensitivity at `K = 16` is TIE and at `K = 15` is LOSE for every positive price. Fails if a printed label differs.

**Headline of this addendum.** If P-gmax holds, the positive-price cell is not WIN. If P-gmax fails, that headline is withdrawn and the cell is re-read.
