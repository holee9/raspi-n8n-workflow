# PROTOCOL ZERO - Work Process Rules

## MANDATORY PRE-WORK CHECKLIST

### Rule 1: Memory Check (MANDATORY)
**BEFORE starting any work, you MUST:**

1. Read `memory/errors.log` - Check for previous errors
2. Read `memory/solutions.md` - Check for known solutions
3. Read `memory/lessons-learned.md` - Check for lessons
4. Read `memory/current-task.md` - Resume if interrupted

### Rule 2: Task Registration (MANDATORY)
**BEFORE starting implementation, you MUST:**

1. Create task record in `memory/current-task.md`
2. Include: task description, approach, expected files
3. Update status as work progresses

### Rule 3: Error Logging (MANDATORY)
**WHEN error occurs, you MUST:**

1. Document immediately in `memory/errors.log`
2. Add solution to `memory/solutions.md`
3. Update `memory/lessons-learned.md` if applicable

---

## Work Flow

```
START
  ↓
CHECK /memory (errors, solutions, lessons)
  ↓
REGISTER task in current-task.md
  ↓
EXECUTE work (update current-task.md as you go)
  ↓
IF error → LOG to errors.log + ADD solution
  ↓
COMPLETE → Update current-task.md status
  ↓
END
```

---

## Quick Reference

| Check | File | Purpose |
|-------|------|---------|
| Pre-work | `memory/errors.log` | What went wrong before |
| Pre-work | `memory/solutions.md` | How to fix known issues |
| Pre-work | `memory/current-task.md` | Resume interrupted work |
| During | `memory/current-task.md` | Track progress |
| Post-error | `memory/errors.log` | Log new error |
| Post-error | `memory/solutions.md` | Document solution |

---

## This Rule is MANDATORY

**Every session must start with:**
> "Reading memory files to avoid past mistakes..."

**Every session must end with:**
> "Updating memory with lessons learned..."

---

**Non-compliance = Repeated mistakes = Wasted time**
