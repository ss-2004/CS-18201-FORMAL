# Q4. Among the formal methods - Model Checking (with Temporal Logic), Petri Nets, Process
# Algebra (e.g., CSP, CCS, π-Calculus), Theorem Proving (e.g., Coq, Isabelle, TLA+), and
# Abstract Interpretation (for static checking) - which is the most suitable for verifying
# concurrent access control mechanisms in a multi-threaded system? Justify your choice and
# demonstrate verification using the selected method.

# Why Model Checking (with Temporal Logic, e.g., TLA+)?
# 1.	Concurrency Modeling: Model checking excels in handling the state-space explosion that occurs due to concurrency.
# 2.	Access Control Properties: Safety (e.g., mutual exclusion) and liveness (e.g., progress, no deadlock) can be specified using temporal logic.
# 3.	Automation: Model checking provides automated tools to exhaustively explore all possible thread interleavings.
# 4.	Expressiveness: TLA+ (Temporal Logic of Actions) allows modeling concurrent processes and specifying high-level properties.
# 5.	Practical Use: Used by industry giants like Amazon and Microsoft to verify real-world concurrent systems.

from itertools import product

IDLE = "IDLE"
WAITING = "WAITING"
CRITICAL = "CRITICAL"
EXIT = "EXIT"

thread_states = [IDLE, WAITING, CRITICAL, EXIT]

state_transitions = {
    IDLE: WAITING,
    WAITING: CRITICAL,
    CRITICAL: EXIT,
    EXIT: IDLE
}

def check_mutual_exclusion(path):
    for state in path:
        if state[0] == CRITICAL and state[1] == CRITICAL:
            return False
    return True

def generate_state_space(depth=3):
    initial = (IDLE, IDLE)
    paths = [[initial]]

    for _ in range(depth):
        new_paths = []
        for path in paths:
            curr = path[-1]
            for i in [0, 1]:
                new_state = list(curr)
                current_state = curr[i]
                next_state = state_transitions.get(current_state)
                if next_state:
                    new_state[i] = next_state
                    new_paths.append(path + [tuple(new_state)])
        paths = new_paths
    return paths

def main():
    print("Model Checking Concurrent Access (Mutual Exclusion)...")
    all_paths = generate_state_space(depth=5)
    violated = 0

    for i, path in enumerate(all_paths):
        if not check_mutual_exclusion(path):
            print(f"❌ Violation in Path {i}:")
            for state in path:
                print("  ", state)
            violated += 1

    if violated == 0:
        print("✅ No mutual exclusion violations found.")
    else:
        print(f"❌ Total Violations Found: {violated}")

if __name__ == "__main__":
    main()
