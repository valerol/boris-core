# SPDX-License-Identifier: MIT
"""No-install source-tree shim for BOIS:SIMA&BORIS.

When the archive is unpacked, `python -m bois_sima_boris` works before
installation by adding `src/bois_sima_boris` to this package path. Installed
usage still uses the package under `src`.
"""
from pathlib import Path

_src_pkg = Path(__file__).resolve().parents[1] / "src" / "bois_sima_boris"
if _src_pkg.exists():
    __path__.append(str(_src_pkg))

__version__ = "1.4.10"
__boris_ego_version__ = "1.7"
