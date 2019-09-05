from pprint import pprint

from functools import reduce
from itertools import combinations
from collections import defaultdict
import operator
from lib import sieve

N = 10**8


def cool_sieve(n):
    c = defaultdict(lambda:[])
    c[0] = False
    c[1] = False
    for i in range(2, n + 1):
        if c[i] == []:
            c[i] = False
            for j in range(2 * i, n + 1, i):
                if c[j] == False or j % (i * i) == 0:
                    c[j] = False
                else:
                    c[j].append(i)

    return {i:c[i] for i in range(2,n+1) if c[i] != False}

fsieve = cool_sieve(N)
sieve = sieve(N)
# pprint(fsieve)

def perfect(divs):
    for s in range(len(divs) + 1):
        for comb in combinations(divs, s):
            d1 = reduce(operator.mul, comb, 1)
            d2 = i // d1
            r = d1 + d2
            # print(d1,d2,r)
            if not sieve[r]:
                return False
    return True


s = 0
for i in fsieve:
    if i % 2 == 0:
        divs = fsieve[i]
        # print(i, divs)
        if perfect(divs):
            print(i, "PERFECT!")
            s += i
        
print(s)

