
for n in range(10**6,2*10**6):
    if n % 2 == 0 or n % 5 == 0:
        continue
    d = 1
    c = 1
    while True:
        if d % n == 0:
            print(n,c)
            break
        d = (d*10+1) % n
        c += 1
    if c > 10**6:
        break

