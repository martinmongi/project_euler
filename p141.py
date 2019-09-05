limit = 10**1
from lib import factorize
from itertools import combinations
from functools import reduce
import operator

limit = 12
s = set()
for b in range(1, 10**limit):
    if b**3 + 1 > 10**limit:
            break
    for a in range(1, b):
        if a * b**3 + a**2 > 10**limit:
            break
        for k in range(1, 10**limit):
            n = k**2 * a * b**3 + k * a**2
            if n > 10**limit:
                break
            if int(n**.5)**2 == n:
                print(k, a, b, '\t', k * a**2, k * a * b, k * b**2, n)
                s.add(n)

print(s)
print(sum(s))
