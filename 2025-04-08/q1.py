# Lab 1: Introduction to Formal Methods Tools
# Objective: Simulate a vending machine using Python.
# Install SimPy (if not installed already)

# !pip install simpy
import simpy
# Vending Machine Model
def vending_machine(env):
    print(f"Vending Machine Ready at {env.now}")
    while True:
        print(f"Waiting for Customer at {env.now}")
        yield env.timeout(5)  # Time until next customer
        print(f"Serving Customer at {env.now}")

# Run the simulation
env = simpy.Environment()
env.process(vending_machine(env))
env.run(until=20)  # Run the simulation for 20 time units
