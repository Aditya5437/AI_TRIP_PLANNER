from trip_planner.mcp_server.registry import register_tool


def estimate_budget(days: int,
                    hotel_per_day: int,
                    food_per_day: int,
                    travel_cost: int):

    total = (
        days * hotel_per_day
        +
        days * food_per_day
        +
        travel_cost
    )

    return {
        "estimated_budget": total
    }


register_tool(
    "budget_estimator_tool",
    estimate_budget
)