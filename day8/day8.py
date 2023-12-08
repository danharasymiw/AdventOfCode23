import re
from math import lcm


def take_path(pos, dir, maps):
    left_path, right_path = maps[pos]
    if dir == "L":
        return left_path
    return right_path


def navigate(start_pos, end_func, directions, maps):
    dir_num = 0
    while not end_func(start_pos):
        direction = directions[dir_num % len(directions)]
        start_pos = take_path(start_pos, direction, maps)
        dir_num += 1
    return dir_num


def __main__():
    f = open("input.txt")
    lines = f.readlines()
    directions = lines[0].strip()

    maps = {}
    for line in lines[2:]:
        pos, left_path, right_path = re.findall(r"\w+", line)
        maps[pos] = (left_path, right_path)

    # part 1
    answer = navigate("AAA", lambda pos: pos == "ZZZ", directions, maps)
    print(f"Part 1 - Took {answer} steps")

    # part 2
    starting_positions = filter(lambda pos: pos[2] == "A", maps.keys())
    starting_positions = list(starting_positions)
    steps = map(
        lambda pos: navigate(pos, lambda pos: pos[2] == "Z", directions, maps),
        starting_positions,
    )

    print(f"Part 2 - Took {lcm(*steps)} steps")


__main__()
