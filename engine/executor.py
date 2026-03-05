######################################################################
# Importing Libraries
######################################################################

from pprint import pprint
from tools.registry import TOOL_REGISTRY

######################################################################
# Plan Execution
######################################################################

def execute_plan(plan, initial_state):

    state = initial_state

    print("\n EXECUTION STARTED")

    for step in plan["steps"]:

        tool_name = step["step"]
        tool_func = TOOL_REGISTRY[tool_name]

        print(f"\n EXECUTING: {tool_name}")

        state = tool_func(state)

        if state.get("errors"):
            print("❌ Execution halted due to error")
            return state

    print("\n🟢 PLAN EXECUTION COMPLETED")

    return state