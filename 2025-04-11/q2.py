# Q2 Develop a simulation tool for Nondeterministic Finite Automata (NFA) and check equivalence with a DFA.

from collections import defaultdict
from itertools import product

EPSILON = 'ε'

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, state_set):
        stack = list(state_set)
        closure = set(state_set)

        while stack:
            state = stack.pop()
            for next_state in self.transition_function.get((state, EPSILON), []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, state_set, symbol):
        result = set()
        for state in state_set:
            result.update(self.transition_function.get((state, symbol), []))
        return result

    def accepts(self, input_string):
        current_states = self.epsilon_closure({self.start_state})
        for symbol in input_string:
            current_states = self.epsilon_closure(self.move(current_states, symbol))
        return any(state in self.accept_states for state in current_states)


class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        state = self.start_state
        for symbol in input_string:
            state = self.transition_function.get((state, symbol))
            if state is None:
                return False
        return state in self.accept_states


def nfa_to_dfa(nfa):
    state_map = {}
    dfa_states = set()
    dfa_start = frozenset(nfa.epsilon_closure({nfa.start_state}))
    unmarked_states = [dfa_start]
    dfa_trans = {}
    dfa_accepts = set()

    while unmarked_states:
        current = unmarked_states.pop()
        if current not in dfa_states:
            dfa_states.add(current)
            if any(state in nfa.accept_states for state in current):
                dfa_accepts.add(current)

            for symbol in nfa.alphabet:
                move_result = nfa.move(current, symbol)
                closure = frozenset(nfa.epsilon_closure(move_result))
                if closure:
                    dfa_trans[(current, symbol)] = closure
                    if closure not in dfa_states and closure not in unmarked_states:
                        unmarked_states.append(closure)

    return DFA(
        states=dfa_states,
        alphabet=nfa.alphabet,
        transition_function=dfa_trans,
        start_state=dfa_start,
        accept_states=dfa_accepts
    )


def generate_all_strings(alphabet, max_length):
    result = set()
    for l in range(max_length + 1):
        for p in product(alphabet, repeat=l):
            result.add(''.join(p))
    return result


def check_equivalence(nfa, dfa, test_depth=4):
    test_set = generate_all_strings(nfa.alphabet, test_depth)
    for test_str in test_set:
        if nfa.accepts(test_str) != dfa.accepts(test_str):
            print(f"Mismatch found for input: '{test_str}'")
            return False
    return True


if __name__ == "__main__":
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transition_function = {
        ('q0', '0'): {'q0', 'q1'},
        ('q0', '1'): {'q0'},
        ('q1', '1'): {'q2'},
    }
    start_state = 'q0'
    accept_states = {'q2'}

    nfa = NFA(states, alphabet, transition_function, start_state, accept_states)
    dfa = nfa_to_dfa(nfa)

    print("Testing equivalence of NFA and converted DFA...")
    equivalent = check_equivalence(nfa, dfa)

    if equivalent:
        print("✅ NFA and DFA are equivalent (within test depth).")
    else:
        print("❌ NFA and DFA are NOT equivalent.")
