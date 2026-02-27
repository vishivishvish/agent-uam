from engine.graph_builder import build_graph;
from pprint import pprint;

print("WORKFLOW ENGINE LOADED FROM:", __file__)

def run_workflow(input_data):

    print("\n" + "=" * 70);
    print("WORKFLOW STARTED");
    print("=" * 70);
    graph = build_graph("config/uam_create_account.yaml");

    initial_state = \
    {
        "raw_input": input_data,
        "normalized": None,
        "approver": None,
        "errors": None
    };

    print("\n INITIAL STATE (Memory Snapshot)");
    print("-" * 70);
    pprint(initial_state);
    print("\nExecuting LangGraph State Machine \n");

    result = graph.invoke(initial_state);

    print("\n" + "=" * 70);
    print("Workflow Completed");
    print("=" * 70);

    print("FINAL STATE (Memory Snapshot)");
    print("-" * 70);
    pprint(result);

    print("\n" + "=" * 70 + "\n");

    return result;

print("engine/workflow_engine.py now ready to be used");