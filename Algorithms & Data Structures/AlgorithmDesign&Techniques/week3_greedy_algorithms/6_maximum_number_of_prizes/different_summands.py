# Uses python3
import sys
from itertools import compress, product


def optimal_summands_(n):
    def combinations(items, n):
        """
		Create all combinations given a range of numbers, no repeat digits
		return those that sum to the target

		:product will return lists of len(n) of zeros and ones
		:compress takes each mask, and filters the initial range object
		:Works similar to filter

		example for compress:
		items = [A,B,C]
		mask = [1,0,1] 
		compress(items,mask) = [A,C] 
		"""
        return (
            set(compress(items, mask))
            for mask in product(*[[0, 1]] * len(items))
            if sum(set(compress(items, mask))) == n
        )

    combos = sorted(
        [i for i in combinations(range(1, n + 1), n)],
        key=lambda x: len(x),
        reverse=True,
    )

    return list(combos[0])


def optimal_summands(n):
    summands = []
    m = 1
    while n > 2 * m:
        print("m = {}".format(m))
        summands.append(m)
        n -= m
        m += 1
        print("n = {}".format(n))
    else:
        summands.append(n)
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")

###Naive Solutions Fails the time constraints

print(optimal_summands(7))
