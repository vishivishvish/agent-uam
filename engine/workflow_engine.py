from engine.graph_builder import build_graph;

def run_workflow(input_data):

    graph = build_graph("config/uam_create_account.yaml");

    initial_state = \
    {
        "raw_input": input_data,
        "normalized": None,
        "approver": None,
        "errors": None
    };

    result = graph.invoke(initial_state);

    return result;


print("All good - engine/workflow_engine.py now ready to be used");