"""Rarest First downloader with parallel pipeline."""

import asyncio


class Downloader:
    def __init__(self, peers, manifest):
        self.peers = peers
        self.manifest = manifest
        self.downloaded = set()

    async def download(self):
        """Implement parallel chunk download with rarest-first strategy."""
        tasks = []
        for chunk_hash in self.manifest.chunks:
            # select rarest peer, request chunk
            task = self._download_chunk(chunk_hash)
            tasks.append(task)
        await asyncio.gather(*tasks)

    async def _download_chunk(self, chunk_hash):
        # fetch from peer
        pass
