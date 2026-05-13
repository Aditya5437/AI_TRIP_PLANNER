from trip_planner.mcp_server.registry import register_tool


def currency_converter(amount: float,
                       from_currency: str,
                       to_currency: str):

    conversion_rates = {
        ("USD", "INR"): 83,
        ("INR", "USD"): 0.012,
        ("EUR", "INR"): 90
    }

    rate = conversion_rates.get(
        (from_currency.upper(), to_currency.upper())
    )

    if rate is None:
        return "Conversion rate unavailable."

    return round(amount * rate, 2)


register_tool(
    "currency_conversion_tool",
    currency_converter
)