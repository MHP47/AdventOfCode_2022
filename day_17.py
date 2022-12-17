from utils import *


def part_1(p_Input):
    rocks = itertools.cycle(
    [
        [(2, 0), (3, 0), (4, 0), (5, 0)], # Horizontal Line
        [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)], # Plus
        [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)], # L
        [(2, 0), (2, 1), (2, 2), (2, 3)], # Vertical Bar
        [(2, 0), (2, 1), (3, 0), (3, 1)], # Square
    ])
    jet_pattern = itertools.cycle(p_Input.strip())
    directions={'>': 1, '<': -1}
    chamber = {(x,0) for x in range(7)}

    for i in range(2022):
        vertical_height = max(y for x,y in chamber) + 4
        rock = [(x, y+vertical_height) for x,y in next(rocks)]
        while True:
            jet = directions[next(jet_pattern)]
            rock_step = [(x+jet, y) for x,y in rock]
            if not all(0<=x<7 for x, y in rock_step) \
                or any(p in chamber for p in rock_step):
                rock_step = rock
            rock = rock_step
            rock_down = [(x, y-1) for x,y in rock]
            if any(p in chamber for p in rock_down):
                chamber.update(rock)
                break
            rock = rock_down
    
    return max(y for x,y in chamber)


def part_2(p_Input):
    pass


example_input_1 = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
challenge_input = Input('17')

assert(part_1(example_input_1) == 3068)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
