from adk_mocks import MockAgent
from config import AGENT_CONFIG

# Note: tools must be passed during agent instantiation in agent.py
class ThreatIdentifierAgent(MockAgent):
    """Agent 1: Gathers and validates initial threat intelligence."""
    
    def __init__(self, tools, **kwargs):
        super().__init__(
            name="Threat Identifier",
            instructions="Your task is to analyze the initial alert data to identify known threats, IoCs, and likely actors.",
            tools=tools,
            **kwargs
        )

    def _mock_process(self, alert_id: str) -> str:
        # Calls the fetch_logs_and_alerts tool (which is the first tool in the list)
        alert_data = self.tools[0](alert_id)
        
        # Simulates the LLM generating the initial assessment
        return (
            f"**THREAT IDENTIFICATION DRAFT**\n"
            f"Alert ID: {alert_data['alert_id']}\n"
            f"Initial IoCs: {alert_data['source_ip']}, {alert_data['target_ip']}\n"
            f"Known IoCs Match: {alert_data['threat_intelligence']['known_iocs_match']}\n"
            f"Likely Threat Actor: {AGENT_CONFIG['threat_actor']} (Based on matching IoCs and geo-location {alert_data['threat_intelligence']['source_ip_geo']})."
        )