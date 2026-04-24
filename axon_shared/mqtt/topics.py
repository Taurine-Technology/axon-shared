"""
MQTT topic patterns for Axon controller <-> agent communication.

Single source of truth — used by both axon-ce and axon-agent-ce.

Topic planes:
  - Control (QoS 2): Controller -> Agent commands. Guaranteed delivery.
  - Data (QoS 0): Agent -> Controller telemetry. Fire-and-forget.
  - Status (QoS 1): Agent -> Controller state changes.
  - Discovery: Agent -> Controller during onboarding.
"""

# =====================================================================
# QoS constants
# =====================================================================
QOS_CONTROL = 2
QOS_DATA = 0
QOS_STATUS = 1

# =====================================================================
# Prefixes (format-string templates)
# =====================================================================
CONTROL_PREFIX = "axon/control/{site_id}/{device_id}"
DATA_PREFIX = "axon/data/{site_id}/{device_id}"
STATUS_PREFIX = "axon/status/{site_id}/{device_id}"

# =====================================================================
# Global / Discovery topics
# =====================================================================
DISCOVERY = "axon/discovery"
PROVISION = "axon/provision/{mac}"

# =====================================================================
# Discovery message fields (JSON payload on DISCOVERY topic)
# =====================================================================
DISCOVERY_FIELD_UNIQUE_ID = "unique_id"
DISCOVERY_FIELD_STATUS = "status"
DISCOVERY_FIELD_IS_SWITCH = "is_switch"
DISCOVERY_FIELD_AGENT_VERSION = "axon_agent_version"
DISCOVERY_FIELD_HARDWARE_INFO = "hardware_info"
DISCOVERY_FIELD_ENROLLMENT_SECRET = "enrollment_secret"  # EE: optional

# =====================================================================
# Provision message fields (JSON payload on PROVISION topic)
# =====================================================================
PROVISION_FIELD_STATUS = "status"
PROVISION_FIELD_DEVICE_ID = "device_id"
PROVISION_FIELD_NETWORK_ID = "network_id"
PROVISION_FIELD_BRIDGE_CONFIG = "bridge_config"
PROVISION_STATUS_CLAIMED = "claimed"

# =====================================================================
# Control Plane topic suffixes (QoS 2)
# Controller -> Agent
# =====================================================================

# OVS Bridge lifecycle
BRIDGE_CREATE = "bridge/create"
BRIDGE_DELETE = "bridge/delete"
BRIDGE_UPDATE_PORTS = "bridge/update_ports"

# OVS Meter management
METER_CREATE = "meter/create"
METER_DELETE = "meter/delete"
METER_MODIFY = "meter/modify"

# Health check
HEALTH_CHECK_REQUEST = "health_check/request"
HEALTH_CHECK_RESPONSE = "health_check/response"

# Uptime monitoring
UPTIME_CHECK_HEARTBEAT = "uptime_check/heartbeat"
UPTIME_CHECK_REQUEST = "uptime_check/request"
UPTIME_CHECK_RESPONSE = "uptime_check/response"

# Policy management
POLICY_SYNC = "policy/sync"
POLICY_BLOCK_ADD = "policy/block/add"
POLICY_BLOCK_REMOVE = "policy/block/remove"
POLICY_RATELIMIT_ADD = "policy/ratelimit/add"
POLICY_RATELIMIT_REMOVE = "policy/ratelimit/remove"
POLICY_IPBLOCK_ADD = "policy/ipblock/add"
POLICY_IPBLOCK_REMOVE = "policy/ipblock/remove"
POLICY_URLBLOCK_ADD = "policy/urlblock/add"
POLICY_URLBLOCK_REMOVE = "policy/urlblock/remove"
POLICY_BLOCKLIST_ADD = "policy/blocklist/add"
POLICY_BLOCKLIST_REMOVE = "policy/blocklist/remove"
POLICY_BLOCKLIST_ENTRY_ADD = "policy/blocklist/entry/add"
POLICY_BLOCKLIST_ENTRY_REMOVE = "policy/blocklist/entry/remove"

