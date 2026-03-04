######################################################################
# Importing Libraries
######################################################################

import json
from engine.llm_config import llm

######################################################################
# Available Tools
######################################################################

AVAILABLE_TOOLS = [
    "validate_and_normalize_request",
    "check_user_exists",
    "resolve_approver",
    "simulate_approval",
    "create_user",
    "close_request"
]

######################################################################
# Plan Generation LLM Call
######################################################################

def generate_plan(user_message):

    prompt = f"""
    You are an enterprise IAM orchestration planner.

    Available tools:
    {AVAILABLE_TOOLS}

    Given the user request, generate a structured execution plan.

    Output STRICT JSON:

    {{
        "intent": "...",
        "steps": [
            {{"step": "tool_name"}}
        ]
    }}

    User Request:
    {user_message}
    """

    response = llm.invoke(prompt);

    return json.loads(response.content);