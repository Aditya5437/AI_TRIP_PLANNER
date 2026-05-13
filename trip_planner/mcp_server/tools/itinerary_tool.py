from trip_planner.mcp_server.registry import register_tool


def generate_itinerary(city: str, days: int):

    itinerary = []

    for day in range(1, days + 1):

        itinerary.append(
            f"Day {day}: Explore famous attractions in {city}"
        )

    return itinerary


register_tool(
    "itinerary_tool",
    generate_itinerary
)