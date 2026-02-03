import asyncio
import sys
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    # Define server parameters
    server_params = StdioServerParameters(
        command="python3",
        args=["deliverables/proof_of_concept/mcp_server.py"],
        env=None
    )

    print("Connecting to MCP server via stdio...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize session
            print("Initializing session...")
            await session.initialize()

            # List tools
            print("\nListing tools...")
            tools = await session.list_tools()
            print(f"Found {len(tools.tools)} tools:")
            for tool in tools.tools:
                print(f" - {tool.name}: {tool.description}")

            # Call a tool
            if tools.tools:
                tool_name = "get_system_info"
                print(f"\nCalling tool '{tool_name}'...")
                result = await session.call_tool(tool_name, arguments={})
                print("Tool Result:")
                for content in result.content:
                    if content.type == 'text':
                        print(content.text)

if __name__ == "__main__":
    asyncio.run(run_client())

