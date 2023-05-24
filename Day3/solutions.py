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