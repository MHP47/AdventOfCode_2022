from utils import *


def part_1(p_Input):
    commands = deque(p_Input.strip().splitlines())
    if commands[0] == "$ cd /": _ = commands.popleft()

    path = ['']
    dirs = {}
    tree = defaultdict(list)

    while commands:
        cmd = commands.popleft()
        if cmd.startswith('$ cd'):
            if cmd.endswith('..'):
                path = path[:-1]
            else:
                path.append(cmd.split(' ')[-1])
        elif cmd.startswith('$ ls'):
            while commands and not commands[0].startswith('$'):
                tree['/'.join(path)].append(commands.popleft())

    N = deque(tree)

    while N:
        n = N.popleft()
        if not any([x.startswith('dir') for x in tree[n]]):
            dirs[n] = str(sum(map(int, [x.split()[0] for x in tree[n]])))
        else:
            tree[n] = flatten([[dirs.get('/'.join((n,x.split()[-1])), x)] for x in tree[n]])
            N.append(n)

    return sum(map(int, [x for x in dirs.values() if int(x) <= 100000]))


def part_2(p_Input):
    pass


example_input_1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
challenge_input = Input('7')

assert(part_1(example_input_1) == 95437)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
