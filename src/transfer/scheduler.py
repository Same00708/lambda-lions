"""Download orchestration and scheduling."""

import asyncio


class Scheduler:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def enqueue(self, task):
        await self.queue.put(task)

    async def process(self):
        while True:
            task = await self.queue.get()
            await task()
