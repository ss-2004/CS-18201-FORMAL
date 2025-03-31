# Q4 Implement a property verification tool using CTL for a given transition system.

from itertools import product


class TransitionSystem:
    def __init__(self, states, transitions, initial_states, atomic_props, labeling):
        self.states = states
        self.transitions = transitions
        self.initial_states = initial_states
        self.atomic_props = atomic_props
        self.labeling = labeling

    def get_successors(self, state):
        return self.transitions.get(state, [])


class CTLModelChecker:
    def __init__(self, transition_system):
        self.ts = transition_system

    def check_property(self, formula):
        return self.evaluate(formula, self.ts.initial_states)

    def evaluate(self, formula, states):
        if formula.startswith("EX"):
            subformula = formula[2:].strip()
            return self.ex(subformula, states)
        elif formula.startswith("EF"):
            subformula = formula[2:].strip()
            return self.ef(subformula, states)
        elif formula.startswith("EG"):
            subformula = formula[2:].strip()
            return self.eg(subformula, states)
        elif formula.startswith("AX"):
            subformula = formula[2:].strip()
            return self.ax(subformula, states)
        elif formula.startswith("AF"):
            subformula = formula[2:].strip()
            return self.af(subformula, states)
        elif formula.startswith("AG"):
            subformula = formula[2:].strip()
            return self.ag(subformula, states)
        else:
            return {s for s in states if formula in self.ts.labeling.get(s, [])}

    def ex(self, formula, states):
        sat_states = self.evaluate(formula, self.ts.states)
        return {s for s in states if any(succ in sat_states for succ in self.ts.get_successors(s))}

    def ax(self, formula, states):
        sat_states = self.evaluate(formula, self.ts.states)
        return {s for s in states if all(succ in sat_states for succ in self.ts.get_successors(s))}

    def ef(self, formula, states):
        sat_states = set()
        stack = list(self.evaluate(formula, self.ts.states))
        while stack:
            s = stack.pop()
            if s not in sat_states:
                sat_states.add(s)
                stack.extend([pred for pred in self.ts.states if s in self.ts.get_successors(pred)])
        return sat_states.intersection(states)

    def af(self, formula, states):
        sat_states = self.evaluate(formula, self.ts.states)
        unsat_states = set(self.ts.states) - sat_states
        result = set(states)
        while True:
            new_result = {s for s in result if all(succ in result for succ in self.ts.get_successors(s))}
            if new_result == result:
                break
            result = new_result
        return result

    def eg(self, formula, states):
        sat_states = self.evaluate(formula, self.ts.states)
        result = set()
        stack = [s for s in sat_states if all(succ in sat_states for succ in self.ts.get_successors(s))]
        while stack:
            s = stack.pop()
            if s not in result:
                result.add(s)
                stack.extend(
                    [pred for pred in self.ts.states if pred in sat_states and s in self.ts.get_successors(pred)])
        return result.intersection(states)

    def ag(self, formula, states):
        return states.intersection(self.ts.states - self.ef(f"!({formula})", self.ts.states))


if __name__ == "__main__":
    states = {"s0", "s1", "s2", "s3"}
    transitions = {"s0": ["s1", "s2"], "s1": ["s3"], "s2": ["s3"], "s3": []}
    initial_states = {"s0"}
    atomic_props = {"p"}
    labeling = {"s0": set(), "s1": {"p"}, "s2": set(), "s3": {"p"}}

    ts = TransitionSystem(states, transitions, initial_states, atomic_props, labeling)
    checker = CTLModelChecker(ts)

    formula = "EF p"
    result = checker.check_property(formula)
    print(f"States satisfying {formula}: {result}")
