"""
Compiled Protocol Buffer modules for Axon controller <-> agent communication.

All _pb2 modules are imported here for convenient access. Imports are wrapped
in try/except to allow the package to be imported even if protobuf files
have not been compiled yet (run ``make proto`` in this directory to generate).
"""

try:
    from axon_shared.proto import bridge_messages_pb2  # noqa: F401
except ImportError:
    bridge_messages_pb2 = None

try:
    from axon_shared.proto import meter_messages_pb2  # noqa: F401
except ImportError:
    meter_messages_pb2 = None

try:
    from axon_shared.proto import health_check_messages_pb2  # noqa: F401
except ImportError:
    health_check_messages_pb2 = None

try:
    from axon_shared.proto import flow_mod_messages_pb2  # noqa: F401
except ImportError:
    flow_mod_messages_pb2 = None

try:
    from axon_shared.proto import flow_messages_pb2  # noqa: F401
except ImportError:
    flow_messages_pb2 = None

try:
    from axon_shared.proto import sniffer_messages_pb2  # noqa: F401
except ImportError:
    sniffer_messages_pb2 = None

try:
    from axon_shared.proto import classifier_config_messages_pb2  # noqa: F401
except ImportError:
    classifier_config_messages_pb2 = None

try:
    from axon_shared.proto import classifier_messages_pb2  # noqa: F401
except ImportError:
    classifier_messages_pb2 = None

try:
    from axon_shared.proto import classifier_flow_stats_messages_pb2  # noqa: F401
except ImportError:
    classifier_flow_stats_messages_pb2 = None

try:
    from axon_shared.proto import flow_stats_messages_pb2  # noqa: F401
except ImportError:
    flow_stats_messages_pb2 = None

try:
    from axon_shared.proto import interface_messages_pb2  # noqa: F401
except ImportError:
    interface_messages_pb2 = None

try:
    from axon_shared.proto import policy_messages_pb2  # noqa: F401
except ImportError:
    policy_messages_pb2 = None

try:
    from axon_shared.proto import uptime_check_messages_pb2  # noqa: F401
except ImportError:
    uptime_check_messages_pb2 = None

try:
    from axon_shared.proto import ee_data_service_pb2  # noqa: F401
except ImportError:
    ee_data_service_pb2 = None

try:
    from axon_shared.proto import ee_data_service_pb2_grpc  # noqa: F401
except ImportError:
    ee_data_service_pb2_grpc = None
