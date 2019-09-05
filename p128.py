from pprint import pprint
import functools

@functools.lru_cache(maxsize=None)
def prime(n):
    if n < 2:
        return False
    for i in range(2,int((n)**.5+1)):
        if n % i == 0:
            return False
    return True


v = [2]
u = [7]
kv = 6
ku = 12
for i in range(100000):
    v.append(v[-1] + kv)
    u.append(u[-1] + ku)
    kv += 6
    ku += 6

# print(v)
# print(u)

print("1")
print("2")
count = 2


for i in range(1,len(v)-2):
    neigv = [v[i - 1], v[i] + 1, v[i + 1] - 1,
            v[i + 1], v[i + 1] + 1, v[i + 2] - 1]

    diff = [abs(k - v[i]) for k in neigv]
    c = 0
    for k in diff:
        if prime(k):
            c += 1
    if c == 3:
        count += 1
        print(count, v[i], neigv, diff)

    neigu = [v[i-1],u[i-1], v[i], u[i] - 1, u[i+1]-1, u[i+1]]
    diff = [abs(k - u[i]) for k in neigu]
    c = 0
    for k in diff:
        if prime(k):
            c += 1
    if c == 3:
        count += 1
        print(count, u[i], neigu, diff)

# pprint(v)
