"""Chunk storage and indexing with SQLite."""

import sqlite3


class Storage:
    def __init__(self, db_file='chunks.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS chunks (
            chunk_hash TEXT PRIMARY KEY,
            filename TEXT,
            chunk_index INTEGER,
            data BLOB
            )"""
        )

    def store_chunk(self, chunk_hash, filename, index, data):
        self.conn.execute(
            "INSERT OR REPLACE INTO chunks VALUES (?, ?, ?, ?)",
            (chunk_hash, filename, index, data)
        )
        self.conn.commit()

    def get_chunk(self, chunk_hash):
        cursor = self.conn.execute(
            "SELECT data FROM chunks WHERE chunk_hash = ?",
            (chunk_hash,)
        )
        row = cursor.fetchone()
        return row[0] if row else None
