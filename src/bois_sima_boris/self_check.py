# SPDX-License-Identifier: MIT
from __future__ import annotations
from pathlib import Path
from typing import Dict, List

PROHIBITED_TOKENS = [
    "requests.", "urllib.request", "http.client", "socket.",
    "subprocess", "os.system", "eval(", "exec(", "pickle.loads",
    "paramiko", "ftplib", "smtplib"
]
SCAN_EXTENSIONS = {".py", ".yml", ".yaml"}
IGNORED_DIRS = {
    ".git", ".github", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache",
    ".venv", "venv", "env", ".env", "build", "dist", ".eggs", "site-packages",
}
IGNORED_SUFFIXES = (".egg-info",)


def _ignored(path: Path) -> bool:
    parts = set(path.parts)
    if parts & IGNORED_DIRS:
        return True
    return any(part.endswith(IGNORED_SUFFIXES) for part in path.parts)


def run_self_check(root: Path) -> Dict[str, object]:
    findings: List[Dict[str, str]] = []
    root = root.resolve()
    for path in root.rglob("*"):
        if _ignored(path):
            continue
        if path.is_dir() or path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        rel = str(path.relative_to(root))
        # Do not flag this policy file for listing the prohibited tokens.
        if rel.endswith("self_check.py") or rel.endswith("SELF_CHECK_POLICY.md"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            findings.append({"file": rel, "token": "read_error", "detail": str(exc)})
            continue
        for token in PROHIBITED_TOKENS:
            if token in text:
                findings.append({"file": rel, "token": token, "detail": "Potentially prohibited feature for public safe baseline."})
    return {
        "ok": not findings,
        "policy": "Public safe baseline: no network, no shell, no dynamic code execution, no autonomous action.",
        "ignored_dirs": sorted(IGNORED_DIRS),
        "findings": findings,
    }
