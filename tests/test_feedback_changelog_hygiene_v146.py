from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_v147_active_versions_and_evidence_files():
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    assert data["version"] == "1.4.10"
    assert data["bois_boris_main"] == "2.23"
    assert data["boris_ego"] == "1.7"
    assert data["active_core"] == "core/ACTIVE_CORE_REFERENCE_v1_4_10.md"


def test_v147_rules_include_changelog_hygiene_and_evidence_priority():
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    ids = [r if isinstance(r, str) else r.get("id") for r in data["rules"]]
    for rid in ["BR-108", "BR-109", "BR-110", "BR-111"]:
        assert rid in ids
    text = (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.md").read_text(encoding="utf-8")
    assert "Release Evidence Source Priority Rule" in text
    assert "Changelog Hygiene and Deduplication Rule" in text


def test_v147_changelog_is_deduplicated_and_noncanonical():
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "not the canonical source of active rules" in text
    assert text.count("## v1.4.3") == 1
    assert text.count("## v1.4.4") == 1
    assert text.count("## v1.4.5") == 1
    assert text.count("## v1.4.10") == 1
    assert "repeated v1.4.3 blocks" in text


def test_v147_language_rule_says_every_occurrence_not_first_occurrence():
    active = (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").read_text(encoding="utf-8")
    rulemap = (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.md").read_text(encoding="utf-8")
    ru = (ROOT / "core" / "BORIS_EGO_LAYER_v1_7_RU.md").read_text(encoding="utf-8")
    assert "при каждом появлении" in active
    assert "at every occurrence" in rulemap
    assert "при каждом появлении" in ru
    # Active v1.3 files should not keep the old weaker rule wording as the active rule.
    forbidden = "при первом появлении в каждом local block"
    assert forbidden not in ru
