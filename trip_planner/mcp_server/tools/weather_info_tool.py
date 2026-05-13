from trip_planner.mcp_server.registry import register_tool


def get_weather(city: str):

    weather_data = {

        "goa": "Sunny, 30°C",
        "manali": "Cold, 12°C",
        "jaipur": "Hot, 35°C"
    }

    return weather_data.get(
        city.lower(),
        "Weather data unavailable."
    )


register_tool(
    "weather_info_tool",
    get_weather
)