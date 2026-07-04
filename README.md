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
TauWorld shared-parent recovery:       100%
NullWorld shared-parent false positive: 0%
NullWorld orientation-only rate:        22.963%
```

Orientation-only structure can appear in null worlds, so orientation is not
allowed to count as Tau Core evidence by itself.

## Does Not Claim

- It does not prove Tau Core.
- It does not analyze real survey data.
- It does not validate a lensing, galaxy, cosmic-web, or dark-sector claim.
- It does not replace Paper 14 or Paper 16.
- It does not claim that morphology/orientation is sufficient evidence.
- It does not claim empirical discovery or physical validation.

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

Claim marker: synthetic methodology only; not empirical validation; not physical validation.

## Relation to Other Tau Core Papers

- Paper 14 gives the cosmic-web witness ladder.
- Paper 16 gives the broader weak-signal amplification protocol.
- Paper 17 supplies the explicit two-axis covariance classifier that explains
  why shared-parent support and morphology/orientation support must be reported
  separately.
