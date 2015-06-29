#!/usr/bin/env python3

from lib import digits

def increasing(n):
	s = digits(n)
	for i in range(len(s) - 1):
		if int(s[i]) > int(s[i+1]):
			return False

	return True

def decreasing(n):
	s = digits(n)
	for i in range(len(s) - 1):
		if int(s[i]) < int(s[i+1]):
			return False

	return True

bcount = 0

i = 1
d = 3
for i in range(1, 10**d):
	if decreasing(i) or increasing(i):
		bcount += 1

print(bcount)