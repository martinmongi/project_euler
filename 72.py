#!/usr/bin/env python3

def sieve(n):
	c = []
	for i in range(n+1):
		count = int(i/2) - int(i/3)
		if i%2 == 0:
			count -= 1
		c.append(count)
	for i in range(2,n+1):
		for j in range(2*i,n+1,i):
			c[j] -= c[i]
	return c



	# for i in range(n+1):
	# 	if c[i]:
	# 		for j in range(2*i, n+1, i):
	# 			c[j] = False

	return c



print(sum(sieve(12000)[1:]))