# SPDX-License-Identifier: MIT
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .sima import analyze_object, validate_object, to_markdown
from .self_check import run_self_check
from .locales import t, LANGS
from .ego import active_status_jsonable


def load_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(json.dumps({"ok": False, "error": "file_not_found", "path": path}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": "invalid_json", "path": path, "line": exc.lineno, "column": exc.colno, "message": exc.msg}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)


def cmd_analyze(args):
    obj = load_json(args.input)
    result = analyze_object(obj)
    result["language"] = args.lang
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    if args.md:
        Path(args.md).write_text(to_markdown(result, args.lang), encoding="utf-8")
    return 0 if result.get("input_validation_passed") else 2


def cmd_validate(args):
    obj = load_json(args.input)
    ok, findings = validate_object(obj)
    print(json.dumps({"ok": ok, "language": args.lang, "findings": [f.__dict__ for f in findings]}, ensure_ascii=False, indent=2))
    return 0 if ok else 2


def cmd_self_check(args):
    result = run_self_check(Path(args.root))
    result["language"] = args.lang
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 3



def cmd_ego_status(args):
    result = active_status_jsonable()
    result["language"] = args.lang
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

def cmd_docs(args):
    names = [
        "START_HERE.md", "README.md", "INSTALL.md", "QUICKSTART.md",
        "USER_INSTRUCTIONS_SHORT.md", "USER_INSTRUCTIONS_FULL.md",
        "USER_MANUAL_SHORT.md", "USER_MANUAL_FULL.md", "LANGUAGE_NEUTRALITY.md",
        "TECHNICAL_OVERVIEW.md", "ARCHITECTURE.md", "DATA_MODEL_AND_SCHEMAS.md",
        "CLI_REFERENCE.md", "SIMA_ANALYZER_GUIDE.md", "LOCAL_BORIS_CONSTRUCTION_GUIDE.md",
        "TESTING_AND_SELF_TESTING.md", "CONTROLLED_EVOLUTIONARY_IMPROVEMENT.md",
        "CAPABILITY_AND_LIMITATION_MATRIX.md", "SECURITY.md", "RESPONSIBLE_USE.md",
        "RELEASE_BOUNDARIES.md", "PRIVACY_AND_ANONYMIZATION.md", "MAINTENANCE_PAUSE_NOTICE.md",
        "FINAL_RELEASE_READINESS.md", "FAQ.md", "BORIS_EGO_LAYER.md", "RESPONSE_FORMAT_STABILITY.md", "ANTI_BUREAUCRATIC_REVISION.md", "TERM_TRANSLATION_UNDERSTANDING.md", "ARCHIVE_PACKAGING_POLICY.md", "FULL_ACTUAL_COMPACT_ARCHIVE.md", "LEGAL_CODE_REGISTRATION_TEXT_CONTENT.md", "FULL_ACTUAL_COMPACT.md",
    ]
    localized_root = Path("docs") / args.lang
    base = localized_root if localized_root.exists() else Path("docs")
    docs = []
    for item in [Path("START_HERE_UN.md"), Path("UN_LANGUAGE_INDEX.md"), Path("docs/INDEX.md"), Path("LEGAL_CODE_REGISTRATION_TEXT_CONTENT.md")]:
        if item.exists():
            docs.append(str(item))
    index = localized_root / "INDEX.md"
    if index.exists():
        docs.append(str(index))
    for name in names:
        path = base / name
        if path.exists():
            docs.append(str(path))
    print(t(args.lang, "docs_title"))
    for item in docs:
        print(f"- {item}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="bois-sima-boris", description="Local SIMA analyzer for BOIS:SIMA&BORIS anonymized public package")
    parser.add_argument("--lang", choices=LANGS, default="en", help="User-interface language for documentation pointers and markdown reports")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_lang_option(p):
        # Allows both `bois-sima-boris --lang ru docs` and `bois-sima-boris docs --lang ru`.
        p.add_argument("--lang", choices=LANGS, default=argparse.SUPPRESS, help="User-interface language")

    p = sub.add_parser("analyze", help="Analyze a local JSON object description")
    p.add_argument("input")
    p.add_argument("--out")
    p.add_argument("--md")
    add_lang_option(p)
    p.set_defaults(func=cmd_analyze)
    p = sub.add_parser("validate", help="Validate input schema minimally")
    p.add_argument("input")
    add_lang_option(p)
    p.set_defaults(func=cmd_validate)
    p = sub.add_parser("self-check", help="Scan package for prohibited implementation features")
    p.add_argument("--root", default=".")
    add_lang_option(p)
    p.set_defaults(func=cmd_self_check)

    p = sub.add_parser("ego-status", help="Print active BORIS EGO public-kernel status")
    add_lang_option(p)
    p.set_defaults(func=cmd_ego_status)
    p = sub.add_parser("docs", help="Print static documentation index")
    add_lang_option(p)
    p.set_defaults(func=cmd_docs)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
