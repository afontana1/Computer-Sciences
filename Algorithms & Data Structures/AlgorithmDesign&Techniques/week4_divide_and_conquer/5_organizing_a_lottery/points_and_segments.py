# Uses python3
import sys
import random
from itertools import chain


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_tuple = list(zip(starts, ["l"] * len(starts), range(len(starts))))
    end_tuple = list(zip(ends, ["r"] * len(ends), range(len(ends))))
    point_tuple = list(zip(points, ["p"] * len(points), range(len(points))))
    result = chain(start_tuple, end_tuple, point_tuple)
    result = sorted(result, key=lambda a: (a[0], a[1]))

    count = 0
    for num, letter, index in result:
        if letter == "l":
            count += 1
        elif letter == "r":
            count -= 1
        else:
            cnt[index] = count
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")


# points = [random.randint(1, 20) for i in range(50)]

# starts = [random.randint(0, 40) for i in range(50)]

# ends = [random.randint(40, 80) for i in range(50)]


# print(fast_count_segments(starts,ends,points))

# print(naive_count_segments(starts,ends,points))
