# Write a Python program to verify synchronization between two CCS processes

import threading
import queue
import time

class CCSChannel:
    def __init__(self):
        self.channel = queue.Queue()

    def synchronize(self, action):
        try:
            complement = "ā" if action == "a" else "a"
            if not self.channel.empty() and self.channel.queue[0] == complement:
                self.channel.get()
                print(f"[Channel] Synchronization successful: ({action}, {complement})")
                return True
            else:
                self.channel.put(action)
                return False
        except Exception as e:
            print(f"[Channel] Error: {e}")
            return False


class CCSProcess:
    def __init__(self, name, action, channel):
        self.name = name
        self.action = action
        self.channel = channel

    def execute(self):
        print(f"[{self.name}] Performing action: {self.action}")
        time.sleep(1)

        if self.channel.synchronize(self.action):
            print(f"[{self.name}] Synchronized successfully with a complementary action!")
        else:
            print(f"[{self.name}] Waiting for a complementary action...")


channel = CCSChannel()

process1 = CCSProcess("P1", "a", channel)
process2 = CCSProcess("P2", "ā", channel)

thread1 = threading.Thread(target=process1.execute)
thread2 = threading.Thread(target=process2.execute)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("CCS synchronization verification completed.")