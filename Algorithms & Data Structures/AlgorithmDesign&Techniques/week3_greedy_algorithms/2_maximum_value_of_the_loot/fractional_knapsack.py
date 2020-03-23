# Uses python3
import sys


def get_optimal_value(max_cap, weights, values):
    val_per_unit = sorted(
        [val for val in zip(values, weights, [i / j for i, j in zip(values, weights)])],
        key=lambda tup: tup[2],
        reverse=True,
    )
    final = 0
    for i, j in enumerate(val_per_unit):
        if max_cap == 0:
            return 0
        a = min(max_cap, val_per_unit[i][1])
        final += a * val_per_unit[i][2]
        max_cap -= a

    return final


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
