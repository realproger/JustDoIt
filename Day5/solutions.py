"""
18th Task
"""
def is_lower(x):
    for i in x:
        if 'a' <= i and i <= 'z':
            return True
    return False
    
def is_upper(x):
    for i in x:
        if 'A' <= i and i <= 'Z':
            return True
    return False

def is_numeric(x):
    for i in x:
        if '0' <= i and i <= '9':
            return True
    return False

def symbols(x):
    for i in x:
        if i == '$' or i == '@' or i == '#':
            return True
    return False

def check_password():
    password = input("Enter your password: ").split(',')
    lst = []

    for i in password:
        length = len(i)
        if 6 <= length and length <= 12 and is_lower(i) and is_upper(i) and is_numeric(i) and symbols(i):
            lst.append(i)
    return ','.join(lst)

# print(check_password())

""" WITH USING REGULAR EXPRESSIONS """
import  re

s = input().split(',')
lst = []

for i in s:
    cnt = 0
    cnt+=(6<=len(i) and len(i)<=12)
    cnt+=bool(re.search("[a-z]",i))      # here re module includes a function re.search() which returns the object information
    cnt+=bool(re.search("[A-Z]",i))      # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt+=bool(re.search("[0-9]",i))      # if not a single match found then returns NONE which converts to False in boolean
    cnt+=bool(re.search("[@#$]",i))      # expression otherwise True if found any.
    if cnt == 5:
        lst.append(i)

print(",".join(lst))

"""
19th Task
"""

journal = []
while True:
    sorting_j = input("Name-Age-Score: ").split(',')
    if not sorting_j[0]:
        break
    journal.append(tuple(sorting_j))

journal.sort(key = lambda x: (x[0], int(x[1]), int(x[2])))
print(journal)

