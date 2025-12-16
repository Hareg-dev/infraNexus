.PHONY: dev-up dev-down test lint build setup

setup:
	echo "Setting up environment..."

dev-up:
	docker-compose up -d --build

dev-down:
	docker-compose down

test:
	cargo test --workspace
	# pytest python/tests/ (commented out until tests exist)

lint:
	cargo clippy --workspace -- -D warnings
	# black python/

build:
	cargo build --release --workspace
	docker build -t infernexus/gateway:latest -f Dockerfile.gateway .
	docker build -t infernexus/worker:latest -f Dockerfile.worker .
