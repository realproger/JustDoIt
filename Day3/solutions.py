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