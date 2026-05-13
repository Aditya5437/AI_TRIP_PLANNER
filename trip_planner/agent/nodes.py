from trip_planner.agent.router import detect_tool

from trip_planner.mcp_server.server import MCPServer

from trip_planner.agent.llm import llm

server = MCPServer()


def tool_selection_node(state):

    query = state["user_query"]

    tool_name = detect_tool(query)

    state["selected_tool"] = tool_name

    return state


def tool_execution_node(state):

    tool_name = state["selected_tool"]

    query = state["user_query"]

    if tool_name == "weather_info_tool":

        city = query.split()[-1]

        result = server.execute_tool(
            tool_name,
            city=city
        )

    elif tool_name == "place_search_tool":

        city = query.split()[-1]

        result = server.execute_tool(
            tool_name,
            city=city
        )

    elif tool_name == "hotel_search_tool":

        city = query.split()[-1]

        result = server.execute_tool(
            tool_name,
            city=city
        )

    else:

        result = "Tool execution not implemented yet."

    state["tool_output"] = str(result)

    return state


def final_response_node(state):
    
    query = state["user_query"]

    tool_output = state["tool_output"]

    prompt = f"""
    You are an AI Trip Planner.

    Generate a concise and structured response.

    Rules:
    - Keep response under 250 words
    - Use bullet points where possible
    - Keep itinerary short and readable
    - Avoid very long explanations

    User Query:
    {query}

    Tool Output:
    {tool_output}
    """

    response = llm.invoke(prompt)

    state["final_response"] = response.content

    return state