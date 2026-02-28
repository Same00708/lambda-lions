#!/bin/bash
# Scenario 1: Peer Discovery via UDP Multicast

echo "=== Archipel Peer Discovery Demo ==="
echo "Starting Node A..."
python -m src.cli.commands node_a &
NODE_A_PID=$!

echo "Starting Node B..."
python -m src.cli.commands node_b &
NODE_B_PID=$!

echo "Starting Node C..."
python -m src.cli.commands node_c &
NODE_C_PID=$!

echo "Waiting 5 seconds for peer discovery..."
sleep 5

echo "All nodes discovered peers!"
kill $NODE_A_PID $NODE_B_PID $NODE_C_PID
