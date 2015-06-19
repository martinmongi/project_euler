#!/usr/bin/env python3

from lib import digits
import itertools

def cyclic(l):
	if digits(l[0])[:2] != digits(l[-1])[2:]:
		return False
	for i in range(1,len(l)):
		if digits(l[i])[:2] != digits(l[i-1])[2:]:
			return False
	return True


p = 0
i = 0
p3 = []

while p < 10000:
	p = i*(i+1)/2
	if p >= 1000 and p < 10000:
		p3.append(int(p))
	i += 1


p = 0
i = 0
p4 = []

while p < 10000:
	p = i**2
	if p >= 1000 and p < 10000:
		p4.append(p)
	i += 1

p = 0
i = 0
p5 = []

while p < 10000:
	p = i*(3*i-1)/2
	if p >= 1000 and p < 10000:
		p5.append(int(p))
	i += 1

p = 0
i = 0
p6 = []

while p < 10000:
	p = i*(2*i-1)
	if p >= 1000 and p < 10000:
		p6.append(int(p))
	i += 1

p = 0
i = 0
p7 = []

while p < 10000:
	p = i*(5*i-3)/2
	if p >= 1000 and p < 10000:
		p7.append(int(p))
	i += 1

p = 0
i = 0
p8 = []

while p < 10000:
	p = i*(3*i-2)
	if p >= 1000 and p < 10000:
		p8.append(int(p))
	i += 1


for i3 in p3:
	for i4 in p4:	
		for i5 in p5:
			for i6 in p6:
				l = [i3,i4,i5,i6]
				ends = set([])
				starts = set([])
				for i in l:
					ends.add("".join(digits(i)[2:]))
					starts.add("".join(digits(i)[:2]))
				if len(starts & ends) > 0:
					for i7 in p7:
						l = [i3,i4,i5,i6,i7]
						ends = set([])
						starts = set([])
						for i in l:
							ends.add("".join(digits(i)[2:]))
							starts.add("".join(digits(i)[:2]))
						if len(starts & ends) > 3:	
							for i8 in p8:
								l = [i3,i4,i5,i6,i7,i8]
								ends = set([])
								starts = set([])
								for i in l:
									ends.add("".join(digits(i)[2:]))
									starts.add("".join(digits(i)[:2]))
								if ends == starts:
									print(ends, starts, l)

