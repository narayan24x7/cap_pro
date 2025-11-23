from typing import Dict, Any
from adk_mocks import MockTool
import time

# --- 3. CUSTOM TOOLS ---

def fetch_logs_and_alerts(alert_id: str) -> Dict[str, Any]:
    """
    Mock function to simulate fetching real security data from a SIEM or Cloud logs.
    In a real app, this would use a secure API client.
    """
    print(f"TOOL: Retrieving data for Alert ID: {alert_id}...")
    time.sleep(1)
    # Mock data return
    return {
        "alert_id": alert_id,
        "source_ip": "203.0.113.42",
        "target_ip": "192.168.1.100",
        "log_snippets": [
            "04:30:00 - Suspicious remote execution attempt detected.",
            "04:30:05 - New file 'shell.exe' created in C:\\temp\\.",
            "04:30:10 - Outbound connection established to 15.22.33.44 on port 443."
        ],
        "threat_intelligence": {
            "source_ip_geo": "Eastern Europe",
            "known_iocs_match": "CVE-2024-5555"
        }
    }

def export_incident_report(filename: str, report_content: str) -> str:
    """
    Mock function to save the final report.
    """
    print(f"\nTOOL: Exporting final report to {filename}.md...")
    time.sleep(0.5)
    # In a real app, this would write to a file or a database.
    return f"Export successful. Report saved as {filename}.md with {len(report_content.split())} words."

# Instantiate Tools
FETCH_LOGS_TOOL = MockTool("fetch_logs_and_alerts", "Fetches logs and security alert data.", fetch_logs_and_alerts)
EXPORT_REPORT_TOOL = MockTool("export_incident_report", "Exports final report documents.", export_incident_report)

# Export list of tools to be used by the Orchestrator
SENTINEL_TOOLS = [FETCH_LOGS_TOOL, EXPORT_REPORT_TOOL]