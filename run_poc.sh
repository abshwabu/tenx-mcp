#!/bin/bash

echo "=== Tenx MCP Setup Challenge: Proof of Concept ==="

# 1. Run MCP Stdio Test
echo ""
echo "Step 1: Running MCP Stdio Client/Server Test..."
python3 deliverables/proof_of_concept/mcp_client_stdio.py

# 2. Generate PowerPoint (if not already there)
echo ""
echo "Step 2: Ensuring PowerPoint deliverable exists..."
if [ ! -f "deliverables/MCP_Setup_Challenge.pptx" ]; then
    python3 deliverables/utils/generate_pptx.py
else
    echo "PowerPoint already exists: deliverables/MCP_Setup_Challenge.pptx"
fi

echo ""
echo "=== PoC Execution Complete ==="
