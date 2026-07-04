# 03 — Lensing × Morphology Protocol

## 1. First empirical target

The first proposed Tau Core protocol is:

\[
\delta_L \times \delta_F.
\]

Where:

- \(\delta_L\): lensing residual,
- \(\delta_F\): filament/morphology residual.

## 2. Baseline subtraction

Do not correlate raw lensing with raw morphology.

Use:

\[
\delta_L = L_{obs}-L_{base}.
\]

The baseline should include:

- \(\Lambda\)CDM model,
- baryonic corrections,
- intrinsic alignment,
- survey mask,
- photo-z uncertainty,
- shape noise.

For morphology:

\[
\delta_F = F_{obs}-F_{base}.
\]

The baseline should come from matched mocks or null catalogues.

## 3. Main cross-correlation

\[
C_{LF}(r_\parallel,r_\perp,z)
=
\langle
\delta_L(x,z)\delta_F(x+r,z)
\rangle.
\]

## 4. Parent morphology kernel

A toy filamentary parent kernel:

\[
K_\tau(r_\parallel,r_\perp)
=
A_\tau^2
\exp
\left(
-\frac{r_\parallel^2}{2\ell_\parallel^2}
-
\frac{r_\perp^2}{2\ell_\perp^2}
\right).
\]

Filament condition:

\[
\ell_\parallel>\ell_\perp.
\]

## 5. Required null tests

Required controls:

1. phase randomization,
2. map rotation,
3. orientation randomization,
4. redshift block shuffle,
5. mask-only surrogate,
6. family permutation,
7. independent-parent synthetic null,
8. train/test split.

## 6. Correct interpretation

A morphology/orientation-like signal alone is insufficient.

\[
Z_{\text{orient}}>2
\]

without:

\[
Z_{\text{shared}}>3
\]

must not be treated as Tau Core evidence.

## 7. Real-data class reporting

Use v11 classes:

- A: shared parent + orientation,
- B: shared parent only,
- C: orientation-like only,
- D: null.

Only A and B are Tau Core candidate classes.

C is a warning class, because orientation-like structure can occur in null worlds.

D is null.
