# Tau Core Readout Covariance Package

## Status

This package is a **synthetic validation and formalization package**, not empirical cosmological proof.

It integrates the Tau Core parent–readout framework with the v8–v12 synthetic tests:

- parent/readout positivity formalism,
- multi-readout covariance,
- lensing × morphology synthetic demonstrator,
- v8 shared-parent detector,
- v9 matched-filter rejection,
- v10 orientation diagnostic,
- v11 two-axis classifier,
- v12 synthetic validation report.

## Central claim

Tau Core should be tested as a **multi-axis readout-covariance programme**, not as a single anomaly detector.

\[
\boxed{
\text{Shared-parent covariance is primary; morphology/orientation is secondary.}
}
\]

## Package structure

```text
taucore_readout_covariance_package/
  README.md
  MANIFEST.json
  docs/
    01_readout_positivity_and_parent_formalism.md
    02_multi_readout_covariance.md
    03_lensing_morphology_protocol.md
    04_synthetic_validation_report_v12.md
    05_claim_boundaries_and_attack_surface.md
  code/
    taucore_v8_synthetic_lensing_morphology.py
    taucore_v11_two_axis_classifier.py
  results/
    tables/
      *.csv
    figures/
      *.png
```

## Main synthetic result

The v11 two-axis classifier separates:

\[
Z_{\text{shared}}
\]

from:

\[
Z_{\text{orient}}.
\]

Classes:

- **A**: shared parent + orientation
- **B**: shared parent only
- **C**: orientation-like only
- **D**: null

The synthetic result:

\[
\boxed{
\text{TauWorld shared-parent recovery}=100\%
}
\]

\[
\boxed{
\text{NullWorld shared-parent false positive}=0\%
}
\]

Orientation-only signatures can appear in NullWorld, so orientation is not enough on its own.

## Correct evidence hierarchy

1. A single anomaly is insufficient.
2. Shared-parent residual covariance is candidate evidence.
3. Shared-parent + morphology/orientation is stronger evidence.
4. Out-of-sample multi-survey survival is required for empirical seriousness.
5. Physical model closure requires independently constrained parent, projectors, dynamics, and response operators.

## Important warning

This package does **not** prove Tau Core. It shows that a disciplined synthetic pipeline can distinguish a shared-parent toy world from an independent-parent toy world without shared-parent false positives in the tested controls.

## Recommended next step

v13 should use more realistic mock cosmology:

- clustered density fields,
- filament skeleton extraction,
- lensing-like projection,
- survey mask,
- photo-z noise,
- shape noise,
- galaxy bias,
- train/test split.

Then apply the v11 classifier:

\[
(Z_{\text{shared}}, Z_{\text{orient}})
\]
