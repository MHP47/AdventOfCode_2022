from utils import *


def part_1(p_Input):
    data = p_Input.split('\n')
    # A - Rock
    # B - Paper
    # C - Scissors
    # X - Rock
    # Y - Paper
    # Z - Scissors
    # Win - 6
    # Draw - 3
    # Loss - 0
    # Points for picking type + points for win/draw/loss
    combo_lookup = {
        "A X": 1+3,
        "A Y": 2+6,
        "A Z": 3+0,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 1+6,
        "C Y": 2+0,
        "C Z": 3+3,
        '': 0
    }
    return sum(combo_lookup[x] for x in data)


def part_2(p_Input):
    pass


example_input_1 = '''A Y
B X
C Z'''
challenge_input = Input('2')

assert(part_1(example_input_1) == 15)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
