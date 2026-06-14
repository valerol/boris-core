# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_BORIS_EGO,
    EGO_EXPANSION, EGO_EXPANSION_RU, goal_authority_manifest, route_calculation,
    physiology_integration_manifest, ACTIVE_CORE_BY_LANG,
)

ROOT = Path(__file__).resolve().parents[1]


def test_v142_ego_expansion_and_versions():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert EGO_EXPANSION == "Ethical Goal Orchestrator"
    assert "производных целей" in EGO_EXPANSION_RU
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()


def test_goal_authority_levels_keep_operator_as_g0_source():
    manifest = goal_authority_manifest()
    levels = manifest["goal_authority_levels"]
    assert levels["G0"]["source"] == "operator"
    assert levels["G0"]["boris_ego_may_set"] is False
    for level in ["G1", "G2", "G3", "G4"]:
        assert levels[level]["boris_ego_may_set"] is True
    assert manifest["boris_ego_may_set_derivative_goals"] is True


def test_derivative_goal_and_physiology_change_route_to_core():
    assert route_calculation("derivative_goal_setting") == "BOIS_CORE"
    assert route_calculation("physiology_change") == "BOIS_CORE"


def test_active_v10_core_mirrors_exist_and_contain_expansion():
    for lang, rel in ACTIVE_CORE_BY_LANG.items():
        path = ROOT / rel
        assert "v1_7" in rel
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "Ethical Goal Orchestrator" in text
        assert "G0" in text and "G4" in text
        assert "subjective experience" in text or "субъективным опытом" in text or "expérience subjective" in text or "experiencia subjetiva" in text or "主观经验" in text or "تجربة ذاتية" in text


def test_physiology_stays_large_but_ego_minimal():
    manifest = physiology_integration_manifest()
    assert manifest["system_physiology_allowed_to_be_large"] is True
    assert manifest["boris_ego_physiology_must_remain_minimal"] is True
