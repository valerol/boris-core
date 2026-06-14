# SPDX-License-Identifier: MIT
"""Local SIMA analyzer.

This module deliberately avoids network calls, operating-system command execution, dynamic code execution,
and autonomous action. It converts a local JSON description of an object/substrate into
an auditable candidate philosophical-machine report.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Tuple

REQUIRED_TOP_LEVEL = ["object_id", "object_type", "domain", "value_interface", "substrate", "observations"]
SUBSTRATE_FIELDS = ["units", "channels", "memory", "costs", "failure_modes", "stop_authority"]
VALUE_FIELDS = ["goals", "constraints", "forbidden_losses"]

@dataclass
class Finding:
    id: str
    severity: str
    message: str
    recommendation: str

@dataclass
class Oper:
    id: str
    trigger: str
    distinction: str
    evidence: str
    carrier: str
    authority: str
    value_risk_gate: str
    transformation: str
    memory_write: str
    closure_signal: str
    transition_residue: str
    cost: str
    confidence: str


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def validate_object(obj: Dict[str, Any]) -> Tuple[bool, List[Finding]]:
    findings: List[Finding] = []
    for field in REQUIRED_TOP_LEVEL:
        if field not in obj:
            findings.append(Finding(
                id=f"missing_{field}", severity="high",
                message=f"Missing top-level field: {field}",
                recommendation=f"Add `{field}` to the object description."
            ))
    substrate = obj.get("substrate", {}) if isinstance(obj.get("substrate", {}), dict) else {}
    for field in SUBSTRATE_FIELDS:
        if not _as_list(substrate.get(field)):
            findings.append(Finding(
                id=f"substrate_missing_{field}", severity="medium",
                message=f"Substrate declaration lacks `{field}`.",
                recommendation=f"Describe substrate `{field}` before claiming accountability."
            ))
    vi = obj.get("value_interface", {}) if isinstance(obj.get("value_interface", {}), dict) else {}
    for field in VALUE_FIELDS:
        if not _as_list(vi.get(field)):
            findings.append(Finding(
                id=f"value_missing_{field}", severity="medium",
                message=f"Value interface lacks `{field}`.",
                recommendation=f"Declare value-interface `{field}` to avoid hidden authority."
            ))
    observations = obj.get("observations", [])
    if not isinstance(observations, list) or not observations:
        findings.append(Finding(
            id="no_observations", severity="high",
            message="No observations supplied; SIMA cannot infer operature from declarations only.",
            recommendation="Add at least one observed episode with trigger, evidence, action, memory, closure and transition."
        ))
    return not any(f.severity == "high" for f in findings), findings


def observation_to_oper(obs: Dict[str, Any], idx: int) -> Oper:
    def g(*names: str, default: str = "unknown") -> str:
        for name in names:
            val = obs.get(name)
            if isinstance(val, str) and val.strip():
                return val.strip()
            if isinstance(val, (int, float)):
                return str(val)
        return default
    return Oper(
        id=g("id", default=f"oper-{idx:03d}"),
        trigger=g("trigger", "event"),
        distinction=g("distinction", "distinguished"),
        evidence=g("evidence", "signal"),
        carrier=g("carrier", "actor"),
        authority=g("authority", "authorized_by"),
        value_risk_gate=g("value_risk_gate", "risk", "gate"),
        transformation=g("transformation", "action", "change"),
        memory_write=g("memory_write", "memory", "log"),
        closure_signal=g("closure_signal", "closure"),
        transition_residue=g("transition_residue", "transition"),
        cost=g("cost", "attention_cost"),
        confidence=g("confidence", default="medium"),
    )


def infer_candidate_machine(obj: Dict[str, Any], opers: List[Oper]) -> Dict[str, Any]:
    substrate = obj.get("substrate", {}) if isinstance(obj.get("substrate", {}), dict) else {}
    vi = obj.get("value_interface", {}) if isinstance(obj.get("value_interface", {}), dict) else {}
    return {
        "name": "candidate_transition_oriented_philosophical_machine",
        "confidence": "medium" if opers else "low",
        "M": {
            "O_ontology": "objects are inferred from domain entities, observations, triggers and evidence fields",
            "E_epistemology": "evidence is treated as observed signals, logs and stated evidence fields, not as final truth",
            "A_agency": f"agency carriers: {', '.join(map(str, _as_list(substrate.get('units')))) or 'unknown'}; stop authority: {', '.join(map(str, _as_list(substrate.get('stop_authority')))) or 'unknown'}",
            "V_value_interface": {
                "goals": _as_list(vi.get("goals")),
                "constraints": _as_list(vi.get("constraints")),
                "forbidden_losses": _as_list(vi.get("forbidden_losses")),
            },
            "R_risk_model": f"risks are drawn from value gates, failure modes and observations: {', '.join(map(str, _as_list(substrate.get('failure_modes')))) or 'unknown'}",
            "C_closure_rule": "closure is inferred from closure_signal fields; missing closure means unresolved cycle",
            "T_transition_rule": "transition is inferred from transition_residue and memory_write fields",
        }
    }


def analyze_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    ok, findings = validate_object(obj)
    observations = obj.get("observations", []) if isinstance(obj.get("observations", []), list) else []
    opers = [observation_to_oper(o if isinstance(o, dict) else {}, i + 1) for i, o in enumerate(observations)]
    candidate = infer_candidate_machine(obj, opers)
    risk_flags = []
    for f in findings:
        if f.severity in ("high", "medium"):
            risk_flags.append(asdict(f))
    operome = {
        "definition": "Set of observed or candidate opers in the selected observation window.",
        "object_id": obj.get("object_id", "unknown"),
        "count": len(opers),
        "confidence": "medium" if len(opers) >= 3 else ("low" if opers else "none"),
        "opers": [asdict(o) for o in opers]
    }
    return {
        "schema_version": "sima-output-v0.2-public",
        "object_id": obj.get("object_id", "unknown"),
        "object_type": obj.get("object_type", "unknown"),
        "domain": obj.get("domain", "unknown"),
        "input_validation_passed": ok,
        "substrate_declaration": obj.get("substrate", {}),
        "value_interface": obj.get("value_interface", {}),
        "operome": operome,
        "candidate_machines": [candidate],
        "risk_flags": risk_flags,
        "limits": [
            "This is a reconstruction, not a final truth.",
            "Do not infer consciousness, legal authority, or human suitability from this output.",
            "Do not use for autonomous coercive governance or decisions about rights, employment, benefits, law enforcement, or military targeting without independent lawful human process."
        ],
        "next_step": "Collect more observations or run an experience test before converting any finding into an instruction."
    }


def to_markdown(result: Dict[str, Any], lang: str = "en") -> str:
    from .locales import t
    lines = []
    lines.append(f"# {t(lang, 'analysis_title')}: {result.get('object_id')}\n")
    lines.append(f"{t(lang, 'object_type')}: `{result.get('object_type')}`\n")
    lines.append(f"{t(lang, 'validation')}: **{result.get('input_validation_passed')}**\n")
    lines.append(f"## {t(lang, 'candidate')}\n")
    for cm in result.get("candidate_machines", []):
        lines.append(f"- Name: `{cm.get('name')}`")
        lines.append(f"- {t(lang, 'confidence')}: `{cm.get('confidence')}`")
        lines.append("\n### M = <O,E,A,V,R,C,T>\n")
        for k, v in cm.get("M", {}).items():
            lines.append(f"- **{k}**: {v}")
    lines.append(f"\n## {t(lang, 'operome')}\n")
    op = result.get("operome", {})
    lines.append(f"Count: **{op.get('count')}**; {t(lang, 'confidence')}: **{op.get('confidence')}**\n")
    for item in op.get("opers", []):
        lines.append(f"- `{item.get('id')}`: trigger={item.get('trigger')}; evidence={item.get('evidence')}; closure={item.get('closure_signal')}; transition={item.get('transition_residue')}")
    lines.append(f"\n## {t(lang, 'risk_flags')}\n")
    if result.get("risk_flags"):
        for r in result["risk_flags"]:
            lines.append(f"- **{r.get('severity')}** `{r.get('id')}`: {r.get('message')} Recommendation: {r.get('recommendation')}")
    else:
        lines.append(f"- {t(lang, 'no_risk')}")
    lines.append(f"\n## {t(lang, 'limits')}\n")
    for limit in result.get("limits", []):
        lines.append(f"- {limit}")
    lines.append(f"\n{t(lang, 'next_step')}: {result.get('next_step')}\n")
    return "\n".join(lines)
