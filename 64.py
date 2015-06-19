#!/usr/bin/env python3

def period_length(n):
	m = 0
	d = 1
	a_0 = int(n**0.5)
	a = a_0

	i = 0
	while a != 2*a_0:
		
		m = int(d*a - m)
		d = int((n-m**2)/d)
		a = int((a_0+m)/d)
		i += 1
	return i
		
count = 0
for i in range(10001):
	if i**0.5 != int(i**.5):
		if period_length(i)%2 == 1:
			count+=1

print(count)