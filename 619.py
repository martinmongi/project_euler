from lib import factorization_sieve, choose
from collections import Counter
import math

class StringList(object): 
 
 def __init__(self, val):
    self.val = val 
 
 def __hash__(self):
    return hash(str(self.val)) 
 
 def __repr__(self):
    # Bonus: define this method to get clean output
    return str(self.val) 
 
 def __eq__(self, other):
    return str(self) == str(other)

def perfect_square(c):
    for k in c:
        if c[k] % 2 == 1:
            return False
    return True

def unpaired_factors_sieve(n):
    s = factorization_sieve(n)
    res = []
    for c in s:
        res.append(set())
        for divisor in c:
            if c[divisor] % 2 == 1:
                res[-1].add(divisor)
        res[-1] = sorted(res[-1])
    return res

def number_of_subsets_with_even_cardinal(k):
    return int(math.ceil(2**(k-1)))
    # res = 0
    # for i in range(0, k + 1, 2):
    #     res += choose(i, k)
    # return res

def solve(a,b):
    c1= unpaired_factors_sieve(b)[a:]
    c1 = [l for l in c1 if all(map(lambda n: n*2 <= b, l))] 
    print(c1)

    c2 = Counter(map(StringList,c1))
    print(c2)

    multiplier = (2**c2['[]']) % 1000000007
    c2['[]'] = 0

    for k,v in c2.items():
        if v >= 2:
            print(k,v)
            multiplier *= number_of_subsets_with_even_cardinal(v)
    print(multiplier)

    # aca hay que tener cuidado de no usar el resto si se tienen numero par

    c3 = [set(i) for i in c1 if i != []]
    print(c3)

    for i1 in range(len(c3)):
        s1 = c3[i1]
        for i2 in range(i1 + 1,len(c3)):
            s2 = c3[i2]
            potential_s3 = s1.symmetric_difference(s2)
            for i3 in range(i2 + 1, len(c3)):
                if c3[i3] == potential_s3:
                    print(s1, s2, potential_s3)
                    multiplier *= 2

    print(multiplier)

    print('-----------------------------------------------------------------------------')
    pass


solve(40,55)
solve(100,123)
# solve(1000,1234)
