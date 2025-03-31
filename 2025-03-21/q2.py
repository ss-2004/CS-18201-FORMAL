# Q2 Develop a Python-based Linear Temporal Logic (LTL) model checker for verifying safety and liveness properties.

import networkx as nx

class LTLModelChecker:
    def __init__(self, transition_system):
        self.transition_system = transition_system

    def check_safety(self, atomic_proposition):
        for state in self.transition_system.nodes():
            if atomic_proposition not in self.transition_system.nodes[state]['labels']:
                return False, state
        return True, None

    def check_liveness(self, atomic_proposition):
        satisfying_states = [state for state in self.transition_system.nodes() if
                             atomic_proposition in self.transition_system.nodes[state]['labels']]
        return satisfying_states if satisfying_states else None

ts = nx.DiGraph()
ts.add_nodes_from([
    ("s0", {"labels": {"p"}}),
    ("s1", {"labels": {"q"}}),
])
ts.add_edges_from([("s0", "s1"), ("s1", "s0")])

checker = LTLModelChecker(ts)

safety_result, safety_state = checker.check_safety("p")
liveness_result = checker.check_liveness("q")
print("Safety holds:" if safety_result else f"Safety fails at {safety_state}")
print(f"Liveness holds in states: {liveness_result}" if liveness_result else "Liveness fails")
