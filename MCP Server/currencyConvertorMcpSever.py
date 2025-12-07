from mcp.server.fastmcp import FastMCP

mcp=FastMCP("currencyConvertor")

@mcp.tool()
def currencyConvertor(value: float) -> float:
    """Calculate Dollar to Indian rupees."""
    return (value * 90)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")