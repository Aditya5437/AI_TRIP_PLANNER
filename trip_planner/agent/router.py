def detect_tool(query: str):
    
    query = query.lower()

    if "weather" in query:
        return "weather_info_tool"

    elif "place" in query:
        return "place_search_tool"

    elif "hotel" in query:
        return "hotel_search_tool"

    elif "budget" in query:
        return "budget_estimator_tool"

    elif "currency" in query:
        return "currency_conversion_tool"

    elif "expense" in query:
        return "expense_calculator_tool"

    elif "itinerary" in query:
        return "itinerary_tool"

    return None