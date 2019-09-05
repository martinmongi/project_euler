from fractions import Fraction

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def perfect_cube(n):
    root = round(n**(1./3.))
    return root**3 == n

def solve(p):
    for n_root in range(1, p):
        n = n_root**3
        if perfect_cube(n**2*(n+p)):
            return n

c = 0
for i in range(1,10**4):
    if prime(i):
        s = solve(i)
        if s:
            print(i, s)
            c += 1

print c