# Uses python3

import sys
from functools import reduce
from itertools import permutations


def largest_number_(num):
    if any(int(num) > 9 for num in num):
        num = list(map(int, "".join([str(i) for i in num])))
    out = ""
    while num:
        tempmax = max(num)
        out += str(tempmax)
        num.pop(num.index(tempmax))
    return out


inp = ["4", "5", "23", "67", "45", "32", "31", "3", "86", "8"]


def groups(data):
    out = {}
    for num in data:
        if num[0] in out:
            out[num[0]].append(num)
        else:
            out[num[0]] = []
            out[num[0]].append(num)
    return out


def get_biggest(nums):
    return max([reduce(lambda x, y: x + y, combo) for combo in permutations(nums)])


def largest_number(a):
    val = ""
    group = groups(a)
    for nums in sorted(group.values(), reverse=True):
        val += get_biggest(nums)
    return val


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))

import random

x = [str(random.randint(0, 100)) for i in range(50)]
print(largest_number(x))

## DOESNT PASS TIME LIMIT
