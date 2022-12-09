from utils import *

def point_add(p1, p2):
    return (X(p1)+X(p2), Y(p1)+Y(p2))


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
    moves = p_Input.strip().splitlines()
    H = T = (0,0)
    rope = [(0,0)] * 10
    directions = {"R": (0,1), "U": (1,0), "L": (0,-1), "D": (-1,0)}
    tail_visited = set()
    tail_visited.add(rope[-1])

    for dir,step in [x.split() for x in moves]:
        for _ in range(int(step)):
            H = rope[0]
            H = (X(H)+X(directions[dir]), Y(H)+Y(directions[dir]))
            rope[0] = H
            for i in range(1, len(rope)):
                T = rope[i]
                if H in neighbors8(T) or H == T:
                    pass
                else:
                    if X(H) == X(T):
                        T = point_add(T, directions["R"]if Y(H) > Y(T) else directions["L"])
                    elif Y(H) == Y(T):
                        T = point_add(T, directions["U"]if X(H) > X(T) else directions["D"])
                    elif X(H) > X(T):
                        if Y(H) > Y(T):
                            T = point_add(T, (1,1))
                        else:
                            T = point_add(T, (1,-1))
                    elif X(H) < X(T):
                        if Y(H) > Y(T):
                            T = point_add(T, (-1,1))
                        else:
                            T = point_add(T, (-1,-1))
                rope[i] = T
                H = T
            tail_visited.add(rope[-1])

    return len(tail_visited)


example_input_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
example_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
challenge_input = Input('9')

assert(part_1(example_input_1) == 13)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 1)
assert(part_2(example_input_2) == 36)
print(f"Part 2: {part_2(challenge_input)}")
