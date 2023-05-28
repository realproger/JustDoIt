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
