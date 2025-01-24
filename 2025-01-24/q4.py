# 4. Create a Python program to simulate a reactive system for a traffic light controller with three lights:
#     RED, YELLOW, and GREEN.

import time

class TrafficLight:
    def __init__(self):
        self.state = "RED"

    def transition(self):
        if self.state == "RED":
            self.state = "GREEN"
        elif self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"

    def run(self, cycles=5):
        for _ in range(cycles):
            print(f"Light is {self.state}")
            if self.state == "RED":
                time.sleep(5)
            elif self.state == "GREEN":
                time.sleep(5)
            elif self.state == "YELLOW":
                time.sleep(2)
            self.transition()

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()
