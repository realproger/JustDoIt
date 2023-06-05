""" 36th Task """

def printList():
    new_list = [i ** 2 for i in range(1, 21)]
    # print(new_list)

    # print(new_list[5:])       # variant

    for i in range(5, 20):
        print(new_list[i])
# printList()

""" 37th Task """

def printTuple():
    nList = [i ** 2 for i in range(1, 21)]
    nTuple = tuple(nList)
    print(nTuple)
printList()

""" 38th Task """

# tp = (1,2,3,4,5,6,7,8,9,10)
# print(f"{tp[:5]}\n{tp[5:]}")

tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')