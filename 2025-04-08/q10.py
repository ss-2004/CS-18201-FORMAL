# Lab 10: Comprehensive System Modeling and Verification
# Model an elevator control system in Python:

def elevator(env, floors):
    current_floor = 0
    for target_floor in floors:
        print(f"Elevator moving from {current_floor} to {target_floor} at {env.now}")
        yield env.timeout(abs(target_floor - current_floor)) # Time to move
        current_floor = target_floor
        print(f"Elevator arrived at {current_floor} at {env.now}")

env = simpy.Environment()
floors = [0, 2, 5, 1]
env.process(elevator(env, floors))
env.run()