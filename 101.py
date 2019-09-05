from fractions import Fraction

def sum_poly(a, b):
    if len(b) > len(a):
        a, b = b, a
    res = []
    for i in range(len(b)):
        res.append(a[i]+b[i])
    for i in range(len(b), len(a)):
        res.append(a[i])
    return res

def prod_poly(a, b):
    res = [0 for i in range(len(a) + len(b) - 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            res[i+j] += a[i]*b[j]
    return res

def interpolating_poly(points):
    res = [0 for i in range(len(points) - 1)]
    for p in points:
        coef = Fraction(p[1])
        lagrange_poly = [1]
        for q in points:
            if p != q:
                coef /= p[0] - q[0]
                lagrange_poly = prod_poly(lagrange_poly, [-q[0], 1])
        lagrange_poly = [i*coef for i in lagrange_poly]
        res = sum_poly(res, lagrange_poly)
    return list(map(int,res))

def eval_poly(poly, x):
    return sum([poly[i]*x**i for i in range(len(poly))])

def OP(k,n):
    if k > 10:
        return eval_poly([1,-1,1,-1,1,-1,1,-1,1,-1,1], n)
    if k == 0:
        return eval_poly([],n)
    if k == 1:
        return eval_poly([[1],n])


points = [(x,OP(11,x)) for x in range(1,12)]
for i in range(1,15):
    print(i, end=",")
    opt = interpolating_poly(points[:i])
    for j in range(1,15):
        print(eval_poly(opt,j), end=',')
    print()