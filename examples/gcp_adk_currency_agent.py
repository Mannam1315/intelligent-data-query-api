"""
Lightweight reference example to demonstrate ADK-style agent flow.

This example shows a simple tool-based pattern where a user query
is routed to a function that returns structured output.
"""

from typing import Dict


def get_exchange_rate(base: str, target: str) -> Dict[str, str]:
    mock_rates = {
        ("USD", "INR"): "83.10",
        ("EUR", "USD"): "1.08",
        ("GBP", "USD"): "1.27",
    }

    rate = mock_rates.get((base.upper(), target.upper()))
    if rate:
        return {
            "base_currency": base.upper(),
            "target_currency": target.upper(),
            "rate": rate,
            "status": "success",
        }

    return {
        "base_currency": base.upper(),
        "target_currency": target.upper(),
        "rate": "N/A",
        "status": "not_found",
    }


def run_agent(user_query: str) -> Dict[str, str]:
    query = user_query.lower()

    if "convert" in query:
        return {"message": "Conversion feature coming soon"}
    if "usd" in query and "inr" in query:
        return get_exchange_rate("USD", "INR")
    if "eur" in query and "usd" in query:
        return get_exchange_rate("EUR", "USD")
    if "gbp" in query and "usd" in query:
        return get_exchange_rate("GBP", "USD")

    return {
        "status": "unsupported_query",
        "message": "Please ask for a supported currency pair like USD to INR.",
    }


if __name__ == "__main__":
    sample_query = "What is the exchange rate from USD to INR?"
    print(run_agent(sample_query))
