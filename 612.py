from operator import mul
import itertools
from collections import Counter


def numbers(n, k):
    # n length, k distinct digits
    if n <= k:
        return reduce(mul, range(k, k-n, -1))

    # n > k means repeated digits


d = Counter()
for n in itertools.product(range(3), repeat=4):
    digits = set(list(n))
    d[len(digits)] += 1
    if len(digits) == 2:
        print n, digits

print d