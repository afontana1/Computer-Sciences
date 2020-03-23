# python3
import sys


def any_(iterable):
    """
	takes in iterable of boolean conditions
	if i means if True (there exists an element satisfying that condition)
	if theyre all False, return False (not one element satisfies the condition)
	"""
    for i in iterable:
        if i:
            return True
    return False


def all_(iterable):
    """
	takes in iterable of boolean conditions
	all boolean values must evaluate to True
	if they do not, then "if not" will evaluate to True
	and False will be returned because there is atleast one element
	in the iterable not satisfying the condition
	"""
    for i in iterable:
        if not i:
            return False
    return True


def compute_min_refills(distance, tank, stops):
    stops.insert(0, 0)
    stops.append(distance)
    if distance < tank:
        return 0
    differences = [stops[i + 1] - stops[i] for i in range(len(stops) - 1)]
    if any(i > tank for i in differences):
        return -1
    accum = 0
    count = 0
    for i in range(len(differences) - 1):
        accum = accum + differences[i]
        if accum >= tank:
            count += 1
            accum = 0
        if (accum + differences[i + 1]) > tank:
            count += 1
            accum = 0
    return count


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

# distance = 500
# tank = 200
# stops = [100,200,300,400]

# print(compute_min_refills(distance,tank,stops))
