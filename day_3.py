from utils import *

def half_string(s):
    return s[:len(s)//2], s[len(s)//2:]


item_lookup = dict((b,a) for a,b in enumerate(alphabet + alphabet.upper(), 1))


def part_1(p_Input):
    elves = p_Input.strip().splitlines()
    total = 0
    for rucksack in elves:
        h1,h2 = half_string(rucksack)
        total += sum([item_lookup[i] for i in set(h1) if i in set(h2)])
    return total

def part_2(p_Input):
    pass


example_input_1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
challenge_input = Input('3')

assert(part_1(example_input_1) == 157)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
