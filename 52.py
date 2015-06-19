#!/usr/bin/env python3

from lib import digits

equal = False
x = 1
while not equal:
	equal = True
	dig = sorted(digits(x))
	for mul in range(2,7):
		if dig != sorted(digits(mul*x)):
			equal = False
	x = x + 1

print(x-1)