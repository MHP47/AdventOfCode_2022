from utils import *
from operator import add, sub
from parse import parse


p = 'Blueprint {:d}: Each ore robot costs {ore} ore. Each clay robot costs {clay} ore. Each obsidian robot costs {obs_ore} ore and {obs_clay} clay. Each geode robot costs {geode_ore} ore and {geode_obs} obsidian.'

class Blueprint:
    def __init__(self, ore, clay, obs_ore, obs_clay, geode_ore, geode_obs):
        self.ore_robot_cost = int(ore)
        self.clay_robot_cost = int(clay)
        self.obsidian_robot_cost = (int(obs_ore), int(obs_clay))
        self.geode_robot_cost = (int(geode_ore), int(geode_obs))
    @classmethod
    def fromchunk(cls, chunk):
        parsed = parse(p, chunk).named
        return cls(**parsed)


def part_1(p_Input):
    # Through trial and error; mostly error, like, a shitload of error, it seems there's only enough time to make 0 or 1
    # bot per round. So assumption is to not try to make multiple bots
    total = 0
    for i,l in enumerate(p_Input.strip().splitlines(), 1):
        bot = Blueprint.fromchunk(l)
        # ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time
        initial = (0, 0, 0, 0, 1, 0, 0, 0, 24)
        Q = deque([initial])
        seen = set() # state lookup
        best = 0
        # Max ore needed per round to make most expensive bot
        max_ore_cost = max(bot.geode_robot_cost[0], bot.obsidian_robot_cost[0], bot.clay_robot_cost, bot.ore_robot_cost)
        while Q:
            ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time = Q.popleft()
            best = max(best, geode)
            if time == 0: continue
            
            # Reduce the search space to get the seen lookup scope smaller
            # Ore never needs to be more than max_ore_cost * number_of_rounds_left
            ore = min(ore, max_ore_cost + (max_ore_cost - ore_robot) * (time - 1))
            # Similarly, clay never needs to be more than obsidian_bot_clay_cost * number_of_rounds_left
            clay = min(clay, bot.obsidian_robot_cost[1] + (bot.obsidian_robot_cost[1] - clay_robot) * (time - 1))
            # Same for obsidian, don't need more than enough to create a geode bot evey round
            obsidian = min(obsidian, bot.geode_robot_cost[1] + (bot.geode_robot_cost[1] - obsidian_robot) * (time - 1))
            
            state = (ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time)
            if state in seen: continue
            seen.add(state)
            
            # Add doing nothing
            Q.append((
                ore + ore_robot,
                clay + clay_robot,
                obsidian + obsidian_robot,
                geode + geode_robot,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                time - 1
            ))
            # Don't make more ore robots than the cost of the most expensive robot
            # i.e. if the most expensive bot costs 4 ore, don't need 5 ore bots
            if ore_robot < max_ore_cost and ore >= bot.ore_robot_cost:
                Q.append((
                    ore + ore_robot - bot.ore_robot_cost,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot + 1,
                    clay_robot,
                    obsidian_robot,
                    geode_robot,
                    time - 1
                ))
            # Build a clay robot if not at the max
            if clay_robot < bot.obsidian_robot_cost[1] and ore >= bot.clay_robot_cost:
                Q.append((
                    ore + ore_robot - bot.clay_robot_cost,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot + 1,
                    obsidian_robot,
                    geode_robot,
                    time - 1
                ))
            # Build obsidian robot if not at the max
            if obsidian_robot < bot.geode_robot_cost[1] and ore >= bot.obsidian_robot_cost[0] and clay >= bot.obsidian_robot_cost[1]:
                Q.append((
                    ore + ore_robot - bot.obsidian_robot_cost[0],
                    clay + clay_robot - bot.obsidian_robot_cost[1],
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot + 1,
                    geode_robot,
                    time - 1
                ))
            # Always build geode robot if able
            if ore >= bot.geode_robot_cost[0] and obsidian >= bot.geode_robot_cost[1]:
                Q.append((
                    ore + ore_robot - bot.geode_robot_cost[0],
                    clay + clay_robot,
                    obsidian + obsidian_robot - bot.geode_robot_cost[1],
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot,
                    geode_robot + 1,
                    time - 1
                ))

        total += i * best

    return total


