#!/usr/bin/env python3

def can(a,b):
	a = set(a)
	b = set(b)
	if 6 in a or 9 in a:
		a.add(6)
		a.add(9)
	if 6 in b or 9 in b:
		b.add(6)
		b.add(9)

	sqs = set([1,4,9,16,25,36,49,64,81])

	formed = set([])
	for na in a:
		for nb in b:
			formed.add(na*10 + nb)
			formed.add(nb*10 + na)

	return sqs <= formed

import itertools

count = 0
for da in itertools.combinations(range(10),6):
	for db in itertools.combinations(range(10),6):
		if can(da,db):
			if da == db:
				count+=.5
			count +=.5
			print(da,db)

print(count)