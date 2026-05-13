from trip_planner.mcp_server.registry import register_tool


def calculate_expense(expenses: list):

    total = sum(expenses)

    return {
        "total_expense": total,
        "number_of_expenses": len(expenses)
    }


register_tool(
    "expense_calculator_tool",
    calculate_expense
)