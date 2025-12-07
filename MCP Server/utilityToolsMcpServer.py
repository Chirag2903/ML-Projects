from mcp.server.fastmcp import FastMCP

mcp=FastMCP("utilityTools")

@mcp.tool()
def percentage(value: float, percent: float) -> float:
    """Calculate X% of a given number."""
    return (value * percent) / 100

@mcp.tool()
def average(numbers: list[float]) -> float:
    """Return the average of numbers."""
    if not numbers:
        raise ValueError("List is empty.")
    return sum(numbers) / len(numbers)


@mcp.tool()
def minmax(numbers: list[float]) -> dict:
    """Return the min and max of a list."""
    if not numbers:
        raise ValueError("List is empty.")
    return {
        "min": min(numbers),
        "max": max(numbers),
    }

@mcp.tool()
def convert_km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


@mcp.tool()
def convert_celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius → Fahrenheit."""
    return (c * 9/5) + 32

@mcp.tool()
def ping() -> str:
    """Simple health check."""
    return "Utility Calculator Server is alive!"


if __name__ == "__main__":
    mcp.run(transport="stdio")