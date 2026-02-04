# PROTOCOL ZERO: Autonomous Hybrid AI Architect on Raspberry Pi 5

## IMPORTANT: Work Process Rules

**BEFORE starting any work, you MUST:**
1. Read memory/WORK_PROCESS_RULES.md
2. Check memory/errors.log for past errors
3. Check memory/solutions.md for known solutions
4. Check memory/current-task.md to resume interrupted work

See memory/WORK_PROCESS_RULES.md for complete process.

---

## Overview

A self-sustaining, cost-optimized AI automation ecosystem on Raspberry Pi 5.

### Architecture

```
User Request -> n8n Orchestrator -> [Ollama (Free) | Claude API (Paid)] -> Qdrant (Memory)
```

### Hybrid Routing

| Complexity | Destination |
|------------|-------------|
| < 5 | Ollama (Free) |
| > 8 | Claude API (Paid) |

## Quick Start

```bash
# Clone
git clone https://github.com/holee9/raspi-n8n-workflow.git
cd raspi-n8n-workflow

# Bootstrap (RPi5)
./scripts/bootstrap.sh

# Start services
docker-compose up -d

# Pull models
./scripts/pull-models.sh
```

## Project Structure

```
raspi-n8n-workflow/
├── memory/                 # ERROR TRACKING - READ FIRST!
│   ├── WORK_PROCESS_RULES.md   # MANDATORY pre-work check
│   ├── errors.log              # All errors with solutions
│   ├── solutions.md            # Known solutions
│   └── current-task.md         # Resume interrupted work
├── scripts/                # Implementation scripts
├── n8n/workflows/          # n8n workflow templates
├── docker-compose.yml      # Container orchestration
├── README.md               # This file
└── DEPLOYMENT.md           # Deployment guide
```

## Scripts Reference

| Script | Purpose |
|--------|---------|
| bootstrap.sh | System setup and configuration |
| bridge.py | n8n API management |
| init-qdrant.py | Initialize vector collections |
| pull-models.sh | Pull Ollama models |
| status.sh | System health check |

## Services

- n8n UI: http://localhost:5678
- Ollama API: http://localhost:11434
- Qdrant Dashboard: http://localhost:6333/dashboard

## Troubleshooting

See memory/solutions.md for common issues and solutions.

## License

MIT License
