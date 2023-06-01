""" 36th Task """

def printList():
    new_list = [i ** 2 for i in range(1, 21)]
    # print(new_list)

    # print(new_list[5:])       # variant
    
    for i in range(5, 20):
        print(new_list[i])
printList()