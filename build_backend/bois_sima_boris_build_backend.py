# SPDX-License-Identifier: MIT
"""Dependency-free build backend for BOIS:SIMA&BORIS public package.

It exists so local offline editable installation can run without downloading a
build backend. It builds a small pure-Python wheel or editable wheel using only
Python's standard library. It performs packaging only; it does not analyze user
objects, call networks, or run shell commands.
"""
from __future__ import annotations

from pathlib import Path
import base64
import csv
import hashlib
import io
import zipfile

NAME = "bois-sima-boris"
PACKAGE = "bois_sima_boris"
VERSION = "1.4.10"
DIST_INFO = f"bois_sima_boris-{VERSION}.dist-info"


def _root() -> Path:
    return Path(__file__).resolve().parents[1]


def _metadata() -> str:
    return "\n".join([
        "Metadata-Version: 2.1",
        f"Name: {NAME}",
        f"Version: {VERSION}",
        "Summary: BOIS:SIMA&BORIS public package with EGO default-core compact packaging, compact actual packaging, legal text content and maximal-format stability",
        "Requires-Python: >=3.9",
        "License: MIT",
        "",
    ])


def _wheel() -> str:
    return "\n".join([
        "Wheel-Version: 1.0",
        "Generator: bois-sima-boris-build-backend",
        "Root-Is-Purelib: true",
        "Tag: py3-none-any",
        "",
    ])


def _entry_points() -> str:
    return "\n".join([
        "[console_scripts]",
        "bois-sima-boris = bois_sima_boris.cli:main",
        "",
    ])


def _hash(data: bytes) -> str:
    digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")
    return f"sha256={digest}"


def _write_record(zf: zipfile.ZipFile, rows: list[tuple[str, bytes | None]]):
    record_path = f"{DIST_INFO}/RECORD"
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    for path, data in rows:
        if data is None:
            writer.writerow([path, "", ""])
        else:
            writer.writerow([path, _hash(data), str(len(data))])
    writer.writerow([record_path, "", ""])
    zf.writestr(record_path, output.getvalue())


def _base_dist_info_files():
    files = []
    for rel, text in [
        (f"{DIST_INFO}/METADATA", _metadata()),
        (f"{DIST_INFO}/WHEEL", _wheel()),
        (f"{DIST_INFO}/entry_points.txt", _entry_points()),
    ]:
        files.append((rel, text.encode("utf-8")))
    return files


def get_requires_for_build_wheel(config_settings=None):
    return []


def get_requires_for_build_editable(config_settings=None):
    return []


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    dist = Path(metadata_directory) / DIST_INFO
    dist.mkdir(parents=True, exist_ok=True)
    (dist / "METADATA").write_text(_metadata(), encoding="utf-8")
    (dist / "WHEEL").write_text(_wheel(), encoding="utf-8")
    (dist / "entry_points.txt").write_text(_entry_points(), encoding="utf-8")
    return DIST_INFO


def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return prepare_metadata_for_build_wheel(metadata_directory, config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    wheel_name = f"bois_sima_boris-{VERSION}-py3-none-any.whl"
    wheel_path = Path(wheel_directory) / wheel_name
    rows: list[tuple[str, bytes | None]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        src_pkg = _root() / "src" / PACKAGE
        for path in sorted(src_pkg.rglob("*.py")):
            rel = f"{PACKAGE}/{path.relative_to(src_pkg).as_posix()}"
            data = path.read_bytes()
            zf.writestr(rel, data)
            rows.append((rel, data))
        for rel, data in _base_dist_info_files():
            zf.writestr(rel, data)
            rows.append((rel, data))
        _write_record(zf, rows)
    return wheel_name


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    wheel_name = f"bois_sima_boris-{VERSION}-py3-none-any.whl"
    wheel_path = Path(wheel_directory) / wheel_name
    src = (_root() / "src").resolve().as_posix() + "\n"
    pth_name = "bois_sima_boris_editable.pth"
    pth_data = src.encode("utf-8")
    rows: list[tuple[str, bytes | None]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(pth_name, pth_data)
        rows.append((pth_name, pth_data))
        for rel, data in _base_dist_info_files():
            zf.writestr(rel, data)
            rows.append((rel, data))
        _write_record(zf, rows)
    return wheel_name
