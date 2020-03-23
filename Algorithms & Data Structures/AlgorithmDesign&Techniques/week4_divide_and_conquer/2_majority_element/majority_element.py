# Uses python3
import sys


def get_majority_element_(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    distinct = set(a)
    for num in distinct:
        check = functional_remove(a, num)
        if len(check) > len(a) // 2:
            return num
    return -1


def remove(arr, value):
    check = 0
    stopping_condition = len(arr) // 2
    while arr.count(value) > 0:
        arr.remove(value)
        check += 1
        if check > stopping_condition:
            # we know for a fact there is a majority element
            return value
    return arr


def functional_remove(arr, value):
    temp = list(filter(lambda x: x != value, arr))
    check = list(filter(lambda x: x == value, arr))
    return check


def get_majority_element(arr, left, right):
    first = 0
    count = 1
    for i in range(len(arr)):
        if arr[first] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            first = i
            count = 1
    if arr.count(arr[first]) > len(arr) // 2:
        return arr[first]
    else:
        return -1


def max_element_hash(arr):
    out = {}
    for i in range(len(arr)):
        if arr[i] in out:
            out[arr[i]] += 1
        else:
            out[arr[i]] = 1
    for k in out.keys():
        if out[k] > len(arr) // 2:
            return k
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# x = [1,2,3,6,6,6,6,6,6,6,6,6,6,6,4,5,5,5,5,5,5]
# y = [1,2,3,4]

# print(max_element_hash(x))
