#!/usr/bin/env python3

from lib import digits

max_sum = 0
for a in range(100):
	for b in range(100):
		s = sum(map(int,digits(a**b)))
		if s > max_sum:
			max_sum = s
			print(a,b,s)