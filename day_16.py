from utils import *
from parse import parse
import functools


def part_1(p_Input):
    valves = set()
    flows = dict()
    connections = dict()

    p1="Valve {} has flow rate={:d}; tunnels lead to valves {}"
    p2="Valve {} has flow rate={:d}; tunnel leads to valve {}"

    for x,y,z in [parse(p1,a) or parse(p2,a) for a in p_Input.strip().splitlines()]:
        valves.add(x)
        if y>0: flows[x]=y
        for a in z.split(', '): connections[x,a] = 1

    # https://favtutor.com/blogs/floyd-warshall-algorithm
    graph = [[connections.get((v,z), BIG) if v != z else 0 for z in sorted(valves) ] for v in sorted(valves) ]

    for r in range(len(valves)):
        for p in range(len(valves)):
            for q in range(len(valves)):
                graph[p][q] = min(graph[p][q], graph[p][r] + graph[r][q])

    shortest_path = defaultdict(lambda: dict())
    for v,paths in zip(sorted(valves), graph):
        for dest,cost in zip(sorted(valves), paths):
            if flow:=flows.get(dest, 0) > 0 and cost > 0:
                shortest_path[v][dest] = cost

    checks = deque([(['AA'], 0, 30)])
    done = []
    while checks:
        v,p,t = checks.popleft()
        if t<=0:
            done.append((v,p,t))
            continue
        found=False
        for a,b in shortest_path[v[-1]].items():
            if t-b-1 < 0: continue
            if a not in v:
                checks.append((v + [a], p+(t-b-1)*flows[a], t-b-1))
                found=True
        if not found:
            done.append((v,p,t))

    return max(done, key=lambda x: x[1])[1]


def part_2(p_Input):
    valves = set()
    flows = dict()
    connections = dict()

    p1="Valve {} has flow rate={:d}; tunnels lead to valves {}"
    p2="Valve {} has flow rate={:d}; tunnel leads to valve {}"

    for x,y,z in [parse(p1,a) or parse(p2,a) for a in p_Input.strip().splitlines()]:
        valves.add(x)
        if y>0: flows[x]=y
        for a in z.split(', '): connections[x,a] = 1

    # https://favtutor.com/blogs/floyd-warshall-algorithm
    graph = [[connections.get((v,z), BIG) if v != z else 0 for z in sorted(valves) ] for v in sorted(valves) ]

    for r in range(len(valves)):
        for p in range(len(valves)):
            for q in range(len(valves)):
                graph[p][q] = min(graph[p][q], graph[p][r] + graph[r][q])

    shortest_path = defaultdict(lambda: dict())
    for v,paths in zip(sorted(valves), graph):
        for dest,cost in zip(sorted(valves), paths):
            if flow:=flows.get(dest, 0) > 0 and cost > 0:
                shortest_path[v][dest] = cost

    @functools.lru_cache(maxsize=None)
    def solve(visited, time_remaining):
        checks = deque([(visited, 0, time_remaining)])
        done = []
        while checks:
            v,p,t = checks.popleft()
            if t<=0:
                done.append((v,p,t))
                continue
            found=False
            for a,b in shortest_path[v[-1]].items():
                if t-b-1 < 0: continue
                if a not in v:
                    checks.append((v + (a,), p+(t-b-1)*flows[a], t-b-1))
                    found=True
            if not found:
                done.append((v,p,t))
        return max(done, key=lambda x: x[1])

    checks = deque([(('AA',), 0, 26)])
    done = []
    while checks:
        v,p,t = checks.popleft()
        if t<=0:
            done.append(p)
            continue
        found=False
        for a,b in shortest_path[v[-1]].items():
            if t-b-1 < 0: continue
            if a not in v:
                checks.append((v + (a,), p+(t-b-1)*flows[a], t-b-1))
                done.append(p+(t-b-1)*flows[a] + solve(v + (a,) + ('AA',), 26)[1])
                found=True
        if not found:
            done.append(p)

    return max(done)


example_input_1 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
challenge_input = Input('16')

assert(part_1(example_input_1) == 1651)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 1707)
print(f"Part 2: {part_2(challenge_input)}")
