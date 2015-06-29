#!/usr/bin/env python3

import sys

base = []
exp = []
for line in sys.stdin:
	s = list(map(int, line.split(',')))
	base.append(s[0])
	exp.append(s[1])

m = max(exp)

for i in range(len(exp)):
	exp[i] = float(exp[i])/m

res = []

for i in range(len(base)):
	res.append(base[i]**exp[i])

print(res)

m = 0

for i in range(len(base)):
	if m < res[i]:
		m = res[i]
		mi = i

print(mi)