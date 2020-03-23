# Uses python3
import sys
import numpy as np
import math
from functools import reduce

M = [[1, 1], [1, 0]]


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def mat_mul(A, B):
    """multiply two matricies"""
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])

    if (rowsA == rowsB) and (colsA == colsB):

        result = [[0 for i in range(len(A))] for j in range(len(A))]

        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(A)):
                    result[i][j] += A[i][k] * B[k][j]

    return result


def powerTwo(n):
    return (n != 0) & ((n & (n - 1)) == 0)


def matrix_inputs(n):
    """Take matrix to n power in log time"""
    """represent n as powers of 2"""
    return [i for i in range(n) if powerTwo(i) and i % 2 == 0]


def identity_(A):
    """returns the identity matrix"""
    identity_mat = [[(i == j) * 1 for i in range(len(A))] for j in range(len(A))]
    return identity_mat


def matrix_power(A, n):
    """take matrix A to the power n"""
    identity = identity_(A)

    for i in range(n):
        identity = mat_mul(identity, A)

    return identity


def matrix_exp(A, n):
    if not n:
        return identity_(A)
    elif n % 2:
        return mat_mul(A, matrix_exp(A, n - 1))
    else:
        sq = matrix_exp(A, n // 2)
        return mat_mul(sq, sq)


def fib_exponential(n):
    """the nth fib is the same as matrix to n power"""
    eig = [[1, 1], [1, 0]]
    start = [1, 0]
    final = [1, 0]

    mat_power = matrix_exp(eig, n)
    for i in range(len(mat_power)):
        for j in range(len(start)):
            final[i] += mat_power[i][j] * start[j]

    return final[1] % 10


def fib_exp_non_recursive(A, n):
    """non recursive solution to the above"""
    init = [1, 0]
    out = [A]
    final = [0, 0]
    for power in matrix_inputs(n):
        if power != 2:
            out.append(matrix_power(A, power))
    # multiply all of the matricies together
    mat_power = reduce(lambda x, y: mat_mul(x, y), out)
    # multiply by the initial conditions
    for i in range(len(mat_power)):
        for j in range(len(init)):
            final[i] += mat_power[i][j] * init[j]
    return final[1] % 10


# print(fib_exponential(133))
# print(fib_exp_non_recursive(M,133))
# print(get_fibonacci_last_digit_naive(133))

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(fib_exponential(n))
