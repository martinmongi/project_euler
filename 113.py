#!/usr/bin/env python

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

digits = 100
import numpy as np
c = np.zeros([digits + 1,10])

c[1,:] = np.ones([1,10])

for i in range(2,digits+1):
	for j in range(10):

		for k in range(j,10):
			c[i,j] += c[i-1,k]

print c
print int(sum(sum(c))*2 - digits*10 -  sum(c[:,0]))