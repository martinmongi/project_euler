#!/usr/bin/env python3
s = 0
for a in range(2,10**9):
	if a%10**6 == 0:
		print(a)
	a = float(a)
	# a a+1 a+1

	area = a/2/2*(3*a*a/4+2*a+1)**.5

	if area == int(area) and 3*a+2 < 10**9:
		s += 3*a+2

	area = a/2/2*(3*a*a/4-2*a+1)**.5

	if area == int(area) and 3*a-2 < 10**9:
		s += 3*a-2

print(s)