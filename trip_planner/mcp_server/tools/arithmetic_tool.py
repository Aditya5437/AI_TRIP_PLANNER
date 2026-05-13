from trip_planner.mcp_server.registry import register_tool


def arithmetic_operation(a: float, b: float, operation: str):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return "Invalid operation."


register_tool(
    "arithmetic_tool",
    arithmetic_operation
)