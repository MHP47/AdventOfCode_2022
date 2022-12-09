from utils import *


def part_1(p_Input):
    moves = p_Input.strip().splitlines()
    H = T = (0,0)
    directions = {"R": (0,1), "U": (1,0), "L": (0,-1), "D": (-1,0)}
    tail_visited = set()
    tail_visited.add(T)

    for dir,step in [x.split() for x in moves]:
        for _ in range(int(step)):
            H = (X(H)+X(directions[dir]), Y(H)+Y(directions[dir]))
            if X(H) == X(T) or Y(H) == Y(T):
                if cityblock_distance(H, T) >= 2: T = (X(T)+X(directions[dir]), Y(T)+Y(directions[dir]))
            else:
                if cityblock_distance(H, T) > 2:
                    if X(H) in (X(T)-1, X(T)+1):
                        T = (X(H), Y(T)+Y(directions[dir]))
                    elif Y(H) in (Y(T)-1, Y(T)+1):
                        T = (X(T)+X(directions[dir]), Y(H))
            tail_visited.add(T)

    return len(tail_visited)


def part_2(p_Input):
    pass


example_input_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
challenge_input = Input('9')

assert(part_1(example_input_1) == 13)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
