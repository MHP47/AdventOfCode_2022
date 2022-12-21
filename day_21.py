from utils import *
import sympy


def part_1(p_Input):
    a = [[x.split(': ')[0]] + x.split(': ')[1].split() for x in p_Input.strip().splitlines()]
    b = deque(a)
    d = dict()

    while b:
        i = b.popleft()
        if len(i) == 2:
            d[i[0]] = int(i[1])
            continue
        if i[1] in d and i[3] in d:
            d[i[0]] = eval(f"{d[i[1]]}{i[2]}{d[i[3]]}")
        else:
            b.append(i)

    return int(d['root'])


def part_2(p_Input):
    pass


example_input_1 = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""
challenge_input = Input('21')

assert(part_1(example_input_1) == 152)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
