from functools import reduce

def func(s1, s2):
    return s1 + s2

print(reduce(func, [1, 2, 3, 4, 5]))