def part_2(p_Input):
    # bot per round. So assumption is to not try to make multiple bots
    total = 1
    for i,l in enumerate(p_Input.strip().splitlines()[:3], 1):
        bot = Blueprint.fromchunk(l)
        # ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time
        initial = (0, 0, 0, 0, 1, 0, 0, 0, 32)
        Q = deque([initial])
        seen = set() # state lookup
        best = 0
        # Max ore needed per round to make most expensive bot
        max_ore_cost = max(bot.geode_robot_cost[0], bot.obsidian_robot_cost[0], bot.clay_robot_cost, bot.ore_robot_cost)
        while Q:
            ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time = Q.popleft()
            best = max(best, geode)
            if time == 0: continue
            
            # Reduce the search space to get the seen lookup scope smaller
            # Ore never needs to be more than max_ore_cost * number_of_rounds_left
            ore = min(ore, max_ore_cost + (max_ore_cost - ore_robot) * (time - 1))
            # Similarly, clay never needs to be more than obsidian_bot_clay_cost * number_of_rounds_left
            clay = min(clay, bot.obsidian_robot_cost[1] + (bot.obsidian_robot_cost[1] - clay_robot) * (time - 1))
            # Same for obsidian, don't need more than enough to create a geode bot evey round
            obsidian = min(obsidian, bot.geode_robot_cost[1] + (bot.geode_robot_cost[1] - obsidian_robot) * (time - 1))
            
            state = (ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot, time)
            if state in seen: continue
            seen.add(state)
            
            # Add doing nothing
            Q.append((
                ore + ore_robot,
                clay + clay_robot,
                obsidian + obsidian_robot,
                geode + geode_robot,
                ore_robot,
                clay_robot,
                obsidian_robot,
                geode_robot,
                time - 1
            ))
            # Don't make more ore robots than the cost of the most expensive robot
            # i.e. if the most expensive bot costs 4 ore, don't need 5 ore bots
            if ore_robot < max_ore_cost and ore >= bot.ore_robot_cost:
                Q.append((
                    ore + ore_robot - bot.ore_robot_cost,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot + 1,
                    clay_robot,
                    obsidian_robot,
                    geode_robot,
                    time - 1
                ))
            # Build a clay robot if not at the max
            if clay_robot < bot.obsidian_robot_cost[1] and ore >= bot.clay_robot_cost:
                Q.append((
                    ore + ore_robot - bot.clay_robot_cost,
                    clay + clay_robot,
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot + 1,
                    obsidian_robot,
                    geode_robot,
                    time - 1
                ))
            # Build obsidian robot if not at the max
            if obsidian_robot < bot.geode_robot_cost[1] and ore >= bot.obsidian_robot_cost[0] and clay >= bot.obsidian_robot_cost[1]:
                Q.append((
                    ore + ore_robot - bot.obsidian_robot_cost[0],
                    clay + clay_robot - bot.obsidian_robot_cost[1],
                    obsidian + obsidian_robot,
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot + 1,
                    geode_robot,
                    time - 1
                ))
            # Always build geode robot if able
            if ore >= bot.geode_robot_cost[0] and obsidian >= bot.geode_robot_cost[1]:
                Q.append((
                    ore + ore_robot - bot.geode_robot_cost[0],
                    clay + clay_robot,
                    obsidian + obsidian_robot - bot.geode_robot_cost[1],
                    geode + geode_robot,
                    ore_robot,
                    clay_robot,
                    obsidian_robot,
                    geode_robot + 1,
                    time - 1
                ))

        total *= best

    return total


example_input_1 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""
challenge_input = Input('19')

assert(part_1(example_input_1) == 33)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == 3472)
print(f"Part 2: {part_2(challenge_input)}")
