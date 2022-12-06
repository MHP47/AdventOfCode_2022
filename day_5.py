from utils import *


def part_1(p_Input):
    starting_pos, steps = p_Input.split('\n\n')
    starting_pos = starting_pos.splitlines()
    stacks = parse_ints(starting_pos[-1])
    positions = [starting_pos[-1].index(x) for x in map(str, stacks)]
    crates = [None]
    for i in positions:
        crates.append(deque([x[i] for x in starting_pos[:-1] if x[i] != ' ']))

    for step in steps.splitlines():
        amount, crate_from, crate_to = parse_ints(step)
        for _ in range(amount):
            crates[crate_to].appendleft(crates[crate_from].popleft())

    return cat(x[0] for x in crates[1:])


def part_2(p_Input):
    starting_pos, steps = p_Input.split('\n\n')
    starting_pos = starting_pos.splitlines()
    stacks = parse_ints(starting_pos[-1])
    positions = [starting_pos[-1].index(x) for x in map(str, stacks)]
    crates = [None]
    for i in positions:
        crates.append(deque([x[i] for x in starting_pos[:-1] if x[i] != ' ']))

    for step in steps.splitlines():
        amount, crate_from, crate_to = parse_ints(step)
        for i in range(amount):
            crates[crate_to].insert(i, crates[crate_from].popleft())

    return cat(x[0] for x in crates[1:])


example_input_1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
challenge_input = Input('5')

assert(part_1(example_input_1) == 'CMZ')
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 'MCD')
print(f"Part 2: {part_2(challenge_input)}")
