from utils import *


def part_1(p_Input):
    data = p_Input.strip()
    pos, marker = [(4+i,data[i:i+4]) for i in range(0, len(data)-4) if len(set(data[i:i+4]))==4][0]
    return pos


def part_2(p_Input):
    pass


example_input_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
example_input_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example_input_3 = "nppdvjthqldpwncqszvftbrmjlhg"
example_input_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example_input_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
challenge_input = Input('6')

assert(part_1(example_input_1) == 7)
assert(part_1(example_input_2) == 5)
assert(part_1(example_input_3) == 6)
assert(part_1(example_input_4) == 10)
assert(part_1(example_input_5) == 11)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
