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
    def common(*args):
        a = set(alphabet+alphabet.upper())
        for n in args:
            a = a.intersection(set(n))
        return a.pop()
    groupings = p_Input.strip().splitlines()
    groupings = [groupings[i:i+3] for i in range(0, len(groupings), 3)]
    total = 0
    for grp in groupings:
        c = common(*grp)
        total += item_lookup[c]
    return total


example_input_1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
challenge_input = Input('3')

assert(part_1(example_input_1) == 157)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 70)
print(f"Part 2: {part_2(challenge_input)}")
