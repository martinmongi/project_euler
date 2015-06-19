#!/usr/bin/env python3

from lib import factorize

def factorization(n):
	ifact_f = {}
	for k in factorize(n):
		if k not in ifact_f:
			ifact_f[k] = 0
		ifact_f[k] += 1
	return ifact_f

def fact_factorization(i):
	ifact_f = {}
	for j in range(2,i+1):
		for k in factorize(j):
			if k not in ifact_f:
				ifact_f[k] = 0
			ifact_f[k] += 1
	return ifact_f

def divisible(a,b):
	#a % b
	for fact in b:
		if fact not in a:
			return False
		if a[fact] < b[fact]:
			return False
	return True

def mult_mod18(a):
	n = 1
	for key in a:
		for i in range(a[key]):
			n = (n*key) % (10**18)
	return n

def N(i):
	n = 1
	n_f = {}
	i_f = fact_factorization(i)
	for key in i_f:
		i_f[key] *= 1234567890
	print(i_f)

	while True:
		if divisible(n_f,i_f):
			break
		n += 1
		print(n, n_f)
		for fact in factorize(n):
			if fact not in n_f:
				n_f[fact] = 0
			n_f[fact] += 1

	return n

def S(u):
	res = 0
	for i in range(10,u+1):
		res += N(i)

print(N(2))