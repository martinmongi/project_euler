#!/usr/bin/env python3

import itertools

def targets(s):
	if len(s) <= 1:
		for i in s:
			return s

	ts = set([])
	for i in s:
		ns = s - set([i])
		subts = targets(ns)
		ts |= set([x + i for x in subts])

		ts |= set([x - i for x in subts])
		ts |= set([i - x for x in subts])
		ts |= set([x * i for x in subts])
		if i != 0:
			ts |= set([x / i for x in subts])

		subts -= set([0])
		ts |= set([i / x for x in subts])
		#print(i,s,ts)

	return ts

maxi = (0,0,0,0,0)
for d in range(10):
	for c in range(d):
		for b in range(c):
			for a in range(b):
				s = set(list(map(float,[a,b,c,d])))
				s = set(map(int,sorted(list(targets(s)))))

				sol = []
				for i in s:
					if i > 0:
						sol.append(i)

				sol.sort()

				for i in range(len(sol)):
					if sol[i] != i+1:
						break

				if maxi[4] < i:
					maxi = (a,b,c,d,i)
					print(maxi, sol)

print(maxi)