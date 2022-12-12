from utils import *

class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""
    def __init__(self, mapping=(), rows=(), neighbors=((0, 1), (1, 0), (0, -1), (-1, 0))):
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
    def copy(self): return Grid(self, neighbors=self.deltas)
    def neighbors(self, point):
        """Points on the grid that neighbor `point`."""
        x, y = point
        return [(x+dx, y+dy) for (dx, dy) in self.deltas
            if (x+dx, y+dy) in self]
    def to_rows(self):
        """The contents of the grid in a rectangular list of lists."""
        return [[self[x, y] for x in range(self.width)]
            for y in range(self.height)]
    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print("{:^4}".format(str(self[(x,y)])), end='')
            print()
        print()
    def find(self, s):
        return [k for k,v in self.items() if v == s]


def part_1(p_Input):
    grid = Grid(rows=[[F"S{alphabet}E".index(x) for x in y] for y in p_Input.strip().splitlines()])
    start = grid.find(0)[0]
    goal = grid.find(27)[0]
    grid[start] = 1
    grid[goal] = 26

    def h_func(x):
        return cityblock_distance(x, goal)

    def moves_func(s):
        return [y for y in grid.neighbors(s) if grid[y]<=grid[s]+1]

    return len(astar_search(start, h_func, moves_func))-1


def part_2(p_Input):
    pass


example_input_1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
challenge_input = Input('12')

assert(part_1(example_input_1) == 31)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
