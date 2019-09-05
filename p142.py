def vals(x,y,z):
    return [x+y,x+z,y+z,y-x,z-x,z-y]

def ps(x):
    return int(x**.5)**2 == x

for xyz in range(6,10000):
    for x in range(1,xyz//3+1):
        if not ps(xyz-x):
            continue
        for y in range(x+1, (xyz-x)//2+1):
            z = xyz-y-x
            if z <= y:
                break
            d = [v for v in vals(x, y, z) if ps(v)]
            if len(d) > 4:
                print(x,y,z, vals(x,y,z), len(d), )
                if len(d) == 6:
                    exit()
