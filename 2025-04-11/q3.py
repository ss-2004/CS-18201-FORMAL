# Q3 Write a Python-based tool to transform a regular expression into an equivalent automaton.

from collections import defaultdict
from itertools import count

EPSILON = 'ε'

class State:
    def __init__(self):
        self.transitions = defaultdict(list)


class Fragment:
    def __init__(self, start, out_states):
        self.start = start
        self.out_states = out_states


class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
        self.states = set()
        self._collect_states(start)

    def _collect_states(self, state):
        if state in self.states:
            return
        self.states.add(state)
        for targets in state.transitions.values():
            for t in targets:
                self._collect_states(t)

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for next_state in state.transitions.get(EPSILON, []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, states, symbol):
        result = set()
        for state in states:
            result.update(state.transitions.get(symbol, []))
        return result

    def accepts(self, input_string):
        current_states = self.epsilon_closure({self.start})
        for symbol in input_string:
            current_states = self.epsilon_closure(self.move(current_states, symbol))
        return self.accept in current_states


class RegexToNFA:
    def __init__(self):
        self.state_id = count()

    def new_state(self):
        return State()

    def re_to_nfa(self, regex):
        postfix = self.infix_to_postfix(regex)
        stack = []

        for token in postfix:
            if token == '*':
                frag = stack.pop()
                start = self.new_state()
                accept = self.new_state()
                start.transitions[EPSILON].extend([frag.start, accept])
                for out in frag.out_states:
                    out.transitions[EPSILON].extend([frag.start, accept])
                stack.append(Fragment(start, [accept]))
            elif token == '.':
                frag2 = stack.pop()
                frag1 = stack.pop()
                for out in frag1.out_states:
                    out.transitions[EPSILON].append(frag2.start)
                stack.append(Fragment(frag1.start, frag2.out_states))
            elif token == '|':
                frag2 = stack.pop()
                frag1 = stack.pop()
                start = self.new_state()
                accept = self.new_state()
                start.transitions[EPSILON].extend([frag1.start, frag2.start])
                for out in frag1.out_states + frag2.out_states:
                    out.transitions[EPSILON].append(accept)
                stack.append(Fragment(start, [accept]))
            else:
                start = self.new_state()
                accept = self.new_state()
                start.transitions[token].append(accept)
                stack.append(Fragment(start, [accept]))

        final_frag = stack.pop()
        return NFA(final_frag.start, final_frag.out_states[0])

    def infix_to_postfix(self, regex):
        precedence = {'*': 3, '.': 2, '|': 1}
        output = []
        stack = []

        new_regex = []
        prev = None
        for c in regex:
            if prev and (prev.isalnum() or prev == ')' or prev == '*') and (c.isalnum() or c == '('):
                new_regex.append('.')
            new_regex.append(c)
            prev = c

        for c in new_regex:
            if c.isalnum():
                output.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence[c] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(c)

        while stack:
            output.append(stack.pop())
        return output


if __name__ == "__main__":
    converter = RegexToNFA()
    regex = "(a|b)*abb"
    nfa = converter.re_to_nfa(regex)
    test_strings = ["abb", "aabb", "abababb", "ab", "bba", "", "abbbb"]

    print(f"Testing regex: {regex}\n")
    for s in test_strings:
        result = nfa.accepts(s)
        print(f"Input: '{s}' → Accepted: {result}")
