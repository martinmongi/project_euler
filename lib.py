
def cribe(n):
	c = [False, False] + [True]*(n-1)
	for i in range(n+1):
		if c[i]:
			for j in range(2*i, n+1, i):
				c[j] = False

	return c

def prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

