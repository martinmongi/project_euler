#!/usr/bin/env python3

from lib import digits

count= 0
for exp in range(1,25):
	for digit in range(1,10):
		if len(digits(digit**exp)) == exp:
			print(digit, exp, digit**exp)
			count += 1

print(count)