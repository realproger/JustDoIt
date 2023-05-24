x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)

"""
OTHER VARIANT
"""
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)

"""
8th Task
"""
cs_words = input("Words: ").split(',')
cs_words.sort()
print(','.join(cs_words))


"""
9th Task
"""

text = []
while True:
    lines = input("Sentence: ")
    if len(lines) == 0:
        break
    text.append(lines.upper())

for each in text:
    print(each)

"""
10th Task
"""

duplicated_wrods = input("Enter: ").split(' ')
duplicated_wrods.sort()
clean_w = []
for each in duplicated_wrods:
    if each not in clean_w:
        clean_w.append(each)
print(' '.join(clean_w))

"""
OTHER VARIANT
"""
word = sorted(list(set(input().split())))   #  input string splits -> converting into set() to store unique
                                            #  element -> converting into list to be able to apply sort
print(" ".join(word))

"""
11 Task
"""

def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))

"""
OTHER VARIANT
"""

data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))    # lambda is an operator that helps to write function of one line
print(",".join(data))


"""
12th Task
"""

lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))

"""
OTHER VARIANT
"""
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))

"""
13th Task
"""

def letter_digit_counter():
    digits = 0
    letters = 0
    text = input("Your message: ")
    for i in text:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
        else:
            pass
    print(f"LETTERS - {letters}\nDIGITS - {digits}")


letter_digit_counter()

"""
OTHER VARIANT
"""
word = input()
letter, digits = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digits += 1
print(f"LETTERS {letter}\n{digits}") # two different types of formating method is shown in both solution