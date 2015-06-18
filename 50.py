#!/usr/bin/env python3

from lib import cribe

c = cribe(10**6)

primes = []

for i in range(len(c)):
	if c[i]:
		primes.append(i)


l = 0

while l < len(primes):
	l = l + 1
	i = 0
	found = False
	while i + l < len(primes) and not found:
		a = sum(primes[i:i+l])
		if a < len(c):
			if c[a]:
				found = True
				print(a, l, primes[i], primes[i+l-1])
		i = i + 1

