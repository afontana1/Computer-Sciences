# Uses python3
import sys


def binary_recursive(arr, x):
    left, right = 0, len(arr) - 1
    if len(arr) == 1 and arr[0] != x:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return arr[mid]
    elif arr[mid] < x:
        return binary_recursive(arr[mid + 1 :], x)
    elif arr[mid] > x:
        return binary_recursive(arr[:mid], x)
    else:
        return -1


def binary_iterative(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            return mid
        elif item < item_list[mid]:
            last = mid - 1
        elif item > item_list[mid]:
            first = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


# if __name__ == "__main__":
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[n + 1]
#     a = data[1 : n + 1]
#     for x in data[n + 2 :]:
#         # replace with the call to binary_search when implemented
#         print(binary_iterative(a, x), end=" ")


arr = [2,3,1]
srt = sorted(arr)
print(srt)
print(binary_iterative(srt,15))
