# Lab 2: Modeling Systems with CCS
#     Python doesn’t directly support CCS, but SimPy can simulate concurrent processes.

import simpy
def producer(env, buffer):
    while True:
        yield env.timeout(1)  # Time to produce
        buffer.append(1)
        print(f"Produced an item at {env.now}, Buffer: {len(buffer)}")

def consumer(env, buffer):
    while True:
        if buffer:
            buffer.pop(0)
            print(f"Consumed an item at {env.now}, Buffer: {len(buffer)}")
        yield env.timeout(2)  # Time to consume

# Run the simulation
env = simpy.Environment()
buffer = []
env.process(producer(env, buffer))
env.process(consumer(env, buffer))
env.run(until=10)
