"""
First task
"""

array = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        array.append(str(i))

# print(','.join(array))

# Solving with using generators
# print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0))

# sign "*" before statement used for unpaking ;)


"""
Second task
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return factorial(x - 1) * x

print(factorial(8))

###
##
"""
The uprising function itself with the argument x - 1 and multiplies the result by x. 
This happens until x becomes the necessary 0, 
and eventually the factor of the original number x is returned
"""
##
###

# Same program/ solution with using while loop
num = int(input("Enter your number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i;
    i = i + 1
# print(fact)