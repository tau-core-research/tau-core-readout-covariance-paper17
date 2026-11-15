"""Publication dependency guard, not Nature validation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_current_state_scope():
    p = json.loads((ROOT / "data/derived/publication_state_20261009.json").read_text())
    assert p["empirical_scores_changed"] is False
    assert p["nature_occupation_proved"] is False
    assert p["tau_specific_evidence"] is False
    assert p["mass_candidate_retained"] is True
    for item in p["manuscripts"]:
        text = (ROOT / item["source"]).read_text()
        assert hashlib.sha256(text.encode()).hexdigest() == item["source_sha256"]
        assert "% BEGIN SOURCE INSTRUMENT RECONCILIATION" not in text
        assert "\\section{Upstream Ownership, Inherited Results, and Scope Boundary}" in text
        assert "nameddest=oir1" in text and "nameddest=msi1" in text
