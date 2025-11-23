from adk_mocks import MockLoopAgent
from sub_agents.validation_checkers import SeverityScoreValidationChecker
from config import AGENT_CONFIG

# Note: tools must be passed during agent instantiation in agent.py
class RiskAssessmentAgent(MockLoopAgent):
    """Agent 3: Analyzes data and assigns risk score and mitigation steps."""
    
    def __init__(self, tools, **kwargs):
        super().__init__(
            name="Risk Assessment Agent",
            instructions="Your task is to assign a Severity score (CRITICAL, HIGH, MEDIUM, LOW) and provide 3 immediate mitigation steps based on the full incident context.",
            tools=tools,
            **kwargs
        )
        self.validation_checker = SeverityScoreValidationChecker(name="Severity Checker", instructions="Checks for valid score/mitigation.")

    # Override the LoopAgent's run method to ensure validation is called
    def run(self, input_data: str) -> str:
        return super().run(input_data, self.validation_checker)

    def _mock_process(self, input_data: str) -> str:
        # Simulates LLM analysis for risk
        # Since this agent is a LoopAgent, the output must adhere to the format
        # defined by the SeverityScoreValidationChecker.
        
        # We need the original alert ID to pass to the tool
        alert_id = input_data.split('\n')[1].split(':')[1].strip()
        alert_data = self.tools[0](alert_id)
        
        return (
            f"{input_data}\n\n"
            f"**RISK ASSESSMENT & MITIGATION**\n"
            f"Severity: HIGH\n"  # This is the expected output format
            f"Reasoning: Successful execution of a known shell backdoor ({alert_data['threat_intelligence']['known_iocs_match']}) on a critical web server.\n"
            f"Mitigation Steps:\n"
            f"1. Immediately isolate {AGENT_CONFIG['compromised_system']}.\n"
            f"2. Block external IP {alert_data['source_ip']} at the firewall.\n"
            f"3. Initiate full forensic investigation on the server image."
        )