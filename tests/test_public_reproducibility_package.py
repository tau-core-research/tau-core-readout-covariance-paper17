from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist() -> None:
    required = [
        "README.md",
        "DATA_NOTICE.md",
        "CITATION.cff",
        "LICENSE",
        "requirements.txt",
        "paper17_submission_source/main.tex",
        "paper17_submission_source/refs.bib",
        "paper17_submission_source/main.pdf",
        "arxiv_submission_source.zip",
        "scripts/reproduce.py",
        "scripts/build_readout_covariance_summary.py",
        "scripts/build_figures.py",
        "scripts/build_arxiv_source.py",
        "data/derived/taucore_v11_overall_summary.csv",
        "data/derived/taucore_v11_class_rates.csv",
        "data/derived/paper17_readout_covariance_summary.csv",
        "figures/fig_v11_threshold_sweep.pdf",
        "paper17_submission_source/figures/fig_v11_threshold_sweep.pdf",
        "source_package_manifest/MANIFEST.json",
    ]
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    assert not missing, missing


def test_claim_boundaries_are_explicit() -> None:
    text = (
        (ROOT / "README.md").read_text(encoding="utf-8")
        + "\n"
        + (ROOT / "paper17_submission_source" / "main.tex").read_text(encoding="utf-8")
    )
    forbidden = [
        "we prove Tau Core",
        "Tau Core is validated",
        "we show that dark matter is solved",
        "we show that dark energy is solved",
        "we report empirical discovery",
    ]
    for phrase in forbidden:
        assert phrase not in text
    for phrase in [
        "synthetic methodology",
        "not empirical",
        "not physical validation",
        "orientation is secondary",
        "threshold-sweep",
        "harder NullWorlds",
    ]:
        assert phrase in text


def test_v11_summary_values() -> None:
    payload = json.loads(
        (ROOT / "data" / "derived" / "paper17_readout_covariance_summary.json").read_text(
            encoding="utf-8"
        )
    )
    assert payload["claim_boundary"] == "synthetic_methodology_not_empirical_validation"
    assert abs(payload["tauworld_shared_parent_recovery"] - 1.0) < 1e-12
    assert abs(payload["nullworld_shared_parent_false_positive"] - 0.0) < 1e-12
    assert abs(payload["nullworld_orientation_only_rate"] - 0.22962962962962963) < 1e-12
    assert payload["total_runs"] == 270
    assert payload["tauworld_n"] == 135
    assert payload["nullworld_n"] == 135
    assert payload["unique_seed_count"] == 10
    assert 0.027 < payload["nullworld_shared_parent_false_positive_ci95_high"] < 0.028


def test_summary_csv_matches_manifest_claim() -> None:
    rows = {}
    with (ROOT / "data" / "derived" / "paper17_readout_covariance_summary.csv").open(
        newline="", encoding="utf-8"
    ) as f:
        for row in csv.DictReader(f):
            rows[row["metric"]] = float(row["value"])
    assert rows["tauworld_shared_parent_recovery"] == 1.0
    assert rows["nullworld_shared_parent_false_positive"] == 0.0
    assert rows["nullworld_orientation_only_rate"] > 0.0
    assert rows["total_runs"] == 270


def test_arxiv_zip_is_source_only() -> None:
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = set(zf.namelist())
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    assert "figures/fig_v11_class_rates.pdf" in names
    assert "figures/fig_v11_threshold_sweep.pdf" in names
