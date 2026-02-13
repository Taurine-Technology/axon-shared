# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

axon-shared is the canonical source of truth for the Axon network management platform's protocol definitions, MQTT topic patterns, and shared constants. It is consumed by both **axon-ce** (controller) and **axon-agent-ce** (edge agent).

## Build & Development Commands

```bash
# Install for development
pip install -e ".[dev,test]"

# Linting (120 char line limit, proto files excluded)
flake8 axon_shared/ --max-line-length=120

# Tests
pytest tests/ -v

# Regenerate protobuf Python files after editing .proto schemas
cd axon_shared/proto && make proto

# Clean generated proto files
cd axon_shared/proto && make clean
```

CI runs three parallel jobs: `lint`, `test`, and `proto-check` (verifies committed `_pb2.py` files match `.proto` sources).

## Architecture

### Three core modules

- **`axon_shared/constants.py`** — Shared configuration: MQTT connection params, OpenFlow cookie masks, packet capture defaults, policy rule priorities, device/port status values, agent config paths, DNS providers, classification versions.
- **`axon_shared/mqtt/topics.py`** — MQTT topic hierarchy and QoS levels. Provides topic builder functions (`control_topic`, `data_topic`, `status_topic`, `provision_topic`) and regex pattern builders (`control_pattern`, `data_pattern`, `status_pattern`) for message routing.
- **`axon_shared/proto/`** — 13 canonical Protocol Buffer schemas (proto3) with generated `_pb2.py` modules checked into git. Organized by domain: `axon.ovs`, `axon.policy`, `axon.classifier`, `axon.traffic`, `axon.health`, `axon.network_device`, `axon.uptime_monitoring`.

### MQTT topic structure

Topics follow `axon/{plane}/{site_id}/{device_id}/{resource}/{action}` with three QoS planes:

- **Control (QoS 2)**: Controller→agent commands (bridge, meter, policy, classifier, sniffer)
- **Data (QoS 0)**: Agent→controller telemetry (stats, flows)
- **Status (QoS 1)**: Agent→controller state changes (port status, interfaces)

### Proto conventions

- All messages support batching via `repeated` fields
- Request/response messages include `correlation_id` for distributed tracing
- Timestamps are milliseconds since epoch
- Proto module imports in `__init__.py` are wrapped in try/except for graceful handling when protoc hasn't been run
- Any `.proto` change requires regenerating and committing the corresponding `_pb2.py`

## Code Conventions

- **Max line length**: 120 characters
- **Python**: 3.10+
- **Linting**: flake8 (excludes `*_pb2.py` and `*_pb2_grpc.py`)
- **License**: AGPL-3.0-only
