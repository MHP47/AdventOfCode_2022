from utils import *


N4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
N8 = ((1, 1), (1, -1), (-1, 1), (-1, -1)) + N4

class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""
    def __init__(self, mapping=(), rows=(), neighbors=N4):
        """Initialize with, e.g., either `mapping={(0, 0): 1, (1, 0): 2, ...}`,
        or `rows=[(1, 2, 3), (4, 5, 6)].
        `neighbors` is a collection of (dx, dy) deltas to neighboring points.`"""
        self.update(mapping if mapping else
            {(x, y): int(val)
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
                print(self[(x,y)], end='')
            print()
        print()


def get_row(grid, point):
    return [grid[(i, Y(point))] for i in range(grid.width)]


def get_column(grid, point):
    return [grid[(X(point), i)] for i in range(grid.height)]


def part_1(p_Input):
    rows = p_Input.strip().splitlines()
    grid = Grid(rows = rows)
    count = 0
    for point in grid:
        row = get_row(grid, point)
        west, east = row[:X(point)], row[X(point)+1:]
        column = get_column(grid, point)
        north, south = column[:Y(point)], column[Y(point)+1:]
        count += any(all(grid[point] > z for z in y) for y in (south, east, north, west))
    return count

def part_2(p_Input):
    pass


example_input_1 = """30373
25512
65332
33549
35390
"""
challenge_input = Input('8')

assert(part_1(example_input_1) == 21)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
