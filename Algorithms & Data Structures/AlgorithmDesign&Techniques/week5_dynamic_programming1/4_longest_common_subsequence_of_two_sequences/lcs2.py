# Uses python3
# http://www.cs.cmu.edu/afs/cs/academic/class/15451-s15/LectureNotes/lecture04.pdf
# http://web.mit.edu/15.053/www/AMP-Chapter-11.pdf
# https://rosettacode.org/wiki/Longest_common_subsequence#Dynamic_Programming_8

import sys


def lcs2(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
 
    # read a substring from the matrix
    result = ''
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]
 
    return result

x = 'abcd'
y = 'abbc'

print(lcs2(x,y))

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))

#     n = data[0]
#     data = data[1:]
#     a = data[:n]

#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]

#     print(lcs2(a, b))
