
from collections import defaultdict
from pprint import pprint

d = defaultdict(lambda: set())

N = 10**4
limit = int(N/2**.5)

for m in range(1,limit):
    if m*m > limit:
        break
    for n in range(1,m):
        dist = m*m + n*n
        if dist > limit:
            break
        c1 = m*m - n*n
        c2 = 2*m*n
        d[dist].add((min(c1, c2), max(c1, c2)))
        # print(c1,c2,dist)

for k,v in d.items():
    if len(v) > 5:
        print(k,v)
