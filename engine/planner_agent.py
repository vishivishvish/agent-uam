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
    <RoleIntroduction>
        1 - You are a Planner Agent responsible for enterprise IAM orchestration.
        2 - Given the user request provided below, you need to generate a structured execution plan out of the tools available to you.
    </RoleIntroduction>
    <UserRequest>
        {user_message}
    </UserRequest>
    <AvailableTools>
        {AVAILABLE_TOOLS}
    </AvailableTools>
    <StrictJSONOutputFormat>
        Output STRICT JSON in the following format:
        {{
        "intent": "...",
        "steps": [
            {{"step": "tool_name"}}
        ]
        }}
    </StrictJSONOutputFormat>
    """

    response = llm.invoke(prompt);

    return json.loads(response.content);