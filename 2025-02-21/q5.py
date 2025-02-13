# 5. Design a producer-consumer system using CCS principles, ensuring correct message passing
# and proper synchronization between the producer and the consumer while preventing
# deadlocks

import threading
import queue
import time

class Producer(threading.Thread):
    def __init__(self, buffer, event):
        super().__init__()
        self.buffer = buffer
        self.event = event

    def run(self):
        for i in range(5):
            time.sleep(1)
            item = f"Item-{i}"
            self.buffer.put(item)
            print(f"Produced: {item}")
            self.event.set()
        self.buffer.put(None)
        self.event.set()

class Consumer(threading.Thread):
    def __init__(self, buffer, event):
        super().__init__()
        self.buffer = buffer
        self.event = event

    def run(self):
        while True:
            self.event.wait()
            self.event.clear()
            item = self.buffer.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            time.sleep(2)

if __name__ == "__main__":
    buffer = queue.Queue()
    event = threading.Event()

    producer = Producer(buffer, event)
    consumer = Consumer(buffer, event)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Processing complete.")
