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

while True:
	if not decreasing(i) and not increasing(i):
		bcount += 1
	if(bcount/i >= .99):
		break
	i += 1

print(i)