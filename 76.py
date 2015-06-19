#!/usr/bin/env python3

from lib import prime

def ways_to_sum(n):
	v = [0]*(n+1)
	v[0] = 1
	v[1] = 1
	for i in range(1,len(v)-1):
		if prime(i):
			for j in range(i,len(v)):
				#i is the number i am counting
				v[j] += v[j-i]

	print(v)

ways_to_sum(75)