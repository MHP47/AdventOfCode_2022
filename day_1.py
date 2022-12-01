from utils import *


def part_1(p_Input):
    elves = [sum(map(int, x.split('\n'))) for x in p_Input.strip().split('\n\n')]
    return max(elves)


def part_2(p_Input):
    elves = [sum(map(int, x.split('\n'))) for x in p_Input.strip().split('\n\n')]
    return sum(sorted(elves, reverse=True)[:3])


example_input_1 = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
challenge_input = Input('1')

assert(part_1(example_input_1) == 24000)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 45000)
print(f"Part 2: {part_2(challenge_input)}")
