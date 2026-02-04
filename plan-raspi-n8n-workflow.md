# PROTOCOL ZERO: Autonomous Hybrid AI Architect on Raspberry Pi 5

## 1. MISSION DIRECTIVE
Establish a self-sustaining, cost-optimized AI automation ecosystem on Raspberry Pi 5 (16GB). The system must utilize **Claude Code (Opus)** for architectural construction and transition to a **Hybrid Engine (Ollama + Claude API)** for operational efficiency.

---

## 2. HARDWARE & KERNEL OPTIMIZATION (CRITICAL)
**Target:** Raspberry Pi 5 (ARM64, 16KB Page Size)
**Objective:** Prevent segmentation faults in memory-intensive vector databases.

### 2.1. Kernel & Memory Tuning
* **Swap Expansion:** Increase swap file to 8GB to accommodate LLM model loading spikes.
* **Page Size Mitigation:** Apply `jemalloc` overrides for Qdrant and node processes.
    * *Env Var:* `MALLOC_CONF=background_thread:true,dirty_decay_ms:0`
    * *Env Var:* `GLIBC_TUNABLES=glibc.malloc.trim_threshold=0`

### 2.2. Dependency Hardening
* **Node.js:** Enforce LTS (v20.x) for Claude Code CLI stability.
* **System Tools:** Install `ripgrep`, `jq`, `curl`, `net-tools` for internal agent diagnostics.

---

## 3. INFRASTRUCTURE LAYER (DOCKER COMPOSITION)
**Strategy:** Unified internal network (`ai-grid`) for zero-latency communication.

### 3.1. Container Specifications
1.  **n8n (The Orchestrator):**
    * *Image:* `n8nio/n8n:latest`
    * *Env:* `N8N_AI_CORE=true`, `N8N_SECURE_COOKIE=false` (for local API access).
    * *Volume:* Local persistence mapping required.
2.  **Ollama (The Local Cortex):**
    * *Image:* `ollama/ollama:latest`
    * *GPU Acceleration:* N/A (CPU inference optimized for RPi 5 16GB).
    * *Models:* Pre-load `llama3.1` (Logic), `mxbai-embed-large` (Memory), `mistral` (Fallback).
3.  **Qdrant (The Supermemory):**
    * *Image:* `qdrant/qdrant:latest` (Must inject `MALLOC_CONF` for RPi5 compatibility).
    * *Collection:* `agent_memory` (Vector dim: 1024).

---

## 4. INTELLIGENCE LAYER (THE HYBRID ROUTER)
**Logic:** "Cost-Aware Intelligence Switching"

### 4.1. Router Node Logic (n8n JavaScript)
* **Input:** User Request / PRD
* **Assessment:**
    * IF `complexity` < 5 OR `task_type` == "formatting":
        * **ROUTE -> Ollama (Llama 3.1)** [Cost: $0]
    * IF `complexity` > 8 OR `task_type` == "workflow_design":
        * **ROUTE -> Claude 3.5 Sonnet (API)** [Cost: Metered]
* **Fallback Mechanism:** If Claude API times out or hits limit -> Auto-switch to Llama 3.1.

---

## 5. AGENTIC CAPABILITIES (SKILLS)
**Objective:** Enable the AI to interact with the world and itself.

1.  **Self-Construction Skill (Claude Code + MCP):**
    * Grant Claude Code access to `n8n/workflows` directory.
    * Capability: Direct JSON file injection for instant workflow creation.
2.  **Research Skill (Tavily/Brave):**
    * Dedicated n8n workflow for web scraping.
    * Output format: Markdown summary stored in Qdrant.
3.  **Code Review Skill (Git Integration):**
    * Watch folder: `/data/scripts`.
    * Action: On file change, trigger LLM review against "Best Practices" doc.

---

## 6. EXECUTION SEQUENCE (FOR CLAUDE CODE)
*Initiate the following sequence via Claude Code CLI:*

**[Step 1: Bootstrap]**
> "Analyze this Protocol. Verify RPi 5 system compatibility (check page size support). Create a `docker-compose.yml` that includes n8n, Ollama, and Qdrant with the specified memory environment variables."

**[Step 2: Connection]**
> "Generate a Python script `bridge.py` that connects to the n8n API. It must authenticate using the API key and support importing a JSON workflow file."

**[Step 3: Memory Genesis]**
> "Initialize Qdrant. Create a collection named 'supermemory'. Configured vector size to match `mxbai-embed-large`."

**[Step 4: The Architect]**
> "Design the 'Master Router' workflow in JSON format. It must take a text input, classify complexity, and route to either Ollama or Claude API. Deploy this workflow to n8n immediately."

---

## 7. SUCCESS METRICS
1.  **Zero Panic:** No container crashes due to RPi 5 memory alignment.
2.  **Latency:** Local inference < 3s, API inference < 5s.
3.  **Cost:** Monthly API usage remains under $5 via active routing.