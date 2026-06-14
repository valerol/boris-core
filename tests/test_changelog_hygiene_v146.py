# SPDX-License-Identifier: MIT
from pathlib import Path
import json
from bois_sima_boris.ego import active_status, route_calculation

ROOT = Path(__file__).resolve().parents[1]

def test_changelog_is_chronological_and_not_repeated_noise():
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert text.splitlines()[0].startswith("# CHANGELOG")
    assert "## v1.4.10" in text
    assert text.index("## v1.4.10") < text.index("## v1.4.5") < text.index("## v1.4.4")
    assert text.count("## v1.4.3") == 1
    assert "duplicate v1.4.3" not in text.lower()

def test_rule_map_matches_active_versions_and_new_rule():
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    ids = [r if isinstance(r, str) else r["id"] for r in data["rules"]]
    assert "BR-110" in ids
    assert data["public_release"] == "1.4.10"
    assert data["bois_boris_main"] == "2.23"
    assert data["boris_ego"] == "1.7"
    assert data["active_core"] == "core/ACTIVE_CORE_REFERENCE_v1_4_10.md"
    assert all("v1_7" in path for path in data["active_core_by_lang"].values())

def test_feedback_and_changelog_hygiene_route_to_core():
    assert route_calculation("external_feedback_audit") == "BOIS_CORE"
    assert route_calculation("changelog_hygiene") == "BOIS_CORE"
    assert route_calculation("negative_regression_assertion") == "BOIS_CORE"
    assert active_status()["changelog_hygiene"]["active"] is True
