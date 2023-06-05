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