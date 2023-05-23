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

object1 = InputOutString()
object1.getString()
object1.printString()