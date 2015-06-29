#!/usr/bin/env python3

from lib import prime

ways = [0]*11

for i in range(10):
	if prime(i):
		ways[i] = 1
	else:
		ways[i] = 0
	for j in range(i):
		if prime(i-j):
			ways[i] += ways[j]

print(ways)