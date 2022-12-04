from utils import *


def part_1(p_Input):
    data = p_Input.strip().splitlines()
    count = 0
    for pairing in data:
        elf1_start, elf1_end, elf2_start, elf2_end = map(int, re.findall(r'\d+', pairing))
        if elf1_start <= elf2_start <= elf2_end <= elf1_end or \
            elf2_start <= elf1_start <= elf1_end <= elf2_end:
            count += 1
    return count


def part_2(p_Input):
    data = p_Input.strip().splitlines()
    count = 0
    for pairing in data:
        elf1_start, elf1_end, elf2_start, elf2_end = map(int, re.findall(r'\d+', pairing))
        if elf2_start in range(elf1_start, elf1_end + 1) or \
            elf1_end in range(elf2_start, elf2_end + 1) or \
            elf1_start in range(elf2_start, elf2_end + 1) or \
            elf2_end in range(elf1_start, elf1_end + 1):
            count += 1
    return count


example_input_1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
challenge_input = Input('4')

assert(part_1(example_input_1) == 2)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 4)
print(f"Part 2: {part_2(challenge_input)}")
