# Axon Shared

Shared protocol definitions, MQTT topic patterns, and common utilities for the
[Axon](https://taurinetech.com) network management platform.

This package is used by both [axon-ce](https://github.com/Taurine-Technology/axon-ce)
(the controller) and [axon-agent-ce](https://github.com/Taurine-Technology/axon-agent-ce)
(the edge agent) to ensure protocol compatibility.

## What's Included

- **Protocol Buffers** — Canonical `.proto` definitions for all controller ↔ agent communication
- **MQTT Topics** — Topic pattern constants and builders for control/data/status planes
- **Shared Constants** — Common configuration values and enums

## Installation

```bash
pip install "axon-shared @ git+https://github.com/Taurine-Technology/axon-shared.git@v0.1.0"
```

## Usage

```python
from axon_shared.proto import policy_messages_pb2
from axon_shared.mqtt.topics import DEVICE_STATS, control_pattern
```

## Regenerating Protobuf Files

```bash
cd axon_shared/proto
make proto
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). All contributions require signing our CLA.

## License

AGPL-3.0-only — see [LICENSE](./LICENSE).
