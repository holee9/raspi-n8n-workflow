#!/usr/bin/env python3
"""PROTOCOL ZERO: Pre-Work Check - Run before starting any work"""

import os
from datetime import datetime

print("=" * 50)
print("  PROTOCOL ZERO - PRE-WORK CHECK")
print("=" * 50)
print("")

files = [
    "memory/WORK_PROCESS_RULES.md",
    "memory/errors.log", 
    "memory/solutions.md",
    "memory/current-task.md"
]

print("Checking memory files...")
for f in files:
    status = "[OK]" if os.path.exists(f) else "[MISSING]"
    print(f"  {status} {f}")
print("")

print("Recent errors:")
if os.path.exists("memory/errors.log"):
    with open("memory/errors.log") as file:
        for line in file:
            if "error" in line.lower() or line.startswith("#"):
                print(f"  {line.strip()}")
                if sum(1 for _ in open("memory/errors.log")) > 20:
                    break
print("")

print("REMINDER: Always check memory before starting work!")
print("=" * 50)
