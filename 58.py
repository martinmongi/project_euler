#!/usr/bin/env python3

from lib import prime

side = 1
diag = [1]

p_count = 0
count = 1

#c = sieve(10**7)

while True:
	side += 2
	
	if prime((3*(side-2)**2 + 1*side**2)/4):
		p_count += 1

	if prime((2*(side-2)**2 + 2*side**2)/4):
		p_count += 1

	if prime((1*(side-2)**2 + 3*side**2)/4):
		p_count += 1

	# if c[int((0*(side-2)**2 + 4*side**2)/4)]:
	# 	p_count += 1
	count += 4
	print(side, (p_count + .0)/count)

	if (p_count + .0)/count < .1:
		break

print(side)