#!/usr/bin/env python3

from lib import gcd

Lmax = 1500000
seen = {}

for m in range(1,int((Lmax)**.5)):
	for n in range(1,m):
		if (m+n)%2 == 1 and gcd(m,n) == 1:
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			s = a+b+c
			for k in range(s, Lmax+1, s):
				if k not in seen:
					seen[k] = set([])
				seen[k].add(",".join(map(str,sorted([k/s*a,k/s*b,k/s*c]))))

#print(seen)
count = 0
for key in seen:
	if len(seen[key]) == 1:
		count += 1

print(count)

