# SPDX-License-Identifier: MIT
from pathlib import Path

from bois_sima_boris.ego import (
    ACTIVE_BORIS_EGO,
    ACTIVE_CORE_RU,
    EGO_BASIC_ETHICAL_CONSTRAINTS,
    enter_mode10,
    advance_mode10,
    should_offer_mode10_extension,
    route_calculation,
    can_boris_ego_edit,
    active_status,
)


def test_active_boris_ego_version_and_core_file():
    assert ACTIVE_BORIS_EGO == "1.7"
    root = Path(__file__).resolve().parents[1]
    assert (root / ACTIVE_CORE_RU).exists()


def test_basic_ego_constraints_are_not_editable():
    assert len(EGO_BASIC_ETHICAL_CONSTRAINTS) == 4
    assert all(item["editable_by_boris_ego"] == "false" for item in EGO_BASIC_ETHICAL_CONSTRAINTS)
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False


def test_mode10_legacy_stub_no_longer_limits_default_ego():
    state = enter_mode10()
    for _ in range(10):
        state = advance_mode10(state)
    assert state.ego_default_active is True
    assert state.mode10_active is False
    assert state.mode10_count == 0
    assert should_offer_mode10_extension(state) is False
    assert ACTIVE_CORE_RU in state.header("4/50")
    assert "EGO default core" in state.header("4/50")


def test_core_calculation_routing_gate():
    assert route_calculation("value_interface") == "BOIS_CORE"
    assert route_calculation("rule_change") == "BOIS_CORE"
    assert route_calculation("format_validation") == "PHYSIOLOGY_ALLOWED_NO_FINAL_PHILOSOPHICAL_CLOSURE"
    assert route_calculation("unclassified") == "BOIS_CORE_BY_DEFAULT_FOR_UNCLASSIFIED_SIGNIFICANT_CASE"


def test_active_status_mentions_core_and_constraints():
    status = active_status()
    assert status["boris_ego"] == "1.7"
    assert status["active_core_ru"] == ACTIVE_CORE_RU
    assert status["ego_default_core_mode"] is True
    assert len(status["basic_constraints"]) == 4
