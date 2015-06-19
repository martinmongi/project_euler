#!/usr/bin/env python3
from lib import digits, prime

def all_ccprimes(s):
	for i in s:
		for j in s:
			if i != j and not prime(int("".join(digits(i)+digits(j)))):
				return False
	return True


from lib import sieve

c = sieve(10**4)

primes = []

for i in range(len(c)):
	if c[i]:
		primes.append(i)

print("Sieve done")
min_sum = len(c)**5
for i1 in range(0,len(primes)):
	for i2 in range(i1+1,len(primes)):
		if all_ccprimes((primes[i1],primes[i2])):
			#print(primes[i1],primes[i2])
			for i3 in range(i2+1,len(primes)):
				if all_ccprimes((primes[i1],primes[i2],primes[i3])):
					#print(primes[i1],primes[i2],primes[i3])
					for i4 in range(i3+1,len(primes)):
						if all_ccprimes((primes[i1],primes[i2],primes[i3],primes[i4])):
							#print(primes[i1],primes[i2],primes[i3],primes[i4])
							for i5 in range(i4+1,len(primes)):
								if all_ccprimes((primes[i1],primes[i2],primes[i3],primes[i4],primes[i5])):
									print(primes[i1],primes[i2],primes[i3],primes[i4],primes[i5])
									if primes[i1] + primes[i2] + primes[i3] + primes[i4] + primes[i5] < min_sum:
										min_sum = primes[i1] + primes[i2] + primes[i3] + primes[i4] + primes[i5]
										min_set = (primes[i1],primes[i2],primes[i3],primes[i4],primes[i5])

print(min_set, min_sum)