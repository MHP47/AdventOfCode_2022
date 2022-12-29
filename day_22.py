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
                print(self.get((x,y), ' '), end='')
            print()
        print()


def part_1(p_Input):
    a,b = p_Input.split('\n\n')
    grid = Grid(rows=a.splitlines())
    b = [int(x) if x.isnumeric() else x for x in re.split(r'(\d+)',b.strip()) if x]

    start = (min(x for (x,y),z in grid.items() if y == 0 and z == '.'), 0)
    H = [(1,0),(0,1),(-1,0),(0,-1)]
    h = 0

    for i in b:
        if isinstance(i, int):
            for _ in range(i):
                t = ((start[0] + H[h][0]) % grid.width, (start[1] + H[h][1]) % grid.height)
                while grid.get(t, ' ') == ' ':
                    t = ((t[0] + H[h][0]) % grid.width, (t[1] + H[h][1]) % grid.height)
                if grid.get(t, ' ') == '.':
                    start = t
                elif grid.get(t, ' ') == '#':
                    break
                else:
                    raise
        else:
            h += {'L': -1, 'R': 1}[i]
            h %= len(H)

    c,r = start
    c+=1
    r+=1
    return(r*1000+c*4+h)


def part_2(p_Input):
    a,b = p_Input.split('\n\n')
    grid = Grid(rows=a.splitlines())
    b = [int(x) if x.isnumeric() else x for x in re.split(r'(\d+)',b.strip()) if x]

    start = (min(x for (x,y),z in grid.items() if y == 0 and z == '.'), 0)
    H = [(1,0),(0,1),(-1,0),(0,-1)]
    h = 0

    for i in b:
        if isinstance(i, int):
            for _ in range(i):
                x,y = ((start[0] + H[h][0]), (start[1] + H[h][1]))
                if y < 0:
                    # Gone off top of 5 or 6
                    if x in range(50,100):
                        # 5
                        # Left side of 1
                        dx,dy = 0, x+100
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 0
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    else:
                        # 6
                        # Bottom of 1
                        dx,dy = x-100, 199
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                elif y > 199:
                    # Off bottom of 1
                    # Top of 6
                    dx,dy = x+100, 0
                    if grid.get((dx,dy), ' ') == '.':
                        start = (dx,dy)
                    elif grid.get((dx,dy), ' ') == '#':
                        break
                elif 0<=y<50:
                    # 5/6
                    if x < 50:
                        # Off left of 5
                        # left of 2
                        dx, dy = 0, 149-y
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 0
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    elif x > 149:
                        # Off right of 6
                        # right of 3
                        dx, dy = 99, 149-y
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 2
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    else:
                        if grid.get((x,y), ' ') == '.':
                            start = (x,y)
                        elif grid.get((x,y), ' ') == '#':
                            break
                elif 50<=y<100:
                    # 4
                    if x < 50:
                        if h == 2:
                            # Off left of 4
                            # top of 2
                            dx, dy = y-50, 100
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 1
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                        else:
                            # Off top of 2
                            # left of 4
                            dx, dy = 50, x+50
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 0
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                    elif x > 99:
                        if h == 0:
                            # Off right of 4
                            # bottom of 6
                            dx, dy = y+50, 49
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 3
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                        else:
                            # Off bottom 6
                            # right of 4
                            dx, dy = 99, x-50
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 2
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                    else:
                        if grid.get((x,y), ' ') == '.':
                            start = (x,y)
                        elif grid.get((x,y), ' ') == '#':
                            break
                elif 100<=y<150:
                    # 2/3
                    if x < 0:
                        # Off left of 2
                        # left of 5
                        dx, dy = 50, 149-y
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 0
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    elif x > 99:
                        # Off right of 3
                        # right of 6
                        dx, dy = 149, 149-y
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 2
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    else:
                        if grid.get((x,y), ' ') == '.':
                            start = (x,y)
                        elif grid.get((x,y), ' ') == '#':
                            break
                elif 150<=y<200:
                    # 1
                    if x < 0:
                        # Off left of 1
                        # top of 5
                        dx, dy = y-100, 0
                        if grid.get((dx,dy), ' ') == '.':
                            start = (dx,dy)
                            h = 1
                        elif grid.get((dx,dy), ' ') == '#':
                            break
                    elif x > 49:
                        if h == 0:
                            # Off right of 1
                            # bottom of 3
                            dx, dy = y-100, 149
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 3
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                        else:
                            # Off bottom 3
                            # Right of 1
                            dx, dy = 49, x+100
                            if grid.get((dx,dy), ' ') == '.':
                                start = (dx,dy)
                                h = 2
                            elif grid.get((dx,dy), ' ') == '#':
                                break
                    else:
                        if grid.get((x,y), ' ') == '.':
                            start = (x,y)
                        elif grid.get((x,y), ' ') == '#':
                            break
        else:
            h += {'L': -1, 'R': 1}[i]
            h %= len(H)

    c,r = start
    c+=1
    r+=1
    return(r*1000+c*4+h)


example_input_1 = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
challenge_input = Input('22')

assert(part_1(example_input_1) == 6032)
print(f"Part 1: {part_1(challenge_input)}")

# assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
