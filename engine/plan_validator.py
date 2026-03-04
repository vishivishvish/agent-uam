######################################################################
# Importing Libraries
######################################################################

from tools.registry import TOOL_REGISTRY;

######################################################################
# Plan Validator
######################################################################

def validate_plan(plan):

    steps = plan.get("steps", [])

    for step in steps:
        tool_name = step["step"]

        if tool_name not in TOOL_REGISTRY:
            raise Exception(f"Unauthorized tool: {tool_name}")

    return True