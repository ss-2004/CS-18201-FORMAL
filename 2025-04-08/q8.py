# Lab 8: Advanced Temporal Verification
# Model a banking transaction system and verify fairness properties using SPIN or Python.
# Banking Transaction Example
def bank_transaction(env):
    print(f"Transaction Initiated at {env.now}")
    yield env.timeout(2)
    print(f"Transaction Approved at {env.now}")

env = simpy.Environment()
env.process(bank_transaction(env))
env.run(until=5)