# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return list(reversed(sequence))


def optimal_sequence_(n):
    v = [0] * (n + 1)  # so that v[n] is there
    v[1] = 1  # length of the sequence to 1 is 1
    for i in range(1, n + 1):
        v[i] = v[i - 1] + 1
        if i % 2 == 0:
            v[i] = min(1 + v[i // 2], v[i])
        if i % 3 == 0:
            v[i] = min(1 + v[i // 3], v[i])

    sequence = []
    i = n
    while i > 1:
        sequence.append(i)
        if v[i - 1] == v[i] - 1:
            i -= 1
        elif i % 2 == 0 and (v[i // 2] == v[i] - 1):
            i = i // 2
        elif i % 3 == 0 and (v[i // 3] == v[i] - 1):
            i = i // 3

    sequence.append(1)

    return list(reversed(sequence))


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
