# SPDX-License-Identifier: MIT
import json
from pathlib import Path
from bois_sima_boris.ego import active_status, route_calculation, localized_term_understanding_manifest

ROOT = Path(__file__).resolve().parents[1]
LANGS = ["ar", "zh", "en", "fr", "ru", "es"]


def test_localized_term_understanding_rule_active_in_code_and_rule_map():
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    ids = [r if isinstance(r, str) else r["id"] for r in data["rules"]]
    assert "BR-108" in ids
    manifest = localized_term_understanding_manifest()
    assert manifest["active"] is True
    assert manifest["selected_non_english_response_language"] == "ru"
    assert route_calculation("localized_term_understanding") == "BOIS_CORE"


def test_active_core_and_language_docs_include_term_understanding():
    active = (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").read_text(encoding="utf-8")
    assert "Localized Term Understanding Rule" in active
    for lang in LANGS:
        path = ROOT / "docs" / lang / "TERM_TRANSLATION_UNDERSTANDING.md"
        assert path.exists(), lang
        text = path.read_text(encoding="utf-8")
        if lang != "en":
            assert "[" in text and "]" in text


def test_ego_status_exposes_term_understanding():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["boris_ego"] == "1.7"
    assert status["localized_term_understanding"]["active"] is True


def test_active_rule_requires_every_occurrence_not_first_only():
    from bois_sima_boris.ego import localized_term_understanding_manifest
    rule = localized_term_understanding_manifest()["rule"]
    assert "every occurrence" in rule
    assert "first appearance" not in rule
    active = (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").read_text(encoding="utf-8")
    assert "при каждом появлении" in active
