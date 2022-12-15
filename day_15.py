from utils import *


def part_1(p_Input, row=2_000_000):
    sensor_ranges = {
        (a,b): cityblock_distance((a,b),(c,d))
        for a,b,c,d in [parse_ints(x) for x in p_Input.strip().splitlines()]
    }

    xmin= BIG
    xmax=-BIG

    for (x,y),c in sensor_ranges.items():
        xmin = min(xmin, x-(c*2+1-(abs(y-row)*2))//2)
        xmax = max(xmax, x+(c*2+1-(abs(y-row)*2))//2)

    return xmax - xmin


def part_2(p_Input):
    pass


example_input_1 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
challenge_input = Input('15')

assert(part_1(example_input_1, 10) == 26)
print(f"Part 1: {part_1(challenge_input)}")

assert(part_2(example_input_1) == None)
print(f"Part 2: {part_2(challenge_input)}")
