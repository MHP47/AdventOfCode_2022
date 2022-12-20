from utils import *


def part_1(p_Input):
    L = [(x, False) for x in map(int, p_Input.strip().splitlines())]

    while not all(y for x,y in L):
        i = 0
        while i < len(L):
            if L[i][1]:
                i += 1
            else:
                t = L.pop(i)
                idx = i + t[0]
                if idx == 0:
                    L.append((t[0], True))
                else:
                    idx %= len(L)
                    L.insert(idx, (t[0], True))
                if idx < i:
                    i -= 1

    q = [x for x,y in L]
    z = q.index(0)
    return sum((q[(z+1000)%len(L)], q[(z+2000)%len(L)], q[(z+3000)%len(L)]))


def part_2(p_Input):
    pass


example_input_1 = """1
2
-3
3
-2
0
4
"""
challenge_input = Input('20')

assert(part_1(example_input_1) == 3)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
