# Simulate a basic producer-consumer system using Python

import threading
import queue
import time

class ProducerConsumer:
    def __init__(self, buffer_size=5):
        self.buffer = queue.Queue(maxsize=buffer_size)
        self.lock = threading.Lock()
        self.produce_count = 0
        self.consume_count = 0

    def produce(self):
        while self.produce_count < 10:
            time.sleep(1)
            item = f"Item-{self.produce_count}"

            with self.lock:
                if not self.buffer.full():
                    self.buffer.put(item)
                    print(f"[Producer] Produced: {item}")
                    self.produce_count += 1
                else:
                    print("[Producer] Buffer full! Waiting...")

    def consume(self):
        while self.consume_count < 10:
            time.sleep(2)

            with self.lock:
                if not self.buffer.empty():
                    item = self.buffer.get()
                    print(f"[Consumer] Consumed: {item}")
                    self.consume_count += 1
                else:
                    print("[Consumer] Buffer empty! Waiting...")

pc_system = ProducerConsumer(buffer_size=5)

producer_thread = threading.Thread(target=pc_system.produce)
consumer_thread = threading.Thread(target=pc_system.consume)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Producer-Consumer simulation completed.")