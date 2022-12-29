from utils import *
from operator import sub


def part_1(p_Input):
    grid = {(x, y): val for y, row in enumerate(p_Input.strip().splitlines()) for x, val in enumerate(row)}
    start = [(x,y) for (x,y),v in grid.items() if v == '.' and y == 0][0]
    goal =  [(x,y) for (x,y),v in grid.items() if v == '.' and y == max(y for x, y in grid)][0]
    grid[(start[0], start[1]-1)] = '#'
    grid[(goal[0], goal[1]+1)] = '#'
    walls = set(k for k,v in grid.items() if v == '#')

    class Blizzard:
        lookup = {
            '<': (-1, 0),
            '>': (1, 0),
            '^': (0, -1),
            'v': (0, 1),
        }
        def __init__(self, start_pos, dir) -> None:
            self.dir = self.lookup[dir]
            self.cycle = [start_pos]
            while True:
                start_pos = tuple(sum(x) for x in zip(start_pos, self.dir))
                if start_pos in walls: break
                self.cycle.append(start_pos)
            while True:
                start_pos = tuple(sub(*x) for x in zip(start_pos, self.dir))
                if start_pos in walls: break
            while True:
                start_pos = tuple(sum(x) for x in zip(start_pos, self.dir))
                if start_pos in self.cycle: break
                self.cycle.append(start_pos)
        def new_pos(self):
            for i in itertools.islice(itertools.cycle(self.cycle), 1, None):
                yield i

    blizzards = [Blizzard(k,v).new_pos() for k,v in grid.items() if v in ('<','>','^','v')]
    state = {start}
    t = 0

    while goal not in state:
        t += 1
        b = set(next(x) for x in blizzards)
        n = set()
        for s in state:
            n.update(set(neighbors4(s)) - walls - b)
            if s not in b:
                n.add(s)
        state = n

    return(t)


def part_2(p_Input):
    grid = {(x, y): val for y, row in enumerate(p_Input.strip().splitlines()) for x, val in enumerate(row)}
    start = [(x,y) for (x,y),v in grid.items() if v == '.' and y == 0][0]
    goal =  [(x,y) for (x,y),v in grid.items() if v == '.' and y == max(y for x, y in grid)][0]
    grid[(start[0], start[1]-1)] = '#'
    grid[(goal[0], goal[1]+1)] = '#'
    walls = set(k for k,v in grid.items() if v == '#')

    class Blizzard:
        lookup = {
            '<': (-1, 0),
            '>': (1, 0),
            '^': (0, -1),
            'v': (0, 1),
        }
        def __init__(self, start_pos, dir) -> None:
            self.dir = self.lookup[dir]
            self.cycle = [start_pos]
            while True:
                start_pos = tuple(sum(x) for x in zip(start_pos, self.dir))
                if start_pos in walls: break
                self.cycle.append(start_pos)
            while True:
                start_pos = tuple(sub(*x) for x in zip(start_pos, self.dir))
                if start_pos in walls: break
            while True:
                start_pos = tuple(sum(x) for x in zip(start_pos, self.dir))
                if start_pos in self.cycle: break
                self.cycle.append(start_pos)
        def new_pos(self):
            for i in itertools.islice(itertools.cycle(self.cycle), 1, None):
                yield i

    blizzards = [Blizzard(k,v).new_pos() for k,v in grid.items() if v in ('<','>','^','v')]
    t = 0

    for _ in range(3):
        state = {start}
        while goal not in state:
            t += 1
            b = set(next(x) for x in blizzards)
            n = set()
            for s in state:
                n.update(set(neighbors4(s)) - walls - b)
                if s not in b:
                    n.add(s)
            state = n
        start, goal = goal, start

    return t


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

assert(part_2(example_input_1) == 54)
print(f"Part 2: {part_2(challenge_input)}")
