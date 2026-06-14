# SPDX-License-Identifier: MIT
from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BORIS_EGO, ACTIVE_BOIS_BORIS_MAIN,
    route_calculation, can_boris_ego_edit, language_parity_manifest,
)

def test_active_versions():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"

def test_core_calculation_language_conflict_routes_to_core():
    assert route_calculation("language_parity_conflict") == "BOIS_CORE"

def test_l0_not_editable():
    assert can_boris_ego_edit("L0", explicit_operator_authority=True)["allowed"] is False

def test_language_parity_manifest():
    manifest = language_parity_manifest()
    assert manifest["no_preferred_public_language"] is True
    assert set(manifest["languages"]) == {"ar", "zh", "en", "fr", "ru", "es"}
    assert "BORIS_EGO_LAYER.md" in manifest["required_user_docs"]
