# Q1 Implement a Deterministic Finite Automaton (DFA) in Python and verify its language acceptance properties.

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Invalid symbol: {symbol}")
                return False
            current_state = self.transition_function.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accept_states


if __name__ == "__main__":
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    start_state = 'q0'
    accept_states = {'q2'}

    transition_function = {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q0',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q1',
        ('q2', '1'): 'q0'
    }

    dfa = DFA(states, alphabet, transition_function, start_state, accept_states)
    test_strings = ['0', '1', '01', '001', '1001', '10', '1010', '1101', '']

    print("DFA to accept strings ending with '01':\n")
    for s in test_strings:
        result = dfa.accepts(s)
        print(f"Input: '{s}' → Accepted: {result}")