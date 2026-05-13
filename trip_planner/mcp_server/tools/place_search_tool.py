from trip_planner.mcp_server.registry import register_tool


def search_places(city: str):

    places_data = {

        "goa": [
            "Baga Beach",
            "Fort Aguada",
            "Anjuna Beach"
        ],

        "manali": [
            "Solang Valley",
            "Rohtang Pass",
            "Hadimba Temple"
        ],

        "jaipur": [
            "Hawa Mahal",
            "Amber Fort",
            "City Palace"
        ]
    }

    return places_data.get(
        city.lower(),
        ["No places found."]
    )


register_tool(
    "place_search_tool",
    search_places
)