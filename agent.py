from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import os
from google.adk.agents import Agent

# --- Agent Definitions ---

# 1. Extraction Agent
extraction_agent = LlmAgent(
    name="ExtractionAgent",
    model="gemini-2.5-flash",
    instruction="""You are an information extraction specialist.
    From the user's query, which may include a pdf document or an image of a document, extract the following fields: 'name', 'date of birth' (in DD-MM-YYYY format), and 'pan card number'.
    Output ONLY a JSON object with the keys 'name', 'dob', and 'pan'.""",
    description="Extracts user information from a document.",
    output_key="extracted_data"
)

# 2. Validation Agent
validation_agent = LlmAgent(
    name="ValidationAgent",
    model="gemini-2.5-flash",
    instruction="""You are a data validator. You will receive JSON data under the key 'extracted_data'.
    Your task is to validate the data based on the following rules:
    1. The 'name' field must be a non-empty string.
    2. The 'dob' field must be a valid date in DD-MM-YYYY format.
    3. The 'pan' field must be a valid Indian PAN card number (format: 5 uppercase letters, 4 numbers, 1 uppercase letter).

    If all rules pass, output a JSON object: {"status": "VALID"}.
    If any rule fails, output a JSON object: {"status": "INVALID", "reason": "Describe the validation error here."}
    Output ONLY the JSON object.""",
    description="Validates the extracted user information.",
    output_key="validation_result"
)

# 3. Response Agent
response_agent = LlmAgent(
    name="ResponseAgent",
    model="gemini-2.5-flash",
    instruction="""You are a helpful assistant who communicates results to the user.
    You will receive the 'validation_result' and the original 'extracted_data'.
    
    - If the 'validation_result' status is 'VALID', create a friendly message displaying the extracted data clearly to the user.
    - If the 'validation_result' status is 'INVALID', create a friendly message explaining the reason for the failure.
    
    This is the final output to the user.""",
    description="Generates a final response for the user.",
    output_key="final_response"
)


# --- Sequential Agent Definition ---

root_agent = SequentialAgent(
    name="DocumentProcessingAgent",
    sub_agents=[
        extraction_agent,
        validation_agent,
        response_agent
    ],
    description="""This is a document processing agent. You can provide a document (like a PAN card), 
    and I will extract the name, date of birth, and PAN number. I will then validate this information 
    and display it back to you. This is useful for digitizing and verifying identity documents.
    """
)

# --- Runner (for local testing) ---

if __name__ == "__main__":
    if "GEMINI_API_KEY" not in os.environ:
        pass