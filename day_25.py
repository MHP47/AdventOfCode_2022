from utils import *


def part_1(p_Input):
    lookup = {
        "0": 0,
        "1": 1,
        "2": 2,
        "=": -2,
        "-": -1,
    }

    total = sum(
        [
            sum((5**i)*lookup[x]
            for i,x in enumerate(l[::-1]))
        for l in p_Input.strip().splitlines()
        ]
    )

    b = []
    n = [0]
    while total:
        total, x = divmod(total, 5)
        x += n.pop(0)
        if x > 2:
            x -= 5
            n.append(1)
        else:
            n.append(0)
        b.append(x)

    b.reverse()

    return cat([list(lookup)[n] for n in b])


example_input_1 = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""
challenge_input = Input('25')

assert(part_1(example_input_1) == '2=-1=0')
print(f"Part 1: {part_1(challenge_input)}")
