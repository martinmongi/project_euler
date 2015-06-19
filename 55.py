#!/usr/bin/env python3

def lychrel(n):
	max_iter = 50
	while max_iter > 0:
		n = n + int(str(n)[::-1])
		if n == int(str(n)[::-1]):
			return False
		max_iter -= 1
	return True

count = 0
for i in range(10**4):
	if lychrel(i):
		count += 1

print(count)