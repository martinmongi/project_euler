#!/usr/bin/env python3
from lib import sieve

MAX_SIEVE = 5*10**7
s = sieve(int(MAX_SIEVE**.5+100))
primes = []

for i in range(len(s)):
	if s[i]:
		primes.append(i)

d = set([])
a = 0
b = 0
c = 0
s = primes[a]**2 + primes[b]**3 + primes[c]**4
while s < MAX_SIEVE:
	while s < MAX_SIEVE:
		while s < MAX_SIEVE:
			if s < MAX_SIEVE:
				d.add(s)
			c += 1
			s = primes[a]**2 + primes[b]**3 + primes[c]**4
		b += 1
		c = 0
		s = primes[a]**2 + primes[b]**3 + primes[c]**4
	a += 1
	b = 0
	c = 0
	s = primes[a]**2 + primes[b]**3 + primes[c]**4

print(len(d))