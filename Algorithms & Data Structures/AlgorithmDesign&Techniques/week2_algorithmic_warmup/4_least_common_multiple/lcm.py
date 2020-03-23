# Uses python3
from __future__ import division
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    small, large = min(a, b), max(a, b)
    i = large
    proceed = True
    while proceed:
        if i % small == 0:
            return i
        else:
            i += large


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
