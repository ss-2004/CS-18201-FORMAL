# Simulate a basic CCS process in Python where one process performs an action (a) and
# transitions to the next state.
class CCSProcess:
    def __init__(self, name):
        self.name = name
        self.state = "Start"

    def transition(self, action):
        print(f"Process {self.name} performs action: {action}")
        self.state = "NextState"

    def current_state(self):
        return self.state

process = CCSProcess("P")
process.transition("a")
print(f"New state: {process.current_state()}")
