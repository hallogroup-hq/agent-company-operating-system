#!/usr/bin/env python3
"""Deterministic monitor example.

Produce a small, normalized snapshot. The scheduler/runner should compare this
output with the previous output and only invoke an LLM/agent when it changes.
"""

from __future__ import annotations
import json
from pathlib import Path
import shutil


def snapshot() -> dict:
    usage = shutil.disk_usage(Path.home())
    free_gb = round(usage.free / (1024 ** 3), 1)

    # Add only stable, high-signal checks. Avoid timestamps and noisy counters.
    return {
        "disk_low": free_gb < 10,
        "required_paths": {
            "shared_knowledge": (Path.home() / "shared-knowledge").exists(),
        },
    }


if __name__ == "__main__":
    print(json.dumps(snapshot(), sort_keys=True, separators=(",", ":")))
