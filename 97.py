#!/usr/bin/env python3

n = 1
for i in range(7830457):
	n = (2*n)%(10**10)

n = (28433*n)%(10**10)
n = n + 1

print(n)