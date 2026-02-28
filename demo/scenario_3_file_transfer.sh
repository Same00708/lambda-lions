#!/bin/bash
# Scenario 3: File Transfer with Chunking and BitTorrent-style Download

echo "=== Archipel File Transfer Demo ==="
echo "Generating test file..."
python scripts/generate_test_file.py

echo "Starting seeder node..."
python -m src.cli.commands transfer seed test_50mb.bin &
SEEDER_PID=$!

echo "Starting downloader node..."
python -m src.cli.commands transfer download test_50mb.bin &
DOWNLOADER_PID=$!

echo "Download started with rarest-first strategy..."
sleep 10

echo "File transfer complete!"
kill $SEEDER_PID $DOWNLOADER_PID
