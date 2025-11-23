from adk_mocks import MockAgent
from config import AGENT_CONFIG

# Note: tools must be passed during agent instantiation in agent.py
class LogContextAgent(MockAgent):
    """Agent 2: Fetches logs and reconstructs the attack timeline."""
    
    def __init__(self, tools, **kwargs):
        super().__init__(
            name="Log & Context Agent",
            instructions="Your task is to synthesize the raw log data into a clear, chronological attack timeline.",
            tools=tools,
            **kwargs
        )

    def _mock_process(self, input_data: str) -> str:
        # We reuse the original alert ID stored in the input_data (which is the first line)
        alert_id = input_data.split('\n')[1].split(':')[1].strip()
        alert_data = self.tools[0](alert_id)
        
        # Synthesize logs into a narrative
        timeline = "\n".join([f"    - {log}" for log in alert_data['log_snippets']])

        # Builds upon the output of the Threat Identifier Agent (input_data)
        return (
            f"{input_data}\n\n"
            f"**LOG & CONTEXT SYNTHESIS**\n"
            f"Compromised System: {AGENT_CONFIG['compromised_system']} at {alert_data['target_ip']}\n"
            f"Timeline:\n{timeline}\n"
            f"IoCs: {alert_data['source_ip']}, shell.exe, 15.22.33.44"
        )