def R(n):
    return int('1'*n)

import functools

@functools.lru_cache(maxsize=None)
def prime(n):
    if n < 2:
        return False
    for i in range(2, int((n)**.5 + 1)):
        if n % i == 0:
            return False
    return True


@functools.lru_cache(maxsize=None)
def fact(n):
    for i in range(2, int((n)**.5 + 1)):
        if n % i == 0:
            # print(i,end=",")
            return [i] + fact(n // i)
    return [n]

def is25power(n):
    while n % 2 == 0:
        n = n // 2
    while n % 5 == 0:
        n = n // 5
    return n == 1

N = 10**5

reps = [(i,R(i)) for i in range(1,N) if is25power(i)]
print([i for i,r in reps])
c = 0
s = 0
for p in [i for i in range(10,10**5) if prime(i)]:
    for i,r in reps:
        if i > p:
            break
        if r % p == 0:
            print(p, ' -> ', i)
            c += 1
            s += p
            # print(c,s)
            break

print(sum(p for p in range(2,10**5) if prime(p))- s)
