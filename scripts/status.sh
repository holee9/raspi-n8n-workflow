#\!/bin/bash
# PROTOCOL ZERO: System Status Check

echo "=== PROTOCOL ZERO System Status ==="
echo ""

# Docker status
echo "Docker:"
docker --version
echo ""

# Containers
echo "Containers:"
docker ps --format "table {{.Names}}	{{.Status}}	{{.Ports}}" | grep -E "NAMES|n8n|ollama|qdrant"
echo ""

# n8n health
echo "n8n Health:"
curl -s http://localhost:5678/healthz && echo " OK" || echo " FAILED"
echo ""

# Ollama health
echo "Ollama Health:"
curl -s http://localhost:11434/api/tags > /dev/null && echo " OK" || echo " FAILED"
echo ""

# Qdrant health
echo "Qdrant Health:"
curl -s http://localhost:6333/health && echo " OK" || echo " FAILED"
echo ""

# Memory
echo "Memory Usage:"
free -h
echo ""

# Disk
echo "Disk Usage:"
df -h | grep -E "Filesystem|/"
