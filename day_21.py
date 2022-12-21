from utils import *
import sympy


def part_1(p_Input):
    def solve(a,e=None,b=None):
        if a == 'X' or a.isnumeric(): return a
        a = solve(*R[a])
        b = solve(*R[b])
        return f"({a}){e}({b})"

    R = { y: z.split() for x in p_Input.strip().splitlines() for (y,z) in [x.split(': ')] }
    return int(eval(solve(*R['root'])))


def part_2(p_Input):
    def solve(a,e=None,b=None):
        if a == 'X' or a.isnumeric(): return a
        a = solve(*R[a])
        b = solve(*R[b])
        return f"({a}){e}({b})"

    R = { y: z.split() for x in p_Input.strip().splitlines() for (y,z) in [x.split(': ')] }
    R['root'][1] = '-'
    R['humn'] = 'X'

    return sympy.solve(solve(*R['root']))[0]


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

assert(part_2(example_input_1) == 301)
print(f"Part 2: {part_2(challenge_input)}")
