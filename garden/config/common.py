"""
Common configurations used across the application
"""
__all__ = [
    "ROOT_PATH",
    "LOG_PATH",
]

import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    ROOT = Path(sys.executable).parent
else:
    ROOT = Path(__file__).parents[2]

ROOT_PATH = ROOT.resolve()

LOG_PATH = ROOT.joinpath("logs").resolve()
LOG_PATH.mkdir(exist_ok=True)
