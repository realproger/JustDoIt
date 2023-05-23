"""
Task 4th
"""
# numbers = input("Numbers: ").split(',')
# print(numbers)

"""
the input is being taken as string and as it is string it has a built in
method name split. ',' inside split function does split where it finds any ','
and save the input as list in lst variable
"""


# tuple method converts list to tuple
# tupled_n = tuple(numbers)
# print(tupled_n)

"""
Task 5th
"""

class InputOutString:

    def getString(self):
        self.our_string = input("Enter your message: ")
    
    def printString(self):
        print(self.our_string.upper())

# object1 = InputOutString()
# object1.getString()
# object1.printString()


"""
Task 6th
"""

from math import sqrt # import specific functions as importing all using *
                      # is bad practice

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input().split(',')] # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

# print(",".join(D))

'''    OR    '''

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))