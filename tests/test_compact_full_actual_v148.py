# SPDX-License-Identifier: MIT
from pathlib import Path
import json
from bois_sima_boris.ego import active_status, route_calculation

ROOT = Path(__file__).resolve().parents[1]


def test_v148_active_versions_and_packaging_policy():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["bois_boris_main"] == "2.23"
    assert status["boris_ego"] == "1.7"
    policy = status["archive_packaging"]
    assert policy["method_3_manifest_only_history"] is True
    assert policy["method_6_canonical_copy"] is True
    assert policy["method_7_archive_type_separation"] is True
    assert policy["full_actual_compact_hard_limit_mb"] == 200
    assert policy["historical_binary_archives_embedded"] is False


def test_v148_core_routing_for_packaging_categories():
    for category in [
        "manifest_only_history",
        "canonical_copy_rule",
        "archive_role_separation",
        "full_actual_compact",
        "compact_full_actual_package",
    ]:
        assert route_calculation(category) == "BOIS_CORE"


def test_v148_rule_map_and_history_manifest():
    data = json.loads((ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").read_text(encoding="utf-8"))
    ids = {item["id"] for item in data["rules"]}
    assert {"BR-113", "BR-114", "BR-115", "BR-116"} <= ids
    manifest = json.loads((ROOT / "history_manifests" / "HISTORY_MANIFEST_ONLY_v1_4_10.json").read_text(encoding="utf-8"))
    assert manifest["policy"] == "manifest-only history"
    assert len(manifest["historical_binaries"]) >= 1
    assert all(item["included_in_compact"] is False for item in manifest["historical_binaries"])


def test_v148_no_large_historical_zip_in_public_release_tree():
    forbidden = ["Full_Current", "FULL_ACTUAL_BOIS", "WITH_ALL_MEMORY", "Development_Log_MAX"]
    offenders = []
    for path in ROOT.rglob("*.zip"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("release_packages/"):
            continue
        if any(token in rel for token in forbidden):
            offenders.append(rel)
    assert offenders == []
