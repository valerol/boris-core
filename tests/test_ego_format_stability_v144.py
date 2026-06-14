# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_BORIS_EGO,
    DEFAULT_RESPONSE_FORMAT, MAXIMUM_RESPONSE_FORMAT_DEFAULT,
    FORMAT_STABILITY_GATE_ACTIVE, CROSS_CHAT_FORMAT_RESTORE_GUARD_ACTIVE,
    ANTI_BUREAUCRATIC_REVISION_ACTIVE, PHYSIOLOGY_AS_CORE_TRANSIT,
    active_status, route_calculation,
)

ROOT = Path(__file__).resolve().parents[1]


def test_v144_active_versions_and_files():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()
    assert (ROOT / "MEMORY_BORIS_EGO_v1_7.md").exists()


def test_maximum_response_format_is_default_and_stable():
    assert DEFAULT_RESPONSE_FORMAT == "MAXIMUM_OPERATIONAL_RESPONSE"
    assert MAXIMUM_RESPONSE_FORMAT_DEFAULT is True
    assert FORMAT_STABILITY_GATE_ACTIVE is True
    assert CROSS_CHAT_FORMAT_RESTORE_GUARD_ACTIVE is True
    status = active_status()
    fmt = status["response_format"]
    assert fmt["maximum_response_format_default"] is True
    assert fmt["answer_counter_required"] is True
    assert fmt["active_core_reference_required"] is True
    assert fmt["compact_mode_default"] is False


def test_anti_bureaucracy_preserves_viability():
    assert ANTI_BUREAUCRATIC_REVISION_ACTIVE is True
    status = active_status()
    ab = status["anti_bureaucracy"]
    assert ab["remove_redundant_confirmation_prompts"] is True
    assert ab["preserve_all_contexts"] is True
    assert ab["no_loss_of_life_supporting_information"] is True
    assert ab["does_not_allow_silent_core_ethics_change"] is True


def test_physiology_as_core_transit():
    assert PHYSIOLOGY_AS_CORE_TRANSIT is True
    status = active_status()
    pt = status["physiology_transit"]
    assert pt["physiology_as_core_transit"] is True
    assert pt["stable_developed_physiology_preserved"] is True
    assert route_calculation("physiology_as_core_transit") == "BOIS_CORE"
    assert route_calculation("response_envelope_rendering_after_core_calculation") == "PHYSIOLOGY_ALLOWED_NO_FINAL_PHILOSOPHICAL_CLOSURE"


def test_new_conflict_categories_route_to_core():
    for category in [
        "anti_bureaucratic_revision", "rule_conflict_resolution", "response_format_stability",
        "maximum_response_default", "cross_chat_restore_format", "format_drift_repair",
        "context_preservation", "meaning_preserving_compression", "real_usage_analysis",
        "self_improvement_hypothesis", "stress_test_gate",
    ]:
        assert route_calculation(category) == "BOIS_CORE"
