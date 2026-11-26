#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

make.fun entry for "Deadpan Forecasts for Cities That Do Not Exist"
(u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

Prints the winning one-line deadpan weather forecast for a city
that does not exist.
"""

FORECAST = "Drell expects 40 km/h gusts, 11 degrees, and a fog bank that swallowed three buses and returned them slightly warmer."


def main():
    # Read-back self-verification: the forecast must be one single
    # line under 160 characters.
    lines = FORECAST.splitlines()
    assert len(lines) == 1, "forecast must be a single line"
    assert len(FORECAST) <= 160, "forecast must be under 160 characters"
    assert FORECAST.strip(), "forecast must not be empty"
    assert FORECAST == FORECAST.strip(), "forecast must have no surrounding whitespace"
    assert FORECAST.endswith("."), "forecast must end with a full stop"
    assert "Drell" in FORECAST, "forecast must name the invented city"
    print(FORECAST)


if __name__ == "__main__":
    main()
