# Uses python3
import sys


def get_change(n):
    """break number down into smallest combination of 1,5,10"""
    if n < 0:
        return n
    if n % 10 == 0:
        return n // 10
    elif n % 10 >= 5:
        if n % 10 == 5:
            return n // 10 + 1
        else:
            pennies = 0
            running_sum = (n // 10) * 10 + 5
            for i in range(0, (n - running_sum)):
                pennies += 1
            return pennies + n // 10 + 1
    else:
        if n % 10 < 5:
            pennies = 0
            running_sum = (n // 10) * 10
            for i in range(0, (n - running_sum)):
                pennies += 1
            return pennies + n // 10


def coins(n):
    if n % 10 == 0:
        return n // 10
    else:
        count = 0
        total = 0
        check = True
        while check:
            if n - total > 10:
                total += 10
                count += 1
            else:
                if n - total == 5:
                    return count + 1
                else:
                    if n - total > 5:
                        total += 5
                        count += 1
                        for i in range(n - total):
                            total += 1
                            count += 1
                        return count
                    if n - total < 5:
                        for i in range(n - total):
                            total += 1
                            count += 1
                        return count

        return count


def get_coins(n):
    denominations = [10, 5, 1]
    total = []
    for coin in denominations:
        while n >= coin:
            n -= coin
            total.append(coin)
    return len(total)


def recurse_coin(n, count=0):
    if n == 0:
        return count
    elif n > 0:
        count += 1
        if n >= 10:
            return recurse_coin(n - 10, count)
        if n < 10 and n >= 5:
            return recurse_coin(n - 5, count)
        if n < 5:
            return recurse_coin(n - 1, count)


def recurse_coin_two(n):
    if n == 0:
        return n
    elif n > 0:
        if n >= 10:
            return 1 + recurse_coin(n - 10)
        if n < 10 and n >= 5:
            return 1 + recurse_coin(n - 5)
        if n < 5:
            return 1 + recurse_coin(n - 1)


# import random
# for i in [random.randint(0,5000000) for i in range(50000)]:
# 	assert coins(i) == get_change(i)

if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_coins(m))
