# 2. Develop a Python program that defines two CCS processes, P and Q, executing actions a and b.
# Apply relabeling (a → b) and restriction (\{a}) to synchronize their execution. Verify whether they
# remain equivalent under strong bisimulation.

class Process:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def relabel(self, old_action, new_action):
        if self.action == old_action:
            self.action = new_action

    def restrict(self, restricted_actions):
        if self.action in restricted_actions:
            self.action = None

def strong_bisimulation(p1, p2):
    return p1.action == p2.action

P = Process("P", "a")
Q = Process("Q", "b")

P.relabel("a", "b")

P.restrict({"a"})
Q.restrict({"a"})

is_equivalent = strong_bisimulation(P, Q)

print(f"Process P: {P.action}")
print(f"Process Q: {Q.action}")
print(f"Are processes P and Q equivalent under strong bisimulation? {is_equivalent}")
