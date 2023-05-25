# """
# 14th Task
# """

# upper_l = 0
# lower_l = 0
# sentence = input("Enter your text:")
# for i in sentence:
#     if i.isupper():
#         upper_l += 1
#     elif i.islower():
#         lower_l += 1
#     else:
#         pass

# # print(f"UPPER CASE {upper_l}\nLOWER CASE {lower_l}")

# """
# OTHER VARIANT
# """

# word = input()
# upper,lower = 0,0

# for i in word:
#         lower+=i.islower()
#         upper+=i.isupper()

# # print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

# """
# OTHER VARIANT
# """
# word = input()
# upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
# lower = sum(1 for i in word if i.islower())

# print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))


# """
# 15th Task
# """
# a = input()
# total,tmp = 0,str()        # initialing an integer and empty string

# for i in range(4):
#     tmp+=a               # concatenating 'a' to 'tmp'
#     total+=int(tmp)      # converting string type to integer type

# print(total)

# """
# OTHER VARIANT
# """

# a = input()
# total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
# print(total)


"""
16th Task
"""

numbers = input("Enter: ").split(',')
odd_numbers = []
for i in numbers:
    if int(i) % 2 != 0:
        odd_numbers.append(str(int(i) ** 2))
print(','.join(odd_numbers))

"""
LIST COMPREHENSION
"""
odd_numbers = [str(int(i) ** 2) for i in numbers if int(i) % 2 != 0]
print(','.join(odd_numbers))


"""
17th Task
"""

total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)
