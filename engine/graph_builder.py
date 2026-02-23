import yaml;
from langgraph.graph import StateGraph;
from tools.registry import TOOL_REGISTRY;
from engine.state import AgentState;

def build_graph(config_path):

    with open(config_path, "r") as f:
        config = yaml.safe_load(f);

    workflow_steps = config["steps"];

    graph = StateGraph(AgentState);

    # Add nodes dynamically from config
    for step in workflow_steps:
        graph.add_node(step, TOOL_REGISTRY[step]);

    # Define linear edges
    for i in range(len(workflow_steps) - 1):
        graph.add_edge(workflow_steps[i], workflow_steps[i+1]);

    graph.set_entry_point(workflow_steps[0]);
    return graph.compile();


print("All good - engine/graph_builder.py now ready to be used");