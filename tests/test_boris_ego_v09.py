# SPDX-License-Identifier: MIT
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_BORIS_EGO,
    ego_acronym_manifest, can_boris_ego_set_goal, route_calculation, ACTIVE_CORE_BY_LANG
)
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_v142_ego_acronym_fixed_as_ethical_goal_orchestrator():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    m = ego_acronym_manifest()
    assert m["expanded"] == "Ethical Goal Orchestrator"
    assert m["ru"] == "этический оркестратор производных целей"
    assert m["final_goal_source"] == "operator"
    assert m["boris_ego_is_final_goal_source"] is False


def test_ego_goal_authority_boundary():
    assert can_boris_ego_set_goal("G0", traceable_to_operator_final_goal=True)["allowed"] is False
    for cls in ["G1", "G2", "G3", "G4"]:
        assert can_boris_ego_set_goal(cls, traceable_to_operator_final_goal=True)["allowed"] is True
        assert can_boris_ego_set_goal(cls, traceable_to_operator_final_goal=False)["allowed"] is False


def test_derivative_goal_and_physiology_changes_route_to_core():
    for category in ["derivative_goal_setting", "instrumental_goal_generation", "physiology_goal_setting", "physiology_change", "ego_acronym_fixation"]:
        assert route_calculation(category) == "BOIS_CORE"


def test_active_core_mirrors_v10_exist():
    for rel in ACTIVE_CORE_BY_LANG.values():
        assert "v1_7" in rel
        assert (ROOT / rel).exists()
