"""
14th Task
"""

upper_l = 0
lower_l = 0
sentence = input("Enter your text:")
for i in sentence:
    if i.isupper():
        upper_l += 1
    elif i.islower():
        lower_l += 1
    else:
        pass

# print(f"UPPER CASE {upper_l}\nLOWER CASE {lower_l}")

"""
OTHER VARIANT
"""

word = input()
upper,lower = 0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

"""
OTHER VARIANT
"""
word = input()
upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))