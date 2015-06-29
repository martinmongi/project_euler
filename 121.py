#!/usr/bin/env python3

def f(r,dif,i):
	if(i == r):
		if dif < 0:
			return 1
		elif dif > 1:
			return 0
		else:
			return 1.0/(r+1)

	p_b = 1/(r+1)*f(r+1,dif-1,i)
	p_r = r/(r+1)*f(r+1,dif+1,i)

	return p_b+p_r

print(1/f(1,1,15))