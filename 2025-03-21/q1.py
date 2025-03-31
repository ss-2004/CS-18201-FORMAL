# Q1 Implement a Kripke Structure in Python and verify Computation Tree Logic (CTL) properties.

class KripkeStructure:
    def __init__(self):
        self.states = set()
        self.transitions = {}
        self.labeling = {}

    def add_state(self, state, labels=set()):
        self.states.add(state)
        self.transitions[state] = set()
        self.labeling[state] = labels

    def add_transition(self, state_from, state_to):
        if state_from in self.states and state_to in self.states:
            self.transitions[state_from].add(state_to)

    def satisfies(self, state, prop):
        return prop in self.labeling.get(state, set())


def EX(kripke, prop):
    result = set()
    for state in kripke.states:
        if any(kripke.satisfies(next_state, prop) for next_state in kripke.transitions[state]):
            result.add(state)
    return result


def AX(kripke, prop):
    result = set()
    for state in kripke.states:
        if kripke.transitions[state] and all(
                kripke.satisfies(next_state, prop) for next_state in kripke.transitions[state]):
            result.add(state)
    return result


def EG(kripke, prop):
    result = set()
    for state in kripke.states:
        visited, stack = set(), [state]
        while stack:
            s = stack.pop()
            if s in visited:
                continue
            visited.add(s)
            if not kripke.satisfies(s, prop):
                break
            stack.extend(kripke.transitions[s])
        else:
            result.add(state)
    return result


def test_kripke_structure():
    ks = KripkeStructure()
    ks.add_state("s0", {"a"})
    ks.add_state("s1", {"b"})
    ks.add_state("s2", {"a", "b"})

    ks.add_transition("s0", "s1")
    ks.add_transition("s1", "s2")
    ks.add_transition("s2", "s0")

    print("EX(b):", EX(ks, "b"))
    print("AX(b):", AX(ks, "b"))
    print("EG(a):", EG(ks, "a"))


test_kripke_structure()
