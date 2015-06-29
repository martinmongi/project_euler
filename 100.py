#!/usr/bin/env python3

import time

br = 1

for br in range(10**12,10**13):
	i = 0

	p_d = br*(br-1)
	p_n = int(p_d/2)

	#blue**2 - blue - p_n

	a = float(1)
	b = float(-1)
	c = float(-p_n)

	if b**2-4*a*c >= 0:
		r2 = (-b+(b**2-4*a*c)**.5)/2/a
		print(p_n, p_d, br, r2)
		if r2 == int(r2):
			
			break


