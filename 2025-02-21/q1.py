# 1. Implement a system where two processes communicate using the π-Calculus framework,
# dynamically creating channels and exchanging messages. Ensure that the processes interact
# correctly and handle concurrent execution

import multiprocessing

def process_a(channel_queue, name):
    new_channel = multiprocessing.Manager().Queue()
    print(f"{name}: Created new channel and sending it to Process B")
    channel_queue.put(new_channel)

    message = f"Hello from {name}!"
    print(f"{name}: Sending message: {message}")
    new_channel.put(message)

def process_b(channel_queue, name):
    new_channel = channel_queue.get()
    print(f"{name}: Received new channel from Process A")

    message = new_channel.get()
    print(f"{name}: Received message: {message}")

def main():
    with multiprocessing.Manager() as manager:
        channel_queue = manager.Queue()

        process1 = multiprocessing.Process(target=process_a, args=(channel_queue, "Process A"))
        process2 = multiprocessing.Process(target=process_b, args=(channel_queue, "Process B"))

        process1.start()
        process2.start()

        process1.join()
        process2.join()

if __name__ == "__main__":
    main()
