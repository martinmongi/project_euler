#!/usr/bin/env python3

from lib import digits


for conv in range(1,100):

	v = []

	for i in range(conv):
		if i % 3 == 1:
			v.append(int((i+2)/3*2))
		else:
			v.append(1)

	#print(v)

	n = v[-1]
	d = 1
	for i in range(conv - 2, -1, -1):
		n,d = d,n
		n = n + v[i]*d
		

	print(conv + 1, "\t\t", d+ 2*n ,"\t\t", n,"\t\t",  2 + d/n)