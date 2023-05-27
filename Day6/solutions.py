"""
21th Task
"""

import math

x, y = 0, 0
while True:
    steps = input(": ").split()
    if not steps:
        break
    if steps[0] == "UP":            # s[0] indicates command
        x -= int(steps[1])          # s[1] indicates unit of move
    if steps[0] == "DOWN":
        x += int(steps[1])
    if steps[0] == "LEFT":
        y -= int(steps[1])
    if steps[0] == "RIGHT":
        y += int(steps[1])
                            # N**P means N^P
distance = round(math.sqrt(x**2 + y**2))       # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(distance)
