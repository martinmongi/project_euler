import functools

@functools.lru_cache(maxsize=None)
def f(n):
    if n == 0:
        print(n,'-->',1)
        return 1
    if n % 2 == 1:
        return f(n//2)
    
    b = bin(n)[2:]
    i = b.rfind('1')
    print(len(b), b, i, b[i:])
    r = f(int(b[:i + 1], base=2)) + \
        (len(b) - i - 1) * f(int(b[:i] + '0', base=2))
    print(n, '-->', r)
    return r



f(10**25)
