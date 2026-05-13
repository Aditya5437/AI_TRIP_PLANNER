from trip_planner.agent.graph_builder import build_graph

import trip_planner.mcp_server.tools


graph = build_graph()


def run_agent(user_query: str):

    response = graph.invoke({

        "user_query": user_query
    })

    return response["final_response"]