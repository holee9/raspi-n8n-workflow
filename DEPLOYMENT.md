# PROTOCOL ZERO - Deployment Guide

## Pre-Deployment Checklist

- [ ] Raspberry Pi 5 (16GB) ready
- [ ] Raspberry Pi OS Bookworm (64-bit) installed
- [ ] Internet connection available
- [ ] At least 32GB free storage
- [ ] Claude API key (optional, for hybrid routing)

## Step-by-Step Deployment

### 1. System Preparation

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Set hostname (optional)
sudo hostnamectl set-hostname ai-pi
```

### 2. Clone Repository

```bash
cd ~
git clone https://github.com/holee9/raspi-n8n-workflow.git
cd raspi-n8n-workflow
```

### 3. Run Bootstrap

```bash
./scripts/bootstrap.sh
```

This will:
- Configure 8GB swap
- Install Docker and dependencies
- Install Node.js 20.x LTS
- Set up environment variables
- Create project structure

### 4. Configure Environment

```bash
# Edit environment file
nano ~/.config/protocol-zero/.env

# Add your Claude API key (optional)
export CLAUDE_API_KEY=sk-ant-your-key-here

# Save and source
source ~/.config/protocol-zero/.env
```

### 5. Copy docker-compose.yml

```bash
mkdir -p ~/protocol-zero
cp docker-compose.yml ~/protocol-zero/
cd ~/protocol-zero
```

### 6. Start Services

```bash
docker-compose up -d
```

### 7. Verify Services

```bash
./scripts/status.sh
```

### 8. Pull Models

```bash
./scripts/pull-models.sh
```

### 9. Initialize Memory

```bash
python3 scripts/init-qdrant.py
```

### 10. Import Workflows

```bash
# Import master router
python3 scripts/bridge.py import -f n8n/workflows/master-router.json

# Import research skill
python3 scripts/bridge.py import -f n8n/workflows/research-skill.json
```

## Post-Deployment

### Access n8n

1. Open browser: http://localhost:5678
2. Create admin account
3. Verify workflows are imported

### Test Hybrid Router

```bash
curl -X POST http://localhost:5678/webhook/hybrid-router   -H "Content-Type: application/json"   -d '{"text": "Hello, world!"}'
```

## Troubleshooting

### Containers won't start

```bash
# Check logs
docker-compose logs

# Check individual container
docker logs n8n
docker logs ollama
docker logs qdrant
```

### Out of Memory

```bash
# Check swap
free -h

# If swap < 8GB, re-run bootstrap
./scripts/bootstrap.sh
```

### n8n not accessible

```bash
# Check if n8n is running
docker ps | grep n8n

# Check n8n logs
docker logs n8n
```

## Maintenance

### Update System

```bash
# Stop containers
docker-compose down

# Update system
sudo apt update && sudo apt upgrade -y

# Restart containers
docker-compose up -d
```

### Backup Data

```bash
# Backup n8n data
tar -czf n8n-backup-$(date +%Y%m%d).tar.gz ~/protocol-zero/n8n/data

# Backup Ollama models
tar -czf ollama-backup-$(date +%Y%m%d).tar.gz ~/protocol-zero/ollama

# Backup Qdrant
tar -czf qdrant-backup-$(date +%Y%m%d).tar.gz ~/protocol-zero/qdrant
```

## Monitoring

Use status script:

```bash
./scripts/status.sh
```

Expected output:
- Docker: version info
- Containers: All 3 running
- n8n Health: OK
- Ollama Health: OK
- Qdrant Health: OK

## Security Notes

1. n8n is configured for local access only
2. Claude API key stored in environment file
3. No external ports exposed except local access
4. Add firewall rules if exposing services

---

**PROTOCOL ZERO** - Deployment Complete
