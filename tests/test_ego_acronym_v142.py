# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import active_status, route_calculation, can_boris_ego_edit

ROOT = Path(__file__).resolve().parents[1]

def test_ego_expansion_and_goal_hierarchy_are_active():
    status = active_status()
    assert status["ego_expansion"] == "Ethical Goal Orchestrator"
    assert status["ego_expansion_ru"] == "этический оркестратор производных целей"
    assert "G0" in status["goal_hierarchy"]
    assert "operator" in status["goal_hierarchy"]["G0"]
    assert "G3" in status["goal_hierarchy"]


def test_derivative_goals_and_physiology_changes_route_to_core():
    assert route_calculation("derivative_goal_setting") == "BOIS_CORE"
    assert route_calculation("physiology_change") == "BOIS_CORE"


def test_basic_ego_ethics_still_not_editable():
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False


def test_active_core_documents_contain_fixed_expansion():
    for lang in ["AR", "ZH", "EN", "FR", "RU", "ES"]:
        path = ROOT / "core" / f"BORIS_EGO_LAYER_v1_7_{lang}.md"
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "Ethical Goal Orchestrator" in text
