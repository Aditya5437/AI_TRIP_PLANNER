from trip_planner.mcp_server.registry import (
    get_tool,
    list_tools
)


class MCPServer:

    def execute_tool(self, tool_name, **kwargs):

        tool = get_tool(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' not found."

        return tool(**kwargs)

    def available_tools(self):

        return list_tools()