#!/usr/bin/env python3

from lib import digits
cubes = {}

i = 1
while True:
	if "".join(sorted(digits(i**3))) not in cubes:
		cubes["".join(sorted(digits(i**3)))] = []
	cubes["".join(sorted(digits(i**3)))].append(i)
	if len(cubes["".join(sorted(digits(i**3)))]) == 5:
		print(cubes["".join(sorted(digits(i**3)))])
		break
	i += 1	

##print(cubes)
