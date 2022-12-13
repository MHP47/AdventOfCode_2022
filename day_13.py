from utils import *


def _comp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a == b:
            return None
        else:
            return False
    elif isinstance(a, list) and isinstance(b, list):
        if a and not b: return False
        if b and not a: return True
        while a and b:
            c = a.pop(0)
            d = b.pop(0)
            t = _comp(c,d)
            if t is None: continue
            if not t:
                return False
            else:
                return True
        if a or b:
            return _comp(a, b)
        return True
    else:
        if isinstance(a, int): a = [a]
        if isinstance(b, int): b = [b]
        return _comp(a, b)


def part_1(p_Input):
    idx_in_order = []
    for i,x in enumerate(p_Input.strip().split('\n\n'), 1):
        a,b = x.split()
        if _comp(eval(a), eval(b)): idx_in_order.append(i)
    return sum(idx_in_order)


def part_2(p_Input):
    pass


example_input_1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
challenge_input = Input('13')

assert(part_1(example_input_1) == 13)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
