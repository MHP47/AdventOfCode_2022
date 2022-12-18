from utils import *


class cube(tuple):
    def __new__ (cls, a, b, c):
        return super(cube, cls).__new__(cls, tuple([a,b,c]))
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    def neighbours(self):
        return set((
            (self.x-1, self.y, self.z),
            (self.x+1, self.y, self.z),
            (self.x, self.y-1, self.z),
            (self.x, self.y+1, self.z),
            (self.x, self.y, self.z-1),
            (self.x, self.y, self.z+1),
        ))


def part_1(p_Input):
    l = [cube(*map(int,x.split(','))) for x in p_Input.strip().splitlines()]
    s = set(x for x in l)
    count = 0

    for c in l:
        count += sum(1 for t in c.neighbours() if t in s)

    return 6*len(l)-count


def part_2(p_Input):
    l = [cube(*map(int,x.split(','))) for x in p_Input.strip().splitlines()]
    s = set(l)

    xmin = min(x for x,y,z in l)
    xmax = max(x for x,y,z in l)
    ymin = min(y for x,y,z in l)
    ymax = max(y for x,y,z in l)
    zmin = min(z for x,y,z in l)
    zmax = max(z for x,y,z in l)
    xr = range(xmin-1,xmax+2)
    yr = range(ymin-1,ymax+2)
    zr = range(zmin-1,zmax+2)

    def N(x,y,z):
        return set((
            (x-1, y, z),
            (x+1, y, z),
            (x, y-1, z),
            (x, y+1, z),
            (x, y, z-1),
            (x, y, z+1),
        ))

    possible_water = set()
    to_check = deque([(xmin-1, ymin-1, zmin-1)])
    while to_check:
        x,y,z = to_check.popleft()
        if x not in xr or y not in yr or z not in zr:
            continue
        if (x,y,z) in s:
            continue
        found = N(x,y,z) - possible_water
        possible_water.update(found)
        to_check.extend(found)

    water = []
    for x,y,z in l:
        water.append(N(x,y,z).intersection(possible_water) - s)

    return sum(len(x) for x in water)


example_input_1 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""
challenge_input = Input('18')

assert(part_1(example_input_1) == 64)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 58)
print(f"Part 2: {part_2(challenge_input)}")
