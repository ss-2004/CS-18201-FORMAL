# Q5 Verify fairness conditions in a concurrent system using temporal logic.

class SystemModel:
    def __init__(self):
        self.states = []
        self.transitions = {}
        self.current_state = None

    def add_state(self, state):
        self.states.append(state)
        self.transitions[state] = []

    def add_transition(self, from_state, to_state):
        if from_state in self.states and to_state in self.states:
            self.transitions[from_state].append(to_state)

    def set_initial_state(self, state):
        if state in self.states:
            self.current_state = state

    def get_reachable_states(self, state, visited=None):
        if visited is None:
            visited = set()
        if state in visited:
            return visited
        visited.add(state)
        for next_state in self.transitions.get(state, []):
            self.get_reachable_states(next_state, visited)
        return visited


class TemporalLogicChecker:
    @staticmethod
    def globally(system, condition):
        visited = system.get_reachable_states(system.current_state)
        return all(condition(state) for state in visited)

    @staticmethod
    def eventually(system, condition):
        visited = system.get_reachable_states(system.current_state)
        return any(condition(state) for state in visited)

    @staticmethod
    def fairness_condition(system, request_condition, grant_condition):
        visited = system.get_reachable_states(system.current_state)
        for state in visited:
            if request_condition(state):
                if not any(grant_condition(next_state) for next_state in visited):
                    return False
        return True


system = SystemModel()

system.add_state("idle")
system.add_state("request")
system.add_state("critical")

system.add_transition("idle", "request")
system.add_transition("request", "critical")
system.add_transition("critical", "idle")

system.set_initial_state("idle")

request_condition = lambda state: state == "request"
grant_condition = lambda state: state == "critical"
fairness_result = TemporalLogicChecker.fairness_condition(system, request_condition, grant_condition)

print("Fairness Condition Holds?" , fairness_result)