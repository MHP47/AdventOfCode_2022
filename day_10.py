from utils import *


def part_1(p_Input):
    data = p_Input.strip().splitlines()
    signals = [0, 1]
    val = 1
    for command in data:
        signals.append(val)
        if command != "noop":
            _, a = command.split()
            val += int(a)
            signals.append(val)

    return sum(signals[i]*i for i in (20, 60, 100, 140, 180, 220))


def part_2(p_Input):
    crt = []
    cmds = deque(p_Input.strip().splitlines())
    x = [0,1,2]

    while cmds:
        c = cmds.popleft()
        crt.append('#' if len(crt)%40 in x else '.')
        if 'addx' in c:
            crt.append('#' if len(crt)%40 in x else '.')
            _,a = c.split()
            x = [y+int(a) for y in x]

    return '\n'.join([cat(n) for n in chunks(crt,40)])


example_input_1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
challenge_input = Input('10')

assert(part_1(example_input_1) == 13140)
print(f"Part 1: {part_1(challenge_input)}")

part_2_example_answer = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

assert(part_2(example_input_1) == part_2_example_answer)
print(f"Part 2: \n{part_2(challenge_input).replace('.', ' ')}")
