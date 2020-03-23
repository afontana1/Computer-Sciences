# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def efficient_pairwise(numbers):
    idx = 0
    for i in range(0, len(numbers)):
        if numbers[i] > numbers[idx]:
            idx = i
    print(numbers[idx])

    if idx == 0:
        idx2 = 1
    else:
        idx2 = 0
    for i in range(0, len(numbers)):
        if (numbers[i] != numbers[idx]) and (numbers[i] > numbers[idx2]):
            idx2 = i
    return numbers[idx] * numbers[idx2]


def pairwise(numbers):
    first = max(numbers)
    numbers.pop(numbers.index(first))
    second = max(numbers)
    return first * second


def best_implementation(numbers):
    new = sorted(numbers)
    return new[len(new) - 1] * new[len(new) - 2]


import random


def test(n):
    for i in range(0, n):
        numbers = [random.randint(0, 100) for i in range(0, 100)]
        first_prod = max_pairwise_product(numbers)
        second_prod = pairwise(numbers)
        if first_prod != second_prod:
            print("not the same {} and {}".format(first_prod, second_prod))
        else:
            print(first_prod, second_prod)


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(best_implementation(input_numbers))
