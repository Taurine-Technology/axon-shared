"""Round-trip and topic-string tests for the agent update / version wire format."""

import pytest

from axon_shared.mqtt.topics import (
    AGENT_UPDATE,
    AGENT_UPDATE_RESPONSE,
    AGENT_VERSION_REQUEST,
    AGENT_VERSION_RESPONSE,
    control_topic,
)
from axon_shared.proto.agent_update_messages_pb2 import (
    AgentUpdateCommand,
    AgentUpdateResponse,
    AgentVersionRequest,
    AgentVersionResponse,
)


def test_topic_constants_have_expected_strings():
    assert AGENT_UPDATE == "agent/update"
    assert AGENT_UPDATE_RESPONSE == "agent/update/response"
    assert AGENT_VERSION_REQUEST == "agent/version"
    assert AGENT_VERSION_RESPONSE == "agent/version/response"


def test_control_topic_for_agent_update():
    assert (
        control_topic("site-1", "dev-1", AGENT_UPDATE)
        == "axon/control/site-1/dev-1/agent/update"
    )


def test_agent_update_command_round_trip_empty():
    cmd = AgentUpdateCommand()
    parsed = AgentUpdateCommand()
    parsed.ParseFromString(cmd.SerializeToString())
    assert parsed.correlation_id == ""
    assert parsed.target_version == ""
    assert parsed.index_url == ""
    assert parsed.timeout_seconds == 0
    assert parsed.dry_run is False


def test_agent_update_command_round_trip_populated():
    cmd = AgentUpdateCommand(
        correlation_id="abc-123",
        target_version="0.3.0",
        index_url="https://pypi.example.com/simple/",
        timeout_seconds=120,
        dry_run=True,
    )
    parsed = AgentUpdateCommand()
    parsed.ParseFromString(cmd.SerializeToString())
    assert parsed.correlation_id == "abc-123"
    assert parsed.target_version == "0.3.0"
    assert parsed.index_url == "https://pypi.example.com/simple/"
    assert parsed.timeout_seconds == 120
    assert parsed.dry_run is True


@pytest.mark.parametrize(
    "status",
    [
        AgentUpdateResponse.STATUS_UNSPECIFIED,
        AgentUpdateResponse.STATUS_OK,
        AgentUpdateResponse.STATUS_ROLLED_BACK,
        AgentUpdateResponse.STATUS_FAILED,
        AgentUpdateResponse.STATUS_ALREADY_AT_VERSION,
    ],
)
def test_agent_update_response_round_trip_all_statuses(status):
    resp = AgentUpdateResponse(
        correlation_id="abc-123",
        status=status,
        previous_version="0.2.6",
        current_version="0.3.0",
        previous_ce_version="0.2.6",
        current_ce_version="0.3.0",
        previous_shared_version="0.2.6",
        current_shared_version="0.3.0",
        completed_steps=["snapshot_versions", "pip_install", "restart_units"],
        failed_steps=["health_check"],
        error_message="health check timed out",
        duration_ms=12_345,
    )
    parsed = AgentUpdateResponse()
    parsed.ParseFromString(resp.SerializeToString())
    assert parsed.correlation_id == "abc-123"
    assert parsed.status == status
    assert parsed.previous_version == "0.2.6"
    assert parsed.current_version == "0.3.0"
    assert parsed.previous_ce_version == "0.2.6"
    assert parsed.current_ce_version == "0.3.0"
    assert parsed.previous_shared_version == "0.2.6"
    assert parsed.current_shared_version == "0.3.0"
    assert list(parsed.completed_steps) == [
        "snapshot_versions",
        "pip_install",
        "restart_units",
    ]
    assert list(parsed.failed_steps) == ["health_check"]
    assert parsed.error_message == "health check timed out"
    assert parsed.duration_ms == 12_345


def test_agent_update_response_round_trip_empty():
    resp = AgentUpdateResponse()
    parsed = AgentUpdateResponse()
    parsed.ParseFromString(resp.SerializeToString())
    assert parsed.correlation_id == ""
    assert parsed.status == AgentUpdateResponse.STATUS_UNSPECIFIED
    assert list(parsed.completed_steps) == []
    assert list(parsed.failed_steps) == []
    assert parsed.duration_ms == 0


def test_agent_version_request_round_trip():
    req = AgentVersionRequest(correlation_id="probe-1")
    parsed = AgentVersionRequest()
    parsed.ParseFromString(req.SerializeToString())
    assert parsed.correlation_id == "probe-1"


def test_agent_version_response_round_trip_empty():
    resp = AgentVersionResponse()
    parsed = AgentVersionResponse()
    parsed.ParseFromString(resp.SerializeToString())
    assert parsed.correlation_id == ""
    assert parsed.ee_version == ""
    assert list(parsed.running_services) == []
    assert parsed.update_in_progress is False
    assert parsed.timestamp_ms == 0


def test_agent_version_response_round_trip_populated():
    resp = AgentVersionResponse(
        correlation_id="probe-1",
        ee_version="0.3.0",
        ce_version="0.3.0",
        shared_version="0.3.0",
        installer_version="2026.04.27-1",
        running_services=["axon-agent-ee.service", "axon-agent-sniffer.service"],
        update_in_progress=True,
        timestamp_ms=1_745_712_000_000,
    )
    parsed = AgentVersionResponse()
    parsed.ParseFromString(resp.SerializeToString())
    assert parsed.correlation_id == "probe-1"
    assert parsed.ee_version == "0.3.0"
    assert parsed.ce_version == "0.3.0"
    assert parsed.shared_version == "0.3.0"
    assert parsed.installer_version == "2026.04.27-1"
    assert list(parsed.running_services) == [
        "axon-agent-ee.service",
        "axon-agent-sniffer.service",
    ]
    assert parsed.update_in_progress is True
    assert parsed.timestamp_ms == 1_745_712_000_000
