def solve(x,r):
    return x**2 - (x - r)**2 - (x - 2 * r)**2

import math
from collections import Counter, defaultdict
from pprint import pprint
from lib import div_sieve
limit = 1000

siv = div_sieve(limit)
rc = 0
for N in range(len(siv)):
    c = 0
    for x in siv[N]:
        r = (N + x*x)/4/x
        if x-r > 0 and int(r) == r and r > 0:
            r = int(r)
            print(x+r,x,x-r,N,sep='\t')
            res = (x-r,x,x+r,N)
            c += 1
            if c > 1:
                break
    if c == 1:
        print(res)
        rc += 1
# print(rc)