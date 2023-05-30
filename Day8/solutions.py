"""
31th Task
"""

def createDict():
    new_dict = {}
    for i in range(1, 21):
        new_dict.setdefault(i, i**2)
    return new_dict

print(createDict())

""" DICT COMPREHENSION """
def createDict():
    new_dict = {i:i**2 for i in range(1, 21)}
    print(new_dict)

createDict()

"""
32nd Task
"""

def getKeysDict():
    new_dict = {i:i**2 for i in range(1, 21)}
    # for key, value in new_dict.items():
    #     print(key)
    print(new_dict.keys())
getKeysDict()

"""
33rd Task
"""

def printList():
    new_list = []
    for i in range(1, 21):
        new_list.append(i**2)
    print(new_list)

printList()

"""LIST COMPREHENSION """

def printList():
    new_list = [i**2 for i in range(1, 21)]
    print(new_list)

printList()

"""
34th Task
"""

def getListItem():
    new_list = [i**2 for i in range(1, 21)]
    # for i in range(5):
    #     print(new_list[i])
    print(new_list[0:5])

getListItem()