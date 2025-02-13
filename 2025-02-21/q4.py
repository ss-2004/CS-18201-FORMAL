# 4. Implement a Python-based verification system that checks whether two given finite-state
# processes are equivalent using strong bisimulation. The program should take two process
# descriptions as input and determine whether they exhibit the same external behavior

from collections import defaultdict, deque

class LTS:
    def __init__(self, transitions, initial_state):
        self.transitions = defaultdict(set, transitions)
        self.initial_state = initial_state
        self.states = set(transitions.keys()) | {s for targets in transitions.values() for (_, s) in targets}

    def get_transitions(self, state):
        return self.transitions[state]

def bisimulation_check(lts1, lts2):
    queue = deque([(lts1.initial_state, lts2.initial_state)])
    visited = set()

    while queue:
        s1, s2 = queue.popleft()
        if (s1, s2) in visited:
            continue
        visited.add((s1, s2))

        trans1 = defaultdict(set)
        trans2 = defaultdict(set)

        for label, target in lts1.get_transitions(s1):
            trans1[label].add(target)
        for label, target in lts2.get_transitions(s2):
            trans2[label].add(target)

        if set(trans1.keys()) != set(trans2.keys()):
            return False

        for label in trans1:
            if trans1[label] != trans2[label]:
                return False
            for t1, t2 in zip(sorted(trans1[label]), sorted(trans2[label])):
                queue.append((t1, t2))
    return True

transitions1 = {
    'q0': {('a', 'q1'), ('b', 'q2')},
    'q1': {('c', 'q3')},
    'q2': {('c', 'q3')},
    'q3': set()
}

transitions2 = {
    'p0': {('a', 'p1'), ('b', 'p2')},
    'p1': {('c', 'p3')},
    'p2': {('c', 'p3')},
    'p3': set()
}

lts1 = LTS(transitions1, 'q0')
lts2 = LTS(transitions2, 'p0')

print("Equivalent under strong bisimulation?", bisimulation_check(lts1, lts2))
