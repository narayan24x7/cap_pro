from adk_mocks import MockAgent
from config import AGENT_CONFIG
import json

# Note: tools must be passed during agent instantiation in agent.py
class ReportWriterAgent(MockAgent):
    """Agent 4: Generates the final, formatted reports (Technical and Executive)."""
    
    def __init__(self, tools, **kwargs):
        super().__init__(
            name="Report Writer Agent",
            instructions="Your task is to take the final risk assessment and format it into two documents: a detailed Technical Incident Report and a concise Executive Summary, outputting them as a single JSON object.",
            tools=tools,
            **kwargs
        )

    def _mock_process(self, full_context: str) -> str:
        # The Orchestrator passes necessary context to the agent's self.context
        alert_id = self.context.get('alert_id', 'N/A')
        known_iocs_match = self.context.get('threat_intelligence', {}).get('known_iocs_match', 'N/A')

        # Simulates LLM structuring the output for two audiences
        technical_report = (
            f"## Technical Incident Report - Alert {alert_id}\n"
            f"**Date/Time:** {AGENT_CONFIG['alert_time']}\n"
            f"**Status:** Confirmed Compromise (Severity: HIGH)\n"
            f"**Summary of Findings:**\n"
            f"The attack exploited {known_iocs_match} to deploy a persistent shell on {AGENT_CONFIG['compromised_system']}.\n"
            f"### Full Assessment\n"
            f"{full_context}"
        )

        executive_summary = (
            f"## Executive Summary: Security Incident on {AGENT_CONFIG['alert_time']}\n"
            f"**Severity:** HIGH\n"
            f"**Impact:** Confirmed compromise of Web Server 03. No immediate data exfiltration detected but system isolation is required.\n"
            f"**Recommended Action:** Immediate funding and approval for the three listed mitigation steps."
        )

        # The output MUST be a JSON string for the orchestrator to parse and export.
        return json.dumps({
            "technical_report": technical_report,
            "executive_summary": executive_summary
        })