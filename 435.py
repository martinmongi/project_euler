fact = 2*3*4*5*6*7*8*9*10*11*12*13*14*15

a = 1
b = 1

seen = set([(1,1)])
print(1)
print(1)

for i in range(100):
	a,b = b, (a+b)
	print(b)
	if (a% fact,b%fact) in seen:
		break
	seen.add((a%fact,b%fact))

print(len(seen))
