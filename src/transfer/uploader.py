"""Chunk upload server."""

import asyncio


class Uploader:
    def __init__(self, port=7777):
        self.port = port
        self.server = None

    async def handle_request(self, reader, writer):
        """Handle incoming chunk requests."""
        pass

    async def start(self):
        self.server = await asyncio.start_server(
            self.handle_request, '0.0.0.0', self.port
        )
        async with self.server:
            await self.server.serve_forever()
