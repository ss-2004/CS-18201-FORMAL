# 3. Simulate a process algebra-based load balancer where multiple clients send requests to a central
# dispatcher that distributes tasks among available workers. Verify that requests are handled
# fairly without starvation.

import asyncio
import random

class Worker:
    def __init__(self, worker_id):
        self.worker_id = worker_id

    async def process_request(self, request_id):
        process_time = random.uniform(1, 3)
        await asyncio.sleep(process_time)
        print(f"Worker {self.worker_id} completed request {request_id} in {process_time:.2f}s")

class Dispatcher:
    def __init__(self, num_workers):
        self.workers = [Worker(i) for i in range(num_workers)]
        self.queue = asyncio.Queue()
        self.round_robin_index = 0

    async def add_request(self, request_id):
        await self.queue.put(request_id)

    async def dispatch_requests(self):
        while True:
            request_id = await self.queue.get()
            worker = self.workers[self.round_robin_index]
            self.round_robin_index = (self.round_robin_index + 1) % len(self.workers)
            asyncio.create_task(worker.process_request(request_id))
            self.queue.task_done()

async def client(dispatcher, client_id, num_requests):
    for i in range(num_requests):
        request_id = f"C{client_id}-R{i}"
        print(f"Client {client_id} sending request {request_id}")
        await dispatcher.add_request(request_id)
        await asyncio.sleep(random.uniform(0.5, 1.5))

async def main():
    num_clients = 3
    num_requests_per_client = 5
    num_workers = 2

    dispatcher = Dispatcher(num_workers)
    asyncio.create_task(dispatcher.dispatch_requests())
    client_tasks = [asyncio.create_task(client(dispatcher, i, num_requests_per_client)) for i in range(num_clients)]

    await asyncio.gather(*client_tasks)
    await dispatcher.queue.join()

if __name__ == "__main__":
    asyncio.run(main())
