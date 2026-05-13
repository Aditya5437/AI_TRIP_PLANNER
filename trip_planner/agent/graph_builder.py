from langgraph.graph import StateGraph, END

from trip_planner.agent.state import AgentState

from trip_planner.agent.nodes import (
    tool_selection_node,
    tool_execution_node,
    final_response_node
)


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "tool_selection",
        tool_selection_node
    )

    graph.add_node(
        "tool_execution",
        tool_execution_node
    )

    graph.add_node(
        "final_response",
        final_response_node
    )

    graph.set_entry_point(
        "tool_selection"
    )

    graph.add_edge(
        "tool_selection",
        "tool_execution"
    )

    graph.add_edge(
        "tool_execution",
        "final_response"
    )

    graph.add_edge(
        "final_response",
        END
    )

    return graph.compile()
