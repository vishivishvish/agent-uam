######################################################################
# Importing Libraries
######################################################################

from engine.planner_agent import generate_plan
from engine.plan_validator import validate_plan
from engine.executor import execute_plan
from memory.memory_store import save_memory

######################################################################
# Main RUN WORKFLOW Function
######################################################################

def run_workflow(user_message, input_payload):

    print("\n================================================");
    print("[S1] GENERATING PLAN from PLANNER AGENT");
    print("================================================\n");

    plan = generate_plan(user_message);

    print("\n==============================");
    print("[S1] PLAN GENERATED");
    print("==============================\n");

    print("\n================================================");
    print("[S2] VALIDATING PLAN from Plan Validator");
    print("================================================\n");

    validate_plan(plan);

    print("\n==============================");
    print("[S2] PLAN VALIDATED");
    print("==============================\n");

    print("\n========================================================");
    print("[S3] EXECUTING PLAN step-by-step with Plan Executor");
    print("========================================================\n");

    initial_state = {
        "raw_input": input_payload,
        "normalized": None,
        "approver": None,
        "approval_status": None,
        "user_exists": None,
        "provisioning_result": None,
        "errors": None
    }

    result = execute_plan(plan, initial_state)

    print("\n==============================");
    print("[S3] PLAN EXECUTED");
    print("==============================\n");

    if not result.get("errors"):
        save_memory(plan, result)
        print("[S3] No Errors in Plan Execution - EXECUTION TRACE SAVED TO MEMORY");

    return result;