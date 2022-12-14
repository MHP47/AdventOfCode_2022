from utils import *


def falldown(point):
    yield (X(point), Y(point)+1)
    yield (X(point)-1, Y(point)+1)
    yield (X(point)+1, Y(point)+1)


def part_1(p_Input):
    rocks = set()
    for l in p_Input.strip().splitlines():
        e = chunks(parse_ints(l),2)
        a = next(e)
        for i in e:
            if a[0] == i[0]:
                for n in range(min(a[1], i[1]), max(a[1], i[1])+1):
                    rocks.add((a[0],n))
            else:
                for n in range(min(a[0], i[0]), max(a[0], i[0])+1):
                    rocks.add((n,a[1]))
            a=i

    width_min  = min(rocks, key=lambda x: x[0])[0]
    width_max  = max(rocks, key=lambda x: x[0])[0] +1
    height_min = min(0, min(rocks, key=lambda x: x[1])[1])
    height_max = max(rocks, key=lambda x: x[1])[1] +1

    grid = {(x,y): 1 if (x,y) in rocks else 0
        for y in range(height_min, height_max)
        for x in range(width_min, width_max)
    }

    try:
        while True:
            s=(500,0)
            while True:
                for n in falldown(s):
                    if not grid[n]:
                        s = n
                        break
                else:
                    if grid[s] == 2:
                        break
                    else:
                        grid[s] = 2
    except KeyError:
        pass

    return(sum(1 for x in grid.values() if x == 2))


def part_2(p_Input):
    rocks = set()
    for l in p_Input.strip().splitlines():
        e = chunks(parse_ints(l),2)
        a = next(e)
        for i in e:
            if a[0] == i[0]:
                for n in range(min(a[1], i[1]), max(a[1], i[1])+1):
                    rocks.add((a[0],n))
            else:
                for n in range(min(a[0], i[0]), max(a[0], i[0])+1):
                    rocks.add((n,a[1]))
            a=i

    width_min  = min(rocks, key=lambda x: x[0])[0]
    width_max  = max(rocks, key=lambda x: x[0])[0] +1
    height_min = min(0, min(rocks, key=lambda x: x[1])[1])
    height_max = max(rocks, key=lambda x: x[1])[1] +1

    grid = {(x,y): 1 if (x,y) in rocks else 0
        for y in range(height_min, height_max)
        for x in range(width_min, width_max)
    }

    for x in range(width_min, width_max): grid[(x,height_max)] = 0
    height_max+=1
    for x in range(500-height_max-1, 500+height_max+2): grid[(x,height_max)] = 1

    width_min = min(grid, key=lambda x: x[0])[0]
    width_max = max(grid, key=lambda x: x[0])[0]

    while True:
        s=(500,0)
        if grid.get(s, 0) == 2:
            break
        while True:
            for n in falldown(s):
                if not grid.get(n, 0):
                    s = n
                    break
            else:
                if grid.get(s, 0) == 2:
                    break
                else:
                    grid[s] = 2

    return(sum(1 for x in grid.values() if x == 2))


example_input_1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
challenge_input = Input('14')

assert(part_1(example_input_1) == 24)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 93)
print(f"Part 2: {part_2(challenge_input)}")
