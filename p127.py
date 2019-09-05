
from pprint import pprint

def gcd(a,b):
    if b > a:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def calc_rad(N):
    rad = {i:1 for i in range(1,N+1)}
    for i in range(2,N+1):
        if rad[i] == 1:
            for j in range(i,N+1,i):
                rad[j] *= i
    return rad
            
    

N = 120000
# N = 1000
r = calc_rad(N)
# pprint(r)

count = 0
for c in range(1,N):
    if r[c] == c:
        continue
    for a in range(1,(c+1)//2):
        b = c - a
        if r[a]*r[b]*r[c] < c:
            if gcd(a,b) == gcd(b,c) == gcd(a,c) == 1:
                print(a,b,c)
                count += c

print(count)