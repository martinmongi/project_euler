#!/usr/bin/env python
def rec_count(x,y):
	return x*(x+1)*y*(y+1)/4

dif = float(2*10**6)
for x in range(1,2500):
	for y in range(1,2500):

		squares = x*(x+1)*y*(y+1)/4

		if abs(squares-2*10**6) < dif:
			dif = abs(squares-2*10**6)
			marea = (x,y,x*y)


print marea