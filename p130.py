def A(n):
    if 0 in [n % 2, n % 5]:
        return -1
    d = 1
    c = 1
    while True:
        if d % n == 0:
            break
        d = (d*10+1) % n
        c += 1
    return c

import functools

@functools.lru_cache(maxsize=None)
def prime(n):
    if n < 2:
        return False
    for i in range(2, int((n)**.5 + 1)):
        if n % i == 0:
            return False
    return True

l = []
for n in range(2,20000):
    if prime(n) or 0 in [n % 2, n % 5]:
        continue
    
    if (n-1) % A(n) == 0:
        print(n)
        l.append(n)

print(len(l))
print(sum(l[:25]))
    
