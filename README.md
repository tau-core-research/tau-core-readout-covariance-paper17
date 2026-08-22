# Tau Core Readout Covariance Paper 17

Private Paper 17 scaffold:

**A readout-covariance classifier for shared-parent Tau Core signals**

This repository turns `taucore_readout_covariance_package` into a reproducible
paper package.  It preserves the source package as provenance, promotes the
v8-v12 synthetic lineage into a structured manuscript, regenerates compact
figures from derived CSV tables, builds a PDF, and prepares an arXiv source
archive.

## Main Claim

The paper defines a two-axis synthetic diagnostic for Tau Core-style
multi-readout evidence:

```text
Z_shared  = shared-parent cross-readout covariance support
Z_orient  = morphology/orientation-like support
```

The claim-safe hierarchy is:

```text
shared-parent covariance first;
morphology/orientation only as conditional reinforcement.
```

The included v11 synthetic classifier reports:

```text
Total v11 runs:                         270
TauWorld / NullWorld split:             135 / 135
Unique seeds:                           10
TauWorld shared-parent recovery:       100%
NullWorld shared-parent false positive: 0%      (0/135; Wilson 95% upper ~2.8%)
NullWorld orientation-only rate:        22.963% (31/135)
```

Orientation-only structure can appear in null worlds, so orientation is not
allowed to count as Tau Core evidence by itself.

The important methodological point is not that TauWorld succeeds; TauWorld is
generated with a shared parent.  The important point is that NullWorld can show
orientation-only structure while the shared-parent covariance axis remains
clean in this synthetic audit.

## Does Not Claim

- It does not prove Tau Core.
- It does not analyze real survey data.
- It does not validate a lensing, galaxy, cosmic-web, or dark-sector claim.
- It does not replace Paper 14 or Paper 16.
- It does not claim that morphology/orientation is sufficient evidence.
- It does not claim empirical discovery or physical validation.

## Source-Transport Boundary

The synthetic covariance model is evaluated under a supplied transport. It
does not infer a physical transport from covariance. Current Tau Core source
accounting allows smooth non-scalar transport only conditionally through full
body-connection holonomy or Kato transport `[dP_O,P_O]` of a varying,
constant-rank, source-owned access projector. The manuscript therefore uses an
ordered source-path parameter rather than an external parent time, and treats
covariance as common-cause candidate evidence rather than connection
identification.

## Included Data

The repository includes compact synthetic CSV tables under `data/derived/`,
source-package provenance under `source_package_manifest/`, and two source
scripts under `code/`.

## Reproduce

```bash
python scripts/reproduce.py
```

The command:

1. rebuilds summary artifacts from the v11 classifier tables;
2. regenerates paper figures from CSV tables;
3. compiles `paper17_submission_source/main.tex`;
4. builds `arxiv_submission_source.zip`;
5. runs public package tests;
6. prints `PAPER17_READOUT_COVARIANCE_REPRODUCTION_COMPLETE`.

## arXiv Source Package

`arxiv_submission_source.zip` is generated from
`paper17_submission_source/` and excludes the compiled PDF plus temporary TeX
build products.

## Scope

Paper 17 is a synthetic methodology paper.  It supports the protocol-level
lesson that shared-parent covariance is a stronger evidence axis than
orientation-only structure.  It is not a physical or empirical validation
paper.

## Required Next Gate

A stronger Paper17/v13 package should be treated as mandatory before any
real-data-facing promotion:

- threshold-free ROC/PR-style reporting, not only fixed `Z_shared=3` and
  `Z_orient=2` cuts;
- seed/split sensitivity, confidence intervals, and explicit failure rates;
- harder NullWorlds with shared survey mask, shared selection bias, foreground
  or systematics templates, common smoothing kernels, and partial parent
  leakage controls;
- realistic mock catalogues with clustered density fields, filament skeleton
  extraction, lensing-like projection, survey mask, photo-z noise, shape noise,
  galaxy bias, and held-out split;
- independent implementation of the same frozen classifier.

Claim marker: synthetic methodology only; not empirical validation; not physical validation.

## Relation to Other Tau Core Papers

- Paper 14 gives the cosmic-web witness ladder.
- Paper 16 gives the broader weak-signal amplification protocol.
- Paper 17 supplies the explicit two-axis covariance classifier that explains
  why shared-parent support and morphology/orientation support must be reported
  separately.
- Paper 18 supplies a photon-lensing MAR template,
  `T_tau = B_env A_f M_bf`, and in v2 extends it to out-of-sample scale
  validation, physical shear mocks, and a toy Null-Matter Link diagnostic.
  Paper 17 is the guardrail for that template family: MAR/shear/null-matter
  correlations should be reported as morphology/orientation support unless
  they also survive the `Z_shared` common-parent covariance axis.
