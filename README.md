# Infer-Nexus

**Infer-Nexus**: A self-optimizing, real-time AI inference infrastructure.

## Architecture

- **Gateway**: Rust + Axum + WebSocket (Port 8080)
- **Worker**: Python + FastAPI + PyTorch (Port 8000)
- **Storage**: Redis
- **Orchestration**: Docker Compose (Local), K8s (Prod)

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Rust (Cargo)
- Python 3.9+

### Quick Start

1. Start the development environment:
   ```bash
   make dev-up
   # OR
   docker-compose up -d --build
   ```

2. Check status:
   ```bash
   docker-compose ps
   ```

3. Test WebSocket Gateway:
   Connect to `ws://localhost:8080/ws` and send a message.

4. Test Inference Worker:
   ```bash
   curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"model": "test", "input": [1, 2, 3]}'
   ```

## Directory Structure
- `crates/`: Rust modules (gateway, router, cache)
- `python/`: Python modules (worker, ml, sdk)
- `deployments/`: K8s, Terraform
