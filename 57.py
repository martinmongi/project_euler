#!/usr/bin/env python3

from lib import digits

a = 3
b = 2
count = 0
for it in range(1, 1001):
	#	print(a,b)
	a,b = 2*b+a,b+a
	if len(digits(a)) > len(digits(b)):
		count += 1

print(count) 
