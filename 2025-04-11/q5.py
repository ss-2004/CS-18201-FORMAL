# Q5 Implement Minimization of Finite State Machines (FSMs) and verify equivalence between two FSMs.

from collections import defaultdict
from typing import Set, Dict, Tuple, List, FrozenSet

class FSM:
    def __init__(self, states: Set[str], alphabet: Set[str], transition: Dict[Tuple[str, str], str],
                 start_state: str, accept_states: Set[str]):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accept_states = accept_states

    def __repr__(self):
        return f"FSM(start={self.start_state}, accept={self.accept_states})"

    def minimize(self):
        partition = [self.accept_states, self.states - self.accept_states]
        stable = False

        while not stable:
            new_partition = []
            stable = True

            for group in partition:
                group_dict = defaultdict(set)
                for state in group:
                    key = tuple(self.get_target_group(state, sym, partition) for sym in sorted(self.alphabet))
                    group_dict[key].add(state)

                new_partition.extend(group_dict.values())

                if len(group_dict) > 1:
                    stable = False

            partition = new_partition

        new_state_map = {}
        for i, group in enumerate(partition):
            for state in group:
                new_state_map[state] = f'q{i}'

        new_states = set(new_state_map.values())
        new_start = new_state_map[self.start_state]
        new_accept = {new_state_map[s] for s in self.accept_states}
        new_trans = {}

        for (state, sym), target in self.transition.items():
            if state in new_state_map and target in new_state_map:
                new_trans[(new_state_map[state], sym)] = new_state_map[target]

        return FSM(new_states, self.alphabet, new_trans, new_start, new_accept)

    def get_target_group(self, state, symbol, partition):
        target = self.transition.get((state, symbol))
        for i, group in enumerate(partition):
            if target in group:
                return i
        return -1

    def is_equivalent(self, other) -> bool:
        min_self = self.minimize()
        min_other = other.minimize()

        return (min_self.states == min_other.states and
                min_self.alphabet == min_other.alphabet and
                min_self.start_state == min_other.start_state and
                min_self.accept_states == min_other.accept_states and
                min_self.transition == min_other.transition)

if __name__ == "__main__":
    states1 = {'A', 'B', 'C', 'D'}
    alphabet = {'0', '1'}
    transitions1 = {
        ('A', '0'): 'B', ('A', '1'): 'C',
        ('B', '0'): 'A', ('B', '1'): 'D',
        ('C', '0'): 'D', ('C', '1'): 'A',
        ('D', '0'): 'C', ('D', '1'): 'B'
    }
    start1 = 'A'
    accept1 = {'A'}

    states2 = {'X', 'Y', 'Z'}
    transitions2 = {
        ('X', '0'): 'Y', ('X', '1'): 'Z',
        ('Y', '0'): 'X', ('Y', '1'): 'Z',
        ('Z', '0'): 'Z', ('Z', '1'): 'X',
    }
    start2 = 'X'
    accept2 = {'X'}

    fsm1 = FSM(states1, alphabet, transitions1, start1, accept1)
    fsm2 = FSM(states2, alphabet, transitions2, start2, accept2)

    print("FSM1 (minimized):", fsm1.minimize().__dict__)
    print("FSM2 (minimized):", fsm2.minimize().__dict__)
    print("Are FSM1 and FSM2 equivalent?", fsm1.is_equivalent(fsm2))