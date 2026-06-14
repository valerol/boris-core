# SPDX-License-Identifier: MIT
from bois_sima_boris.ego import active_status, route_calculation, can_boris_ego_edit


def test_ego_expansion_and_goal_hierarchy_are_active():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["boris_ego"] == "1.7"
    assert status["ego_expansion"] == "Ethical Goal Orchestrator"
    assert status["ego_expansion_ru"] == "этический оркестратор производных целей"
    assert status["goal_hierarchy"]["G0"].startswith("operator-only")
    assert "G3" in status["goal_hierarchy"]


def test_goal_orchestration_routes_to_core_for_boundary_cases():
    assert route_calculation("derived_goal_setting") == "BOIS_CORE"
    assert route_calculation("physiology_goal_setting") == "BOIS_CORE"
    assert route_calculation("ego_acronym_fixation") == "BOIS_CORE"


def test_ego_cannot_edit_l0_after_goal_orchestration_fixation():
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False
