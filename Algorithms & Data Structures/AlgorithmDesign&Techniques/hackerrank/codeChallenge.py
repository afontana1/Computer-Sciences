import requests
import math
from functools import reduce
import csv

def calculateFuel(mass, tot = 0):
	if mass == 0 or mass < 0:
		return tot
	temp = math.floor(mass/3) - 2
	if temp < 0:
		tot+=0
	else:
		tot+=temp
	return calculateFuel(temp,tot)

def iterativeFuel(mass):
	tot = 0
	while True:
		temp = math.floor(mass/3) - 2
		if temp < 0:
			break
		tot+= temp
		mass = temp
	return tot

def add(arr):
	sum_ = 0
	for element in arr:
		sum_+=element
	return sum_

def calcOpCode(codes):
	i = 0
	while i <= len(codes) - 3:
		if codes[i] == 99:
			return codes
		elif codes[i] == 1:
			codes[codes[i+3]] = codes[codes[i+1]]+codes[codes[i+2]]
			i+=3
		elif codes[i] == 2:
			codes[codes[i+3]] = codes[codes[i+1]]*codes[codes[i+2]]
			i+=3
		else:
			i+=1
	return out

def getOpCode(codes,target):
	for i in range(1,100):
		for j in range(1,100):
			temp = codes.copy()
			temp[1],temp[2] = i, j
			if calcOpCode(temp)[0] == target:
				return temp[1],temp[2]
	return -1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        store = ''
        for i in range(len(s),-1,-1):
            for j in range(len(s)):
                temp = s[j:i]
                backwards = "".join([i for i in temp[::-1]])
                if temp == backwards:
                    if len(temp) > len(store):
                        store = temp
        return store
        
def palindrome(s):
    length = len(s)
    palindromes = []
    for i in range(2,len(s)+1):
        small = 0
        while (small+i) < length+1:
            if(s[small:(small+i)] == s[small:(small+i)][::-1]):
                palindromes.append(s[small:(small+i)])
            small +=1
    return palindromes

if __name__ == "__main__":
	out = []
	with open("data.txt","r") as f:
		for line in f:
			out.append(calculateFuel(int(line)))
	print(reduce(lambda x,y: x+ y, out))
	print(add(out))

	with open("data_.txt","r") as f:
		stuff = csv.reader(f, delimiter=',')
		out = [int(x) for b in stuff for x in b]
		out[1] = 1
		out[2] = 3
		print(getOpCode(out, 19690720))