# 1. Write a Python program to model a client-server interaction using CCS process constructions. The
# client sends a request (req) and waits for a response (res), while the server listens for req, processes it,
# and responds with res. Simulate the sequential communication between both processes.

import asyncio

async def client(server_queue, client_queue):
    print("Client: Sending request (req)")
    await server_queue.put("req")

    response = await client_queue.get()
    print(f"Client: Received response ({response})")

async def server(server_queue, client_queue):
    request = await server_queue.get()
    print(f"Server: Received request ({request})")

    await asyncio.sleep(1)

    print("Server: Sending response (res)")
    await client_queue.put("res")


async def main():
    server_queue = asyncio.Queue()
    client_queue = asyncio.Queue()
    await asyncio.gather(client(server_queue, client_queue), server(server_queue, client_queue))

asyncio.run(main())
