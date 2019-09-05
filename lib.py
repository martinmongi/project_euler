
from collections import Counter

def sieve(n):
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

def digits(n):
	return list(str(n))

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

def choose(r,n):
	return fact(n)/fact(n-r)/fact(r)

def coprimes(a,b):
	return gcd(a,b) == 1

def gcd(a,b):
	if min(a,b) == 0:
		return max(a,b)
	return gcd(min(a,b), max(a,b) % min(a,b))

def factorize(n):
	i = 2
	factors = []
	divided = True
	while i <= n**0.5 or divided:
		if divided:
			i = 2
			divided = False
		if n % i == 0:
			factors.append(i)
			n = n/i
			divided = True
		i = i + 1
	if n > 1:
		factors.append(int(n))
	return factors

def factorization_sieve(n):
	c = [Counter() for i in range(n+1)]
	for i in range(2, n+1):
		if c[i] == Counter([]):
			c[i][i] += 1
			for j in range(2*i, n+1, i):
				aux = j
				while aux % i == 0:
					c[j][i] += 1
					aux /= i

	return c


def div_sieve(n):
	c = [[1] for i in range(n + 1)]
	for i in range(2, n + 1):
		for j in range(i, n + 1, i):
			c[j].append(i)

	return c
