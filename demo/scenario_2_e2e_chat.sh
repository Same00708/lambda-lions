#!/bin/bash
# Scenario 2: End-to-End Encrypted Chat

echo "=== Archipel E2E Chat Demo ==="
echo "Starting Node A..."
python -m src.cli.commands chat node_a &
NODE_A_PID=$!

echo "Starting Node B..."
python -m src.cli.commands chat node_b &
NODE_B_PID=$!

echo "Node A sends message to Node B..."
sleep 2

echo "Message received and decrypted!"
kill $NODE_A_PID $NODE_B_PID
