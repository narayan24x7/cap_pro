from adk_mocks import MockAgent

# --- 4. VALIDATION CHECKERS (LoopAgent Components) ---

class ReportDataValidationChecker(MockAgent):
    """Ensures the data collected by the first two agents is complete."""
    
    # We override _mock_process to contain the validation logic
    def _mock_process(self, input_data: str) -> str:
        # Check if key timeline elements are present
        if "Timeline:" in input_data and "IoCs:" in input_data:
            return "VALIDATION_PASSED: All necessary data points (Timeline, IoCs) are present."
        else:
            return "Validation Failed. Missing critical data points for the technical report."

class SeverityScoreValidationChecker(MockAgent):
    """Ensures the Risk Assessment agent provided a valid score and mitigation steps."""
    
    # We override _mock_process to contain the validation logic
    def _mock_process(self, input_data: str) -> str:
        # Expected format: "Severity: HIGH/MEDIUM/LOW\nMitigation Steps:\n..."
        if "Severity:" in input_data and "Mitigation Steps:" in input_data:
            score_line = next((line for line in input_data.split('\n') if "Severity:" in line), "")
            score = score_line.split(":")[1].strip().upper() if score_line else ""
            
            valid_scores = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
            if score in valid_scores:
                return "VALIDATION_PASSED: Severity score and mitigation steps are valid."
            else:
                return f"Validation Failed. Severity score '{score}' is not valid. Must be one of {valid_scores}."
        else:
            return "Validation Failed. Missing 'Severity' or 'Mitigation Steps' section."