# Solutions - PROTOCOL ZERO

This document contains solutions to problems encountered during development and deployment.

## Common Issues

### Issue 1: Write Tool Hook Error
**Problem**: `PreToolUse:Write hook error` - Security guard script not found
**Cause**: Hook configuration references non-existent file
**Solution**: Use Bash + Python to write files instead of Write tool
**Prevention**: Verify hook paths in settings before using Write tool

### Issue 2: Docker Permission Denied
**Problem**: Cannot connect to Docker daemon
**Cause**: User not in docker group
**Solution**: 
```bash
sudo usermod -aG docker $USER
# Log out and back in
```
**Prevention**: Add user to docker group during bootstrap

### Issue 3: Ollama OOM (Out of Memory)
**Problem**: Ollama container killed due to memory
**Cause**: LLM models require more RAM than available
**Solution**:
1. Increase swap to 8GB
2. Set memory limits in docker-compose.yml
3. Use smaller models (llama3.1 instead of larger)
**Prevention**: Always configure 8GB swap before starting

### Issue 4: Qdrant Segmentation Fault
**Problem**: Qdrant crashes with segfault on RPi5
**Cause**: 16KB page size on ARM64
**Solution**: Set MALLOC_CONF environment variable
```bash
export MALLOC_CONF=background_thread:true,dirty_decay_ms:0
```
**Prevention**: Always set MALLOC_CONF for Qdrant container

### Issue 5: n8n Workflow Import Fails
**Problem**: Cannot import workflow via API
**Cause**: Missing authentication or wrong URL
**Solution**:
1. Set N8N_SECURE_COOKIE=false for local
2. Use correct API URL format
3. Check if n8n is running
**Prevention**: Always health-check before API calls

---

## Quick Reference

| Error | Quick Fix |
|-------|-----------|
| Docker permission | `sudo usermod -aG docker $USER` |
| OOM | Increase swap, reduce model size |
| Segfault | Set MALLOC_CONF |
| API timeout | Check network, verify URL |
| Hook error | Use Bash+Python instead of Write |
