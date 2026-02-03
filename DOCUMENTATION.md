# MCP Setup Challenge Documentation

## Overview
This project demonstrates the setup and configuration of the Model Context Protocol (MCP) for AI agent workflows. It includes research on industry best practices, configuration of MCP servers, and a functional proof-of-concept.

## Deliverables
- **.vscode/mcp.json**: Configuration for the Tenx MCP Analysis server.
- **.github/copilot-instructions.md**: Rigorous rules and workflows for the AI agent.
- **deliverables/MCP_Setup_Challenge.pptx**: A summary presentation of the project.
- **deliverables/proof_of_concept/**: Source code for a local MCP server and client demonstration.
- **run_poc.sh**: A script to execute the proof-of-concept.

## Research & Methodology
- **Boris Cherny's Workflow**: Researched the workflow principles of Boris Cherny (creator of Claude Code), emphasizing:
    - **Plan vs. Act**: Distinguishing between analysis and implementation phases.
    - **Codebase Exploration**: Using search and glob tools to build context before editing.
    - **Intent Logging**: Explicitly stating the purpose of tool calls.
- **MCP Protocol**: Analyzed the Model Context Protocol for tool-calling, resource access, and prompt management.

## Proof of Concept (PoC)
To prove the configurations actually run and the protocol is understood, a local MCP demonstration was implemented:
- **Server**: Uses `mcp.server.fastmcp` to expose a `get_system_info` tool.
- **Client**: Uses `mcp.ClientSession` to connect via stdio, list tools, and execute them.
- **Result**: Successfully retrieved system information (OS, version, etc.) through the MCP protocol.

### Running the PoC
Ensure you have the necessary dependencies installed:
```bash
pip install mcp fastapi uvicorn python-pptx httpx
```
Then run the PoC script:
```bash
./run_poc.sh
```

## Challenges & Iterations
- **Authentication**: The remote Tenx proxy requires OAuth2. While the configuration is correct, a 401 error is expected without a browser-based login flow.
- **Library Selection**: Iterated through different MCP library versions and APIs (FastMCP vs. low-level) to find the most efficient implementation.
- **Deliverable Organization**: Restructured the repository to separate source code, utilities, and final outputs into a dedicated `deliverables` directory.

## Insights
- **Behavioral Control**: Rules files (`copilot-instructions.md`) are active guardrails that significantly improve agent reliability and transparency.
- **Standardization**: MCP provides a powerful standard for extending AI capabilities across different platforms and tools.

## Recent Iterations (Feb 2, 2026)
- **Implemented local MCP PoC**: Added `mcp_server.py` and `mcp_client_stdio.py` to prove configuration logic works in practice.
- **Enhanced Rules**: Updated `copilot-instructions.md` with a detailed evaluation rubric and explicit iteration requirements.
- **Deliverable Organization**: Created a structured `deliverables/` hierarchy and added a `run_poc.sh` for easy verification.
- **PowerPoint Deliverable**: Generated a comprehensive project summary presentation.