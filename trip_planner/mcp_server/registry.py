TOOLS_REGISTRY = {}


def register_tool(tool_name, tool_function):

    TOOLS_REGISTRY[tool_name] = tool_function


def get_tool(tool_name):

    return TOOLS_REGISTRY.get(tool_name)


def list_tools():

    return list(TOOLS_REGISTRY.keys())