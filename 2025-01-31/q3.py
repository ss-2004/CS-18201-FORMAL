# Implement Pi-Calculus communication in Python

import threading
import queue
import time

class PiChannel:
    def __init__(self):
        self.channel = queue.Queue()

    def send(self, message):
        print(f"[Channel] Sending message: {message}")
        self.channel.put(message)

    def receive(self):
        message = self.channel.get()
        print(f"[Channel] Received message: {message}")
        return message


class SenderProcess:
    def __init__(self, name, channel, message):
        self.name = name
        self.channel = channel
        self.message = message

    def send_message(self):
        print(f"[{self.name}] Preparing to send message...")
        time.sleep(1)
        self.channel.send(self.message)
        print(f"[{self.name}] Message sent: {self.message}")


class ReceiverProcess:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    def receive_message(self):
        print(f"[{self.name}] Waiting for a message...")
        message = self.channel.receive()
        print(f"[{self.name}] Message received: {message}")

channel = PiChannel()

sender = SenderProcess("Sender", channel, "Hello, Pi-Calculus!")
receiver = ReceiverProcess("Receiver", channel)

sender_thread = threading.Thread(target=sender.send_message)
receiver_thread = threading.Thread(target=receiver.receive_message)

receiver_thread.start()
sender_thread.start()

receiver_thread.join()
sender_thread.join()

print("Pi-Calculus communication simulation completed.")