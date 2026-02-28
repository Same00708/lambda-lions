"""File chunking utilities (split/merge)."""


def chunk_file(filepath: str, chunk_size: int = 512 * 1024):
    """Split file into chunks and yield them."""
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def write_chunk(output_path: str, chunk: bytes, append=True):
    """Write a chunk to output file."""
    mode = 'ab' if append else 'wb'
    with open(output_path, mode) as f:
        f.write(chunk)
