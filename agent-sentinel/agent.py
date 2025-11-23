class InteractiveSentinelAgent(MockAgent):
    """The main agent that manages the workflow and delegates tasks."""
    def __init__(self, **kwargs):
        super().__init__(
            name="Interactive Sentinel Orchestrator",
            instructions="You are a security orchestration engine that runs the incident response workflow.",
            tools=[FETCH_LOGS_TOOL, EXPORT_REPORT_TOOL],
            sub_agents=[
                ThreatIdentifierAgent("Threat Identifier", "Gathers initial data.", [FETCH_LOGS_TOOL]),
                LogContextAgent("Log & Context Agent", "Synthesizes timeline.", [FETCH_LOGS_TOOL]),
                RiskAssessmentAgent("Risk Assessment Agent", "Scores risk and mitigation.", [FETCH_LOGS_TOOL]),
                ReportWriterAgent("Report Writer Agent", "Generates final documents.", [FETCH_LOGS_TOOL]),
            ],
            **kwargs
        )

    def run_workflow(self, alert_id: str):
        print(f"\n=======================================================")
        print(f"       Agent Sentinel: Incident Response Workflow")
        print(f"  Incident ID: {alert_id} | Initial Time: {AGENT_CONFIG['alert_time']}")
        print(f"=======================================================\n")

        full_context = alert_id

        # 1. Threat Identification (Uses LoopAgent pattern for validation)
        # We wrap the TIA run in the validation structure for quality assurance
        threat_identifier_agent = self.sub_agents[0]
        full_context = MockLoopAgent(threat_identifier_agent.name, threat_identifier_agent.instructions).run(
            full_context, ReportDataValidationChecker("Report Data Checker", "Checks if data is complete.")
        )
        if "ERROR" in full_context: return print(full_context)
        print("\n--- PHASE 1 COMPLETE: THREAT IDENTIFIED ---")

        # 2. Log & Context Synthesis (Uses the output from Phase 1)
        full_context = self.sub_agents[1].run(full_context)
        print("\n--- PHASE 2 COMPLETE: CONTEXT ESTABLISHED ---")
        
        # 3. Risk Assessment (Crucial validation step)
        risk_assessment_agent = self.sub_agents[2]
        full_context = risk_assessment_agent.run(
            full_context, SeverityScoreValidationChecker("Severity Checker", "Checks for valid score/mitigation.")
        )
        if "ERROR" in full_context: return print(full_context)
        print("\n--- PHASE 3 COMPLETE: RISK ASSESSED AND MITIGATION READY ---")

        # 4. Report Generation
        self.context['alert_id'] = alert_id # Pass context for naming
        self.context['threat_intelligence'] = FETCH_LOGS_TOOL(alert_id)['threat_intelligence']
        
        report_json_str = self.sub_agents[3].run(full_context)
        
        # 5. Export
        try:
            reports = json.loads(report_json_str)
            
            # Export the Technical Report
            report_name = f"incident_report_{alert_id}"
            self.tools[1](report_name, reports.get("technical_report", "N/A"))

            # Display Executive Summary (optional display/final step)
            print("\n=======================================================")
            print("         FINAL EXECUTIVE SUMMARY (for Review)")
            print("=======================================================")
            print(reports.get("executive_summary", "Summary not generated."))
            
        except json.JSONDecodeError:
            print(f"ERROR: Final Report Writer did not return valid JSON: {report_json_str}")
        

# --- 7. MAIN EXECUTION (Demonstration) ---

if __name__ == "__main__":
    # The hackathon project starts here by initializing and running the Orchestrator
    sentinel_orchestrator = InteractiveSentinelAgent()
    sentinel_orchestrator.run_workflow(alert_id="SEC4567")