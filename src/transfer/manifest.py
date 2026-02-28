"""File manifest and metadata."""

import json
from typing import List


class Manifest:
    def __init__(self, filename: str, file_hash: str, total_size: int):
        self.filename = filename
        self.file_hash = file_hash
        self.total_size = total_size
        self.chunks: List[str] = []

    def add_chunk(self, chunk_hash: str):
        self.chunks.append(chunk_hash)

    def to_json(self) -> str:
        return json.dumps({
            "filename": self.filename,
            "file_hash": self.file_hash,
            "total_size": self.total_size,
            "chunks": self.chunks
        })

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        m = cls(data["filename"], data["file_hash"], data["total_size"])
        m.chunks = data["chunks"]
        return m
