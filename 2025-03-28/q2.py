# Q2 Implement a basic workflow system (e.g., an order processing system) using Petri Nets and
# analyze its correctness.

class PetriNet:
    def __init__(self):
        self.places = {"order_received": 1, "processing": 0, "shipped": 0, "delivered": 0}
        self.transitions = {
            "start_processing": {"input": "order_received", "output": "processing"},
            "ship_order": {"input": "processing", "output": "shipped"},
            "deliver_order": {"input": "shipped", "output": "delivered"}
        }

    def fire_transition(self, transition_name):
        if transition_name in self.transitions:
            transition = self.transitions[transition_name]
            input_place = transition["input"]
            output_place = transition["output"]

            if self.places[input_place] > 0:
                self.places[input_place] -= 1
                self.places[output_place] += 1
                print(f"Transition '{transition_name}' fired: {input_place} → {output_place}")
            else:
                print(f"Cannot fire '{transition_name}': No tokens in {input_place}")
        else:
            print(f"Transition '{transition_name}' not found.")

    def is_reachable(self, target_state):
        return all(self.places[p] == target_state[p] for p in self.places)

    def print_state(self):
        print("Current Marking:", self.places)


net = PetriNet()
net.print_state()
net.fire_transition("start_processing")
net.print_state()
net.fire_transition("ship_order")
net.print_state()
net.fire_transition("deliver_order")
net.print_state()

final_state = {"order_received": 0, "processing": 0, "shipped": 0, "delivered": 1}
if net.is_reachable(final_state):
    print("Workflow successfully completed!")
else:
    print("Workflow did not reach final state.")
