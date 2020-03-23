# Uses python3

import sys
from functools import reduce


def max_dot_product(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    combo = list(zip(a, b))
    return reduce(lambda x, y: x + y, [a * b for a, b in combo])


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))

# a = [1,3,-5]
# b = [-2,4,1]

# print(max_dot_product(a,b))
