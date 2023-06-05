""" 41th Task """

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_nums = list(map(lambda x: x ** 2, given_list))
print(squared_nums)

""" 42nd Task """

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, given_list)))
print(squared_even_nums)

def even(num):
    return num % 2 == 0
def squared(num):
    return num ** 2

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squared,filter(even,given_list))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))

""" 43rd Task """

result = filter(lambda x: x % 2 == 0, range(1, 21))
print(list(result))

def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))

""" 44th Task """

def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)

"""45th Task """

class American:
    @staticmethod
    def printNationality():
        print("I am American")

american = American()

american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()