# PROTOCOL ZERO: Autonomous Hybrid AI Architect on Raspberry Pi 5

A self-sustaining, cost-optimized AI automation ecosystem running on Raspberry Pi 5.

## Overview

This project implements a hybrid AI system that intelligently routes tasks between:
- **Ollama** (Local Llama 3.1 - Free, Fast)
- **Claude API** (Cloud-based - High Quality, Metered)

The system orchestrates workflows through **n8n** and maintains persistent memory via **Qdrant** vector database.

## Hardware Requirements

- **Platform**: Raspberry Pi 5 (16GB RAM recommended)
- **Architecture**: ARM64 (aarch64)
- **Storage**: 32GB+ microSD or SSD

## Quick Start

### 1. Clone and Bootstrap

```bash
git clone https://github.com/holee9/raspi-n8n-workflow.git
cd raspi-n8n-workflow
./scripts/bootstrap.sh
```

### 2. Start Services

```bash
source ~/.config/protocol-zero/.env
docker-compose up -d
```

### 3. Pull Models

```bash
./scripts/pull-models.sh
```

### 4. Initialize Memory

```bash
python3 scripts/init-qdrant.py
```

### 5. Access Services

- n8n UI: http://localhost:5678
- Ollama API: http://localhost:11434
- Qdrant Dashboard: http://localhost:6333/dashboard

## Scripts Reference

| Script | Purpose |
|--------|---------|
| bootstrap.sh | System setup and configuration |
| bridge.py | n8n API management |
| init-qdrant.py | Initialize vector collections |
| pull-models.sh | Pull Ollama models |
| status.sh | System health check |

### bridge.py Commands

```bash
# Health check
python3 scripts/bridge.py health

# List workflows
python3 scripts/bridge.py list

# Import workflow
python3 scripts/bridge.py import -f n8n/workflows/master-router.json
```

## Hybrid Routing Logic

| Complexity | Task Type | Destination |
|------------|-----------|-------------|
| < 5 | simple | Ollama (Free) |
| > 8 | complex | Claude API (Metered) |

## Troubleshooting

Check `memory/solutions.md` for common issues and solutions.

## License

MIT License
