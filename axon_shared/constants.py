"""Shared constants for the Axon platform."""

# =====================================================================
# MQTT Connection
# =====================================================================
MQTT_MAX_RETRIES = 5
MQTT_INITIAL_BACKOFF = 2  # seconds
MQTT_MAX_BACKOFF = 60  # seconds
MQTT_AUTH_ERROR_CODES = {4, 5}
MQTT_KEEPALIVE = 60  # seconds
MQTT_CONNECT_TIMEOUT = 10  # seconds

# =====================================================================
# OpenFlow Cookie Masks
# =====================================================================
COOKIE_IP_BLOCK_MASK = 0x0A01000000000000
COOKIE_BLOCK_LIST_MASK = 0x0A02000000000000

# =====================================================================
# Packet Capture / Classification
# =====================================================================
DEFAULT_NUM_BYTES = 225
DEFAULT_NUM_PACKETS = 5
DEFAULT_BATCH_INTERVAL = 1.0  # seconds
DEFAULT_IDLE_TIMEOUT = 30  # seconds
DEFAULT_FLOW_EXPIRATION = 30  # seconds
DEFAULT_BLOCK_CACHE_TTL = 300  # seconds

# =====================================================================
# Policy Rule Priorities (OpenFlow)
# =====================================================================
PRIORITY_IP_BLOCK = 7000
PRIORITY_APP_BLOCK = 6000
PRIORITY_RATE_LIMIT = 5000

# =====================================================================
# Generic Protocols (not classifiable by nDPI)
# =====================================================================
GENERIC_PROTOCOLS = {
    "HTTP",
    "TCP",
    "UDP",
    "TLS",
    "QUIC",
    "DNS",
    "ICMP",
    "Unknown",
    "HTTP_Proxy",
    "HTTPS",
    "SSL",
    "DTLS",
}

# =====================================================================
# Port Status
# =====================================================================
PORT_STATUS_UP = "up"
PORT_STATUS_DOWN = "down"
PORT_STATUS_UNKNOWN = "unknown"

# =====================================================================
# Device Status
# =====================================================================
DEVICE_STATUS_UNCLAIMED = "unclaimed"
DEVICE_STATUS_PENDING = "pending_adoption"
DEVICE_STATUS_ADOPTED = "adopted"
DEVICE_STATUS_ACTIVE = "active"
DEVICE_STATUS_INACTIVE = "inactive"

# =====================================================================
# Compression
# =====================================================================
ZSTD_COMPRESSION_LEVEL = 3
MAX_ZSTD_DECOMPRESSED_SIZE = 10 * 1024 * 1024  # 10 MB

# =====================================================================
# Agent Configuration Paths
# =====================================================================
BOOTSTRAP_CONFIG_PATH = "/etc/axon/bootstrap.json"
DEVICE_CONFIG_PATH = "/etc/axon/config.json"
CLASSIFIER_CONFIG_PATH = "/etc/axon/classifier_config.json"
SNIFFER_CONFIG_PATH = "/etc/axon/sniffer_config.json"
POLICY_CACHE_PATH = "/var/lib/axon/policy_cache.db"

# =====================================================================
# DNS Provider IPs (for dns_icmp uptime checks)
# =====================================================================
DNS_PROVIDERS = {
    "google": ["8.8.8.8", "8.8.4.4"],
    "cloudflare": ["1.1.1.1", "1.0.0.1"],
    "opendns": ["208.67.222.222"],
    "quad9": ["9.9.9.9"],
}

# =====================================================================
# Uptime Check Types
# =====================================================================
CHECK_TYPE_HEARTBEAT = "agent_heartbeat"
CHECK_TYPE_ICMP = "endpoint_icmp"
CHECK_TYPE_DNS = "dns_icmp"

# =====================================================================
# Buffer Flush Intervals
# =====================================================================
DEFAULT_STATS_FLUSH_INTERVAL = 15  # seconds

# =====================================================================
# Agent Config Search Paths
# =====================================================================
CONFIG_PATHS = ["/etc/axon/", "./"]

# =====================================================================
# Classification Versions
# =====================================================================
CLASSIFICATION_V1 = "traffic_classification"
CLASSIFICATION_V2 = "nfstream_classification"
