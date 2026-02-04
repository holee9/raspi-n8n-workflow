# Lessons Learned - PROTOCOL ZERO

Last Updated: 2026-02-04

## Key Principles

### 1. Memory Management on RPi5
- **Lesson**: RPi5 has 16KB page size (not 4KB like x86)
- **Impact**: Memory allocators may misbehave
- **Rule**: Always set `MALLOC_CONF` for containers

### 2. Cost-Aware Routing
- **Lesson**: Not all tasks need expensive Claude API
- **Impact**: Can save significant cost with smart routing
- **Rule**: Route simple tasks to Ollama, complex to Claude

### 3. Swap is Critical
- **Lesson**: 16GB RAM not enough for LLM loading
- **Impact**: OOM kills without swap
- **Rule**: Always configure 8GB swap before starting

### 4. Container Dependencies
- **Lesson**: n8n depends on Ollama and Qdrant
- **Impact**: Wrong startup order causes failures
- **Rule**: Use healthcheck and depends_on in compose

### 5. File Writing in Claude Code
- **Lesson**: Write tool may have hooks that fail
- **Impact**: Cannot write files directly
- **Rule**: Have fallback method (Bash+Python)

## Development Workflow

1. **Plan**: Write SPEC in EARS format
2. **Implement**: Create scripts and configs
3. **Test**: Verify on actual RPi5 hardware
4. **Document**: Update README and memory
5. **Iterate**: 3 rounds of verification

## Critical Path

1. Bootstrap script must complete successfully
2. All containers must pass healthcheck
3. Master Router workflow must be imported
4. Ollama models must be pre-loaded
5. Qdrant collection must be initialized

## Red Flags

- Swap less than 8GB
- MALLOC_CONF not set
- Container restart loops
- API timeouts > 10s
- Memory usage > 90%

## Success Indicators

- Containers stable for 24 hours
- Routing decisions visible in logs
- Local inference > 80%
- API cost under $5/month

---

**Remember**: Document every error and solution immediately. Future you will thank current you.
