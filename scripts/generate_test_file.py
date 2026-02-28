#!/usr/bin/env python3
"""Generate a 50MB test file for transfer testing."""

import os

def generate_test_file(filename="test_50mb.bin", size_mb=50):
    """Generate a file with random data."""
    size_bytes = size_mb * 1024 * 1024
    with open(filename, "wb") as f:
        # Write in chunks to avoid memory issues
        chunk_size = 1024 * 1024  # 1MB chunks
        for _ in range(size_mb):
            f.write(os.urandom(chunk_size))
    print(f"Generated {filename} ({size_mb}MB)")

if __name__ == "__main__":
    generate_test_file()
