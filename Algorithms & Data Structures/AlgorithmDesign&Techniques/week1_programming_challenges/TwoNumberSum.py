# Two number sum algorithm

x = [2, 3, 5, 6, 9, 10, 6, 4, 6, 3, 5, 8]


def twoNumberSum(array, targetSum):
    out = []
    for i in range(len(array) - 1):
        num1 = array[i]
        for j in range(i + 1, len(array)):
            num2 = array[j]
            if num1 + num2 == targetSum:
                out.append(sorted([num1, num2]))
    no_dupe = []
    for ls in out:
        if ls not in no_dupe:
            no_dupe.append(ls)

    return no_dupe


print(twoNumberSum(x, 10))


def two_sum_2(arr, target):
    tups = []
    hashtab = {}
    for i in arr:
        y = target - i
        if y not in hashtab:
            hashtab.update({i: True})
        else:
            tups.append([y, i])
    return tups


print(two_sum_2(x, 10))


def simple_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


import random

nums = [random.randrange(0, 200, 1) for i in range(1, 2000)]
print(two_sum_3(x, 10))
print(simple_sort(x))
