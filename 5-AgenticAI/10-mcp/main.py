from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Calculator")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power b."""
    return a ** b


@mcp.tool()
def modulus(a: int, b: int) -> int:
    """Return remainder after division."""
    return a % b


if __name__ == "__main__":
    mcp.run()