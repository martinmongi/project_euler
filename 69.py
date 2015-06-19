#!/usr/bin/env python3

from lib import coprimes,factorize

facts = {}

for n in range(1,1000001):
	facts[n] = set(factorize(n))

print("Fact done")

def phi(n):
	count = 0
	for i in range(1,n):
		if len(facts[n] & facts[i]) == 0:
			count += 1
	return count

maxnp = 1
for n in range(2,1000000):
	np = float(n)/phi(n)
	if maxnp < np:
		maxn = n
		maxnp = np

print(maxn, maxnp)
