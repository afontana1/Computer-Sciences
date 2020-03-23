# Uses python3
import sys

denominations = [1,3,4]
def get_change_recursive(m,coins):
	if m == 0:
		return 0
	min_coins = m*10
	for i in range(len(coins)):
		if m >= coins[i]:
			numCoins = get_change_recursive(m-coins[i],coins)
			if numCoins + 1 < min_coins:
				min_coins = numCoins + 1
	return min_coins


def get_change(total):
	coins_list = [1,3,4]
	s = [0]
	for i in range(1, total+1):
		s.append(-1)
		for coin_val in coins_list:
			if i-coin_val >=0 and s[i-coin_val] != -1 and (s[i] > s[i-coin_val] or s[i] == -1):
				s[i] = 1 + s[i-coin_val]
	return s[total]

if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
