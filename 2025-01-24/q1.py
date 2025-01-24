# 1. Write a Python program to implement a simple state transition system.

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol, None)


class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def transition(self, input_symbol):
        next_state = self.current_state.get_next_state(input_symbol)
        if next_state:
            print(f"Transitioning from {self.current_state.name} to {next_state.name} on input '{input_symbol}'")
            self.current_state = next_state
        else:
            print(f"No transition from {self.current_state.name} on input '{input_symbol}'")

state_a = State("A")
state_b = State("B")
state_c = State("C")

state_a.add_transition('0', state_b)
state_a.add_transition('1', state_c)
state_b.add_transition('0', state_a)
state_b.add_transition('1', state_c)
state_c.add_transition('0', state_a)
state_c.add_transition('1', state_b)

fsm = StateMachine(state_a)

inputs = ['0', '1', '1', '0', '1']
for input_symbol in inputs:
    fsm.transition(input_symbol)
