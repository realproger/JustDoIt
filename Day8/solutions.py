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