#!/usr/bin/env python3

from lib import sieve
import itertools

max_i = 10**6
c = sieve(max_i)

max_count = 0
for i in range(56003, max_i, 2):
	#print(i)
	#print("============")
	##if c[i]:
	s = str(i)
	for mask in itertools.product(range(2), repeat=len(s)):
		stars = []
		#print(mask)
		for j in range(len(mask)):

			if mask[j] == 1:
				stars.append(j)
		#print(stars)

		if len(stars) > 0:
			if mask[0] == 1:
				start = ord('1')
			else:
				start = ord('0')
			count = 0
			for digit in range(start, ord('9') + 1):
				n = list(s)
				for j in stars:
					n[j] = chr(digit)
				n = ''.join(n)
				if c[int(n)]:
					count = count + 1
			if count > max_count:
				max_count = count
				print(i, count, mask)