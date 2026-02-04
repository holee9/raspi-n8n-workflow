#!/bin/bash
################################################################################
# PROTOCOL ZERO: Pre-Work Check
# MANDATORY: Run this BEFORE starting any work
################################################################################

echo "=========================================="
echo "  PROTOCOL ZERO - PRE-WORK CHECK"
echo "=========================================="
echo ""

echo "Checking memory files..."
FILES=(
    "memory/WORK_PROCESS_RULES.md"
    "memory/errors.log"
    "memory/solutions.md"
    "memory/current-task.md"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  [OK] $file"
    else
        echo "  [MISSING] $file"
    fi
done
echo ""

echo "Recent errors:"
if [ -f "memory/errors.log" ]; then
    grep -i "error" memory/errors.log | head -5
fi
echo ""

echo "Current task:"
if [ -f "memory/current-task.md" ]; then
    head -10 memory/current-task.md
fi
echo ""

echo "REMEMBER:"
echo "- Read WORK_PROCESS_RULES.md before starting"
echo "- Check errors.log for past issues"
echo "- Update current-task.md with your work"
echo "=========================================="
