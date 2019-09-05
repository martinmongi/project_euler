def solve(x,r):
    return x**2 - (x - r)**2 - (x - 2 * r)**2

import math
from collections import Counter, defaultdict
from pprint import pprint
from lib import div_sieve
limit = 10**6

siv = div_sieve(limit)
rc = 0
for N in range(len(siv)):
    if len(siv[N]) < 10:
        continue
    c = 0
    for x in siv[N]:
        r = (N + x*x)/4/x
        if x-r > 0 and int(r) == r and r > 0:
            r = int(r)
            # print(x+r,x,x-r,N,sep='\t')
            c += 1
            if c > 10:
                break
    if c == 10:
        print(N)
        rc += 1
print(rc)
    
# count = defaultdict(lambda:[])

# for x in range(2,limit*5//4):
#     for r in range(math.ceil(x/5)+1,math.ceil(x/2)):
#         if solve(x,r) >= limit:
#             break
#         print(x,x-r,x-r-r, solve(x,r))
#         count[solve(x,r)].append((x,x-r,x-r-r))

# pprint(count)