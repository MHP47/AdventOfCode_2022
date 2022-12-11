from utils import *
from parse import parse


def part_1(p_Input):
    data = p_Input.strip().split('\n\n')
    monkeys = dict()
    for m in data:
        n,items,op,tst,t,f = m.splitlines()
        n = parse_ints(n)[0]
        items = parse_ints(items)
        try:
            op_calc, op_val = parse("  Operation: new = old {} {:d}", op).fixed
        except AttributeError:
            op_calc = "**"
            op_val = 2
        tst  = parse("  Test: divisible by {:d}", tst).fixed[0]
        t = parse("    If true: throw to monkey {:d}", t).fixed[0]
        f = parse("    If false: throw to monkey {:d}", f).fixed[0]
        monkeys[n] = {'items': deque(items), 'op': [op_calc, op_val], 'test': tst, 'True': t, 'False': f, 'count': 0}

    for _ in range(20):
        for m in monkeys:
            while monkeys[m]['items']:
                item = monkeys[m]['items'].popleft()
                w = eval(f"{item} {monkeys[m]['op'][0]} {monkeys[m]['op'][1]}")
                w //= 3
                _, t = divmod(w, monkeys[m]['test'])
                monkeys[monkeys[m][str(t == 0)]]['items'].append(w)
                monkeys[m]['count'] += 1

    return mul_reduce(sorted([v['count'] for k,v in monkeys.items()])[-2:])


def part_2(p_Input):
    pass


example_input_1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
challenge_input = Input('11')

assert(part_1(example_input_1) == 10605)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
