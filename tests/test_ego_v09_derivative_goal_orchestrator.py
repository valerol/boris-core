# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_BORIS_EGO,
    EGO_ACRONYM, EGO_ACRONYM_RU, GOAL_CLASS_AUTHORITY,
    route_calculation, active_status, can_boris_ego_edit,
)

ROOT = Path(__file__).resolve().parents[1]


def test_v142_versions_and_active_core():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()


def test_ego_expansion_is_derivative_goal_orchestrator():
    assert EGO_ACRONYM == "Ethical Goal Orchestrator"
    assert "производных целей" in EGO_ACRONYM_RU
    status = active_status()
    assert status["ego_acronym"] == "Ethical Goal Orchestrator"
    assert status["goal_class_authority"]["G0"].startswith("final/existential")
    assert set(GOAL_CLASS_AUTHORITY) == {"G0", "G1", "G2", "G3", "G4"}


def test_final_goals_are_not_boris_ego_sourced_but_derivative_goals_are_allowed():
    assert "operator" in GOAL_CLASS_AUTHORITY["G0"]
    assert "may not" in GOAL_CLASS_AUTHORITY["G0"]
    for key in ["G1", "G2", "G3", "G4"]:
        assert "may" in GOAL_CLASS_AUTHORITY[key]


def test_derivative_goal_and_physiology_change_route_to_core():
    assert route_calculation("derived_goal_orchestration") == "BOIS_CORE"
    assert route_calculation("instrumental_goal_setting") == "BOIS_CORE"
    assert route_calculation("physiology_change_by_ego") == "BOIS_CORE"


def test_rule_boundaries_for_physiology_change_remain_enforced():
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False
    assert can_boris_ego_edit("L1", explicit_operator_authority=True, core_change_protocol=False)["allowed"] is False
    assert can_boris_ego_edit("L2", explicit_operator_authority=True)["allowed"] is True
