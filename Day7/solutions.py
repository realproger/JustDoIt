"""
26th Task
"""

def sum_func(param_1, param_2):
    return param_1 + param_2
print(sum_func(22, 22))

get_sum = lambda param_1, param_2: param_1 + param_2
print(get_sum(12, 12))

"""
27th Task
"""

def int_to_str(param_1):
    return str(param_1)
print(int_to_str(1239))

convert_func = lambda param: str(param)
number = convert_func(12312)
print(number, type(number))

"""
28th Task
"""

def get_strs_sum(param_1, param_2):
    return int(param_1) + int(param_2)
print(get_strs_sum(331, 1212))

converting = lambda param_1, param_2: int(param_1) + int(param_2)
print(converting(212, 123))


"""
29th Task
"""

def str_concatenating(param_1, param_2):
    if isinstance(param_1, str) and isinstance(param_2, str):
        return param_1 + param_2
    else:
        raise TypeError("You must pass a string data type parameter to the function")

print(str_concatenating("23", " years old"))

str_concat = lambda str1, str2: str1+str2
print(str_concat("asd", "asd"))

"""
30th Task
"""

def get_maxLen(param_1, param_2):
    param_1_len = len(param_1)
    param_2_len = len(param_2)
    if param_1_len > param_2_len:
        print(param_1)
    elif param_1_len < param_2_len:
        print(param_2)
    else:
        print(f"{param_1}\n{param_2}")
