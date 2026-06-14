# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_BORIS_EGO,
    EGO_DEFAULT_CORE_MODE, EGO_LAYER_IS_CORE_PART, EGO_SPECIAL_MODE_LIMITS_SUPERSEDED,
    MODE10_SPECIAL_MODE_ACTIVE, MODE10_TRIGGER, active_status, route_calculation,
    POST_CHANGE_DOWNLOAD_OFFER_REQUIRED, ASKING_OPERATOR_TO_CONFIRM_OBVIOUS_ARTIFACT_DELIVERY_IS_ATTENTION_THEFT,
)

ROOT = Path(__file__).resolve().parents[1]


def test_ego_default_core_versions():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()


def test_ego_is_default_core_not_special_mode():
    assert EGO_DEFAULT_CORE_MODE is True
    assert EGO_LAYER_IS_CORE_PART is True
    assert EGO_SPECIAL_MODE_LIMITS_SUPERSEDED is True
    assert MODE10_SPECIAL_MODE_ACTIVE is False
    assert MODE10_TRIGGER is None
    status = active_status()
    assert status["ego_default_core"]["mode10_counter_required"] is False
    assert status["ego_default_core"]["mode10_extension_prompt_required"] is False


def test_post_change_artifact_rule_active():
    assert POST_CHANGE_DOWNLOAD_OFFER_REQUIRED is True
    assert ASKING_OPERATOR_TO_CONFIRM_OBVIOUS_ARTIFACT_DELIVERY_IS_ATTENTION_THEFT is True
    status = active_status()
    assert status["post_change_artifact_delivery"]["post_change_download_offer_required"] is True
    assert status["post_change_artifact_delivery"]["ask_confirmation_for_obvious_artifact_delivery"] is False


def test_default_core_changes_route_to_bois_core():
    for category in ["ego_default_core_adoption", "special_mode_limit_removal", "post_change_artifact_delivery", "attention_theft_confirmation_avoidance"]:
        assert route_calculation(category) == "BOIS_CORE"
