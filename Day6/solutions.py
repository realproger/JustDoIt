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


"""
22th Task
"""

s_text = input("Enter: ").split()
word = sorted(set(s_text))

for i in word:
    print(f"{i}:{s_text.count(i)}")

""" ANOTHER VARIANT """
ss = input().split()
dict = {}
for i in ss:
    i = dict.setdefault(i,ss.count(i))    # setdefault() function takes key & value to set it as dictionary.

dict = sorted(dict.items())               # items() function returns both key & value of dictionary as a list
                                          # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))

""" ANOTHER VARIANT """

text = input().split()
dict_co = {i:text.count(i) for i in text}
dict_co = sorted(dict_co.items())

for i in dict_co:
    print(f"{i[0]} : {i[1]}")


"""
23th Task
"""

num = int(input("Enter your num: "))
print(num**2)


"""
24th Task
"""

print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)