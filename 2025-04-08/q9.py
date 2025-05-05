# Lab 9: Real-World Protocol Verification
# Simulate the TCP three-way handshake using Python:

def tcp_handshake(env):
    print("SYN sent")
    yield env.timeout(1)
    print("SYN-ACK received")
    yield env.timeout(1)
    print("ACK sent")
    yield env.timeout(1)
    print("Connection Established")

env = simpy.Environment()
env.process(tcp_handshake(env))
env.run(until=5)