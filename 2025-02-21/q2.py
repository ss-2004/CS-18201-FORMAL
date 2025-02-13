# 2. Develop a Python program that models a system of three CCS processes executing actions in
# parallel, ensuring synchronization where required. Introduce relabeling and restriction to study
# their impact on process behavior.

class CCSProcess:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions

    def relabel(self, relabel_map):
        self.actions = {relabel_map.get(action, action) for action in self.actions}

    def restrict(self, restricted_actions):
        self.actions -= restricted_actions

    def synchronize(self, other):
        common_actions = self.actions & other.actions
        return CCSProcess(f"{self.name}|{other.name}", common_actions)

    def __repr__(self):
        return f"{self.name}: {self.actions}"

P1 = CCSProcess("P1", {"a", "b", "c"})
P2 = CCSProcess("P2", {"b", "c", "d"})
P3 = CCSProcess("P3", {"c", "d", "e"})

relabel_map = {"a": "x", "d": "y"}
P1.relabel(relabel_map)
P2.relabel(relabel_map)
P3.relabel(relabel_map)

restricted_actions = {"c"}
P1.restrict(restricted_actions)
P2.restrict(restricted_actions)
P3.restrict(restricted_actions)

P1_P2 = P1.synchronize(P2)
P1_P2_P3 = P1_P2.synchronize(P3)

print("After Relabeling and Restriction:")
print(P1)
print(P2)
print(P3)
print("\nSynchronization Result:")
print(P1_P2_P3)
