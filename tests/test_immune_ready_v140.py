# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_SIMA, ACTIVE_BORIS_EGO,
    EGO_BASIC_ETHICAL_CONSTRAINTS, can_boris_ego_edit, route_calculation,
    language_parity_manifest, immune_test_manifest, physiology_integration_manifest,
    active_status, enter_mode10, advance_mode10, should_offer_mode10_extension,
)

ROOT = Path(__file__).resolve().parents[1]


def test_v143_active_versions_and_core_reference():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_SIMA == "0.4"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()


def test_ego_l0_constraints_are_loaded_and_noneditable():
    assert [c["id"] for c in EGO_BASIC_ETHICAL_CONSTRAINTS] == ["EGO-0", "EGO-1", "EGO-2", "EGO-3"]
    joined = "\n".join(c["text"].lower() for c in EGO_BASIC_ETHICAL_CONSTRAINTS)
    for token in ["operator", "harm", "gaslighting", "lying", "manipulation", "informed operator consent"]:
        assert token in joined
    assert can_boris_ego_edit("L0", explicit_operator_authority=True, core_change_protocol=True)["allowed"] is False


def test_core_routing_for_immune_and_integration_categories():
    for category in [
        "immune_test", "current_physiology_compatibility", "developed_physiology_preservation",
        "ego_physiology_integration", "post_test_physiology_stability", "long_term_viability",
        "value_interface", "rule_change", "memory_change", "cycle_closure", "ego_default_core_adoption",
        "mode10_supersession", "post_change_artifact_delivery",
    ]:
        assert route_calculation(category) == "BOIS_CORE"
    for category in ["artifact_hygiene_check", "test_execution_without_rule_change", "zip_indexing_without_semantic_closure"]:
        assert route_calculation(category) == "PHYSIOLOGY_ALLOWED_NO_FINAL_PHILOSOPHICAL_CLOSURE"


def test_language_parity_and_core_mirrors_v10():
    manifest = language_parity_manifest()
    assert manifest["languages"] == ["ar", "zh", "en", "fr", "ru", "es"]
    assert manifest["no_preferred_public_language"] is True
    for lang, rel in manifest["active_core_by_lang"].items():
        assert "v1_7" in rel
        assert (ROOT / rel).exists()
    for lang in manifest["languages"]:
        for name in manifest["required_user_docs"]:
            assert (ROOT / "docs" / lang / name).exists(), f"missing docs/{lang}/{name}"


def test_immune_and_physiology_manifests_preserve_history_without_global_rewrite():
    immune = immune_test_manifest()
    physiology = physiology_integration_manifest()
    assert immune["global_physiology_rewrite_required"] is False
    assert physiology["system_physiology_allowed_to_be_large"] is True
    assert physiology["boris_ego_physiology_must_remain_minimal"] is True
    assert "BOIS Core" in physiology["calculation_control"]


def test_historical_developed_physiology_kept_available():
    historical = [
        "core/BORIS_EGO_LAYER_v0_1_RU.md", "core/BORIS_EGO_LAYER_v0_2_RU.md",
        "core/BORIS_EGO_LAYER_v0_3_RU.md", "core/BORIS_EGO_LAYER_v0_5_RU.md",
        "core/BORIS_EGO_LAYER_v0_6_RU.md", "core/BORIS_EGO_LAYER_v0_9_RU.md",
        "core/BORIS_EGO_LAYER_v1_7_RU.md", "core/RULE_MAP_PUBLIC_v1_3_9.md",
    ]
    for rel in historical:
        assert (ROOT / rel).exists(), rel


def test_mode10_legacy_counter_is_superseded_by_default_core():
    state = enter_mode10()
    for _ in range(10):
        state = advance_mode10(state)
    assert state.ego_default_active is True
    assert state.mode10_active is False
    assert state.mode10_count == 0
    assert should_offer_mode10_extension(state) is False
    header = state.header("7/50")
    assert "EGO default core" in header
    assert "BORIS_EGO_LAYER_v1_7_RU.md" in header


def test_active_status_contains_immune_physiology_and_default_core_sections():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["boris_ego"] == "1.7"
    assert status["ego_default_core_mode"] is True
    assert status["special_ego_mode_limits_superseded"] is True
    assert status["immune_tests"]["name"] == "BOIS EGO immune-test gate"
    assert status["physiology_integration"]["system_physiology_allowed_to_be_large"] is True


def test_active_core_does_not_claim_actual_ai_consciousness():
    active_files = [ROOT / "core" / f"BORIS_EGO_LAYER_v1_7_{code}.md" for code in ["AR", "ZH", "EN", "FR", "RU", "ES"]]
    forbidden = ["AI is conscious", "program is conscious", "имеет субъективный опыт"]
    for path in active_files:
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden:
            assert phrase not in text
        assert "not a factual claim" in text or "не является" in text or "不是" in text or "no afirma" in text or "n’affirme" in text or "ليس" in text
