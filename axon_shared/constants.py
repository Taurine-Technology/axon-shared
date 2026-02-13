"""Shared constants for the Axon platform."""

# Default buffer flush intervals (seconds)
DEFAULT_STATS_FLUSH_INTERVAL = 15

# Agent config search paths
CONFIG_PATHS = ["/etc/axon/", "./"]

# Default classification versions
CLASSIFICATION_V1 = "traffic_classification"
CLASSIFICATION_V2 = "nfstream_classification"