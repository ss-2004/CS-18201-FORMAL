# 3. Simulate a mobile communication system using Pi-Calculus in Python, where a parent process
# dynamically spawns a child process and exchanges messages over a dynamically created channel.
# Ensure the child process correctly receives and processes the messages.

import asyncio
import random

class Channel:
    def __init__(self, name):
        self.name = name
        self.queue = asyncio.Queue()

    async def send(self, message):
        await self.queue.put(message)

    async def receive(self):
        return await self.queue.get()

async def parent_process():
    channel = Channel("dynamic_channel")

    asyncio.create_task(child_process(channel))

    message = "Hello from parent"
    print(f"Parent: Sending message to child: {message}")
    await channel.send(message)

    response = await channel.receive()
    print(f"Parent: Received response from child: {response}")

async def child_process(channel):
    message = await channel.receive()
    print(f"Child: Received message from parent: {message}")

    response = f"Processed: {message}"

    await channel.send(response)
    print(f"Child: Sent response to parent: {response}")

async def main():
    await parent_process()

asyncio.run(main())