# Plugin / Sniffer
SNIFFER_INSTALL = "plugin/sniffer/install"

# Classifier management
CLASSIFIER_INSTALL = "classifier/install"
CLASSIFIER_CONFIGURE = "classifier/configure"
CLASSIFIER_ENABLE = "classifier/enable"
CLASSIFIER_DISABLE = "classifier/disable"
CLASSIFIER_STATUS_REQUEST = "classifier/status"

# Flow modification (v1 ML classification)
FLOW_MOD_ADD = "flow_mod/add"

# Device lifecycle (graceful uninstall / decommission)
DEVICE_UNINSTALL = "device/uninstall"
DEVICE_UNINSTALL_RESPONSE = "device/uninstall/response"

# Client status (LWT / Last Will and Testament)
# Note: uses site-level scope, not device-level
CLIENT_STATUS = "client/status"
CLIENT_STATUS_TOPIC = "axon/control/{site_id}/client/status"

# =====================================================================
# Data Plane topic suffixes (QoS 0 unless noted)
# Agent -> Controller
# =====================================================================

# Device statistics
DEVICE_STATS = "stats"
PORT_STATS = "port-stats"
PORT_STATUS = "port-status"

# Interface changes (QoS 1)
INTERFACES = "interfaces"

# Traffic flows (v1 sniffer)
FLOWS = "flows"
FLOWS_RAW = "flows/raw"

# Flow statistics
FLOW_STATS = "flow-stats"
FLOW_STATS_RAW = "flow-stats-raw"

# Classified flows (v2 NFStream)
CLASSIFIED_FLOWS = "classified_flows"
CLASSIFIER_FLOW_STATS = "classifier-flow-stats"

# Classifier status response (QoS 1)
CLASSIFIER_STATUS_RESPONSE = "classifier/status"
CLASSIFIER_INSTALL_RESPONSE = "classifier/install/response"

# Sniffer install response
SNIFFER_INSTALL_RESPONSE = "plugin/sniffer/install/response"

# =====================================================================
# Subscription wildcard patterns (used by controller listener)
# =====================================================================
SUB_DISCOVERY = "axon/discovery"
SUB_CONTROL_SITE = "axon/control/{site_id}/#"
SUB_DATA_SITE = "axon/data/{site_id}/#"
SUB_CONTROL_GLOBAL = "axon/control/+/#"


# =====================================================================
# Topic builder helpers
# =====================================================================


def control_topic(site_id: str, device_id: str, suffix: str) -> str:
    """Build a concrete control plane topic for publishing."""
    return f"axon/control/{site_id}/{device_id}/{suffix}"


def data_topic(site_id: str, device_id: str, suffix: str) -> str:
    """Build a concrete data plane topic for publishing."""
    return f"axon/data/{site_id}/{device_id}/{suffix}"


def status_topic(site_id: str, device_id: str, suffix: str) -> str:
    """Build a concrete status topic for publishing."""
    return f"axon/status/{site_id}/{device_id}/{suffix}"


def provision_topic(mac: str) -> str:
    """Build a provision topic for a specific device MAC address."""
    return f"axon/provision/{mac}"


def client_status_topic(site_id: str) -> str:
    """Build the LWT client status topic for a site."""
    return f"axon/control/{site_id}/client/status"


# =====================================================================
# Handler pattern builders (regex patterns for MQTTHandler.topic_pattern)
# =====================================================================


def control_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a control plane topic handler."""
    return rf"^axon/control/([^/]+)/([^/]+)/{topic_suffix}$"


def data_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a data plane topic handler."""
    return rf"^axon/data/([^/]+)/([^/]+)/{topic_suffix}$"


def status_pattern(topic_suffix: str) -> str:
    """Build a regex pattern for a status topic handler."""
    return rf"^axon/status/([^/]+)/([^/]+)/{topic_suffix}$"
