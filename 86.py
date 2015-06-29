#!/usr/bin/env python3
M = 100

count = 0
for a in range(1,M+1):
	for bc in range(1,2*a+1):
		sp = (a**2 + bc**2)**.5
		if sp == int(sp):
			for b in range(1,a):
				c = bc - b
				if c <= b and b <= a:
					count += 1

print(count)