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
    pass


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

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
