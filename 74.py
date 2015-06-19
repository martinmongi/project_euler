#!/usr/bin/env python3

from lib import fact, digits

def cycle_length(n):
	seen = {n:0}
	i = 0
	while True:
		n = sum(map(fact,map(int,digits(n))))
		i += 1
		if n in seen:
			return i
		else:
			seen[n] = i

count = 0
for n in range(1000000):
	if cycle_length(n) == 60:
		count += 1

print(count)