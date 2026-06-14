# SPDX-License-Identifier: MIT
import json
from pathlib import Path
from bois_sima_boris.ego import active_status, can_boris_ego_edit, can_boris_ego_set_goal

ROOT = Path(__file__).resolve().parents[1]


def test_rule_map_has_unique_new_rules_and_active_defaults():
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    ids = [r if isinstance(r, str) else r["id"] for r in data["rules"]]
    assert len(ids) == len(set(ids))
    for rid in ["BR-102", "BR-103", "BR-104", "BR-105", "BR-106", "BR-107", "BR-108"]:
        assert rid in ids
    assert data["default_response_format"] == "MAXIMUM_OPERATIONAL_RESPONSE"
    assert data["physiology_as_core_transit"] is True


def test_ego_basic_ethics_and_goal_hierarchy_still_boundaries():
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False
    assert can_boris_ego_edit("L1", explicit_operator_authority=True, core_change_protocol=False)["allowed"] is False
    assert can_boris_ego_edit("L1", explicit_operator_authority=True, core_change_protocol=True)["allowed"] is True
    assert can_boris_ego_set_goal("G0")["allowed"] is False
    assert can_boris_ego_set_goal("G1", traceable_to_operator_final_goal=True)["allowed"] is True
    assert can_boris_ego_set_goal("G2", traceable_to_operator_final_goal=False)["allowed"] is False


def test_mode10_not_active_and_not_contradicting_default_ego():
    status = active_status()
    assert status["ego_default_core_mode"] is True
    assert status["mode10_special_mode_active"] is False
    assert status["ego_default_core"]["mode10_counter_required"] is False
    assert status["ego_default_core"]["mode10_extension_prompt_required"] is False
