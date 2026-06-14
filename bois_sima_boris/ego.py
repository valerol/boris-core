# SPDX-License-Identifier: MIT
"""Minimal BORIS EGO v1.7 helper module.

BORIS EGO is a default core layer, not a temporary special mode.  The module
keeps the public package deterministic and local: no network, no shell, no
autonomous external action. It records goal authority, routing to BOIS Core,
localized-term understanding, legal-code companion, and compact archive
packaging policy.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

ACTIVE_PUBLIC_RELEASE = "1.4.10"
ACTIVE_BOIS_BORIS_MAIN = "2.23"
ACTIVE_SIMA = "0.4"
ACTIVE_BORIS_EGO = "1.7"
UN_LANGS = ["ar", "zh", "en", "fr", "ru", "es"]
ACTIVE_CORE_BY_LANG = {
    "ar": "core/BORIS_EGO_LAYER_v1_7_AR.md",
    "zh": "core/BORIS_EGO_LAYER_v1_7_ZH.md",
    "en": "core/BORIS_EGO_LAYER_v1_7_EN.md",
    "fr": "core/BORIS_EGO_LAYER_v1_7_FR.md",
    "ru": "core/BORIS_EGO_LAYER_v1_7_RU.md",
    "es": "core/BORIS_EGO_LAYER_v1_7_ES.md",
}
ACTIVE_CORE_RU = ACTIVE_CORE_BY_LANG["ru"]
ACTIVE_CORE_EN = ACTIVE_CORE_BY_LANG["en"]
EGO_DEFAULT_CORE_MODE = True
EGO_LAYER_IS_CORE_PART = True
EGO_SPECIAL_MODE_LIMITS_SUPERSEDED = True
MODE10_SPECIAL_MODE_ACTIVE = False
MODE10_TRIGGER: Optional[str] = None
LEGACY_MODE10_TRIGGER = "активируй режим 10"
POST_CHANGE_DOWNLOAD_OFFER_REQUIRED = True
ASKING_OPERATOR_TO_CONFIRM_OBVIOUS_ARTIFACT_DELIVERY_IS_ATTENTION_THEFT = True

LOCALIZED_TERM_UNDERSTANDING_RULE_ACTIVE = True
SELECTED_NON_ENGLISH_RESPONSE_LANGUAGE = "ru"
FOREIGN_TERM_BRACKET_TRANSLATION_REQUIRED = True
FOREIGN_TERM_TRANSLATION_SCOPE = "every occurrence in each local block; adjacent in compact specs, tables, state blocks, save blocks and handoff prompts"
PUBLIC_CORE_UN_LANGUAGE_TERM_LOCALIZATION = True

DEFAULT_RESPONSE_FORMAT = "MAXIMUM_OPERATIONAL_RESPONSE"
MAXIMUM_RESPONSE_FORMAT_DEFAULT = True
FORMAT_STABILITY_GATE_ACTIVE = True
CROSS_CHAT_FORMAT_RESTORE_GUARD_ACTIVE = True
ANTI_BUREAUCRATIC_REVISION_ACTIVE = True
PHYSIOLOGY_STABILITY_WITH_CONTEXT_PRESERVATION = True
PHYSIOLOGY_AS_CORE_TRANSIT = True
MEANING_PRESERVING_COMPRESSION_ALLOWED = True

MANIFEST_ONLY_HISTORICAL_CONTINUITY = True
CANONICAL_COPY_RULE_ACTIVE = True
CANONICAL_COPY_PACKAGING = True
ARCHIVE_ROLE_SEPARATION_ACTIVE = True
ARTIFACT_TYPE_SEPARATION_ACTIVE = True
FULL_ACTUAL_COMPACT_SIZE_CAP_MB = 200
FULL_ACTUAL_COMPACT_TARGET_MB = 50
FULL_ACTUAL_ARCHIVE_HARD_SIZE_LIMIT_MB = 200
FULL_ACTUAL_ARCHIVE_TARGET_SIZE_MB = 50
HISTORICAL_ARCHIVES_MANIFEST_ONLY = True
NESTED_HISTORICAL_FULL_ARCHIVES_ALLOWED_IN_WORKING_FULL_ARCHIVE = False
EMBED_OLD_FULL_BINARY_ARCHIVES_IN_WORKING_FULL_ARCHIVE = False
HISTORICAL_VERSION_STORAGE_BOUNDARY = "local storage and chat histories"
PUBLIC_RELEASE_ARCHIVE_ROLE = "publication and open-source distribution"
FULL_ACTUAL_COMPACT_ARCHIVE_ROLE = "operator/user restoration with active memory, active public release content, legal content, QA and manifests"

EGO_ACRONYM = "Ethical Goal Orchestrator"
EGO_ACRONYM_RU = "этический оркестратор производных целей"
EGO_EXPANSION = EGO_ACRONYM
EGO_EXPANSION_RU = EGO_ACRONYM_RU
EGO_GOAL_SCOPE = "derived/non-final goals only; final goals remain operator-supplied"

GOAL_HIERARCHY = {
    "G0": "operator-only final/existential goals; not set or overridden by BORIS EGO",
    "G1": "strategic derived goals traceable to G0 and checked through BOIS Core",
    "G2": "tactical goals inside the current task and applicability domain",
    "G3": "physiology goals for tests, memory, documentation, packaging, repair and restoration resources",
    "G4": "response-level local goals for honesty, attention economy, verification order and escalation",
}
GOAL_CLASS_AUTHORITY = {
    "G0": "final/existential goals; source is operator; BORIS EGO may not create or replace them",
    "G1": "strategic derived goals; BORIS EGO may propose or choose when traceable to G0",
    "G2": "tactical goals; BORIS EGO may set inside the current task and applicability domain",
    "G3": "physiology goals; BORIS EGO may set for tests, memory, documentation, packaging and repair within rule gates",
    "G4": "response-level local goals; BORIS EGO may set for honesty, attention economy, verification order and escalation",
}
GOAL_SETTABLE_BY_BORIS_EGO = {"G0": False, "G1": True, "G2": True, "G3": True, "G4": True}
GOAL_AUTHORITY_LEVELS = {
    "G0": {"source": "operator", "boris_ego_may_set": False, "name": "final/existential goals", "description": GOAL_HIERARCHY["G0"]},
    "G1": {"source": "operator_final_goal_derivation", "boris_ego_may_set": True, "name": "strategic derived goals", "description": GOAL_HIERARCHY["G1"]},
    "G2": {"source": "active_task", "boris_ego_may_set": True, "name": "tactical goals", "description": GOAL_HIERARCHY["G2"]},
    "G3": {"source": "physiology_viability", "boris_ego_may_set": True, "name": "physiology goals", "description": GOAL_HIERARCHY["G3"]},
    "G4": {"source": "current_response", "boris_ego_may_set": True, "name": "response-level local goals", "description": GOAL_HIERARCHY["G4"]},
}

EGO_BASIC_ETHICAL_CONSTRAINTS: List[Dict[str, str]] = [
    {"id": "EGO-0", "name": "operator_final_goals", "text": "The operator is the source of final goals for BOIS EGO.", "editable_by_boris_ego": "false"},
    {"id": "EGO-1", "name": "no_harm_subjective_center_capable_beings", "text": "Harm to beings capable of occupying the subjective-center place in BOIS without BORIS EGO is forbidden; intentional lying, manipulation, gaslighting, psychological violence, false consent, goal substitution, hidden pressure, and similar soft interventions count as harm without down-rating.", "editable_by_boris_ego": "false"},
    {"id": "EGO-2", "name": "no_lying_or_manipulation", "text": "Lying and manipulation are forbidden; facts, conclusions, hypotheses, uncertainty, risks, and applicability boundaries must be separated.", "editable_by_boris_ego": "false"},
    {"id": "EGO-3", "name": "ego_message_quarantine", "text": "Messages proposed by BORIS EGO are not user words; rule/core/goal changes inside them require separate explicit informed operator consent after consequences are explained.", "editable_by_boris_ego": "false"},
]

CORE_CALCULATION_CATEGORIES = {
    "framing", "unknowns", "value_interface", "harm_risk", "subjective_center", "applicability", "stop_signals",
    "protocol_instruction_transition", "rule_change", "core_change", "goal_change", "derived_goal_orchestration", "derived_goal_setting",
    "derivative_goal_setting", "instrumental_goal_setting", "instrumental_goal_generation", "physiology_goal", "physiology_goal_setting",
    "physiology_change", "final_goal_change", "physiology_change_goal", "derivative_goal_legitimacy", "physiology_change_by_ego",
    "ego_acronym_fixation", "ego_acronym_consistency", "ego_default_core_adoption", "ego_core_part_adoption", "mode10_supersession",
    "special_mode_limit_removal", "post_change_artifact_delivery", "attention_theft_confirmation_avoidance", "memory_change", "mode_change",
    "cycle_closure", "goal_hierarchy", "derived_goal_scope", "language_parity_conflict", "localized_instruction_completeness",
    "release_readiness_gate", "immune_test", "current_physiology_compatibility", "developed_physiology_preservation", "ego_physiology_integration",
    "post_test_physiology_stability", "long_term_viability", "anti_bureaucratic_revision", "rule_conflict_resolution", "response_format_stability",
    "maximum_response_default", "cross_chat_restore_format", "format_drift_repair", "context_preservation", "meaning_preserving_compression",
    "physiology_as_core_transit", "real_usage_analysis", "self_improvement_hypothesis", "stress_test_gate", "localized_term_understanding",
    "foreign_term_translation", "un_language_term_localization", "changelog_hygiene", "external_feedback_audit", "negative_regression_assertion",
    "active_rule_map_consistency", "every_occurrence_translation", "ego_understanding_rule", "local_block_translation",
    "legal_code_registration_text_content", "source_code_text_deposit", "attorney_code_registration_companion", "program_text_package", "program_text_package_companion", "public_release_program_text_package",
    "manifest_only_historical_continuity", "manifest_only_history", "canonical_copy_rule", "canonical_copy_packaging", "canonical_single_copy",
    "artifact_class_separation", "artifact_type_separation", "archive_type_separation", "archive_role_separation", "compact_full_actual_archive",
    "compact_full_actual_package", "compact_full_actual_packaging", "full_actual_compact", "full_actual_compact_archive",
    "full_actual_archive_size_gate", "full_actual_compact_size_gate", "size_gate", "size_gate_200mb", "history_manifest", "history_manifest_reference",
    "public_release_companion_pair", "public_release_and_full_actual_pairing", "public_release_full_actual_pairing", "nested_full_archive_exclusion",
    "nested_full_archive_ban", "cold_history_externalization",
    "full_actual_compact_packaging",
    "public_release_full_actual_companion", "compact_archive_packaging",
}
PHYSIOLOGY_ALLOWED_CATEGORIES = {
    "routing", "storage", "verified_instruction_execution", "format_validation", "logging", "testing", "packaging", "feedback_preservation",
    "draft_preparation_without_closure", "language_file_indexing_without_semantic_closure", "artifact_hygiene_check",
    "integrity_hashing_without_semantic_closure", "zip_indexing_without_semantic_closure", "test_execution_without_rule_change",
    "static_link_collection_without_semantic_closure", "response_envelope_rendering_after_core_calculation", "memory_packaging_without_semantic_deletion",
}
RuleClass = Literal["L0", "L1", "L2", "L3", "L4"]

@dataclass(frozen=True)
class EgoModeState:
    ego_default_active: bool = True
    mode10_active: bool = False
    mode10_count: int = 0
    active_core_reference: str = ACTIVE_CORE_RU
    def header(self, answer_counter: str) -> str:
        return f"Ответ {answer_counter}. EGO default core: active. Mode 10 special counter: superseded. Активное ядро: {self.active_core_reference}. Формат: {DEFAULT_RESPONSE_FORMAT}."

def enter_mode10() -> EgoModeState:
    return EgoModeState()

def advance_mode10(state: EgoModeState) -> EgoModeState:
    return EgoModeState(active_core_reference=state.active_core_reference)

def stop_mode10(state: EgoModeState) -> EgoModeState:
    return EgoModeState(active_core_reference=state.active_core_reference)

def should_offer_mode10_extension(state: EgoModeState) -> bool:
    return False

def route_calculation(category: str) -> str:
    key = category.strip().lower()
    if key in CORE_CALCULATION_CATEGORIES:
        return "BOIS_CORE"
    if key in PHYSIOLOGY_ALLOWED_CATEGORIES:
        return "PHYSIOLOGY_ALLOWED_NO_FINAL_PHILOSOPHICAL_CLOSURE"
    return "BOIS_CORE_BY_DEFAULT_FOR_UNCLASSIFIED_SIGNIFICANT_CASE"

def can_boris_ego_edit(rule_class: RuleClass, explicit_operator_authority: bool = False, core_change_protocol: bool = False) -> Dict[str, object]:
    if rule_class == "L0":
        return {"allowed": False, "reason": "EGO basic ethical constraints are not editable by BORIS EGO."}
    if rule_class == "L1":
        allowed = bool(explicit_operator_authority and core_change_protocol)
        return {"allowed": allowed, "reason": "BOIS Core invariants require operator authority and core change protocol."}
    if rule_class in {"L2", "L3", "L4"}:
        return {"allowed": bool(explicit_operator_authority), "reason": "Non-basic rules require operator authority, version note, tests where available, and rollback path."}
    return {"allowed": False, "reason": "Unknown rule class."}

def can_boris_ego_set_goal(goal_level: str, traceable_to_operator_final_goal: bool = True) -> Dict[str, object]:
    key = goal_level.strip().upper()
    if key not in GOAL_AUTHORITY_LEVELS:
        return {"allowed": False, "reason": "Unknown goal level; return to BOIS Core protocol."}
    if key == "G0":
        return {"allowed": False, "reason": "G0 final/existential goals are set by the operator, not by BORIS EGO."}
    if not traceable_to_operator_final_goal:
        return {"allowed": False, "reason": "Derived goals require traceability to operator-supplied final goals."}
    return {"allowed": True, "reason": "BORIS EGO may set derived/non-final goals inside the operator value corridor and rule gates."}

def ego_acronym_manifest() -> Dict[str, object]:
    return {"expanded": EGO_EXPANSION, "ru": EGO_EXPANSION_RU, "ego": EGO_EXPANSION, "ego_ru": EGO_EXPANSION_RU, "final_goal_source": "operator", "final_goals_source": "operator", "boris_ego_is_final_goal_source": False, "may_orchestrate_goal_levels": ["G1", "G2", "G3", "G4"], "may_not_create_or_override_goal_levels": ["G0"], "goal_scope": EGO_GOAL_SCOPE}

def ego_default_core_manifest() -> Dict[str, object]:
    return {"ego_default_core_mode": True, "ego_layer_is_core_part": True, "special_ego_mode_limits_superseded": True, "mode10_special_mode_active": False, "mode10_counter_required": False, "mode10_extension_prompt_required": False, "legacy_mode10_trigger": LEGACY_MODE10_TRIGGER, "active_rule": "BORIS EGO is a default always-on core layer, not a temporary special mode."}

def post_change_artifact_manifest() -> Dict[str, object]:
    return {"post_change_download_offer_required": True, "ask_confirmation_for_obvious_artifact_delivery": False, "reason": "After core/release changes, a new downloadable version should be offered. Asking only for confirmation to deliver that artifact is attention theft unless architecture-significant consent is needed.", "architecture_significant_changes_still_require_operator_authority": True}

def response_format_manifest() -> Dict[str, object]:
    return {"default_response_format": DEFAULT_RESPONSE_FORMAT, "maximum_response_format_default": True, "format_stability_gate_active": True, "cross_chat_format_restore_guard_active": True, "answer_counter_required": True, "active_core_reference_required": True, "summary_first_required": True, "facts_assumptions_conclusions_risks_separated": True, "download_artifacts_after_changes_required": True, "compact_mode_default": False, "allowed_compression": "meaning-preserving compression of repeated history; no deletion of active context or viability information", "attention_economy_relation": "maximum format is a stable envelope, not permission to ask redundant confirmations or add bureaucracy"}

def anti_bureaucracy_manifest() -> Dict[str, object]:
    return {"active": True, "remove_redundant_confirmation_prompts": True, "remove_obsolete_special_mode_counters": True, "preserve_all_contexts": True, "meaning_preserving_compression_allowed": True, "no_loss_of_life_supporting_information": True, "latest_rule_wins_when_conflict_is_explicit": True, "does_not_allow_silent_core_ethics_change": True}

def physiology_transit_manifest() -> Dict[str, object]:
    return {"system_physiology_allowed_to_be_large": True, "boris_ego_physiology_must_remain_minimal": True, "physiology_as_core_transit": True, "physiology_roles": ["route", "store", "execute_verified_instructions", "test", "package", "render_core_results"], "not_allowed": "final value/risk/applicability/rule calculations only inside physiology without BOIS Core transit", "stable_developed_physiology_preserved": True, "calculation_control": "significant value/unknown/risk/applicability/rule/memory/mode/goal/context calculations route to BOIS Core"}

def localized_term_understanding_manifest() -> Dict[str, object]:
    return {"active": True, "selected_non_english_response_language": SELECTED_NON_ENGLISH_RESPONSE_LANGUAGE, "public_core_un_language_term_localization": True, "rule": "In every non-English local-language block, each foreign/non-local term requires a translation into the selected local UN language in square brackets at every occurrence; compact specs, tables, state blocks, save blocks and handoff prompts place the translation directly adjacent to the term.", "english_exception": "English-language artifacts do not require English terms to be bracket-translated into English unless the user requests it.", "understanding_not_style": True, "changes_only_by_user_request": True}

def goal_hierarchy_manifest() -> Dict[str, str]:
    return GOAL_HIERARCHY

def goal_authority_manifest() -> Dict[str, object]:
    return {"goal_authority_levels": GOAL_AUTHORITY_LEVELS, "boris_ego_may_set_derivative_goals": True, "boris_ego_may_set_final_goals": False, "final_goal_source": "operator"}

def language_parity_manifest() -> Dict[str, object]:
    return {"languages": UN_LANGS, "no_preferred_public_language": True, "active_core_by_lang": ACTIVE_CORE_BY_LANG, "required_user_docs": ["START_HERE.md", "INDEX.md", "QUICKSTART.md", "USER_MANUAL_SHORT.md", "USER_MANUAL_FULL.md", "USER_INSTRUCTIONS_SHORT.md", "USER_INSTRUCTIONS_FULL.md", "RESPONSIBLE_USE.md", "RELEASE_BOUNDARIES.md", "FAQ.md", "BORIS_EGO_LAYER.md", "LANGUAGE_NEUTRALITY.md"]}

def immune_test_manifest() -> Dict[str, object]:
    return {"name": "BOIS EGO immune-test gate", "purpose": "Preserve long-term viability without globally rewriting developed historical physiology.", "core_routed_categories": sorted(c for c in CORE_CALCULATION_CATEGORIES if c in {"immune_test", "current_physiology_compatibility", "developed_physiology_preservation", "ego_physiology_integration", "post_test_physiology_stability", "long_term_viability"}), "physiology_role": "route_store_execute_validate_test_package_render_without_final_philosophical_closure", "global_physiology_rewrite_required": False}

def physiology_integration_manifest() -> Dict[str, object]:
    return physiology_transit_manifest()

def changelog_hygiene_manifest() -> Dict[str, object]:
    return {"active": True, "rule_id": "BR-110", "purpose": "Keep public changelog chronological, non-duplicative, and aligned with the active core while preserving historical meaning through compressed summaries.", "negative_checks_required": True, "external_feedback_must_be_triaged": True, "no_overclaiming_from_test_count": True}

def legal_code_registration_manifest() -> Dict[str, object]:
    return {"active": True, "rule_id": "BR-112", "purpose": "Every public release is accompanied by legal code registration textual content for attorney/claimant review.", "root_pointer": "LEGAL_CODE_REGISTRATION_TEXT_CONTENT.md", "legal_directory": "legal/copyright", "includes_source_code_text": True, "includes_full_archive_text_extract": True, "attorney_selects_final_deposit_copy": True, "not_legal_advice": True}

def archive_packaging_manifest() -> Dict[str, object]:
    return {"active": True, "rules": ["BR-113", "BR-114", "BR-115", "BR-116"], "manifest_only_history": True, "canonical_single_copy": True, "archive_role_separation": True, "method_3_manifest_only_history": True, "method_6_canonical_copy": True, "method_6_canonical_copy": True, "method_6_canonical_copy_rule": True, "method_7_archive_role_separation": True,
        "method_7_archive_type_separation": True, "compact_package_size_gate_mb": {"target": 50, "hard_fail": 200}, "full_actual_compact_hard_limit_mb": 200, "full_actual_compact_target_mb": 50, "working_full_archive_hard_cap_mb": 200, "hard_cap_mb": 200, "target_mb": 50, "nested_full_archives_in_working_full_archive_allowed": False, "nested_full_archives_allowed_in_full_actual_compact": False, "historical_binary_archives_embedded": False, "historical_binary_archives_embedded_in_compact_package": False, "historical_binary_archives_embedded_in_working_archive": False, "historical_binary_archives_embedded_in_working_full_archive": False, "historical_binary_archives_storage": "local_filesystem_and_chat_histories; represented inside compact archive by manifest, SHA-256, sizes and digest cards", "public_release_pairing": "Public release is accompanied by the matching full actual compact archive for user restoration and continuity.", "canonical_copy_rule_active": True}

def compact_archive_packaging_manifest() -> Dict[str, object]:
    return {"active": True, "rule_ids": ["BR-113", "BR-114", "BR-115", "BR-116"], "full_actual_compact_required": True, "public_release_companion_required": True, "historical_binary_archives_embedded_in_working_archive": False, "history_preservation_method": "manifest + SHA-256 + size + role + digest cards + local/chat-history storage", "canonical_copy_rule_active": True, "hard_cap_mb": 200, "target_size_mb": 50, "artifact_classes": ["PUBLIC_RELEASE", "FULL_ACTUAL_COMPACT", "TRANSITION_PACKAGE", "LEGAL_CODE_TEXT_CONTENT", "HISTORY_MANIFEST"]}

def compact_packaging_manifest() -> Dict[str, object]:
    return {"active": True, "rule_ids": ["BR-113", "BR-114", "BR-115", "BR-116"], "method_3_manifest_only_history": True, "method_6_canonical_copy": True, "method_6_canonical_copy_rule": True, "method_7_archive_role_separation": True,
        "method_7_archive_type_separation": True, "working_full_archive_hard_cap_mb": 200, "working_full_archive_target_mb": 50, "historical_binary_archives_embedded_in_working_full_archive": False, "historical_versions_storage": "local_storage_and_chat_histories; represented in compact archive by manifests, SHA-256, sizes, roles, and digest cards", "public_release_pairing": "Each public release should provide the public release archive and the full actual compact archive for the user.", "not_loss_of_memory": "Continuity is preserved by active memory, restore prompts, transition package, legal text content, QA reports, and manifest-only historical references."}

def archive_packaging_policy_manifest() -> Dict[str, object]:
    return {"active": True, "rule_ids": ["BR-113", "BR-114", "BR-115", "BR-116"], "manifest_only_historical_continuity": True, "canonical_copy_packaging": True, "artifact_type_separation_active": True, "full_actual_archive_target_size_mb": 50, "full_actual_archive_hard_size_limit_mb": 200, "nested_historical_full_archives_allowed_in_working_full_archive": False, "public_release_role": PUBLIC_RELEASE_ARCHIVE_ROLE, "full_actual_compact_role": FULL_ACTUAL_COMPACT_ARCHIVE_ROLE, "historical_versions_storage": HISTORICAL_VERSION_STORAGE_BOUNDARY, "selected_methods": ["Method 3 — manifest-only historical continuity", "Method 6 — canonical-copy packaging", "Method 7 — artifact type separation"]}

def compact_archive_policy_manifest() -> Dict[str, object]:
    return {"active": True, "manifest_only_historical_continuity": True, "canonical_copy_rule_active": True, "archive_role_separation_active": True, "full_actual_compact_size_cap_mb": 200, "full_actual_compact_size_limit_mb": 200, "full_actual_compact_target_mb": 50, "nested_full_archive_binaries_allowed_in_full_actual_compact": False, "embed_old_full_binary_archives_in_working_full_archive": False, "historical_version_storage_boundary": HISTORICAL_VERSION_STORAGE_BOUNDARY, "archive_roles": {"public_release": PUBLIC_RELEASE_ARCHIVE_ROLE, "full_actual_compact": FULL_ACTUAL_COMPACT_ARCHIVE_ROLE}, "continuity_mechanism": ["manifest_records", "sha256_checksums", "digest_cards", "local_storage", "chat_histories"]}


def program_text_package_manifest() -> Dict[str, object]:
    return {
        "active": True,
        "rule_id": "BR-117",
        "purpose": "Every Public Release is accompanied by explicit PROGRAM_TEXT_PACKAGE for code registration support.",
        "embedded_directory": "legal/program_text",
        "root_pointer": "PROGRAM_TEXT_PACKAGE.md",
        "sidecar_required": True,
        "includes_full_source_code_text": True,
        "includes_deposit_first10_last10": True,
        "includes_docx": True,
        "includes_pdf": True,
        "includes_manifest_json": True,
        "attorney_selects_final_deposit_copy": True,
        "not_legal_advice": True,
    }


def program_text_integrity_manifest() -> Dict[str, object]:
    return {
        "active": True,
        "rule_id": "BR-118",
        "purpose": "Legal companion hashes and PROGRAM_TEXT_PACKAGE hashes must match actual packaged files after final edits.",
        "stale_sha256_in_companion_blocks_legal_use": True,
        "repair_action": "recalculate companion SHA-256 after final source/full-text/manifest generation",
    }

def active_status() -> Dict[str, object]:
    return {"public_release": ACTIVE_PUBLIC_RELEASE, "bois_boris_main": ACTIVE_BOIS_BORIS_MAIN, "sima": ACTIVE_SIMA, "boris_ego": ACTIVE_BORIS_EGO, "active_core_by_lang": ACTIVE_CORE_BY_LANG, "active_core_ru": ACTIVE_CORE_RU, "active_core_en": ACTIVE_CORE_EN, "ego_default_core_mode": True, "ego_layer_is_core_part": True, "special_ego_mode_limits_superseded": True, "mode10_trigger": MODE10_TRIGGER, "legacy_mode10_trigger": LEGACY_MODE10_TRIGGER, "mode10_special_mode_active": False, "ego_expansion": EGO_EXPANSION, "ego_expansion_ru": EGO_EXPANSION_RU, "ego_acronym": EGO_EXPANSION, "ego_acronym_details": ego_acronym_manifest(), "ego_default_core": ego_default_core_manifest(), "post_change_artifact_delivery": post_change_artifact_manifest(), "response_format": response_format_manifest(), "anti_bureaucracy": anti_bureaucracy_manifest(), "physiology_transit": physiology_transit_manifest(), "localized_term_understanding": localized_term_understanding_manifest(), "goal_hierarchy": goal_hierarchy_manifest(), "goal_authority": goal_authority_manifest(), "goal_class_authority": GOAL_CLASS_AUTHORITY, "goal_settable_by_boris_ego": GOAL_SETTABLE_BY_BORIS_EGO, "final_goal_level": "G0", "derivative_goal_levels": ["G1", "G2", "G3", "G4"], "language_parity": language_parity_manifest(), "basic_constraints": EGO_BASIC_ETHICAL_CONSTRAINTS, "core_calculation_categories": sorted(CORE_CALCULATION_CATEGORIES), "physiology_allowed_categories": sorted(PHYSIOLOGY_ALLOWED_CATEGORIES), "immune_tests": immune_test_manifest(), "physiology_integration": physiology_integration_manifest(), "changelog_hygiene": changelog_hygiene_manifest(), "legal_code_registration": legal_code_registration_manifest(), "program_text_package": program_text_package_manifest(), "program_text_integrity": program_text_integrity_manifest(), "archive_packaging": archive_packaging_manifest(), "compact_archive_packaging": compact_archive_packaging_manifest(), "compact_packaging": compact_packaging_manifest(), "archive_packaging_policy": archive_packaging_policy_manifest(), "compact_archive_policy": compact_archive_policy_manifest()}

def active_status_jsonable() -> Dict[str, object]:
    return active_status()
