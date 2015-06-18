
def cribe(n):
	c = [False, False] + [True]*(n-1)
	for i in range(n+1):
		if c[i]:
			for j in range(2*i, n+1, i):
				c[j] = False

	return c
