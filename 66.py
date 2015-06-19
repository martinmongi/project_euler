#!/usr/bin/env python3

for d in range(2,1001):
	if d**.5 == int(d**.5):
		continue
	x = 2
	y = 0
	while True and abs(x-y) > 1:
		y = ((x**2 - 1 + .0)/d)**.5
		
		if y == int(y):
			print(x,d,y)
			break
		x = x + 1