# Uses python3
import sys
import math


def distance(p1, p2):
    """
	takes as input a list of x and y coordinates
	Optimal solution would be to use numpy
	"""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def check_dups(arr):
    out = []
    dups = []
    for tup in arr:
        if tup not in out:
            out.append(tup)
        elif tup in out:
            dups.append(tup)
    return dups


def minimum_distance(x, y):
    distances = []
    final = list(sorted(zip(x, y), key=lambda x: (x[0], x[1]), reverse=True))
    if check_dups(final):
        return 0.0
    for i in range(len(final)):
        distances.append(distance(final[i], final[i - 1]))
    return min(distances)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))


# import random

# x = [random.randint(0,10) for i in range(50)]
# y = [random.randint(10,20) for i in range(50)]

# print(minimum_distance(x,y))
