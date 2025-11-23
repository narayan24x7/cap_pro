import time
from typing import Dict, Any, List

# --- MOCK GOOGLE ADK FRAMEWORK COMPONENTS (For Runnable Demonstration) ---
# In a real ADK project, these would be imported from the Google ADK Library.

class MockTool:
    """Mock class for an ADK Tool."""
    def __init__(self, name: str, description: str, func: callable):
        self.name = name
        self.description = description
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"--- TOOL: Calling {self.name} ---")
        return self.func(*args, **kwargs)

class MockAgent:
    """Mock base class for an ADK Agent."""
    def __init__(self, name: str, instructions: str, model: str = "gemini-2.5-flash-preview-09-2025", tools: List[MockTool] = None, sub_agents: List['MockAgent'] = None):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.tools = tools if tools is not None else []
        self.sub_agents = sub_agents if sub_agents is not None else []
        self.context = {} # Internal storage for processing data

    def run(self, input_data: str) -> str:
        """Simulates the agent's core reasoning and output generation."""
        print(f"\n[{self.name} is running...]")
        # In a real app, this would be an LLM API call (generateContent)
        time.sleep(0.5)
        return self._mock_process(input_data)

    def _mock_process(self, input_data: str) -> str:
        """Placeholder for specialized agent logic. MUST be overridden."""
        raise NotImplementedError("Specialized agents must implement _mock_process.")

class MockLoopAgent(MockAgent):
    """Mock class for an ADK LoopAgent, used for retries/validation."""
    def run(self, input_data: str, validation_checker: MockAgent) -> str:
        """Simulates a loop with a validation step."""
        print(f"[{self.name} started in Loop mode with ValidationChecker...]")
        
        MAX_RETRIES = 2
        for attempt in range(MAX_RETRIES):
            # 1. Generate content (e.g., the report draft or severity score)
            try:
                # Call the specialized _mock_process defined in the derived class
                generated_content = super().run(input_data)
            except NotImplementedError:
                 # If the derived class didn't implement _mock_process, use a generic one
                generated_content = f"Generic Processed input by {self.name}: {input_data}"

            # 2. Validate the content
            validation_result = validation_checker.run(generated_content)

            if "VALIDATION_PASSED" in validation_result:
                print(f"[{self.name}] Validation successful on attempt {attempt + 1}.")
                return generated_content
            else:
                print(f"[{self.name}] Validation FAILED on attempt {attempt + 1}. Retrying...")
                # The input_data is updated to guide the retry
                input_data = f"RETRY (Attempt {attempt + 2}): Original output failed validation: {validation_result}. Please correct and generate a new response based on: {input_data}"
        
        return "ERROR: Max retries reached. Output failed final validation."