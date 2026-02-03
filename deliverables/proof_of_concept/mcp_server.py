from mcp.server.fastmcp import FastMCP
import platform
import json

# Create an MCP server
mcp = FastMCP("TenxPoCServer")

@mcp.tool()
def get_system_info() -> str:
    """Returns information about the current system environment."""
    info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    # FastMCP can run as a stdio server by default, 
    # but for this PoC we want to show it running.
    # We'll use the built-in run method which handles the transport.
    mcp.run()