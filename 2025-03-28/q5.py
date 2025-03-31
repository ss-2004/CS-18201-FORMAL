# Q5 Implement a distributed computation model using Pi-Calculus for mobile process interactions.

import threading
import queue

class Channel:
    def __init__(self):
        self._queue = queue.Queue()

    def send(self, message):
        self._queue.put(message)

    def receive(self):
        return self._queue.get()

class Process(threading.Thread):
    def __init__(self, name, channel, action):
        super().__init__()
        self.name = name
        self.channel = channel
        self.action = action

    def run(self):
        # Execute the action
        self.action(self.channel)

def action_a(channel):
    print("Process A: Waiting to receive a message.")
    message = channel.receive()
    print(f"Process A: Received message '{message}'")
    print("Process A: Sending response.")
    channel.send("Hello from Process A")

def action_b(channel):
    print("Process B: Sending message to Process A.")
    channel.send("Hello from Process B")
    message = channel.receive()
    print(f"Process B: Received message '{message}'")

channel = Channel()

process_a = Process("Process A", channel, action_a)
process_b = Process("Process B", channel, action_b)

process_b.start()
process_a.start()

process_b.join()
process_a.join()

print("Both processes have completed their interactions.")
