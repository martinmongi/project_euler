
import functools


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

@functools.lru_cache(maxsize=None)
def fact(n):
    for i in range(2, int((n)**.5 + 1)):
        if n % i == 0:
            return [i] + fact(n//i)
    return [n]

@functools.lru_cache(maxsize=None)
def prime(n):
    if n < 2:
        return False
    for i in range(2, int((n)**.5 + 1)):
        if n % i == 0:
            return False
    return True

# for x in range(1,100000):
#     for y in range(1,x):
#         p = (x**3 - y**3)/y/y
#         if int(p) == p and prime(p):
#             print(x,y,p)
#             g = gcd(x,y)
#             print(g, x/g,y/g)
#             print('-----------------')

a = 2
c = 0
while True:
    b = a - 1
    res = a**3-b**3
    if prime(res):
        print(a,b,res)
        c += 1
    if res >= 10**6:
        break 
    a += 1
print(c)