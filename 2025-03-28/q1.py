# Q1 Model a synchronization problem using Petri Nets and verify deadlock freedom.

class PetriNet:
    def __init__(self):
        self.places = {
            "P1_waiting": 1,
            "P2_waiting": 1,
            "Resource_free": 1,
            "P1_in_CS": 0,
            "P2_in_CS": 0,
        }

        self.transitions = {
            "P1_enters": {"inputs": ["P1_waiting", "Resource_free"], "outputs": ["P1_in_CS"]},
            "P1_exits": {"inputs": ["P1_in_CS"], "outputs": ["Resource_free", "P1_waiting"]},
            "P2_enters": {"inputs": ["P2_waiting", "Resource_free"], "outputs": ["P2_in_CS"]},
            "P2_exits": {"inputs": ["P2_in_CS"], "outputs": ["Resource_free", "P2_waiting"]},
        }

    def can_fire(self, transition):
        for place in self.transitions[transition]["inputs"]:
            if self.places[place] == 0:
                return False
        return True

    def fire(self, transition):
        if not self.can_fire(transition):
            print(f"Transition {transition} cannot fire.")
            return False

        for place in self.transitions[transition]["inputs"]:
            self.places[place] -= 1

        for place in self.transitions[transition]["outputs"]:
            self.places[place] += 1

        print(f"Fired transition: {transition}")
        return True

    def is_deadlock(self):
        return not any(self.can_fire(t) for t in self.transitions)

    def display_state(self):
        print("Current State:", self.places)


pn = PetriNet()
pn.display_state()
transitions = ["P1_enters", "P1_exits", "P2_enters", "P2_exits"]

for _ in range(5):
    for t in transitions:
        if pn.fire(t):
            pn.display_state()

    if pn.is_deadlock():
        print("Deadlock detected!")
        break
else:
    print("No deadlock, system is safe.")
