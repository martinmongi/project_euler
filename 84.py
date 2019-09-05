import random

n = 10**7	

position = 0
doubles = 0
ch_vec = [0,10,11,24,39,5]
cc_vec = [0,10] 

count = [0 for i in range(40)]

for i in range(n):
	count[position] += 1
	d1 = random.randint(1,4)
	d2 = random.randint(1,4)
	position += d1 + d2
	position %= 40
	if d1 == d2:
		doubles += 1
	else:
		doubles = 0
	if doubles == 3:
		position = 10
		doubles = 0
	if position == 7 or position == 22 or position == 36:
		r = random.randint(0,15)
		if r < 6:
			position = ch_vec[r]
		elif r == 6 or r == 7:
			if position == 7:
				position = 15
			elif position == 22:
				position = 25
			elif position == 36:
				position = 5
		elif r == 8:
			if position == 2:
				position = 2
			else:
				position = 12
		elif r == 9:
			position -= 3
	if position == 2 or position == 17 or position == 33:
		r = random.randint(0,15)
		if r < 2:
			position = cc_vec[r]
	if position == 30:
		position = 10

	
res = []
for i in range(40):
	res.append((round(count[i]*100/n,5),i))

for i in sorted(res)[::-1]:
	print(i)
