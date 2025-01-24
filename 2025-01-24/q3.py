# 3. Implement a Python program to verify Linear Temporal Logic (LTL) formulas against a simple
# finite-state machine (FSM).

import networkx as nx

class Formula:
    def __init__(self, formula_str):
        self.formula_str = formula_str
        self.operands = []
        self.parse_formula(formula_str)

    def parse_formula(self, formula_str):
        # Simple parsing logic for demonstration purposes
        if "&&" in formula_str:
            self.operands = formula_str.split("&&")
            self.type = "AND"
        elif "||" in formula_str:
            self.operands = formula_str.split("||")
            self.type = "OR"
        elif "!" in formula_str:
            self.operands = [formula_str[1:]]
            self.type = "NOT"
        elif "X" in formula_str:
            self.operands = [formula_str[1:]]
            self.type = "NEXT"
        elif "U" in formula_str:
            self.operands = formula_str.split("U")
            self.type = "UNTIL"
        else:
            self.type = "LITERAL"
            self.value = formula_str.strip()

    def is_literal(self):
        return self.type == "LITERAL"

    def is_and(self):
        return self.type == "AND"

    def is_or(self):
        return self.type == "OR"

    def is_not(self):
        return self.type == "NOT"

    def is_next(self):
        return self.type == "NEXT"

    def is_until(self):
        return self.type == "UNTIL"

class FSM:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.initial_state = None

    def add_state(self, state, is_initial=False):
        self.graph.add_node(state)
        if is_initial:
            self.initial_state = state

    def add_transition(self, from_state, to_state, label):
        self.graph.add_edge(from_state, to_state, label=label)

    def get_transitions(self, state):
        return self.graph.out_edges(state, data=True)

def check_ltl_formula(fsm, formula):
    for state in fsm.graph.nodes:
        if not check_state(fsm, state, formula):
            return False
    return True

def check_state(fsm, state, formula):
    if formula.is_literal():
        return formula.value in fsm.graph.nodes[state]  # Check for the literal in node data
    elif formula.is_and():
        return check_state(fsm, state, Formula(formula.operands[0])) and check_state(fsm, state,
                                                                                     Formula(formula.operands[1]))
    elif formula.is_or():
        return check_state(fsm, state, Formula(formula.operands[0])) or check_state(fsm, state,
                                                                                    Formula(formula.operands[1]))
    elif formula.is_not():
        return not check_state(fsm, state, Formula(formula.operands[0]))
    elif formula.is_next():
        for _, next_state, data in fsm.get_transitions(state):
            if check_state(fsm, next_state, Formula(formula.operands[0])):
                return True
        return False
    elif formula.is_until():
        for _, next_state, data in fsm.get_transitions(state):
            if check_state(fsm, next_state, Formula(formula.operands[1])):
                return True
            if check_state(fsm, next_state, Formula(formula.operands[0])) and check_state(fsm, next_state, formula):
                return True
        return False
    return False

fsm = FSM()
fsm.add_state("S0", is_initial=True)
fsm.add_state("S1")
fsm.add_state("S2")
fsm.add_transition("S0", "S1", "a")
fsm.add_transition("S1", "S2", "b")
fsm.add_transition("S2", "S0", "c")

fsm.graph.nodes["S0"]["a"] = True
fsm.graph.nodes["S0"]["b"] = True

ltl_formula_nl = "a && b"
ltl_formula = Formula(ltl_formula_nl)

if check_ltl_formula(fsm, ltl_formula):
    print("The FSM satisfies the LTL formula.")
else:
    print("The FSM does not satisfy the LTL formula.")
