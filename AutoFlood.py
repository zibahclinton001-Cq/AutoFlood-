import time
import random

class AutoFloodGate:
    def __init__(self, name):
        self.name = name
        self.closed = False
        print(f"Gate installed at {name}")

    def close(self):
        if not self.closed:
            print("CLOSING GATE!")
            self.closed = True
            print("Gate closed")

    def open(self):
        if self.closed:
            print("Opening gate")
            self.closed = False
            print("Gate open")

    def check(self):
        outside = random.randint(0, 60)
        inside = random.randint(0, 10)
        print(f"\nOutside {outside}cm | Inside {inside}cm")

        if outside < 10:
            print("Safe")
            self.open()
        elif outside < 25:
            print(f"Warning {outside}cm rising")
        elif outside < 40:
            print("Danger!")
            self.close()
        else:
            print("Critical flood!")
            self.close()
            if inside > 5:
                print("Pump ON")

gate = AutoFloodGate("Borokiri 12")

for i in range(10):
    print(f"\n--- Hour {i+1} ---")
    gate.check()
    time.sleep(1)

print("\nDone - House dry")