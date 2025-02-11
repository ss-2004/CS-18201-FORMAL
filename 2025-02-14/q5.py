# 5. Design a Python program to simulate a fair resource scheduler for two processes (P and Q). Ensure
#     that both processes get access to a shared resource in a round-robin manner, preventing livelock or
# starvation. Verify fairness using CCS-style modeling.

import threading
import time

class Resource:
    def __init__(self):
        self.lock = threading.Lock()
        self.turn = 'P'

    def access(self, process_name):
        while True:
            with self.lock:
                if self.turn == process_name:
                    print(f"Process {process_name} is accessing the shared resource")
                    time.sleep(1)
                    self.turn = 'P' if process_name == 'Q' else 'Q'

def process(resource, process_name):
    while True:
        resource.access(process_name)

resource = Resource()
p_thread = threading.Thread(target=process, args=(resource, 'P'))
q_thread = threading.Thread(target=process, args=(resource, 'Q'))

p_thread.start()
q_thread.start()

p_thread.join()
q_thread.join()
