x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

# print(lst)

"""
OTHER VARIANT
"""
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)