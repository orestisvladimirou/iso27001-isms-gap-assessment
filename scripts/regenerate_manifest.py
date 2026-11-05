#!/usr/bin/env python3
"""Deterministically refresh the committed source manifest after intentional changes."""
import json
from pathlib import Path

from validate_project import ROOT
from validate_manifest import inventory

def main():
    files = inventory()
    manifest = {
        "project": "ISO27001-ISMS-Gap-Assessment",
        "version": "0.4",
        "purpose": "Fictional non-certification portfolio exercise",
        "files": [
            {"path": path, "sha256": value["sha256"], "size": value["size"]}
            for path, value in sorted(files.items())
        ],
    }
    (ROOT / "PROJECT_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Manifest updated: {len(files)} audited files (v0.4).")

if __name__ == "__main__":
    main()
