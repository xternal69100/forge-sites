#!/usr/bin/env python3
"""Lance les contrats stdlib du cockpit Forge Capital depuis la racine projet."""
from __future__ import annotations
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[2]
result = subprocess.run(
    ["python3", "-m", "unittest", "tests.test_cyber_ops_contract", "tests.test_matrix_contract", "-v"],
    cwd=root,
    text=True,
)
raise SystemExit(result.returncode)
