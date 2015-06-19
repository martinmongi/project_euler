#!/usr/bin/env python3

from lib import choose

count = 0

for n in range(1, 101):
	for r in range(1,n + 1):
		if choose(r,n) > 10**6:
			count += 1

print(count)