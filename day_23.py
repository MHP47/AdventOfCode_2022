from utils import *

N4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
N8 = ((1, 1), (1, -1), (-1, 1), (-1, -1)) + N4

def part_1(p_Input):
    grid = defaultdict(lambda: '.', {(x, y): val for y, row in enumerate(p_Input.strip().splitlines()) for x, val in enumerate(row)})

    def north(x,y):
        if not any(
            grid[(x + dx, y + dy)]=="#"
            for dx,dy in ((-1,-1), (0,-1), (1,-1))
        ):
            return (x + 0, y + -1)
        return None

    def south(x,y):
        if not any(
            grid[(x + dx, y + dy)]=="#"
            for dx,dy in ((-1,1), (0,1), (1,1))
        ):
            return (x + 0, y + 1)
        return None

    def west(x,y):
        if not any(
            grid[(x + dx, y + dy)]=="#"
            for dx,dy in ((-1,-1), (-1,0), (-1,1))
        ):
            return (x + -1, y + 0)
        return None

    def east(x,y):
        if not any(
            grid[(x + dx, y + dy)]=="#"
            for dx,dy in ((1,-1), (1,0), (1,1))
        ):
            return (x + 1, y + 0)
        return None

    D = [north, south, west, east]

    for _ in range(10):
        a=[(x,y) for (x,y),z in grid.items() if z == '#']
        p = dict()
        for ex,ey in a:
            if not any(grid.get((ex + dx, ey + dy), '.')=="#" for dx,dy in N8):
                continue
            for d in D:
                if t := d(ex,ey):
                    if t not in p:
                        p[t] = (ex,ey)
                    else:
                        p[t] = None
                    break
        for k,v in p.items():
            if not v: continue
            grid[k] = '#'
            grid[v] = '.'
        D.append(D.pop(0))

    total = 0
    for y in range(min(y for (x,y),z in grid.items() if z == '#'), max(y for (x,y),z in grid.items() if z == '#')+1):
        for x in range(min(x for (x,y),z in grid.items() if z == '#'), max(x for (x,y),z in grid.items() if z == '#')+1):
            if grid[(x,y)] == '.': total +=1

    return total


def part_2(p_Input):
    pass


example_input_1 = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""
challenge_input = Input('23')

assert(part_1(example_input_1) == 110)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
