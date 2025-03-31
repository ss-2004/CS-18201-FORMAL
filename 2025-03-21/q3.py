# Q3 Model a state transition system and check for deadlock freedom using model checking.

class StateTransitionSystem:
    def __init__(self):
        self.transitions = {}

    def add_state(self, state):
        if state not in self.transitions:
            self.transitions[state] = []

    def add_transition(self, from_state, to_state):
        if from_state not in self.transitions:
            self.add_state(from_state)
        if to_state not in self.transitions:
            self.add_state(to_state)
        self.transitions[from_state].append(to_state)

    def check_deadlock_freedom(self):
        deadlocks = [state for state in self.transitions if not self.transitions[state]]
        if deadlocks:
            print("Deadlock detected in states:", deadlocks)
            return False
        else:
            print("System is deadlock-free.")
            return True

sts = StateTransitionSystem()
sts.add_transition("S1", "S2")
sts.add_transition("S2", "S3")
sts.add_transition("S3", "S4")
sts.add_transition("S4", "S2")

sts.check_deadlock_freedom()
