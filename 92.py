#!/usr/bin/env python3

from lib import digits

def sq(n):
	return n**2

def f89(n):
	if n == 89:
		return True
	elif n <= 1:
		return False
	else:
		d = digits(n)
		d = list(map(int,d))
		d = list(map(sq,d))
		d = sum(d)
		return f89(d)

e89 = [-1] * (10**8+1)
e89[89] = 1
e89[1] = 0

count = 0
for i in range(1,10**7):
	n = i
	#print(n)
	while e89[n] < 0:
		d = digits(n)
		d = list(map(int,d))
		d = list(map(sq,d))
		n = sum(d)
	e89[i] = e89[n]
	if e89[i] > 0:
		#print(i)
		count += 1

print(count)
