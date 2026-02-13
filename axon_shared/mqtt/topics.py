"""
MQTT topic patterns for Axon controller <-> agent communication.

Single source of truth — used by both axon-ce and axon-agent-ce.

Topic planes:
  - Control (QoS 2): Controller -> Agent commands. Guaranteed delivery.
  - Data (QoS 0): Agent -> Controller telemetry. Fire-and-forget.
  - Status: Agent -> Controller state changes.
  - Discovery: Agent -> Controller during onboarding.
"""

# --- Control Plane (QoS 2) — Controller → Agent ---
CONTROL_PREFIX = "axon/control/{site_id}/{device_id}"

# --- Data Plane (QoS 0) — Agent → Controller ---
DATA_PREFIX = "axon/data/{site_id}/{device_id}"

# --- Status — Agent → Controller ---
STATUS_PREFIX = "axon/status/{site_id}/{device_id}"

# --- Discovery ---
DISCOVERY = "axon/discovery"
PROVISION = "axon/provision/{mac}"

# --- QoS constants ---
QOS_CONTROL = 2
QOS_DATA = 0


def control_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a control plane topic handler."""
    return rf"^axon/control/([^/]+)/([^/]+)/{topic_suffix}$"


def data_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a data plane topic handler."""
    return rf"^axon/data/([^/]+)/([^/]+)/{topic_suffix}$"


def status_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a status topic handler."""
    return rf"^axon/status/([^/]+)/([^/]+)/{topic_suffix}$"