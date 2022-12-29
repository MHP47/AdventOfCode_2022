from utils import *
from copy import deepcopy


N4 = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""
    def __init__(self, mapping=(), rows=(), neighbors=N4):
        """Initialize with, e.g., either `mapping={(0, 0): 1, (1, 0): 2, ...}`,
        or `rows=[(1, 2, 3), (4, 5, 6)].
        `neighbors` is a collection of (dx, dy) deltas to neighboring points.`"""
        self.update(mapping if mapping else
            {(x, y): val
             for y, row in enumerate(rows)
             for x, val in enumerate(row)})
        self.width  = max(x for x, y in self) + 1
        self.height = max(y for x, y in self) + 1
        self.deltas = neighbors
        self.blizzards = { i: ((x,y),v) for i,((x,y),v) in enumerate([(k,v) for k,v in self.items() if v in ('<','>','^','v')]) }
    def copy(self): return Grid(self, neighbors=self.deltas)
    def neighbors(self, point):
        """Points on the grid that neighbor `point`."""
        x, y = point
        return [(x+dx, y+dy) for (dx, dy) in self.deltas
            if (x+dx, y+dy) in self and self[(x+dx, y+dy)] != '#'] + [point]
    def to_rows(self):
        """The contents of the grid in a rectangular list of lists."""
        return [[self[x, y] for x in range(self.width)]
            for y in range(self.height)]
    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.get((x,y), ' '), end='')
            print()
        print()


def part_1(p_Input):
    grid = Grid(rows=p_Input.strip().splitlines())
    start = [(x,y) for (x,y),v in grid.items() if v == '.' and y == 0][0]
    goal =  [(x,y) for (x,y),v in grid.items() if v == '.' and y == grid.height-1][0]
    walls = set(k for k,v in grid.items() if v == '#')
    blizzards = {k:v for k,v in grid.items() if v in ('<','>','^','v')}
    lookup = {
        '<': (-1, 0),
        '>': (1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }
    grid.update({ k: '.' for k in blizzards })
    state = {start}
    seen = {frozenset(blizzards)}
    t = 0

    def get_blizz(time):
        r = set()
        for k,v in blizzards.items():
            for _ in range(time):
                k = tuple(sum(x) for x in zip(k, lookup[v]))
                if k in walls:
                    if v == '<':
                        k = (grid.width-2, k[1])
                    elif v == '>':
                        k = (1, k[1])
                    elif v == '^':
                        k = (k[0], grid.height-2)
                    elif v == 'v':
                        k = (k[0], 1)
            r.add(k)
        return r

    while goal not in state:
        t += 1
        b = set(get_blizz(t))
        n = set()
        for s in state:
            n |= set(grid.neighbors(s)) - b
        state = n

    return(t)


def part_2(p_Input):
    pass


example_input_1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""
challenge_input = Input('24')

assert(part_1(example_input_1) == 18)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
