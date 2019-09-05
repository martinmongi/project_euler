
# ARQ
# (red(3), blue(2), white(1), yellow(2 not yellow), light yellow(1 not yellow))

from pprint import pprint
from collections import defaultdict

g2 = {(2, 0, 0, 0, 0): 1,  # red red
      (1, 1, 0, 0, 0): 1,  # red blue
      (1, 0, 0, 1, 0): 1,  # red yellow
      (0, 2, 0, 0, 0): 1,  # blue blue
      (0, 1, 0, 1, 0): 1}  # blue yellow

pprint(g2)

def next_step(gs):

    g3 = defaultdict(lambda:0)

    for g,k in gs.items():
        cr,cb,cw,cy,cly = g

        # USING RED NODE
        if cr > 0:
            # adding red node to red node
            g3[(cr,cb+1,cw,cy,cly)] = 1
            # adding blue node to red node
            g3[(cr - 1, cb + 2, cw, cy, cly)] = 1
            # adding yellow node to red node
            g3[(cr - 1, cb + 1, cw, cy + 1, cly)] = 1

        # USING BLUE NODE
        if cb > 0:
            # adding red node to blue node
            g3[(cr + 1, cb - 1, cw + 1, cy, cly)] = 1
            # adding blue node to blue node
            g3[(cr, cb, cw + 1, cy, cly)] = 1
            # adding yellow node to blue node
            g3[(cr, cb - 1, cw + 1, cy + 1, cly)] = 1
        
        # USING WHITE NODE
        if cw > 0:
            # adding red node to white node
            g3[(cr + 1, cb, cw - 1, cy, cly)] = 1
            # adding blue node to white node
            g3[(cr, cb + 1, cw - 1, cy, cly)] = 1
            # adding yellow node to white node
            g3[(cr, cb, cw - 1, cy + 1, cly)] = 1

        # USING YELLOW NODE
        if cy > 0:
            # adding red node to yellow node
            g3[(cr + 1, cb, cw, cy - 1, cly + 1)] = 1
            # adding blue node to yellow node
            g3[(cr, cb + 1, cw, cy - 1, cly + 1)] = 1
        
        # USING LIGHT YELLOW NODE
        if cly > 0:
            # adding red node to light yellow node
            g3[(cr + 1, cb, cw, cy, cly-1)] = 1
            # adding blue node to light yellow node
            g3[(cr, cb + 1, cw, cy, cly - 1)] = 1
    return g3

g3 = next_step(g2)
pprint(dict(g3))
print(sum(v for k,v in g3.items()))

g4 = next_step(g3)
pprint(dict(g4))
print(sum(v for k, v in g4.items()))
