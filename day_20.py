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
    decryption_key = 811589153
    class Num:
        def __init__(self, val, prev=None, nxt=None):
            self.value = val
            self.prev = prev
            self.nxt = nxt
        def __repr__(self):
            return str(self.value)

    Q = [Num(x * decryption_key) for x in map(int, p_Input.strip().splitlines())]
    for p,n in zip(Q, Q[1:]):
        p.nxt = n
        n.prev = p

    Q[-1].nxt = Q[0]
    Q[0].prev = Q[-1]

    for _ in range(10):
        for i in Q:
            i.prev.nxt = i.nxt
            i.nxt.prev = i.prev
            n, p = i.nxt, i.prev
            for _ in range(i.value%(len(Q)-1)):
                n = n.nxt
                p = p.nxt
            p.nxt = i
            i.prev = p
            n.prev = i
            i.nxt = n

    zero_index = p_Input.strip().splitlines().index('0')
    total = 0
    n = Q[zero_index]
    for _ in range(3):
        for _ in range(1000):
            n = n.nxt
        total += n.value
    return total


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

assert(part_2(example_input_1) == 1623178306)
print(f"Part 2: {part_2(challenge_input)}")
