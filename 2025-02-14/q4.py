# 4. Write a Python program to define two finite-state processes in CCS and implement a bisimulation
# equivalence check between them. The program should determine whether both processes exhibit the
# same behavior using strong bisimulation principles from CWB.

class Process:
    def __init__(self, name):
        self.name = name
        self.states = {}
        self.initial_state = None

    def add_state(self, state, transitions):
        self.states[state] = transitions

    def set_initial_state(self, state):
        self.initial_state = state

def strong_bisimulation(p1, p2):
    visited = set()
    return check_bisimulation(p1.initial_state, p2.initial_state, p1, p2, visited)

def check_bisimulation(state1, state2, p1, p2, visited):
    if (state1, state2) in visited:
        return True
    visited.add((state1, state2))

    transitions1 = p1.states.get(state1, {})
    transitions2 = p2.states.get(state2, {})

    if transitions1.keys() != transitions2.keys():
        return False

    for action in transitions1:
        next_states1 = transitions1[action]
        next_states2 = transitions2[action]

        if len(next_states1) != len(next_states2):
            return False

        for next_state1, next_state2 in zip(next_states1, next_states2):
            if not check_bisimulation(next_state1, next_state2, p1, p2, visited):
                return False

    return True

P = Process("P")
Q = Process("Q")

P.add_state("s0", {"a": ["s1"], "b": ["s2"]})
P.add_state("s1", {"c": ["s0"]})
P.add_state("s2", {})

Q.add_state("t0", {"a": ["t1"], "b": ["t2"]})
Q.add_state("t1", {"c": ["t0"]})
Q.add_state("t2", {})

P.set_initial_state("s0")
Q.set_initial_state("t0")

is_equivalent = strong_bisimulation(P, Q)

print(f"Are processes P and Q equivalent under strong bisimulation? {is_equivalent}")
