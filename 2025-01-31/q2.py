# Model and simulate a parallel composition of two CCS processes in Python, where both
# processes execute concurrently.

import threading
import time

class CCSProcess:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
        self.current_index = 0

    def execute(self):
        while self.current_index < len(self.actions):
            action = self.actions[self.current_index]
            print(f"Process {self.name} performs action: {action}")
            self.current_index += 1
            time.sleep(1)

        print(f"Process {self.name} has finished execution.")

def parallel_composition(process1, process2):
    thread1 = threading.Thread(target=process1.execute)
    thread2 = threading.Thread(target=process2.execute)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Both processes have completed execution.")

process_A = CCSProcess("P1", ["a", "b", "c"])
process_B = CCSProcess("P2", ["x", "y", "z"])

parallel_composition(process_A, process_B)