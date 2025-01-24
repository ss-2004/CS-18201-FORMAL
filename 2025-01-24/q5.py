# 5. Write a Python program to simulate process communication using the Communicating
# Sequential Processes (CSP) model.

import threading
import queue
import time

class CSPChannel:
    def __init__(self):
        self.channel = queue.Queue()

    def send(self, data):
        self.channel.put(data)

    def receive(self):
        return self.channel.get()

def process_a(channel_out, data):
    print("Process A: Sending data to Process B...")
    time.sleep(1)
    channel_out.send(data)
    print(f"Process A: Sent data '{data}' to Process B.")


def process_b(channel_in, channel_out):
    print("Process B: Waiting to receive data from Process A...")
    data = channel_in.receive()
    print(f"Process B: Received data '{data}' from Process A.")
    time.sleep(1)
    response = f"{data} processed by B"
    print("Process B: Sending response to Process C...")
    channel_out.send(response)

def process_c(channel_in):
    print("Process C: Waiting to receive response from Process B...")
    response = channel_in.receive()
    print(f"Process C: Received response '{response}' from Process B.")


if __name__ == "__main__":
    channel_a_to_b = CSPChannel()
    channel_b_to_c = CSPChannel()

    thread_a = threading.Thread(target=process_a, args=(channel_a_to_b, "Hello, B!"))
    thread_b = threading.Thread(target=process_b, args=(channel_a_to_b, channel_b_to_c))
    thread_c = threading.Thread(target=process_c, args=(channel_b_to_c,))

    thread_a.start()
    thread_b.start()
    thread_c.start()

    thread_a.join()
    thread_b.join()
    thread_c.join()

    print("All processes completed communication.")
