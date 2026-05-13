from trip_planner.mcp_server.registry import register_tool


def search_hotels(city: str):

    hotels = {

        "goa": [
            "Taj Resort Goa",
            "Sea View Resort",
            "Beach Paradise Hotel"
        ],

        "manali": [
            "Snow Peak Hotel",
            "Mountain View Resort"
        ]
    }

    return hotels.get(
        city.lower(),
        ["No hotels found."]
    )


register_tool(
    "hotel_search_tool",
    search_hotels
)