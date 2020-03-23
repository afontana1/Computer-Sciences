# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def list_fib(n):
    """Calculate Nth fib number.
	Args:
		n: Non-negative integer
	Output:
		The nth fib number.
	"""
    if n <= 1:
        return n

    store = [0] * (n + 1)
    store[0] = 0
    store[1] = 1
    for i in range(2, n + 1):
        store[i] = store[i - 1] + store[i - 2]
    return store[-1]


n = int(input())
print(list_fib(n))
