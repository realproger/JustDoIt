"""
First task
"""

array = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        array.append(str(i))

# print(','.join(array))

# Solving with using generators
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0))

# sign "*" before statement used for unpaking ;)

