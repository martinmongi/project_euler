from lib import sieve

N = 10**2 + 1

siv = sieve(N)

primes = [p for p in range(N) if siv[p]]

s = 0
for i in range(len(primes)-1):
    # if i % 1000 == 0:
    #     print(i)
    p1 = primes[i]
    if p1 == 3:
        continue
    p2 = primes[i+1]
    d = len(str(p1))

    r = 10**d + p1
    print(10**d, '%', p2, '=', 10**d % p2)
    while True:
        print(r, '%', p2, '=', r % p2)
        if r % p2 == 0:
            print(p1,p2,r)
            s += r
            break
        r += 10**d
        
print(s)
