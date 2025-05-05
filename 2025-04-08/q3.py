# Lab 3: Pi-Calculus and Dynamic Systems
# For dynamic systems, use Python functions to model communication and dynamic behavior.

import simpy
def client_server(env):
    print(f"Client sends request at {env.now}")
    yield env.timeout(1)
    print(f"Server processes request at {env.now}")
    yield env.timeout(2)
    print(f"Server sends response at {env.now}")

env = simpy.Environment()
env.process(client_server(env))
env.run(until=5)